# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator: one class declaring the array, the buffers and the sequence.

The fields a tile names, plus those marked ``array=True``, configure the
array, which serves every extent; the rest reach only the runtime sequence.
"""

from __future__ import annotations

import copy
import dataclasses
import hashlib
import inspect
import math
from collections.abc import Iterable, Mapping
from contextvars import ContextVar
from types import FunctionType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Self,
    TypeVar,
    dataclass_transform,
    overload,
)

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import ceildiv
from aie.utils.trace import TraceConfig
from aie.utils.verify import Tolerance

from ..testing import Testing
from .bound import BoundBuffer, BoundValue
from .creation import declare
from .domain import Domain, Width
from .field import DimRef, OptionalDim, Select, Tier, Unresolvable, param
from .member import (
    Extent,
    In,
    Scratchpad,
    Value,
    _Buffer,
    _Member,
    _Value,
    present,
)
from .profile import Profile

if TYPE_CHECKING:
    from ..graph.handle import Handle

_T = TypeVar("_T")

graph_tracer: ContextVar[Any] = ContextVar("graph_tracer", default=None)


class _OperatorMeta(type):
    """``GEMV(w, h)`` inside a graph's body records a step; anything else constructs."""

    if TYPE_CHECKING:

        @overload
        def __call__(
            cls: type[_T], operand: Any, /, *operands: Any, **kwargs: Any
        ) -> Handle: ...
        @overload
        def __call__(cls: type[_T], **kwargs: Any) -> _T: ...

    def __call__(cls, *args, **kwargs):
        tracer = graph_tracer.get()
        if tracer is not None and args and tracer.accepts(args):
            return tracer.call(cls, args, kwargs)
        if args:
            raise TypeError(
                f"{cls.__name__} is constructed by keyword ({cls.__name__}(M=..., "
                f"K=...)); operands are given inside a graph's body"
            )
        kwargs.setdefault(
            "pinned",
            frozenset(
                k
                for k, v in kwargs.items()
                if k in cls._tunable_fields and v is not None
            ),
        )
        profile = Profile.current()
        if profile is not None:
            kwargs = {**profile.tunables_for(cls, kwargs), **kwargs}
        return super().__call__(*args, **kwargs)


def _check_shipped(cls: type) -> None:
    if "array" in vars(cls):
        raise TypeError(
            f"{cls.__name__} runs a shipped image, so nothing builds its array(); "
            f"drop the override"
        )
    for m in cls._members:
        if isinstance(m, _Buffer) and m.tile is not None and m.via is None:
            raise TypeError(
                f"{cls.__name__}.{m.name}: a stream into a shipped image must be "
                f"pinned with via=; nothing else says which shim it uses"
            )
        if isinstance(m, Value) and m.derive is not None and m.address is None:
            raise TypeError(
                f"{cls.__name__}.{m.name}: a value written into a shipped image "
                f"needs an address; the sequence writes it there"
            )


class _ArrayView:
    """The array tier of an operator: reading any other field raises."""

    __slots__ = ("_op",)

    def __init__(self, op: "Operator") -> None:
        object.__setattr__(self, "_op", op)

    @property
    def __class__(self):
        # super() and isinstance() inside a hook see the operator's class.
        return type(object.__getattribute__(self, "_op"))

    def __getattr__(self, name: str):
        op = object.__getattribute__(self, "_op")
        fields = {f.name for f in dataclasses.fields(op) if Tier in f.metadata}
        if name in fields and name not in op._array_fields:
            raise TypeError(
                f"{type(op).__name__}.array() reads {name}, which no tile names: "
                f"an array serves every extent. Declare it param(..., array=True) "
                f"if the array does read it, or move the dependence into the "
                f"sequence or a Value"
            )
        attr = inspect.getattr_static(type(op), name, None)
        if isinstance(attr, FunctionType):
            return attr.__get__(self, type(op))
        if isinstance(attr, property) and attr.fget is not None:
            return attr.fget(self)
        return getattr(op, name)

    def __setattr__(self, name: str, value) -> None:
        setattr(object.__getattribute__(self, "_op"), name, value)


class _ExtentWord(Value):
    """The tiles per lane of one operand under a bound, rounded up to whole tiles."""

    def __init__(self, owner: type, extent: Extent, buffer: str, axis: int) -> None:
        super().__init__(np.int32, derive=self._tiles)
        self.owner = owner
        self.name = f"{extent.name}_{buffer}"
        self.extent, self.buffer, self.axis = extent, buffer, axis

    def _tiles(self, op) -> int:
        extent = getattr(op, self.extent.name)  # read first: it makes this per call
        return ceildiv(extent, self.divisor(op))

    def divisor(self, op) -> int:
        b = op.value_buffer(self.buffer)
        lanes = 1 if b.replicate else b.count
        return lanes * b.extent_unit(self.axis)

    def __repr__(self) -> str:
        return f"<tiles per lane of {self.buffer} under {self.extent.name}>"


class _ChainWord(Value):
    """Which of its array's chains, ``finishes`` or ``prepares``, an
    operator's cores apply.
    """

    def __init__(self, owner: type, kind: str) -> None:
        super().__init__(np.int32, derive=self._index, optional=True)
        self.owner = owner
        self.kind = kind
        self.name = f"{kind}_chain"

    def _index(self, op) -> int:
        own, chains = (
            (op.finish, op.finishes)
            if self.kind == "finish"
            else (op.prepare, op.prepares)
        )
        keys = [tuple(link.array_key() for link in c) for c in chains]
        return keys.index(tuple(link.array_key() for link in own))

    def __repr__(self) -> str:
        return f"<the {self.kind} chain a design selects>"


