# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tracing a graph: the handles it threads and the steps it records."""

from __future__ import annotations

import dataclasses
import itertools
import math
from collections.abc import Callable, Hashable, Iterable, Mapping
from typing import TYPE_CHECKING

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.utils import bfp

from .. import declare
from ..declare import In, InOut, Operand, Operator, Out
from ..declare.value import Extent
from ..declare.operator import graph_tracer
from ..declare.profile import Profile
from ..image.packaging import Kind
from ..image.step import BufferRef, SequenceStep
from .handle import (
    Affine,
    Handle,
    PerCall,
    State,
    Weight,
    _HostView,
    _rescale_bounds,
    is_operand,
)
from .visualize import Dataflow

if TYPE_CHECKING:
    from .tuner import Prices


@dataclasses.dataclass
class TracedStep:
    op: Operator
    slots: list  # one handle per declared buffer
    inputs: list
    outputs: list

    def refs(self) -> tuple[BufferRef, ...]:
        """Where each declared buffer of the step is."""
        return tuple(h.ref() for h in self.slots)


@dataclasses.dataclass(frozen=True)
class Encoder:
    """How the host turns an input into the words the device reads, from
    ``buffer``'s device address: ``encode(input, address, valid)``, with
    ``valid`` the call's ``bound`` on the input's rows, or None.
    """

    buffer: str
    encode: Callable[[np.ndarray, int, int | None], np.ndarray]
    bound: Affine | None = None

    def __call__(
        self, tensor: np.ndarray, address: int, values: Mapping[str, int]
    ) -> np.ndarray:
        valid = None if self.bound is None else self.bound.evaluate(values)
        return self.encode(tensor, address, valid)


@dataclasses.dataclass(frozen=True)
class Binding:
    """A graph value bound to one operator's value member, written per call
    as ``expression``.
    """

    op: Operator
    member: declare.Value
    expression: Affine

    @property
    def symbol(self) -> str:
        return self.member.symbol


@dataclasses.dataclass(frozen=True)
class Limit:
    """A per-call ``expression`` a view of ``view`` holds in ``[lo, hi)``."""

    expression: Affine
    lo: int
    hi: int
    view: str


def _unbounded(h: Handle) -> Handle:
    if not h.bounds:
        return h
    return Handle(
        h.shape, h.dtype, h.name, h.role, h.parent, h.start, h.tap, h.index_by
    )


