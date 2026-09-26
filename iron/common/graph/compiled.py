# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph function, and the images it compiles to.

A graph function is compiled once per input signature (shapes and dtypes):
each is a *version*, its own image. Every version reads the same weights
and states, and on a full ELF they share one scratch arena
(:class:`~iron.common.image.ArenaPlan`), so a weight is on the device once
and a state one version writes is where the next reads it. This needs no
setup: calling the function with a new shape compiles a version into the
arena its other versions already use.
"""

from __future__ import annotations

import contextlib
import inspect
from collections.abc import Callable, Mapping
from typing import Any, overload

import aie.utils as aie_utils
import numpy as np
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare.member import Extent, ValueSpec, _Value
from ..declare.profile import Profile
from ..design import device_symbol
from ..device import device_name
from ..image.allocator import ArenaPlan
from ..image.callable import ScratchArena
from ..image.packaging import Plan, plan
from ..image.sequence import ALIGNMENT
from .handle import Handle, State, Value, _tensor_dtype
from .trace import TracedGraph, Tracer, _ReferenceTracer

# One (parameter, shape, dtype name) per input: what picks a version.
Signature = tuple[tuple[str, tuple[int, ...], str], ...]


def _shape_and_dtype(spec):
    """``(shape)`` or ``((shape), dtype)``."""
    if (
        isinstance(spec, tuple)
        and len(spec) == 2
        and isinstance(spec[0], (tuple, list))
    ):
        return tuple(spec[0]), spec[1]
    return tuple(spec), bfloat16


# A weight is uploaded in pieces of at most this many bytes of the host copy.
UPLOAD_PIECE = 64 * 2**20


def _store(
    view: np.ndarray,
    tensor,
    release: Callable[[np.ndarray], None] | None = None,
    piece_bytes: int = UPLOAD_PIECE,
) -> None:
    """Copy ``tensor`` into a buffer view, casting in place.

    Assignment casts element by element into the destination; ``astype``
    first would build a whole temporary, and faulting in the 501 MiB one
    for Llama's embedding took 5-50 s per upload.

    ``release``, if given, is called with each piece of the flattened host
    copy once it is in the buffer, so a mapped checkpoint need never have
    more than a piece of a weight resident beside it.
    """
    flat = np.asarray(tensor).reshape(-1)
    if release is None:
        view[:] = flat
        return
    step = max(1, piece_bytes // flat.itemsize)
    for begin in range(0, flat.size, step):
        piece = flat[begin : begin + step]
        view[begin : begin + step] = piece
        release(piece)


class GraphFunction:
    """A function decorated with :func:`graph`."""

    def __init__(self, fn, names_from=None, profile=None):
        self.fn = fn
        self.names_from = names_from
        self.profile = profile
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
        self._versions: dict[Signature, CompiledGraph] = {}
        self._arena = ScratchArena(ArenaPlan(ALIGNMENT))

    @property
    def versions(self) -> dict[Signature, CompiledGraph]:
        """Every version compiled so far, by input signature."""
        return dict(self._versions)

    @property
    def arena(self) -> ScratchArena:
        """The scratch arena every full-ELF version runs in."""
        return self._arena

    @staticmethod
    def _signature(inputs: list[Handle]) -> Signature:
        return tuple((h.name, h.shape, bfp.dtype_name(h.dtype)) for h in inputs)

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
        with self._scope(), Tracer(self.__name__, self.names_from) as tracer:
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
    ) -> CompiledGraph:
        """Compile the version for the given input shapes and return it.

        ``boundaries`` and ``image`` are the two packaging choices
        (:mod:`iron.common.image.packaging`); everything else is derived and, under
        ``verbose``, printed. ``record="disk"`` writes the image's
        :class:`~iron.common.image.artifacts.Artifacts` record beside it.

        A full-ELF version is placed in :attr:`arena`, with the weights and
        states of every other version. Compile every version before the
        first call where you can: a version placed after the arena's buffer
        exists grows it, which copies it once.
        """
        if dev is not None:
            aie_utils.set_current_device(dev)
        traced = self.trace(**shapes)
        bound = aie_utils.get_current_device()
        assert bound is not None, "compile() needs a bound device"
        npu = device_name(bound)
        chosen = plan(npu, traced, boundaries, image)
        if verbose:
            print(chosen.report(self.__name__))
        signature = self._signature(traced.inputs)
        shared = chosen.dispatch == "fused"
        # Versions see one state only through the arena. Weights alone could
        # be copied per version, so a stateless function still compiles.
        others = [v for k, v in self._versions.items() if k != signature]
        apart = not shared or any(v.arena is None for v in others)
        stateful = traced.states or any(v.traced.states for v in others)
        if others and apart and stateful:
            raise NotImplementedError(
                f"{self.__name__}: versions share their states through one "
                f"scratch arena, which only a full ELF addresses; this version "
                f"dispatches {chosen.dispatch!r}"
            )
        version = CompiledGraph(
            traced, chosen, record=record, arena=self._arena if shared else None
        )
        self._versions[signature] = version
        return version

    def __call__(self, *tensors, **values) -> Any:
        if len(tensors) != len(self.params):
            raise TypeError(
                f"{self.__name__} takes {len(self.params)} input(s), got "
                f"{len(tensors)}"
            )
        signature = tuple(
            (name, tuple(int(n) for n in t.shape), bfp.dtype_name(_tensor_dtype(t)))
            for name, t in zip(self.params, tensors)
        )
        version = self._versions.get(signature)
        if version is None:
            shapes = {
                name: (tuple(t.shape), _tensor_dtype(t))
                for name, t in zip(self.params, tensors)
            }
            print(f"{self.__name__}: compiling for {shapes}")
            # A checker matches **shapes against compile()'s named parameters.
            version = self.compile(**shapes)  # pyright: ignore[reportArgumentType]
        return version(*tensors, **values)

    def reference(self, *tensors, **values):
        """The same function, each operator run through its ``reference()``."""
        with self._scope(), _ReferenceTracer(self.__name__):
            return self.fn(*tensors, **{k: values.get(k) for k in self.value_params})

    def _scope(self):
        """The profile applied while the function's body runs, if it has one."""
        return self.profile if self.profile is not None else contextlib.nullcontext()


