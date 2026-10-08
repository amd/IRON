# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tracing a graph: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import inspect
import itertools
import math
from collections.abc import Callable, Hashable, Iterable, Mapping

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp

from ..declare import Direction, Operator
from ..declare.bound import BoundValue
from ..declare.member import Extent, _Value
from ..declare.operator import graph_tracer
from ..design import device_symbol
from ..image.sequence import OperatorSequence
from .handle import (
    Affine,
    Handle,
    State,
    Value,
    Weight,
    _HostView,
    _rescale_bounds,
    _tensor_dtype,
    is_operand,
)


@dataclasses.dataclass
class TracedStep:
    op: Operator
    slots: list  # one handle per declared buffer
    inputs: list
    outputs: list

    @property
    def names(self) -> list:
        return [h.buffer_name for h in self.slots]


@dataclasses.dataclass(frozen=True)
class Binding:
    """A graph value bound to one operator's value member, written per call
    as ``expression``.
    """

    op: Operator
    member: BoundValue
    expression: Affine

    @property
    def symbol(self) -> str:
        return device_symbol(self.op, self.member)


def _unbounded(h: Handle) -> Handle:
    if not h.bounds:
        return h
    return Handle(
        h.shape, h.dtype, h.name, h.role, h.parent, h.start, h.tap, h.index_by
    )


def _take_views(cls, operands, kwargs, values):
    """Hand each view operand's pattern to the operator (``cls.accept_views``)
    and stand its parent in.
    """
    out = []
    for i, h in enumerate(operands):
        if i < len(cls.accept_views):
            param, offset_member = cls.accept_views[i]
            tap = TensorAccessPattern.full(h.shape or (1,)) if h.tap is None else h.tap
            kwargs.setdefault(param, tap)
            if h.bounds:
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
    steps: list
    inputs: list
    outputs: list  # returned, then carried handles not returned
    values: list
    pinned: dict  # buffer name -> nbytes, for weights, states and slice parents
    weights: dict[int, tuple[object, Handle]]
    states: dict[int, tuple[State, Handle]]
    bindings: list[Binding]
    returned: list = dataclasses.field(default_factory=list)
    carry: dict[str, Handle | Affine] = dataclasses.field(default_factory=dict)
    feedback: list[str] = dataclasses.field(default_factory=list)
    # An input the device reads as words the host encodes from it and a
    # buffer's device address (a gather's ids): input -> (buffer, encode).
    encoders: dict[str, tuple[str, Callable[[np.ndarray, int], np.ndarray]]] = (
        dataclasses.field(default_factory=dict)
    )
    # A per-call value the graph fills in rather than the caller, from a
    # buffer's device address (a gather by ids the device made):
    # value -> (buffer, address -> words by name, its word's name).
    addresses: dict[str, tuple[str, Callable[[int], dict], str]] = dataclasses.field(
        default_factory=dict
    )

    @property
    def runlist(self) -> list:
        return [(s.op, *s.names) for s in self.steps]

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

    @property
    def input_args(self) -> list:
        return [h.name for h in self.inputs]

    @property
    def output_args(self) -> list:
        return [h.name for h in self.outputs]

    def sequence(self, name=None, **kwargs):
        kwargs.setdefault("buffer_sizes", dict(self.pinned))
        kwargs.setdefault("share_designs", True)
        kwargs.setdefault("feedback_args", list(self.feedback))
        return OperatorSequence(
            name or self.name,
            self.runlist,
            self.input_args,
            self.output_args,
            **kwargs,
        )

    def with_operators(self, replace: Mapping[int, Operator]) -> TracedGraph:
        """This graph with operators swapped, keyed by ``id`` of the one each
        replaces; a binding moves to the replacement's same-named value.
        """
        steps = [
            dataclasses.replace(s, op=replace.get(id(s.op), s.op)) for s in self.steps
        ]
        bindings = []
        for b in self.bindings:
            new = replace.get(id(b.op))
            if new is None:
                bindings.append(b)
                continue
            member = next(v for v in new.values if v.name == b.member.name)
            bindings.append(Binding(new, member, b.expression))
        return dataclasses.replace(self, steps=steps, bindings=bindings)

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


