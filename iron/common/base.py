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
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from aie.utils.hostruntime.tensor_class import Tensor
from . import compilation as comp
from .context import AIEContext
from .device_manager import AIEDeviceManager, pyxrt
from .utils import numpy_to_torch, torch_to_numpy
from .compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    def __init__(self, context=None):
        self.artifacts = comp.CompilationArtifactGraph(
            []
        )  # CompilationArtifact objects are uniqued within the context
        if context is None:
            context = self.get_default_context()
        context.register_operator(self)
        self.context = context

    @abstractmethod
    def set_up_artifacts(self):
        """
        Subclasses should overwrite this method to set up their required dependenices and runtime runlist, kernels and buffers with calls to add_artifacts(), add_kernel(), add_buffer(), and add_to_runlist().
        Note: This method should only *describe* the required artifacts and runtime buffers, and not yet do any computation or compilation.
        Compilation will be handled automatically based on the provided description.
        """
        pass

    @abstractmethod
    def get_arg_spec(self):
        pass

    @abstractmethod
    def get_callable(self):
        pass

    @classmethod
    def get_default_context(cls):
        """One global 'default' context if none is specified"""
        if not hasattr(AIEOperatorBase, "_default_context"):
            AIEOperatorBase._default_context = AIEContext()
        return AIEOperatorBase._default_context

    def compile(self, dry_run=False):
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up(); they may register any artifacts that they need to be compiled there.
        """
        self.set_up_artifacts()
        comp.compile(
            self.context.compilation_rules,
            self.artifacts,
            self.context.build_dir,
            dry_run=dry_run,
        )
        return self

    def add_artifacts(self, artifacts):
        for artifact in artifacts:
            self.artifacts.add(artifact)


def sync_to_device(bos):
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)


def sync_from_device(bos):
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)


def execute_runlist(runlist):
    runlist.execute()
    runlist.wait()


class MLIROperator(AIEOperatorBase, ABC):
    """Base class for AIE-accelerated operations defined by a single MLIR source"""

    def __init__(self, *args, **kwargs):
        self.kernel_archive = f"{self.get_operator_name()}_kernels.a"
        AIEOperatorBase.__init__(self, *args, **kwargs)

    @abstractmethod
    def get_operator_name(self):
        pass

    @abstractmethod
    def get_mlir_artifact(self):
        pass

    @abstractmethod
    def get_kernel_artifacts(self):
        pass

    def get_artifacts(self, prefix=""):
        operator_name = prefix + self.get_operator_name()
        mlir_artifact = self.get_mlir_artifact()
        kernel_deps_inputs = self.get_kernel_artifacts()
        if len(kernel_deps_inputs) > 0:
            # FIXME: currently hard-coding that the design will accept this argument as an input if it uses kernels
            # Also not handling name collisions of kernels with the same name
            mlir_artifact.callback_kwargs["kernel_archive"] = self.kernel_archive
        kernel_deps = (
            [
                KernelArchiveArtifact(
                    self.kernel_archive,
                    dependencies=kernel_deps_inputs,
                )
            ]
            if kernel_deps_inputs
            else []
        )
        xclbin_artifact = XclbinArtifact(
            f"{operator_name}.xclbin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_deps,
        )
        insts_artifact = InstsBinArtifact(
            f"{operator_name}.bin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact],
        )
        return xclbin_artifact, insts_artifact

    def set_up_artifacts(self):
        xclbin_artifact, insts_artifact = self.get_artifacts()
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def get_callable(self):
        return SingleXclbinCallable(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=self.xclbin_artifact.kernel_name,
            insts_bin_path=self.insts_artifact.filename,
            args_spec=self.get_arg_spec(),
        )


class CompositeOperator(AIEOperatorBase, ABC):
    """Base class for composite operators that chain multiple sub-operators"""

    def __init__(self, context=None):
        super().__init__(context)


class AIERuntimeArgSpec:
    def __init__(self, direction, shape, dtype=bfloat16):
        self.shape = shape
        self.dtype = dtype
        assert direction in {"in", "out", "inout"}
        self.direction = direction
    
    def __repr__(self):
        return f"AIERuntimeArgSpec(direction={self.direction}, shape={self.shape}, dtype={self.dtype})"


class AIEBuffer(XRTTensor):
    def __init__(self, shape, dtype=bfloat16, bo=None, device_manager=None):
        self.device_manager = device_manager or AIEDeviceManager()
        self.subviews = []

        if bo is not None:
            Tensor.__init__(self, shape, dtype=dtype, device="cpu")
            self._shape = shape
            self.xrt_device = self.device_manager.device
            self._bo = bo
            ptr = self._bo.map()
            self._data = np.frombuffer(ptr, dtype=self.dtype).reshape(self._shape)
        else:
            super().__init__(shape, dtype=dtype, device="cpu")

    @property
    def bo(self):
        return self._bo

    @property
    def on(self):
        return self.device

    @on.setter
    def on(self, value):
        self.device = value

    def subbuffer(self, length, offset, shape, dtype=None):
        if dtype is None:
            dtype = self.dtype
        assert np.prod(shape) == length
        itemsize = np.dtype(dtype).itemsize
        assert offset >= 0
        assert offset * itemsize <= np.prod(self.shape) * np.dtype(self.dtype).itemsize
        assert (
            length * itemsize + offset * itemsize
            <= np.prod(self.shape) * np.dtype(self.dtype).itemsize
        )
        sub_bo = pyxrt.bo(
            self.bo,  # parent bo
            length * itemsize,  # size
            offset * itemsize,  # offset
        )
        sub_buffer = AIEBuffer(
            shape=shape, dtype=dtype, bo=sub_bo, device_manager=self.device_manager
        )
        sub_buffer.on = self.on
        self.subviews.append(sub_buffer)
        return sub_buffer

    def view(self, shape):
        assert np.prod(shape) == np.prod(self.shape)
        sub_buffer = AIEBuffer(
            shape=shape,
            dtype=self.dtype,
            bo=self.bo,
            device_manager=self.device_manager,
        )
        sub_buffer.on = self.on
        self.subviews.append(sub_buffer)
        return sub_buffer

    def view_as_np(self):
        return self.numpy()

    def view_as_torch(self):
        return numpy_to_torch(self.numpy())

    def to(self, dest):
        super().to(dest)
        todo = self.subviews.copy()
        while todo:
            sub_buffer = todo.pop()
            sub_buffer.device = dest
            todo.extend(sub_buffer.subviews)
        return self

    @staticmethod
    def from_np(buffer):
        aie_buffer = AIEBuffer(buffer.shape, dtype=buffer.dtype)
        aie_buffer.data[:] = buffer
        aie_buffer.to("npu")
        return aie_buffer

    @staticmethod
    def from_torch(tensor):
        return AIEBuffer.from_np(torch_to_numpy(tensor))


class SingleXclbinCallable:
    def __init__(
        self, xclbin_path, kernel_name, insts_bin_path, args_spec, device_manager=None
    ):
        self.device_manager = device_manager or AIEDeviceManager()
        self.context, self.xrt_kernel = self.device_manager.get_context_and_kernel(
            str(xclbin_path), kernel_name
        )
        with open(str(insts_bin_path), "rb") as f:
            instructions = np.frombuffer(f.read(), dtype=np.uint32)
        insts_bo = pyxrt.bo(
            self.device_manager.device,
            instructions.nbytes,
            pyxrt.bo.cacheable,
            self.xrt_kernel.group_id(1),
        )
        insts_bo.write(instructions.view(np.uint8), 0)
        self.insts_buffer = AIEBuffer(
            shape=(len(instructions),), dtype=np.uint32, bo=insts_bo
        )
        self.insts_buffer.to("npu")
        self.args_spec = args_spec

    def __call__(self, *buffers):
        assert len(buffers) == len(self.args_spec)
        # assert all(
        #    np.prod(buffers[i].shape) >= np.prod(self.args_spec[i].shape) and buffers[i].dtype == self.args_spec[i].dtype
        #    for i in range(len(buffers))
        # ), "Input buffer shapes or dtypes do not match expected argument specification."
        self.insts_buffer.to("npu")
        for buf in buffers:
            buf.to("npu")
        opcode = 3
        bos = [buffer.bo for buffer in buffers]
        run = self.xrt_kernel(
            opcode, self.insts_buffer.bo, self.insts_buffer.shape[0], *bos
        )
        ret_code = run.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel did not complete correctly: {ret_code}")


class PatchableSingleXclbinCallable(SingleXclbinCallable):
    def __init__(
        self, xclbin_path, kernel_name, insts_bin_path, args_spec, device_manager=None
    ):
        super().__init__(
            xclbin_path, kernel_name, insts_bin_path, args_spec, device_manager
        )
        self.baseline_instructions = self.insts_buffer.view_as_np().copy()

    def patch(self, patches):
        """Apply patches with masking: dict of {position: (value, mask)}."""
        insts = self.insts_buffer.view_as_np()
        insts[:] = self.baseline_instructions
        for pos, (val, mask) in patches.items():
            insts[pos] = (np.int64(insts[pos]) & ~mask) | (val & mask)
        self.insts_buffer.to("npu")


class CompositeCallable:
    """Callable for executing a sequence of sub-operators"""

    def __init__(self, sequence, intermediate_buffers=None):
        """
        Args:
            sequence: List of (callable, args_indices) tuples.
                      args_indices is a list of indices into the combined list of [inputs, outputs, intermediates].
            intermediate_buffers: List of AIEBuffer objects for intermediate results.
        """
        self.sequence = sequence
        self.intermediate_buffers = intermediate_buffers or []

    def __call__(self, *args):
        # args contains inputs and outputs
        all_buffers = list(args) + self.intermediate_buffers

        for op_callable, indices in self.sequence:
            op_args = [all_buffers[i] for i in indices]
            op_callable(*op_args)
