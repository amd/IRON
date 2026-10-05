# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph, and the images it compiles to.

A graph is compiled once per input signature (shapes and dtypes): each is a
*version*, its own image. Every version reads the same weights and states,
and on a full ELF they share one scratch arena
(``ArenaPlan``), so a weight is on the device once
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

from ..declare import Operator
from ..declare.member import Extent, ValueSpec, _Value
from ..declare.operator import _ExtentWord
from ..declare.profile import Profile
from ..design import device_symbol
from ..image.allocator import ArenaPlan
from ..image.artifacts import Parameter
from ..image.callable import FullELFRun, ScratchArena
from ..image.coresidence import AdjacentPacking
from ..image.packaging import ELF, Plan, plan
from ..image.sequence import ALIGNMENT
from .carried import CARRY, EmitSite, Form, attach_emit, compose
from .handle import Affine, Carry, Handle, State, Value, _tensor_dtype, is_operand
from .narrowing import JointNarrowing, Tuning
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
    """A graph: a subclass whose ``body`` is traced on handles.

    ``body``'s positional parameters are the inputs, its keyword-only ones
    (annotated ``Scratchpad[T]`` or ``DispatchTime[T]``) the per-call values,
    and what it returns the outputs. An input defaulting to None may be left
    out: the version without it is traced with None in its place, and
    ``body`` branches on that as it does on a shape. The weights and states are what the
    instance holds: a tensor or an ``state`` in an attribute,
    or in a list, tuple, dict, dataclass or namespace there, named by its
    path (``self.layers[3].q`` is ``layers.3.q``). A tensor ``body`` reaches
    any other way is a weight too, named ``w<n>``.

    ``profile`` is the ``Profile`` applied
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
    # The per-call values annotated Carried[T], which body computes the next of.
    _carried: list[str] = []

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
                    ann = ValueSpec(ann.kind, np.int32, ann.carried)
                if not isinstance(ann, ValueSpec):
                    raise TypeError(
                        f"{cls.__name__}.body: keyword-only parameter {p.name!r} "
                        f"is a per-call value and must be annotated Scratchpad[T], "
                        f"Carried[T] or DispatchTime[T]"
                    )
                cls._values[p.name] = ann
            elif p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                raise TypeError(
                    f"{cls.__name__}.body: *args/**kwargs are not traceable"
                )
        cls._optional = frozenset(optional)
        cls._carried = [n for n, spec in cls._values.items() if spec.carried]

    @property
    def name(self) -> str:
        return type(self).__name__

    @functools.cached_property
    def _versions(self) -> dict[Signature, CompiledGraph]:
        return {}

    @functools.cached_property
    def _arena(self) -> ScratchArena:
        return ScratchArena(ArenaPlan(ALIGNMENT))

    @functools.cached_property
    def _carry(self) -> State | None:
        """The values a call started from and the elements it computed,
        which every full-ELF version's Emit reads (see ``carried``).
        """
        if not self._carried:
            return None
        return State((2, len(self._carried)), np.int32, CARRY)

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
        """Run ``body`` on handles of the given shapes; return the graph.

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
        values = [
            Value(n, spec.kind, spec.dtype, spec.carried)
            for n, spec in self._values.items()
        ]
        with self._scope(), Tracer(self.name, self.names()) as tracer:
            result = self.body(*args, **{v.name: v for v in values})
        items, carry = self._split_carry(result)
        outputs = self._outputs(items, tracer)
        return tracer.finish(
            inputs, outputs, values, self._traced_carry(carry, values, tracer)
        )

    def _split_carry(self, result) -> tuple[list, Carry | None]:
        """The returned outputs, and the ``Carry`` returned last, if any.

        A graph with carried values must return their next values, and one
        without must not.
        """
        if result is None:
            items = []
        elif isinstance(result, (tuple, list)):
            items = list(result)
        else:
            items = [result]
        carry = items.pop() if items and isinstance(items[-1], Carry) else None
        if any(isinstance(item, Carry) for item in items):
            raise TypeError(f"{self.name}: iron.carry(...) is returned last")
        names = [] if carry is None else list(carry)
        missing = [n for n in self._carried if n not in names]
        unknown = [n for n in names if n not in self._carried]
        if missing or unknown:
            raise TypeError(
                f"{self.name}: carries {names}, but its Carried values are "
                f"{self._carried}"
                + (f"; return iron.carry({missing[0]}=...)" if missing else "")
            )
        return items, carry

    def _traced_carry(
        self, carry: Carry | None, values: list[Value], tracer: Tracer
    ) -> dict[str, Handle | Affine]:
        """Each traced next value, checked: an expression of the values, or
        one integer element the graph computed, which becomes an output.
        """
        if carry is None:
            return {}
        dtypes = {v.name: v.dtype for v in values}
        traced: dict[str, Handle | Affine] = {}
        for name, nxt in carry.items():
            if isinstance(nxt, Affine):
                traced[name] = nxt
                continue
            if not isinstance(nxt, Handle):
                raise TypeError(
                    f"{self.name}: the next {name} is {nxt!r}; carry an "
                    f"expression of the values or a handle the graph computed"
                )
            if nxt.parent is not None or nxt.role == "input" or nxt.elements != 1:
                raise TypeError(
                    f"{self.name}: the next {name} is {nxt!r}; a carried "
                    f"handle is one whole element the graph computed"
                )
            if bfp.dtype_name(nxt.dtype) != bfp.dtype_name(dtypes[name]):
                raise TypeError(
                    f"{self.name}: the next {name} is {nxt!r}, but {name} "
                    f"is {np.dtype(dtypes[name]).name}"
                )
            if nxt.role == "intermediate":
                _rename(tracer, nxt, f"carry_{name}")
            traced[name] = nxt
        return traced

    def _outputs(self, items: list, tracer: Tracer) -> list:
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
                _rename(tracer, item, f"out{i}" if len(items) > 1 else "out")
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
        feeds: CompiledGraph | None = None,
        coresident: AdjacentPacking | JointNarrowing | None = None,
        **shapes,
    ) -> CompiledGraph:
        """Compile the version for the given input shapes and return it.

        ``boundaries`` and ``image`` are the two packaging choices
        (``iron.common.image.packaging``); everything else is derived and, under
        ``verbose``, printed. ``record="disk"`` writes the image's
        ``Artifacts`` record beside it.
        ``coresident`` packs designs into shared device configurations
        (``iron.common.image.coresidence``); a full ELF only. A
        ``JointNarrowing`` also narrows designs so that
        they fit; what it chose is the version's ``CompiledGraph.tuning``.

        A full-ELF version is placed in ``arena``, with the weights and
        states of every other version. Compile every version before the
        first call where you can: a version placed after the arena's buffer
        exists grows it, which copies it once.

        A full-ELF version with carried values ends in an Emit step, which
        writes the scratchpad of the version it ``feeds`` -- by default
        itself, where it takes no tensor (nothing would write one between
        its calls) -- so that one can run without the host
        (``CarriedLoop``). A version that
        takes a tensor and feeds nothing has no Emit; a call still returns
        its carried values.
        """
        if dev is not None:
            aie_utils.set_current_device(dev)
        traced = self.trace(**shapes)
        tuning = None
        groups: AdjacentPacking | list[list[Operator]] | None
        if isinstance(coresident, JointNarrowing):
            tuning = coresident.tune(traced, aie_utils.ensure_current_device())
            traced, groups = tuning.apply(traced)
        else:
            groups = coresident
        chosen = plan(aie_utils.ensure_current_device(), traced, boundaries, image)
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
        emit = None
        # The words an Emit feeding its own version was sized for.
        sized: list[Word] | None = None
        loops = feeds is not None or not traced.inputs
        if chosen.image == ELF and traced.carry and loops:
            if feeds is None:
                sized = _words(traced, share=shared, extents=False)[0]
                slots = len(sized)
            elif feeds.emit is None or not any(
                feeds is v for v in self._versions.values()
            ):
                raise ValueError(
                    f"{self.name}: feeds= takes a full-ELF version of this "
                    f"graph, got {feeds!r}"
                )
            else:
                slots = len(feeds.parameters)
            assert self._carry is not None
            emit = attach_emit(traced, self._carried, self._carry, slots)
        elif feeds is not None:
            raise ValueError(
                f"{self.name}: only a full-ELF version with carried values "
                f"feeds another"
            )
        version = CompiledGraph(
            traced,
            chosen,
            record=record,
            arena=self._arena if shared else None,
            emit=emit,
            coresident=groups,
            tuning=tuning,
        )
        if sized is not None and len(version.parameters) != len(sized):
            read = {p.name for p in version.parameters}
            raise NotImplementedError(
                f"{self.name}: the image reads {len(version.parameters)} of the "
                f"{len(sized)} words its Emit was sized for; a word it reads only "
                f"through a derivation cannot be fed yet (sized for but not "
                f"read: {sorted(w.symbol for w in sized if w.symbol not in read)})"
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
            version = self.compile(**shapes)
        return version(*given.values(), **values)

    def reference(self, *tensors, **values) -> Any:
        """``body`` on host tensors, each operator run through its ``reference()``.

        An optional input left out, or passed as None, is None in ``body``.
        Returns what a call returns: the outputs, then the next values of
        the carried ones as numbers.
        """
        args = list(tensors) + [None] * (len(self._inputs) - len(tensors))
        with self._scope(), _ReferenceTracer(self.name):
            result = self.body(*args, **{k: values.get(k) for k in self._values})
        items, carry = self._split_carry(result)
        if carry is None:
            return result
        nxt = Carry(**{n: int(np.asarray(v).reshape(-1)[0]) for n, v in carry.items()})
        return _results(items, nxt)

    def _scope(self):
        """The profile applied while ``body`` runs, if there is one."""
        profile = self.profile
        if isinstance(profile, (str, Path)):
            dev = aie_utils.ensure_current_device()
            if dev is None:
                raise ValueError(f"{self.name}: a profile is per device; none is bound")
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
        emit: EmitSite | None = None,
        coresident: AdjacentPacking | list[list[Operator]] | None = None,
        tuning: Tuning | None = None,
    ):
        self.traced = traced
        self.plan = plan
        self.arena = arena
        # What a JointNarrowing chose for this version; None without one.
        self.tuning = tuning
        # Where the Emit step ending a full ELF with carried values reads
        # and writes; None without one.
        self.emit = emit
        # Each scratchpad word a call writes (``Word``): each bound value (a
        # per-call index on a view scaled to an element offset), and each
        # value derived from a bounded extent, computed by the operator from
        # the call's bound.
        # On a full ELF, symbols that always hold one number share a word:
        # ``shared`` maps each such design symbol to its word.
        self.words, self.shared = _words(
            traced, share=plan.dispatch == "fused", extents=plan.image != ELF
        )
        # Equal design keys are one build (two projections on one array).
        # compile() builds the image; the runtime that loads it is made on
        # first use, so a host without an NPU can still compile.
        placement: dict[str, Any] = (
            {} if arena is None else dict(arena=arena.plan, residents=traced.residents)
        )
        if coresident:
            placement["coresident"] = coresident
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
            self.words = [
                w for w in self.words if w.symbol in self.artifacts.parameters
            ]
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
    def parameters(self) -> list[Parameter]:
        """The per-call values a full ELF's scratchpad holds, as its
        parameter table lays them out; none on another image.
        """
        return self.artifacts.parameter_table

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
        (a slice's own, which is aligned, else the whole of its lines).
        """
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
        call; ``release`` and ``piece_bytes`` as for ``upload``.

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
        self._stage(tensors, values)
        self.callable()
        outputs = [self.callable.get_buffer(h.name) for h in self.traced.returned]
        if not self.traced.carry:
            return _results(outputs, None)
        return _results(outputs, self._next_values(values))

    def start(self, run: FullELFRun, /, *tensors, **values) -> None:
        """Start a call of this full ELF on ``run`` (one of its callable's
        ``new_run()``), without waiting for it.
        """
        self._stage(tensors, values, run)
        self.callable.start(run)

    def emit_to(self, target: CompiledGraph) -> None:
        """Program this version's Emit to start a call of ``target``: its
        scratchpad words, and the carried values it starts from.
        """
        if self.emit is None:
            raise ValueError(f"{self.traced.name}: this version has no Emit step")
        program = compose(self.emit, self.traced.carry, target.words, target.parameters)
        self.write(self.emit.program, program)

    def _stage(self, tensors, values, run: FullELFRun | None = None) -> None:
        """Everything a call writes before it is dispatched: the weights not
        yet uploaded, the inputs, and the per-call values, into ``run``'s
        scratchpad (the callable's own by default).
        """
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
        self._write_values(values, run)

    def _next_values(self, values: Mapping[str, int]) -> Carry:
        """The carried values' next values, after a call with ``values``: an
        expression evaluated here, a computed element read back.
        """
        nxt: dict[str, int] = {}
        planes = None if self.emit is None else self.read(self.emit.carry)
        for name, expression in self.traced.carry.items():
            if isinstance(expression, Affine):
                nxt[name] = expression.evaluate(values)
            elif planes is not None:
                # Computed into the carry's second plane (see .carried).
                assert self.emit is not None
                nxt[name] = int(planes[1, self.emit.carried.index(name)])
            else:
                buf = self.callable.get_buffer(expression.name)
                buf.to("cpu")
                nxt[name] = int(buf.numpy().reshape(-1)[0])
        return Carry(**nxt)

    def _write_values(self, values, run: FullELFRun | None = None) -> None:
        expected = {v.name for v in self.traced.values}
        missing, unknown = expected - set(values), set(values) - expected
        if missing or unknown:
            raise TypeError(
                f"{self.traced.name}: per-call values {sorted(missing)} missing"
                + (f"; {sorted(unknown)} unknown" if unknown else "")
            )
        if self.emit is not None:
            # The values this call starts from, for its Emit.
            n = len(self.emit.carried)
            head = self._storage(self.emit.carry).numpy_view()
            head[:n] = [values[name] for name in self.emit.carried]
        if not self.words:
            return
        words = {w.symbol: np.dtype(w.dtype).type(w(values)) for w in self.words}
        (self.callable if run is None else run).write_values(words)


def _rename(tracer: Tracer, handle: Handle, name: str) -> None:
    """Make an intermediate a graph output named ``name``: the handle, and
    every view of its buffer the steps hold (a reshape is a new handle).
    """
    old = handle.name
    for step in tracer.steps:
        for h in step.slots + step.inputs + step.outputs:
            for view in (h, h.parent):  # a slice names its parent's buffer
                if (
                    view is not None
                    and view.role == "intermediate"
                    and view.name == old
                ):
                    view.name, view.role = name, "output"
    handle.name, handle.role = name, "output"


def _results(outputs: list, carry: Carry | None):
    """A call's return, shaped as the body's: one output alone, several as
    a tuple, and the carry last.
    """
    items = list(outputs) + ([] if carry is None else [carry])
    if not items:
        return None
    return items[0] if len(items) == 1 else tuple(items)


@dataclasses.dataclass(frozen=True)
class Linear:
    """A word as one graph value times a ratio plus an offset, rounded up."""

    value: str
    ratio: Fraction
    offset: Fraction
    dtype: str  # the word's, by name: two dtypes of one number are two words

    @property
    def is_integral(self) -> bool:
        """Whether it rounds nothing: an integer scale and offset."""
        return self.ratio.denominator == 1 and self.offset.denominator == 1


@dataclasses.dataclass(frozen=True)
class Word:
    """A scratchpad word a call writes: its device symbol, its dtype, how it
    follows from the call's values and, where it has them, the linear form it
    has in one graph value (by which words share) and the form an Emit row
    computes it by.
    """

    symbol: str
    dtype: Any
    compute: Callable[[Mapping[str, int]], Any]
    linear: Linear | None
    form: Form | None = None

    def __call__(self, values: Mapping[str, int]) -> Any:
        return self.compute(values)


def _derived_form(op, name: str, symbolic: Mapping[str, Form]) -> Form | None:
    """The Emit form of ``op``'s derived value ``name``: its derivation run
    on the forms of the bounds, or ``None`` where it does more than a form
    can (it compares, or divides by other than a power of two).
    """
    try:
        got = op.derived_at(name, **symbolic)
    except TypeError:
        return None
    if isinstance(got, Form):
        return got
    if isinstance(got, (int, np.integer)) and symbolic:  # the same every call
        value = next(iter(symbolic.values())).value
        return Form(value, 0, 0, add=int(got))
    return None


def _words(
    traced: TracedGraph, *, share: bool = False, extents: bool = True
) -> tuple[list[Word], dict[str, str]]:
    """The scratchpad words a call writes, each from the call's values, and
    with ``share`` the design symbols that share one word.

    A word is a bound value (a per-call index on a view, scaled to an
    element offset) or a value an operator, resolved for the device, derives
    from a bounded extent, computed from the call's bound. With ``extents``
    a bound extent is a word itself, as an xclbin's dispatch scalar is;
    without, it is not, as on a full ELF, where no design reads one but
    through what it derives from it. The full ELF has
    32 words for its whole image, and a bounded prompt binds its row count
    to every operator's extents, so symbols that always hold one number
    share a word: those whose derivation is ``Linear`` (a bound
    expression, or a bounded extent over the lanes and rows it is divided
    into), in one dtype. Any other derivation keeps its own word.
    """
    dev = aie_utils.get_current_device()
    words: list[Word] = []
    for b in traced.bindings:
        if not extents and isinstance(b.member.member, Extent):
            continue  # its derivations below
        e = b.expression
        linear = Linear(
            e.value.name,
            Fraction(e.scale),
            Fraction(e.bias),
            np.dtype(b.member.dtype).name,
        )
        form = Form(e.value.name, int(e.scale), int(e.bias))
        words.append(
            Word(b.symbol, e.dtype, lambda v, e=e: e.evaluate(v), linear, form)
        )
    seen: set[int] = set()
    derived: set[str] = set()
    for b in traced.bindings:
        if id(b.op) in seen or not isinstance(b.member.member, Extent):
            continue
        seen.add(id(b.op))
        op = b.op.resolved(dev)
        counts = {
            e.member.name: e.expression
            for e in traced.bindings
            if e.op is b.op and isinstance(e.member.member, Extent)
        }
        symbolic = {
            name: Form(count.value.name, int(count.scale), int(count.bias))
            for name, count in counts.items()
        }

        def at(v, counts=counts):
            return {name: count.evaluate(v) for name, count in counts.items()}

        for name in sorted(op._per_call_derived() - op.bound_values.keys()):
            word = op.value(name)  # a value the graph binds itself is above
            symbol = device_symbol(op, word)
            if symbol in derived:
                continue  # another instance of the design, bound alike
            derived.add(symbol)
            linear = None
            spec = word.member
            if isinstance(spec, _ExtentWord) and spec.extent.name in counts:
                count, divisor = counts[spec.extent.name], spec.divisor(op)
                linear = Linear(
                    count.value.name,
                    Fraction(count.scale, divisor),
                    Fraction(count.bias, divisor),
                    np.dtype(word.dtype).name,
                )
            words.append(
                Word(
                    symbol,
                    word.dtype,
                    lambda v, op=op, name=name, at=at: op.derived_at(name, **at(v)),
                    linear,
                    _derived_form(op, name, symbolic),
                )
            )

    shared: dict[str, str] = {}
    if share:
        forms: dict[str, set[Linear | None]] = {}
        for w in words:
            forms.setdefault(w.symbol, set()).add(w.linear)
        groups: dict[Linear, list[str]] = {}
        for symbol, found in forms.items():
            if len(found) == 1 and None not in found:
                groups.setdefault(next(iter(found)), []).append(symbol)

        def spell(r: Fraction) -> str:
            # An identifier's: m for minus, d for over.
            den = f"d{r.denominator}" if r.denominator > 1 else ""
            return f"{'m' if r < 0 else ''}{abs(r.numerator)}{den}"

        for form, symbols in groups.items():
            if len(symbols) > 1:
                name = f"graph_{form.value}_x{spell(form.ratio)}"
                if form.offset:
                    name += (
                        f"{'p' if form.offset > 0 else 'm'}{spell(abs(form.offset))}"
                    )
                shared.update(dict.fromkeys(symbols, f"{name}_{form.dtype}"))
    out: list[Word] = []
    written: set[str] = set()
    for w in words:
        symbol = shared.get(w.symbol, w.symbol)
        if symbol not in written:
            written.add(symbol)
            out.append(dataclasses.replace(w, symbol=symbol))
    return out, shared
