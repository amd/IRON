# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Recording a graph: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import itertools
import math
from collections.abc import Callable, Hashable, Iterable, Mapping
from typing import Any

import numpy as np
from aie.helpers.taplib import Affine, PerCall, TensorAccessPattern
from aie.iron import In, InOut, Out
from aie.utils import bfp

from ..declare import Operator, Value
from ..declare.operand import concrete
from ..declare.operator import graph_recorder
from ..declare.profile import Profile
from ..image.packaging import Kind
from ..image.step import BufferRef, SequenceStep
from .handle import (
    Dense,
    Gather,
    Handle,
    State,
    Strided,
    Weight,
    _count,
    _rescale_bounds,
    is_operand,
)


@dataclasses.dataclass
class Step:
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
class HostStep:
    """``fn(*reads, *writes)`` on the host before step ``at``.

    Each read is as the device left it, cut to its bounds; each write is
    a part of a state no step writes, holding what ``fn`` last wrote there.
    """

    at: int
    fn: Callable[..., None]
    reads: tuple[Handle, ...]
    writes: tuple[Handle, ...]


@dataclasses.dataclass(frozen=True)
class Encoder:
    """How the host turns an input into the ``words`` the device reads.

    From ``buffer``'s device address: ``encode(input, address, valid)``,
    with ``valid`` the call's ``bound`` on the input's rows, or None.
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
    """A graph value bound to one operator's value member.

    Written per call as ``expression``.
    """

    op: Operator
    member: Value
    expression: Affine

    @property
    def symbol(self) -> str:
        return self.member.symbol


@dataclasses.dataclass(frozen=True)
class Limit:
    """A per-call ``expression``, plus ``plus`` where given (a second value's).

    A view of ``view`` holds it in ``[lo, hi)``.
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


def _take_views(cls, operands, kwargs, values):
    """Hand each view operand's pattern to the operator (``cls.accept_views``).

    Stand its parent in; a bound on one view bounds the others alike, and
    a source with a per-call repeat or length (``Handle.at``) takes them
    itself.
    """
    given = operands[: len(cls.accept_views)]
    held = next((h for h in given if h.valid), None)
    if held is not None and len(held.valid) == 1:
        ((axis, count),) = held.valid.items()
        for i, (param, _) in enumerate(cls.accept_views):
            if i < len(given) and given[i].valid:
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
        view = h.layout if isinstance(h.layout, Strided) else None
        if i >= len(cls.accept_views):
            if view is not None:
                raise TypeError(
                    f"{cls.__name__} takes a contiguous operand at position {i}, "
                    f"not the view {h!r}; Copy takes views"
                )
            out.append(h)
            continue
        param, offset_member = cls.accept_views[i]
        tap = TensorAccessPattern.full(h.shape or (1,)) if view is None else view.tap
        kwargs.setdefault(param, tap)
        if view is not None and (view.repeat is not None or view.length is not None):
            if i:
                raise ValueError(f"{h!r}: a per-call repeat or length is a source's")
            if view.length is not None:
                kwargs.setdefault(f"{param}_bound", 1)
                values[f"{param}_valid"] = view.length
            if view.repeat is not None:
                kwargs.setdefault(f"{param}_repeat", True)
                for k, r in enumerate(view.repeat):
                    values[f"{param}_repeats{k}"] = r - 1
        elif h.valid:
            (axis, count), *more = h.valid.items()
            if more:
                raise ValueError(f"{h!r}: a copy takes one bounded axis")
            kwargs.setdefault(f"{param}_bound", axis)
            values[f"{param}_valid"] = count
        if view is None:
            out.append(dataclasses.replace(h, valid={}))
            continue
        if view.offset is not None:
            values[offset_member] = view.offset
        # What the pattern walks: the whole buffer, in the pattern's shape.
        walked = view.tap[0] if isinstance(view.tap, tuple) else view.tap
        out.append(Handle(h.buffer, concrete(walked.tensor_dims, walked), h.dtype))
    return out


@dataclasses.dataclass
class Recording:
    """What recording a graph for given shapes produced.

    ``weights`` and ``states`` hold the objects whose ``id`` keys them,
    so no key is reused; ``carry`` is each carried value's next, a
    handle there an output too.
    """

    name: str
    steps: list[Step]
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
    # Per-call values the graph fills in itself rather than the caller, from
    # a buffer's device address (for a gather by ids the device made). Each
    # value's name maps to the buffer, a function from its address to words
    # by name, and the name of the word that is the value.
    addresses: dict[str, tuple[str, Callable[[int], dict], str]] = dataclasses.field(
        default_factory=dict
    )
    limits: list[Limit] = dataclasses.field(default_factory=list)
    # Run between the steps, each ending a full ELF's command (``on_host``).
    host: list[HostStep] = dataclasses.field(default_factory=list)

    @property
    def reads(self) -> set[str]:
        """The per-call values a call of this version must give.

        Its carried ones and those its steps, bounds, host encodings and
        carry read, not a gather's table address, which the image writes
        itself.
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
            *(n for s in self.host for h in s.reads for n in h.valid.values()),
        ]
        declared = {v.name for v in self.values}
        carried = {v.name for v in self.values if v.marker is Kind.CARRIED}
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
    ) -> Recording:
        """Build a graph of ``steps`` over buffers known by name alone, as bytes.

        The host writes ``inputs`` and reads ``outputs``, and ``pinned``
        sizes a buffer a step names only in part or holds at a size of
        its own.
        """
        pinned = dict(pinned or {})
        roots: dict[str, Handle] = {}
        recording = []
        for step in steps:
            slots = []
            for ref in step.buffers:
                root = roots.setdefault(
                    ref.root,
                    Handle.whole(
                        (pinned.get(ref.root, 0),), np.uint8, ref.root, "intermediate"
                    ),
                )
                if ref.nbytes is None:
                    slots.append(root)
                    continue
                slots.append(
                    Handle(root.buffer, (ref.nbytes,), np.uint8, {}, Dense(ref.start))
                )
            declared = list(zip(slots, step.op.buffers))
            recording.append(
                Step(
                    step.op,
                    slots,
                    [h for h, b in declared if b.fills],
                    [h for h, b in declared if b.drains],
                )
            )
        return cls(
            name,
            recording,
            [Handle.whole((), np.uint8, n, "input") for n in inputs],
            [Handle.whole((), np.uint8, n, "output") for n in outputs],
            pinned,
            feedback=list(feedback),
        )

    @classmethod
    def of_step(cls, op: Operator) -> Recording:
        """Build a recording of ``op`` alone, over its own buffers by their declared names.

        The host writes what it reads and reads what it only writes.
        """
        return cls.of_steps(
            op.name,
            [SequenceStep(op, tuple(BufferRef(b.name) for b in op.buffers))],
            [b.name for b in op.buffers if b.fills],
            [b.name for b in op.buffers if b.drains and not b.fills],
        )

    @property
    def residents(self) -> dict[str, Hashable]:
        """Buffer name -> storage key of every weight and state.

        The same in every recording so each version addresses one copy.
        """
        found: dict[str, Hashable] = {
            h.name: key for key, (_, h) in self.weights.items()
        }
        found.update((h.name, key) for key, (_, h) in self.states.items())
        return found

    def check_limits(self, values: Mapping[str, int]) -> None:
        """Raise ``IndexError`` if ``values`` index or bound a view outside it."""
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
        """Run each step's ``reference()`` on host buffers.

        Return the returned outputs, cut to their bounds, and each
        carried value's next. A state's buffer is its ``host`` array,
        kept from call to call.

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
                buffers[ref.root] = np.zeros(h.buffer.nbytes, np.uint8)
            raw = buffers[ref.root][ref.start : ref.start + h.nbytes]
            return raw if bfp.is_bfp(h.dtype) else raw.view(h.dtype).reshape(h.shape)

        def valid(h: Handle) -> tuple:
            key = [slice(None)] * len(h.shape)
            for axis, count in h.valid.items():
                key[axis] = slice(count.evaluate(values))
            return tuple(key)

        bound: dict[int, list[Binding]] = {}
        for b in self.bindings:
            bound.setdefault(id(b.op), []).append(b)
        kept = {h.ref().root for h in (*self.inputs, *self.returned)}
        kept |= {
            h.ref().root for _, h in (*self.weights.values(), *self.states.values())
        }
        kept |= {n.ref().root for n in self.carry.values() if not isinstance(n, Affine)}
        last: dict[str, int] = {}
        for i, step in enumerate(self.steps):
            gather = [] if step.gather is None else [step.gather]
            for h in (*step.slots, *step.inputs, *step.outputs, *gather):
                last[h.ref().root] = i
        host: dict[int, list[HostStep]] = {}
        for s in self.host:
            host.setdefault(s.at, []).append(s)
            for h in (*s.reads, *s.writes):
                last[h.ref().root] = max(last.get(h.ref().root, s.at), s.at)
        # Each intermediate is dropped before the first step past its last reader,
        # so the host holds about one layer's at a time, as the device does.
        dead: dict[int, list[str]] = {}
        for root, i in last.items():
            if root not in kept:
                dead.setdefault(i + 1, []).append(root)
        for i, step in enumerate([*self.steps, None]):
            for root in dead.get(i, ()):
                buffers.pop(root, None)
            for s in host.get(i, ()):
                s.fn(
                    *(view(h)[valid(h)] for h in s.reads),
                    *(view(h) for h in s.writes),
                )
            if step is None:
                break
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


def _gather_reference(step: Step, ids: np.ndarray, view) -> None:
    """Run a per-call gather's step on the host.

    Writes the table's rows ``ids`` names, each clipped to the table
    where the device made them.
    """
    table, out = (view(h) for h in (step.inputs[0], step.outputs[0]))
    table = table.reshape(table.shape[0], -1)
    rows = ids.astype(np.int64)
    assert step.gather is not None, "a gather's step"
    if step.gather.role != "input":
        rows = np.clip(rows, -len(table), len(table) - 1)
    out.reshape(-1, table.shape[1])[: len(rows)] = table[rows]


class Recorder:
    """Records operator calls on handles while a graph's body runs."""

    def __init__(
        self,
        name: str,
        profile: Profile | None = None,
        held: Mapping[int, tuple[str, object]] | None = None,
        inputs: Iterable[str] = (),
    ) -> None:
        self.name = name
        self.profile = profile
        held = held or {}
        self._held_arrays = [
            x.array if isinstance(x, Weight) else x
            for _, x in held.values()
            if isinstance(x, (Weight, np.ndarray))
        ]
        self.steps: list[Step] = []
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
        self.host: list[HostStep] = []
        self._counter = itertools.count()
        self._constants: dict[tuple, np.ndarray] = {}
        self._names: dict[int, str] = {}
        for key, (path, x) in held.items():
            self._names.setdefault(key, path)
            if isinstance(x, Weight):
                self._names.setdefault(id(x.array), path)
        self._taken = {*self._names.values(), *inputs}

    def fresh(self, name: str) -> str:
        """Return a buffer name no buffer of the graph has.

        ``name``, or the first of ``name_1``, ``name_2``, ...; a name the
        recorder makes up never aliases one it was given.
        """
        candidates = (f"{name}_{k}" for k in itertools.count(1))
        free = next(
            n for n in itertools.chain([name], candidates) if n not in self._taken
        )
        self._taken.add(free)
        return free

    def constant(self, value, width: int, dtype) -> np.ndarray:
        """Return a row of ``width`` ``value``s in ``dtype``.

        One array, so one weight buffer, per number, width and dtype.
        """
        key = (float(value), width, bfp.dtype_name(dtype))
        if key not in self._constants:
            self._constants[key] = np.full(width, value, dtype)
        return self._constants[key]

    def __enter__(self):
        self._token = graph_recorder.set(self)
        return self

    def __exit__(self, *exc):
        graph_recorder.reset(self._token)

    def operand(self, x) -> Handle:
        if isinstance(x, Handle):
            if isinstance(x.layout, Strided) and x.layout.window is not None:
                # A run from a per-call start taken whole ends inside its axis.
                _, start, width, n = x.layout.window
                end = start + width
                assert isinstance(end, Affine), "a per-call start"
                self.limit(end, 0, n + 1, x)
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
                self.states[key] = (x, Handle.whole(x.shape, x.dtype, x.name, "state"))
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
                    Handle.whole(
                        array.shape, np.dtype(array.dtype).type, name, "weight"
                    ),
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
        """Return what an output a call gives would write over that no call may.

        ``"weight"`` or ``"input"``, through any view of it, else None.
        """
        if isinstance(given, State):
            return None
        if not isinstance(given, Handle):
            return "weight"
        return given.role if given.role in ("weight", "input") else None

    def check_outputs(self, cls, outputs) -> None:
        """Raise ``TypeError`` for a given output that is a weight, an input, or a view of one.

        As a weight passed where an optional input was meant.
        """
        for given in outputs:
            kind = self.overwrites(given)
            if kind is None:
                continue
            keywords = [
                f"{m.name}="
                for m in cls.declaration.operands
                if m.fills and m.when is not None
            ]
            hint = f"; an optional input is given by keyword ({', '.join(keywords)})"
            raise TypeError(
                f"{cls.__name__}: the output given, {list(given.shape)}, is a "
                f"graph {kind} or a view of one, which a call does not write over"
                f"{hint if keywords else ''}"
            )

    def call(self, target, args, kwargs):
        """Record ``target(*args, **kwargs)``: inputs then optional outputs.

        Keywords give optional inputs, per-call value handles or, for a
        class, construction; a refusal re-raises naming the graph,
        operator and operands.
        """
        try:
            return self._call(target, args, kwargs)
        except (TypeError, ValueError, IndexError) as e:
            cls = target if isinstance(target, type) else type(target)
            given = ", ".join(self._describe(a) for a in args)
            e.args = (f"{self.name}: {cls.__name__}({given}): {e}", *e.args[1:])
            raise

    def _describe(self, x) -> str:
        """Describe ``x`` in the body's terms.

        A handle's buffer, a held tensor's path, else its kind and shape.
        """
        if isinstance(x, Handle):
            return str(x.ref())
        if isinstance(x, State) and x.name:
            return x.name
        array = x.array if isinstance(x, Weight) else x
        name = self._names.get(id(x)) or self._names.get(id(array))
        kind = "ndarray" if isinstance(x, np.ndarray) else type(x).__name__
        return name or f"{kind} {list(x.shape) if is_operand(x) else []}"

    def _call(self, target, args, kwargs):
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = cls.call_operands(args, kwargs)
        self.check_outputs(cls, outputs)
        names = list(inputs)
        operands = [self.operand(a) for a in [*inputs.values(), *outputs]]
        values = {
            k: kwargs.pop(k)
            for k in list(kwargs)
            if isinstance(kwargs[k], (PerCall, Affine))
        }
        if any(isinstance(h.layout, Gather) for h in operands):
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
            op = target
            own = self._split_values(type(op), values)
            operands = _take_views(type(op), operands, {}, own)
            if kwargs or values:
                raise TypeError(
                    f"{type(op).__name__} instance called with unexpected keyword "
                    f"arguments {sorted(kwargs) + sorted(values)}"
                )
            params = type(op).declaration.params
            type(op).declaration.infer(
                {name: h.shape for name, h in zip(names, operands)},
                [h.shape for h in operands[len(names) :]],
                **{n: vars(op)[n] for n in params if vars(op)[n] is not None},
            )
        if values:
            raise TypeError(
                f"{type(op).__name__} has no per-call value {sorted(values)}"
            )
        for name, value in own.items():
            self._bind(op, name, value)
        return self._record(op, operands, called)

    def _gather(self, target, operands: list[Handle], extra) -> Handle:
        """Record ``Copy(table[ids])`` with per-call ``ids`` as a ``Gather``.

        The host encodes an input's ids into control words each call, and
        a word source writes device-made ids into the template.
        """
        from iron.operators.copy import Copy  # a cycle
        from iron.operators.copy import Gather as GatherRows

        view = operands[0]
        assert isinstance(view.layout, Gather), "a gather"
        ids, row = view.layout.rows, math.prod(view.shape[1:])
        rows = view.buffer.nbytes // (row * bfp.itemsize(view.dtype))
        table = Handle(view.buffer, (rows, *view.shape[1:]), view.dtype)
        if target is not Copy or len(operands) != 1 or extra:
            raise TypeError(
                f"{view!r} takes the rows the input {ids.name!r} names each "
                f"call; only a Copy of it alone does, Copy(table[ids])"
            )
        given: dict[str, Any] = dict(
            rows=ids.shape[0],
            table_rows=table.shape[0],
            row=row,
            dtype=table.dtype,
        )
        if self.profile is None:
            op = GatherRows(**given)
        else:
            op = self.profile.make(GatherRows, **given)
        bound = ids.valid.get(0)
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
            control = Handle.whole((start + op.words,), np.uint32, ids.name, "input")
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
        assert isinstance(out, Handle), "one output"
        self.steps[-1].gather = ids
        return out if out.shape == view.shape else out.reshape(view.shape)

    def on_host(self, fn: Callable[..., None], reads, writes) -> None:
        """Record ``fn`` to run on the host before the next step (``HostStep``).

        Each read is contiguous and each write a contiguous part of a state.
        """
        reads = tuple(self.operand(x) for x in reads)
        writes = tuple(self.operand(x) for x in writes)
        for h in reads:
            if not isinstance(h.layout, Dense):
                raise TypeError(f"on_host reads contiguous handles, not {h!r}")
        for h in writes:
            if h.role != "state" or not isinstance(h.layout, Dense) or h.valid:
                raise TypeError(f"on_host writes contiguous parts of states, not {h!r}")
        self.host.append(HostStep(len(self.steps), fn, reads, writes))

    @staticmethod
    def _split_values(op_cls, kwargs) -> dict:
        values = {m.name for m in op_cls.declaration.per_calls}
        return {k: kwargs.pop(k) for k in list(kwargs) if k in values}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        inferred = cls.declaration.infer(
            {name: h.shape for name, h in inputs.items()},
            [h.shape for h in outputs],
            **kwargs,
        )
        given = {**kwargs, **inferred}
        if self.profile is not None:
            return self.profile.make(cls, **given)
        pinned = frozenset(
            name
            for name, value in given.items()
            if name in cls.declaration.tunables and value is not None
        )
        return cls(**given, pinned=pinned)

    def _output_bounds(self, op, buffer, rank: int) -> dict:
        bounds = {}
        for binding in self.bindings:
            if binding.op is not op or binding.member.bounds is None:
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
        # An offset may floor; an extent's derived words take a linear or
        # clamped one.
        if isinstance(value, PerCall) or op.value(name).bounds is not None:
            value = _count(value)
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
        """Record ``op`` on ``operands``.

        ``called`` are the operands as the call gave them, a view where
        ``operands`` holds its buffer.
        """
        called = operands if called is None else called
        buffers = op.buffers
        ins = [b for b in buffers if b.fills]
        outs = [b for b in buffers if b.role is Out]
        given_outs = operands[len(ins) :]
        for h, b in zip(operands, ins + outs):
            shape = tuple(b.shape)
            if bfp.dtype_name(h.dtype) != bfp.dtype_name(b.dtype):
                raise TypeError(
                    f"{type(op).__name__}.{b.name} is {bfp.dtype_name(b.dtype)}; "
                    f"operand {h!r} is {bfp.dtype_name(h.dtype)}"
                )
            bounds = (
                h.valid if len(h.shape) == len(shape) else _rescale_bounds(h, shape)
            )
            for axis, count in bounds.items():
                extent = next(
                    (
                        m
                        for m in type(op).declaration.per_calls
                        if m.bounds is not None and b.extent_axis(m) == axis
                    ),
                    None,
                )
                if extent is None:
                    raise TypeError(
                        f"{type(op).__name__}.{b.name} cannot be bounded per call on "
                        f"axis {axis} ({count}): it declares no per_call(bounds=) for the "
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
                # An Out(like=x) has x's shape and bounds as the call gave
                # x: (rows, cols) stays (rows, cols) through SiLU.
                bounds: dict = {}
                if b.like is not None:
                    like = called[[i.name for i in ins].index(b.like.name)]
                    shape, bounds = like.shape, dict(like.valid)
                # A copy of a view has the view's; like= gives the buffer's dims.
                elif type(op).accept_views and called[0].elements == b.elements:
                    shape, bounds = called[0].shape, dict(called[0].valid)
                if not bounds:
                    bounds = self._output_bounds(op, b, len(shape))
                name = self.fresh(f"{type(op).__name__.lower()}{next(self._counter)}")
                h = Handle.whole(shape, b.dtype, name, "intermediate")
                h = dataclasses.replace(h, valid=bounds)
                slots.append(h)
                outputs.append(h)
        self.steps.append(
            Step(op, slots, operands[: len(ins)], outputs + list(given_outs))
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
    ) -> Recording:
        """Return the recorded graph.

        ``carry`` is the next value of each carried value, whose handles
        are outputs too.
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
                if h.layout != Dense():
                    pinned.setdefault(h.name, h.buffer.nbytes)
        # A host write's bytes are the last the host wrote there.
        written = {h.name for step in self.steps for h in step.outputs}
        for s in self.host:
            for h in s.writes:
                if h.name in written:
                    raise ValueError(
                        f"{self.name}: on_host writes {h!r}, which a step writes too"
                    )
        return Recording(
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
            host=self.host,
        )

    def limit(
        self,
        expression: Affine,
        lo: int,
        hi: int,
        view: Handle,
        plus: Affine | None = None,
    ) -> None:
        """Record that a call's ``expression``, plus ``plus`` where given, must lie in ``[lo, hi)``.

        For ``view``, which it indexes or bounds.
        """
        self.limits.append(Limit(expression, lo, hi, repr(view), plus))
