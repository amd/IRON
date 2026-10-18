# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tracing a graph: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import itertools
import math
from collections.abc import Callable, Hashable, Iterable, Mapping

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import In, InOut, Out
from aie.utils import bfp

from .. import declare
from ..declare import Operand, Operator
from ..declare.value import Extent
from ..declare.operator import graph_tracer
from ..declare.precision import Precision
from ..declare.profile import Profile
from ..image.packaging import Kind
from ..image.step import BufferRef, SequenceStep
from .handle import (
    Affine,
    Handle,
    PerCall,
    State,
    Weight,
    _rescale_bounds,
    is_operand,
)


@dataclasses.dataclass
class TracedStep:
    op: Operator
    slots: list  # one handle per declared buffer
    inputs: list
    outputs: list
    # The ids a per-call gather takes, on both its steps: the reference
    # gathers by them where the table is read, and skips the step that
    # writes the table's words.
    gather: Handle | None = None

    def refs(self) -> tuple[BufferRef, ...]:
        """Where each declared buffer of the step is."""
        return tuple(h.ref() for h in self.slots)


@dataclasses.dataclass(frozen=True)
class Encoder:
    """How the host turns an input into the ``words`` the device reads, from
    ``buffer``'s device address: ``encode(input, address, valid)``, with
    ``valid`` the call's ``bound`` on the input's rows, or None.
    """

    buffer: str
    encode: Callable[[np.ndarray, int, int | None], np.ndarray]
    bound: Affine | None = None
    words: int = 0

    def __call__(
        self, tensor: np.ndarray, address: int, values: Mapping[str, int]
    ) -> np.ndarray:
        valid = None if self.bound is None else self.bound.evaluate(values)
        return self.encode(tensor, address, valid)


@dataclasses.dataclass(frozen=True)
class Binding:
    """A graph value bound to one operator's value member, written per call
    as ``expression``.
    """

    op: Operator
    member: declare.Value
    expression: Affine

    @property
    def symbol(self) -> str:
        return self.member.symbol


@dataclasses.dataclass(frozen=True)
class Limit:
    """A per-call ``expression``, plus ``plus`` where given (a second
    value's), that a view of ``view`` holds in ``[lo, hi)``.
    """

    expression: Affine
    lo: int
    hi: int
    view: str
    plus: Affine | None = None

    def evaluate(self, values: Mapping[str, int]) -> int:
        at = self.expression.evaluate(values)
        return at if self.plus is None else at + self.plus.evaluate(values)

    def __str__(self) -> str:
        return str(self.expression) + ("" if self.plus is None else f" + {self.plus}")


def _unbounded(h: Handle) -> Handle:
    if not h.bounds:
        return h
    return Handle(
        h.shape, h.dtype, h.name, h.role, h.parent, h.start, h.tap, h.index_by
    )


def _take_views(cls, operands, kwargs, values):
    """Hand each view operand's pattern to the operator (``cls.accept_views``)
    and stand its parent in.

    A bound on one view holds the others: each side moves the same rows. A
    side not given (a fresh output) is the bounded view's shape, bounded
    alike; a given one must be that shape, and is bounded on the same axis.
    A source walked with a per-call repeat or length (``Handle.at``) takes
    them itself, and its ``bounds`` hold the others.
    """
    given = operands[: len(cls.accept_views)]
    held = next((h for h in given if h.bounds), None)
    if held is not None and len(held.bounds) == 1:
        ((axis, count),) = held.bounds.items()
        for i, (param, _) in enumerate(cls.accept_views):
            if i < len(given) and given[i].bounds:
                continue
            if i >= len(given):
                kwargs.setdefault(param, TensorAccessPattern.full(held.shape))
            elif given[i].shape != held.shape:
                raise ValueError(
                    f"{given[i]!r} is every row of a {given[i].shape} view while "
                    f"{held!r} moves {count} on axis {axis}; bound it alike"
                )
            kwargs.setdefault(f"{param}_bound", axis)
            values[f"{param}_valid"] = count
    out = []
    for i, h in enumerate(operands):
        if i < len(cls.accept_views):
            param, offset_member = cls.accept_views[i]
            tap = TensorAccessPattern.full(h.shape or (1,)) if h.tap is None else h.tap
            kwargs.setdefault(param, tap)
            if h.repeat is not None or h.length is not None:
                if i:
                    raise ValueError(
                        f"{h!r}: a per-call repeat or length is a source's"
                    )
                if h.length is not None:
                    kwargs.setdefault(f"{param}_bound", 1)
                    values[f"{param}_valid"] = h.length
                if h.repeat is not None:
                    kwargs.setdefault(f"{param}_repeat", True)
                    for k, r in enumerate(h.repeat):
                        values[f"{param}_repeats{k}"] = r - 1
            elif h.bounds:
                (axis, count), *more = h.bounds.items()
                if more:
                    raise ValueError(f"{h!r}: a copy takes one bounded axis")
                kwargs.setdefault(f"{param}_bound", axis)
                values[f"{param}_valid"] = count
            if h.index_by is not None:
                values[offset_member] = h.index_by
            out.append(_unbounded(h.parent if h.tap is not None else h))
        elif h.tap is not None:
            raise TypeError(
                f"{cls.__name__} takes a contiguous operand at position {i}, not "
                f"the view {h!r}; Copy takes views"
            )
        else:
            out.append(h)
    return out


