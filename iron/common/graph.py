# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions: a graph is a Python function traced on handles.

Inputs are its positional parameters, outputs its return values, weights
what it closes over, state an :func:`state` object created outside, and
per-call scalars its keyword-only parameters annotated ``Scratchpad[T]`` or
``DispatchTime[T]``. Operators are called on handles: ``GEMV(w, h)`` infers
its overlay and extent from its arguments (deduplicating overlays by
``design_key``), and an explicit instance ``q(w, h)`` is applied the same way.

    kv = [iron.state((n_kv, MAX, head_dim)) for _ in range(n_layers)]

    @iron.graph
    def decode(x, angles, *, pos: Scratchpad[np.int32]):
        h = RMSNorm(x, model.norm.weight)
        k = RoPE(GEMV(wk, h), angles)
        StridedCopy(k, kv[0], out_offset=pos)
        return GEMV(wo, h)

    net = decode.compile(dev, x=(1, emb), angles=(1, head_dim))
    logits = net(x_tok, ang_tok, pos=n * head_dim)

Tracing produces a :class:`TracedGraph`: the runlist, the buffer names and
sizes, the value bindings. It is pure bookkeeping and needs no toolchain.
:meth:`GraphFunction.compile` hands that to :class:`OperatorSequence` for
the image (a fused ELF on NPU2, per-step xclbins on NPU1) and returns a
:class:`CompiledGraph` to call. Calling an uncompiled graph with real
tensors compiles for their shapes, says so once, and dispatches.
"""

from __future__ import annotations

import dataclasses
import inspect
import itertools
from math import prod
from typing import Any

import numpy as np
from ml_dtypes import bfloat16

from .declare import Operator, Overlay, ValueSpec, _Buffer as _Buffer_, _Value

_STACK: list = []


def current():
    """The tracer a graph function is being traced under, or ``None``."""
    return _STACK[-1] if _STACK else None


# --------------------------------------------------------------------------
# Handles
# --------------------------------------------------------------------------


class Handle:
    """A traced tensor: a buffer of the graph, with a shape and a dtype.

    Carries no data. ``h[a:b]`` is a static slice along the leading axis; it
    is a view into the parent's buffer, so it costs nothing at run time.
    """

    __slots__ = ("shape", "dtype", "name", "role", "parent", "start")

    def __init__(self, shape, dtype, name, role, parent=None, start=0):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        self.role = role  # input | output | weight | state | intermediate | slice
        self.parent = parent
        self.start = start  # element offset into the parent, for a slice

    @property
    def elements(self) -> int:
        return prod(self.shape) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * np.dtype(self.dtype).itemsize

    @property
    def buffer_name(self) -> str:
        """The name the runlist uses: a slice is ``parent[start:stop]`` in bytes."""
        if self.parent is None:
            return self.name
        item = np.dtype(self.dtype).itemsize
        return f"{self.parent.buffer_name}[{self.start * item}:{(self.start + self.elements) * item}]"

    def reshape(self, *shape) -> "Handle":
        """The same buffer seen with another shape (no data moves)."""
        if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
            shape = tuple(shape[0])
        if prod(shape) != self.elements:
            raise ValueError(f"cannot reshape {self!r} to {list(shape)}")
        return Handle(shape, self.dtype, self.name, self.role, self.parent, self.start)

    def __getitem__(self, index) -> "Handle":
        if self.parent is not None:
            raise TypeError("slicing a slice is not supported; slice the parent")
        n = self.shape[0]
        if isinstance(index, int):
            if not -n <= index < n:
                raise IndexError(f"index {index} out of range for {self.shape}")
            index = index % n
            start, stop, shape = index, index + 1, self.shape[1:]
        elif isinstance(index, slice):
            if index.step not in (None, 1):
                raise ValueError("only unit steps are supported")
            start, stop, _ = index.indices(n)
            if stop <= start:
                raise ValueError(f"empty slice {index}")
            shape = (stop - start,) + self.shape[1:]
        else:
            raise TypeError("a handle is sliced along its leading axis only")
        inner = prod(self.shape[1:]) if len(self.shape) > 1 else 1
        return Handle(shape, self.dtype, self.name, "slice", self, start * inner)

    def __repr__(self) -> str:
        return f"Handle({self.buffer_name!r}, {list(self.shape)}, {np.dtype(self.dtype).name})"


class State:
    """A tensor that persists on the device across calls (a KV cache).

    Created outside the graph function with :func:`state` and closed over.
    Zero when the graph is first uploaded; read and written through
    :meth:`CompiledGraph.buffer`.
    """

    __slots__ = ("shape", "dtype", "name", "host")

    def __init__(self, shape, dtype=bfloat16, name=None):
        self.shape = tuple(int(s) for s in shape)
        self.dtype = dtype
        self.name = name
        self.host = None  # the reference path's copy, made on first use

    def __repr__(self) -> str:
        return f"State({self.name or ''}{list(self.shape)})"


def state(shape, dtype=bfloat16, name=None) -> State:
    """Declare device-resident state a graph function closes over."""
    return State(shape, dtype, name)


class Value:
    """A per-call scalar parameter of a graph function."""

    __slots__ = ("name", "kind", "dtype")

    def __init__(self, name, kind, dtype):
        self.name, self.kind, self.dtype = name, kind, dtype

    def __repr__(self) -> str:
        return f"Value({self.name!r}, {self.kind}[{np.dtype(self.dtype).name}])"


def is_operand(x) -> bool:
    """A graph handle, a state, or a host tensor (a weight)."""
    if isinstance(x, (Handle, State)):
        return True
    if isinstance(x, (Overlay, Operator, type)):
        return False
    return hasattr(x, "shape") and hasattr(x, "dtype")


def _tensor_dtype(t):
    dt = getattr(t, "dtype", None)
    name = str(dt).replace("torch.", "")
    return {
        "bfloat16": bfloat16,
        "float32": np.float32,
        "int32": np.int32,
        "int8": np.int8,
        "uint8": np.uint8,
        "int16": np.int16,
    }.get(name, dt)


# --------------------------------------------------------------------------
# Tracing
# --------------------------------------------------------------------------


@dataclasses.dataclass
class Step:
    op: Operator
    slots: list  # the handle in each of the operator's buffers, in declaration order
    inputs: list  # handles consumed
    outputs: list  # handles produced

    @property
    def names(self) -> list:
        """Buffer names in declaration order, as the runlist spells them."""
        return [h.buffer_name for h in self.slots]


@dataclasses.dataclass
class TracedGraph:
    """What tracing a graph function for given shapes produced."""

    name: str
    steps: list
    inputs: list  # Handles, in parameter order
    outputs: list  # Handles returned
    values: list  # Values, in parameter order
    pinned: dict  # buffer name -> nbytes, for weights, states and slice parents
    weights: dict  # id(tensor) -> (tensor, Handle)
    states: dict  # id(State) -> Handle
    bindings: list  # (op, member name, Value)

    @property
    def runlist(self) -> list:
        return [(s.op, *s.names) for s in self.steps]

    @property
    def input_args(self) -> list:
        return [h.name for h in self.inputs]

    @property
    def output_args(self) -> list:
        return [h.name for h in self.outputs]

    def sequence(self, name=None, **kwargs):
        """The :class:`OperatorSequence` this graph lowers to (the image builder)."""
        from .sequence import OperatorSequence

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
    def overlays(self) -> list:
        seen = {}
        for op in self.operators:
            seen.setdefault(op.ov.design_key(), op.ov)
        return list(seen.values())


class Tracer:
    """Records operator calls on handles while a graph function runs."""

    def __init__(self, name: str, names_from=None):
        self.name = name
        self.steps: list[Step] = []
        self.weights: dict[int, tuple] = {}
        self.states: dict[int, Handle] = {}
        self.overlays: dict = {}
        self.bindings: list = []
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
                self.states[key] = Handle(x.shape, x.dtype, x.name, "state")
            return self.states[key]
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
        # A keyword whose value is a per-call handle binds a value member: the
        # operator's own, or one on the overlay a class picks for it (the
        # dynamic softmax), which the class's translation sees first.
        values = {
            k: kwargs.pop(k) for k in list(kwargs) if isinstance(kwargs[k], Value)
        }
        if isinstance(target, type):
            cls = target.resolve_class(len(operands), kwargs)
            own = self._split_values(cls, values)
            n_in = sum(
                1
                for m in cls._members
                if isinstance(m, _Buffer_) and m.direction != "out"
            )
            op = self._construct(
                cls, operands[:n_in], operands[n_in:], {**kwargs, **values}
            )
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
        overlay_cls = cls._overlay_class
        dim_kwargs = {
            k: v
            for k, v in kwargs.items()
            if k in cls._dim_fields
            or (overlay_cls is not None and k in overlay_cls._dim_fields)
        }
        inferred = cls.infer(
            *[h.shape for h in inputs],
            outputs=[h.shape for h in outputs],
            **dim_kwargs,
        )
        # The class's own translation splits overlay fields from the
        # operator's and fills what it derives (a transfer size, a dtype
        # spelling), exactly as the keyword constructor does.
        ov, op_kwargs = cls._classic({**kwargs, **inferred})
        # One build per distinct overlay: equal keys are one array.
        ov = self.overlays.setdefault(ov.design_key(), ov)
        return cls(ov, **op_kwargs)

    def _bind(self, op, name, value) -> None:
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
            op.use_value(name)
            bound[name] = value
            self.bindings.append((op, name, value))

    def _bind_overlay(self, op, name, value) -> None:
        """Bind a core-read value the operator's overlay declares."""
        if name not in {v.name for v in op.ov.values}:
            raise TypeError(
                f"{type(op).__name__} has no per-call value {name!r}, on itself or "
                f"on {type(op.ov).__name__}"
            )
        bound = self._bound.setdefault(id(op), {})
        if name in bound and bound[name] is not value:
            raise ValueError(
                f"{type(op).__name__}.{name} is bound to {bound[name]!r} at an "
                f"earlier call site and to {value!r} here"
            )
        if name not in bound:
            bound[name] = value
            self.bindings.append((op, name, value))

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
            if np.dtype(h.dtype) != np.dtype(b.dtype):
                raise TypeError(
                    f"{type(op).__name__}.{b.name} is {np.dtype(b.dtype).name}; "
                    f"operand {h!r} is {np.dtype(h.dtype).name}"
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
            Step(op, slots, operands[: len(ins)], outputs + list(given_outs))
        )
        if not outputs:
            return None
        return outputs[0] if len(outputs) == 1 else tuple(outputs)

    # -- the result ----------------------------------------------------------

    def finish(self, inputs, outputs, values) -> TracedGraph:
        pinned = {}
        for _, h in self.weights.values():
            pinned[h.name] = h.nbytes
        for h in self.states.values():
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


