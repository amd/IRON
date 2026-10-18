# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator: one class declaring the array, the buffers and the sequence.

The fields its ``Array`` lists, which hold those a tile names, configure the
array, which serves every extent; the rest reach only the runtime sequence.
"""

from __future__ import annotations

import copy
import dataclasses
import functools
import hashlib
import inspect
from collections.abc import Mapping
from contextvars import ContextVar
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Self,
    dataclass_transform,
)

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.hostruntime.tensor_class import NpuTensor
from aie.utils.trace import TraceConfig
from aie.utils.verify import Tolerance, Verdict, compare

from ..testing import Testing
from .declaration import Declaration
from .domain import Domain, Width
from .field import Auto, Param, ParamSpec, Unresolvable
from .operand import Operand
from .precision import Precision
from .rtp import Rtp
from .value import Extent, ExtentWord, Value

if TYPE_CHECKING:
    from ..graph.handle import Affine, Handle
    from ..image.artifacts import Artifacts
    from ..image.standalone import OperatorImage

graph_tracer: ContextVar[Any] = ContextVar("graph_tracer", default=None)
# False while a graph's reference is traced: a reference runs shapes no
# device fits (a small model's), so compatible() is not asked.
device_fit: ContextVar[bool] = ContextVar("device_fit", default=True)


def spelled(v: Any) -> str:
    """A field's value as it may appear in a device symbol (``Operator.name``)."""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, float):
        # repr() round-trips; a symbol takes neither '.' nor '-'.
        return repr(v).replace(".", "p").replace("-", "n").replace("+", "")
    if isinstance(v, tuple) and all(isinstance(x, TensorAccessPattern) for x in v):
        # A gather's rows, one pattern each: too many to spell out.
        return f"{len(v)}p{hashlib.sha256(repr(v).encode()).hexdigest()[:8]}"
    if isinstance(v, (list, tuple)):
        return "x".join(str(x) for x in v)
    if isinstance(v, TensorAccessPattern):
        return (
            f"o{v.offset}s{'x'.join(map(str, v.sizes))}"
            f"t{'x'.join(map(str, v.strides))}"
        )
    return f"{v}"


@dataclasses.dataclass(frozen=True)
class Built:
    """What an operator's ``Array.build`` made: what the array declares,
    and the runtime parameters its cores read, which the sequence writes.

    An array whose sequence programs more of what it built keeps that on a
    subclass of its own, which ``sequence`` reads through ``rt.built``.

    Attributes:
        objects: The Workers, Flows, PacketFlows, Locks, TileDmas, Buffers
            and pinned DmaEndpoints the array declares.
        rtps: Every core's runtime parameters, one ``Rtp`` each.
    """

    objects: list
    rtps: list[Rtp] = dataclasses.field(default_factory=list)


@dataclass_transform(kw_only_default=True, frozen_default=True)
class Array:
    """The array tier of an operator, which its array is built from alone.
    Each subclass is a frozen dataclass, made so as its body finishes; the
    operator's ``Declaration`` adds every field a stream names, every field
    declared ``array=True`` and every member.

    Besides those, an ``Array`` may annotate its operands (``buffers``,
    ``inputs``, ``outputs``) and ``dev``; a property of the operator it may
    not, since what it reads would be outside the array's identity.
    """

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        dataclasses.dataclass(cls, frozen=True, kw_only=True)  # in place

    def build(self) -> Built:
        """Build the array for the bound device.

        Bind every operand's lanes to fifos' shim ends, and give each core
        reading ``Value``s its runtime parameters (``Rtp``).
        """
        raise NotImplementedError(
            f"{type(self).__qualname__}.build() is not implemented"
        )


