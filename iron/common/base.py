# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod
from ml_dtypes import bfloat16

from aie.utils.npukernel import NPUKernel
from . import compilation as comp
from .context import AIEContext
from .compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelArchiveArtifact,
)


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    def __init__(self, context=None):
        self.artifacts = comp.CompilationArtifactGraph()
        if context is None:
            context = self.get_default_context()
        context.register_operator(self)
        self.context = context

    @abstractmethod
    def set_up_artifacts(self):
        """
        Declare the artifact dependency graph for this operator.

        Subclasses must implement this method and call add_artifacts() to register
        the artifacts they require. This method should only *describe* dependencies;
        it must not perform any computation or compilation.  Compilation is triggered
        separately via compile().
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
        """Return the process-wide default AIEContext, creating it on first call (lazy singleton)."""
        if not hasattr(AIEOperatorBase, "_default_context"):
            AIEOperatorBase._default_context = AIEContext()
        return AIEOperatorBase._default_context

    def compile(self, dry_run=False):
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up_artifacts(); they may register any
        artifacts that they need to be compiled there.
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


class MLIROperator(AIEOperatorBase, ABC):
    """Base class for AIE-accelerated operations defined by a single MLIR source"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kernel_archive = f"{self.get_operator_name()}_kernels.a"

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
        if kernel_deps_inputs:
            # Inject kernel archive name into the MLIR generation callback so the
            # design function knows which archive to link against.
            mlir_artifact.callback_kwargs["kernel_archive"] = self.kernel_archive
        kernel_deps = (
            [
                KernelArchiveArtifact(
                    self.kernel_archive, dependencies=kernel_deps_inputs
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
        return NPUKernel(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=self.xclbin_artifact.kernel_name,
            insts_path=self.insts_artifact.filename,
        )


class CompositeOperator(AIEOperatorBase, ABC):
    """Base class for composite operators that chain multiple sub-operators"""


class AIERuntimeArgSpec:
    """Specification for a single runtime argument of an AIE operator."""

    def __init__(self, direction, shape, dtype=bfloat16):
        self.shape = shape
        self.dtype = dtype
        if direction not in {"in", "out", "inout"}:
            raise ValueError(
                f"Invalid direction {direction!r}: must be one of 'in', 'out', 'inout'"
            )
        self.direction = direction

    def __repr__(self):
        return f"AIERuntimeArgSpec(direction={self.direction}, shape={self.shape}, dtype={self.dtype})"


class CompositeCallable:
    """Callable for executing a sequence of sub-operators"""

    def __init__(self, sequence, intermediate_buffers=None):
        """
        Args:
            sequence: List of (callable, args_indices) tuples.
                      args_indices is a list of indices into the combined list of [inputs, outputs, intermediates].
            intermediate_buffers: List of XRTTensor objects for intermediate results.
        """
        self.sequence = sequence
        self.intermediate_buffers = (
            intermediate_buffers if intermediate_buffers is not None else []
        )

    def __call__(self, *args):
        """
        Execute the sub-operator sequence.

        Buffer index layout: the combined buffer list is [*args, *intermediate_buffers],
        where args contains the caller-supplied inputs and outputs in declaration order,
        and intermediate_buffers contains any pre-allocated scratch tensors.
        Each (callable, indices) entry in self.sequence selects buffers by position
        from this combined list.
        """
        # args contains inputs and outputs
        all_buffers = list(args) + self.intermediate_buffers

        for op_callable, indices in self.sequence:
            op_args = [all_buffers[i] for i in indices]
            op_callable(*op_args)
