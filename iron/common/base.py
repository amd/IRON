# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from abc import ABC, abstractmethod
import dataclasses
from ml_dtypes import bfloat16
from typing import Any, Callable, ClassVar, Dict

import inspect
from pathlib import Path

import numpy as np
from aie.utils.npukernel import NPUKernel
import aie.utils as aie_utils
from . import compilation as comp
from .context import AIEContext
from .utils import float_to_name
from .compilation import (
    CompilationArtifact,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    def __init__(self, context: AIEContext | None = None) -> None:
        self.artifacts = comp.CompilationArtifactGraph()
        if context is None:
            context = self.get_default_context()
        self.context = context

    @abstractmethod
    def set_up_artifacts(self) -> None:
        """
        Declare the artifact dependency graph for this operator.

        Subclasses must implement this method and call add_artifacts() to register
        the artifacts they require. This method should only *describe* dependencies;
        it must not perform any computation or compilation.  Compilation is triggered
        separately via compile().
        """
        pass

    @abstractmethod
    def get_arg_spec(self) -> list[AIERuntimeArgSpec]:
        pass

    @abstractmethod
    def get_callable(self) -> Callable[..., Any]:
        pass

    @classmethod
    def get_default_context(cls) -> AIEContext:
        """Return the process-wide default AIEContext, creating it on first call (lazy singleton)."""
        if not hasattr(AIEOperatorBase, "_default_context"):
            AIEOperatorBase._default_context = AIEContext()
        return AIEOperatorBase._default_context

    def compile(self, dry_run: bool = False) -> AIEOperatorBase:
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up_artifacts(); they may register any
        artifacts that they need to be compiled there.
        """
        if not self.artifacts:
            self.set_up_artifacts()
        comp.compile(
            self.context.compilation_rules,
            self.artifacts,
            self.context.build_dir,
            dry_run=dry_run,
        )
        return self

    def add_artifacts(self, artifacts: list[CompilationArtifact]) -> None:
        for artifact in artifacts:
            self.artifacts.add(artifact)


def _serialize_param(v: object) -> str:
    """Convert a parameter value to a filesystem-safe string for operator names."""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, float):
        return float_to_name(v)
    if isinstance(v, (list, tuple)):
        return "x".join(str(x) for x in v)
    return str(v)


class MLIROperator(AIEOperatorBase):
    """Base class for AIE-accelerated operations defined by a single MLIR source"""

    _name_aliases: ClassVar[Dict[str, str]] = {
        "num_aie_columns": "c",
        "num_channels": "ch",
        "tile_size": "t",
        "size": "sz",
        "scalar_factor": "sf",
        "rows": "r",
        "cols": "n",
    }

    def __init__(self, *args, **kwargs):
        AIEOperatorBase.__init__(self, *args, **kwargs)

    @property
    def operator_dir(self) -> Path:
        return Path(inspect.getfile(type(self))).parent

    @property
    def _params(self) -> dict[str, Any] | None:
        return None

    @property
    def name(self) -> str:
        if dataclasses.is_dataclass(self):
            aliases = type(self)._name_aliases
            parts = (
                f"{aliases.get(f.name, f.name)}{_serialize_param(getattr(self, f.name))}"
                for f in dataclasses.fields(self)
                if f.repr and getattr(self, f.name) is not None
            )
            base = type(self).__name__ + "_" + "_".join(parts)
        elif self._params is not None:
            parts = (
                f"{k}{_serialize_param(v)}"
                for k, v in self._params.items()
                if v is not None
            )
            base = type(self).__name__ + "_" + "_".join(parts)
        else:
            raise NotImplementedError(
                f"{type(self).__name__} must be a @dataclass or define a _params property"
            )
        dev = aie_utils.get_current_device()
        return f"{base}_{dev.resolve().name}"

    @abstractmethod
    def get_mlir_artifact(self) -> CompilationArtifact:
        pass

    @abstractmethod
    def get_kernel_artifacts(self) -> list[CompilationArtifact]:
        pass

    def get_artifacts(
        self, prefix: str = "", dynamic_obj_fifos: bool = False
    ) -> tuple[XclbinArtifact, InstsBinArtifact]:
        operator_name = prefix + self.name
        arch = self.name.rsplit("_", 1)[-1]
        mlir_artifact = self.get_mlir_artifact()
        kernel_deps = self.get_kernel_artifacts()
        for dep in kernel_deps:
            if isinstance(dep, KernelObjectArtifact):
                p = Path(dep.filename)
                dep.filename = str(p.with_stem(f"{p.stem}_{arch}"))
        extra_flags = ["--dynamic-objFifos"] if dynamic_obj_fifos else []
        xclbin_artifact = XclbinArtifact(
            f"{operator_name}.xclbin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_deps,
            extra_flags=extra_flags,
        )
        insts_artifact = InstsBinArtifact(
            f"{operator_name}.bin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact],
            extra_flags=extra_flags,
        )
        return xclbin_artifact, insts_artifact

    def set_up_artifacts(self) -> None:
        xclbin_artifact, insts_artifact = self.get_artifacts()
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def get_callable(self) -> Callable[..., Any]:
        handle: list = [None]  # use list for nonlocal mutation in Python 3

        def call(*args):
            if handle[0] is None:
                # compile() is idempotent: populate_availability_from_filesystem()
                # checks disk and skips already-compiled artifacts
                self.compile()
                npu_kernel = NPUKernel(
                    xclbin_path=self.xclbin_artifact.filename,
                    kernel_name=self.xclbin_artifact.kernel_name,
                    insts_path=self.insts_artifact.filename,
                )
                handle[0] = aie_utils.DefaultNPURuntime.load(npu_kernel)
            return aie_utils.DefaultNPURuntime.run(handle[0], list(args))

        return call


class CompositeOperator(AIEOperatorBase):
    """Base class for composite operators that chain multiple sub-operators"""

    def __init__(self, context: AIEContext | None = None) -> None:
        super().__init__(context)


class AIERuntimeArgSpec:
    """Specification for a single runtime argument of an AIE operator."""

    def __init__(
        self, direction: str, shape: tuple[int, ...], dtype: np.dtype = bfloat16
    ) -> None:
        self.shape = shape
        self.dtype = dtype
        if direction not in {"in", "out", "inout"}:
            raise ValueError(
                f"Invalid direction {direction!r}: must be one of 'in', 'out', 'inout'"
            )
        self.direction = direction

    def __repr__(self) -> str:
        return f"AIERuntimeArgSpec(direction={self.direction}, shape={self.shape}, dtype={self.dtype})"
