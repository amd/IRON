# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import os
from pathlib import Path
from abc import ABC, abstractmethod
import logging
import time
import torch
from ml_dtypes import bfloat16

import aie.utils.config
from . import compilation as comp
from .aie_context import AIEContext
from .aie_device_manager import AIEDeviceManager, pyxrt
from .utils import numpy_to_torch, torch_to_numpy


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    @classmethod
    def get_default_context(cls):
        """One global 'default' context if none is specified"""
        if not hasattr(AIEOperatorBase, "_default_context"):
            AIEOperatorBase._default_context = AIEContext()
        return AIEOperatorBase._default_context

    def __init__(self, context=None):
        self.artifacts = (
            []
        )  # CompilationArtifact objects are uniqued within the context
        self.kernels = {}  # Name -> (xclbin_path, xclbin_kernel_name, insts_path)
        self.buffers = {}  # Name -> required buffer size in bytes
        self.buffer_static_data = {}
        self.runlist = (
            []
        )  # List of (kernel_name, buffers_name, buffer_name...), will be executed in sequence

        # AIE runtime state
        self.buffer_bos = {}  # Buffer name -> buffer object
        self.xrt_kernels = (
            {}
        )  # Kernel name -> (XRT context, XRT kernel object, instruction buffer object, instruction length)
        self.xrt_runlist = None

        if context is None:
            context = self.get_default_context()
        context.register_operator(self)

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def add_kernel(
        self,
        name: str,
        xclbin_artifact: comp.XclbinArtifact,
        xclbin_kernel_name: str,
        insts_artifact: comp.InstsBinArtifact,
    ):
        assert name not in self.kernels
        self.kernels[name] = (xclbin_artifact, xclbin_kernel_name, insts_artifact)

    def add_buffer(self, name, count, dtype=bfloat16, static_data=None):
        assert name not in self.buffers
        self.buffers[name] = count * np.dtype(dtype).itemsize
        if static_data is not None:
            assert (
                static_data.nbytes <= self.buffers[name]
            ), f"Static data for buffer {name} exceeds allocated size."
            static_data_bytes = static_data.flatten().view(np.uint8).tobytes()
            if static_data_bytes not in self.context.static_data_pool:
                self.context.static_data_pool[static_data_bytes] = None
            self.buffer_static_data[name] = next(
                k
                for k, v in self.context.static_data_pool.items()
                if k == static_data_bytes
            )

    def add_to_runlist(self, kernel_name, *args):
        if kernel_name not in self.kernels:
            raise RuntimeError(f"No such kernel: {kernel_name}")
        for arg in args:
            if arg not in self.buffers:
                raise RuntimeError(f"No such buffer: {arg}")
        self.runlist.append((kernel_name, *args))

    def get_bo(self, buffer_name):
        return self.buffer_bos[buffer_name]

    def read_buffer(self, buffer_name, shape, dtype=bfloat16):
        """Read buffer and return values as a numpy array"""
        size = np.prod(shape) * np.dtype(dtype).itemsize
        output_bytes = self.get_bo(buffer_name).read(size, 0)
        output_data_flat = np.frombuffer(output_bytes, dtype=dtype)
        return output_data_flat.reshape(*shape)

    def read_buffer_as_torch(self, buffer_name, shape, dtype=bfloat16):
        return numpy_to_torch(self.read_buffer(buffer_name, shape, dtype))

    def write_buffer(self, buffer_name, array):
        """Write buffer from a numpy array into a XRT buffer object"""
        if isinstance(array, torch.Tensor):
            numpy_array = torch_to_numpy(array)
        else:
            numpy_array = array
        if buffer_name in self.buffer_static_data:
            raise RuntimeError(f"Cannot write to static buffer: {buffer_name}")
        self.get_bo(buffer_name).write(numpy_array.flatten().view(np.uint8), 0)

    @abstractmethod
    def set_up_artifacts(self):
        """
        Subclasses should overwrite this method to set up their required dependenices and runtime runlist, kernels and buffers with calls to add_artifacts(), add_kernel(), add_buffer(), and add_to_runlist().
        Note: This method should only *describe* the required artifacts and runtime buffers, and not yet do any computation or compilation.
        Compilation will be handled automatically based on the provided description.
        """
        pass

    @abstractmethod
    def set_up_runtime(self):
        pass

    def compile(self, dry_run=None):
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up(); they may register any artifacts that they need to be compiled there.
        """
        context = self.context
        self.set_up_artifacts()
        self._move_artifact_paths()
        work_list = comp.get_work_list(self.artifacts)
        compilation_rules = [
            comp.GenerateMLIRFromPythonCompilationRule(dry_run=dry_run),
            comp.PeanoCompilationRule(
                context.peano_dir, context.mlir_aie_dir, dry_run=dry_run
            ),
            comp.ArchiveCompilationRule(context.peano_dir, dry_run=dry_run),
            comp.AieccCompilationRule(
                context.build_dir,
                context.peano_dir,
                context.mlir_aie_dir,
                dry_run=dry_run,
            ),
        ]
        if work_list:
            logging.info(
                f"Compiling {len(work_list)} new artifacts for AIE operator {self.__class__.__name__}: {', '.join(str(artifact.path.name) for artifact in work_list)}"
            )
        comp.compile(compilation_rules, work_list)

    def add_artifacts(self, artifacts):
        self.artifacts.extend(artifacts)

    def _move_artifact_paths(self):
        """Make all artifacts paths point into the build directory (source artifacts into the ironclad source directory). This doesn't phyisically move files; this function is called before artifact generation."""
        context = self.context
        todo = self.artifacts.copy()
        while todo:
            artifact = todo[0]
            todo.pop(0)
            if isinstance(artifact, comp.SourceArtifact):
                artifact.set_path(context.base_dir / artifact.path)
            else:
                artifact.set_path(context.build_dir / artifact.path)
            todo.extend(artifact.depends)

    def run_runlist(self):
        elapsed = 0.0
        if self.xrt_runlist is None:
            # Execute as separate xclbin kernel invocations
            for i, (kernel_name, *buffer_args) in enumerate(self.runlist):
                context, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kernel_name]
                insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
                bos = [self.buffer_bos[buffer_arg] for buffer_arg in buffer_args]
                for bo in bos:
                    bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
                opcode = 3
                start = time.perf_counter()
                run = xrt_kernel(opcode, insts_bo, insts_len, *bos)
                result = run.wait()
                stop = time.perf_counter()
                elapsed += stop - start
                if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
                    raise RuntimeError(
                        f"Kernel {kernel_name} did not complete correctly: {result}"
                    )
                for bo in bos:
                    bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
        else:
            bos = set(
                self.buffer_bos[buffer_arg]
                for _, *buffer_args in self.runlist
                for buffer_arg in buffer_args
            )
            insts_bos = set(
                self.xrt_kernels[kernel_name][2] for (kernel_name, *_) in self.runlist
            )
            for bo in bos | insts_bos:
                bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
            start = time.perf_counter()
            self.xrt_runlist.execute()
            self.xrt_runlist.wait()
            stop = time.perf_counter()
            for bo in bos:
                bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
            elapsed = stop - start
        return elapsed


class AIEOperatorConstraintError(RuntimeError):
    pass
