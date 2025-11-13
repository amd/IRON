# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import os
from pathlib import Path
from abc import ABC, abstractmethod
import logging
from ml_dtypes import bfloat16

import aie.utils.config
from .. import compilation as comp
from ..aie_device_manager import AIEDeviceManager, pyxrt
from ..utils import numpy_to_torch, torch_to_numpy


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    registered_operators = []

    # Global configuration
    device_manager = AIEDeviceManager()
    llama_dir = Path(__file__).parent.parent.parent
    base_dir = llama_dir.parent.parent  # IRON base dir
    build_dir = llama_dir / "build"
    mlir_aie_dir = Path(aie.utils.config.root_path())
    peano_dir = Path(aie.utils.config.peano_install_dir())

    @classmethod
    def compile_all_operators(cls):
        """Compile all registered AIE operators."""
        cls.build_dir.mkdir(parents=True, exist_ok=True)
        for op in cls.registered_operators:
            op.compile()

    @classmethod
    def prepare_runtime(cls):
        """Setup XRT runtime for AIE execution using shared device manager"""

        # Pools of preallocated buffer objects; each buffer object is allocated
        # once at program start and then reused across operators where possible.
        bo_pools = {}  # size (multiple of page_sz) -> list of XRT buffer objects
        page_sz = 4096
        get_pool_sz = lambda x: (x + page_sz - 1) // page_sz * page_sz

        for op in cls.registered_operators:
            logging.info(f"Preparing runtime for AIE operator: {op.__class__.__name__}")

            for kernel_name, (xclbin, xclbin_kernel_name, insts) in op.kernels.items():
                context, xrt_kernel = cls.device_manager.get_context_and_kernel(
                    str(xclbin.path), xclbin_kernel_name
                )
                with open(str(insts.path), "rb") as f:
                    instructions = np.frombuffer(f.read(), dtype=np.uint32)
                logging.info(
                    f"Allocating instruction buffer for {len(instructions)} instructions."
                )
                insts_bo = pyxrt.bo(
                    cls.device_manager.device,
                    instructions.nbytes,
                    pyxrt.bo.cacheable,
                    xrt_kernel.group_id(1),
                )
                insts_bo.write(instructions.view(np.uint8), 0)
                op.xrt_kernels[kernel_name] = (
                    context,
                    xrt_kernel,
                    insts_bo,
                    len(instructions),
                )

            # If multiple buffers (of the same binned size) are used in the
            # same kernel invocation, they require separate allocations.
            conflicting_buffers = {}  # map buffer -> {set of conflicting buffers}
            for kernel, *args in op.runlist:
                for arg in args:
                    # Conflict only exists if buffers are in the same size pool
                    pool_sz = get_pool_sz(op.buffers[arg])
                    conflicting_args = {
                        a for a in args if get_pool_sz(op.buffers[a]) == pool_sz
                    } - {arg}
                    conflicting_buffers[arg] = conflicting_buffers.get(
                        arg, set()
                    ).union(conflicting_args)

            buffer_allocations = {}  # map buffer -> (key into bo_pools, list index)
            for buffer_name, buffer_min_size in op.buffers.items():
                alloc_pool = get_pool_sz(buffer_min_size)
                alloc_idx = 0
                for conflict in conflicting_buffers.get(buffer_name, set()):
                    if conflict not in buffer_allocations:
                        # Conflicting buffer does not yet have an allocation
                        continue
                    conflict_pool, conflict_idx = buffer_allocations[conflict]
                    alloc_idx = max(alloc_idx, conflict_idx + 1)
                assert 0 <= alloc_idx < len(bo_pools.get(alloc_pool, [])) + 1
                if alloc_idx == len(bo_pools.get(alloc_pool, [])):
                    # 0x10000 == group_id(3) and above, i.e., for all user buffers
                    bo = pyxrt.bo(
                        cls.device_manager.device,
                        alloc_pool,
                        pyxrt.bo.host_only,
                        0x10000,
                    )
                    bo_pools.setdefault(alloc_pool, []).append(bo)
                buffer_allocations[buffer_name] = (alloc_pool, alloc_idx)
                op.buffer_bos[buffer_name] = bo_pools[alloc_pool][alloc_idx]

        bo_count = sum(len(pool) for pool in bo_pools.values())
        bo_footprint = sum(len(pool) * pool_sz for pool_sz, pool in bo_pools.items())
        logging.info(
            f"Allocated {bo_count} total buffer objects with a total memory footprint of {bo_footprint} bytes."
        )

    def __init__(self):
        self.artifacts = (
            []
        )  # CompilationArtifact objects are globally uniqued, so any overlapping elements of this list will be shared with other operators and will be cached.
        self.kernels = {}  # Name -> (xclbin_path, xclbin_kernel_name, insts_path)
        self.buffers = {}  # Name -> required buffer size in bytes
        self.runlist = (
            []
        )  # List of (kernel_name, buffers_name, buffer_name...), will be executed in sequence

        # AIE runtime state
        self.buffer_bos = {}  # Buffer name -> buffer object
        self.xrt_kernels = (
            {}
        )  # Kernel name -> (XRT kernel object, instruction sequence, instruction buffer object, instruction length)

        self.registered_operators.append(self)

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

    def add_buffer(self, name, count, dtype=bfloat16):
        assert name not in self.buffers
        self.buffers[name] = count * np.dtype(dtype).itemsize

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

    def write_buffer(self, buffer_name, numpy_array):
        """Write buffer from a numpy array into a XRT buffer object"""
        self.get_bo(buffer_name).write(numpy_array.flatten().view(np.uint8), 0)

    @abstractmethod
    def set_up(self):
        """
        Subclasses should overwrite this method to set up their required dependenices and runtime runlist, kernels and buffers with calls to add_artifacts(), add_kernel(), add_buffer(), and add_to_runlist().
        Note: This method should only *describe* the required artifacts and runtime buffers, and not yet do any computation or compilation.
        Compilation will be handled automatically based on the provided description.
        """
        pass

    def compile(self):
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up(); they may register any artifacts that they need to be compiled there.
        """
        self.set_up()
        self._move_artifact_paths()
        work_list = comp.get_work_list(self.artifacts)
        compilation_rules = [
            comp.GenerateMLIRFromPythonCompilationRule(),
            comp.PeanoCompilationRule(self.peano_dir, self.mlir_aie_dir),
            comp.ArchiveCompilationRule(self.peano_dir),
            comp.AieccCompilationRule(
                self.build_dir, self.peano_dir, self.mlir_aie_dir
            ),
        ]
        logging.info(
            f"Compiling AIE operator {self.__class__.__name__} with {len(work_list)} artifacts: {', '.join(str(artifact.path.name) for artifact in work_list)}"
        )
        comp.compile(compilation_rules, work_list)

    def add_artifacts(self, artifacts):
        self.artifacts.extend(artifacts)

    def _move_artifact_paths(self):
        """Make all artifacts paths point into the build directory (source artifacts into the ironclad source directory). This doesn't phyisically move files; this function is called before artifact generation."""
        todo = self.artifacts.copy()
        while todo:
            artifact = todo[0]
            todo.pop(0)
            if isinstance(artifact, comp.SourceArtifact):
                artifact.set_path(self.base_dir / artifact.path)
            else:
                artifact.set_path(self.build_dir / artifact.path)
            todo.extend(artifact.depends)

    def run_runlist(self):
        for i, (kernel_name, *buffer_args) in enumerate(self.runlist):
            context, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kernel_name]
            insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
            bos = [self.buffer_bos[buffer_arg] for buffer_arg in buffer_args]
            for bo in bos:
                bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
            opcode = 3
            run = xrt_kernel(opcode, insts_bo, insts_len, *bos)
            result = run.wait()
            if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
                raise RuntimeError(
                    f"Kernel {kernel_name} did not complete correctly: {result}"
                )
            for bo in bos:
                bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)


class AIEOperatorConstraintError(RuntimeError):
    pass
