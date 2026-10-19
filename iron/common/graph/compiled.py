# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph, and the images it compiles to: one version per input signature.

Versions share one scratch arena, so a weight is on the device once and a
state one version writes is where the next reads it: a full ELF places its
scratch there, an xclbin its weights and states.
"""

from __future__ import annotations

import contextlib
import dataclasses
import functools
import inspect
import logging
from collections.abc import Callable, Iterator, Mapping
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
from typing import Annotated, Any, get_args, get_origin

import aie.utils as aie_utils
import numpy as np
from aie.utils import bfp
from ml_dtypes import bfloat16

from ..declare import Operator
from ..declare.operator import device_fit, graph_tracer
from ..declare.value import Extent, ExtentWord
from ..declare.precision import Precision
from ..declare.profile import Profile
from ..image.allocator import ArenaPlan
from ..image.artifacts import Parameter
from ..image.callable import FullELFRun, ScratchArena
from ..image.coresidence import AdjacentPacking
from ..image.packaging import Kind, Plan, plan, require_device
from ..image.sequence import ALIGNMENT, OperatorSequence
from ..image.step import BufferRef
from .carried import CARRY, EmitSite, attach_emit, compose
from .fill import filled
from .handle import Affine, Carry, Handle, PerCall, State, Weight, is_operand
from .trace import TracedGraph, Tracer

logger = logging.getLogger(__name__)

# One (parameter, shape, dtype name) per input: what picks a version.
Signature = tuple[tuple[str, tuple[int, ...], str], ...]


def _shape_and_dtype(spec):
    if (
        isinstance(spec, tuple)
        and len(spec) == 2
        and isinstance(spec[0], (tuple, list))
    ):
        return tuple(spec[0]), spec[1]
    return tuple(spec), bfloat16


def _kind(dtype):
    # np.dtype.kind calls bfloat16 "V".
    return "f" if dtype == bfloat16 else np.dtype(dtype).kind


UPLOAD_PIECE = 64 * 2**20


def _store(
    view: np.ndarray,
    tensor,
    release: Callable[[np.ndarray], None] | None = None,
    piece_bytes: int = UPLOAD_PIECE,
) -> None:
    """Copy ``tensor`` into a buffer view, casting in place (``astype`` would
    fault in a whole temporary); ``release`` gets each piece once copied.
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


@dataclasses.dataclass(frozen=True)
class _Parameters:
    """A body's inputs, which of them may be left out, and its per-call
    values, read from its signature."""

    inputs: list[str]
    values: dict[str, tuple[Kind, Any]]
    optional: frozenset[str]

    @property
    def carried(self) -> list[str]:
        return [n for n, (kind, _) in self.values.items() if kind is Kind.CARRIED]

    @classmethod
    def of(cls, owner: str, signature: inspect.Signature) -> _Parameters:
        """``signature``'s parameters, ``self`` left out, as a graph reads them.

        Raises:
            TypeError: An input defaults to other than None or is named as a
                ``compile()`` keyword, a per-call value is unannotated or
                floating point, or a parameter is ``*args``/``**kwargs``.
        """
        params = list(signature.parameters.values())
        inputs = [
            p.name
            for p in params
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        ]
        keywords = inspect.signature(Graph.compile).parameters
        taken = [
            n
            for n in inputs
            if n in keywords and keywords[n].kind is not keywords[n].VAR_KEYWORD
        ]
        if taken:
            raise TypeError(
                f"{owner}.body: inputs {taken} are named as compile()'s "
                f"keywords, so no shape could be given them; rename them"
            )
        values = {}
        optional = set()
        for p in params:
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD):
                if p.default is None:
                    optional.add(p.name)
                elif p.default is not p.empty:
                    raise TypeError(
                        f"{owner}.body: input {p.name!r} defaults to "
                        f"{p.default!r}; an input may only default to None"
                    )
            elif p.kind is p.KEYWORD_ONLY:
                ann = p.annotation
                marks = ann.__metadata__ if get_origin(ann) is Annotated else ()
                kinds = [k for k in Kind if k.value in marks]
                if not kinds:
                    raise TypeError(
                        f"{owner}.body: keyword-only parameter {p.name!r} "
                        f"is a per-call value and must be annotated Scratchpad[T], "
                        f"Carried[T] or aie.iron.DispatchTime[T]"
                    )
                dtype = get_args(ann)[0]
                if np.dtype(dtype).kind == "f":
                    raise TypeError(
                        f"{owner}.body: per-call value {p.name!r} cannot be "
                        f"floating point: the scratchpad encoding zeroes the top "
                        f"two bits of the value"
                    )
                values[p.name] = (kinds[0], dtype)
            elif p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                raise TypeError(f"{owner}.body: *args/**kwargs are not traceable")
        return cls(inputs, values, frozenset(optional))