# --------------------------------------------------------------------------
# Graph functions
# --------------------------------------------------------------------------


def _shape_and_dtype(spec):
    """``(shape)`` or ``((shape), dtype)``."""
    if (
        isinstance(spec, tuple)
        and len(spec) == 2
        and isinstance(spec[0], (tuple, list))
    ):
        return tuple(spec[0]), spec[1]
    return tuple(spec), bfloat16


class GraphFunction:
    """A function decorated with :func:`graph`."""

    def __init__(self, fn, names_from=None):
        self.fn = fn
        self.names_from = names_from
        self.__name__ = fn.__name__
        self.__doc__ = fn.__doc__
        sig = inspect.signature(fn)
        self.params = [
            p.name
            for p in sig.parameters.values()
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        ]
        self.value_params = {}
        for p in sig.parameters.values():
            if p.kind is p.KEYWORD_ONLY:
                ann = p.annotation
                if isinstance(ann, type) and issubclass(ann, _Value):
                    ann = ValueSpec(ann.kind, np.int32)
                if not isinstance(ann, ValueSpec):
                    raise TypeError(
                        f"{fn.__name__}: keyword-only parameter {p.name!r} is a "
                        f"per-call value and must be annotated Scratchpad[T] or "
                        f"DispatchTime[T]"
                    )
                self.value_params[p.name] = ann
            elif p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                raise TypeError(f"{fn.__name__}: *args/**kwargs are not traceable")
        self._compiled = None

    # -- tracing ---------------------------------------------------------------

    def trace(self, **shapes) -> TracedGraph:
        """Run the function on handles of the given shapes; return the graph."""
        missing = [p for p in self.params if p not in shapes]
        unknown = [k for k in shapes if k not in self.params]
        if missing or unknown:
            raise TypeError(
                f"{self.__name__}: shapes for {missing} missing"
                + (f"; {unknown} are not inputs" if unknown else "")
            )
        inputs = []
        for name in self.params:
            shape, dtype = _shape_and_dtype(shapes[name])
            inputs.append(Handle(shape, dtype, name, "input"))
        values = [
            Value(n, spec.kind, spec.dtype) for n, spec in self.value_params.items()
        ]
        with Tracer(self.__name__, self.names_from) as tracer:
            result = self.fn(*inputs, **{v.name: v for v in values})
        outputs = self._outputs(result, tracer)
        return tracer.finish(inputs, outputs, values)

    def _outputs(self, result, tracer) -> list:
        if result is None:
            return []
        items = list(result) if isinstance(result, (tuple, list)) else [result]
        outputs = []
        for i, item in enumerate(items):
            if not isinstance(item, Handle) or item.parent is not None:
                raise TypeError(
                    f"{self.__name__} returned {item!r}; a graph returns whole "
                    f"handles produced inside it"
                )
            if item.role == "input":
                raise TypeError(
                    f"{self.__name__} returns its input {item.name!r} unchanged"
                )
            if item.role == "intermediate":
                item.name = f"out{i}" if len(items) > 1 else "out"
                item.role = "output"
            outputs.append(item)
        return outputs

    # -- compiling and calling -----------------------------------------------------

    def compile(
        self,
        dev=None,
        *,
        boundaries=None,
        image=None,
        verbose=False,
        context=None,
        **shapes,
    ):
        """Compile for the given input shapes and return a :class:`CompiledGraph`.

        ``boundaries`` and ``image`` are the two packaging choices
        (:mod:`iron.common.packaging`); everything else is derived and, under
        ``verbose``, printed.
        """
        import aie.utils as aie_utils

        from .packaging import plan

        if dev is not None:
            aie_utils.set_current_device(dev)
        traced = self.trace(**shapes)
        chosen = plan(
            aie_utils.get_current_device().resolve().name, traced, boundaries, image
        )
        if verbose:
            print(chosen.report(self.__name__))
        self._compiled = CompiledGraph(
            traced, context=context, dispatch=chosen.dispatch
        )
        self._compiled.plan = chosen
        return self._compiled

    def __call__(self, *tensors, **values):
        if self._compiled is None:
            shapes = {
                name: (tuple(t.shape), _tensor_dtype(t))
                for name, t in zip(self.params, tensors)
            }
            print(f"{self.__name__}: compiling for {shapes}")
            self.compile(**shapes)
        return self._compiled(*tensors, **values)

    def reference(self, *tensors, **values):
        """The same function, each operator run through its ``reference()``."""
        with _ReferenceTracer(self.__name__) as tracer:
            return self.fn(*tensors, **{k: values.get(k) for k in self.value_params})


