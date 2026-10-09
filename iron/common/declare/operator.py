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
from collections.abc import Mapping
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
from .field import DimRef, OptionalDim, Select, Tier, Unresolvable, param
from .member import (
    DispatchTime,
    Extent,
    Value,
    _Buffer,
    _Member,
    _Value,
    present,
)
from .profile import Profile

if TYPE_CHECKING:
    from ..graph.handle import Affine, Handle

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
    _array_fields: ClassVar[tuple[str, ...]] = ()
    _external: ClassVar[Any] = None
    test: ClassVar[Testing | None] = None
    # True when sequence() calls rt.preamble() itself, behind its first fills.
    own_preamble: ClassVar[bool] = False
    # A fused image lowers every operator's sequence under the union.
    aiecc_flags: ClassVar[tuple[str, ...]] = ()
    # What a call on a view gathered by a graph input (``Copy(table[ids])``)
    # becomes: the class, built with ``rows``, ``table_rows``, ``row`` and
    # ``dtype``, and ``control_words(ids, address)`` encoding each call's ids.
    per_call_gather: ClassVar[type[Operator] | None] = None

    trace: TraceConfig | None = dataclasses.field(
        default=None, repr=False, kw_only=True
    )
    # The graph expressions bound to per-call values, by member name;
    # design_key adds their names, since a dict does not hash.
    bound_values: dict[str, Affine | None] = dataclasses.field(
        default_factory=dict, repr=False, compare=False, kw_only=True
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

    # -- declared surface --------------------------------------------------

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

    def ops(self) -> int:
        """The arithmetic operations one call performs, for its throughput."""
        return sum(b.elements for b in self.outputs)

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
        cls, dev, num_channels: int = 1, flags: Mapping[str, Any] | None = None
    ) -> int:
        """How many of ``dev``'s columns fit this operator's streams in the shim DMA budget.

        A ``replicate`` stream is paid once per channel rather than per column,
        a ``broadcast`` one once.
        """
        streams = [
            m
            for m in cls._members
            if isinstance(m, _Buffer) and m.tile is not None and present(m, flags or {})
        ]
        cols = dev.cols
        for drains, budget in (
            (False, dev.shim_dma_channels_in),
            (True, dev.shim_dma_channels_out),
        ):
            ours = [m for m in streams if m.direction.drains == drains]
            per_core = (
                sum(not (m.replicate or m.broadcast) for m in ours) * num_channels
            )
            shared = sum(m.replicate for m in ours) * num_channels
            shared += sum(m.broadcast for m in ours)
            if per_core:
                cols = min(cols, (budget - shared) // per_core)
        return max(1, cols)

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        allowed = self.shim_columns(dev, num_channels, vars(self))
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
        budget = self.shim_columns(dev, num_channels, vars(self))
        return next((c for c in range(budget, 0, -1) if fits is None or fits(c)), 1)

    def addressed_inputs(
        self, addresses: Mapping[str, int], rng: np.random.Generator
    ) -> dict[str, np.ndarray]:
        """What the inputs that name device addresses hold, for a run alone.

        Random bytes in such an input would steer the operator's DMA
        anywhere; every other input is safe to fill at random.

        Args:
            addresses: Each of the operator's buffers' device addresses, by
                buffer name.
            rng: The generator any representative content is drawn from.

        Returns:
            Each such input's content, by buffer name.
        """
        return {}

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

    # -- library surface ---------------------------------------------------

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
            names = {
                k: None if v is None else v.name for k, v in self.bound_values.items()
            }
            own += (("values", tuple(sorted(names.items()))),)
        return (type(self).__qualname__, own)

    def array_key(self):
        return (type(self).__qualname__,) + tuple(
            (name, getattr(self, name)) for name in self._array_fields
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
        new.validate()
        new.compatible()
        new._resolved = True
        return new

    def copy(self) -> Self:
        """A fresh instance for one build, keeping resolution and bound values."""
        new = dataclasses.replace(self)
        new._resolved = self._resolved
        if self._resolved:
            # replace() resets the init=False fields compatible() records.
            new.compatible()
        return new

    def with_tunables(self, **tunables: Any) -> Self:
        """This operator, unresolved, with the given ``auto()`` fields set."""
        unknown = [n for n in tunables if n not in self._auto_fields]
        if unknown:
            raise TypeError(f"{type(self).__name__} has no tunable {unknown}")
        return dataclasses.replace(self, **tunables)

    @property
    def widths(self) -> dict[str, int | None]:
        """The settable tunables a ``per=`` stream's count is a product of, and their values."""
        settable = {
            f.name: getattr(self, f.name)
            for f in dataclasses.fields(self)
            if f.init and f.name in self._auto_fields
        }
        found: dict[str, int | None] = {}
        for b in self.buffers:
            for ref in b.member.per.dims if b.streamed and b.member.per else ():
                if isinstance(ref, DimRef) and ref.name in settable:
                    found.setdefault(ref.name, settable[ref.name])
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
    def values(self) -> list[BoundValue]:
        return [
            self._bound[m.name] for m in self._value_members if self.uses_value(m.name)
        ]

    @property
    def residents(self) -> dict[str, Any]:
        """What the preamble writes once per build, by name."""
        fixed = self._derived_under_bound()
        return {
            m.name: m.derive(self) if fixed.get(m.name) is None else fixed[m.name]
            for m in self._members
            if isinstance(m, Value)
            and m.derive is not None
            and not self.uses_value(m.name)
        }

    def uses_value(self, name: str) -> bool:
        """Whether this instance drives the per-call value ``name``; unused ones get no parameter."""
        member = next((m for m in self._value_members if m.name == name), None)
        if isinstance(member, Extent):
            return name in self.bound_values
        if isinstance(member, Value) and member.derive is not None:
            return name in self.bound_values or name in self._per_call_derived()
        return True

    @property
    def bound_extents(self) -> dict[str, Affine | None]:
        bound = self.bound_values
        return {
            m.name: bound[m.name]
            for m in self._members
            if isinstance(m, Extent) and m.name in bound
        }

    def _per_call_derived(self) -> frozenset[str]:
        return frozenset(k for k, v in self._derived_under_bound().items() if v is None)

    def _derived_under_bound(self) -> dict[str, int | None]:
        """Each derived value that reads a bound extent: the number it is at
        every bound (``n - n``, ``(4 * n) // n``), or None where it follows
        the call.
        """
        bound = self.bound_extents
        if not bound:
            return {}
        # From array(), derivations run on the operator: reading an extent here is not the array's.
        op = object.__getattribute__(self, "_op") if type(self) is _ArrayView else self
        probe = copy.copy(op)
        forms = None if None in bound.values() else bound
        out: dict[str, int | None] = {}
        for m in self._value_members:
            if not (isinstance(m, Value) and m.derive is not None):
                continue
            reads: set[str] = set()
            vars(probe)["_extent_reads"] = reads
            try:
                m.derive(probe)
            except Exception:
                pass  # unresolved: what it read before failing still counts
            if not reads & bound.keys():
                continue
            out[m.name] = None
            if forms is None:
                continue
            try:
                got = op.derived_at(m.name, **forms)
            except Exception:
                continue  # no form, or unresolved: per call either way
            if isinstance(got, (int, np.integer)) and not isinstance(got, bool):
                out[m.name] = int(got)
        return out

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

    def use_value(self, name: str, bound_to: Affine | None = None) -> None:
        """Record that a graph binds the per-call value ``name`` to its expression ``bound_to``."""
        if not any(isinstance(m, _Value) and m.name == name for m in self._members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        # Rebound, not updated: replace() hands a copy the same dict.
        self.bound_values = {**self.bound_values, name: bound_to}

    # -- graphs ---------------------------------------------------------

    def __call__(self, *args, **kwargs):
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(
                f"{type(self).__name__} instances are called on graph handles inside "
                f"a graph's body; outside one, run it as an OperatorImage"
            )
        return tracer.call(self, args, kwargs)

    def _bind(self) -> None:
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

    @property
    def _value_members(self) -> list[_Value]:
        return [m for m in self._members if isinstance(m, _Value)] + list(
            self.__dict__.get("_extent_words", ())
        )

    # -- construction from operand shapes ----------------------------------

    @classmethod
    def from_operands(cls, *operand_shapes, **overrides) -> Self:
        """Construct from operand shapes, an optional input's by keyword."""
        inputs, outputs, overrides = cls.call_operands(operand_shapes, overrides)
        return cls(**{**overrides, **cls.infer(inputs, outputs, **overrides)})

    @classmethod
    def call_operands(cls, args, kwargs) -> tuple[dict[str, Any], list, dict[str, Any]]:
        """Bind a call's operands to the declared ones, as a signature
        ``(x, ..., [outputs...], *, weight=None, ...)`` would.

        The positional operands are the required inputs, in declaration
        order, then any outputs; an optional input (``when=`` a flag) is a
        keyword, its name, so an output is never taken for it.

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

    # -- the device and the label ---------------------------------------------

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
        return "_".join([type(self).__name__, *own, dev.name])

    def _members_io(self) -> list[_Buffer]:
        # getattr rather than vars(): array() runs this on its view.
        return [
            m
            for m in self._members
            if isinstance(m, _Buffer) and (m.when is None or getattr(self, m.when.name))
        ]

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={getattr(self, f.name)!r}"
            for f in dataclasses.fields(self)
            if f.repr
        )
        return f"{type(self).__name__}({own})"

    def explain(self) -> str:
        """What a build of this operator compiles in and what it takes per call."""
        fields = {
            f.name: getattr(self, f.name)
            for f in dataclasses.fields(self)
            if f.compare and Tier in f.metadata
        }

        def spell(names):
            return ", ".join(f"{n}={fields[n]!r}" for n in names) or "nothing"

        array = [n for n in fields if n in self._array_fields]
        sequence = [n for n in fields if n not in self._array_fields]
        lines = [
            repr(self) + (" (resolved)" if self._resolved else " (unresolved)"),
            f"  array, compiled into every core: {spell(array)}",
            f"  sequence, the host's alone: {spell(sequence)}",
        ]
        per_call_derived = self._per_call_derived()
        for m in self._value_members:
            if isinstance(m, _ExtentWord) and m.name not in per_call_derived:
                continue
            if isinstance(m, Extent):
                bound = self.bound_extents.get(m.name)
                how = (
                    f"per call, bounds {m.field.name} (graph value {bound})"
                    if m.name in self.bound_extents
                    else f"{m.field.name}, unbounded"
                )
            elif (
                isinstance(m, Value)
                and m.name in per_call_derived
                and m.name not in self.bound_values
            ):
                how = "per call, derived from a bounded extent"
            elif (
                isinstance(m, Value)
                and m.derive is not None
                and not self.uses_value(m.name)
            ):
                given = f", {self.residents[m.name]!r} here" if self._resolved else ""
                how = "written once per build" + given
            elif self.uses_value(m.name):
                how = "per call, " + (
                    "the instruction stream regenerated around it"
                    if isinstance(m, DispatchTime)
                    else "a scratchpad word patched or read"
                )
            else:
                how = "unused here"
            lines.append(f"  {m.name}: {how}")
        if self.trace is not None:
            lines.append(f"  traced: {self.trace.trace_size} bytes of trace buffer")
        return "\n".join(lines)