class _Param(np.ndarray):
    """A ``param`` not yet bound: no storage, only its shape and dtype."""


def param(*shape: int, dtype=bfloat16) -> np.ndarray:
    """A weight a graph declares by shape, typed as the array
    ``Graph.load_state_dict`` binds in its place.
    """
    return np.broadcast_to(np.zeros((), dtype), shape).view(_Param)


def _leaves(
    root, graphs: bool = True, shared: list[str] | None = None
) -> Iterator[tuple[str, Any, Any, Any]]:
    """Each state and tensor under ``root``, by its dotted path from it, with
    the container holding it and its key there, through lists, tuples,
    dicts, dataclasses, namespaces and graphs (their attributes not starting
    with ``_``), each container once, the path it is met at again appended
    to ``shared``; without ``graphs``, a graph under ``root`` is yielded in
    place of what it holds.
    """
    seen: set[int] = set()

    def walk(x, path, parent, key):
        if (
            isinstance(x, State)
            or (is_operand(x) and not isinstance(x, Handle))
            or (not graphs and isinstance(x, Graph) and x is not root)
        ):
            yield path, x, parent, key
            return
        if isinstance(x, (list, tuple)):
            items = enumerate(x)
        elif isinstance(x, dict):
            items = x.items()
        elif dataclasses.is_dataclass(x) and not isinstance(x, type):
            items = ((f.name, getattr(x, f.name)) for f in dataclasses.fields(x))
        elif isinstance(x, SimpleNamespace):
            items = vars(x).items()
        elif isinstance(x, Graph):
            items = ((k, v) for k, v in vars(x).items() if not k.startswith("_"))
        else:
            return
        if id(x) in seen:
            if shared is not None:
                shared.append(path)
            return
        seen.add(id(x))
        for k, item in items:
            yield from walk(item, f"{path}.{k}" if path else str(k), x, k)

    return walk(root, "", None, None)