class _ReferenceTracer(Tracer):
    """Runs each operator's CPU reference on host tensors as the graph is traced."""

    def operand(self, x):
        return x

    def call(self, target, args, kwargs):
        import torch

        tensors = []
        for a in args:
            if isinstance(a, State):
                if a.host is None:
                    a.host = torch.zeros(a.shape, dtype=torch.bfloat16)
                a = a.host
            tensors.append(a)
        kwargs = dict(kwargs)
        if isinstance(target, type):
            cls = target.resolve_class(len(tensors), kwargs)
            self._split_values(cls, kwargs)  # per-call values are not modelled here
            shapes = [Handle(t.shape, _tensor_dtype(t), "", "input") for t in tensors]
            n_in = sum(
                1
                for m in cls._members
                if isinstance(m, _Buffer_) and m.direction != "out"
            )
            op = self._construct(cls, shapes[:n_in], shapes[n_in:], kwargs)
            tensors = tensors[:n_in]
        else:
            op = target
        return op.reference(*tensors)


def graph(fn=None, *, names_from=None):
    """Declare a graph function; see the module docstring."""
    if fn is None:
        return lambda f: GraphFunction(f, names_from)
    return GraphFunction(fn, names_from)


# --------------------------------------------------------------------------
# The compiled graph
# --------------------------------------------------------------------------


