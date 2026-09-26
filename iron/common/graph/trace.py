# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tracing a graph function: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import itertools
from collections.abc import Hashable

import numpy as np
from ml_dtypes import bfloat16

from aie.utils import bfp

from ..declare import BoundValue, Operator, Resident, infer, infer_kwargs
from ..declare.member import _Buffer as _Buffer_, _Value
from ..design import device_symbol
from ..image.sequence import OperatorSequence
from .handle import Affine, Carry, Handle, State, Value, _tensor_dtype, is_operand

_STACK: list = []


def _as_affine(value: Value | Affine) -> Affine:
    return value.affine() if isinstance(value, Value) else value


def current():
    """The tracer a graph function is being traced under, or ``None``."""
    return _STACK[-1] if _STACK else None


def handle_of(x):
    """What a graph function sees for an array or state it closes over.

    Slicing a closed-over numpy array makes a new array, which would trace
    as a weight of its own; slice this instead. Under the reference it is
    ``x`` itself, so the slice is numpy's.
    """
    tracer = current()
    if tracer is None:
        raise RuntimeError("handle_of is for use inside a graph function")
    return tracer.operand(x)


@dataclasses.dataclass
class TracedStep:
    op: Operator
    slots: list  # the handle in each of the operator's buffers, in declaration order
    inputs: list  # handles consumed
    outputs: list  # handles produced

    @property
    def names(self) -> list:
        """Buffer names in declaration order, as the runlist spells them."""
        return [h.buffer_name for h in self.slots]


@dataclasses.dataclass(frozen=True)
class Binding:
    """A per-call value of the graph, bound to one operator's value member.

    ``member`` is the operator's own, or its overlay's for a core-read value
    the overlay declares (the dynamic softmax's vector size).
    ``expression`` is what the member is written, computed per call from one
    of the graph's values.
    """

    op: Operator
    member: BoundValue
    expression: Affine

    @property
    def value(self) -> Value:
        """The graph's value the member is computed from."""
        return self.expression.value

    @property
    def symbol(self) -> str:
        """The device symbol the host writes this value through."""
        return device_symbol(self.op, self.member)


@dataclasses.dataclass
class TracedGraph:
    """What tracing a graph function for given shapes produced.

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

        The key is the identity of the tensor or :class:`State` closed over:
        the same in every trace of the function, so each version compiled
        from it addresses one copy.
        """
        found = {h.name: key for key, (_, h) in self.weights.items()}
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
        kwargs.setdefault("feedback_args", list(self.feedback))
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
    def overlays(self) -> list:
        seen = {}
        for op in self.operators:
            seen.setdefault(op.ov.design_key(), op.ov)
        return list(seen.values())


