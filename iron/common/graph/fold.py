# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a step into the step that produced one of its inputs."""

from __future__ import annotations

import dataclasses
from collections import Counter
from collections.abc import Collection, Hashable

from ..declare import Operator, Unresolvable
from .trace import TracedGraph


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
        names = [f"{k[0]}{f' (input {at})' if at else ''}" for k, at in self.chain]
        return f"{', then '.join(names)} into {self.producer[0]}"


def folded(
    traced: TracedGraph, dev, only: Collection[Fold] | None = None
) -> tuple[TracedGraph, Counter[Fold]]:
    """``traced`` with each step its producer can apply in its own cores
    folded into the producer (``Operator.fold``), then each operator that
    can run on a folded one's array moved onto it (``Operator.on_array``),
    so a fold does not split an array two designs shared.

    A step folds where one input is a whole intermediate that it and its
    producer alone name, each other input a whole buffer of its output's
    size and type, its one output a whole buffer of that size the graph
    does not hold, no per-call value is bound to it, and its producer runs
    at one step and keeps every width it had. Its other inputs then stream
    into the producer's cores. The folded step runs where the producer ran
    if no step between them writes those inputs, else where the consumer
    ran if none writes the producer's, and writes the consumer's output;
    a step it reads produces into it in turn.

    Args:
        traced: The graph as traced.
        dev: The device the folded operators must resolve for.
        only: The folds to apply, each with the folds of its chain before
            it; every one the graph admits if not given.

    Returns:
        The folded graph (``traced`` itself where nothing folds) and the
        steps folded away, by fold.
    """
    named = Counter((h.parent or h).name for s in traced.steps for h in s.slots)
    named.update((h.parent or h).name for h in traced.outputs)
    calls = Counter(id(s.op) for s in traced.steps)
    bound = {id(b.op) for b in traced.bindings}
    producers = {h.name: i for i, s in enumerate(traced.steps) for h in s.outputs}
    steps = list(traced.steps)
    # Per folded step: its producer's design and the designs folded into it.
    origins: dict[int, tuple[Hashable, tuple[tuple[Hashable, int], ...]]] = {}
    replace: dict[int, Operator] = {}
    applied: Counter[Fold] = Counter()
    for k, step in enumerate(traced.steps):
        if len(step.outputs) != 1:
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
                or x.bounds
                or named[x.name] != 2
                or y.parent is not None
                or y.role not in ("intermediate", "output")
                or y.elements != x.elements
                or y.dtype != x.dtype
                or id(step.op) in bound
                or calls[id(steps[j].op)] != 1
                or any(
                    e.parent is not None
                    or e.tap is not None
                    or e.bounds
                    or e.elements != y.elements
                    or e.dtype != y.dtype
                    for e in extras
                )
            ):
                continue
            producer = steps[j]
            current = replace.get(id(producer.op), producer.op)
            fused = current.fold(step.op, at)
            if fused is None:
                continue
            start, after = origins.get(j, (current.resolved(dev).design_key(), ()))
            fold = Fold(start, step.op.resolved(dev).design_key(), at, after)
            if only is not None and not any(
                f.producer == start and f.chain[: len(fold.chain)] == fold.chain
                for f in only
            ):
                continue
            try:
                widths = fused.resolved(dev).widths
            except (Unresolvable, ValueError):
                continue
            if any(widths[n] < w for n, w in current.resolved(dev).widths.items()):
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
    if not replace:
        return traced, applied
    arrays = {f.resolved(dev).array_key(): f for f in replace.values()}
    for s in traced.steps:
        if id(s.op) in replace:
            continue
        for key, f in arrays.items():
            moved = s.op.on_array(f)
            if moved is None:
                continue
            try:
                if moved.resolved(dev).array_key() == key:
                    replace[id(s.op)] = moved
                    break
            except (Unresolvable, ValueError):
                continue
    kept = dataclasses.replace(traced, steps=[s for s in steps if s is not None])
    return kept.with_operators(replace), applied


def replaced(
    traced: TracedGraph, folds: TracedGraph
) -> list[tuple[Operator, Operator]]:
    """The operators ``folded`` swapped to make ``folds`` from ``traced``:
    each step of ``folds`` whose operator is not its step's in ``traced``,
    as (traced's, folds').

    A folded step reads what its producer's step read, then its finish's
    other inputs, so its twin is the first step of ``traced`` not yet
    paired, of its type, that reads what it reads without them.
    """
    paired: set[int] = set()
    pairs = []
    for step in folds.steps:
        reads = [h.name for h in step.inputs]
        own = reads[: len(reads) - len(step.op.finish_inputs)]
        i = next(
            i
            for i, s in enumerate(traced.steps)
            if i not in paired
            and type(s.op) is type(step.op)
            and [h.name for h in s.inputs] == own
        )
        paired.add(i)
        if traced.steps[i].op is not step.op:
            pairs.append((traced.steps[i].op, step.op))
    return pairs