class CompiledGraph:
    """A traced graph built into an image, ready to call."""

    def __init__(self, traced: TracedGraph, context=None, dispatch="auto"):
        from .build import value_symbol

        self.traced = traced
        for _, name, value in traced.bindings:
            if value.kind == "dispatch":
                raise NotImplementedError(
                    f"{value!r}: DispatchTime values arrive with the packaging "
                    f"step (OPERATOR_MODEL_PLAN.md §8)"
                )
        self.symbols = []
        for op, name, value in traced.bindings:
            bound = getattr(op, name, None)
            if bound is None or not hasattr(bound, "kind"):
                bound = next(v for v in op.ov.values if v.name == name)
            self.symbols.append((value.name, value_symbol(op, bound), value.dtype))
        # Equal design keys are one build (two projections on one array).
        # compile() builds the image; the runtime that loads it is made on
        # first use, so a host without an NPU can still compile.
        self.sequence = traced.sequence(dispatch=dispatch, context=context).compile()
        self.image = self.sequence.image
        self._callable = None
        self._uploaded = False

    @property
    def callable(self):
        """The loaded image, made on first use (needs the XRT runtime)."""
        if self._callable is None:
            self._callable = self.sequence.get_callable()
        return self._callable

    # -- buffers ---------------------------------------------------------------

    def buffer(self, x):
        """The device buffer of a state, a weight tensor, or a handle."""
        if isinstance(x, State):
            name = self.traced.states[id(x)].name
        elif isinstance(x, Handle):
            name = x.buffer_name
        elif id(x) in self.traced.weights:
            name = self.traced.weights[id(x)][1].name
        else:
            raise KeyError(f"{x!r} is not a state, weight or handle of this graph")
        return self.callable.get_buffer(name)

    def write(self, x, tensor) -> None:
        """Copy ``tensor`` into a state's or weight's buffer and push it to the device."""
        buf = self.buffer(x)
        view = buf.torch_view()
        import torch

        if not isinstance(tensor, torch.Tensor):
            tensor = torch.as_tensor(np.asarray(tensor))
        view[:] = tensor.reshape(-1).to(view.dtype)
        buf.to("npu")

    def read(self, x):
        """A state's or weight's current contents, as a host tensor of its shape."""
        buf = self.buffer(x)
        buf.to("cpu")
        shape = self.traced.states[id(x)].shape if isinstance(x, State) else x.shape
        return buf.to_torch().reshape(tuple(shape))

    def _copy_in(self, name, tensor) -> None:
        import torch

        if not isinstance(tensor, torch.Tensor):
            tensor = torch.as_tensor(np.asarray(tensor))
        view = self.callable.get_buffer(name).torch_view()
        view[:] = tensor.reshape(-1).to(view.dtype)

    def upload(self) -> None:
        """Copy every closed-over weight into its buffer; once."""
        if self._uploaded:
            return
        for tensor, handle in self.traced.weights.values():
            self._copy_in(handle.name, tensor)
        self._uploaded = True

    # -- calling ---------------------------------------------------------------

    def __call__(self, *tensors, **values):
        if len(tensors) != len(self.traced.inputs):
            raise TypeError(
                f"{self.traced.name} takes {len(self.traced.inputs)} input(s), "
                f"got {len(tensors)}"
            )
        self.upload()
        for handle, tensor in zip(self.traced.inputs, tensors):
            if tuple(tensor.shape) != handle.shape:
                raise ValueError(
                    f"{self.traced.name}: input {handle.name} was compiled for "
                    f"{handle.shape}, got {tuple(tensor.shape)}; a new shape is a "
                    f"new compile"
                )
            self._copy_in(handle.name, tensor)
        self._write_values(values)
        self.callable()
        outputs = [self.callable.get_buffer(h.name) for h in self.traced.outputs]
        if not outputs:
            return None
        return outputs[0] if len(outputs) == 1 else tuple(outputs)

    def _write_values(self, values) -> None:
        expected = {v.name for v in self.traced.values}
        missing, unknown = expected - set(values), set(values) - expected
        if missing or unknown:
            raise TypeError(
                f"{self.traced.name}: per-call values {sorted(missing)} missing"
                + (f"; {sorted(unknown)} unknown" if unknown else "")
            )
        if not self.symbols:
            return
        params = getattr(self.callable, "params", None)
        if params is None:
            raise NotImplementedError(
                "per-call values on this dispatch path arrive with the packaging "
                "step (OPERATOR_MODEL_PLAN.md §6, §8)"
            )
        for name, symbol, dtype in self.symbols:
            params.write(symbol, np.dtype(dtype).type(values[name]))
        params.sync()