class Tracer:
    """Records operator calls on handles while a graph's body runs."""

    checks = True

    def __init__(
        self,
        name: str,
        names: dict[int, str] | None = None,
        inputs: Iterable[str] = (),
    ) -> None:
        self.name = name
        self.steps: list[TracedStep] = []
        self.weights: dict[int, tuple[object, Handle]] = {}
        self.states: dict[int, tuple[State, Handle]] = {}
        self.bindings: list[Binding] = []
        self._bound: dict[int, dict] = {}
        self.encoders: dict[str, tuple[str, Callable]] = {}
        self.addresses: dict[str, tuple[str, Callable, str]] = {}
        self._counter = itertools.count()
        self._names = names or {}
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

    def __enter__(self):
        self._token = graph_tracer.set(self)
        return self

    def __exit__(self, *exc):
        graph_tracer.reset(self._token)

    def accepts(self, args) -> bool:
        return all(is_operand(a) for a in args)

    def viewed(self, x: State | Weight):
        return self.operand(x)

    def operand(self, x) -> Handle:
        if isinstance(x, Handle):
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
            key = id(x)
            if key not in self.weights:
                name = self._names.get(key) or self.fresh(f"w{len(self.weights)}")
                self.weights[key] = (
                    x,
                    Handle(x.shape, _tensor_dtype(x), name, "weight"),
                )
            return self.weights[key][1]
        raise TypeError(f"{x!r} is not a graph handle, a state, or a tensor")

    def call(self, target, args, kwargs):
        """Record ``target(*args, **kwargs)``: inputs, optionally followed by
        outputs; keywords are optional inputs, per-call value handles, or
        construction arguments when ``target`` is a class.
        """
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = cls.call_operands(args, kwargs)
        names = list(inputs)
        operands = [self.operand(a) for a in [*inputs.values(), *outputs]]
        values = {
            k: kwargs.pop(k)
            for k in list(kwargs)
            if isinstance(kwargs[k], (Value, Affine))
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
            op = target
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
        op = target.per_call_gather(
            rows=ids.shape[0],
            table_rows=table.shape[0],
            row=math.prod(table.shape[1:]),
            dtype=table.dtype,
        )
        if ids.role == "input":
            if ids.name in self.encoders:
                raise ValueError(f"the input {ids.name!r} gathers from one table once")
            control = Handle((op.words,), np.uint32, ids.name, "input")
            self.encoders[ids.name] = (table.name, op.control_words)
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
                self._bind(source, member, Value(name, "scratchpad", np.int32))
            self._record(source, [ids, control])
        out = self._record(op, [table, control])
        return out if out.shape == view.shape else out.reshape(view.shape)

    @staticmethod
    def _split_values(op_cls, kwargs) -> dict:
        names = {m.name for m in op_cls._members if isinstance(m, _Value)}
        return {k: kwargs.pop(k) for k in list(kwargs) if k in names}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        """``cls`` on ``inputs`` (by name) and ``outputs``, its extents and
        optional-input flags inferred from them.
        """
        inferred = cls.infer(
            {name: h.shape for name, h in inputs.items()},
            [h.shape for h in outputs],
            **kwargs,
        )
        return cls(**{**kwargs, **inferred})

    def _output_bounds(self, op, buffer, rank: int) -> dict:
        """An output sized by a bounded extent's field is bounded the same way."""
        bounds = {}
        for binding in self.bindings:
            if binding.op is not op or not isinstance(binding.member.member, Extent):
                continue
            axis = buffer.extent_axis(binding.member.member)
            if axis is not None:
                bounds[axis] = binding.expression
        return bounds

    def _bind(self, op, name, value) -> None:
        if not isinstance(value, (Value, Affine)):
            raise TypeError(
                f"{type(op).__name__}.{name} takes a per-call value handle (a "
                f"keyword-only parameter of the graph's body), got {value!r}"
            )
        value = value.affine()
        bound = self._bound.setdefault(id(op), {})
        if name in bound and bound[name] != value:
            raise ValueError(
                f"{type(op).__name__}.{name} is bound to {bound[name]} at an "
                f"earlier call site and to {value} here; one instance has one "
                f"value, bind one expression at every site or use two instances"
            )
        if name not in bound:
            op.use_value(name, value.name)
            bound[name] = value
            member = next(v for v in op.values if v.name == name)
            self.bindings.append(Binding(op, member, value))

    def _record(self, op, operands, called=None):
        """Record ``op`` on ``operands``; ``called`` are the operands as the
        call gave them, a view where ``operands`` holds its buffer.
        """
        called = operands if called is None else called
        # A shape that Selects on an auto() field is the device's: resolve()
        # gives it, unchecked, so a profile may still tune the op.
        unset = {n for n in type(op)._auto_fields if getattr(op, n) is None}
        shaped = op
        if any(unset & m.shape.names() for m in op._members_io()):
            shaped = op.resolve(op.dev)
        buffers = shaped.buffers
        ins = [b for b in buffers if b.direction.fills]
        outs = [b for b in buffers if b.direction is Direction.OUT]
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
        for h, b in zip(operands, ins + outs):
            # Another rank matches on the count; the same rank must match the
            # shape, or a transposed weight would pass.
            shape = tuple(b.shape)
            wrong = (
                tuple(h.shape) != shape
                if len(h.shape) == len(shape)
                else h.elements != b.elements
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
                        for m in type(op)._members
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
            if b.direction is Direction.IN:
                slots.append(next(it))
            elif b.direction is Direction.INOUT:
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
                        bounds = dict(operands[like].bounds)
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
            values,
            pinned,
            self.weights,
            self.states,
            self.bindings,
            returned,
            next_values,
            encoders=self.encoders,
            addresses=self.addresses,
        )


class _ReferenceTracer(Tracer):
    """Runs each call as ``op.reference(*inputs, *outputs, **values)`` on host
    tensors, a state written in place and per-call values as plain numbers.
    """

    # Operators are constructed at a bounded call's valid rows, which only
    # their reference() runs at.
    checks = False

    def operand(self, x):
        return x

    def viewed(self, x: State | Weight):
        if isinstance(x, Weight):
            return x.array
        if x.host is None:
            x.host = np.zeros(x.shape, dtype=x.dtype)
        return _HostView(x, x.shape)

    def call(self, target, args, kwargs):
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = cls.call_operands(args, kwargs)
        n_views = len(cls.accept_views)
        tensors, patterns = [], []
        for i, a in enumerate([*inputs.values(), *outputs]):
            pattern = None
            if isinstance(a, _HostView):
                pattern = a.pattern()
                if pattern.tap is not None and i < n_views:
                    a = a.state.host
                else:
                    pattern, a = None, a.tensor()
            elif isinstance(a, State):
                if a.host is None:
                    a.host = np.zeros(a.shape, dtype=a.dtype)
                a = a.host
            elif isinstance(a, Weight):
                a = a.array
            tensors.append(a)
            patterns.append(pattern)
        n_in = len(inputs)
        if isinstance(target, type):
            values = self._split_values(cls, kwargs)
            shapes = [
                Handle(t.shape, _tensor_dtype(t), "", "input") if p is None else p
                for t, p in zip(tensors, patterns)
            ]
            shapes = _take_views(cls, shapes, kwargs, {})
            op = self._construct(cls, dict(zip(inputs, shapes)), shapes[n_in:], kwargs)
        else:
            op = target
            values = self._split_values(cls, kwargs)
        values = {k: v for k, v in values.items() if v is not None}
        # A reference that takes no output returns its result, which lands in
        # the given output below.
        positional = [
            p
            for p in inspect.signature(op.reference).parameters.values()
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        ]
        result = op.reference(*tensors[: max(n_in, len(positional))], **values)
        # Shaped as Tracer._record shapes a flat output.
        outs = [b for b in op.buffers if b.direction is Direction.OUT]
        fresh = len(tensors) == n_in and len(outs) == 1
        if fresh and result is not None and len(outs[0].shape) == 1:
            called = [t if p is None else p for t, p in zip(tensors, patterns)]
            like = next(
                (t for t in called if math.prod(t.shape) == outs[0].elements), None
            )
            if like is not None:
                result = result.reshape(like.shape, copy=False)
        for given in tensors[n_in:]:
            if result is not None and result is not given:
                given[...] = np.asarray(result).reshape(given.shape)
        return result