class _PlaceWord(Scratchpad):
    """The per-call element offset of an operand placed in a larger buffer:
    every transfer of it moves by the word (``Operator.placed``).
    """

    def __init__(self, owner: type, buffer: str) -> None:
        super().__init__(np.int32)
        self.owner = owner
        self.buffer = buffer
        self.name = f"{buffer}_offset"

    def __repr__(self) -> str:
        return f"<the offset {self.buffer} is placed at>"


@dataclasses.dataclass(frozen=True)
class CopyRun:
    """Where an operator writes its one input verbatim, as one contiguous
    run of its one output (``Operator.copies_to``).
    """

    # The elements of the output, and the one the run starts at.
    into: int
    start: int
    # The per-call value adding to ``start``, if any.
    offset: str | None = None


@dataclasses.dataclass(frozen=True)
class Link:
    """One step of a finish or a prologue: ``op`` applied to a tile of the
    producer's output, which enters as its input ``at``, or to a tile of the
    consumer's prepared input, which ``op`` produced from its input ``at``.
    Its other inputs stream into the cores beside it, their
    ``finish_inputs`` or ``prepare_inputs``.
    """

    op: Operator
    at: int = 0

    def array_key(self):
        return (self.op.array_key(), self.at)

    def at_line(self, line: int, dtype, dev, ordered: bool = True) -> Link:
        """This step resolved at one tile (``Operator.at_line``)."""
        return Link(self.op.at_line(line, dtype, dev, ordered, self.at), self.at)

    def operands(self, tile, extras) -> list:
        """``tile`` at input ``at`` among this step's ``extras``."""
        operands = list(extras)
        operands.insert(self.at, tile)
        return operands


