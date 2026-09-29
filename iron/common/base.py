# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import dataclasses
import inspect
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, ClassVar

import numpy as np
from ml_dtypes import bfloat16
import aie.utils as aie_utils
from aie.utils.compile.utils import SHARED_LIB_SUFFIX
from aie.utils.npukernel import NPUKernel
from aie.utils.verify import Tolerance

from . import compilation as comp
from .context import AIEContext
from .device_utils import pin_current_device
from .utils import float_to_name
from .compilation import (
    CompilationArtifact,
    XclbinArtifact,
    InstsBinArtifact,
    DispatchLibArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
)


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    _default_context: ClassVar[AIEContext | None] = None

    def __init__(self, context: AIEContext | None = None) -> None:
        self.artifacts = comp.CompilationArtifactGraph()
        pin_current_device()
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
        if AIEOperatorBase._default_context is None:
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

    _name_aliases: ClassVar[dict[str, str]] = {
        "num_aie_columns": "c",
        "num_channels": "ch",
        "tile_size": "t",
        "size": "sz",
        "scalar_factor": "sf",
        "rows": "r",
        "cols": "n",
    }

    @property
    def operator_dir(self) -> Path:
        return Path(inspect.getfile(type(self))).parent

    def design_key(self) -> str | None:
        """Identifies the design this operator compiles to, for sharing it.

        Two operators returning the same key must produce byte-identical MLIR before
        the fused build prefixes their kernel symbols, and must take the same runtime
        argument shapes. ``None`` means the design is never shared.
        """
        return None

    @property
    def name(self) -> str:
        """Unique name for this operator instance, derived from its parameters.

        For @dataclass subclasses the name is automatically constructed from the
        dataclass fields using ``_name_aliases`` to shorten field names.
        Non-dataclass subclasses must override this property directly.
        """
        if dataclasses.is_dataclass(self):
            aliases = type(self)._name_aliases
            parts = (
                f"{aliases.get(f.name, f.name)}{_serialize_param(getattr(self, f.name))}"
                for f in dataclasses.fields(self)
                if f.repr and getattr(self, f.name) is not None
            )
            base = type(self).__name__ + "_" + "_".join(parts)
        else:
            raise NotImplementedError(
                f"{type(self).__name__} must be a @dataclass or override the name property"
            )
        dev = aie_utils.get_current_device()
        return f"{base}_{dev.resolve().name}"

    @abstractmethod
    def get_mlir_artifact(self) -> CompilationArtifact:
        pass

    @abstractmethod
    def get_kernel_artifacts(self) -> list[CompilationArtifact]:
        pass

    def reference_tolerance(self) -> Tolerance | None:
        """How close the NPU output must come to ``reference()``.

        This is the declared contract of the one kernel the operator runs, its
        ``_kernel()``. ``None`` when it runs several kernels or none (a
        ``_kernel()`` that returns ``None``), or when that kernel declares no
        tolerance.
        """
        kernel = getattr(self, "_kernel", lambda: None)()
        if kernel is None or kernel.contract is None:
            return None
        return kernel.contract.tolerance

    def get_dispatch_params(self) -> dict[str, type]:
        """The scalars the runtime sequence takes, by name, in argument order.

        Each value is the NumPy scalar type the sequence declares, e.g.
        ``np.int32``. Scalars can set loop bounds and DMA sizes, so an operator
        that declares them has no single instruction stream. It builds a
        library that generates the stream in place of a ``.bin``, and its
        callable is a :class:`DispatchCallable`.
        """
        return {}

    def get_artifacts(
        self, prefix: str = ""
    ) -> tuple[XclbinArtifact, InstsBinArtifact]:
        if self.get_dispatch_params():
            raise NotImplementedError(
                f"{type(self).__name__} generates its instruction stream per "
                "dispatch and has no .bin to sequence"
            )
        return self._artifacts(prefix)

    def _artifacts(
        self, prefix: str = ""
    ) -> tuple[XclbinArtifact, InstsBinArtifact | DispatchLibArtifact]:
        """The xclbin, and the ``.bin`` or the library that generates the stream."""
        operator_name = prefix + self.name
        mlir_artifact = self.get_mlir_artifact()
        kernel_deps = self.get_kernel_artifacts()
        xclbin_artifact = XclbinArtifact(
            f"{operator_name}.xclbin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_deps,
        )
        dispatch_params = self.get_dispatch_params()
        if not dispatch_params:
            return xclbin_artifact, InstsBinArtifact(
                f"{operator_name}.bin",
                mlir_input=mlir_artifact,
                dependencies=[mlir_artifact],
            )
        return xclbin_artifact, DispatchLibArtifact(
            f"{operator_name}{SHARED_LIB_SUFFIX}",
            mlir_input=mlir_artifact,
            # aiecc compiles the cores on the way to the sequence.
            dependencies=[mlir_artifact] + kernel_deps,
            dispatch_params=dispatch_params,
        )

    def set_up_artifacts(self) -> None:
        self.xclbin_artifact, stream_artifact = self._artifacts()
        if isinstance(stream_artifact, DispatchLibArtifact):
            self.dispatch_artifact = stream_artifact
        else:
            self.insts_artifact = stream_artifact
        self.add_artifacts([self.xclbin_artifact, stream_artifact])

    def get_callable(self) -> Callable[..., Any]:
        dispatch_params = self.get_dispatch_params()
        if dispatch_params:
            return DispatchCallable(
                NPUKernel(
                    xclbin_path=self.xclbin_artifact.filename,
                    kernel_name=self.xclbin_artifact.kernel_name,
                    dispatch_params=list(dispatch_params),
                    dispatch_lib_path=Path(self.dispatch_artifact.filename).resolve(),
                )
            )
        npu_kernel = NPUKernel(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=self.xclbin_artifact.kernel_name,
            insts_path=self.insts_artifact.filename,
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call


class DispatchCallable:
    """Runs an operator whose instruction stream depends on dispatch parameters.

    ``set_parameters()`` sets the parameters of every later call. Each call
    generates the instruction stream for those parameters and runs it.
    """

    def __init__(self, npu_kernel: NPUKernel) -> None:
        self._npu_kernel = npu_kernel
        self._params: dict[str, int] | None = None

    def set_parameters(self, **params: int) -> None:
        expected = self._npu_kernel.dispatch_params
        if sorted(params) != sorted(expected):
            raise TypeError(
                f"set_parameters() takes exactly {expected}, got {sorted(params)}"
            )
        self._params = params

    def __call__(self, *args):
        if self._params is None:
            raise RuntimeError(
                "call set_parameters() before the first call: the instruction "
                "stream depends on them"
            )
        _, result = self._npu_kernel(*args, **self._params)
        return result


class CompositeOperator(AIEOperatorBase):
    """Base class for composite operators that chain multiple sub-operators"""

    def __init__(self, context: AIEContext | None = None) -> None:
        super().__init__(context)


@dataclass(frozen=True)
class AIERuntimeArgSpec:
    """Specification for a single runtime argument of an AIE operator."""

    direction: str
    shape: tuple[int, ...]
    dtype: np.dtype = dataclasses.field(default_factory=lambda: bfloat16)

    def __post_init__(self) -> None:
        if self.direction not in {"in", "out", "inout"}:
            raise ValueError(
                f"Invalid direction {self.direction!r}: must be one of 'in', 'out', 'inout'"
            )