class Graph:
    """A graph: a subclass whose ``body`` is traced on handles.

    ``body``'s positional parameters are the inputs (one defaulting to None
    may be left out), its keyword-only ones the per-call values, and what it
    returns the outputs; a graph whose inputs and values follow what it
    holds names them in ``signature()`` instead. Weights and states are what
    the instance holds, named by attribute path (``self.layers[3].q`` is
    ``layers.3.q``). ``profile`` is a ``Profile`` or a directory of
    ``<device>.json`` ones, the one way a step's tunables come from one.
    ``precision`` is the
    most any step may round (``Precision``): a step that would round more
    is raised to it, and ``compile(precision=)`` overrides it in turn.

    Called in another graph's body, on its handles and per-call values, a
    graph's body traces into that graph: its steps are the caller's, its
    weights and states are named by the path the caller holds it at, and
    the caller's one compile covers it.
    """

    profile: Profile | Path | None = None
    precision: Precision | None = None

    def body(self, *inputs: Any, **values: Any) -> Any:
        raise NotImplementedError(f"{type(self).__name__} defines no body()")

    def signature(self) -> inspect.Signature:
        """The inputs and per-call values ``body`` takes, ``self`` left out:
        ``body``'s own parameters, unless a subclass names them here.
        """
        signature = inspect.signature(type(self).body, eval_str=True)
        return signature.replace(parameters=list(signature.parameters.values())[1:])

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # A body of its own is checked as its class is made, unless the
        # class names its parameters in signature() instead.
        if "body" in cls.__dict__ and cls.signature is Graph.signature:
            signature = inspect.signature(cls.body, eval_str=True)
            parameters = list(signature.parameters.values())[1:]
            _Parameters.of(cls.__name__, signature.replace(parameters=parameters))

    def __repr__(self) -> str:
        traced = dict.fromkeys([*self._versions, *self._references])
        shapes = "; ".join(
            ", ".join(f"{n}={shape} {dtype}" for n, shape, dtype in signature)
            for signature in traced
        )
        return f"{self.name}({shapes})"

    @functools.cached_property
    def _parameters(self) -> _Parameters:
        return _Parameters.of(type(self).__name__, self.signature())

    @property
    def name(self) -> str:
        return type(self).__name__

    @functools.cached_property
    def _versions(self) -> dict[Signature, CompiledGraph]:
        return {}

    @functools.cached_property
    def _references(self) -> dict[Signature, TracedGraph]:
        return {}

    @functools.cached_property
    def _arena(self) -> ScratchArena:
        return ScratchArena(ArenaPlan(ALIGNMENT))

    @functools.cached_property
    def _carry(self) -> State | None:
        if not self._parameters.carried:
            return None
        return State((2, len(self._parameters.carried)), np.int32, CARRY)

    @property
    def versions(self) -> dict[Signature, CompiledGraph]:
        return dict(self._versions)

    @property
    def arena(self) -> ScratchArena:
        return self._arena

    @staticmethod
    def _signature(inputs: Mapping[str, tuple[tuple[int, ...], Any]]) -> Signature:
        return tuple(
            (name, shape, bfp.dtype_name(dtype))
            for name, (shape, dtype) in inputs.items()
        )

    def held(self) -> dict[int, tuple[str, Any]]:
        """Each tensor and state the instance holds, by identity, with its
        path name.

        Raises:
            TypeError: A ``param`` was never loaded.
        """
        held: dict[int, tuple[str, Any]] = {}
        for path, x, _, _ in _leaves(self):
            if isinstance(x, _Param):
                raise TypeError(f"{self.name}: {path} was never loaded")
            held.setdefault(id(x), (path, x))
        return held

    def load_state_dict(self, tree, *, path: str = "") -> None:
        """Bind each ``param`` of this graph and of what it holds to the
        tensor at its dotted path in ``tree`` (a ``Checkpoint.tree()``, or
        tensors by dotted path) under ``path``, this graph's own prefix
        (``"model."``), cast to the param's dtype as torch's ``copy_``
        casts it, a value past the dtype's range becoming inf. A param held
        at several paths is tied: its first path, in attribute order, binds
        every holder, and a tensor at another is ignored; so is any tensor
        under a graph or container held again at a second path. Each graph
        it holds binds through its own ``load_state_dict``, so a subclass derives a
        tensor after ``super().load_state_dict()``.

        Raises:
            ValueError: ``path`` does not end in a dot; the graph is
                already loaded; or a param's tensor is missing, of another
                shape or of another kind (float for int), or ``tree`` holds
                a tensor under ``path`` that no param declares, one error
                naming every such path.
            TypeError: A param is in a tuple or a frozen dataclass, which
                cannot be rebound.
        """
        if path and not path.endswith("."):
            raise ValueError(
                f"{self.name}: load_state_dict's path {path!r} must end in a dot"
            )
        if self.__dict__.get("_bound"):
            raise ValueError(f"{self.name}: already loaded")
        tensors = {n: t for n, t, _, _ in _leaves(tree) if n.startswith(path)}
        tied: dict[int, list[str]] = {}
        params: dict[str, _Param] = {}
        shared: list[str] = []
        for n, p, parent, _ in _leaves(self, shared=shared):
            if not isinstance(p, _Param):
                continue
            if isinstance(parent, tuple) or getattr(
                getattr(parent, "__dataclass_params__", None), "frozen", False
            ):
                raise TypeError(
                    f"{self.name}: {path}{n} is in a tuple or a frozen "
                    f"dataclass, which load_state_dict cannot rebind; hold it in a list"
                )
            tied.setdefault(id(p), []).append(path + n)
            params.setdefault(tied[id(p)][0], p)
        held = {n for paths in tied.values() for n in paths}
        missing = sorted(params.keys() - tensors.keys())
        extra = sorted(
            n
            for n in tensors.keys() - held
            if not any(n.startswith(f"{path}{s}.") for s in shared)
        )
        given = [(n, p, tensors[n]) for n, p in params.items() if n in tensors]
        shapes = [
            f"{n} {tuple(t.shape)}, not {p.shape}"
            for n, p, t in given
            if tuple(t.shape) != p.shape
        ]
        kinds = [
            f"{n} {t.dtype}, not {p.dtype}"
            for n, p, t in given
            if _kind(t.dtype) != _kind(p.dtype)
        ]
        if missing or extra or shapes or kinds:
            found = {
                "missing": missing,
                "extra": extra,
                "wrong shape": shapes,
                "wrong kind": kinds,
            }
            raise ValueError(
                f"{self.name}: cannot load: "
                + "; ".join(f"{k} {', '.join(v)}" for k, v in found.items() if v)
            )
        for first, *others in tied.values():
            tensors[first] = np.asarray(tensors[first]).astype(
                params[first].dtype, copy=False
            )
            tensors.update(dict.fromkeys(others, tensors[first]))
        for n, x, parent, key in _leaves(self, graphs=False):
            if isinstance(x, Graph):
                if not x.__dict__.get("_bound"):
                    x.load_state_dict(tensors, path=f"{path}{n}.")
            elif not isinstance(x, _Param):
                continue
            elif isinstance(parent, (list, dict)):
                parent[key] = tensors[path + n]
            else:
                setattr(parent, key, tensors[path + n])
        self._bound = True

    def draw(self, seed: int) -> None:
        """Bind each ``param`` drawn at ``seed`` in the order the graph
        holds them (``filled``).
        """
        self.load_state_dict(filled("random", self._shapes(), seed))

    def unread(self) -> None:
        """Bind each ``param`` allocated and never written (``filled``)."""
        self.load_state_dict(filled("unread", self._shapes()))

    def _shapes(self) -> dict[str, tuple[tuple[int, ...], Any]]:
        """Each param's shape and dtype at its first path."""
        shapes: dict[str, tuple[tuple[int, ...], Any]] = {}
        seen: set[int] = set()
        for n, p, _, _ in _leaves(self):
            if isinstance(p, _Param) and id(p) not in seen:
                seen.add(id(p))
                shapes[n] = (p.shape, p.dtype)
        return shapes

    def trace(self, *, precision: Precision | None = None, **shapes) -> TracedGraph:
        """Run ``body`` on handles of the given shapes; an optional input
        given none is None. ``precision`` overrides ``self.precision``.
        """
        shapes = {k: v for k, v in shapes.items() if v is not None}
        params = self._parameters
        missing = [
            p for p in params.inputs if p not in shapes and p not in params.optional
        ]
        unknown = [k for k in shapes if k not in params.inputs]
        if missing or unknown:
            raise TypeError(
                f"{self.name}: shapes for {missing} missing"
                + (f"; {unknown} are not inputs" if unknown else "")
            )
        inputs: list[Handle] = []
        args: list[Handle | None] = []
        for name in params.inputs:
            if name not in shapes:
                args.append(None)
                continue
            shape, dtype = _shape_and_dtype(shapes[name])
            inputs.append(Handle(shape, dtype, name, "input"))
            args.append(inputs[-1])
        values = [PerCall(n, kind, dtype) for n, (kind, dtype) in params.values.items()]
        with Tracer(
            self.name,
            self._profile(),
            self.held(),
            params.inputs,
            self.precision if precision is None else precision,
        ) as tracer:
            result = self.body(*args, **{v.name: v for v in values})
        items, carry = self._split_carry(result)
        outputs = self._outputs(items, tracer)
        return tracer.finish(
            inputs, outputs, values, self._traced_carry(carry, values, tracer)
        )

    def _split_carry(self, result) -> tuple[list, Carry | None]:
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
        carried = self._parameters.carried
        missing = [n for n in carried if n not in names]
        unknown = [n for n in names if n not in carried]
        if missing or unknown:
            raise TypeError(
                f"{self.name}: carries {names}, but its Carried values are "
                f"{carried}"
                + (f"; return iron.carry({missing[0]}=...)" if missing else "")
            )
        return items, carry

    def _traced_carry(
        self, carry: Carry | None, values: list[PerCall], tracer: Tracer
    ) -> dict[str, Handle | Affine]:
        """Each next value: an expression of the values, or one element the graph computed."""
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
                _rename(tracer, nxt, tracer.fresh(f"carry_{name}"))
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
                _rename(
                    tracer, item, tracer.fresh(f"out{i}" if len(items) > 1 else "out")
                )
            outputs.append(item)
        return outputs

    def compile(
        self,
        *,
        dev=None,
        precision: Precision | str | None = None,
        full_elf: bool | None = None,
        check: bool = False,
        feeds: CompiledGraph | None = None,
        coresident: AdjacentPacking | None = None,
        **shapes,
    ) -> CompiledGraph:
        """Compile the version for the given input shapes and return it.

        Compile every version before the first call where you can: one placed
        after the arena's buffer exists grows it, which copies it once.

        Args:
            dev: The device to compile for, bound for this compile alone;
                else the current one.
            precision: The most any step may round, bound for this
                compile alone; else ``self.precision``.
            full_elf: One full ELF, else an xclbin per step; ``None``
                derives it (``iron.common.image.packaging``).
            check: Run each step on its own dispatch and hold its outputs to
                its reference on the same inputs, by its ``tolerance()``;
                a step outside it raises, naming the step.
            feeds: The version a full ELF's Emit starts; by default itself
                when it takes no tensor.
            coresident: Packs designs into shared configurations.
            **shapes: Each input's shape, or ``(shape, dtype)``.
        """
        with (
            aie_utils.set_current_device(dev)
            if dev is not None
            else contextlib.nullcontext()
        ):
            traced = self.trace(
                precision=None if precision is None else Precision(precision), **shapes
            )
            chosen = plan(require_device(), traced, full_elf, check)
            logger.info("%s", chosen.report(self.name))
            signature = self._signature(
                {h.name: (h.shape, h.dtype) for h in traced.inputs}
            )
            emit, sized = self._emit(traced, chosen, feeds)
            version = CompiledGraph(
                traced,
                chosen,
                check=check,
                arena=self._arena,
                emit=emit,
                coresident=coresident,
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

    def _emit(
        self, traced: TracedGraph, chosen: Plan, feeds: CompiledGraph | None
    ) -> tuple[EmitSite | None, list[Word] | None]:
        """The Emit step a full ELF with carried values ends in, appended to
        ``traced``, sized for ``feeds``' words or, feeding itself, for its
        own; and those own words, or None.

        Raises:
            ValueError: ``feeds`` is not a full-ELF version of this graph,
                or this version does not loop.
        """
        loops = feeds is not None or not traced.inputs
        if not (chosen.full_elf and traced.carry and loops):
            if feeds is not None:
                raise ValueError(
                    f"{self.name}: only a full-ELF version with carried values "
                    f"feeds another"
                )
            return None, None
        sized = None
        if feeds is None:
            sized = _words(traced, share=True, extents=False)[0]
            slots = len(sized)
        elif feeds.emit is None or not any(feeds is v for v in self._versions.values()):
            raise ValueError(
                f"{self.name}: feeds= takes a full-ELF version of this graph, "
                f"got {feeds!r}"
            )
        else:
            slots = len(feeds.parameters)
        assert self._carry is not None
        emit = attach_emit(traced, self._parameters.carried, self._carry, slots)
        return emit, sized

    def _given(self, tensors) -> dict[str, Any]:
        params = self._parameters
        if len(tensors) > len(params.inputs):
            raise TypeError(
                f"{self.name} takes {len(params.inputs)} input(s), got {len(tensors)}"
            )
        given = {n: t for n, t in zip(params.inputs, tensors) if t is not None}
        missing = [
            p for p in params.inputs if p not in given and p not in params.optional
        ]
        if missing:
            raise TypeError(f"{self.name}: inputs {missing} missing")
        return given

    def __call__(self, *tensors, **values) -> Any:
        given = self._given(tensors)
        _check_values(self.name, self._parameters.values, values)
        if graph_tracer.get() is not None:
            if self._parameters.carried:
                raise TypeError(
                    f"{self.name}: a graph called in another's body carries "
                    f"no values of its own; its caller carries them"
                )
            return self.inline(
                self.body, *(given.get(n) for n in self._parameters.inputs), **values
            )
        shapes = {
            name: (tuple(int(n) for n in t.shape), np.dtype(t.dtype).type)
            for name, t in given.items()
        }
        version = self._versions.get(self._signature(shapes))
        if version is None:
            logger.info("%s: compiling for %s", self.name, shapes)
            version = self.compile(**shapes)
        return version(*given.values(), **values)

    def inline(self, method: Callable, /, *args, **kwargs) -> Any:
        """``method``, one of this graph's, traced into the body of the graph
        being traced, under this graph's profile: its steps are that graph's.
        That graph names the values ``method`` takes, carried ones included.

        Raises:
            TypeError: No graph's body is being traced.
        """
        tracer = graph_tracer.get()
        if tracer is None:
            raise TypeError(f"{self.name}: inline() traces into a graph's body")
        own = self._profile()
        if own is None:
            return method(*args, **kwargs)
        previous, tracer.profile = tracer.profile, own
        try:
            return method(*args, **kwargs)
        finally:
            tracer.profile = previous

    def reference(self, *tensors, **values) -> Any:
        """The graph traced for these tensors' shapes, each step run on the
        host through its operator's ``reference()`` (``TracedGraph.reference``):
        what a call on the device returns, each output cut to its bounds,
        at any shape the operators take, one no device fits too.

        Raises:
            TypeError: An input is missing, or a per-call value is missing or
                unknown, as a call on the device refuses them; or the body
                does not trace.
            IndexError: The values index or bound a view outside it, as a
                call on the device refuses them.
        """
        given = {n: np.asarray(t) for n, t in self._given(tensors).items()}
        _check_values(self.name, self._parameters.values, values)
        shapes = {n: (t.shape, np.dtype(t.dtype).type) for n, t in given.items()}
        signature = self._signature(shapes)
        traced = self._references.get(signature)
        if traced is None:
            token = device_fit.set(False)
            try:
                traced = self._references[signature] = self.trace(**shapes)
            finally:
                device_fit.reset(token)
        outputs, carry = traced.reference(given, values)
        return _results(outputs, Carry(**carry) if traced.carry else None)

    def _profile(self) -> Profile | None:
        profile = self.profile
        if isinstance(profile, (str, Path)):
            dev = require_device()
            path = Path(profile) / f"{dev.name}.json"
            if not path.exists():
                raise ValueError(f"{self.name}: no profile {path}")
            profile = Profile.load(path)
        return profile


class CompiledGraph:
    """A traced graph built into an image, ready to call.

    A call gives the per-call values this version reads (``TracedGraph.reads``)
    and may give the graph's others, which another version reads; they go
    unused.
    """

    def __init__(
        self,
        traced: TracedGraph,
        plan: Plan,
        check: bool = False,
        arena: ScratchArena | None = None,
        emit: EmitSite | None = None,
        coresident: AdjacentPacking | list[list[Operator]] | None = None,
    ):
        self.traced = traced
        self.plan = plan
        self.arena = arena
        self.emit = emit
        self.words, self.shared = _words(
            traced, share=plan.full_elf, extents=not plan.full_elf
        )
        placement: dict[str, Any] = (
            {} if arena is None else dict(arena=arena.plan, residents=traced.residents)
        )
        if coresident:
            placement["coresident"] = coresident
        self.sequence = OperatorSequence(
            traced,
            full_elf=plan.full_elf,
            check=check,
            shared_words=self.shared,
            commands=plan.commands,
            **placement,
        ).compile()
        self.image = self.sequence.image
        self.artifacts = self.sequence.artifacts
        if plan.full_elf:
            # An extent read only through its derivations has no word.
            self.words = [
                w for w in self.words if w.symbol in self.artifacts.parameters
            ]
        self._callable = None
        self._addressed: dict[str, tuple[Any, int]] = {}
        # Shared with the arena when there is one: its weights are every image's.
        self._loaded: set = set() if arena is None else arena.loaded

    @property
    def callable(self):
        """The loaded image, made on first use so a host without an NPU can compile."""
        if self._callable is None:
            self._callable = self.sequence.get_callable(self.arena)
        return self._callable

    @property
    def parameters(self) -> list[Parameter]:
        return self.artifacts.parameter_table

    @property
    def is_loaded(self) -> bool:
        return self._callable is not None

    def __repr__(self) -> str:
        inputs = ", ".join(
            f"{h.name}={h.shape} {bfp.dtype_name(h.dtype)}" for h in self.traced.inputs
        )
        report = self.plan.report(f"{self.traced.name}({inputs})")
        if self.artifacts.directory is None:
            return report
        return f"{report}\n  built in {self.artifacts.directory}"

    def _ref(self, x) -> BufferRef:
        if isinstance(x, State):
            return BufferRef(self.traced.states[id(x)][1].name)
        if isinstance(x, Handle):
            return x.ref()
        key = id(x.array) if isinstance(x, Weight) else id(x)
        if key in self.traced.weights:
            return BufferRef(self.traced.weights[key][1].name)
        raise KeyError(f"{x!r} is not a state, weight or handle of this graph")

    def _storage(self, x):
        ref = self._ref(x)
        if ref.nbytes is not None:
            return self.callable.get_buffer(ref)
        return self.callable.get_storage(ref.root)

    def write(self, x, tensor) -> None:
        buf = self._storage(x)
        _store(buf.numpy_view()[: int(np.prod(x.shape))], tensor)
        buf.to("npu")

    def read(self, x):
        """``x``'s buffer as the device left it: a view of its host memory."""
        buf = self._storage(x)
        return buf.numpy()[: int(np.prod(x.shape))].reshape(tuple(x.shape))

    def push(self, x) -> None:
        """Send to the device what the host wrote into ``read(x)``'s view."""
        buf = self._storage(x)
        buf.numpy_view()  # marks the host copy the newer, so to() sends it
        buf.to("npu")

    def _copy_in(
        self,
        name,
        tensor,
        release: Callable[[np.ndarray], None] | None = None,
        piece_bytes: int = UPLOAD_PIECE,
    ) -> None:
        view = self.callable.get_storage(name).numpy_view()[: np.size(tensor)]
        _store(view, tensor, release, piece_bytes)

    def upload(
        self,
        release: Callable[[np.ndarray], None] | None = None,
        piece_bytes: int = UPLOAD_PIECE,
    ) -> None:
        """Copy every closed-over weight into its buffer, once per storage."""
        for key, (tensor, handle) in self.traced.weights.items():
            if key not in self._loaded:
                self._copy_in(handle.name, tensor, release, piece_bytes)
                self._loaded.add(key)

    def load(
        self,
        release: Callable[[np.ndarray], None] | None = None,
        piece_bytes: int = UPLOAD_PIECE,
    ) -> CompiledGraph:
        """Load the image and upload its weights now rather than on first call."""
        self.callable
        self.upload(release, piece_bytes)
        return self

    def __call__(self, *tensors, **values) -> Any:
        self._stage(tensors, values)
        if self.plan.commands:
            self.callable(idle=self.plan.idle(self.traced.steps, values))
        else:
            self.callable()
        outputs = [self.callable.get_buffer(h.ref()) for h in self.traced.returned]
        if not self.traced.carry:
            return _results(outputs, None)
        return _results(outputs, self._next_values(values))

    def start(self, run: FullELFRun, /, *tensors, **values) -> None:
        """Start a call of this full ELF on ``run`` without waiting for it."""
        self._stage(tensors, values, run)
        self.callable.start(run, idle=self.plan.idle(self.traced.steps, values))

    def emit_to(self, target: CompiledGraph) -> None:
        """Program this version's Emit to start a call of ``target``."""
        if self.emit is None:
            raise ValueError(f"{self.traced.name}: this version has no Emit step")
        if target.traced.addresses:
            tables = sorted(
                {buffer for buffer, _, _ in target.traced.addresses.values()}
            )
            raise ValueError(
                f"{target.traced.name}: an Emit cannot start it: its gather by ids "
                f"the device made reads the address of {tables}, which the host "
                f"writes each call and no carried value holds"
            )
        program = compose(self.emit, self.traced.carry, target.words, target.parameters)
        self.write(self.emit.program, program)

    def _stage(self, tensors, values, run: FullELFRun | None = None) -> None:
        if len(tensors) != len(self.traced.inputs):
            raise TypeError(
                f"{self.traced.name} takes {len(self.traced.inputs)} input(s), "
                f"got {len(tensors)}"
            )
        reads = self.traced.reads
        _check_values(
            self.traced.name, reads, {n: x for n, x in values.items() if n in reads}
        )
        unknown = set(values) - {v.name for v in self.traced.values}
        if unknown:
            raise TypeError(
                f"{self.traced.name}: per-call values {sorted(unknown)} unknown"
            )
        self.traced.check_limits(values)
        for handle, tensor in zip(self.traced.inputs, tensors):
            if tuple(tensor.shape) != handle.shape:
                raise ValueError(
                    f"{self.traced.name}: input {handle.name} was compiled for "
                    f"{handle.shape}, got {tuple(tensor.shape)}; a new shape is a "
                    f"new compile"
                )
            if not np.can_cast(tensor.dtype, handle.dtype, "same_kind"):
                dtype = np.dtype(handle.dtype)
                module = dtype.type.__module__.replace("numpy", "np")
                raise TypeError(
                    f"{self.traced.name}: input {handle.name} is {dtype}, got "
                    f"{tensor.dtype}; pass {handle.name}.astype({module}.{dtype})"
                )
        self.upload()
        for handle, tensor in zip(self.traced.inputs, tensors):
            held = self.traced.encoders.get(handle.name)
            if held is not None:
                tensor = np.concatenate(
                    [e(tensor, self._address(e.buffer), values) for e in held]
                )
            self._copy_in(handle.name, tensor)
        self._write_values(values, run)

    def _address(self, name: str) -> int:
        """The device address of buffer ``name``, put until the arena holding
        it grows (a new view).
        """
        view = self.callable.get_storage(name)
        if name not in self._addressed or self._addressed[name][0] is not view:
            storage = view.storage
            root = storage.binding_handle(0, storage.nbytes)
            self._addressed[name] = (view, root.address() + view.storage_offset)
        return self._addressed[name][1]

    def _next_values(self, values: Mapping[str, int]) -> Carry:
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
                buf = self.callable.get_buffer(expression.ref())
                nxt[name] = int(buf.numpy().reshape(-1)[0])
        return Carry(**nxt)

    def _write_values(self, values, run: FullELFRun | None = None) -> None:
        if self.emit is not None:
            n = len(self.emit.carried)
            head = self._storage(self.emit.carry).numpy_view()
            head[:n] = [values[name] for name in self.emit.carried]
        if not self.words:
            return
        values = dict(values)
        for name, (buffer, address_words, word) in self.traced.addresses.items():
            values[name] = address_words(self._address(buffer))[word]
        words = {w.symbol: np.dtype(w.dtype).type(w(values)) for w in self.words}
        (self.callable if run is None else run).write_values(words)


def _check_values(name: str, declared, values: Mapping[str, Any]) -> None:
    missing, unknown = set(declared) - set(values), set(values) - set(declared)
    if missing or unknown:
        raise TypeError(
            f"{name}: per-call values {sorted(missing)} missing"
            + (f"; {sorted(unknown)} unknown" if unknown else "")
        )


def _rename(tracer: Tracer, handle: Handle, name: str) -> None:
    """Make an intermediate, and every view of its buffer, a graph output named ``name``."""
    old = handle.name
    for step in tracer.steps:
        for h in step.slots + step.inputs + step.outputs:
            root = h.root  # one buffer may have several roots, one per reshape
            if root.role == "intermediate" and root.name == old:
                root.name, root.role = name, "output"
    handle.name, handle.role = name, "output"


def _results(outputs: list, carry: Carry | None):
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


@dataclasses.dataclass(frozen=True)
class Word:
    """A scratchpad word a call writes; words with one ``linear`` form, or one
    clamped ``form``, share a word.
    """

    symbol: str
    dtype: Any
    compute: Callable[[Mapping[str, int]], Any]
    linear: Linear | None
    form: Affine | None = None

    def __call__(self, values: Mapping[str, int]) -> Any:
        return self.compute(values)


def _derived_form(op, name: str, counts: Mapping[str, Affine]) -> Affine | None:
    """The Emit form of ``op``'s derived value ``name``, or ``None`` where no form expresses it."""
    try:
        got = op.derived_at(name, **counts)
    except TypeError:
        return None
    if isinstance(got, Affine):
        return got
    if isinstance(got, (int, np.integer)) and counts:  # the same every call
        return Affine(next(iter(counts.values())).value, 0, int(got))
    return None


def _words(
    traced: TracedGraph, *, share: bool = False, extents: bool = True
) -> tuple[list[Word], dict[str, str]]:
    """The scratchpad words a call writes, and with ``share`` the symbols
    sharing one: a full ELF has 32 words for its whole image.
    """
    dev = aie_utils.get_current_device()
    words: list[Word] = []
    for b in traced.bindings:
        if not extents and isinstance(b.member, Extent):
            continue
        e = b.expression
        linear = None
        if not (e.down or e.clamped or e.mod is not None):
            linear = Linear(
                e.value.name,
                Fraction(e.scale),
                Fraction(e.bias),
                np.dtype(b.member.dtype).name,
            )
        words.append(Word(b.symbol, e.dtype, lambda v, e=e: e.evaluate(v), linear, e))
    seen: set[int] = set()
    derived: set[str] = set()
    for b in traced.bindings:
        if id(b.op) in seen or not isinstance(b.member, Extent):
            continue
        seen.add(id(b.op))
        op = b.op.resolved(dev)
        counts = {
            e.member.name: e.expression
            for e in traced.bindings
            if e.op is b.op and isinstance(e.member, Extent)
        }

        def at(v, counts=counts):
            return {name: count.evaluate(v) for name, count in counts.items()}

        for name in sorted(op._per_call_derived() - op.bound_values.keys()):
            word = op.value(name)
            symbol = word.symbol
            if symbol in derived:
                continue  # another instance of the design, bound alike
            derived.add(symbol)
            linear = None
            spec = word
            if isinstance(spec, ExtentWord) and spec.extent.name in counts:
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
                    _derived_form(op, name, counts),
                )
            )

    shared = _shared(words) if share else {}
    out: list[Word] = []
    written: set[str] = set()
    for w in words:
        symbol = shared.get(w.symbol, w.symbol)
        if symbol not in written:
            written.add(symbol)
            out.append(dataclasses.replace(w, symbol=symbol))
    return out, shared


