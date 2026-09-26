# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tracing a graph function: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import itertools
from collections.abc import Hashable

import numpy as np
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare import Operator
from ..declare.bound import BoundValue
from ..declare.infer import infer, infer_kwargs
from ..declare.member import Extent, _Value
from ..declare.member import _Buffer as _Buffer_
from ..design import device_symbol
from ..image.sequence import OperatorSequence
from ..tiling import Walk
from .handle import (
    Handle,
    State,
    Value,
    _HostView,
    _HostViews,
    _tensor_dtype,
    is_operand,
)

_STACK: list = []


def current():
    """The tracer a graph function is being traced under, or ``None``."""
    return _STACK[-1] if _STACK else None


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

    ``member`` is the value member the site binds.
    """

    op: Operator
    member: BoundValue
    value: Value
    scale: int = 1  # a per-call index on a view: the axis stride, in elements

    @property
    def symbol(self) -> str:
        """The device symbol the host writes this value through."""
        return device_symbol(self.op, self.member)


def _unbounded(h: Handle) -> Handle:
    """``h`` without its per-call bounds (the same buffer)."""
    if not h.bounds:
        return h
    return Handle(
        h.shape, h.dtype, h.name, h.role, h.parent, h.start, h.walk, h.index_by
    )


def _take_views(cls, operands, kwargs, values, scales):
    """Hand each view operand's walk to the operator and stand its parent in.

    A class that takes views names, in operand order, the param that holds
    each operand's walk and the per-call value a dynamic index binds
    (``Copy.accept_views``). Any other operator takes contiguous operands.
    """
    accept = getattr(cls, "accept_views", ())
    out = []
    for i, h in enumerate(operands):
        if i < len(accept):
            param, offset_member = accept[i]
            walk = Walk.of(h.shape) if h.walk is None else h.walk
            if h.bounds:
                # A bound on one axis of the view: the walk keeps that axis
                # and the copy patches its size from the value.
                (axis, (value, scale)), *more = h.bounds.items()
                if more:
                    raise ValueError(f"{h!r}: a copy takes one bounded axis")
                walk = dataclasses.replace(walk, bounded=axis)
                values[f"{param}_valid"] = value
                scales[f"{param}_valid"] = scale
            kwargs.setdefault(param, walk)
            if h.index_by is not None:
                value, stride = h.index_by
                values[offset_member] = value
                scales[offset_member] = stride
            # The bound is the walk's now: the buffer stands in, plain.
            out.append(_unbounded(h.parent if h.walk is not None else h))
        elif h.walk is not None:
            raise TypeError(
                f"{cls.__name__} takes a contiguous operand at position {i}, not "
                f"the view {h!r}; Copy takes views"
            )
        else:
            out.append(h)
    return out


@dataclasses.dataclass
class TracedGraph:
    """What tracing a graph function for given shapes produced.

    ``weights`` and ``states`` are keyed by the identity of the object the
    function closed over, and hold that object, so the key stays its own.
    """

    name: str
    steps: list
    inputs: list  # Handles, in parameter order
    outputs: list  # Handles returned
    values: list  # Values, in parameter order
    pinned: dict  # buffer name -> nbytes, for weights, states and slice parents
    weights: dict[int, tuple[object, Handle]]  # id(tensor) -> (tensor, Handle)
    states: dict[int, tuple[State, Handle]]  # id(State) -> (State, Handle)
    bindings: list[Binding]

    @property
    def runlist(self) -> list:
        return [(s.op, *s.names) for s in self.steps]

    @property
    def residents(self) -> dict[str, Hashable]:
        """Buffer name -> storage key of every weight and state.

        The key is the identity of the tensor or :class:`State` closed over:
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
        """The :class:`OperatorSequence` this graph lowers to (the image builder)."""
        kwargs.setdefault("buffer_sizes", dict(self.pinned))
        kwargs.setdefault("share_designs", True)
        return OperatorSequence(
            name or self.name,
            self.runlist,
            self.input_args,
            self.output_args,
            **kwargs,
        )

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
    """Records operator calls on handles while a graph function runs."""

    def __init__(self, name: str, names_from=None):
        self.name = name
        self.steps: list[TracedStep] = []
        self.weights: dict[int, tuple[object, Handle]] = {}
        self.states: dict[int, tuple[State, Handle]] = {}
        self.bindings: list[Binding] = []
        self._bound: dict[int, dict] = {}  # id(op) -> {member: Value}
        self._counter = itertools.count()
        self._names = {}
        if names_from is not None:
            self._names = {id(p): n for n, p in names_from.named_parameters()}

    def __enter__(self):
        _STACK.append(self)
        return self

    def __exit__(self, *exc):
        _STACK.pop()

    # -- operands ---------------------------------------------------------

    def state_as(self, state: State):
        """What stands for a state viewed inside the graph function: its handle."""
        return self.operand(state)

    def operand(self, x) -> Handle:
        if isinstance(x, Handle):
            return x
        if isinstance(x, State):
            key = id(x)
            if key not in self.states:
                x.name = x.name or f"state{len(self.states)}"
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
        outputs (a state it writes into); ``kwargs`` are per-call value
        handles for its value members, and otherwise construction arguments
        (dimensions, tunables, flags) when ``target`` is a class.
        """
        operands = [self.operand(a) for a in args]
        kwargs = dict(kwargs)
        # A keyword whose value is a per-call handle binds a value member of
        # the class resolve_class picks.
        values = {
            k: kwargs.pop(k) for k in list(kwargs) if isinstance(kwargs[k], Value)
        }
        if isinstance(target, type):
            cls = target.resolve_class(len(operands), {**kwargs, **values})
            own = self._split_values(cls, values)
            scales: dict[str, int] = {}
            operands = _take_views(cls, operands, kwargs, own, scales)
            n_in = sum(
                1
                for m in cls._members
                if isinstance(m, _Buffer_) and m.direction != "out"
            )
            op = self._construct(cls, operands[:n_in], operands[n_in:], kwargs)
        else:
            op = target
            own = self._split_values(type(op), values)
            scales = {}
            operands = _take_views(type(op), operands, {}, own, scales)
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
            self._bind(op, name, value, scales.get(name, 1))
        return self._record(op, operands)

    @staticmethod
    def _split_values(op_cls, kwargs) -> dict:
        names = {m.name for m in op_cls._members if isinstance(m, _Value)}
        return {k: kwargs.pop(k) for k in list(kwargs) if k in names}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        inferred = infer(
            cls,
            *[h.shape for h in inputs],
            outputs=[h.shape for h in outputs],
            **infer_kwargs(cls, kwargs),
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
                bounds[axis] = (binding.value, binding.scale)
        return bounds

    def _bind(self, op, name, value, scale: int = 1) -> None:
        if not isinstance(value, Value):
            raise TypeError(
                f"{type(op).__name__}.{name} takes a per-call value handle (a "
                f"keyword-only parameter of the graph function), got {value!r}"
            )
        bound = self._bound.setdefault(id(op), {})
        if name in bound and bound[name] is not value:
            raise ValueError(
                f"{type(op).__name__}.{name} is bound to {bound[name]!r} at an "
                f"earlier call site and to {value!r} here; one instance has one "
                f"value, bind one handle at every site or use two instances"
            )
        if name not in bound:
            op.use_value(name, value.name)
            bound[name] = value
            member = next(v for v in op.values if v.name == name)
            self.bindings.append(Binding(op, member, value, scale))

    def _record(self, op, operands):
        buffers = op.buffers
        ins = [b for b in buffers if b.direction in ("in", "inout")]
        outs = [b for b in buffers if b.direction == "out"]
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
            for axis, (value, scale) in h.bounds.items():
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
                        f"axis {axis} ({value.name}): it declares no Extent for the "
                        f"field sizing it"
                    )
                self._bind(op, extent.name, value, scale)
        slots, outputs, it, given = [], [], iter(operands[: len(ins)]), iter(given_outs)
        for b in buffers:
            if b.direction == "in":
                slots.append(next(it))
            elif b.direction == "inout":
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

    def finish(self, inputs, outputs, values) -> TracedGraph:
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

    def operand(self, x):
        return x

    def state_as(self, state: State):
        """A state viewed in the reference: a view of its host tensor that
        remembers the key, so the operator gets the whole tensor and its
        walk, as the device does, and writes it in place.
        """
        if state.host is None:
            state.host = np.zeros(state.shape, dtype=bfloat16)
        return _HostViews(state)

    def call(self, target, args, kwargs):
        tensors, states, keys = [], [], []
        for a in args:
            state, key = None, None
            if isinstance(a, _HostView):
                state, key, a = a.state, a.key, a.state.host
            elif isinstance(a, State):
                if a.host is None:
                    a.host = np.zeros(a.shape, dtype=bfloat16)
                state, a = a, a.host
            tensors.append(a)
            states.append(state)
            keys.append(key)
        kwargs = dict(kwargs)
        if isinstance(target, type):
            cls = target.resolve_class(len(tensors), kwargs)
            # A per-call value's number goes to the reference, not to
            # construction.
            values = self._split_values(cls, kwargs)
            shapes = [Handle(t.shape, _tensor_dtype(t), "", "input") for t in tensors]
            shapes = [h if k is None else h[k] for h, k in zip(shapes, keys)]
            shapes = _take_views(cls, shapes, kwargs, {}, {})
            n_in = sum(
                1
                for m in cls._members
                if isinstance(m, _Buffer_) and m.direction != "out"
            )
            op = self._construct(cls, shapes[:n_in], shapes[n_in:], kwargs)
        else:
            op = target
            values = {}
            n_in = sum(1 for b in op.buffers if b.direction != "out")
        values = {k: v for k, v in values.items() if v is not None}
        result = op.reference(*tensors, **values)
        # A state written in place keeps its host tensor; a result returned
        # for a given output lands in it.
        for state, given in zip(states[n_in:], tensors[n_in:]):
            if state is not None and result is not None and result is not given:
                given.copy_(result.reshape(given.shape).to(given.dtype))
        return result
