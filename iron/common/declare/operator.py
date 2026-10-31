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
from enum import Enum
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Self, cast

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.compile.jit import operator as jit
from aie.utils.compile.jit.operator import Unresolvable
from aie.utils.compile.jit.params import PerCallMember, Select
from aie.utils.hostruntime.tensor_class import NpuTensor
from aie.utils.trace import TraceConfig
from aie.utils.verify import Tolerance, Verdict, compare

from ..testing import Testing
from .operand import Operand
from .rtp import Rtp
from .value import ExtentWord, Value

if TYPE_CHECKING:
    from aie.helpers.taplib import Affine
    from aie.iron.device import Device

    from ..graph.handle import Handle
    from ..image.artifacts import Artifacts
    from ..image.standalone import OperatorImage

graph_recorder: ContextVar[Any] = ContextVar("graph_recorder", default=None)
# False while a graph's reference is recorded: a reference runs shapes no
# device fits (a small model's), so compatible() is not asked.
device_fit: ContextVar[bool] = ContextVar("device_fit", default=True)


def spelled(v: Any) -> str:
    """Return a field's value as it appears in a device symbol (``Operator.name``)."""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, float):
        # repr() round-trips; a symbol takes no '.', '-' or '+'.
        return repr(v).replace(".", "p").replace("-", "n").replace("+", "")
    if isinstance(v, tuple) and all(isinstance(x, TensorAccessPattern) for x in v):
        # A gather's rows, one pattern each: too many to spell out.
        return f"{len(v)}p{hashlib.sha256(repr(v).encode()).hexdigest()[:8]}"
    if isinstance(v, (list, tuple)):
        return "x".join(spelled(x) for x in v)
    if isinstance(v, type):
        return v.__name__
    if dataclasses.is_dataclass(v):
        return type(v).__name__ + "".join(
            f"{f.name}{spelled(vars(v)[f.name])}" for f in dataclasses.fields(v)
        )
    if isinstance(v, TensorAccessPattern):
        return (
            f"o{v.offset}s{'x'.join(map(str, v.sizes))}"
            f"t{'x'.join(map(str, v.strides))}"
        )
    return f"{v}"


@dataclasses.dataclass(frozen=True)
class Built:
    """What ``build()`` made: the array's objects and each core's ``Rtp``.

    The objects are what the array declares (Workers, Flows, PacketFlows,
    Locks, TileDmas, Buffers, pinned DmaEndpoints). A ``sequence`` needing
    more reads a subclass via ``rt.built``.
    """

    objects: list
    rtps: list[Rtp] = dataclasses.field(default_factory=list)