@dataclass_transform(kw_only_default=True, field_specifiers=(Param, Auto))
@dataclasses.dataclass(eq=False, repr=True)
class Operator:
    """An operator. Subclass it; every subclass is a dataclass checked as its body finishes."""

    declaration: ClassVar[Declaration]
    Array: ClassVar[type[Array]] = Array
    _external: ClassVar[Any] = None
    test: ClassVar[Testing | None] = None
    # True when sequence() calls rt.preamble() itself, behind its first fills.
    own_preamble: ClassVar[bool] = False
    # A fused image lowers every operator's sequence under the union.
    aiecc_flags: ClassVar[tuple[str, ...]] = ()
    # Per leading operand that may be a view: the param holding its pattern
    # and the per-call value a dynamic index binds.
    accept_views: ClassVar[tuple[tuple[str, str], ...]] = ()
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
    # The tunables its caller gave, which the tuner holds; a profile's and
    # resolve()'s are starting points it may move. None until __post_init__
    # computes it from the Auto fields not None at construction, unless the
    # profile path (Tracer._construct, Profile.make) already worked that out
    # from its own pre-merge kwargs and passed it here itself.
    pinned: frozenset[str] | None = dataclasses.field(
        default=None, repr=False, compare=False, kw_only=True
    )

    def __init_subclass__(cls, image=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if image is not None:
            cls._external = image
        cls.declaration = Declaration(cls, Operator, shipped=image is not None)

    @classmethod
    def step(cls, *operands: Any, **kwargs: Any) -> Handle:
        """Record a step inside a graph's body: ``GEMV.step(w, h, **kw)``.

        Raises:
            TypeError: Called outside a graph's body.
        """
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(f"{cls.__name__}.step() is for a graph's body")
        return tracer.call(cls, operands, kwargs)

    def apply(self, *operands: Any, **values: Any) -> Handle:
        """Record a step applying this already-constructed instance, inside
        a graph's body.

        Raises:
            TypeError: Called outside a graph's body.
        """
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(f"{type(self).__name__}.apply() is for a graph's body")
        return tracer.call(self, operands, values)

    def __post_init__(self) -> None:
        # dataclass reads an init=False default through the class, where the field is.
        for f in dataclasses.fields(self):
            if not f.init and f.default is not dataclasses.MISSING:
                vars(self).setdefault(f.name, f.default)
        self._resolved = False
        self._image: OperatorImage | None = None
        self._library_values: tuple[Value, ...] = ()
        # An Enum-domain tunable (GEMM's placement) takes its own Enum
        # alone, or None (left for resolve() to fill): a string names one
        # in a profile's JSON, which Profile.load converts before it
        # reaches here.
        for name, domain in self.declaration.domains.items():
            value = vars(self)[name]
            if (
                isinstance(domain, type)
                and issubclass(domain, Enum)
                and value is not None
                and not isinstance(value, domain)
            ):
                raise TypeError(
                    f"{type(self).__name__}: {name} ({value!r}) must be a "
                    f"{domain.__name__}"
                )
        if self.pinned is None:
            self.pinned = frozenset(
                name
                for name in self.declaration.tunables
                if vars(self)[name] is not None
            )
        for name in self.declaration.autos:
            spec = ParamSpec.of(vars(type(self))[name])
            if vars(self)[name] is None and spec.default is not None:
                setattr(self, name, spec.default)
        self._derive_params()
        self.validate()
        self._bind()
        self._check_complete()

    def _check_complete(self) -> None:
        """Run ``compatible()`` once every tunable is known, where the
        device fit is checked.
        """
        if device_fit.get() and not any(
            vars(self)[n] is None for n in self.declaration.autos
        ):
            self.compatible()

    def _derive_params(self) -> None:
        for name, derive in self.declaration.derived.items():
            if vars(self)[name] is None:
                value = derive(self)
                # A T | None field's formula may answer None itself (GEMV's
                # num_matrices, following num_batches): that is the computed
                # value, not an unset one.
                if value is None and name not in self.declaration.nullable:
                    raise ValueError(
                        f"{type(self).__name__}: {name} (None) must be given: "
                        f"nothing computes it"
                    )
                setattr(self, name, value)

    def check_derived(self, *names: str) -> None:
        """Raise ``ValueError`` if a given computed-default parameter disagrees with its rule.

        Only a `Param(derive=)` field an operator's own `validate()` names
        here is held to its formula: a plain computed default (MHA's
        ``num_KV_heads``, left to default to ``num_heads``) may be
        overridden to something the formula disagrees with on purpose.
        """
        for name in names:
            given, expected = vars(self)[name], self.declaration.derived[name](self)
            if given != expected:
                raise ValueError(
                    f"{type(self).__name__}: {name} ({given!r}) must be "
                    f"{expected!r}, what its other fields make it"
                )

    def validate(self) -> None:
        """Check the sequence-tier fields on their own. Runs at construction."""

    def compatible(self) -> None:
        """Check the extents against the resolved tunables; raise ``ValueError``."""

    def resolve(self, dev) -> Self:
        """Return a copy with every ``Auto()`` filled from ``dev`` and the extents.

        Raises:
            Unresolvable: No legal value exists on ``dev``.
        """
        return dataclasses.replace(self)

    def array_config(self) -> Array:
        """This operator's ``Array``: what its array is built from, read off
        the operator by the names the ``Array`` declares. A member absent
        on this instance (``when=`` False) is None.
        """
        array = type(self).Array
        members = {m.name for m in self.declaration.members}
        return array(
            **{
                f.name: (
                    self._bound.get(f.name)
                    if f.name in members
                    else getattr(self, f.name)
                )
                for f in dataclasses.fields(array)
            }
        )

    def tolerance(self) -> Tolerance | None:
        """What each output of the resolved operator is judged by; None where
        nothing bounds it, which check mode refuses.
        """
        return None

    def ops(self) -> int:
        """The arithmetic operations one call performs, for its throughput."""
        return sum(b.elements for b in self.outputs)

    def array_device(self):
        """The device the array's Program is built for: the bound device
        unless the array takes a part of it.
        """
        return self.dev

    @property
    def external(self):
        return type(self)._external

    def xclbin_operator(self) -> Self:
        """The operator whose xclbin this one runs when it runs alone."""
        return self

    def exported_design(self):
        """The design another tool exports for this operator; ``None`` derives it."""
        return None

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        allowed = self.declaration.shim_columns(dev, num_channels, vars(self))
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
        budget = self.declaration.shim_columns(dev, num_channels, vars(self))
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

    def _call_reference(
        self,
        inputs: Mapping[str, np.ndarray],
        outputs: Mapping[str, np.ndarray] | None = None,
        values: Mapping[str, Any] | None = None,
    ) -> dict[str, np.ndarray]:
        """Run `reference` on buffers by name, returning each written one's
        result by name: the inputs positional, in declaration order, and an
        output or a per-call value it names a parameter after given to it.

        Raises:
            ValueError: `inputs` are not this operator's, `outputs` name a
                buffer that is not its output, or the reference returns
                another number of results than this operator writes, or None
                for one.
        """
        name = type(self).__name__
        declared = [b.name for b in self.inputs]
        if sorted(inputs) != sorted(declared):
            raise ValueError(
                f"{name} takes the inputs {declared}, not {sorted(inputs)}"
            )
        outputs = outputs or {}
        unknown = set(outputs) - {b.name for b in self.outputs}
        if unknown:
            raise ValueError(f"{name} has no output {sorted(unknown)}")
        named = inspect.signature(self.reference).parameters
        result = self.reference(
            *(inputs[n] for n in declared),
            **{k: v for k, v in outputs.items() if k in named},
            **{k: v for k, v in (values or {}).items() if k in named and v is not None},
        )
        results = result if isinstance(result, tuple) else (result,)
        written = [b.name for b in self.outputs]
        if len(results) != len(written) or any(r is None for r in results):
            raise ValueError(
                f"{name}.reference returned {results!r:.80} for {written}; "
                f"it returns each buffer it writes, an output written in place "
                f"among them"
            )
        return dict(zip(written, results))

    def judge(
        self,
        inputs: Mapping[str, np.ndarray],
        written: Mapping[str, np.ndarray],
        tolerance: Tolerance,
        expected: Mapping[str, np.ndarray] | None = None,
    ) -> dict[str, Verdict]:
        """Each buffer this operator writes held to its reference result.

        Args:
            inputs: The inputs it was given, by buffer name; a bound
                tolerance is evaluated on them, in declaration order.
            written: What it wrote to each buffer it writes, by buffer name.
            tolerance: What every written buffer is judged by.
            expected: Each written buffer's reference result, by buffer
                name; `_call_reference` on `inputs` where None.

        Returns:
            Each written buffer's verdict, by buffer name.

        Raises:
            ValueError: `written` or `expected` do not name every buffer this
                operator writes and no other, an expected result is None, or
                a written buffer holds another number of elements than its
                result.
        """
        if expected is None:
            expected = self._call_reference(inputs)
        names = [b.name for b in self.outputs]
        for given, what in ((written, "written"), (expected, "expected")):
            if sorted(given) != sorted(names):
                raise ValueError(
                    f"{type(self).__name__} writes {names}; the {what} "
                    f"buffers are {sorted(given)}"
                )
        unknown = [n for n in names if expected[n] is None]
        if unknown:
            raise ValueError(f"{type(self).__name__}: no expected result for {unknown}")
        bound = None
        if tolerance.kind == "bound":
            bound = tolerance.bound(*(inputs[b.name] for b in self.inputs))
        return {
            n: compare(
                np.reshape(written[n], np.shape(expected[n])),
                expected[n],
                tolerance,
                bound=bound,
            )
            for n in names
        }

    def sequence(self, rt) -> None:
        """Override to write the runtime sequence by hand; otherwise it is derived."""
        raise NotImplementedError

    @classmethod
    def has_sequence_override(cls) -> bool:
        return cls.sequence is not Operator.sequence

    def design_key(self):
        """Identity for sharing a build: equal keys generate byte-identical MLIR.

        An Enum field (GEMM's placement) is its own value, not the member:
        a rename must not move a design's key.
        """
        own = tuple(
            (f.name, v.value if isinstance(v := vars(self)[f.name], Enum) else v)
            for f in dataclasses.fields(self)
            if f.compare
        )
        if self.bound_values:
            names = {
                k: None if v is None else v.name for k, v in self.bound_values.items()
            }
            own += (("values", tuple(sorted(names.items()))),)
        return (type(self), own)

    def _probed(self) -> Self:
        """This operator with each ``Param(probe=)`` field at its probe: the
        one its step time is measured as, for every value of those fields.
        Itself when they are there already, unresolved otherwise.
        """
        if all(vars(self)[n] == v for n, v in self.declaration.probes.items()):
            return self
        return dataclasses.replace(self, **self.declaration.probes)

    def array_key(self):
        key = (type(self),) + tuple(
            (name, v.value if isinstance(v := vars(self)[name], Enum) else v)
            for name in self.declaration.array
        )
        if self.trace is not None:
            key += (("trace", self.trace),)
        return key

    def resolved(self, dev=None) -> Self:
        """This operator resolved for ``dev`` (the bound device unless given),
        checked. ``dev`` is bound while it resolves, so what the operator's
        operands read of the device (``Operand.split``) is ``dev``'s.
        """
        if self._resolved:
            return self
        if dev is None:
            dev = self.dev
        with aie_utils.set_current_device(dev):
            new = self.resolve(dev)
            if new is self:
                raise TypeError(
                    f"{type(self).__name__}.resolve() must return a copy, "
                    f"dataclasses.replace(self, ...), not self"
                )
            if not isinstance(new, type(self)):
                raise TypeError(
                    f"{type(self).__name__}.resolve() must return a {type(self).__name__}"
                )
            missing = [n for n in self.declaration.autos if vars(new)[n] is None]
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
        new = self.replace()
        new._resolved = self._resolved
        return new

    def replace(self, **changes: Any) -> Self:
        """``dataclasses.replace`` that also takes and keeps the ``init=False``
        fields, which it would refuse and reset: what ``resolve`` returns,
        ``self.replace(tile=..., derived=...)``.
        """
        fixed = {
            f.name: changes.pop(f.name, vars(self)[f.name])
            for f in dataclasses.fields(self)
            if not f.init
        }
        new = dataclasses.replace(self, **changes)
        vars(new).update(fixed)
        new._bind()
        new._check_complete()
        return new

    def _with_tunables(self, **tunables: Any) -> Self:
        unknown = [n for n in tunables if n not in self.declaration.tunables]
        if unknown:
            raise TypeError(f"{type(self).__name__} has no tunable {unknown}")
        return dataclasses.replace(self, **tunables)

    @property
    def _widths(self) -> dict[str, int | None]:
        """The tunables searched as a `Width`, and their values: those that
        declare one, and those a streamed ``per=`` names that declare no
        other domain.
        """
        found = {
            n: vars(self)[n]
            for n, domain in self.declaration.domains.items()
            if isinstance(domain, Width)
        }
        for b in self.buffers:
            for ref in b.per.dims if b.streamed and b.per else ():
                if (
                    ParamSpec.of(ref) is not None
                    and ref.name in self.declaration.tunables
                    and ref.name not in self.declaration.domains
                ):
                    found.setdefault(ref.name, vars(self)[ref.name])
        return found

    def _domains(self, dev) -> dict[str, tuple[Any, ...]]:
        """The values the tuner tries for each tunable it searches, asked of
        the resolved operator: the field's declared domain where its
        ``when`` flag holds, a `Width` for one of `widths`, and nothing for
        any other. A combination the operator cannot resolve at is left
        out by the tuner. A ``pinned`` tunable is not searched.

        A fixed tuple is the resolved value's own, the resolved one first if
        it is not already there; an `Enum`-annotated field with no domain is
        searched over that `Enum`'s members, the resolved one first (GEMM's
        placement: a hand-found default tried before the rest).
        """
        widths = self._widths
        found = {}
        for name in dict.fromkeys([*widths, *self.declaration.tunables]):
            domain = self.declaration.domains.get(
                name, Width() if name in widths else None
            )
            # A precision is the model's to choose (Graph.precision), not a
            # step's timing: its output is judged against the model's own.
            if name in self.pinned or domain is None or domain is Precision:
                continue
            when = domain.when if isinstance(domain, Domain) else None
            if when is not None and not when(self, dev):
                continue
            start = vars(self)[name]
            if isinstance(domain, tuple):
                found[name] = domain if start in domain else (start, *domain)
            elif isinstance(domain, type):  # an Enum, auto-detected
                found[name] = (start, *(m for m in domain if m != start))
            else:
                found[name] = domain.values(self, dev, start)
        return found

    @property
    def buffers(self) -> list[Operand]:
        return [self._bound[m.name] for m in self._members_io()]

    @property
    def inputs(self) -> list[Operand]:
        return [b for b in self.buffers if b.fills]

    @property
    def outputs(self) -> list[Operand]:
        return [b for b in self.buffers if b.drains]

    @property
    def values(self) -> list[Value]:
        """The per-call values: each gets a device parameter."""
        values = [self._bound[m.name] for m in self._value_members]
        return [v for v in values if v.per_call]

    @property
    def residents(self) -> dict[str, Any]:
        """What the preamble writes once per build, by name."""
        fixed = self._derived_under_bound
        return {
            m.name: m.derive(self) if fixed.get(m.name) is None else fixed[m.name]
            for m in self.declaration.members
            if isinstance(m, Value)
            and m.derive is not None
            and not self._bound[m.name].per_call
        }

    @property
    def bound_extents(self) -> dict[str, Affine | None]:
        bound = self.bound_values
        return {
            m.name: bound[m.name]
            for m in self.declaration.members
            if isinstance(m, Extent) and m.name in bound
        }

    def _per_call_derived(self) -> frozenset[str]:
        return frozenset(k for k, v in self._derived_under_bound.items() if v is None)

    @functools.cached_property
    def _derived_under_bound(self) -> dict[str, int | None]:
        """Each derived value that reads a bound extent: the number it is at
        every bound (``n - n``, ``(4 * n) // n``), or None where it follows
        the call. Kept per instance: ``use_value`` forgets it, and every
        other change makes a new instance.
        """
        bound = self.bound_extents
        if not bound:
            return {}
        op = self
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
            except (TypeError, ValueError, AttributeError):
                pass  # unresolved: what it read before failing still counts
            if not reads & bound.keys():
                continue
            out[m.name] = None
            if forms is None:
                continue
            try:
                got = op.derived_at(m.name, **forms)
            except (TypeError, ValueError, AttributeError):
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
            m.name for m in self.declaration.members if isinstance(m, Extent)
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

    def value(self, name: str) -> Value:
        """The device word of value ``name`` (an ``Extent`` attribute reads as an integer)."""
        try:
            return self._bound[name]
        except KeyError:
            raise TypeError(
                f"{type(self).__name__} declares no value {name!r}"
            ) from None

    def use_value(self, name: str, bound_to: Affine | None = None) -> None:
        """Record that a graph binds the per-call value ``name`` to its expression ``bound_to``."""
        if not any(m.name == name for m in self._value_members):
            raise TypeError(
                f"{type(self).__name__} declares no per-call value {name!r}"
            )
        # Rebound, not updated: replace() hands a copy the same dict.
        self.bound_values = {**self.bound_values, name: bound_to}
        vars(self).pop("_derived_under_bound", None)

    def compile(self) -> Artifacts:
        """Build the image this operator runs on outside a graph, once.

        Returns:
            What the build produced: the xclbin, the instruction stream and
            the cache entry holding them.
        """
        if self._image is None:
            # The image layer builds on this one: imported here to break the cycle.
            from ..image.standalone import OperatorImage

            self._image = OperatorImage(self)
        return self._image.compile().artifacts

    def __call__(self, *args, **kwargs):
        """A run of this operator's own image (``compile``) on device
        tensors, one per declared buffer in declaration order, ``kwargs``
        its ``DispatchTime`` values by device symbol. Inside a graph's body,
        call ``op.apply(*operands, **values)`` instead.
        """
        if graph_tracer.get() is not None:
            raise TypeError(
                f"{type(self).__name__} instance called inside a graph's "
                f"body; use op.apply(*operands, **values)"
            )
        names = [b.name for b in self.buffers]
        if len(args) != len(names) or not all(isinstance(a, NpuTensor) for a in args):
            raise TypeError(
                f"{type(self).__name__} runs outside a graph's body on device "
                f"tensors, one per declared buffer {names}; got "
                f"{[type(a).__name__ for a in args]}"
            )
        self.compile()
        return self._image(*args, **kwargs)

    def _bind(self) -> None:
        vars(self).pop("_derived_under_bound", None)
        bound: dict[str, Any] = {}
        for m in self._members_io():
            bound[m.name] = m.of(self)
        for m in self.declaration.members:
            if isinstance(m, Value):
                bound[m.name] = m.of(self)
        self._bound = bound
        # The values the library adds: tiles per bound operand.
        words: list[Value] = []
        for e in self.declaration.members:
            if not isinstance(e, Extent):
                continue
            for b in self._members_io():
                # Asked first: an unshortened shape may Select on an Auto() field.
                if b.obj_dims is not None and self.extent_unit(b.name) != 0:
                    axis = bound[b.name].extent_axis(e)
                    if axis is not None:
                        words.append(ExtentWord(type(self), e, b.name, axis))
        for word in words:
            bound[word.name] = word.of(self)
        self._library_values = tuple(words)

    @property
    def _value_members(self) -> list[Value]:
        own = [m for m in self.declaration.members if isinstance(m, Value)]
        return own + list(self._library_values)

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
        own = [
            f"{f.name}{spelled(vars(op)[f.name])}"
            for f in dataclasses.fields(op)
            if f.repr and vars(op)[f.name] is not None
        ]
        return "_".join([type(self).__name__, *own, dev.name])

    def _members_io(self) -> list[Operand]:
        return [
            m
            for m in self.declaration.members
            if isinstance(m, Operand) and (m.when is None or vars(self)[m.when.name])
        ]

    def __repr__(self) -> str:
        own = ", ".join(
            f"{f.name}={vars(self)[f.name]!r}"
            for f in dataclasses.fields(self)
            if f.repr
        )
        return f"{type(self).__name__}({own})"