@dataclasses.dataclass
class TracedGraph:
    """What tracing a graph for given shapes produced.

    ``weights`` and ``states`` hold the object they are keyed by the
    identity of, so the key stays its own. ``carry`` is the next value of
    each carried value; a handle there is an output too.
    """

    name: str
    steps: list[TracedStep]
    inputs: list[Handle]
    outputs: list[Handle]  # returned, then carried handles not returned
    # buffer name -> nbytes, for weights, states and slice parents
    pinned: dict[str, int] = dataclasses.field(default_factory=dict)
    values: list[PerCall] = dataclasses.field(default_factory=list)
    weights: dict[int, tuple[object, Handle]] = dataclasses.field(
        default_factory=dict, repr=False
    )
    states: dict[int, tuple[State, Handle]] = dataclasses.field(default_factory=dict)
    bindings: list[Binding] = dataclasses.field(default_factory=list)
    returned: list[Handle] = dataclasses.field(default_factory=list)
    carry: dict[str, Handle | Affine] = dataclasses.field(default_factory=dict)
    feedback: list[str] = dataclasses.field(default_factory=list)
    # An input the device reads as words the host encodes from it and a
    # buffer's device address (a gather's ids): a table's after another's,
    # each gathered from by the same input.
    encoders: dict[str, list[Encoder]] = dataclasses.field(default_factory=dict)
    # A per-call value the graph fills in rather than the caller, from a
    # buffer's device address (a gather by ids the device made):
    # value -> (buffer, address -> words by name, its word's name).
    addresses: dict[str, tuple[str, Callable[[int], dict], str]] = dataclasses.field(
        default_factory=dict
    )
    limits: list[Limit] = dataclasses.field(default_factory=list)

    @property
    def reads(self) -> set[str]:
        """The per-call values a call of this version must give: those of the
        graph's its steps, bounds, host encodings and carry read, and its
        carried ones; not the words the image writes itself (a gather's
        table address).
        """
        expressions = [
            *(b.expression for b in self.bindings),
            *(limit.expression for limit in self.limits),
            *(limit.plus for limit in self.limits if limit.plus is not None),
            *(e for e in self.carry.values() if isinstance(e, Affine)),
            *(
                e.bound
                for held in self.encoders.values()
                for e in held
                if e.bound is not None
            ),
        ]
        declared = {v.name for v in self.values}
        carried = {v.name for v in self.values if v.kind is Kind.CARRIED}
        return ({e.value.name for e in expressions} & declared) | carried

    @classmethod
    def of_steps(
        cls,
        name: str,
        steps: Iterable[SequenceStep],
        inputs: Iterable[str],
        outputs: Iterable[str],
        pinned: Mapping[str, int] | None = None,
        feedback: Iterable[str] = (),
    ) -> TracedGraph:
        """A graph of ``steps`` over buffers known by name alone, as bytes.

        Args:
            name: The graph's name.
            steps: Each step's operator and where its buffers are.
            inputs: The buffers the host writes.
            outputs: The buffers the host reads.
            pinned: The bytes of each buffer a step names only in part, and
                of any it should hold at a size of its own.
            feedback: The buffers of the feedback argument.
        """
        pinned = dict(pinned or {})
        roots: dict[str, Handle] = {}
        traced = []
        for step in steps:
            slots = []
            for ref in step.buffers:
                root = roots.setdefault(
                    ref.root,
                    Handle(
                        (pinned.get(ref.root, 0),), np.uint8, ref.root, "intermediate"
                    ),
                )
                if ref.nbytes is None:
                    slots.append(root)
                    continue
                slots.append(
                    Handle(
                        (ref.nbytes,), np.uint8, ref.root, root.role, root, ref.start
                    )
                )
            declared = list(zip(slots, step.op.buffers))
            traced.append(
                TracedStep(
                    step.op,
                    slots,
                    [h for h, b in declared if b.fills],
                    [h for h, b in declared if b.drains],
                )
            )
        return cls(
            name,
            traced,
            [Handle((), np.uint8, n, "input") for n in inputs],
            [Handle((), np.uint8, n, "output") for n in outputs],
            pinned,
            feedback=list(feedback),
        )

    @classmethod
    def of_step(cls, op: Operator) -> TracedGraph:
        """``op`` alone, over its own buffers by their declared names: the
        host writes what it reads and reads what it only writes.
        """
        return cls.of_steps(
            op.name,
            [SequenceStep(op, tuple(BufferRef(b.name) for b in op.buffers))],
            [b.name for b in op.buffers if b.fills],
            [b.name for b in op.buffers if b.drains and not b.fills],
        )

    @property
    def residents(self) -> dict[str, Hashable]:
        """Buffer name -> storage key of every weight and state, the same in
        every trace so each version addresses one copy.
        """
        found: dict[str, Hashable] = {
            h.name: key for key, (_, h) in self.weights.items()
        }
        found.update((h.name, key) for key, (_, h) in self.states.items())
        return found

    def dot(self) -> str:
        """This graph drawn as Graphviz text (``visualize.dot``)."""
        from .visualize import dot

        return dot(self)

    def check_limits(self, values: Mapping[str, int]) -> None:
        """Refuse a call whose values index or bound a view outside it.

        Raises:
            IndexError: A recorded limit does not hold for ``values``.
        """
        for limit in self.limits:
            at = limit.evaluate(values)
            if not limit.lo <= at < limit.hi:
                raise IndexError(
                    f"{self.name}: {limit} is {at}, outside "
                    f"[{limit.lo}, {limit.hi}) for {limit.view}"
                )

    def reference(
        self, tensors: Mapping[str, np.ndarray], values: Mapping[str, int]
    ) -> tuple[list[np.ndarray], dict[str, int]]:
        """Run each step's ``reference()`` on host buffers: the returned
        outputs, each cut to the rows its bounds keep, and each carried
        value's next.

        A step reads its buffers as the device holds them, and its per-call
        values, an extent's (``op.valid``) too, evaluated for this call; it
        writes only the rows its outputs' bounds keep. A state's
        buffer is its ``host`` array, kept from call to call.

        Args:
            tensors: Each input, by name.
            values: Each per-call value, by name.

        Raises:
            IndexError: ``values`` index or bound a view outside it.
        """
        self.check_limits(values)
        buffers: dict[str, np.ndarray] = {}

        def store(name: str, array) -> None:
            buffers[name] = np.ascontiguousarray(array).reshape(-1).view(np.uint8)

        for h in self.inputs:
            store(h.name, tensors[h.name])
        for array, h in self.weights.values():
            store(h.name, array)
        for state, h in self.states.values():
            if state.host is None:
                state.host = np.zeros(state.shape, state.dtype)
            store(h.name, state.host)

        def view(h: Handle) -> np.ndarray:
            ref = h.ref()
            if ref.root not in buffers:
                buffers[ref.root] = np.zeros(h.root.nbytes, np.uint8)
            raw = buffers[ref.root][ref.start : ref.start + h.nbytes]
            return raw if bfp.is_bfp(h.dtype) else raw.view(h.dtype).reshape(h.shape)

        def valid(h: Handle) -> tuple:
            key = [slice(None)] * len(h.shape)
            for axis, count in h.bounds.items():
                key[axis] = slice(count.evaluate(values))
            return tuple(key)

        bound: dict[int, list[Binding]] = {}
        for b in self.bindings:
            bound.setdefault(id(b.op), []).append(b)
        for step in self.steps:
            if step.gather is not None:
                if step.inputs[0] is not step.gather:
                    _gather_reference(step, view(step.gather)[valid(step.gather)], view)
                continue
            op = step.op
            given = {
                b.member.name: b.expression.evaluate(values)
                for b in bound.get(id(op), ())
            }
            extents = {n: given[n] for n in op.bound_extents}
            if extents:
                # Each extent reads as this call's in the reference.
                op = op._at_extents(**extents)
            declared = list(zip(op.buffers, step.slots))
            inputs = {b.name: view(h) for b, h in declared if b.fills}
            outputs = {b.name: view(h) for b, h in declared if not b.fills}
            results = op._call_reference(inputs, outputs, given)
            for b, h in declared:
                if not b.drains:
                    continue
                target = outputs[b.name] if b.name in outputs else inputs[b.name]
                if results[b.name] is not target:
                    rows = valid(h)
                    result = np.asarray(results[b.name]).reshape(target.shape)
                    target[rows] = result[rows]
        returned = [view(h)[valid(h)] for h in self.returned]
        carry = {
            name: (
                nxt.evaluate(values)
                if isinstance(nxt, Affine)
                else int(view(nxt).reshape(-1)[0])
            )
            for name, nxt in self.carry.items()
        }
        return returned, carry

    @property
    def operators(self) -> list:
        seen = {}
        for s in self.steps:
            seen.setdefault(id(s.op), s.op)
        return list(seen.values())

    @property
    def arrays(self) -> list:
        seen = {}
        for op in self.operators:
            seen.setdefault(op.array_key(), op)
        return list(seen.values())


