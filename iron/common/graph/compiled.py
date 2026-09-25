# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph function, and the image it compiles to."""

from __future__ import annotations

import inspect

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils

from ..declare import ValueSpec
from ..declare.member import _Value
from ..design import device_symbol
from ..image.packaging import plan
from .handle import Handle, State, Value, _tensor_dtype
from .trace import TracedGraph, Tracer, _ReferenceTracer


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
        record="memory",
        **shapes,
    ):
        """Compile for the given input shapes and return a :class:`CompiledGraph`.

        ``boundaries`` and ``image`` are the two packaging choices
        (:mod:`iron.common.image.packaging`); everything else is derived and, under
        ``verbose``, printed. ``record="disk"`` writes the image's
        :class:`~iron.common.image.artifacts.Artifacts` record beside it.
        """
        if dev is not None:
            aie_utils.set_current_device(dev)
        traced = self.trace(**shapes)
        chosen = plan(
            aie_utils.get_current_device().resolve().name, traced, boundaries, image
        )
        if verbose:
            print(chosen.report(self.__name__))
        self._compiled = CompiledGraph(traced, record=record, dispatch=chosen.dispatch)
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


class CompiledGraph:
    """A traced graph built into an image, ready to call."""

    def __init__(self, traced: TracedGraph, record="memory", dispatch="auto"):
        self.traced = traced
        self.symbols = []
        for op, name, value in traced.bindings:
            bound = getattr(op, name, None)
            if bound is None or not hasattr(bound, "kind"):
                bound = next(v for v in op.ov.values if v.name == name)
            self.symbols.append((value.name, device_symbol(op, bound), value.dtype))
        # Equal design keys are one build (two projections on one array).
        # compile() builds the image; the runtime that loads it is made on
        # first use, so a host without an NPU can still compile.
        self.sequence = traced.sequence(dispatch=dispatch).compile(record=record)
        self.image = self.sequence.image
        # What the image consists of, by identity: its designs, which step
        # runs which, and where each buffer lands in its plan.
        self.artifacts = self.sequence.artifacts
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
        view = buf.numpy_view()
        view[:] = np.asarray(tensor).reshape(-1).astype(view.dtype)
        buf.to("npu")

    def read(self, x):
        """A state's or weight's current contents, as a host tensor of its shape."""
        buf = self.buffer(x)
        buf.to("cpu")
        shape = self.traced.states[id(x)].shape if isinstance(x, State) else x.shape
        return buf.numpy().reshape(tuple(shape))

    def _copy_in(self, name, tensor) -> None:
        view = self.callable.get_buffer(name).numpy_view()
        view[:] = np.asarray(tensor).reshape(-1).astype(view.dtype)

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
        # Looked up on the class: getattr() on the instance would turn an
        # AttributeError raised inside the property (a pyxrt without the ctrl
        # scratchpad) into "takes no per-call values".
        params = (
            self.callable.params if hasattr(type(self.callable), "params") else None
        )
        if params is not None:
            for name, symbol, dtype in self.symbols:
                params.write(symbol, np.dtype(dtype).type(values[name]))
            params.sync()
            return
        if hasattr(self.callable, "dispatch_values"):
            # An image without a scratchpad: each kernel takes its values as
            # dispatch-time scalars and regenerates its stream (§6).
            self.callable.dispatch_values = {
                symbol: np.dtype(dtype).type(values[name])
                for name, symbol, dtype in self.symbols
            }
            return
        raise NotImplementedError(
            f"{type(self.callable).__name__} takes no per-call values"
        )


def graph(fn=None, *, names_from=None):
    """Declare a graph function; see the module docstring."""
    if fn is None:
        return lambda f: GraphFunction(f, names_from)
    return GraphFunction(fn, names_from)