class Tracer:
    """Records operator calls on handles while a graph function runs."""

    def __init__(self, name: str, names_from=None):
        self.name = name
        self.steps: list[TracedStep] = []
        self.weights: dict[int, tuple[object, Handle]] = {}
        self.states: dict[int, tuple[State, Handle]] = {}
        self.overlays: dict = {}
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
        # A keyword whose value is a per-call handle, or an expression of
        # one, binds a value member: the operator's own, or one on the
        # overlay of the class resolve_class picks for it (the dynamic
        # softmax).
        values = {
            k: _as_affine(kwargs.pop(k))
            for k in list(kwargs)
            if isinstance(kwargs[k], (Value, Affine))
        }
        if isinstance(target, type):
            # The class sees the values too: a family that picks a member from
            # a bound value (the dynamic softmax) decides here.
            cls = target.resolve_class(len(operands), {**kwargs, **values})
            own = self._split_values(cls, values)
            n_in = sum(
                1
                for m in cls._members
                if isinstance(m, _Buffer_) and m.direction != "out"
            )
            op = self._construct(cls, operands[:n_in], operands[n_in:], kwargs)
        else:
            op = target
            own = self._split_values(type(op), values)
            if kwargs or values:
                raise TypeError(
                    f"{type(op).__name__} instance called with unexpected keyword "
                    f"arguments {sorted(kwargs) + sorted(values)}"
                )
        for name, value in own.items():
            self._bind(op, name, value)
        for name, value in values.items():
            self._bind_overlay(op, name, value)
        return self._record(op, operands)

    @staticmethod
    def _split_values(cls, kwargs) -> dict:
        names = {m.name for m in cls._members if isinstance(m, _Value)}
        return {k: kwargs.pop(k) for k in list(kwargs) if k in names}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        inferred = infer(
            cls,
            *[h.shape for h in inputs],
            outputs=[h.shape for h in outputs],
            **infer_kwargs(cls, kwargs),
        )
        # The class's own translation splits overlay fields from the
        # operator's and fills what it derives (a transfer size, a dtype
        # spelling), exactly as the keyword constructor does.
        ov, op_kwargs = cls._split_kwargs({**kwargs, **inferred})
        # One build per distinct overlay: equal keys are one array.
        ov = self.overlays.setdefault(ov.design_key(), ov)
        return cls(ov, **op_kwargs)

    def _bind(self, op, name, value: Affine) -> None:
        if not isinstance(value, Affine):
            raise TypeError(
                f"{type(op).__name__}.{name} takes a per-call value handle (a "
                f"keyword-only parameter of the graph function), got {value!r}"
            )
        bound = self._bound.setdefault(id(op), {})
        if name in bound and bound[name] != value:
            raise ValueError(
                f"{type(op).__name__}.{name} is bound to {bound[name]!r} at an "
                f"earlier call site and to {value!r} here; one instance has one "
                f"value, bind one expression at every site or use two instances"
            )
        if name not in bound:
            op.use_value(name)
            bound[name] = value
            member = next(v for v in op.values if v.name == name)
            self.bindings.append(Binding(op, member, value))

    def _bind_overlay(self, op, name, value: Affine) -> None:
        """Bind a core-read value the operator's overlay declares."""
        if name not in {v.name for v in op.ov.values}:
            raise TypeError(
                f"{type(op).__name__} has no per-call value {name!r}, on itself or "
                f"on {type(op.ov).__name__}"
            )
        bound = self._bound.setdefault(id(op), {})
        if name in bound and bound[name] != value:
            raise ValueError(
                f"{type(op).__name__}.{name} is bound to {bound[name]!r} at an "
                f"earlier call site and to {value!r} here"
            )
        if name not in bound:
            bound[name] = value
            member = next(v for v in op.ov.values if v.name == name)
            self.bindings.append(Binding(op, member, value))

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
            if h.elements != b.elements:
                raise ValueError(
                    f"{type(op).__name__}.{b.name} is {b.shape} "
                    f"({b.elements} elements); operand {h!r} has {h.elements}"
                )
            if bfp.dtype_name(h.dtype) != bfp.dtype_name(b.dtype):
                raise TypeError(
                    f"{type(op).__name__}.{b.name} is {bfp.dtype_name(b.dtype)}; "
                    f"operand {h!r} is {bfp.dtype_name(h.dtype)}"
                )
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
                if len(shape) == 1:
                    like = next((h for h in operands if h.elements == b.elements), None)
                    if like is not None:
                        shape = like.shape
                h = Handle(
                    shape,
                    b.dtype,
                    f"{type(op).__name__.lower()}{next(self._counter)}",
                    "intermediate",
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
        self, inputs, outputs, values, carry: Carry | None = None
    ) -> TracedGraph:
        carry = dict(carry or {})
        returned = list(outputs)
        outputs = returned + [
            h
            for h in carry.values()
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
            carry,
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

    def call(self, target, args, kwargs):
        tensors, states = [], []
        for a in args:
            state = None
            if isinstance(a, State):
                if a.host is None:
                    a.host = np.zeros(a.shape, dtype=bfloat16)
                state, a = a, a.host
            tensors.append(a)
            states.append(state)
        kwargs = dict(kwargs)
        if isinstance(target, type):
            cls = target.resolve_class(len(tensors), kwargs)
            values = self._split_values(cls, kwargs)
            # A value bound on the overlay is a core-read one: a scratchpad on
            # the dynamic overlay, or the resident a class swaps for it when a
            # site binds a handle (the softmax's vector_size). Either way the
            # number goes to the reference, not to construction.
            overlay_cls = cls._overlay_class
            if overlay_cls is not None:
                names = {
                    m.name
                    for m in overlay_cls._members
                    if isinstance(m, (_Value, Resident))
                }
                values.update({k: kwargs.pop(k) for k in list(kwargs) if k in names})
            shapes = [Handle(t.shape, _tensor_dtype(t), "", "input") for t in tensors]
            n_in = sum(
                1
                for m in cls._members
                if isinstance(m, _Buffer_) and m.direction != "out"
            )
            op = self._construct(cls, shapes[:n_in], shapes[n_in:], kwargs)
        else:
            # An instance is called with its values alone.
            op = target
            values = kwargs
            n_in = sum(1 for b in op.buffers if b.direction != "out")
        values = {k: v for k, v in values.items() if v is not None}
        result = op.reference(*tensors, **values)
        # A state written in place keeps its host tensor; a result returned
        # for a given output lands in it.
        for state, given in zip(states[n_in:], tensors[n_in:]):
            if state is not None and result is not None and result is not given:
                given.copy_(result.reshape(given.shape).to(given.dtype))
        return result
