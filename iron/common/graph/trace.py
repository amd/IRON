# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tracing a graph: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import itertools
import math
from collections.abc import Hashable, Mapping

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp

from ..declare import Direction, Operator
from ..declare.bound import BoundValue
from ..declare.infer import call_operands, infer, infer_kwargs, operand_flags
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
    slots: list  # the handle in each of the operator's buffers, in declaration order
    inputs: list  # handles consumed
    outputs: list  # handles produced

    @property
    def names(self) -> list:
        """Buffer names in declaration order, as the runlist uses them."""
        return [h.buffer_name for h in self.slots]


@dataclasses.dataclass(frozen=True)
class Binding:
    """A per-call value of the graph, bound to one operator's value member.

    ``member`` is the value member the site binds, and ``expression`` what
    it is written per call: a graph value, scaled and offset (a per-call
    index on a view is scaled by the axis stride, to elements).
    """

    op: Operator
    member: BoundValue
    expression: Affine

    @property
    def symbol(self) -> str:
        """The device symbol the host writes this value through."""
        return device_symbol(self.op, self.member)


def _unbounded(h: Handle) -> Handle:
    """``h`` without its per-call bounds (the same buffer)."""
    if not h.bounds:
        return h
    return Handle(
        h.shape, h.dtype, h.name, h.role, h.parent, h.start, h.tap, h.index_by
    )


def _take_views(cls, operands, kwargs, values):
    """Hand each view operand's pattern to the operator and stand its parent in.

    A class that takes views names, in operand order, the param that holds
    each operand's pattern and the per-call value a dynamic index binds
    (``Copy.accept_views``). Any other operator takes contiguous operands.
    """
    accept = getattr(cls, "accept_views", ())
    out = []
    for i, h in enumerate(operands):
        if i < len(accept):
            param, offset_member = accept[i]
            # A scalar (one element indexed out of a vector) is one element.
            tap = TensorAccessPattern.full(h.shape or (1,)) if h.tap is None else h.tap
            kwargs.setdefault(param, tap)
            if h.bounds:
                # A bound on one axis of the view: the pattern keeps that
                # axis and the copy patches its size from the value.
                (axis, count), *more = h.bounds.items()
                if more:
                    raise ValueError(f"{h!r}: a copy takes one bounded axis")
                kwargs.setdefault(f"{param}_bound", axis)
                values[f"{param}_valid"] = count
            if h.index_by is not None:
                values[offset_member] = h.index_by
            # The bound is the pattern's now: the buffer stands in, plain.
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

    ``weights`` and ``states`` are keyed by the identity of the object the
    function closed over, and hold that object, so the key stays its own.
    ``carry`` is the next value of each carried value, by name; a handle
    there is an output buffer too, so the host can read it back.
    """

    name: str
    steps: list
    inputs: list  # Handles, in parameter order
    outputs: list  # Handles returned, then carried handles not returned
    values: list  # Values, in parameter order
    pinned: dict  # buffer name -> nbytes, for weights, states and slice parents
    weights: dict[int, tuple[object, Handle]]  # id(tensor) -> (tensor, Handle)
    states: dict[int, tuple[State, Handle]]  # id(State) -> (State, Handle)
    bindings: list[Binding]
    returned: list = dataclasses.field(default_factory=list)  # Handles returned
    carry: dict[str, Handle | Affine] = dataclasses.field(default_factory=dict)
    # Buffers drained to the image's feedback argument (an Emit's image).
    feedback: list[str] = dataclasses.field(default_factory=list)

    @property
    def runlist(self) -> list:
        return [(s.op, *s.names) for s in self.steps]

    @property
    def residents(self) -> dict[str, Hashable]:
        """Buffer name -> storage key of every weight and state.

        The key is the identity of the tensor or ``State`` closed over:
        the same in every trace of the function, so each version compiled
        from it addresses one copy.
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
        """The ``OperatorSequence`` this graph lowers to (the image builder)."""
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
        replaces: same host ABI, another build (a narrower array, say). A
        binding on a swapped operator moves to the same-named value of its
        replacement.
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
        """One operator per distinct array, in runlist order."""
        seen = {}
        for op in self.operators:
            seen.setdefault(op.array_key(), op)
        return list(seen.values())


