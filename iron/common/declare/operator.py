# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The buffer-sizing half of a declaration.

An operator is declared against one overlay and adds the extents that size
the host buffers. Changing an extent re-issues the runtime sequence; it does
not rebuild the array, which is why the two layers are separate classes.
Calling one binds it: :meth:`Operator.infer` turns operand shapes into the
extents, and the instance's buffer attributes answer in elements.
"""

from __future__ import annotations

import dataclasses
from abc import ABCMeta
from dataclasses import MISSING
from typing import Any, Callable, ClassVar, Generic, TypeVar

import numpy as np
from ml_dtypes import bfloat16

from .bound import BoundBuffer, BoundValue
from .field import DimRef, dim, _Optional, _Select
from .member import In, Out, _Buffer, _Member, _Value
from .naming import label_parts
from .overlay import Overlay

O = TypeVar("O", bound=Overlay)


class _OperatorMeta(ABCMeta):
    """``GEMV(w, h)`` inside a graph function records a step; anything else constructs.

    The class tells the two apart by whether it received graph handles (or
    host tensors, which a graph closes over as weights); see
    :mod:`iron.common.graph`. Outside a graph the call constructs as usual.
    """

    def __call__(cls, *args, **kwargs):
        from .. import graph as _graph

        tracer = _graph.current()
        if tracer is not None and args and all(_graph.is_operand(a) for a in args):
            return tracer.call(cls, args, kwargs)
        return super().__call__(*args, **kwargs)


@dataclasses.dataclass(eq=False, repr=True)


class Operator(Generic[O], metaclass=_OperatorMeta):
    """A host ABI declared against an overlay. Subclass, decorate with ``@operator``.

    Declare ``dim()`` fields and buffers (``In``/``Out``/``InOut`` naming their
    streams) in the class body. Implement :meth:`reference`; optionally
    :meth:`compatible` and :meth:`design` (an override for a sequence the
    library cannot derive).
    """

    ov: O

    _members: ClassVar[tuple[_Member, ...]] = ()
    _dim_fields: ClassVar[tuple[str, ...]] = ()
    _tunable_fields: ClassVar[tuple[str, ...]] = ()
    _overlay_class: ClassVar[type | None] = None

    def __post_init__(self) -> None:
        if self._overlay_class is not None and not isinstance(
            self.ov, self._overlay_class
        ):
            raise TypeError(
                f"{type(self).__name__} is declared against {self._overlay_class.__name__}, "
                f"got {type(self.ov).__name__}"
            )
        self.validate()
        self._bind()

    # -- declared surface --------------------------------------------------

    def validate(self) -> None:
        """Check the sequence-tier fields on their own. Runs at construction."""

    def compatible(self) -> None:
        """Check the extents against the tuned overlay; raise :class:`Incompatible`."""

    def reference(self, *inputs):
        raise NotImplementedError(
            f"{type(self).__name__}.reference() is not implemented"
        )

    def design(self, rt) -> None:
        """Override to write the runtime sequence by hand; otherwise it is derived.

        ``rt`` is an :class:`iron.common.build.Sequence`: ``rt.fill(stream,
        view)``, ``rt.drain(stream, view)``, ``rt.group()``. The preamble
        (residents, barriers, parameter sync) has already run.
        """
        raise NotImplementedError

    def residents(self) -> dict[str, int]:
        """Values for the overlay's residents (trip counts, RTPs), from the extents."""
        return {}

    @classmethod
    def has_design_override(cls) -> bool:
        return cls.design is not Operator.design

    # -- library surface ---------------------------------------------------

    @classmethod
    def overlay_defaults(cls, kwargs: dict) -> None:
        """Fill, in place, overlay tunables this operator's own extent decides.

        An overlay is tuned from the device alone, so a tunable whose right
        value follows from the operator's shape (a copy's transfer size from
        its sizes) is defaulted here, at construction, when it was not
        given. The default fills nothing.
        """

    @classmethod
    def _split_kwargs(cls, kwargs: dict) -> tuple["Overlay", dict]:
        """Split keyword arguments into the overlay's and the operator's own."""
        overlay_cls = cls._overlay_class
        assert overlay_cls is not None
        cls.overlay_defaults(kwargs)
        names = {f.name for f in dataclasses.fields(overlay_cls) if f.init}
        ov_kwargs = {k: kwargs.pop(k) for k in list(kwargs) if k in names}
        return overlay_cls(**ov_kwargs), kwargs

    def value_symbol(self, value: "BoundValue") -> str | None:
        """An explicit device symbol for a per-call value, or ``None`` for the default."""
        return None

    def design_key(self):
        """Identity for sharing a build: the class, the overlay's key, every compared field.

        Two operators with equal keys generate byte-identical MLIR, so a
        sequence builds, prefixes and configures the design once.
        """
        return (
            type(self).__qualname__,
            self.ov.design_key(),
            tuple(
                (f.name, getattr(self, f.name))
                for f in dataclasses.fields(self)
                if f.compare and f.name != "ov"
            ),
        )

    def tuned(self, dev) -> "Operator":
        """A copy bound to its own tuned copy of the overlay, with :meth:`compatible` checked."""
        ov = self.ov.tuned(dev).copy()
        new = dataclasses.replace(self, ov=ov)
        # What a graph bound on this instance is part of it, not of a field:
        # the build works on the copy, and a copy that forgot would silently
        # drop the per-call value from the sequence.
        if self.used_values:
            new.__dict__["_used_values"] = set(self.used_values)
        new.compatible()
        return new

    @property
    def buffers(self) -> list[BoundBuffer]:
        return [self._bound[m.name] for m in self._members if isinstance(m, _Buffer)]

    @property
    def inputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction in ("in", "inout")]

    @property
    def outputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction in ("out", "inout")]

    @property
    def values(self) -> list[BoundValue]:
        """The per-call values this instance uses (see :meth:`uses_value`)."""
        return [
            self._bound[m.name]
            for m in self._members
            if isinstance(m, _Value) and self.uses_value(m.name)
        ]

    def uses_value(self, name: str) -> bool:
        """Whether this instance drives the declared per-call value ``name``.

        A value an instance does not use gets no device parameter and no
        sync. The default is every declared value; an operator whose values
        are optional (a strided copy with or without a patched offset)
        overrides this, and a graph binding one calls :meth:`use_value`.
        """
        return True

    def use_value(self, name: str) -> None:
        """Record that a graph binds the per-call value ``name`` on this instance."""
        if not any(isinstance(m, _Value) and m.name == name for m in self._members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        self.__dict__.setdefault("_used_values", set()).add(name)

    @property
    def used_values(self) -> frozenset:
        return frozenset(self.__dict__.get("_used_values", ()))

    # -- graph functions ---------------------------------------------------

    @classmethod
    def resolve_class(cls, n_operands: int, kwargs: dict) -> type:
        """The class a graph call with ``n_operands`` operands constructs.

        The default is the class itself; a family that picks a subclass from
        its arguments (RMSNorm with a weight) overrides.
        """
        return cls

    def __call__(self, *args, **kwargs):
        """An explicit instance applied to graph handles records a step."""
        from .. import graph as _graph

        tracer = _graph.current()
        if tracer is None:
            raise TypeError(
                f"{type(self).__name__} instances are called on graph handles inside "
                f"an @iron.graph function; outside one, compile() and get_callable()"
            )
        return tracer.call(self, args, kwargs)

    def _bind(self) -> None:
        bound: dict[str, Any] = {}
        for m in self._members:
            if isinstance(m, _Buffer):
                bound[m.name] = BoundBuffer(m, self)
            elif isinstance(m, _Value):
                bound[m.name] = BoundValue(m, self)
        self._bound = bound

    # -- inference ---------------------------------------------------------

    @classmethod
    def from_spec(
        cls,
        name: str,
        *,
        inputs: dict[str, tuple[int, ...]],
        outputs: dict[str, tuple[int, ...]],
        dtype: Any = bfloat16,
        key: str = "",
        params: dict[str, Any] | None = None,
        generator: Callable | None = None,
    ) -> type:
        """An operator class from an exported description, at run time.

        The dynamic escape for a design whose shapes come from a file rather
        than a formula (swiglu_prefill_stream's stream-dse export). ``inputs``
        and ``outputs`` are literal shapes in argument order; ``params`` are
        the numbers that identify the instance (they become ``dim()`` fields
        with those defaults and reach the name); ``key`` identifies the
        generated design, for sharing; ``generator`` replaces
        :meth:`generator`, since the sequence is not derived. The
        overlay is a stand-in carrying only ``key``.
        """
        import types

        from .decorator import operator  # a class made at run time still checks

        def overlay_ns(ns):
            ns["__module__"] = cls.__module__
            ns["__annotations__"] = {"key": str}
            ns["key"] = dim(key, repr=False)

        overlay_cls = operator(
            types.new_class(f"{name}Overlay", (Overlay,), {}, overlay_ns)
        )

        def operator_ns(ns):
            ns["__module__"] = cls.__module__
            ns["__annotations__"] = {}
            for pname, value in (params or {}).items():
                ns["__annotations__"][pname] = type(value)
                ns[pname] = dim(value)
            for bname, shape in inputs.items():
                ns[bname] = In(*shape, dtype=dtype)
            for bname, shape in outputs.items():
                ns[bname] = Out(*shape, dtype=dtype)
            ns["design_key"] = lambda self: self.ov.key or None
            if generator is not None:
                ns["generator"] = generator

        return operator(
            types.new_class(name, (cls[overlay_cls],), {}, operator_ns)  # type: ignore[index]
        )

    @classmethod
    def infer(cls, *operand_shapes, outputs=(), **given) -> dict[str, Any]:
        """Bind dimension fields from operand shapes, in ``In`` declaration order.

        A lookup, not a solver: each declared dimension is a field or a
        literal. Returns ``{field: value}`` for both the operator's and the
        overlay's fields; ``given`` pins values and is checked for agreement.
        ``outputs`` are the shapes of caller-supplied ``Out`` buffers, in
        declaration order, which bind the same way.
        """
        ins = [
            m
            for m in cls._members
            if isinstance(m, _Buffer) and m.direction in ("in", "inout")
        ]
        if len(operand_shapes) != len(ins):
            raise TypeError(
                f"{cls.__name__} takes {len(ins)} operand(s) "
                f"({', '.join(m.name for m in ins)}), got {len(operand_shapes)}"
            )
        outs = [
            m for m in cls._members if isinstance(m, _Buffer) and m.direction == "out"
        ]
        if outputs and len(outputs) != len(outs):
            raise TypeError(
                f"{cls.__name__} produces {len(outs)} output(s) "
                f"({', '.join(m.name for m in outs)}), got {len(outputs)}"
            )
        pairs = list(zip(ins, operand_shapes)) + list(zip(outs, outputs))
        bound: dict[str, Any] = dict(given)
        origin: dict[str, str] = {k: "given" for k in given}

        def bind(ref: DimRef, value: int, where: str) -> None:
            key = ref.name
            if key in bound and bound[key] != value:
                raise ValueError(
                    f"{cls.__name__}: {ref!r} is {value} from {where} but "
                    f"{bound[key]} from {origin[key]}"
                )
            bound[key] = value
            origin.setdefault(key, where)

        for m, shape in pairs:
            shape = tuple(int(s) for s in shape)
            dims = list(m.dims)
            leading = dims[0] if dims and isinstance(dims[0], _Optional) else None
            if leading is not None:
                if len(shape) == len(dims):
                    bind(leading.ref, shape[0], f"{m.name}.shape[0]")
                    shape = shape[1:]
                elif len(shape) == len(dims) - 1:
                    bind(leading.ref, 1, f"{m.name} (rank {len(shape)})")
                else:
                    raise ValueError(
                        f"{cls.__name__}: operand {m.name} has rank {len(shape)}, "
                        f"declared {m!r}"
                    )
                dims = dims[1:]
            expanded: list = []
            for d in dims:
                if isinstance(d, _Select):
                    flag = d.flag
                    if flag.name in bound:
                        value = bound[flag.name]
                    else:
                        fld = next(
                            (
                                f
                                for f in dataclasses.fields(flag.owner)
                                if f.name == flag.name
                            ),
                            None,
                        )
                        if fld is None or fld.default is MISSING:
                            raise ValueError(
                                f"{cls.__name__}: {flag!r} selects {m.name}'s shape and "
                                f"has no default; pass it explicitly"
                            )
                        value = fld.default
                    expanded.extend(d.when_true if value else d.when_false)
                else:
                    expanded.append(d)
            dims = expanded
            if len(dims) == 1 and len(shape) != 1:
                # A flat buffer takes an operand of any rank: its one
                # dimension is the element count.
                shape = (int(np.prod(shape)) if shape else 1,)
            if len(shape) != len(dims):
                raise ValueError(
                    f"{cls.__name__}: operand {m.name} has rank {len(shape)} {shape}, "
                    f"declared rank {len(dims)} {m!r}"
                )
            for i, (d, n) in enumerate(zip(dims, shape)):
                if isinstance(d, DimRef):
                    bind(d, n, f"{m.name}.shape[{i}]")
                elif int(d) != n:
                    raise ValueError(
                        f"{cls.__name__}: operand {m.name}.shape[{i}] is {n}, declared {d}"
                    )
        return bound

    @classmethod
    def infer_kwargs(cls, kwargs) -> dict[str, Any]:
        """The part of ``kwargs`` that :meth:`infer` takes: both layers' dimension
        fields and the flags that select a buffer's shape."""
        names = set(cls._dim_fields)
        if cls._overlay_class:
            names.update(cls._overlay_class._dim_fields)
        for m in cls._members:
            if isinstance(m, _Buffer):
                names.update(d.flag.name for d in m.dims if isinstance(d, _Select))
        return {k: v for k, v in kwargs.items() if k in names}

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> "Operator":
        """Construct an operator (and its overlay) from operand shapes."""
        values = cls.infer(*operand_shapes, **cls.infer_kwargs(overrides))
        kwargs = {**overrides, **values}
        return cls(**kwargs)  # classic-construction path splits overlay fields

    # -- the image of one operator on its own -------------------------------

    @property
    def dev(self):
        """The device a design is generated for."""
        import aie.utils as aie_utils

        return aie_utils.get_current_device()

    # Bytes of trace buffer to emit; 0 disables tracing. A plain attribute
    # rather than a property: OperatorSequence and LayerNorm assign it.
    trace_size = 0

    @property
    def name(self) -> str:
        """This instance's label: the class, every shown field of both layers,
        the device. It names the per-call value symbols a host writes through
        and the kernel instances a chained image carries; nothing on disk,
        which the compile cache keys by content."""
        import aie.utils as aie_utils

        own = label_parts(self, skip=("ov",))
        base = type(self).__name__ + "_" + "_".join(own + self.ov.name_parts())
        dev = aie_utils.get_current_device()
        return f"{base}_{dev.resolve().name}"

    def generator(self, image: str = "elf"):
        """The design generator :class:`CompilableDesign` runs for this operator."""
        from ..build import generator_for

        return generator_for(self, image=image)

    def compile(self, record: str = "memory") -> "Operator":
        """Build this operator's own image, once; sets :attr:`artifacts`.

        ``record="disk"`` also writes the :class:`~iron.common.artifacts.Artifacts`
        record beside the image; by default it is only kept in memory.
        """
        if getattr(self, "_artifacts", None) is None:
            self._artifacts = self._build()
            if record == "disk":
                self._artifacts.dump()
        return self

    @property
    def artifacts(self):
        """The record of what :meth:`compile` produced (None before)."""
        return getattr(self, "_artifacts", None)

    def _members_io(self):
        """The declared buffers, without resolving a shape: their names alone."""
        return [m for m in self._members if isinstance(m, _Buffer)]

    def buffer_map(self) -> dict[str, tuple[str, int, int]]:
        """Each buffer as ``(arena, position, nbytes)``, for an image's record.

        From the tuned operator: a shape may follow a tunable the device
        fills (flm/gemm's B layout), and the built image's buffers are the
        tuned ones. A standalone operator has no arena plan -- its buffers
        are the kernel's positional arguments.
        """
        tuned = self.ov._tuned and self or self.tuned(self.dev)
        return {b.name: ("arg", i, b.nbytes) for i, b in enumerate(tuned.buffers)}

    def _build(self):
        """Compile to an xclbin and an instruction stream, or, on an external
        overlay, to the stream alone against the downloaded image."""
        from ..artifacts import Artifacts, Design, Step
        from ..jit_compile import insts_design, xclbin_design

        image = self.ov.external
        if image is None:
            design = xclbin_design(self.generator(), kernel_name="MLIR_AIE")
            entry = design.get_cache_entry()
            picture, insts = entry.xclbin, entry.insts
        else:
            picture = self.ov.prebuilt()
            design = insts_design(self.generator())
            entry = design.get_cache_entry()
            insts = entry.insts
        self._design = design
        return Artifacts(
            kind="xclbin",
            image=picture,
            insts=insts,
            entry=entry,
            designs=(
                Design(
                    name=self.name,
                    operators=(self.name,),
                    entry=entry,
                    image=picture,
                    insts=insts,
                ),
            ),
            steps=(Step(0, self.name, self.name, tuple(b.name for b in self.buffers)),),
            buffers={b.name: ("arg", i, b.nbytes) for i, b in enumerate(self.buffers)},
        )

    def get_callable(self):
        """The loaded image, ready to call on device tensors."""
        import aie.utils as aie_utils
        from aie.utils.npukernel import NPUKernel

        self.compile()
        image = self.ov.external
        npu_kernel = NPUKernel(
            xclbin_path=str(self.artifacts.image),
            kernel_name="MLIR_AIE" if image is None else image.kernel_name,
            insts_path=str(self.artifacts.insts),
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={getattr(self, f.name)!r}"
            for f in dataclasses.fields(self)
            if f.repr and f.name != "ov"
        )
        return f"{type(self).__name__}({self.ov!r}, {own})"
