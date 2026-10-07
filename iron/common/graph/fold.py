# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a step into the step that produced its one input."""

from __future__ import annotations

import dataclasses
from collections import Counter

from ..declare import Operator, Unresolvable
from .trace import TracedGraph


def folded(traced: TracedGraph, dev) -> tuple[TracedGraph, int]:
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

    Returns:
        The folded graph (``traced`` itself where nothing folds) and the
        number of steps folded away.
    """
    named = Counter((h.parent or h).name for s in traced.steps for h in s.slots)
    named.update((h.parent or h).name for h in traced.outputs)
    calls = Counter(id(s.op) for s in traced.steps)
    bound = {id(b.op) for b in traced.bindings}
    producers = {h.name: i for i, s in enumerate(traced.steps) for h in s.outputs}
    steps = list(traced.steps)
    replace: dict[int, Operator] = {}
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
    if not replace:
        return traced, 0
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
    return kept.with_operators(replace), len(traced.steps) - len(kept.steps)