class CompiledGraph:
    """A traced graph built into an image, ready to call.

    With an ``arena`` its weights and states are residents of that shared
    scratch arena: placed once for every image in it, and uploaded once.
    """

    def __init__(
        self,
        traced: TracedGraph,
        plan: Plan,
        record="memory",
        arena: ScratchArena | None = None,
    ):
        self.traced = traced
        self.plan = plan
        self.arena = arena
        # (device symbol, dtype, word) per scratchpad word a call writes:
        # each bound value (a per-call index on a view scaled to an element
        # offset), and each value derived from a bounded extent, computed by
        # the operator from the call's bound.
        self.words = _words(traced)
        # Equal design keys are one build (two projections on one array).
        # compile() builds the image; the runtime that loads it is made on
        # first use, so a host without an NPU can still compile.
        placement = (
            {} if arena is None else dict(arena=arena.plan, residents=traced.residents)
        )
        self.sequence = traced.sequence(dispatch=plan.dispatch, **placement).compile(
            record=record
        )
        self.image = self.sequence.image
        # What the image consists of, by identity: its designs, which step
        # runs which, and where each buffer lands in its plan.
        self.artifacts = self.sequence.artifacts
        self._callable = None
        # Weights in this image's buffers, by storage key; an arena's own set
        # when there is one, since then every image's weights are the same.
        self._loaded: set = set() if arena is None else arena.loaded

    @property
    def callable(self):
        """The loaded image, made on first use (needs the XRT runtime)."""
        if self._callable is None:
            self._callable = self.sequence.get_callable(self.arena)
        return self._callable

    @property
    def is_loaded(self) -> bool:
        """Whether the image is on the device, so a call pays no setup."""
        return self._callable is not None

    # -- buffers ---------------------------------------------------------------

    def buffer(self, x):
        """The device buffer of a state, a weight tensor, or a handle."""
        if isinstance(x, State):
            name = self.traced.states[id(x)][1].name
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
        _store(buf.numpy_view(), tensor)
        buf.to("npu")

    def read(self, x):
        """A state's or weight's current contents, as a host tensor of its shape."""
        buf = self.buffer(x)
        buf.to("cpu")
        return buf.numpy().reshape(tuple(x.shape))

    def _copy_in(
        self,
        name,
        tensor,
        release: Callable[[np.ndarray], None] | None = None,
        piece_bytes: int = UPLOAD_PIECE,
    ) -> None:
        view = self.callable.get_buffer(name).numpy_view()
        _store(view, tensor, release, piece_bytes)

    def upload(
        self,
        release: Callable[[np.ndarray], None] | None = None,
        piece_bytes: int = UPLOAD_PIECE,
    ) -> None:
        """Copy every closed-over weight into its buffer, once per storage.

        ``release``, if given, is called with each piece of each weight (a
        flat view of at most ``piece_bytes``) as soon as it is in its
        buffer, so the weight's owner can drop the host copy's pages. In an
        arena that is the last time the weight is read: a grown arena keeps
        the device's contents.
        """
        for key, (tensor, handle) in self.traced.weights.items():
            if key not in self._loaded:
                self._copy_in(handle.name, tensor, release, piece_bytes)
                self._loaded.add(key)

    def load(
        self,
        release: Callable[[np.ndarray], None] | None = None,
        piece_bytes: int = UPLOAD_PIECE,
    ) -> CompiledGraph:
        """Load the image and upload its weights now, rather than on first
        call; ``release`` and ``piece_bytes`` as for :meth:`upload`.

        The image is loaded even when there is nothing to upload: in an
        arena, another version may have put every weight there already, and
        loading on first call cost Llama's first prefill 88 ms.
        """
        if not self.is_loaded:
            self._callable = self.sequence.get_callable(self.arena)
        self.upload(release, piece_bytes)
        return self

    # -- calling ---------------------------------------------------------------

    def __call__(self, *tensors, **values) -> Any:
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
        if not self.words:
            return
        self.callable.write_values(
            {
                symbol: np.dtype(dtype).type(word(values))
                for symbol, dtype, word in self.words
            }
        )