def _gather_reference(step: TracedStep, ids: np.ndarray, view) -> None:
    """A per-call gather's step, on the host: the table's rows ``ids``
    names, each clipped to the table where the device made them.
    """
    table, out = (view(h) for h in (step.inputs[0], step.outputs[0]))
    table = table.reshape(table.shape[0], -1)
    rows = ids.astype(np.int64)
    if step.gather.role != "input":
        rows = np.clip(rows, -len(table), len(table) - 1)
    out.reshape(-1, table.shape[1])[: len(rows)] = table[rows]


class Tracer:
    """Records operator calls on handles while a graph's body runs."""

    def __init__(
        self,
        name: str,
        profile: Profile | None = None,
        held: Mapping[int, tuple[str, object]] | None = None,
        inputs: Iterable[str] = (),
        precision: Precision | None = None,
    ) -> None:
        self.name = name
        self.profile = profile
        self.precision = precision
        # Each instance applied, held so its id stays its own, and as raised
        # to the precision.
        self._raised: dict[int, tuple[Operator, Operator]] = {}
        held = held or {}
        self._held_arrays = [
            x.array if isinstance(x, Weight) else x
            for _, x in held.values()
            if isinstance(x, (Weight, np.ndarray))
        ]
        self.steps: list[TracedStep] = []
        self.weights: dict[int, tuple[object, Handle]] = {}
        self.states: dict[int, tuple[State, Handle]] = {}
        self.bindings: list[Binding] = []
        self.limits: list[Limit] = []
        self._bound: dict[int, dict] = {}
        self.encoders: dict[str, list[Encoder]] = {}
        # Each encoded input's first control words, whole until a second
        # table's follow them.
        self._controls: dict[str, Handle] = {}
        self.addresses: dict[str, tuple[str, Callable, str]] = {}
        self._counter = itertools.count()
        self._constants: dict[tuple, np.ndarray] = {}
        self._names: dict[int, str] = {}
        for key, (path, x) in held.items():
            self._names.setdefault(key, path)
            if isinstance(x, Weight):
                self._names.setdefault(id(x.array), path)
        self._taken = {*self._names.values(), *inputs}

    def fresh(self, name: str) -> str:
        """``name``, or the first of ``name_1``, ``name_2``, ... no buffer of
        the graph has: a name the tracer makes up never aliases one it was
        given.
        """
        candidates = (f"{name}_{k}" for k in itertools.count(1))
        free = next(
            n for n in itertools.chain([name], candidates) if n not in self._taken
        )
        self._taken.add(free)
        return free

    def constant(self, value, width: int, dtype) -> np.ndarray:
        """A row of ``width`` ``value``s in ``dtype``: one array, so one
        weight buffer, per number, width and dtype.
        """
        key = (float(value), width, bfp.dtype_name(dtype))
        if key not in self._constants:
            self._constants[key] = np.full(width, value, dtype)
        return self._constants[key]

    def __enter__(self):
        self._token = graph_tracer.set(self)
        return self

    def __exit__(self, *exc):
        graph_tracer.reset(self._token)

    def operand(self, x) -> Handle:
        if isinstance(x, Handle):
            if x.window is not None:
                # A run from a per-call start taken whole ends inside its axis.
                _, start, width, n = x.window
                self.limit(start + width, 0, n + 1, x)
            return x
        if isinstance(x, State):
            key = id(x)
            if key not in self.states:
                x.name = (
                    x.name
                    or self._names.get(key)
                    or self.fresh(f"state{len(self.states)}")
                )
                self._taken.add(x.name)
                self.states[key] = (x, Handle(x.shape, x.dtype, x.name, "state"))
            return self.states[key][1]
        if is_operand(x):
            array = x.array if isinstance(x, Weight) else x
            key = id(array)
            if key not in self.weights:
                name = self._names.get(id(x)) or self._names.get(key)
                if name is None and isinstance(array, np.ndarray):
                    view = self._held_view(array)
                    if view is not None:
                        return view
                name = name or self.fresh(f"w{len(self.weights)}")
                self.weights[key] = (
                    array,
                    Handle(array.shape, np.dtype(array.dtype).type, name, "weight"),
                )
            return self.weights[key][1]
        raise TypeError(f"{x!r} is not a graph handle, a state, or a tensor")

    def _held_view(self, x: np.ndarray) -> Handle | None:
        """``x``, a numpy view of a held array, as a view of its buffer, or None."""
        if not x.size or any(s < 0 for s in x.strides):
            return None
        address = x.__array_interface__["data"][0]
        for held in self._held_arrays:
            base = held.__array_interface__["data"][0]
            offset, misaligned = divmod(address - base, x.itemsize)
            if (
                held.dtype != x.dtype
                or not held.flags.c_contiguous
                or misaligned
                or not 0 <= offset < held.size
                or any(s % x.itemsize for s in x.strides)
            ):
                continue
            strides = [
                s // x.itemsize if n > 1 else 0 for s, n in zip(x.strides, x.shape)
            ]
            if offset + sum((n - 1) * s for n, s in zip(x.shape, strides)) >= held.size:
                continue
            if not offset and x.size == held.size and x.flags.c_contiguous:
                # All of the buffer, as a reshape: the buffer itself, which a gather reads.
                return self.operand(held).reshape(x.shape)
            tap = TensorAccessPattern(held.shape, offset, list(x.shape), strides)
            return self.operand(held).at(tap, x.shape)
        return None

    def overwrites(self, given) -> str | None:
        """What an output a call gives would write over that no call may:
        ``"weight"`` or ``"input"``, through any view of it, else None.
        """
        if isinstance(given, State):
            return None
        if not isinstance(given, Handle):
            return "weight"
        return given.role if given.role in ("weight", "input") else None

    def check_outputs(self, cls, outputs) -> None:
        """Refuse an output a call gives that is a weight or an input.

        A positional operand past the inputs is an output, so a weight given
        where an optional input was meant would be written over.

        Raises:
            TypeError: An output is a weight or an input, or a view of one.
        """
        for given in outputs:
            kind = self.overwrites(given)
            if kind is None:
                continue
            keywords = [
                f"{m.name}="
                for m in cls.declaration.members
                if isinstance(m, Operand) and m.fills and m.when is not None
            ]
            hint = f"; an optional input is given by keyword ({', '.join(keywords)})"
            raise TypeError(
                f"{cls.__name__}: the output given, {list(given.shape)}, is a "
                f"graph {kind} or a view of one, which a call does not write over"
                f"{hint if keywords else ''}"
            )

    def call(self, target, args, kwargs):
        """Record ``target(*args, **kwargs)``: inputs, optionally followed by
        outputs; keywords are optional inputs, per-call value handles, or
        construction arguments when ``target`` is a class.

        Raises:
            TypeError, ValueError, IndexError: The call is refused; the
                message starts with the graph, the operator and the
                operands as the body named them.
        """
        try:
            return self._call(target, args, kwargs)
        except (TypeError, ValueError, IndexError) as e:
            cls = target if isinstance(target, type) else type(target)
            given = ", ".join(self._describe(a) for a in args)
            e.args = (f"{self.name}: {cls.__name__}({given}): {e}", *e.args[1:])
            raise

    def _describe(self, x) -> str:
        """``x`` in the body's terms: a handle's buffer, a held tensor's
        path, else its kind and shape.
        """
        if isinstance(x, Handle):
            return str(x.ref())
        if isinstance(x, State) and x.name:
            return x.name
        array = x.array if isinstance(x, Weight) else x
        name = self._names.get(id(x)) or self._names.get(id(array))
        return name or f"{type(x).__name__} {list(getattr(x, 'shape', ()))}"

    def _call(self, target, args, kwargs):
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = cls.declaration.call_operands(args, kwargs)
        self.check_outputs(cls, outputs)
        names = list(inputs)
        operands = [self.operand(a) for a in [*inputs.values(), *outputs]]
        values = {
            k: kwargs.pop(k)
            for k in list(kwargs)
            if isinstance(kwargs[k], (PerCall, Affine))
        }
        if any(h.gather_by is not None for h in operands):
            return self._gather(target, operands, kwargs or values)
        called = operands
        if isinstance(target, type):
            own = self._split_values(cls, values)
            operands = _take_views(cls, operands, kwargs, own)
            op = self._construct(
                cls,
                dict(zip(names, operands)),
                operands[len(names) :],
                kwargs,
            )
        else:
            _, op = self._raised.setdefault(
                id(target), (target, self._at_precision(target))
            )
            own = self._split_values(type(op), values)
            operands = _take_views(type(op), operands, {}, own)
            if kwargs or values:
                raise TypeError(
                    f"{type(op).__name__} instance called with unexpected keyword "
                    f"arguments {sorted(kwargs) + sorted(values)}"
                )
        if values:
            raise TypeError(
                f"{type(op).__name__} has no per-call value {sorted(values)}"
            )
        for name, value in own.items():
            self._bind(op, name, value)
        return self._record(op, operands, called)

    def _gather(self, target, operands: list[Handle], extra) -> Handle:
        """``Copy(table[ids])`` with ``ids`` per call: the class's per-call
        gather. For ids an input the host encodes its control words from
        the ids each call; for ids the device made, its word source writes
        them into its template first.
        """
        view = operands[0]
        ids, table = view.gather_by, view.parent
        if (
            not isinstance(target, type)
            or target.per_call_gather is None
            or len(operands) != 1
            or extra
        ):
            raise TypeError(
                f"{view!r} takes the rows the input {ids.name!r} names each "
                f"call; only a Copy of it alone does, Copy(table[ids])"
            )
        given = dict(
            rows=ids.shape[0],
            table_rows=table.shape[0],
            row=math.prod(table.shape[1:]),
            dtype=table.dtype,
        )
        gather = target.per_call_gather
        if self.profile is None:
            op = gather(**given)
        else:
            op = self.profile.make(gather, **given)
        bound = ids.bounds.get(0)
        if bound is not None:
            self._bind(op, "valid_rows", bound)
        if ids.role == "input":
            held = self.encoders.setdefault(ids.name, [])
            if any(e.buffer == table.name for e in held):
                raise ValueError(
                    f"the input {ids.name!r} gathers from {table.name!r} once"
                )
            # Each table's words follow the last's in the input's buffer, each
            # then a part of it, the first's too.
            start = sum(e.words for e in held)
            control = Handle((start + op.words,), np.uint32, ids.name, "input")
            if not held:
                self._controls[ids.name] = control
            else:
                control = control[start:]
            if len(held) == 1:
                first = self._controls[ids.name]
                part = first[:]
                for step in self.steps:
                    step.slots = [part if h is first else h for h in step.slots]
                    step.inputs = [part if h is first else h for h in step.inputs]
            held.append(Encoder(table.name, op.control_words, bound, op.words))
        else:
            source = op.word_source()
            template = op.template[0]
            self._names[id(template)] = self.fresh(f"{table.name}_gather")
            control = self.operand(template)
            for member in ("base_lo", "base_hi"):
                name = next(
                    (
                        n
                        for n, (buffer, _, m) in self.addresses.items()
                        if (buffer, m) == (table.name, member)
                    ),
                    f"address{len(self.addresses) // 2}_{member}",
                )
                self.addresses[name] = (table.name, source.address_words, member)
                self._bind(source, member, PerCall(name, Kind.SCRATCHPAD, np.int32))
            self._record(source, [ids, control])
            self.steps[-1].gather = ids
        out = self._record(op, [table, control])
        self.steps[-1].gather = ids
        return out if out.shape == view.shape else out.reshape(view.shape)

    @staticmethod
    def _split_values(op_cls, kwargs) -> dict:
        names = {
            m.name for m in op_cls.declaration.members if isinstance(m, declare.Value)
        }
        return {k: kwargs.pop(k) for k in list(kwargs) if k in names}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        inferred = cls.declaration.infer(
            {name: h.shape for name, h in inputs.items()},
            [h.shape for h in outputs],
            **kwargs,
        )
        given = {**kwargs, **inferred}
        if self.profile is not None:
            return self._at_precision(self.profile.make(cls, **given))
        pinned = frozenset(
            name
            for name, value in given.items()
            if name in cls.declaration.tunables and value is not None
        )
        return self._at_precision(cls(**given, pinned=pinned))

    def _at_precision(self, op: Operator) -> Operator:
        """``op``, its precision raised to the graph's where it rounds more."""
        if self.precision is None or "precision" not in op.declaration.tunables:
            return op
        level = op.precision.at_least(self.precision)
        if level == op.precision:
            return op
        raised = op.at_precision(level)
        if type(raised) is type(op) or self.profile is None:
            return raised
        # An operator handed over to another takes that one's profile entry.
        cls = type(raised)
        given = {n: getattr(raised, n) for n in cls.declaration.params}
        return self.profile.make(cls, **given, precision=level)

    def _output_bounds(self, op, buffer, rank: int) -> dict:
        bounds = {}
        for binding in self.bindings:
            if binding.op is not op or not isinstance(binding.member, Extent):
                continue
            axis = buffer.extent_axis(binding.member)
            if axis is not None:
                bounds[axis] = binding.expression
        return bounds

    def _bind(self, op, name, value) -> None:
        if not isinstance(value, (PerCall, Affine)):
            raise TypeError(
                f"{type(op).__name__}.{name} takes a per-call value handle (a "
                f"keyword-only parameter of the graph's body), got {value!r}"
            )
        # An offset may floor; an extent's derived words take a linear one.
        if isinstance(value, PerCall) or isinstance(op.value(name), Extent):
            value = value.affine()
        bound = self._bound.setdefault(id(op), {})
        if name in bound and bound[name] != value:
            raise ValueError(
                f"{type(op).__name__}.{name} is bound to {bound[name]} at an "
                f"earlier call site and to {value} here; one instance has one "
                f"value, bind one expression at every site or use two instances"
            )
        if name not in bound:
            op.use_value(name, value)
            bound[name] = value
            member = next(v for v in op.values if v.name == name)
            self.bindings.append(Binding(op, member, value))

    def _record(self, op, operands, called=None):
        """Record ``op`` on ``operands``; ``called`` are the operands as the
        call gave them, a view where ``operands`` holds its buffer.
        """
        called = operands if called is None else called
        # A shape that Selects on an Auto() field is the device's: resolve()
        # gives it, unchecked, so a profile may still tune the op.
        unset = {n for n in type(op).declaration.autos if vars(op)[n] is None}
        shaped = op
        if any(unset & m.dims.names() for m in op._members_io()):
            shaped = op.resolve(op.dev)
        buffers = shaped.buffers
        ins = [b for b in buffers if b.fills]
        outs = [b for b in buffers if b.role is Out]
        if len(operands) == len(ins):
            given_outs = []
        elif len(operands) == len(ins) + len(outs):
            given_outs = operands[len(ins) :]
        else:
            raise TypeError(
                f"{type(op).__name__} takes {len(ins)} operand(s) "
                f"({', '.join(b.name for b in ins)}), optionally followed by "
                f"{len(outs)} output(s); got {len(operands)}"
            )
        for i, (h, b) in enumerate(zip(operands, ins + outs)):
            # Another rank matches on the count, for an output only a flat
            # one; the same rank must match the shape, or a transposed weight
            # would pass.
            shape = tuple(b.shape)
            wrong = (
                tuple(h.shape) != shape
                if len(h.shape) == len(shape)
                else h.elements != b.elements or (i >= len(ins) and len(shape) != 1)
            )
            if wrong:
                raise ValueError(
                    f"{type(op).__name__}.{b.name} is {shape} "
                    f"({b.elements} elements); operand {h!r} is {tuple(h.shape)}"
                )
            if bfp.dtype_name(h.dtype) != bfp.dtype_name(b.dtype):
                raise TypeError(
                    f"{type(op).__name__}.{b.name} is {bfp.dtype_name(b.dtype)}; "
                    f"operand {h!r} is {bfp.dtype_name(h.dtype)}"
                )
            bounds = (
                h.bounds if len(h.shape) == len(shape) else _rescale_bounds(h, shape)
            )
            for axis, count in bounds.items():
                extent = next(
                    (
                        m
                        for m in type(op).declaration.members
                        if isinstance(m, Extent) and b.extent_axis(m) == axis
                    ),
                    None,
                )
                if extent is None:
                    raise TypeError(
                        f"{type(op).__name__}.{b.name} cannot be bounded per call on "
                        f"axis {axis} ({count}): it declares no Extent for the "
                        f"field sizing it"
                    )
                self._bind(op, extent.name, count)
        slots, outputs, it, given = [], [], iter(operands[: len(ins)]), iter(given_outs)
        for b in buffers:
            if b.role is In:
                slots.append(next(it))
            elif b.role is InOut:
                h = next(it)
                slots.append(h)
                outputs.append(h)
            elif given_outs:
                slots.append(next(given))
            else:
                shape = b.shape
                # A flat output keeps the shape and bounds of the operand it
                # is the size of: (rows, cols) stays (rows, cols) through SiLU,
                # and a copy of a view has the view's shape.
                bounds: dict = {}
                if len(shape) == 1:
                    like = next(
                        (i for i, h in enumerate(called) if h.elements == b.elements),
                        None,
                    )
                    if like is not None:
                        shape = called[like].shape
                        bounds = dict(called[like].bounds)
                if not bounds:
                    bounds = self._output_bounds(op, b, len(shape))
                h = Handle(
                    shape,
                    b.dtype,
                    self.fresh(f"{type(op).__name__.lower()}{next(self._counter)}"),
                    "intermediate",
                    bounds=bounds,
                )
                slots.append(h)
                outputs.append(h)
        self.steps.append(
            TracedStep(op, slots, operands[: len(ins)], outputs + list(given_outs))
        )
        if not outputs:
            return None
        return outputs[0] if len(outputs) == 1 else tuple(outputs)

    def finish(
        self,
        inputs,
        outputs,
        values,
        carry: Mapping[str, Handle | Affine] | None = None,
    ) -> TracedGraph:
        """The traced graph; ``carry`` is the next value of each carried
        value, whose handles are outputs too.
        """
        next_values = dict(carry or {})
        returned = list(outputs)
        outputs = returned + [
            h
            for h in next_values.values()
            if isinstance(h, Handle) and not any(h is o for o in returned)
        ]
        pinned = {}
        for _, h in self.weights.values():
            pinned[h.name] = h.nbytes
        for name, held in self.encoders.items():
            if len(held) > 1:
                pinned[name] = sum(e.words for e in held) * np.dtype(np.uint32).itemsize
        for _, h in self.states.values():
            pinned[h.name] = h.nbytes
        # A slice's parent needs an explicit size: no step may name it whole.
        for step in self.steps:
            for h in step.inputs + step.outputs:
                if h.parent is not None:
                    pinned.setdefault(h.parent.name, h.parent.nbytes)
        return TracedGraph(
            self.name,
            self.steps,
            inputs,
            outputs,
            pinned,
            values=values,
            weights=self.weights,
            states=self.states,
            bindings=self.bindings,
            returned=returned,
            carry=next_values,
            encoders=self.encoders,
            addresses=self.addresses,
            limits=self.limits,
        )

    def limit(
        self,
        expression: Affine,
        lo: int,
        hi: int,
        view: Handle,
        plus: Affine | None = None,
    ) -> None:
        """Record that a call's ``expression``, plus ``plus`` where given,
        must lie in ``[lo, hi)`` for ``view``, which it indexes or bounds.
        """
        self.limits.append(Limit(expression, lo, hi, repr(view), plus))