class Tracer:
    """Records operator calls on handles while a graph's body runs."""

    # Whether an operator constructed under it checks its shape (validate(),
    # compatible()).
    checks = True

    def __init__(self, name: str, names: dict[int, str] | None = None):
        self.name = name
        self.steps: list[TracedStep] = []
        self.weights: dict[int, tuple[object, Handle]] = {}
        self.states: dict[int, tuple[State, Handle]] = {}
        self.bindings: list[Binding] = []
        self._bound: dict[int, dict] = {}  # id(op) -> {member: Affine}
        self._counter = itertools.count()
        # A name per tensor and state the graph holds, by identity.
        self._names = names or {}

    def __enter__(self):
        self._token = graph_tracer.set(self)
        return self

    def __exit__(self, *exc):
        graph_tracer.reset(self._token)

    def accepts(self, args) -> bool:
        """Whether a call on ``args`` is a step: every one an operand."""
        return all(is_operand(a) for a in args)

    # -- operands ---------------------------------------------------------

    def viewed(self, x: State | Weight):
        """What stands for a state or weight viewed inside the graph's body:
        its handle.
        """
        return self.operand(x)

    def operand(self, x) -> Handle:
        if isinstance(x, Handle):
            return x
        if isinstance(x, State):
            key = id(x)
            if key not in self.states:
                x.name = x.name or self._names.get(key) or f"state{len(self.states)}"
                self.states[key] = (x, Handle(x.shape, x.dtype, x.name, "state"))
            return self.states[key][1]
        if is_operand(x):
            key = id(x)
            if key not in self.weights:
                name = self._names.get(key) or f"w{len(self.weights)}"
                self.weights[key] = (
                    x,
                    Handle(x.shape, _tensor_dtype(x), name, "weight"),
                )
            return self.weights[key][1]
        raise TypeError(f"{x!r} is not a graph handle, a state, or a tensor")

    # -- calls -------------------------------------------------------------

    def call(self, target, args, kwargs):
        """Record ``target(*args, **kwargs)``.

        ``args`` are the operator's inputs, optionally followed by its
        outputs (a state it writes into); an optional input is a keyword
        (``RMSNorm(x, weight=w)``). The other ``kwargs`` are per-call value
        handles for its value members, and otherwise construction arguments
        (dimensions, tunables, flags) when ``target`` is a class.
        """
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = call_operands(cls, args, kwargs)
        names = list(inputs)
        operands = [self.operand(a) for a in [*inputs.values(), *outputs]]
        # A keyword whose value is a per-call handle (or an expression of
        # one) binds a value member.
        values = {
            k: kwargs.pop(k)
            for k in list(kwargs)
            if isinstance(kwargs[k], (Value, Affine))
        }
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
        return self._record(op, operands)

    @staticmethod
    def _split_values(op_cls, kwargs) -> dict:
        names = {m.name for m in op_cls._members if isinstance(m, _Value)}
        return {k: kwargs.pop(k) for k in list(kwargs) if k in names}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        """``cls`` on ``inputs`` (by name) and ``outputs``: an optional
        input's flag is set by its presence, as the extents are by the
        shapes, not by a keyword of the call.
        """
        inferred = infer(
            cls,
            *[h.shape for h in inputs.values()],
            outputs=[h.shape for h in outputs],
            **{**infer_kwargs(cls, kwargs), **operand_flags(cls, inputs, kwargs)},
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

    def _record(self, op, operands):
        buffers = op.buffers
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
            # A buffer takes an operand of another rank with the same count
            # (a flat buffer, a stack); at the same rank the shapes must agree,
            # or a transposed weight would pass on its element count.
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
            # Of another rank, the operand is the buffer reshaped: a bound on
            # its rows is so many more of the buffer's (a flat buffer's elements).
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
                outputs.append(h)  # in place: the handle given is the result
            elif given_outs:
                slots.append(next(given))  # written where the caller said
            else:
                shape = b.shape
                # A flat-declared output (an elementwise operator) keeps the
                # shape of the operand it is the size of, so a (rows, cols)
                # activation stays (rows, cols) through SiLU.
                bounds: dict = {}
                if len(shape) == 1:
                    like = next((h for h in operands if h.elements == b.elements), None)
                    if like is not None:
                        shape = like.shape
                        bounds = dict(like.bounds)  # sized by it: bounded like it
                if not bounds:
                    bounds = self._output_bounds(op, b, len(shape))
                h = Handle(
                    shape,
                    b.dtype,
                    f"{type(op).__name__.lower()}{next(self._counter)}",
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

    # -- the result ----------------------------------------------------------

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
        # A slice's parent must have an explicit size, whatever produced it.
        for step in self.steps:
            for h in step.inputs + step.outputs:
                if h.parent is not None and h.parent.role == "intermediate":
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
        )


class _ReferenceTracer(Tracer):
    """Runs each operator's CPU reference on host tensors as the graph is traced.

    Each call becomes ``op.reference(*inputs, *outputs, **values)``: the
    tensors the graph passed, a state passed as an output as its host tensor
    (the reference writes it in place, as the device writes the buffer), and
    the per-call values the site binds, by name, as plain numbers. So a
    graph's reference models the values too: a cache offset moves the copy,
    a vector size masks the softmax.
    """

    # Operators are constructed at the valid rows of a bounded call, which
    # only their reference() runs at.
    checks = False

    def operand(self, x):
        return x

    def viewed(self, x: State | Weight):
        """A state viewed in the reference: a view of its host tensor that
        remembers its shape and key (``_HostView``). A weight's is
        numpy's own view, since nothing writes it.
        """
        if isinstance(x, Weight):
            return x.array
        if x.host is None:
            x.host = np.zeros(x.shape, dtype=x.dtype)
        return _HostView(x, x.shape)

    def call(self, target, args, kwargs):
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = call_operands(cls, args, kwargs)
        n_views = len(getattr(cls, "accept_views", ()))
        tensors, patterns = [], []
        for i, a in enumerate([*inputs.values(), *outputs]):
            pattern = None
            if isinstance(a, _HostView):
                pattern = a.pattern()
                if pattern.tap is not None and i < n_views:
                    a = a.state.host  # the whole tensor, walked by the pattern
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
            # A per-call value's number goes to the reference, not to
            # construction.
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
        result = op.reference(*tensors, **values)
        # A flat-declared output the call did not give keeps the shape of the
        # operand it is the size of, as the traced handle does
        # (``Tracer._record``): a view, never a copy.
        outs = [b for b in op.buffers if b.direction is Direction.OUT]
        fresh = len(tensors) == n_in and len(outs) == 1
        if fresh and result is not None and len(outs[0].shape) == 1:
            like = next(
                (t for t in tensors if math.prod(t.shape) == outs[0].elements), None
            )
            if like is not None:
                result = result.reshape(like.shape, copy=False)
        # A state written in place keeps its host tensor; a result returned
        # for a given output lands in it.
        for given in tensors[n_in:]:
            if result is not None and result is not given:
                given[...] = np.asarray(result).reshape(given.shape)
        return result