# ``auto`` is not a listed specifier: pyright reads a default only from
# ``default=``, and ``auto(2)`` passes it positionally.
@dataclass_transform(kw_only_default=True, field_specifiers=(param,))
@dataclasses.dataclass(eq=False, repr=True)
class Operator(metaclass=_OperatorMeta):
    """An operator. Subclass it; every subclass is a dataclass checked as its body finishes."""

    _members: ClassVar[tuple[_Member, ...]] = ()
    _param_fields: ClassVar[tuple[str, ...]] = ()
    _derived_params: ClassVar[dict[str, Callable[[Any], Any]]] = {}
    _auto_fields: ClassVar[tuple[str, ...]] = ()
    _tunable_fields: ClassVar[tuple[str, ...]] = ()
    _domains: ClassVar[dict[str, Domain]] = {}
    _array_fields: ClassVar[tuple[str, ...]] = ()
    _probe_fields: ClassVar[dict[str, Any]] = {}
    _external: ClassVar[Any] = None
    test: ClassVar[Testing | None] = None
    # True when sequence() calls rt.preamble() itself, behind its first fills.
    own_preamble: ClassVar[bool] = False
    # A fused image lowers every operator's sequence under the union.
    aiecc_flags: ClassVar[tuple[str, ...]] = ()
    # Per leading operand that may be a view: the param holding its pattern
    # and the per-call value a dynamic index binds.
    accept_views: ClassVar[tuple[tuple[str, str], ...]] = ()
    # An instance's operands beside the declared ones: its prologue's and
    # its finish's other inputs.
    _prepare_inputs: ClassVar[tuple[_Buffer, ...]] = ()
    _finish_inputs: ClassVar[tuple[_Buffer, ...]] = ()

    trace: TraceConfig | None = dataclasses.field(
        default=None, repr=False, kw_only=True
    )
    # The graph values bound to per-call values, by member name; design_key
    # adds them, since a dict does not hash.
    bound_values: dict[str, str | None] = dataclasses.field(
        default_factory=dict, repr=False, compare=False, kw_only=True
    )
    # The tunables its caller gave, which the tuner holds; a profile's and
    # resolve()'s are starting points it may move.
    pinned: frozenset[str] = dataclasses.field(
        default=frozenset(), repr=False, compare=False, kw_only=True
    )
    # The steps each core applies, in order, to a tile of the output
    # declared Out(finish=True) before releasing it; resolved, each one at
    # that tile (``at_line``). The keys add them, since operators compare by
    # identity.
    finish: tuple[Link, ...] = dataclasses.field(
        default=(), repr=False, compare=False, kw_only=True
    )
    # The finishes the array applies, each design selecting its own; empty
    # for the array of ``finish`` alone.
    finishes: tuple[tuple[Link, ...], ...] = dataclasses.field(
        default=(), repr=False, compare=False, kw_only=True
    )
    # The steps each core applies, in order, to a tile of the input declared
    # In(prepare=True) after acquiring it, and the prologues its array
    # applies; as ``finish`` and ``finishes``.
    prepare: tuple[Link, ...] = dataclasses.field(
        default=(), repr=False, compare=False, kw_only=True
    )
    prepares: tuple[tuple[Link, ...], ...] = dataclasses.field(
        default=(), repr=False, compare=False, kw_only=True
    )
    # Per output a graph placed in a larger buffer (``placed``): its name,
    # that buffer's elements and the one it starts at; design_key adds them.
    placements: tuple[tuple[str, int, int], ...] = dataclasses.field(
        default=(), repr=False, compare=False, kw_only=True
    )

    def __init_subclass__(cls, image=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if image is not None:
            cls._external = image
        declare(cls)
        if image is not None:
            _check_shipped(cls)

    def __post_init__(self) -> None:
        self._resolved = False
        self._derive_params()
        # A graph's reference constructs at a bounded call's valid rows, a
        # shape no device runs, for reference() alone: it is not checked.
        tracer = graph_tracer.get()
        checked = tracer is None or tracer.checks
        if checked:
            self.validate()
        self._bind()
        if checked and not any(getattr(self, n) is None for n in self._auto_fields):
            self.compatible()

    def _derive_params(self) -> None:
        for name, derive in self._derived_params.items():
            if getattr(self, name) is None:
                value = derive(self)
                if value is None:
                    raise ValueError(
                        f"{type(self).__name__}.{name}: not given, and nothing "
                        f"to compute it from"
                    )
                setattr(self, name, value)

    def check_derived(self, *names: str) -> None:
        """Raise ``ValueError`` if a given computed-default parameter disagrees with its rule."""
        for name in names:
            given, expected = getattr(self, name), self._derived_params[name](self)
            if given != expected:
                raise ValueError(
                    f"{type(self).__name__}.{name}={given!r} is not what its "
                    f"other fields make it ({expected!r})"
                )

    def validate(self) -> None:
        """Check the sequence-tier fields on their own. Runs at construction."""

    def compatible(self) -> None:
        """Check the extents against the resolved tunables; raise ``ValueError``."""

    def resolve(self, dev) -> Self:
        """Return a copy with every ``auto()`` filled from ``dev`` and the extents.

        Raises:
            Unresolvable: No legal value exists on ``dev``.
        """
        return dataclasses.replace(self)

    def array(self, target) -> list:
        """Build the array for ``target`` and return its workers.

        Bind every operand's lane to a fifo's shim end and every ``Value`` to
        the buffer a core reads it from.
        """
        raise NotImplementedError(f"{type(self).__name__}.array() is not implemented")

    def build_array(self, target) -> list:
        return type(self).array(_ArrayView(self), target)

    def tolerance(self) -> Tolerance | None:
        """The contract tolerance of the kernel this array runs; ``None`` if none applies."""
        return None

    def gate(self) -> Tolerance | None:
        """What this operator's output is judged by: its ``Testing``
        tolerance where it declares one, else its resolved contract's. A
        declared tolerance is the plain operator's, so a finish or a
        prologue is judged by ``tolerance()``, which composes it.
        """
        declared = type(self).test
        if (
            declared is not None
            and declared.tolerance is not None
            and not (self.finish or self.prepare)
        ):
            return declared.tolerance
        return self.resolved().tolerance()

    def ops(self) -> int:
        """The arithmetic operations one call performs, for its throughput."""
        return sum(b.elements for b in self.outputs)

    def fold(self, consumer: Operator, at: int = 0) -> Self | None:
        """This operator applying ``consumer`` to its output in its own cores:
        ``consumer`` appended to its ``finish``. The array keeps the
        finishes it had, unless a step of the chain takes inputs of its own,
        which stream into this array alone. Whether ``consumer`` runs on one
        of its tiles is asked when the result resolves (``at_line``).

        Args:
            consumer: The operator whose input ``at`` is this one's one output.
            at: The input of ``consumer`` the output enters; its others
                become this operator's ``finish_inputs``.

        Returns:
            The folded operator, or None where this one's one output is not
            declared ``finish=True``.
        """
        if len(self.outputs) != 1 or not self.outputs[0].member.finish:
            return None
        chain = (*self.finish, Link(consumer, at))
        if any(len(link.op.inputs) > 1 for link in chain):
            return dataclasses.replace(self, finish=chain, finishes=())
        return dataclasses.replace(
            self, finish=chain, finishes=(*(self.finishes or (self.finish,)), chain)
        )

    def prefold(self, producer: Operator, at: int = 0) -> Self | None:
        """This operator applying ``producer`` to its prepared input in its
        own cores: ``producer`` prepended to its ``prepare``, as ``fold``
        appends to a finish. Whether ``producer`` runs on one of its tiles
        is asked when the result resolves (``at_line``).

        Args:
            producer: The operator whose one output is this one's input
                declared ``In(prepare=True)``.
            at: The input of ``producer`` that tile takes the place of; its
                others become this operator's ``prepare_inputs``.

        Returns:
            The folded operator, or None where this one declares no
            prepared input.
        """
        if not any(m.prepare for m in self._members_io()):
            return None
        chain = (Link(producer, at), *self.prepare)
        if any(len(link.op.inputs) > 1 for link in chain):
            return dataclasses.replace(self, prepare=chain, prepares=())
        return dataclasses.replace(
            self, prepare=chain, prepares=(*(self.prepares or (self.prepare,)), chain)
        )

    def on_array(self, other: Operator) -> Self | None:
        """This operator declared to run on ``other``'s array, or None:
        one of its type, given its finishes and prologues.

        A graph's fold calls it after folding ``other``; the replacement is
        taken only where it resolves to ``other``'s array.
        """
        if type(other) is not type(self) or not (other.finishes or other.prepares):
            return None
        return dataclasses.replace(
            self, finishes=other.finishes, prepares=other.prepares
        )

    def copies_to(self) -> CopyRun | None:
        """Where this operator writes its one input verbatim, as one run of
        its one output; None where it does not, the default.
        """
        return None

    def placed(self, copy: Operator, operand: str) -> Self | None:
        """This operator writing its output ``operand`` where ``copy``
        writes it (``copies_to``), so a graph drops the copy: the operand is
        ``copy``'s output at runtime, every transfer of it moved to the run,
        and by the per-call value moving the run.

        Returns:
            The placed operator, or None where its transfers cannot move:
            a shipped image's, or one whose sequence moves them itself.
        """
        if self.external is not None:
            return None
        run = copy.copies_to()
        if run is None:
            return None
        values = dict(self.bound_values)
        if run.offset is not None:
            values[f"{operand}_offset"] = copy.bound_values[run.offset]
        return dataclasses.replace(
            self,
            bound_values=values,
            placements=(*self.placements, (operand, run.into, run.start)),
        )

    def at_line(self, line: int, dtype, dev, ordered: bool = True, at: int = 0) -> Self:
        """This operator applied by another's core to one tile of its output,
        a run of ``line`` elements of ``dtype``, resolved for ``dev``.
        ``ordered`` is False where the core holds the run in an order of its
        own (``Out(finish=block)``); the tile enters as its input ``at``.

        Raises:
            ValueError: It runs on cores of its own, or not at this line, in
                this order or with the tile at this input.
        """
        raise ValueError(f"{type(self).__name__} runs on cores of its own")

    def finish_line(self, dev, lines: Iterable[int]) -> int:
        """The first of ``lines`` each chain of this operator's array
        finishes a tile of, for a ``resolve`` choosing its output's tile.

        Raises:
            Unresolvable: None of them.
        """
        links = [link for c in self.finishes or (self.finish,) for link in c]
        out = self.outputs[0]
        ordered = out.member.finish_block is None
        tried = []
        for line in lines:
            try:
                for link in links:
                    link.at_line(line, out.dtype, dev, ordered)
            except ValueError as e:
                tried.append(f"{line}: {e}")
                continue
            return line
        raise Unresolvable(
            f"{type(self).__name__}: no output tile its finish runs at; "
            + "; ".join(tried)
        )

    def device(self, target):
        return target.dev

    @property
    def external(self):
        return type(self)._external

    def configuration(self) -> Self:
        """The operator whose xclbin this one runs when it runs alone."""
        return self

    def exported_design(self, image: str):
        """The design another tool exports for this operator; ``None`` derives it."""
        return None

    @classmethod
    def shim_columns(
        cls,
        dev,
        num_channels: int = 1,
        flags: Mapping[str, Any] | None = None,
        operands: Iterable[_Buffer] = (),
    ) -> int:
        """How many of ``dev``'s columns fit this operator's streams in the shim DMA budget.

        A ``replicate`` stream is paid once per channel rather than per column,
        and a stream with no ``per=`` once. ``operands`` are an instance's
        streams beside the declared ones (``finish_inputs``; a prologue's
        inputs share the stream they prepare).
        """
        streams = [
            m
            for m in (*cls._members, *operands)
            if isinstance(m, _Buffer) and m.tile is not None and present(m, flags or {})
        ]
        cols = dev.cols
        for drains, budget in (
            (False, dev.shim_dma_channels_in),
            (True, dev.shim_dma_channels_out),
        ):
            ours = [m for m in streams if m.direction.drains == drains]
            lanes = [m for m in ours if m.per is not None]
            per_core = sum(not m.replicate for m in lanes) * num_channels
            once = len(ours) - len(lanes)
            shared = sum(m.replicate for m in lanes) * num_channels + once
            if per_core:
                cols = min(cols, (budget - shared) // per_core)
        return max(1, cols)

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        allowed = self.shim_columns(dev, num_channels, vars(self), self._finish_inputs)
        if cols > allowed:
            raise Unresolvable(
                f"{type(self).__name__} with {cols} columns x {num_channels} "
                f"channels exceeds this device's shim DMA budget; "
                f"{allowed} columns fit"
            )

    def resolve_columns(
        self,
        dev,
        given: int | None,
        num_channels: int = 1,
        *,
        fits: Callable[[int], bool] | None = None,
    ) -> int:
        """``given``, checked against the shim budget, or the most columns that ``fits``.

        When no count fits, one column is returned and ``compatible`` names the rule.
        """
        if given is not None:
            if dev is not None:
                self.check_shim_columns(dev, given, num_channels)
            return given
        if dev is None:
            raise Unresolvable(
                f"{type(self).__name__}: the column count defaults from the "
                f"device; none is bound and none was given"
            )
        budget = self.shim_columns(dev, num_channels, vars(self), self._finish_inputs)
        return next((c for c in range(budget, 0, -1) if fits is None or fits(c)), 1)

    def reference(self, *inputs):
        raise NotImplementedError(
            f"{type(self).__name__}.reference() is not implemented"
        )

    def sequence(self, rt) -> None:
        """Override to write the runtime sequence by hand; otherwise it is derived."""
        raise NotImplementedError

    @classmethod
    def has_sequence_override(cls) -> bool:
        return cls.sequence is not Operator.sequence

    def value_symbol(self, value: "BoundValue") -> str | None:
        return None

    def design_key(self):
        """Identity for sharing a build: equal keys generate byte-identical MLIR."""
        own = tuple(
            (f.name, getattr(self, f.name))
            for f in dataclasses.fields(self)
            if f.compare
        )
        if self.bound_values:
            own += (("values", tuple(sorted(self.bound_values.items()))),)
        if self.placements:
            own += (("placements", self.placements),)
        if self.finish:
            own += (("finish", tuple(link.array_key() for link in self.finish)),)
        if any(self.finishes):
            own += (("finishes", self._finish_keys()),)
        if self.prepare:
            own += (("prepare", tuple(link.array_key() for link in self.prepare)),)
        if any(self.prepares):
            own += (("prepares", self._prepare_keys()),)
        return (type(self).__qualname__, own)

    def probed(self) -> Self:
        """This operator with each ``param(probe=)`` field at its probe: the
        one its step time is measured as, for every value of those fields.
        Itself when they are there already, unresolved otherwise.
        """
        if all(getattr(self, n) == v for n, v in self._probe_fields.items()):
            return self
        return dataclasses.replace(self, **self._probe_fields)

    def array_key(self):
        key = (type(self).__qualname__,) + tuple(
            (name, getattr(self, name)) for name in self._array_fields
        )
        if any(self.finishes or (self.finish,)):
            key += (("finishes", self._finish_keys()),)
        if any(self.prepares or (self.prepare,)):
            key += (("prepares", self._prepare_keys()),)
        return key

    def _finish_keys(self) -> tuple:
        return tuple(
            tuple(link.array_key() for link in c)
            for c in self.finishes or (self.finish,)
        )

    def _prepare_keys(self) -> tuple:
        return tuple(
            tuple(link.array_key() for link in c)
            for c in self.prepares or (self.prepare,)
        )

    def resolved(self, dev=None) -> Self:
        """This operator resolved for ``dev`` (the bound device unless given), checked."""
        if self._resolved:
            return self
        new = self.resolve(dev if dev is not None else self.dev)
        if new is self:
            raise TypeError(
                f"{type(self).__name__}.resolve() must return a copy, "
                f"dataclasses.replace(self, ...), not self"
            )
        if not isinstance(new, type(self)):
            raise TypeError(
                f"{type(self).__name__}.resolve() must return a {type(self).__name__}"
            )
        missing = [n for n in self._auto_fields if getattr(new, n) is None]
        if missing:
            raise Unresolvable(
                f"{type(self).__name__}.resolve() left {missing} unset for {dev}"
            )
        if any(new.prepares or (new.prepare,)):
            new._prepare_at(dev if dev is not None else self.dev)
        if any(new.finishes or (new.finish,)):
            new._finish_at(dev if dev is not None else self.dev)
        new.validate()
        new.compatible()
        new._resolved = True
        return new

    def _finish_at(self, dev) -> None:
        """Rebuild each finish at the output tile, the array's unique and in
        a fixed order.

        Raises:
            ValueError: No output is finished by the array that runs, a step
                does not run at the tile, or ``finish`` is not among
                ``finishes``.
            Unresolvable: Each core reads more streams, its own and the
                finish's inputs, than a core tile has input channels, or a
                finish input would stream into a block held out of order.
        """
        out = self.outputs[0] if len(self.outputs) == 1 else None
        # A subclass replacing array() does not apply what its base's output declares.
        runs = next(k for k in type(self).__mro__ if "array" in vars(k))
        if out is None or not out.member.finish or runs not in out.member.owner.__mro__:
            raise ValueError(
                f"{type(self).__name__}: its cores finish no output, so it "
                f"applies no finish"
            )
        line = out.finish_line
        ordered = out.member.finish_block is None
        own = tuple(link.at_line(line, out.dtype, dev, ordered) for link in self.finish)
        chains: dict[tuple, tuple[Link, ...]] = {}
        for chain in self.finishes or (self.finish,):
            at = tuple(link.at_line(line, out.dtype, dev, ordered) for link in chain)
            chains.setdefault(tuple(link.array_key() for link in at), at)
        if not ordered and any(len(link.op.inputs) > 1 for link in own):
            raise Unresolvable(
                f"{type(self).__name__}: its cores hold each block of the output "
                f"in an order of their own, which a finish input does not stream in"
            )
        if tuple(link.array_key() for link in own) not in chains:
            raise ValueError(
                f"{type(self).__name__}: its finish is not one its array applies"
            )
        if len(chains) > 1 and any(
            len(link.op.inputs) > 1 for c in chains.values() for link in c
        ):
            raise ValueError(
                f"{type(self).__name__}: a finish step with inputs of its own "
                f"streams them into an array serving no other finish"
            )
        self.finish = own
        self.finishes = (
            ()
            if len(chains) == 1
            else tuple(chains[k] for k in sorted(chains, key=repr))
        )
        self._bind()
        reads = sum(
            m.direction.fills and m.tile is not None for m in self._members_io()
        )
        if reads > dev.core_dma_channels_in:
            raise Unresolvable(
                f"{type(self).__name__}: its cores read {reads} streams with the "
                f"finish's inputs, past a core tile's {dev.core_dma_channels_in} "
                f"input channels"
            )

    def _prepare_at(self, dev) -> None:
        """Rebuild each prologue at the prepared input's tile, the array's
        unique and in a fixed order.

        Raises:
            ValueError: No input is prepared, a step does not run at the
                tile, ``prepare`` is not among ``prepares``, or a step
                with inputs of its own is in an array serving another
                prologue.
            Unresolvable: A step's other input is not one tile, or the
                prepared input brings a core more than one tile a call,
                beside which no other input's tile streams.
        """
        into = next((b for b in self.inputs if b.member.prepare), None)
        if into is None:
            raise ValueError(
                f"{type(self).__name__}: its cores prepare no input, so it "
                f"applies no prologue"
            )
        line = math.prod(into.tile_shape)
        for link in self.prepare:
            for k, b in enumerate(link.op.inputs):
                if k != link.at and b.elements != line:
                    raise Unresolvable(
                        f"{type(self).__name__}: {type(link.op).__name__}.{b.name} "
                        f"is {b.elements} elements, not the {line}-element tile "
                        f"it streams in beside"
                    )
        extras = any(len(link.op.inputs) > 1 for link in self.prepare)
        tiles = into.elements // (1 if into.replicate else into.count)
        if extras and tiles != line:
            raise Unresolvable(
                f"{type(self).__name__}: each core takes {tiles // line} tiles of "
                f"{into.name} a call, and a prologue's inputs stream in beside one"
            )
        own = tuple(link.at_line(line, into.dtype, dev) for link in self.prepare)
        chains: dict[tuple, tuple[Link, ...]] = {}
        for chain in self.prepares or (self.prepare,):
            at = tuple(link.at_line(line, into.dtype, dev) for link in chain)
            chains.setdefault(tuple(link.array_key() for link in at), at)
        if tuple(link.array_key() for link in own) not in chains:
            raise ValueError(
                f"{type(self).__name__}: its prologue is not one its array applies"
            )
        if len(chains) > 1 and any(
            len(link.op.inputs) > 1 for c in chains.values() for link in c
        ):
            raise ValueError(
                f"{type(self).__name__}: a prologue step with inputs of its own "
                f"streams them into an array serving no other prologue"
            )
        self.prepare = own
        self.prepares = (
            ()
            if len(chains) == 1
            else tuple(chains[k] for k in sorted(chains, key=repr))
        )
        self._bind()

    def copy(self) -> Self:
        """A fresh instance for one build, keeping resolution and bound values."""
        new = dataclasses.replace(self)
        new._resolved = self._resolved
        if self._resolved:
            # replace() resets the init=False fields compatible() records.
            new.compatible()
        return new

    def with_tunables(self, **tunables: Any) -> Self:
        """This operator, unresolved, with the given ``auto()`` fields set.

        Raises:
            TypeError: A name is not a settable tunable: not an ``auto()``
                field, fixed with ``init=False``, or ``derived``.
        """
        unknown = [n for n in tunables if n not in self._tunable_fields]
        if unknown:
            raise TypeError(f"{type(self).__name__} has no tunable {unknown}")
        return dataclasses.replace(self, **tunables)

    @property
    def widths(self) -> dict[str, int | None]:
        """The tunables searched as a `Width`, and their values: those that
        declare one, and those a streamed ``per=`` names that declare no
        other domain.
        """
        found = {
            n: getattr(self, n)
            for n, domain in self._domains.items()
            if isinstance(domain, Width)
        }
        for b in self.buffers:
            for ref in b.member.per.dims if b.streamed and b.member.per else ():
                if (
                    isinstance(ref, DimRef)
                    and ref.name in self._tunable_fields
                    and ref.name not in self._domains
                ):
                    found.setdefault(ref.name, getattr(self, ref.name))
        return found

    def domains(self, dev) -> dict[str, tuple[Any, ...]]:
        """The values the tuner tries for each tunable it searches, asked of
        the resolved operator: the field's declared domain where its
        ``when`` flag holds, a `Width` for one of `widths`, and nothing for
        any other. A combination the operator cannot resolve at is left
        out by the tuner. A ``pinned`` tunable is not searched.
        """
        widths = self.widths
        found = {}
        for name in dict.fromkeys([*widths, *self._tunable_fields]):
            domain = self._domains.get(name, Width() if name in widths else None)
            if (
                name in self.pinned
                or domain is None
                or (domain.when is not None and not getattr(self, domain.when))
            ):
                continue
            found[name] = domain.values(self, dev, name)
        return found

    @property
    def buffers(self) -> list[BoundBuffer]:
        return [self._bound[m.name] for m in self._members_io()]

    @property
    def inputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction.fills]

    @property
    def outputs(self) -> list[BoundBuffer]:
        return [b for b in self.buffers if b.direction.drains]

    @property
    def prepare_inputs(self) -> list[BoundBuffer]:
        """The inputs of ``prepare``'s steps other than the tile, in order,
        each a tile filled into the prepared input's stream after it: the
        inputs after the declared ones.
        """
        return [self._bound[m.name] for m in self._prepare_inputs]

    @property
    def finish_inputs(self) -> list[BoundBuffer]:
        """The inputs of ``finish``'s steps other than the tile, in order,
        each streamed as the finished output is: the last of ``inputs``.
        """
        return [self._bound[m.name] for m in self._finish_inputs]

    @property
    def values(self) -> list[BoundValue]:
        return [
            self._bound[m.name] for m in self._value_members if self.uses_value(m.name)
        ]

    @property
    def residents(self) -> dict[str, Any]:
        """What the preamble writes once per build, by name."""
        return {
            m.name: m.derive(self)
            for m in (*self._members, *self._chain_words)
            if isinstance(m, Value)
            and m.derive is not None
            and not self.uses_value(m.name)
        }

    def uses_value(self, name: str) -> bool:
        """Whether this instance drives the per-call value ``name``; unused ones get no parameter."""
        member = next((m for m in self._value_members if m.name == name), None)
        if isinstance(member, (Extent, _PlaceWord)):
            return name in self.bound_values
        if isinstance(member, Value) and member.derive is not None:
            return name in self.bound_values or name in self._per_call_derived()
        return True

    @property
    def bound_extents(self) -> dict[str, str | None]:
        bound = self.bound_values
        return {
            m.name: bound[m.name]
            for m in self._members
            if isinstance(m, Extent) and m.name in bound
        }

    def _per_call_derived(self) -> frozenset[str]:
        bound = self.bound_extents
        if not bound:
            return frozenset()
        # From array(), derivations run on the operator: reading an extent here is not the array's.
        op = object.__getattribute__(self, "_op") if type(self) is _ArrayView else self
        probe = copy.copy(op)
        out = set()
        for m in self._value_members:
            if not (isinstance(m, Value) and m.derive is not None):
                continue
            reads: set[str] = set()
            vars(probe)["_extent_reads"] = reads
            try:
                m.derive(probe)
            except Exception:
                pass  # unresolved: what it read before failing still counts
            if reads & bound.keys():
                out.add(m.name)
        return frozenset(out)

    def derived_at(self, name: str, **extents: int) -> Any:
        """The word the host writes for ``name`` with the extents at the given bounds."""
        member = next((m for m in self._value_members if m.name == name), None)
        if not (isinstance(member, Value) and member.derive is not None):
            raise TypeError(f"{type(self).__name__}.{name} is not a derived value")
        unknown = set(extents) - {
            m.name for m in self._members if isinstance(m, Extent)
        }
        if unknown:
            raise TypeError(
                f"{type(self).__name__} declares no Extent {sorted(unknown)}"
            )
        at = copy.copy(self)
        vars(at)["_extents"] = {**self.__dict__.get("_extents", {}), **extents}
        return member.derive(at)

    def extent_unit(self, buffer: str) -> int | None:
        """The rows of ``buffer`` one lane takes at a time under a bound.

        ``None`` for the stream tile's rows; ``0`` when a bound does not shorten it.
        """
        return None

    def value_buffer(self, name: str) -> BoundBuffer:
        b = self._bound.get(name)
        if not isinstance(b, BoundBuffer):
            raise TypeError(f"{type(self).__name__} declares no operand {name!r}")
        return b

    def value(self, name: str) -> BoundValue:
        """The device word of value ``name`` (an ``Extent`` attribute reads as an integer)."""
        try:
            return self._bound[name]
        except KeyError:
            raise TypeError(
                f"{type(self).__name__} declares no value {name!r}"
            ) from None

    def use_value(self, name: str, bound_to: str | None = None) -> None:
        """Record that a graph binds the per-call value ``name`` to its value ``bound_to``."""
        if not any(m.name == name for m in self._value_members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        # Rebound, not updated: replace() hands a copy the same dict.
        self.bound_values = {**self.bound_values, name: bound_to}

    def __call__(self, *args, **kwargs):
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(
                f"{type(self).__name__} instances are called on graph handles inside "
                f"a graph's body; outside one, run it as an OperatorImage"
            )
        return tracer.call(self, args, kwargs)

    def _bind(self) -> None:
        self._prepare_inputs = ()
        self._finish_inputs = ()
        prepared = next((m for m in self._members_io() if m.prepare), None)
        extras = []
        for i, link in enumerate(self.prepare if prepared is not None else ()):
            for k, b in enumerate(link.op.inputs):
                if k == link.at:
                    continue
                extra = In(*prepared.tile.dims, dtype=prepared.dtype)
                extra.__set_name__(type(self), f"prepare{i}_{b.name}")
                extras.append(extra)
        self._prepare_inputs = tuple(extras)
        outs = [m for m in self._members_io() if m.direction.drains]
        extras = []
        if len(outs) == 1 and outs[0].finish:
            (out,) = outs
            for i, link in enumerate(self.finish):
                for k, b in enumerate(link.op.inputs):
                    if k == link.at:
                        continue
                    extra = In(
                        *out.shape.dims,
                        dtype=out.dtype,
                        tile=out.tile.dims,
                        per=None if out.per is None else out.per.dims,
                        depth=out.depth,
                    )
                    extra.__set_name__(type(self), f"finish{i}_{b.name}")
                    extras.append(extra)
        self._finish_inputs = tuple(extras)
        bound: dict[str, Any] = {}
        for m in self._members_io():
            bound[m.name] = BoundBuffer(m, self)
        for m in self._members:
            if isinstance(m, _Value):
                bound[m.name] = BoundValue(m, self)
        self._bound = bound
        words = []
        for e in self._members:
            if not isinstance(e, Extent):
                continue
            for b in self._members_io():
                if b.tile is not None:
                    axis = bound[b.name].extent_axis(e)
                    if axis is not None and self.extent_unit(b.name) != 0:
                        word = _ExtentWord(type(self), e, b.name, axis)
                        bound[word.name] = BoundValue(word, self)
                        words.append(word)
        self._extent_words = tuple(words)
        self._chain_words: tuple[_ChainWord, ...] = ()
        for kind, chains in (("prepare", self.prepares), ("finish", self.finishes)):
            if len(chains) > 1:
                word = _ChainWord(type(self), kind)
                bound[word.name] = BoundValue(word, self)
                self._chain_words += (word,)
        self._place_words = tuple(
            _PlaceWord(type(self), m.name) for m in self._members_io()
        )
        for word in self._place_words:
            bound[word.name] = BoundValue(word, self)

    @property
    def _value_members(self) -> list[_Value]:
        return [m for m in self._members if isinstance(m, _Value)] + [
            *self.__dict__.get("_extent_words", ()),
            *self.__dict__.get("_chain_words", ()),
            *self.__dict__.get("_place_words", ()),
        ]

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> Self:
        """Construct from operand shapes, an optional input's by keyword."""
        inputs, outputs, overrides = cls.call_operands(operand_shapes, overrides)
        return cls(**{**overrides, **cls.infer(inputs, outputs, **overrides)})

    @classmethod
    def call_operands(cls, args, kwargs) -> tuple[dict[str, Any], list, dict[str, Any]]:
        """Bind a call's operands as ``(x, ..., [outputs...], *, weight=None,
        ...)`` would: an optional input is a keyword, so an output is never
        taken for it.

        Returns:
            The inputs by name, in declaration order; the outputs; the other
            keywords.
        """
        ins = [m for m in cls._members if isinstance(m, _Buffer) and m.direction.fills]
        required = [m.name for m in ins if m.when is None]
        optional = {m.name for m in ins if m.when is not None}
        given = {k: v for k, v in kwargs.items() if k in optional and v is not None}
        if len(args) < len(required):
            raise TypeError(
                f"{cls.__name__} takes {len(required)} positional operand(s) "
                f"({', '.join(required)}), got {len(args)}"
            )
        bound = {**dict(zip(required, args)), **given}
        inputs = {m.name: bound[m.name] for m in ins if m.name in bound}
        rest = {k: v for k, v in kwargs.items() if k not in optional}
        return inputs, list(args[len(required) :]), rest

    @classmethod
    def infer(cls, inputs: Mapping[str, Any], outputs=(), **kwargs) -> dict[str, Any]:
        """Bind the dimension fields from operand shapes.

        Each declared dimension is a field or a literal, so this is a lookup.
        An optional input's ``when=`` flag is true where ``inputs`` names it.

        Args:
            inputs: The input shapes, by operand name.
            outputs: The shapes of caller-supplied outputs, in declaration
                order.
            **kwargs: Construction arguments; the dimension fields and shape
                flags among them pin values and are checked for agreement.

        Returns:
            ``{field: value}``: the pinned and the inferred fields, and the
            operand flags.

        Raises:
            TypeError: The operands are not the declared ones.
            ValueError: A shape disagrees with the declaration or another
                operand.
        """
        buffers = [m for m in cls._members if isinstance(m, _Buffer)]
        names = set(cls._param_fields)
        for m in buffers:
            names.update(d.flag.name for d in m.shape.dims if isinstance(d, Select))
        given = {k: v for k, v in kwargs.items() if k in names}
        flags: dict[str, bool] = {}
        for m in buffers:
            if not m.direction.fills or m.when is None:
                continue
            flag, has = m.when.name, m.name in inputs
            if flags.setdefault(flag, has) != has:
                raise TypeError(
                    f"{cls.__name__}: the operands {flag}= brings are given together"
                )
            if flag in given and bool(given[flag]) != has:
                raise TypeError(
                    f"{cls.__name__}({flag}=True) takes {m.name}="
                    if has is False
                    else f"{cls.__name__}: {m.name}= is an operand only where "
                    f"{flag} is true"
                )
        given |= flags
        ins = [m for m in buffers if m.direction.fills and present(m, given)]
        if [m.name for m in ins] != list(inputs):
            raise TypeError(
                f"{cls.__name__} takes {len(ins)} operand(s) "
                f"({', '.join(m.name for m in ins)}), got {len(inputs)}"
            )
        outs = [m for m in buffers if not m.direction.fills and present(m, given)]
        if outputs and len(outputs) != len(outs):
            raise TypeError(
                f"{cls.__name__} produces {len(outs)} output(s) "
                f"({', '.join(m.name for m in outs)}), got {len(outputs)}"
            )
        pairs = [(m, inputs[m.name]) for m in ins] + list(zip(outs, outputs))
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
            dims = list(m.shape.dims)
            at = next(
                (i for i, d in enumerate(dims) if isinstance(d, OptionalDim)), None
            )
            if at is not None:
                optional = dims.pop(at)
                if len(shape) == len(dims) + 1:
                    bind(optional.ref, shape[at], f"{m.name}.shape[{at}]")
                    shape = shape[:at] + shape[at + 1 :]
                elif len(shape) == len(dims):
                    bind(optional.ref, 1, f"{m.name} (rank {len(shape)})")
                else:
                    raise ValueError(
                        f"{cls.__name__}: operand {m.name} has rank {len(shape)}, "
                        f"declared {m!r}"
                    )
            expanded: list = []
            for d in dims:
                if not isinstance(d, Select):
                    expanded.append(d)
                    continue
                flag = d.flag
                value = bound.get(flag.name, flag.default)
                if value is dataclasses.MISSING:
                    raise ValueError(
                        f"{cls.__name__}: {flag!r} selects {m.name}'s shape and "
                        f"has no default; pass it explicitly"
                    )
                expanded.extend(d.when_true if value else d.when_false)
            dims = expanded
            if len(dims) == 1 and len(shape) != 1:
                # A flat buffer takes an operand of any rank: its one
                # dimension is the element count.
                shape = (math.prod(shape),)
            if len(shape) != len(dims):
                raise ValueError(
                    f"{cls.__name__}: operand {m.name} has rank {len(shape)} "
                    f"{shape}, declared rank {len(dims)} {m!r}"
                )
            for i, (d, n) in enumerate(zip(dims, shape)):
                if isinstance(d, DimRef):
                    bind(d, n, f"{m.name}.shape[{i}]")
                elif int(d) != n:
                    raise ValueError(
                        f"{cls.__name__}: operand {m.name}.shape[{i}] is {n}, "
                        f"declared {d}"
                    )
        return bound

    @property
    def dev(self):
        return aie_utils.ensure_current_device()

    @property
    def name(self) -> str:
        """The label of the resolved operator: its class, shown fields and device."""
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                f"{type(self).__name__}: the label names the device; none is bound"
            )
        op = self.resolved(dev)
        own = []
        for f in dataclasses.fields(op):
            v = getattr(op, f.name)
            if not f.repr or v is None:
                continue
            if isinstance(v, bool):
                v = int(v)
            elif isinstance(v, float):
                # repr() round-trips; a symbol takes neither '.' nor '-'.
                v = repr(v).replace(".", "p").replace("-", "n").replace("+", "")
            elif isinstance(v, tuple) and all(
                isinstance(x, TensorAccessPattern) for x in v
            ):
                # A gather's rows, one pattern each: too many to spell out.
                digest = hashlib.sha256(repr(v).encode()).hexdigest()[:8]
                v = f"{len(v)}p{digest}"
            elif isinstance(v, (list, tuple)):
                v = "x".join(str(x) for x in v)
            elif isinstance(v, TensorAccessPattern):
                v = (
                    f"o{v.offset}s{'x'.join(map(str, v.sizes))}"
                    f"t{'x'.join(map(str, v.strides))}"
                )
            own.append(f"{f.name}{v}")
        if any(op.finishes or (op.finish,)):
            # A step's scalars and the array's other finishes change the build too.
            keys = (tuple(link.array_key() for link in op.finish), op._finish_keys())
            digest = hashlib.sha256(repr(keys).encode()).hexdigest()[:8]
            names = "".join(type(link.op).__name__ for link in op.finish)
            own.append(f"finish{names}{digest}")
        if any(op.prepares or (op.prepare,)):
            keys = (tuple(link.array_key() for link in op.prepare), op._prepare_keys())
            digest = hashlib.sha256(repr(keys).encode()).hexdigest()[:8]
            names = "".join(type(link.op).__name__ for link in op.prepare)
            own.append(f"prepare{names}{digest}")
        return "_".join([type(self).__name__, *own, dev.name])

    def _members_io(self) -> list[_Buffer]:
        # getattr rather than vars(): array() runs this on its view.
        return [
            m
            for m in self._members
            if isinstance(m, _Buffer) and (m.when is None or getattr(self, m.when.name))
        ] + [*self._prepare_inputs, *self._finish_inputs]

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={getattr(self, f.name)!r}"
            for f in dataclasses.fields(self)
            if f.repr
        )
        return f"{type(self).__name__}({own})"