class Operator(jit.Operator, library=True):
    """An operator, whose subclass body is its declaration.

    The declaration is mlir-aie's ``param()``, ``tunable()``, ``per_call()``;
    aie.iron's ``In``/``Out``/``InOut``.

    Attributes:
        bound_values: The graph expression bound to each per-call value, by name.
        pinned: The tunables its caller gave, which the tuner holds; it may
            move a profile's and ``resolve()``'s.
    """

    _external: ClassVar[Any] = None
    test: ClassVar[Testing | None] = None
    # True when sequence() calls rt.preamble() itself, behind its first fills.
    own_preamble: ClassVar[bool] = False
    # A full ELF lowers every operator's sequence under the union.
    aiecc_flags: ClassVar[tuple[str, ...]] = ()
    # Per leading operand that may be a view: the param holding its pattern
    # and the per-call value a dynamic index binds.
    accept_views: ClassVar[tuple[tuple[str, str], ...]] = ()

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
        recorder = graph_recorder.get()
        if recorder is None:
            raise TypeError(f"{cls.__name__}.step() is for a graph's body")
        return recorder.call(cls, operands, kwargs)

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
        """Run ``compatible()`` once every tunable is known.

        The device fit is checked there.
        """
        params = self.declaration.params
        if device_fit.get() and not any(
            p.tunable and vars(self)[n] is None for n, p in params.items()
        ):
            self.compatible()

    def build(self) -> Built:
        """Build the array for the bound device on ``layout()``.

        Bind every operand's lanes to fifo ends and give each core reading
        ``Value``s an ``Rtp``.
        """
        raise NotImplementedError(f"{type(self).__name__}.build() is not implemented")

    def fold(self, consumer: Self, at: int) -> Self | None:
        """This operator with ``consumer`` finishing its output tile in its
        own cores: ``consumer``'s kernel runs there before the tile leaves
        L1, input ``at`` the tile and its others new streams of this
        operator's. None where this operator does not finish others, or
        not this one.
        """
        return None

    def tolerance(self) -> Tolerance | None:
        """Return what each output of the resolved operator is judged by.

        None where nothing bounds it, which check mode refuses.
        """
        return None

    def ops(self) -> int:
        """Return the arithmetic operations one call performs, for its throughput."""
        return sum(b.elements for b in self.outputs)

    def array_device(self):
        """Return the device the array's Program is built for.

        The bound device unless the array takes a part of it.
        """
        return self.dev

    @property
    def external(self):
        return type(self)._external

    def xclbin_operator(self) -> Self:
        """Return the operator whose xclbin this one runs when it runs alone."""
        return self

    def exported_design(self) -> Callable[..., Any] | None:
        """Return another tool's design for this operator; ``None`` derives it."""
        return None

    @classmethod
    def shim_columns(
        cls, dev, num_channels: int = 1, flags: Mapping[str, Any] | None = None
    ) -> int:
        """How many of ``dev``'s columns fit the class's streams in the shim DMA
        budget: a ``replicate`` stream costs once per channel, one with no
        ``per=`` once, and a ``when=`` flag, or an obj_shape ``Select``'s,
        ``flags`` leaves out is its default.

        Raises:
            Unresolvable: Not even one column's streams fit.
        """
        flags = flags or {}
        streams = [
            m
            for m in cls.declaration.operands
            if m.streamed
            and (m.when is None or flags.get(m.when.name, m.when.default))
            and not any(
                isinstance(d, Select)
                and (
                    d.when_true
                    if flags.get(d.flag.name, d.flag.default)
                    else d.when_false
                )
                is None
                for d in m.obj_dims
            )
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
        """Split a call into inputs by name, outputs and other keywords.

        As ``(x, ..., [outputs...], *, weight=None, ...)`` would: inputs are
        in declaration order, and an optional input is a keyword, so never
        taken for an output.
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
        self,
        addresses: Mapping[str, int],
        rng: np.random.Generator,
        values: Mapping[str, int],
    ) -> dict[str, np.ndarray]:
        """For a run alone, the content of each input that names device
        ``addresses`` (every buffer's, by name), by buffer name: random bytes
        there would steer the DMA anywhere. Other inputs are filled at random.

        Args:
            values: The call's per-call values by member name; an input built
                from a bound (``valid_rows``) must follow it, as the call does.
        """
        return {}

    def reference(self, *inputs: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{type(self).__name__}.reference() is not implemented"
        )

    def _call_reference(
        self,
        inputs: Mapping[str, np.ndarray],
        outputs: Mapping[str, np.ndarray] | None = None,
        values: Mapping[str, Any] | None = None,
    ) -> dict[str, np.ndarray]:
        """Run ``reference`` on buffers by name, returning each written one's result.

        Inputs are positional in declaration order, an output or per-call
        value a keyword where it names a parameter.

        Raises:
            ValueError: The inputs or outputs are not this operator's, or the
                reference does not return one non-None result per written buffer.
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
        """Each written buffer's verdict against its reference result.

        Every mapping is by buffer name. ``expected`` defaults to
        ``reference`` on ``inputs``, which a bound tolerance is also
        evaluated on.

        Raises:
            ValueError: ``written`` or ``expected`` name other buffers than it
                writes, an expected result is None, or a written buffer's
                element count differs from its result's.
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
            assert tolerance.bound is not None, "kind == 'bound' iff bound is set"
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

    def lane_transfers(
        self, operand: Operand
    ) -> list[tuple[int, TensorAccessPattern, Value | None, int | None]] | None:
        """``operand``'s per-lane host access order, where ``sequence(rt)`` is
        hand-written and the derived order does not hold: ``Operand.transfers()``'s
        own ``(lane, tap, length_parameter, length_unit)`` tuples, one lane at
        a time. None where this operator does not describe ``operand``
        (``transfers()`` then falls back to the derived order, or raises).

        A lane whose bound start is not static, or whose ``length_parameter``
        does not reach ``Operand.transfers()``'s own round-robin axis, is
        also not describable here; return None for it too.
        """
        return None

    def design_key(self):
        """Identity for sharing a build: equal keys generate byte-identical MLIR.

        A graph's bound per-call values add their names.
        """
        cls, own = super().design_key()
        if self.bound_values:
            names = {
                k: None if v is None else v.name for k, v in self.bound_values.items()
            }
            own += (("values", tuple(sorted(names.items()))),)
        return cls, own

    def resolved(self, dev: Device | None = None) -> Self:
        """Return this operator resolved for ``dev``, the bound device unless given."""
        dev = self.dev if dev is None else dev
        if dev is None:
            raise Unresolvable(
                f"{type(self).__name__}: resolved() needs a device; none is bound"
            )
        return super().resolved(dev)

    def replace(self, **changes: Any) -> Self:
        """Return a copy with ``changes``, checked against the device once complete.

        ``changes`` may name any parameter, the ``bound_values`` or the
        ``pinned`` tunables.
        """
        bound_values = changes.pop("bound_values", self.bound_values)
        pinned = changes.pop("pinned", self.pinned)
        new = super().replace(**changes)
        new.bound_values, new.pinned = bound_values, pinned
        new._check_complete()
        return new

    def _with_tunables(self, **tunables: Any) -> Self:
        unknown = [n for n in tunables if n not in self.declaration.tunables]
        if unknown:
            raise TypeError(f"{type(self).__name__} has no tunable {unknown}")
        # What resolve() computes is computed again.
        fixed = {n: None for n, p in self.declaration.params.items() if not p.init}
        return self.replace(**fixed, **tunables)

    def _domains(self, dev) -> dict[str, tuple[Any, ...]]:
        """Return the values the tuner tries per searched tunable.

        Asked of the resolved operator; skips ``pinned`` tunables and one
        whose domain is empty here. A tuple gains the resolved value in
        front if missing; an ``Enum`` puts it first.
        """
        found = {}
        for name in self.declaration.tunables:
            domain = self.declaration.params[name].domain
            if name in self.pinned or domain is None:
                continue
            start = vars(self)[name]
            if isinstance(domain, tuple):
                values = domain if start in domain else (start, *domain)
            elif isinstance(domain, type) and issubclass(domain, Enum):
                values = (start, *(m for m in domain if m != start))
            else:
                values = domain(self, dev, start)
            if values:
                found[name] = values
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
        return [v for v in self._value_members if v.per_call]

    @property
    def residents(self) -> dict[str, Any]:
        """What the preamble writes once per build, by name."""
        fixed = self._derived_under_bound
        out = {}
        for m in self.declaration.per_calls:
            v = self._values[m.name]
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
        """Each derived value that reads a bound extent.

        The number it is at every bound (``n - n``, ``(4 * n) // n``), or
        None where it follows the call. ``use_value`` forgets it; any other
        change makes a new instance.
        """
        bound = self.bound_extents
        if not bound:
            return {}
        op = self
        probe = copy.copy(op)
        forms = (
            None
            if None in bound.values()
            else {k: v for k, v in bound.items() if v is not None}
        )
        out: dict[str, int | None] = {}
        for m in self._value_members:
            if m.derive is None:
                continue
            reads: set[str] = set()
            vars(probe)["_bound"] = _Reads(self._bound, reads)
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

    def derived_at(self, name: str, **extents: int | Affine) -> Any:
        """Return the word the host writes for ``name``.

        With the extents at the given bounds (an ``Affine`` form where the
        caller evaluates it symbolically rather than at one number).
        """
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

    def _at_extents(self, **extents: int | Affine) -> Self:
        """Return a copy whose extents read as given numbers (``per_call(bounds=)``)."""
        at = copy.copy(self)
        vars(at)["_bound"] = {**self._bound, **extents}
        return at

    def extent_unit(self, buffer: str) -> int | None:
        """Return the rows of ``buffer`` one lane takes at a time under a bound.

        ``None`` for the stream tile's rows; ``0`` when a bound does not shorten it.
        """
        return None

    def value(self, name: str) -> Value:
        """Return the device word of value ``name``.

        An extent attribute reads as an integer.
        """
        try:
            return self._values[name]
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
        """Build, once, the image this operator runs on outside a graph.

        Returns its artifacts (the xclbin, the instruction stream and their
        cache entry).
        """
        if self._image is None:
            # The image layer builds on this one: imported here to break the cycle.
            from ..image.standalone import OperatorImage

            self._image = OperatorImage(self)
        return self._image.compile().artifacts

    def __call__(self, *args, **kwargs):
        """Run this operator's own image on device tensors, one per declared buffer.

        In order, ``kwargs`` its ``DispatchTime`` values by device symbol.
        Inside a graph's body, record a step on handles instead, ``kwargs``
        per-call values.
        """
        if (recorder := graph_recorder.get()) is not None:
            return recorder.call(self, args, kwargs)
        names = [b.name for b in self.buffers]
        if len(args) != len(names) or not all(isinstance(a, NpuTensor) for a in args):
            raise TypeError(
                f"{type(self).__name__} runs outside a graph's body on device "
                f"tensors, one per declared buffer {names}; got "
                f"{[type(a).__name__ for a in args]}"
            )
        self.compile()
        assert self._image is not None, "compile() built it"
        return self._image(*args, **kwargs)

    def _bind(self) -> None:
        """Bind each member: an operand an ``Operand``, a per-call value a ``Value``.

        Per-call values go in ``_values``, which an extent reads as its number.
        """
        vars(self).pop("_derived_under_bound", None)
        self._bound: dict[str, Any] = {}
        self._values: dict[str, Value] = {}
        for m in self.declaration.members:
            if isinstance(m, PerCallMember):
                # Bound as mlir-aie binds a member (Member.of), now a Value.
                value = m.of(self)
                value.__class__ = Value
                value = cast(Value, value)
                self._values[m.name] = value
                self._bound[m.name] = (
                    value if m.bounds is None else vars(self)[m.bounds.name]
                )
            elif m.when is None or vars(self)[m.when.name]:
                self._bound[m.name] = Operand(m, self)
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
                        self._values[word.name] = word

    def layout(self) -> Self:
        """Return this operator as its cores see it.

        Each operand is bound to the view and its values this operator's; an
        extent reads as its number only where the key holds its bound.
        """
        view = object.__new__(type(self))
        vars(view).update(
            {n: vars(self)[n] for n in self.declaration.key}, trace=self.trace
        )
        view._values = self._values
        view._bound = {}
        for m in self.declaration.members:
            if m.name not in self._bound:
                continue
            if isinstance(m, PerCallMember) and m.bounds is not None:
                if m.bounds.name in vars(view):
                    view._bound[m.name] = vars(view)[m.bounds.name]
            elif isinstance(m, PerCallMember):
                view._bound[m.name] = self._bound[m.name]
            else:
                view._bound[m.name] = Operand(m, view)
        return view

    @property
    def _value_members(self) -> list[Value]:
        """Every per-call value: the declared ones, then the library's."""
        return list(self._values.values())

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


class _Reads(dict):
    """An operator's members by name, noting each name read in ``reads``."""

    def __init__(self, members: dict[str, Any], reads: set[str]) -> None:
        super().__init__(members)
        self.reads = reads

    def __getitem__(self, name: str) -> Any:
        self.reads.add(name)
        return super().__getitem__(name)