def _words(traced: TracedGraph) -> list[tuple[str, Any, Callable[[Mapping], Any]]]:
    """The scratchpad words a call writes, each from the call's values."""
    words: list[tuple[str, Any, Callable[[Mapping], Any]]] = []
    for b in traced.bindings:
        words.append(
            (b.symbol, b.value.dtype, lambda v, b=b: v[b.value.name] * b.scale)
        )
    seen: set[int] = set()
    for b in traced.bindings:
        op = b.op
        if id(op) in seen or not isinstance(b.member.member, Extent):
            continue
        seen.add(id(op))
        extents = [
            (e.member.name, e.value.name, e.scale)
            for e in traced.bindings
            if e.op is op and isinstance(e.member.member, Extent)
        ]

        def at(v, extents=extents):
            return {name: v[graph_name] * scale for name, graph_name, scale in extents}

        for name in sorted(op._per_call_derived() - op.bound_values.keys()):
            word = op.value(name)  # a value the graph binds itself is above
            symbol = device_symbol(op, word)
            words.append(
                (
                    symbol,
                    word.dtype,
                    lambda v, op=op, name=name, at=at: op.derived_at(name, **at(v)),
                )
            )
    return words


@overload
def graph(fn: Callable[..., Any], /) -> GraphFunction: ...
@overload
def graph(
    *, names_from: Any = None, profile: Profile | None = None
) -> Callable[[Callable[..., Any]], GraphFunction]: ...
def graph(
    fn: Callable[..., Any] | None = None,
    *,
    names_from: Any = None,
    profile: Profile | None = None,
) -> Any:
    """Declare a graph function; see the module docstring.

    ``profile`` is a :class:`~iron.common.declare.Profile` applied whenever
    the function's body runs: traced, compiled or run as a reference.
    """
    if fn is None:
        return lambda f: GraphFunction(f, names_from, profile)
    return GraphFunction(fn, names_from, profile)
