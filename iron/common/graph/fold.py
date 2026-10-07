# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a step into the step that produced its one input."""

from __future__ import annotations

import dataclasses
from collections import Counter
from collections.abc import Collection, Hashable

from ..declare import Operator, Unresolvable
from .trace import TracedGraph


@dataclasses.dataclass(frozen=True)
class Fold:
    """The steps of one design folded into producers of another: each
    names the resolved ``design_key()`` of its operator.
    """

    producer: Hashable
    consumer: Hashable

    def __str__(self) -> str:
        return f"{self.consumer[0]} into {self.producer[0]}"


def folded(
    traced: TracedGraph, dev, only: Collection[Fold] | None = None
) -> tuple[TracedGraph, Counter[Fold]]:
    """``traced`` with each step its producer can apply in its own cores
    folded into the producer (``Operator.fold``), then each operator that
    can run on a folded one's array moved onto it (``Operator.on_array``),
    so a fold does not split an array two designs shared.

    A step folds where its one input is a whole intermediate that it and
    its producer alone name, its one output is a whole buffer of the same
    size the graph does not hold, no per-call value is bound to it, and its
    producer runs at one step. The folded step runs where the producer ran
    and writes the consumer's output.

    Args:
        traced: The graph as traced.
        dev: The device the folded operators must resolve for.
        only: The folds to apply; every one the graph admits if not given.

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
    replace: dict[int, Operator] = {}
    applied: Counter[Fold] = Counter()
    for k, step in enumerate(traced.steps):
        if len(step.inputs) != 1 or len(step.outputs) != 1:
            continue
        (x,), (y,) = step.inputs, step.outputs
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
        ):
            continue
        producer = steps[j]
        fused = producer.op.fold(step.op)
        if fused is None:
            continue
        fold = Fold(
            producer.op.resolved(dev).design_key(), step.op.resolved(dev).design_key()
        )
        if only is not None and fold not in only:
            continue
        try:
            fused.resolved(dev)
        except (Unresolvable, ValueError):
            continue
        steps[j] = dataclasses.replace(
            producer,
            slots=[
                y.reshape(h.shape) if h.name == x.name else h for h in producer.slots
            ],
            outputs=[
                y.reshape(h.shape) if h.name == x.name else h for h in producer.outputs
            ],
        )
        steps[k] = None
        replace[id(producer.op)] = fused
        applied[fold] += 1
    if not replace:
        return traced, applied
    arrays = {f.resolved(dev).array_key(): f for f in replace.values()}
    for s in traced.steps:
        if id(s.op) in replace:
            continue
        for key, f in arrays.items():
            moved = s.op.on_array(f)
            if moved is not None and moved.resolved(dev).array_key() == key:
                replace[id(s.op)] = moved
                break
    kept = dataclasses.replace(traced, steps=[s for s in steps if s is not None])
    return kept.with_operators(replace), applied


def replaced(
    traced: TracedGraph, folds: TracedGraph
) -> list[tuple[Operator, Operator]]:
    """The operators ``folded`` swapped to make ``folds`` from ``traced``:
    each step of ``folds`` whose operator is not its step's in ``traced``,
    as (traced's, folds').

    A folded graph keeps its steps' order and inputs, and a step folded away
    took an input no other step does, so each step of ``folds`` is the next
    step of ``traced`` that reads what it reads.
    """
    plain = iter(traced.steps)
    pairs = []
    for step in folds.steps:
        reads = [h.name for h in step.inputs]
        twin = next(s for s in plain if [h.name for h in s.inputs] == reads)
        if twin.op is not step.op:
            pairs.append((twin.op, step.op))
    return pairs
