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
from aie.utils.npukernel import NPUKernel

from . import compilation as comp
from .context import AIEContext
from .utils import float_to_name
from .compilation import (
    CompilationArtifact,
    KernelObjectArtifact,
    SourceArtifact,
)


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    _default_context: ClassVar[AIEContext | None] = None

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

    def bind(self, fn: Callable, skip: Any = ()) -> dict[str, Any]:
        """Collect ``fn``'s parameters from this operator's own attributes.

        ``skip`` names parameters the caller supplies itself; they are neither
        bound nor reported missing, so an explicit value can stand in for an
        attribute the operator does not have.

        Matching is by name and nothing else: a parameter is filled from the
        attribute of the same name, whether that is a dataclass field or a
        property. A parameter with no matching attribute and no default is an
        error *here*, naming both sides -- rather than a TypeError from deep
        inside a design, or worse, a silently defaulted value.

        This replaces the hand-written kwargs dict each operator used to keep,
        which restated every field's name a second time and drifted from the
        signature it was feeding with nothing to catch it.
        """
        bound = {}
        missing = []
        for name, parameter in inspect.signature(fn).parameters.items():
            if parameter.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ):
                continue
            if name in skip:
                continue
            if hasattr(self, name):
                bound[name] = getattr(self, name)
            elif parameter.default is inspect.Parameter.empty:
                missing.append(name)
        if missing:
            raise TypeError(
                f"{type(self).__name__} cannot supply {sorted(missing)} to "
                f"{getattr(fn, '__qualname__', fn)}: no attribute of that name. "
                f"Rename the parameter to match a field, or give it a default."
            )
        return bound

    def get_arg_spec(self) -> list[AIERuntimeArgSpec]:
        """Return this operator's runtime argument specification.

        Derived from the ``arg_spec`` shape function the operator declares,
        with its parameters bound from the operator's own fields. Operators
        whose spec is not a pure function of their fields override this
        instead.
        """
        arg_spec = getattr(type(self), "arg_spec", None)
        if arg_spec is None:
            raise NotImplementedError(
                f"{type(self).__name__} declares neither an arg_spec() shape "
                f"function nor a get_arg_spec() override."
            )
        return arg_spec(**self.bind(arg_spec))

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

    # Parameters every design takes but no operator stores. Exposing them as
    # attributes is what lets bind() fill a design's signature whole, instead
    # of each operator keeping a dict to splice them in by hand.

    @property
    def dev(self):
        """The device a design is generated for."""
        return aie_utils.get_current_device()

    @property
    def kernels_dir(self):
        """Where a design finds the C++ its kernels are compiled from.

        Taken from the context rather than resolved in the design, so that
        IRON_AIE_KERNELS_DIR still redirects it -- and so that pointing IRON at
        a different kernel tree changes the compile cache key, which it should.
        """
        return self.context.kernels_dir

    # Bytes of trace buffer to emit; 0 disables tracing, which is what every
    # hand-written kwargs dict passed. Deliberately a plain class attribute
    # rather than a property: OperatorSequence and LayerNorm both assign
    # self.trace_size, and a property without a setter cannot be shadowed by
    # an instance attribute -- it raises instead. Left unannotated so that
    # dataclass subclasses do not pick it up as a field.
    trace_size = 0

    @property
    def verbose(self) -> bool:
        """Whether a design should log while generating.

        Read off the context, which is where the setting already lived; every
        operator that passed this spelled it ``mlir_verbose`` by hand.
        """
        return getattr(self.context, "mlir_verbose", False)


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

    def set_up_artifacts(self) -> None:
        # Kernel objects still go through the artifact-graph rules (Peano/chess
        # compile isn't on CompilableDesign yet -- its own kernel auto-compile
        # only triggers for upstream's ExternalFunction, which no IRON design
        # uses). The xclbin/insts pair is no longer an artifact: link_xclbin()
        # builds it lazily, through CompilableDesign, the first time
        # get_callable() needs it. Kept on self so link_xclbin() can read
        # their resolved (post move_artifacts()) paths later.
        self._kernel_artifacts = self.get_kernel_artifacts()
        self.add_artifacts(self._kernel_artifacts)

    def compile(self, dry_run: bool = False) -> AIEOperatorBase:
        """Build the artifact graph, then the xclbin+insts.

        link_xclbin() is lazy for get_callable()'s benefit, but compile() is an
        explicit request to compile and has to honour it. Once the xclbin/insts
        pair stopped being artifacts, the base implementation alone built only
        kernel objects -- so for a design with no C++ kernel it built nothing at
        all, and compile() returned success for configurations whose MLIR cannot
        even be generated. Errors that belong to compile() surfaced from
        get_callable() instead, or not at all.
        """
        super().compile(dry_run=dry_run)
        if not dry_run:
            self.link_xclbin()
        return self

    def link_xclbin(self) -> None:
        """Compile this operator's xclbin+insts through CompilableDesign, once.

        Idempotent, mirroring FusedDispatch.link_elf /
        SeparateDispatch.link_xclbins. compile() drives it, and get_callable()
        also calls it so an operator that was never explicitly compiled still
        works.
        """
        if getattr(self, "_xclbin_path", None) is not None:
            return
        from .jit_compile import compile_xclbin_insts

        object_files = [Path(a.filename) for a in self._kernel_artifacts]
        self._xclbin_path, self._insts_path = compile_xclbin_insts(
            self.get_mlir_artifact().generator,
            object_files,
            Path(self.context.build_dir) / f"{self.name}.xclbin",
            Path(self.context.build_dir) / f"{self.name}.bin",
            # XclbinArtifact's own former default; no caller ever overrode it.
            kernel_name="MLIR_AIE",
        )

    def get_callable(self) -> Callable[..., Any]:
        self.link_xclbin()
        npu_kernel = NPUKernel(
            xclbin_path=str(self._xclbin_path),
            kernel_name="MLIR_AIE",
            insts_path=str(self._insts_path),
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call


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

    @property
    def reads(self) -> bool:
        """Whether the step consumes this buffer.

        Asking the question directly, rather than comparing ``direction``
        against a set at each call site, is what lets ``"inout"`` answer yes to
        both this and :attr:`writes` -- which is the case a liveness analysis
        gets wrong if it partitions arguments into inputs and outputs.
        """
        return self.direction in {"in", "inout"}

    @property
    def writes(self) -> bool:
        """Whether the step produces this buffer."""
        return self.direction in {"out", "inout"}

    def nbytes(self) -> int:
        """Size of this argument in bytes."""
        return int(np.prod(self.shape) * np.dtype(self.dtype).itemsize)


def same_shape_unary(size, dtype=bfloat16):
    """One input and one output of identical shape.

    Shared by every elementwise activation and by the operators that move or
    relayout a buffer without resizing it. Those two groups have nothing in
    common in their *designs* -- a ReLU and a transpose generate very different
    MLIR -- which is exactly why this is a function rather than a base class:
    an operator can reuse the shape rule without inheriting a design it does
    not want.
    """
    shape = (size,) if isinstance(size, int) else tuple(size)
    return [
        AIERuntimeArgSpec("in", shape, dtype=dtype),
        AIERuntimeArgSpec("out", shape, dtype=dtype),
    ]


def same_shape_binary(size, dtype=bfloat16):
    """Two inputs and one output, all of identical shape."""
    shape = (size,) if isinstance(size, int) else tuple(size)
    return [
        AIERuntimeArgSpec("in", shape, dtype=dtype),
        AIERuntimeArgSpec("in", shape, dtype=dtype),
        AIERuntimeArgSpec("out", shape, dtype=dtype),
    ]
