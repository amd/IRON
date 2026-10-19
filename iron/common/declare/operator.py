# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator: mlir-aie's declaration, plus IRON's build, graph and tuning.

The parameters its cores read (``declaration.key``) configure the array,
which serves every extent; the rest reach only the runtime sequence.
"""

from __future__ import annotations

import copy
import dataclasses
import functools
import hashlib
import inspect
from collections.abc import Mapping
from contextvars import ContextVar
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Self

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.hostruntime.tensor_class import NpuTensor
from aie.utils.compile.jit import operator as jit
from aie.utils.compile.jit.operator import Unresolvable
from aie.utils.compile.jit.params import PerCallMember
from aie.utils.trace import TraceConfig
from aie.utils.verify import Tolerance, Verdict, compare

from ..testing import Testing
from .operand import Operand
from .precision import Precision
from .rtp import Rtp
from .value import Bound, ExtentWord, Value

if TYPE_CHECKING:
    from aie.helpers.taplib import Affine

    from ..graph.handle import Handle
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
        # repr() round-trips; a symbol takes no '.', '-' or '+'.
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
    """What an operator's ``build()`` made: what the array declares,
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


class Operator(jit.Operator, library=True):
    """An operator. Subclass it; each subclass's body is its declaration
    (mlir-aie's ``param()``, ``tunable()``, ``per_call()`` and aie.iron's
    ``In``/``Out``/``InOut``), read as the body finishes.

    Attributes:
        bound_values: The graph expressions bound to per-call values, by
            member name.
        pinned: The tunables its caller gave, which the tuner holds; a
            profile's and resolve()'s are starting points it may move.
    """

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

    trace: TraceConfig | None = None
    # Rebound, never updated: a copy shares its operator's dict.
    bound_values: dict[str, Affine | None] = {}
    pinned: frozenset[str] = frozenset()
    _image: OperatorImage | None = None

    def __init_subclass__(cls, image=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if image is not None:
            cls._external = image
        # mlir-aie refuses a reference-only class's build() or sequence().
        if cls.reference_only and image is not None:
            raise TypeError(f"{cls.__name__} is reference-only, so it takes no image=")
        for m in cls.declaration.per_calls if image is not None else ():
            if m.derive is None:
                raise TypeError(
                    f"{cls.__name__}.{m.name}: a shipped image takes no per-call "
                    f"value; its stream is built once per shape"
                )

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

    def __init__(
        self,
        *,
        bound_values: dict[str, Affine | None] | None = None,
        pinned: frozenset[str] | None = None,
        **given: Any,
    ) -> None:
        if bound_values:
            self.bound_values = bound_values
        super().__init__(**given)
        if pinned is None:
            pinned = frozenset(
                n for n in self.declaration.tunables if given.get(n) is not None
            )
        self.pinned = pinned
        self._check_complete()

    def _check_complete(self) -> None:
        """Run ``compatible()`` once every tunable is known, where the
        device fit is checked.
        """
        params = self.declaration.params
        if device_fit.get() and not any(
            p.tunable and vars(self)[n] is None for n, p in params.items()
        ):
            self.compatible()

    def build(self) -> Built:
        """Build the array for the bound device, on the operator as its
        cores see it (``layout()``).

        Bind every operand's lanes to fifos' shim ends, and give each core
        reading ``Value``s its runtime parameters (``Rtp``).
        """
        raise NotImplementedError(f"{type(self).__name__}.build() is not implemented")

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

    @classmethod
    def shim_columns(
        cls, dev, num_channels: int = 1, flags: Mapping[str, Any] | None = None
    ) -> int:
        """How many of ``dev``'s columns fit the class's streams in the shim DMA budget.

        A ``replicate`` stream is paid once per channel rather than per column,
        and a stream with no ``per=`` once. A ``when=`` flag ``flags`` leaves
        out is its default.

        Raises:
            Unresolvable: Not even one column's streams fit.
        """
        flags = flags or {}
        streams = [
            m
            for m in cls.declaration.operands
            if m.streamed and (m.when is None or flags.get(m.when.name, m.when.default))
        ]
        cols = dev.cols
        for drains, budget in (
            (False, dev.shim_dma_channels_in),
            (True, dev.shim_dma_channels_out),
        ):
            ours = [m for m in streams if m.drains == drains]
            lanes = [m for m in ours if m.per is not None]
            per_core = sum(not m.replicate for m in lanes) * num_channels
            once = len(ours) - len(lanes)
            shared = sum(m.replicate for m in lanes) * num_channels + once
            if per_core:
                cols = min(cols, (budget - shared) // per_core)
        if cols < 1:
            raise Unresolvable(
                f"{cls.__name__}: one column's streams exceed this device's shim DMA budget"
            )
        return cols

    @classmethod
    def call_operands(cls, args, kwargs) -> tuple[dict[str, Any], list, dict[str, Any]]:
        """Bind a call's operands as ``(x, ..., [outputs...], *, weight=None,
        ...)`` would: an optional input is a keyword, so an output is never
        taken for it.

        Returns:
            The inputs by name, in declaration order; the outputs; the other
            keywords.
        """
        ins = [m for m in cls.declaration.operands if m.fills]
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
        """Identity for sharing a build: equal keys generate byte-identical
        MLIR. A graph's bound per-call values add their names.
        """
        cls, own = super().design_key()
        if self.bound_values:
            names = {
                k: None if v is None else v.name for k, v in self.bound_values.items()
            }
            own += (("values", tuple(sorted(names.items()))),)
        return cls, own

    def resolved(self, dev=None) -> Self:
        """This operator resolved for ``dev``, the bound device unless given."""
        return super().resolved(self.dev if dev is None else dev)

    def copy(self) -> Self:
        """A fresh instance for one build, keeping resolution and bound values."""
        new = self.replace()
        new._resolved = self._resolved
        return new

    def replace(self, **changes: Any) -> Self:
        """A copy with ``changes``, which may name any parameter, the
        ``bound_values`` or the ``pinned`` tunables; checked against the
        device once complete.
        """
        bound_values = changes.pop("bound_values", self.bound_values)
        pinned = changes.pop("pinned", self.pinned)
        new = super().replace(**changes)
        new.bound_values, new.pinned = bound_values, pinned
        new._check_complete()
        return new

    def at_precision(self, level: Precision) -> Operator:
        """This operator rounding at ``level``."""
        return self._with_tunables(precision=level)

    def _with_tunables(self, **tunables: Any) -> Self:
        unknown = [n for n in tunables if n not in self.declaration.tunables]
        if unknown:
            raise TypeError(f"{type(self).__name__} has no tunable {unknown}")
        # What resolve() computes is computed again.
        fixed = {n: None for n, p in self.declaration.params.items() if not p.init}
        return self.replace(**fixed, **tunables)

    def _domains(self, dev) -> dict[str, tuple[Any, ...]]:
        """The values the tuner tries for each tunable it searches, asked of
        the resolved operator. A combination the operator cannot resolve at
        is left out by the tuner. A ``pinned`` tunable is not searched, nor
        one whose domain gives no values here.

        A fixed tuple is the resolved value's own, the resolved one first if
        it is not already there; an `Enum` is its members, the resolved one
        first (GEMM's placement: a hand-found default tried before the rest).
        """
        found = {}
        for name in self.declaration.tunables:
            domain = self.declaration.params[name].domain
            # A precision is the model's to choose (Graph.precision), not a
            # step's timing: its output is judged against the model's own.
            if name in self.pinned or domain is None or domain is Precision:
                continue
            start = vars(self)[name]
            if isinstance(domain, tuple):
                values = domain if start in domain else (start, *domain)
            elif isinstance(domain, type):
                values = (start, *(m for m in domain if m != start))
            else:
                values = domain(self, dev, start)
            if values:
                found[name] = values
        return found

    @property
    def buffers(self) -> list[Operand]:
        return [self._bound.member(m.name) for m in self._members_io()]

    @property
    def inputs(self) -> list[Operand]:
        return [b for b in self.buffers if b.fills]

    @property
    def outputs(self) -> list[Operand]:
        return [b for b in self.buffers if b.drains]

    @property
    def values(self) -> list[Value]:
        """The per-call values: each gets a device parameter."""
        return [v for v in self._value_members if v.per_call]

    @property
    def residents(self) -> dict[str, Any]:
        """What the preamble writes once per build, by name."""
        fixed = self._derived_under_bound
        out = {}
        for m in self.declaration.per_calls:
            v = self._bound.member(m.name)
            if v.derive is not None and not v.per_call:
                out[m.name] = (
                    v.derive(self) if fixed.get(m.name) is None else fixed[m.name]
                )
        return out

    @property
    def bound_extents(self) -> dict[str, Affine | None]:
        bound = self.bound_values
        return {
            m.name: bound[m.name]
            for m in self.declaration.per_calls
            if m.bounds is not None and m.name in bound
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
            if m.derive is None:
                continue
            reads: set[str] = set()
            vars(probe)["_bound"] = self._bound.recording(reads)
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
        if member is None or member.derive is None:
            raise TypeError(f"{type(self).__name__}.{name} is not a derived value")
        unknown = set(extents) - {
            m.name for m in self.declaration.per_calls if m.bounds is not None
        }
        if unknown:
            raise TypeError(
                f"{type(self).__name__} declares no extent {sorted(unknown)}"
            )
        return member.derive(self._at_extents(**extents))

    def _at_extents(self, **extents: int) -> Self:
        """A copy whose extents (``per_call(bounds=)``) read as the given numbers."""
        at = copy.copy(self)
        vars(at)["_bound"] = self._bound.at(**extents)
        return at

    def extent_unit(self, buffer: str) -> int | None:
        """The rows of ``buffer`` one lane takes at a time under a bound.

        ``None`` for the stream tile's rows; ``0`` when a bound does not shorten it.
        """
        return None

    def value(self, name: str) -> Value:
        """The device word of value ``name`` (an extent attribute reads as an integer)."""
        try:
            return self._bound.member(name)
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
        members: dict[str, Any] = {}
        for m in self.declaration.members:
            if isinstance(m, PerCallMember):
                members[m.name] = Value(
                    self,
                    m.name,
                    dtype=m.dtype,
                    derive=m.derive,
                    bounds=m.bounds,
                    words=getattr(m, "words", 1),
                )
            elif m.when is None or vars(self)[m.when.name]:
                members[m.name] = Operand(m, self)
        self._bound = Bound(self, members)
        # The values the library adds: tiles per bound operand.
        for e in self.declaration.per_calls:
            if e.bounds is None:
                continue
            for b in self.buffers:
                # Asked first: an unshortened shape may Select on a tunable.
                if b.streamed and self.extent_unit(b.name) != 0:
                    axis = b.extent_axis(e)
                    if axis is not None:
                        word = ExtentWord(self, e.name, b.name, axis)
                        dict.__setitem__(self._bound, word.name, word)

    @property
    def _value_members(self) -> list[Value]:
        """Every per-call value: the declared ones, then the library's."""
        return [v for v in dict.values(self._bound) if isinstance(v, Value)]

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
            f"{n}{spelled(vars(op)[n])}"
            for n, p in op.declaration.params.items()
            if p.repr and vars(op)[n] is not None
        ]
        return "_".join([type(self).__name__, *own, dev.name])

    def _members_io(self) -> list:
        return [
            m
            for m in self.declaration.operands
            if m.when is None or vars(self)[m.when.name]
        ]