def _shared(words: list[Word]) -> dict[str, str]:
    """The symbol each word shares with the words of its one form: a
    ``Linear``, or a clamped or wrapped expression's name.
    """
    shared: dict[str, str] = {}
    forms: dict[str, set[Linear | str | None]] = {}
    for w in words:
        found, e = w.linear, w.form
        if found is None and e is not None and (e.clamped or e.mod is not None):
            # A clamped or wrapped expression has no Linear form; its name spells it whole.
            found = f"{e.name}_{np.dtype(w.dtype).name}"
        elif found is None and e is not None and e.mul in (1, -1):
            # ((s v + b) >> k) * m + a as a Linear, which rounds up: a
            # floor is the ceiling of (s v + b - 2^k + 1) / 2^k, and
            # -floor(x) is ceil(-x).
            d = 1 << e.down
            bias = e.bias * e.mul - (d - 1 if e.mul == 1 else 0)
            found = Linear(
                e.value.name,
                Fraction(e.scale * e.mul, d),
                Fraction(bias, d) + e.add,
                np.dtype(w.dtype).name,
            )
        forms.setdefault(w.symbol, set()).add(found)
    groups: dict[Linear | str, list[str]] = {}
    for symbol, found in forms.items():
        if len(found) == 1 and None not in found:
            groups.setdefault(next(iter(found)), []).append(symbol)

    def spell(r: Fraction) -> str:
        # An identifier's: m for minus, d for over.
        den = f"d{r.denominator}" if r.denominator > 1 else ""
        return f"{'m' if r < 0 else ''}{abs(r.numerator)}{den}"

    for form, symbols in groups.items():
        if len(symbols) > 1 and isinstance(form, str):
            shared.update(dict.fromkeys(symbols, f"graph_{form}"))
        elif len(symbols) > 1:
            name = f"graph_{form.value}_x{spell(form.ratio)}"
            if form.offset:
                name += f"{'p' if form.offset > 0 else 'm'}{spell(abs(form.offset))}"
            shared.update(dict.fromkeys(symbols, f"{name}_{form.dtype}"))
    return shared
