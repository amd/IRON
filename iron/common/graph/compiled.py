# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph, and the images it compiles to.

A graph is compiled once per input signature (shapes and dtypes): each is a
*version*, its own image. Every version reads the same weights and states,
and on a full ELF they share one scratch arena
(:class:`~iron.common.image.ArenaPlan`), so a weight is on the device once
and a state one version writes is where the next reads it. This needs no
setup: calling the graph with a new shape compiles a version into the arena
its other versions already use.
"""

from __future__ import annotations

import contextlib
import dataclasses
import functools
import inspect
from collections.abc import Callable, Mapping
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import aie.utils as aie_utils
import numpy as np
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare.member import Extent, ValueSpec, _Value
from ..declare.operator import _ExtentWord
from ..declare.profile import Profile
from ..design import device_symbol
from ..image.allocator import ArenaPlan
from ..image.callable import ScratchArena
from ..image.packaging import Plan, plan
from ..image.sequence import ALIGNMENT
from .handle import Handle, State, Value, _tensor_dtype, is_operand
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


class Graph:
    """A graph: a subclass whose :meth:`body` is traced on handles.

    ``body``'s positional parameters are the inputs, its keyword-only ones
    (annotated ``Scratchpad[T]`` or ``DispatchTime[T]``) the per-call values,
    and what it returns the outputs. An input defaulting to None may be left
    out: the version without it is traced with None in its place, and
    ``body`` branches on that as it does on a shape. The weights and states are what the
    instance holds: a tensor or an :func:`~.handle.state` in an attribute,
    or in a list, tuple, dict, dataclass or namespace there, named by its
    path (``self.layers[3].q`` is ``layers.3.q``). A tensor ``body`` reaches
    any other way is a weight too, named ``w<n>``.

    ``profile`` is the :class:`~iron.common.declare.Profile` applied
    whenever ``body`` runs -- traced, compiled or as a reference -- or a
    directory of them, ``<device>.json``, of which the bound device's is
    read. A subclass or an instance sets it.
    """

    profile: Profile | Path | None = None

    # (name) per input, (name -> spec) per per-call value: body's signature.
    _inputs: list[str] = []
    _values: dict[str, ValueSpec] = {}
    # The inputs defaulting to None, which a version may be traced without.
    _optional: frozenset[str] = frozenset()

    def body(self, *inputs: Any, **values: Any) -> Any:
        raise NotImplementedError(f"{type(self).__name__} defines no body()")

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "body" not in cls.__dict__:
            return  # its parent's inputs and values
        params = list(inspect.signature(cls.body).parameters.values())[1:]
        cls._inputs = [
            p.name
            for p in params
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        ]
        cls._values = {}
        optional = set()
        for p in params:
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD):
                if p.default is None:
                    optional.add(p.name)
                elif p.default is not p.empty:
                    raise TypeError(
                        f"{cls.__name__}.body: input {p.name!r} defaults to "
                        f"{p.default!r}; an input may only default to None"
                    )
            elif p.kind is p.KEYWORD_ONLY:
                ann = p.annotation
                if isinstance(ann, type) and issubclass(ann, _Value):
                    ann = ValueSpec(ann.kind, np.int32)
                if not isinstance(ann, ValueSpec):
                    raise TypeError(
                        f"{cls.__name__}.body: keyword-only parameter {p.name!r} "
                        f"is a per-call value and must be annotated Scratchpad[T] "
                        f"or DispatchTime[T]"
                    )
                cls._values[p.name] = ann
            elif p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                raise TypeError(
                    f"{cls.__name__}.body: *args/**kwargs are not traceable"
                )
        cls._optional = frozenset(optional)

    @property
    def name(self) -> str:
        return type(self).__name__

    @functools.cached_property
    def _versions(self) -> dict[Signature, CompiledGraph]:
        return {}

    @functools.cached_property
    def _arena(self) -> ScratchArena:
        return ScratchArena(ArenaPlan(ALIGNMENT))

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

    def names(self) -> dict[int, str]:
        """The name of each tensor and state the instance holds, by identity."""
        names: dict[int, str] = {}
        seen: set[int] = set()

        def walk(x, path):
            if isinstance(x, State) or (is_operand(x) and not isinstance(x, Handle)):
                names.setdefault(id(x), path)
                return
            if isinstance(x, (list, tuple)):
                items = enumerate(x)
            elif isinstance(x, dict):
                items = x.items()
            elif dataclasses.is_dataclass(x) and not isinstance(x, type):
                items = ((f.name, getattr(x, f.name)) for f in dataclasses.fields(x))
            elif isinstance(x, SimpleNamespace):
                items = vars(x).items()
            else:
                return
            if id(x) in seen:
                return
            seen.add(id(x))
            for key, item in items:
                walk(item, f"{path}.{key}")

        for key, x in vars(self).items():
            if not key.startswith("_"):
                walk(x, key)
        return names

    def trace(self, **shapes) -> TracedGraph:
        """Run :meth:`body` on handles of the given shapes; return the graph.

        An input defaulting to None that is given no shape (or None) is
        absent: ``body`` sees None for it, and the version takes no such
        input.
        """
        shapes = {k: v for k, v in shapes.items() if v is not None}
        missing = [
            p for p in self._inputs if p not in shapes and p not in self._optional
        ]
        unknown = [k for k in shapes if k not in self._inputs]
        if missing or unknown:
            raise TypeError(
                f"{self.name}: shapes for {missing} missing"
                + (f"; {unknown} are not inputs" if unknown else "")
            )
        inputs: list[Handle] = []
        args: list[Handle | None] = []
        for name in self._inputs:
            if name not in shapes:
                args.append(None)
                continue
            shape, dtype = _shape_and_dtype(shapes[name])
            inputs.append(Handle(shape, dtype, name, "input"))
            args.append(inputs[-1])
        values = [Value(n, spec.kind, spec.dtype) for n, spec in self._values.items()]
        with self._scope(), Tracer(self.name, self.names()) as tracer:
            result = self.body(*args, **{v.name: v for v in values})
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
                    f"{self.name} returned {item!r}; a graph returns whole "
                    f"handles produced inside it"
                )
            if item.role == "input":
                raise TypeError(
                    f"{self.name} returns its input {item.name!r} unchanged"
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
        chosen = plan(
            aie_utils.ensure_current_device(required=True), traced, boundaries, image
        )
        if verbose:
            print(chosen.report(self.name))
        signature = self._signature(traced.inputs)
        shared = chosen.dispatch == "fused"
        # Versions see one state only through the arena. Weights alone could
        # be copied per version, so a stateless graph still compiles.
        others = [v for k, v in self._versions.items() if k != signature]
        apart = not shared or any(v.arena is None for v in others)
        stateful = traced.states or any(v.traced.states for v in others)
        if others and apart and stateful:
            raise NotImplementedError(
                f"{self.name}: versions share their states through one "
                f"scratch arena, which only a full ELF addresses; this version "
                f"dispatches {chosen.dispatch!r}"
            )
        version = CompiledGraph(
            traced, chosen, record=record, arena=self._arena if shared else None
        )
        self._versions[signature] = version
        return version

    def _given(self, tensors) -> dict[str, Any]:
        """Input name -> tensor, for the inputs a call passes (in order)."""
        if len(tensors) > len(self._inputs):
            raise TypeError(
                f"{self.name} takes {len(self._inputs)} input(s), got {len(tensors)}"
            )
        given = {n: t for n, t in zip(self._inputs, tensors) if t is not None}
        missing = [
            p for p in self._inputs if p not in given and p not in self._optional
        ]
        if missing:
            raise TypeError(f"{self.name}: inputs {missing} missing")
        return given

    def __call__(self, *tensors, **values) -> Any:
        given = self._given(tensors)
        signature = tuple(
            (name, tuple(int(n) for n in t.shape), bfp.dtype_name(_tensor_dtype(t)))
            for name, t in given.items()
        )
        version = self._versions.get(signature)
        if version is None:
            shapes = {
                name: (tuple(t.shape), _tensor_dtype(t)) for name, t in given.items()
            }
            print(f"{self.name}: compiling for {shapes}")
            # A checker matches **shapes against compile()'s named parameters.
            version = self.compile(**shapes)  # pyright: ignore[reportArgumentType]
        return version(*given.values(), **values)

    def reference(self, *tensors, **values):
        """:meth:`body` on host tensors, each operator run through its ``reference()``.

        An optional input left out, or passed as None, is None in ``body``.
        """
        args = list(tensors) + [None] * (len(self._inputs) - len(tensors))
        with self._scope(), _ReferenceTracer(self.name):
            return self.body(*args, **{k: values.get(k) for k in self._values})

    def _scope(self):
        """The profile applied while :meth:`body` runs, if there is one."""
        profile = self.profile
        if isinstance(profile, (str, Path)):
            dev = aie_utils.ensure_current_device(required=True)
            path = Path(profile) / f"{dev.name}.json"
            if not path.exists():
                raise ValueError(f"{self.name}: no profile {path}")
            profile = Profile.load(path)
        return profile if profile is not None else contextlib.nullcontext()


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
        # On a full ELF, symbols that always hold one number share a word:
        # ``shared`` maps each such design symbol to its word.
        self.words, self.shared = _words(traced, share=plan.dispatch == "fused")
        # Equal design keys are one build (two projections on one array).
        # compile() builds the image; the runtime that loads it is made on
        # first use, so a host without an NPU can still compile.
        placement = (
            {} if arena is None else dict(arena=arena.plan, residents=traced.residents)
        )
        self.sequence = traced.sequence(
            dispatch=plan.dispatch, shared_words=self.shared, **placement
        ).compile(record=record)
        self.image = self.sequence.image
        # What the image consists of, by identity: its designs, which step
        # runs which, and where each buffer lands in its plan.
        self.artifacts = self.sequence.artifacts
        if self.artifacts.kind == "elf":
            # The image declares only the words its designs read: an extent
            # read only through its derivations has none.
            self.words = [w for w in self.words if w[0] in self.artifacts.parameters]
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

    def _buffer_name(self, x) -> str:
        if isinstance(x, State):
            return self.traced.states[id(x)][1].name
        if isinstance(x, Handle):
            return x.buffer_name
        if id(x) in self.traced.weights:
            return self.traced.weights[id(x)][1].name
        raise KeyError(f"{x!r} is not a state, weight or handle of this graph")

    def buffer(self, x):
        """The device buffer of a state, a weight tensor, or a handle."""
        return self.callable.get_buffer(self._buffer_name(x))

    def _storage(self, x):
        """A host-synchronizable flat view that starts with ``x``'s buffer
        (a slice's own, which is aligned, else the whole of its lines)."""
        name = self._buffer_name(x)
        if isinstance(x, Handle) and x.parent is not None:
            return self.callable.get_buffer(name)
        return self.callable.get_storage(name)

    def write(self, x, tensor) -> None:
        """Copy ``tensor`` into a state's or weight's buffer and push it to the device."""
        buf = self._storage(x)
        _store(buf.numpy_view()[: int(np.prod(x.shape))], tensor)
        buf.to("npu")

    def read(self, x):
        """A state's or weight's current contents, as a host tensor of its shape."""
        buf = self._storage(x)
        buf.to("cpu")
        return buf.numpy()[: int(np.prod(x.shape))].reshape(tuple(x.shape))

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


def _words(
    traced: TracedGraph, *, share: bool = False
) -> tuple[list[tuple[str, Any, Callable[[Mapping], Any]]], dict[str, str]]:
    """The scratchpad words a call writes, each from the call's values, and
    with ``share`` the design symbols that share one word.

    A word is a bound value (a per-call index on a view, scaled to an
    element offset) or a value an operator, resolved for the device, derives
    from a bounded extent, computed from the call's bound. The full ELF has
    32 words for its whole image, and a bounded prompt binds its row count
    to every operator's extents, so symbols that always hold one number
    share a word: those that are one graph value times one ratio plus one
    offset (a bound expression's, or a bounded extent's over the lanes and
    rows it is divided into), rounded up, in one dtype. Any other
    derivation keeps its own word.
    """
    dev = aie_utils.get_current_device()
    # (symbol, dtype, word, (graph value, ratio, offset, dtype) or None)
    words: list[tuple[str, Any, Callable[[Mapping], Any], Any]] = []
    for b in traced.bindings:
        e = b.expression
        key = (e.value.name, Fraction(e.scale), Fraction(e.bias))
        key += (np.dtype(b.member.dtype).name,)
        words.append((b.symbol, e.dtype, lambda v, e=e: e.evaluate(v), key))
    seen: set[int] = set()
    derived: set[str] = set()
    for b in traced.bindings:
        if id(b.op) in seen or not isinstance(b.member.member, Extent):
            continue
        seen.add(id(b.op))
        op = b.op.resolved(dev)
        extents = {
            e.member.name: e.expression
            for e in traced.bindings
            if e.op is b.op and isinstance(e.member.member, Extent)
        }

        def at(v, extents=extents):
            return {name: count.evaluate(v) for name, count in extents.items()}

        for name in sorted(op._per_call_derived() - op.bound_values.keys()):
            word = op.value(name)  # a value the graph binds itself is above
            symbol = device_symbol(op, word)
            if symbol in derived:
                continue  # another instance of the design, bound alike
            derived.add(symbol)
            key = None
            spec = word.member
            if isinstance(spec, _ExtentWord) and spec.extent.name in extents:
                count, divisor = extents[spec.extent.name], spec.divisor(op)
                key = (
                    count.value.name,
                    Fraction(count.scale, divisor),
                    Fraction(count.bias, divisor),
                    np.dtype(word.dtype).name,
                )
            words.append(
                (
                    symbol,
                    word.dtype,
                    lambda v, op=op, name=name, at=at: op.derived_at(name, **at(v)),
                    key,
                )
            )

    shared: dict[str, str] = {}
    if share:
        keys: dict[str, set] = {}
        for symbol, _, _, key in words:
            keys.setdefault(symbol, set()).add(key)
        groups: dict[Any, list[str]] = {}
        for symbol, found in keys.items():
            if len(found) == 1 and None not in found:
                groups.setdefault(next(iter(found)), []).append(symbol)

        def spell(r: Fraction) -> str:
            # An identifier's: m for minus, d for over.
            den = f"d{r.denominator}" if r.denominator > 1 else ""
            return f"{'m' if r < 0 else ''}{abs(r.numerator)}{den}"

        for (graph, ratio, offset, dtype), symbols in groups.items():
            if len(symbols) > 1:
                name = f"graph_{graph}_x{spell(ratio)}"
                if offset:
                    name += f"{'p' if offset > 0 else 'm'}{spell(abs(offset))}"
                shared.update(dict.fromkeys(symbols, f"{name}_{dtype}"))
    out, written = [], set()
    for symbol, dtype, word, _ in words:
        symbol = shared.get(symbol, symbol)
        if symbol not in written:
            written.add(symbol)
            out.append((symbol, dtype, word))
    return out, shared
