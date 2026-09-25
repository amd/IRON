# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The buffer-sizing half of a declaration.

An operator is declared against one overlay and adds the extents that size
the host buffers. Changing an extent re-issues the runtime sequence; it does
not rebuild the array, which is why the two layers are separate classes.
Calling one binds it: :func:`~iron.common.declare.infer` turns operand shapes into the
extents, and the instance's buffer attributes answer in elements.
"""

from __future__ import annotations

import dataclasses
from abc import ABCMeta
from typing import Any, ClassVar, Generic, TypeVar


import aie.utils as aie_utils
from aie.utils.npukernel import NPUKernel


from .bound import BoundBuffer, BoundValue
from .infer import infer, infer_kwargs
from .member import _Buffer, _Member, _Value
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
        from .. import graph as _graph  # imports this package: a cycle at module scope

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

        ``rt`` is an :class:`iron.common.design.Sequence`: ``rt.fill(stream,
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
        from .. import graph as _graph  # as above

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

    # -- construction from operand shapes ----------------------------------

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> "Operator":
        """Construct an operator (and its overlay) from operand shapes."""
        values = infer(cls, *operand_shapes, **infer_kwargs(cls, overrides))
        kwargs = {**overrides, **values}
        return cls(**kwargs)  # classic-construction path splits overlay fields

    # -- the image of one operator on its own -------------------------------

    @property
    def dev(self):
        """The device a design is generated for."""
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
        own = label_parts(self, skip=("ov",))
        base = type(self).__name__ + "_" + "_".join(own + self.ov.name_parts())
        dev = aie_utils.get_current_device()
        return f"{base}_{dev.resolve().name}"

    def generator(self, image: str = "elf"):
        """The design generator :class:`CompilableDesign` runs for this operator.

        An override point, not a forwarder: an operator whose design is
        exported text rather than derived from the declaration replaces this
        (see :func:`from_spec`, and swiglu_prefill_stream, which loads its
        group from the exported module). Everything else takes the default,
        which is ``build_design`` over the declaration.
        """
        from ..design import (
            generator_for,
        )  # reads this package: a cycle at module scope

        return generator_for(self, image=image)

    def compile(self, record: str = "memory") -> "Operator":
        """Build this operator's own image, once; sets :attr:`artifacts`.

        ``record="disk"`` also writes the :class:`~iron.common.image.artifacts.Artifacts`
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
        # image/ reads this package, so naming it at module scope would make
        # the two import each other.
        from ..image.artifacts import Artifacts, Design, Step
        from ..image.jit_compile import insts_design, xclbin_design

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
