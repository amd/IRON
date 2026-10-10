# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a step into the step that produced one of its inputs, or into
the steps that read its output, and a copy into its producer's drain.
"""

from __future__ import annotations

import dataclasses
from collections import Counter
from collections.abc import Collection, Hashable
from types import MethodType

from ..declare import Operator, Unresolvable
from ..declare.member import Extent
from .trace import Binding, TracedGraph

# The most ``folded`` runs ``foldings`` makes, each with others left out.
FOLD_RUNS = 256


@dataclasses.dataclass(frozen=True)
class Fold:
    """A step of one design folded into the producer of its input ``at``,
    a step of another, after the steps of ``after`` were folded into it in
    turn: each names the resolved ``design_key()`` of its operator, those
    of ``after`` with the input each took the tile at.
    """

    producer: Hashable
    consumer: Hashable
    at: int = 0
    after: tuple[tuple[Hashable, int], ...] = ()

    @property
    def chain(self) -> tuple[tuple[Hashable, int], ...]:
        """The steps folded into the producer, through this one."""
        return (*self.after, (self.consumer, self.at))

    def __str__(self) -> str:
        names = [
            f"{k[0].__name__}{f' (input {at})' if at else ''}" for k, at in self.chain
        ]
        return f"{', then '.join(names)} into {self.producer[0].__name__}"


@dataclasses.dataclass(frozen=True)
class Prologue:
    """A step of one design folded into the steps that read its output,
    each applying it to the input it prepares, the tile taking its input
    ``at``, before the steps of ``after`` folded into them already: each
    names the resolved ``design_key()`` of its operator, those of ``after``
    with the input each took the tile at.
    """

    producer: Hashable
    consumers: tuple[Hashable, ...]
    at: int = 0
    after: tuple[tuple[Hashable, int], ...] = ()

    @property
    def chain(self) -> tuple[tuple[Hashable, int], ...]:
        """The steps folded into the consumers through this one, in the
        order they run.
        """
        return ((self.producer, self.at), *self.after)

    def __str__(self) -> str:
        names = [
            f"{k[0].__name__}{f' (input {at})' if at else ''}" for k, at in self.chain
        ]
        consumers = ", ".join(k[0].__name__ for k in self.consumers)
        return f"{', then '.join(names)} into {consumers}"


@dataclasses.dataclass(frozen=True)
class Place:
    """A copy of one design folded into the drain of the producer of its
    input, a step of another, after the steps of ``after`` were folded into
    that: the producer writes the run the copy wrote. Each names the
    resolved ``design_key()`` of its operator, those of ``after`` with the
    input each took the tile at.
    """

    producer: Hashable
    copy: Hashable
    after: tuple[tuple[Hashable, int], ...] = ()

    def __str__(self) -> str:
        names = [self.producer[0].__name__, *(k[0].__name__ for k, _ in self.after)]
        return f"{self.copy[0].__name__} into the drain of {', then '.join(names)}"


# Every kind of fold ``folded`` applies.
Folding = Fold | Prologue | Place


class Made:
    """The operators ``folded`` makes from a graph's, and their
    resolutions, each made once: the runs of one search (``foldings``)
    share one, so what runs leaving different folds out make alike is made
    once. Each is kept by the ``id`` of what it is made from, held here so
    the ids stay theirs.
    """

    def __init__(self, dev):
        self.dev = dev
        self._made: dict[tuple, tuple[Operator, Operator, Operator | None]] = {}
        self._resolved: dict[int, tuple[Operator, Operator | None]] = {}

    def of(
        self, method: MethodType, other: Operator, *args: Hashable
    ) -> Operator | None:
        """``method``, an operator's ``fold``, ``prefold``, ``on_array`` or
        ``placed``, applied to ``other`` and ``args``.
        """
        key = (method.__func__, id(method.__self__), id(other), args)
        if key not in self._made:
            self._made[key] = (method.__self__, other, method(other, *args))
        return self._made[key][2]

    def resolved(self, op: Operator) -> Operator | None:
        """``op`` resolved for the device, or None where it does not."""
        if id(op) not in self._resolved:
            try:
                new = op.resolved(self.dev)
            except (Unresolvable, ValueError):
                new = None
            self._resolved[id(op)] = (op, new)
        return self._resolved[id(op)][1]


def folded(
    traced: TracedGraph,
    dev,
    only: Collection[Folding] | None = None,
    without: Collection[Folding] = (),
    made: Made | None = None,
) -> tuple[TracedGraph, Counter[Folding]]:
    """``traced`` with each step whose readers can apply it in their own
    cores folded into them (``Operator.prefold``), each step its producer
    can apply in its own cores folded into the producer
    (``Operator.fold``), each copy its producer can write in its place
    folded into the producer's drain (``Operator.placed``), then each
    operator that can run on a folded one's array moved onto it
    (``Operator.on_array``), so a fold does not split an array two designs
    shared.

    A step folds into its readers where its one output is a whole,
    unbounded intermediate each of them reads, once, as the input it
    prepares, they and it called once and it bound to no per-call value;
    its input ``at`` takes the place of that output, of its size and type,
    and its others stream into each reader's prepared input. No step
    between it and a reader may write those inputs, and each reader must
    keep every width it had.

    A step folds where one input is a whole intermediate that it and its
    producer alone name, each other input a whole buffer of its output's
    size and type, its one output a whole buffer of that size the graph
    does not hold, and its producer runs at one step and keeps every width
    it had. A bounded input folds where the output and every other input
    are of its shape and bounds, and the step's only per-call values are
    the extents those bounds bind: the producer's own bound then sizes the
    tiles it finishes. Its other inputs then stream into the producer's
    cores. The folded step runs where the producer ran
    if no step between them writes those inputs, else where the consumer
    ran if none writes the producer's, and writes the consumer's output;
    a step it reads produces into it in turn.

    A copy folds into its producer's drain where it writes its input, a
    whole intermediate that it and its producer alone name, verbatim to
    one run of its output (``Operator.copies_to``), neither bounded, each
    called once, and no step between them names that output: the producer
    then drains into the copy's output, at the run and moved by the copy's
    per-call offset (``Operator.placed``).

    Args:
        traced: The graph as traced.
        dev: The device the folded operators must resolve for.
        only: The folds to apply, each ``Fold`` with the folds of its
            chain before it; every one the graph admits if not given.
        without: Folds not to apply, so that those they would pre-empt
            can be.
        made: The operators earlier runs over ``traced`` on ``dev`` made.

    Returns:
        The folded graph (``traced`` itself where nothing folds) and the
        steps folded away, by fold.
    """
    made = Made(dev) if made is None else made
    named = Counter((h.parent or h).name for s in traced.steps for h in s.slots)
    named.update((h.parent or h).name for h in traced.outputs)
    calls = Counter(id(s.op) for s in traced.steps)
    bindings = Counter(id(b.op) for b in traced.bindings)
    extents = Counter(
        id(b.op) for b in traced.bindings if isinstance(b.member.member, Extent)
    )
    steps: list = list(traced.steps)
    replace: dict[int, Operator] = {}
    applied: Counter[Folding] = Counter()
    # Per prepared step: the designs folded into it, the first applied first.
    prologues: dict[int, tuple[tuple[Hashable, int], ...]] = {}
    for j in reversed(range(len(steps))):
        producer = steps[j]
        if (
            len(producer.outputs) != 1
            or calls[id(producer.op)] != 1
            or bindings[id(producer.op)]
        ):
            continue
        (h,) = producer.outputs
        if h.role != "intermediate" or h.parent or h.tap is not None or h.bounds:
            continue
        readers = [
            k
            for k in range(j + 1, len(steps))
            if steps[k] is not None and any(i.name == h.name for i in steps[k].inputs)
        ]
        # Each reader's prepared input: the slot of its member declared so.
        prepared = {
            k: next(
                (i for i, b in enumerate(steps[k].op.buffers) if b.member.prepare),
                None,
            )
            for k in readers
        }
        if (
            not readers
            or named[h.name] != 1 + len(readers)
            or any(calls[id(steps[k].op)] != 1 for k in readers)
            or any(
                i is None or steps[k].slots[i].name != h.name
                for k, i in prepared.items()
            )
            or len({prologues.get(k, ()) for k in readers}) != 1
        ):
            continue
        for at, x in enumerate(producer.inputs):
            if x.elements != h.elements or x.dtype != h.dtype or x.bounds:
                continue
            extras = [e for i, e in enumerate(producer.inputs) if i != at]
            fused = _prefolded(steps, replace, readers, j, x, extras, at, made)
            if fused is None:
                continue
            fold = Prologue(
                made.resolved(producer.op).design_key(),
                tuple(made.resolved(steps[k].op).design_key() for k in readers),
                at,
                prologues.get(readers[0], ()),
            )
            if fold in without:
                continue
            if only is not None and not any(
                isinstance(f, Prologue)
                and f.consumers == fold.consumers
                and f.chain[len(f.chain) - len(fold.chain) :] == fold.chain
                for f in only
            ):
                continue
            for k in readers:
                step, slot = steps[k], prepared[k]
                op = replace.get(id(step.op), step.op)
                # Before the prologue's inputs so far: the producer runs first.
                tail = len(op.prepare_inputs) + len(op.finish_inputs)
                given = [
                    e.reshape(b.shape) for e, b in zip(extras, fused[k].prepare_inputs)
                ]
                tile = x.reshape(step.slots[slot].shape)
                slots = [tile if i == slot else e for i, e in enumerate(step.slots)]
                inputs = [tile if e.name == h.name else e for e in step.inputs]
                steps[k] = dataclasses.replace(
                    step,
                    slots=[
                        *slots[: len(slots) - tail],
                        *given,
                        *slots[len(slots) - tail :],
                    ],
                    inputs=[
                        *inputs[: len(inputs) - tail],
                        *given,
                        *inputs[len(inputs) - tail :],
                    ],
                )
                replace[id(step.op)] = fused[k]
                prologues[k] = fold.chain
            steps[j] = None
            applied[fold] += 1
            break
    current = [s for s in steps if s is not None]
    named = Counter((h.parent or h).name for s in current for h in s.slots)
    named.update((h.parent or h).name for h in traced.outputs)
    producers = {
        h.name: i for i, s in enumerate(steps) if s is not None for h in s.outputs
    }
    # Per folded step: its producer's design and the designs folded into it.
    origins: dict[int, tuple[Hashable, tuple[tuple[Hashable, int], ...]]] = {}
    for k, step in enumerate(list(steps)):
        if step is None or len(step.outputs) != 1:
            continue
        (y,) = step.outputs
        for at, x in enumerate(step.inputs):
            extras = [h for i, h in enumerate(step.inputs) if i != at]
            j = producers.get(x.name)
            if (
                j is None
                or steps[j] is None
                or x.role != "intermediate"
                or x.parent is not None
                or x.tap is not None
                or named[x.name] != 2
                or y.parent is not None
                or y.role not in ("intermediate", "output")
                or y.elements != x.elements
                or y.dtype != x.dtype
                or y.bounds != x.bounds
                or (x.bounds and y.shape != x.shape)
                or bindings[id(step.op)] != (extents[id(step.op)] if x.bounds else 0)
                or calls[id(steps[j].op)] != 1
                or any(
                    e.parent is not None
                    or e.tap is not None
                    or e.bounds != x.bounds
                    or (x.bounds and e.shape != x.shape)
                    or e.elements != y.elements
                    or e.dtype != y.dtype
                    for e in extras
                )
            ):
                continue
            producer = steps[j]
            current = replace.get(id(producer.op), producer.op)
            fused = made.of(current.fold, replace.get(id(step.op), step.op), at)
            if fused is None:
                continue
            start, after = origins.get(j, (made.resolved(producer.op).design_key(), ()))
            fold = Fold(start, made.resolved(step.op).design_key(), at, after)
            if fold in without:
                continue
            if only is not None and not any(
                isinstance(f, Fold)
                and f.producer == start
                and f.chain[: len(fold.chain)] == fold.chain
                for f in only
            ):
                continue
            new = made.resolved(fused)
            if new is None or any(
                new.widths[n] < w for n, w in made.resolved(current).widths.items()
            ):
                continue
            written = {
                (h.parent or h).name
                for s in steps[j + 1 : k]
                if s is not None
                for h in s.outputs
            }
            if not written & {e.name for e in extras}:
                to = j
            elif not written & {(h.parent or h).name for h in producer.inputs}:
                to = k
            else:
                continue
            shape = next(h.shape for h in producer.slots if h.name == x.name)
            extras = [e.reshape(shape) for e in extras]
            steps[j] = None
            steps[to] = dataclasses.replace(
                producer,
                slots=[
                    y.reshape(h.shape) if h.name == x.name else h
                    for h in producer.slots
                ]
                + extras,
                inputs=[*producer.inputs, *extras],
                outputs=[
                    y.reshape(h.shape) if h.name == x.name else h
                    for h in producer.outputs
                ],
            )
            if to == j:
                steps[k] = None
            producers[y.name] = to
            origins.pop(j, None)
            origins[to] = (start, fold.chain)
            replace[id(producer.op)] = fused
            applied[fold] += 1
            break
    given: dict[int, dict] = {}
    for b in traced.bindings:
        given.setdefault(id(b.op), {})[b.member.name] = b.expression
    placings = []
    for k, step in enumerate(list(steps)):
        if step is None or len(step.inputs) != 1 or len(step.outputs) != 1:
            continue
        (x,), (y,) = step.inputs, step.outputs
        run = step.op.copies_to()
        j = producers.get(x.name)
        values = given.get(id(step.op), {})
        if (
            run is None
            or j is None
            or steps[j] is None
            or calls[id(step.op)] != 1
            or calls[id(steps[j].op)] != 1
            or extents[id(steps[j].op)]
            or x.role != "intermediate"
            or x.parent is not None
            or x.tap is not None
            or x.bounds
            or named[x.name] != 2
            or y.tap is not None
            or y.bounds
            or (y.parent is not None and y.parent.parent is not None)
            or run.start + x.elements > y.elements
            or any(
                (y.parent or y).name in {(h.parent or h).name for h in s.slots}
                for s in steps[j + 1 : k]
                if s is not None
            )
        ):
            continue
        producer = steps[j]
        current = replace.get(id(producer.op), producer.op)
        i = next(i for i, h in enumerate(producer.slots) if h.name == x.name)
        operand = current.buffers[i].name
        fused = made.of(current.placed, step.op, operand)
        if fused is None or made.resolved(fused) is None:
            continue
        start, after = origins.get(j, (made.resolved(producer.op).design_key(), ()))
        place = Place(start, made.resolved(step.op).design_key(), after)
        if place in without or (only is not None and place not in only):
            continue
        steps[j] = dataclasses.replace(
            producer,
            slots=[y if n == i else s for n, s in enumerate(producer.slots)],
            outputs=[y if o.name == x.name else o for o in producer.outputs],
        )
        steps[k] = None
        replace[id(producer.op)] = fused
        if run.offset is not None:
            word = producer.op.value(f"{operand}_offset")
            placings.append(Binding(producer.op, word, values[run.offset]))
        applied[place] += 1
    if not replace:
        return traced, applied
    arrays = {made.resolved(f).array_key(): f for f in replace.values()}
    for s in traced.steps:
        base = replace.get(id(s.op), s.op)
        for key, f in arrays.items():
            if base is f:
                continue
            moved = made.of(base.on_array, f)
            new = None if moved is None else made.resolved(moved)
            if new is not None and new.array_key() == key:
                replace[id(s.op)] = moved
                break
    kept = [s for s in steps if s is not None]
    running = {id(s.op) for s in kept}
    kept = dataclasses.replace(
        traced,
        steps=kept,
        bindings=[b for b in [*traced.bindings, *placings] if id(b.op) in running],
    )
    return kept.with_operators(replace), applied


def foldings(
    traced: TracedGraph, dev, limit: int = FOLD_RUNS, made: Made | None = None
) -> tuple[dict[frozenset[Folding], tuple[TracedGraph, Counter[Folding]]], bool]:
    """Each way ``folded`` folds ``traced`` with some of its folds left out:
    leaving out a fold it applies lets one that fold pre-empted apply, and
    leaving out each fold a site admits leaves the site as traced.

    Args:
        traced: The graph as traced.
        dev: The device the folded operators must resolve for.
        limit: The most ``folded`` runs, each with other folds left out.
        made: The operators earlier runs over ``traced`` on ``dev`` made.

    Returns:
        Each folded graph and the steps it folded away, by the folds
        applied, folding everything first; and whether they are every way,
        False where ``limit`` runs did not reach them all.
    """
    found: dict[frozenset[Folding], tuple[TracedGraph, Counter[Folding]]] = {}
    queue: list[frozenset[Folding]] = [frozenset()]
    seen = set(queue)
    made = Made(dev) if made is None else made
    for _ in range(limit):
        if not queue:
            break
        left = queue.pop(0)
        trial, applied = folded(traced, dev, without=left, made=made)
        found.setdefault(frozenset(applied), (trial, applied))
        for fold in applied:
            more = left | {fold}
            if more not in seen:
                seen.add(more)
                queue.append(more)
    return found, not queue


def _prefolded(
    steps: list,
    replace: dict[int, Operator],
    readers,
    j: int,
    x,
    extras,
    at,
    made: Made,
) -> dict[int, Operator] | None:
    """Each of ``readers`` (indices of ``steps``) with the operator of step
    ``j`` folded into it, ``x`` the tile and ``extras`` its other inputs,
    or None: where one does not prepare it, does not resolve, narrows, or
    runs after a step that writes what the fold reads.
    """
    reads = {(e.parent or e).name for e in [x, *extras]}
    fused = {}
    for k in readers:
        written = {
            (o.parent or o).name
            for s in steps[j + 1 : k]
            if s is not None
            for o in s.outputs
        }
        op = replace.get(id(steps[k].op), steps[k].op)
        new = made.of(op.prefold, steps[j].op, at)
        if new is None or written & reads:
            return None
        resolved = made.resolved(new)
        if resolved is None or any(
            resolved.widths[n] < w for n, w in made.resolved(op).widths.items()
        ):
            return None
        fused[k] = new
    return fused


def replaced(
    traced: TracedGraph, folds: TracedGraph
) -> list[tuple[Operator, Operator]]:
    """The operators ``folded`` swapped to make ``folds`` from ``traced``:
    each step of ``folds`` whose operator is not its step's in ``traced``,
    as (traced's, folds').

    A folded step reads what its producer's step read, then its finish's
    other inputs, and a step a prologue folded into reads that step's input
    in place of its output, then the prologue's other inputs. Its twin is
    the first step of ``traced`` not yet paired, of its type, that reads
    what it reads without those, its prepared input aside.
    """
    paired: set[int] = set()
    pairs = []
    for step in folds.steps:
        op = step.op
        extra = {b.name for b in [*op.prepare_inputs, *op.finish_inputs]}
        reads = [
            None if b.member.prepare and op.prepare else h.name
            for b, h in zip(op.buffers, step.slots)
            if b.direction.fills and b.name not in extra
        ]
        i = next(
            i
            for i, s in enumerate(traced.steps)
            if i not in paired
            and type(s.op) is type(op)
            and [
                None if b.member.prepare and op.prepare else h.name
                for b, h in zip(s.op.buffers, s.slots)
                if b.direction.fills
            ]
            == reads
        )
        paired.add(i)
        if traced.steps[i].op is not step.op:
            pairs.append((traced.steps[i].op, step.op))
    return pairs