def _take_views(cls, operands, kwargs, values):
    """Hand each view operand's pattern to the operator (``cls.accept_views``)
    and stand its parent in.

    A bound on one view holds the others: each side moves the same rows. A
    side not given (a fresh output) is the bounded view's shape, bounded
    alike; a given one must be that shape, and is bounded on the same axis.
    """
    given = operands[: len(cls.accept_views)]
    held = next((h for h in given if h.bounds), None)
    if held is not None and len(held.bounds) == 1:
        ((axis, count),) = held.bounds.items()
        for i, (param, _) in enumerate(cls.accept_views):
            if i < len(given) and given[i].bounds:
                continue
            if i >= len(given):
                kwargs.setdefault(param, TensorAccessPattern.full(held.shape))
            elif given[i].shape != held.shape:
                raise ValueError(
                    f"{given[i]!r} is every row of a {given[i].shape} view while "
                    f"{held!r} moves {count} on axis {axis}; bound it alike"
                )
            kwargs.setdefault(f"{param}_bound", axis)
            values[f"{param}_valid"] = count
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
    # buffer's device address (a gather's ids).
    encoders: dict[str, Encoder] = dataclasses.field(default_factory=dict)
    # A per-call value the graph fills in rather than the caller, from a
    # buffer's device address (a gather by ids the device made):
    # value -> (buffer, address -> words by name, its word's name).
    addresses: dict[str, tuple[str, Callable[[int], dict], str]] = dataclasses.field(
        default_factory=dict
    )
    # A weight whose bytes are not known until its own table buffer is
    # placed (GatherWords.static_base): handle name -> (buffer, address ->
    # words by name). Filled in once, at upload, not a per-call value.
    static_addresses: dict[str, tuple[str, Callable[[int], dict]]] = dataclasses.field(
        default_factory=dict
    )
    limits: list[Limit] = dataclasses.field(default_factory=list)

    @classmethod
    def of_steps(
        cls,
        name: str,
        steps: Iterable[SequenceStep],
        inputs: Iterable[str],
        outputs: Iterable[str],
        pinned: Mapping[str, int] | None = None,
        feedback: Iterable[str] = (),
    ) -> TracedGraph:
        """A graph of ``steps`` over buffers known by name alone, as bytes.

        Args:
            name: The graph's name.
            steps: Each step's operator and where its buffers are.
            inputs: The buffers the host writes.
            outputs: The buffers the host reads.
            pinned: The bytes of each buffer a step names only in part, and
                of any it should hold at a size of its own.
            feedback: The buffers of the feedback argument.
        """
        pinned = dict(pinned or {})
        roots: dict[str, Handle] = {}
        traced = []
        for step in steps:
            slots = []
            for ref in step.buffers:
                root = roots.setdefault(
                    ref.root,
                    Handle(
                        (pinned.get(ref.root, 0),), np.uint8, ref.root, "intermediate"
                    ),
                )
                if ref.nbytes is None:
                    slots.append(root)
                    continue
                slots.append(
                    Handle((ref.nbytes,), np.uint8, ref.root, "slice", root, ref.start)
                )
            declared = list(zip(slots, step.op.buffers))
            traced.append(
                TracedStep(
                    step.op,
                    slots,
                    [h for h, b in declared if b.fills],
                    [h for h, b in declared if b.drains],
                )
            )
        return cls(
            name,
            traced,
            [Handle((), np.uint8, n, "input") for n in inputs],
            [Handle((), np.uint8, n, "output") for n in outputs],
            [],
            pinned,
            {},
            {},
            [],
            feedback=list(feedback),
        )

    @classmethod
    def of_step(cls, op: Operator) -> TracedGraph:
        """``op`` alone, over its own buffers by their declared names: the
        host writes what it reads and reads what it only writes.
        """
        return cls.of_steps(
            op.name,
            [SequenceStep(op, tuple(BufferRef(b.name) for b in op.buffers))],
            [b.name for b in op.buffers if b.fills],
            [b.name for b in op.buffers if b.drains and not b.fills],
        )

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

    def picture(
        self,
        title: str = "",
        layers: set[int] | None = None,
        weights: bool = True,
        prices: Prices | None = None,
    ) -> Dataflow:
        """This graph drawn (``visualize.Dataflow``): its ``dot()``, ``svg()``
        and ``html()``.

        Args:
            title: The caption; the graph's name if empty.
            layers: The layers drawn, or None for every step.
            weights: Draw each weight as its own node.
            prices: Show the time these prices give each design.
        """
        return Dataflow(self, title, layers, weights, prices=prices)

    def dot(self) -> str:
        """This graph drawn as Graphviz text (``picture``)."""
        return self.picture().dot()

    def html(self) -> str:
        """This graph drawn as one self-contained page (``picture``)."""
        return self.picture().html()

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
        profile: Profile | None = None,
        held: Mapping[int, tuple[str, object]] | None = None,
        inputs: Iterable[str] = (),
    ) -> None:
        self.name = name
        self.profile = profile
        held = held or {}
        self._held_arrays = [
            x.array if isinstance(x, Weight) else x
            for _, x in held.values()
            if isinstance(x, (Weight, np.ndarray))
        ]
        self.steps: list[TracedStep] = []
        self.weights: dict[int, tuple[object, Handle]] = {}
        self.states: dict[int, tuple[State, Handle]] = {}
        self.bindings: list[Binding] = []
        self.limits: list[Limit] = []
        self._bound: dict[int, dict] = {}
        self.encoders: dict[str, Encoder] = {}
        self.addresses: dict[str, tuple[str, Callable, str]] = {}
        # A weight whose bytes are not known until its own table buffer is
        # placed (GatherWords.static_base): handle name -> (table name,
        # address_words). Filled in once, at upload, not a per-call value.
        self.static_addresses: dict[str, tuple[str, Callable]] = {}
        self._counter = itertools.count()
        self._names: dict[int, str] = {}
        for key, (path, x) in held.items():
            self._names.setdefault(key, path)
            if isinstance(x, Weight):
                self._names.setdefault(id(x.array), path)
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
            array = x.array if isinstance(x, Weight) else x
            key = id(array)
            if key not in self.weights:
                name = self._names.get(id(x)) or self._names.get(key)
                if name is None and isinstance(array, np.ndarray):
                    view = self._held_view(array)
                    if view is not None:
                        return view
                name = name or self.fresh(f"w{len(self.weights)}")
                self.weights[key] = (
                    array,
                    Handle(array.shape, np.dtype(array.dtype).type, name, "weight"),
                )
            return self.weights[key][1]
        raise TypeError(f"{x!r} is not a graph handle, a state, or a tensor")

    def _held_view(self, x: np.ndarray) -> Handle | None:
        """``x``, a numpy view of a held array, as a view of its buffer, or None."""
        if not x.size or any(s < 0 for s in x.strides):
            return None
        address = x.__array_interface__["data"][0]
        for held in self._held_arrays:
            base = held.__array_interface__["data"][0]
            offset, misaligned = divmod(address - base, x.itemsize)
            if (
                held.dtype != x.dtype
                or not held.flags.c_contiguous
                or misaligned
                or not 0 <= offset < held.size
                or any(s % x.itemsize for s in x.strides)
            ):
                continue
            strides = [
                s // x.itemsize if n > 1 else 0 for s, n in zip(x.strides, x.shape)
            ]
            if offset + sum((n - 1) * s for n, s in zip(x.shape, strides)) >= held.size:
                continue
            if not offset and x.size == held.size and x.flags.c_contiguous:
                # All of the buffer, as a reshape: the buffer itself, which a gather reads.
                return self.operand(held).reshape(x.shape)
            tap = TensorAccessPattern(held.shape, offset, list(x.shape), strides)
            return self.operand(held).at(tap, x.shape)
        return None

    def overwrites(self, given) -> str | None:
        """What an output a call gives would write over that no call may:
        ``"weight"`` or ``"input"``, through any view of it, else None.
        """
        if isinstance(given, State):
            return None
        if not isinstance(given, Handle):
            return "weight"
        while given.parent is not None:
            given = given.parent
        return given.role if given.role in ("weight", "input") else None

    def check_outputs(self, cls, outputs) -> None:
        """Refuse an output a call gives that is a weight or an input.

        A positional operand past the inputs is an output, so a weight given
        where an optional input was meant would be written over.

        Raises:
            TypeError: An output is a weight or an input, or a view of one.
        """
        for given in outputs:
            kind = self.overwrites(given)
            if kind is None:
                continue
            keywords = [
                f"{m.name}="
                for m in cls.declaration.members
                if isinstance(m, Operand) and m.fills and m.when is not None
            ]
            hint = f"; an optional input is given by keyword ({', '.join(keywords)})"
            raise TypeError(
                f"{cls.__name__}: the output given, {list(given.shape)}, is a "
                f"graph {kind} or a view of one, which a call does not write over"
                f"{hint if keywords else ''}"
            )

    def call(self, target, args, kwargs):
        """Record ``target(*args, **kwargs)``: inputs, optionally followed by
        outputs; keywords are optional inputs, per-call value handles, or
        construction arguments when ``target`` is a class.
        """
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = cls.declaration.call_operands(args, kwargs)
        self.check_outputs(cls, outputs)
        names = list(inputs)
        operands = [self.operand(a) for a in [*inputs.values(), *outputs]]
        values = {
            k: kwargs.pop(k)
            for k in list(kwargs)
            if isinstance(kwargs[k], (PerCall, Affine))
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
        static_base = (
            extra.pop("static_base", False) if isinstance(extra, dict) else False
        )
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
        given = dict(
            rows=ids.shape[0],
            table_rows=table.shape[0],
            row=math.prod(table.shape[1:]),
            dtype=table.dtype,
            static_base=static_base,
        )
        gather = target.per_call_gather
        if self.profile is None:
            op = gather(**given)
        else:
            op = self.profile.make(gather, **given)
        bound = ids.bounds.get(0)
        if bound is not None:
            self._bind(op, "valid_rows", bound)
        if ids.role == "input":
            if ids.name in self.encoders:
                raise ValueError(f"the input {ids.name!r} gathers from one table once")
            control = Handle((op.words,), np.uint32, ids.name, "input")
            self.encoders[ids.name] = Encoder(table.name, op.control_words, bound)
        else:
            source = op.word_source()
            template = op.template[0]
            self._names[id(template)] = self.fresh(f"{table.name}_gather")
            control = self.operand(template)
            if source.static_base:
                base_handle = self.operand(np.zeros(2, dtype=np.int32))
                self.static_addresses[base_handle.name] = (
                    table.name,
                    source.address_words,
                )
                self._record(source, [ids, base_handle, control])
            else:
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
                    self._bind(source, member, PerCall(name, Kind.SCRATCHPAD, np.int32))
                self._record(source, [ids, control])
        out = self._record(op, [table, control])
        return out if out.shape == view.shape else out.reshape(view.shape)

    @staticmethod
    def _split_values(op_cls, kwargs) -> dict:
        names = {
            m.name for m in op_cls.declaration.members if isinstance(m, declare.Value)
        }
        return {k: kwargs.pop(k) for k in list(kwargs) if k in names}

    def _construct(self, cls, inputs, outputs, kwargs) -> Operator:
        inferred = cls.declaration.infer(
            {name: h.shape for name, h in inputs.items()},
            [h.shape for h in outputs],
            **kwargs,
        )
        given = {**kwargs, **inferred}
        if self.profile is not None:
            return self.profile.make(cls, **given)
        pinned = frozenset(
            name
            for name, value in given.items()
            if name in cls.declaration.tunables and value is not None
        )
        return cls(**given, pinned=pinned)

    def _output_bounds(self, op, buffer, rank: int) -> dict:
        bounds = {}
        for binding in self.bindings:
            if binding.op is not op or not isinstance(binding.member, Extent):
                continue
            axis = buffer.extent_axis(binding.member)
            if axis is not None:
                bounds[axis] = binding.expression
        return bounds

    def _bind(self, op, name, value) -> None:
        if not isinstance(value, (PerCall, Affine)):
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
            op.use_value(name, value)
            bound[name] = value
            member = next(v for v in op.values if v.name == name)
            self.bindings.append(Binding(op, member, value))

    def _record(self, op, operands, called=None):
        """Record ``op`` on ``operands``; ``called`` are the operands as the
        call gave them, a view where ``operands`` holds its buffer.
        """
        called = operands if called is None else called
        # A shape that Selects on an Auto() field is the device's: resolve()
        # gives it, unchecked, so a profile may still tune the op.
        unset = {n for n in type(op).declaration.autos if vars(op)[n] is None}
        shaped = op
        if any(unset & m.dims.names() for m in op._members_io()):
            shaped = op.resolve(op.dev)
        buffers = shaped.buffers
        ins = [b for b in buffers if b.fills]
        outs = [b for b in buffers if isinstance(b, Out)]
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
        for i, (h, b) in enumerate(zip(operands, ins + outs)):
            # Another rank matches on the count, for an output only a flat
            # one; the same rank must match the shape, or a transposed weight
            # would pass.
            shape = tuple(b.shape)
            wrong = (
                tuple(h.shape) != shape
                if len(h.shape) == len(shape)
                else h.elements != b.elements or (i >= len(ins) and len(shape) != 1)
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
                        for m in type(op).declaration.members
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
            if isinstance(b, In):
                slots.append(next(it))
            elif isinstance(b, InOut):
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
                        bounds = dict(called[like].bounds)
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
            static_addresses=self.static_addresses,
            limits=self.limits,
        )

    def limit(self, expression: Affine, lo: int, hi: int, view: Handle) -> None:
        """Record that a call's ``expression`` must lie in ``[lo, hi)`` for
        ``view``, which it indexes or bounds.
        """
        self.limits.append(Limit(expression, lo, hi, repr(view)))


class _ReferenceTracer(Tracer):
    """Runs each call as ``op.call_reference`` on host tensors, a state
    written in place and per-call values as plain numbers.
    """

    # Operators are constructed at a bounded call's valid rows, which only
    # their reference() runs at.
    checks = False

    def __init__(
        self,
        name: str,
        profile: Profile | None = None,
        held: Iterable[tuple[str, np.ndarray]] = (),
    ):
        super().__init__(name, profile)
        self.held = list(held)

    def operand(self, x):
        return x

    def viewed(self, x: State | Weight):
        if isinstance(x, Weight):
            return x.array
        if x.host is None:
            x.host = np.zeros(x.shape, dtype=x.dtype)
        return _HostView(x, x.shape)

    def overwrites(self, given) -> str | None:
        if isinstance(given, Weight):
            return "weight"
        if not isinstance(given, np.ndarray):
            return None
        return next(
            (kind for kind, t in self.held if np.may_share_memory(given, t)), None
        )

    def call(self, target, args, kwargs):
        cls = target if isinstance(target, type) else type(target)
        inputs, outputs, kwargs = cls.declaration.call_operands(args, kwargs)
        self.check_outputs(cls, outputs)
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
                Handle(t.shape, np.dtype(t.dtype).type, "", "input") if p is None else p
                for t, p in zip(tensors, patterns)
            ]
            # The reference runs a bounded call on the rows it covers, so a
            # view one axis longer than the operand it copies is narrowed to
            # it there, as the trace bounds the view alike.
            given = [t.shape for t, p in zip(tensors[:n_views], patterns) if p is None]
            for i, p in enumerate(patterns[:n_views]):
                for shape in given if p is not None else ():
                    axes = [a for a, (m, n) in enumerate(zip(p.shape, shape)) if m != n]
                    if len(shape) != len(p.shape) or len(axes) != 1:
                        continue
                    (axis,) = axes
                    if shape[axis] < p.shape[axis]:
                        key = [slice(None)] * len(shape)
                        key[axis] = slice(shape[axis])
                        shapes[i] = Handle(
                            shape,
                            p.dtype,
                            p.name,
                            p.role,
                            p.parent,
                            p.start,
                            p.tap[tuple(key)],
                        )
            shapes = _take_views(cls, shapes, kwargs, {})
            op = self._construct(cls, dict(zip(inputs, shapes)), shapes[n_in:], kwargs)
        else:
            op = target
            values = self._split_values(cls, kwargs)
        outs = [b for b in op.buffers if isinstance(b, Out)]
        given = dict(zip((b.name for b in outs), tensors[n_in:]))
        results = op._call_reference(dict(zip(inputs, tensors[:n_in])), given, values)
        for name, out in given.items():
            if results[name] is not out:
                out[...] = np.asarray(results[name]).reshape(out.shape)
        if len(results) > 1:
            return tuple(results.values())
        (result,) = results.values()
        # Shaped as Tracer._record shapes a flat output.
        if not given and len(outs) == 1 and len(outs[0].shape) == 1:
            called = [t if p is None else p for t, p in zip(tensors, patterns)]
            like = next(
                (t for t in called if math.prod(t.shape) == outs[0].elements), None
            )
            if like is not None:
                result = result.reshape(like.shape, copy=False)
        return result
