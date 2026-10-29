# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a step into the producer of its one input: a recording rewrite
collapsing the pair into one step, the producer's operator carrying the
``finish`` (``Operator.fold``). Unlike a stream fusion, which runs the
consumer in cores of its own fed on-chip from the producer's, a fold leaves
the consumer no cores: its kernel runs inside the producer's, on the tile
before it leaves L1.
"""

from __future__ import annotations

import dataclasses
from collections import Counter
from collections.abc import Sequence

from ..declare.operator import Operator, Unresolvable
from ..declare.profile import Profile
from ..image.step import Edge, Fusion, FusionKind
from .record import Binding, Recording, Step


def _excluded(recording: Recording) -> set[str]:
    return (
        {h.name for h in recording.outputs}
        | set(recording.feedback)
        | set(recording.pinned)
        | set(recording.residents)
    )


def _admits(producer: Operator, consumer: Operator, at: int) -> Operator | None:
    """``producer.fold(consumer, at)``, or None where it refuses or does not
    resolve on the current device.
    """
    try:
        fused = producer.fold(consumer, at)
    except Unresolvable:
        return None
    if fused is None:
        return None
    try:
        fused.resolved(fused.dev)
    except (Unresolvable, ValueError):
        return None
    return fused


def _adjacent(recording: Recording) -> dict[int, tuple[Operator, int]]:
    """Index ``i`` admissible to fold step ``i + 1`` into step ``i``: the
    fused operator and the input of step ``i + 1`` the tile enters at, where
    step ``i`` has one output, read only by step ``i + 1``, never again, is
    not a graph output, feedback, pinned or resident buffer, and names its
    whole buffer, unbounded; step ``i + 1``'s other inputs do too, of the
    tile's element count and dtype; step ``i``'s operator runs one step; and
    ``producer.fold(consumer, at)`` (``_admits``) admits it, which is where
    the channel budget, the shapes and dtypes, and a tile a later call reads
    are refused.
    """
    excluded = _excluded(recording)
    readers: dict[str, list[int]] = {}
    writers: dict[str, list[int]] = {}
    for i, step in enumerate(recording.steps):
        for buf, ref in zip(step.op.buffers, step.refs()):
            if buf.fills:
                readers.setdefault(ref.root, []).append(i)
            if buf.drains:
                writers.setdefault(ref.root, []).append(i)
    for host_step in recording.host:
        for h in host_step.reads:
            readers.setdefault(h.ref().root, []).append(-1)
        for h in host_step.writes:
            writers.setdefault(h.ref().root, []).append(-1)
    calls = Counter(id(s.op) for s in recording.steps)

    found: dict[int, tuple[Operator, int]] = {}
    for i in range(len(recording.steps) - 1):
        step, nxt = recording.steps[i], recording.steps[i + 1]
        if calls[id(step.op)] != 1:
            continue
        # Handle-level shapes and bounds, not the (possibly unresolved)
        # Operand's: a Select()-shaped operand (GEMM's bfp16_b) needs its
        # tunable resolved before its own elements/dtype read.
        outs = [
            (buf, ref, h)
            for buf, ref, h in zip(step.op.buffers, step.refs(), step.slots)
            if buf.drains
        ]
        if len(outs) != 1:
            continue
        buf, ref, tile = outs[0]
        if (
            ref.nbytes is not None
            or tile.valid
            or ref.root in excluded
            or readers.get(ref.root) != [i + 1]
            or writers.get(ref.root) != [i]
        ):
            continue
        matches = [
            (cbuf, cref, ch)
            for cbuf, cref, ch in zip(nxt.op.buffers, nxt.refs(), nxt.slots)
            if cbuf.fills and cref.root == ref.root
        ]
        if len(matches) != 1 or matches[0][1].nbytes is not None or matches[0][2].valid:
            continue
        cbuf, _, _ = matches[0]
        at = next(k for k, b in enumerate(nxt.op.inputs) if b.name == cbuf.name)
        if len([b for b in nxt.op.buffers if b.drains]) != 1:
            continue
        others = [
            (b, r, h)
            for b, r, h in zip(nxt.op.buffers, nxt.refs(), nxt.slots)
            if b.fills and b.name != cbuf.name
        ]
        if any(
            r.nbytes is not None
            or h.valid
            or h.elements != tile.elements
            or h.dtype != tile.dtype
            for _, r, h in others
        ):
            continue
        fused = _admits(step.op, nxt.op, at)
        if fused is None:
            continue
        found[i] = (fused, at)
    return found


def fold_candidates(recording: Recording) -> tuple[Fusion, ...]:
    """Every admissible fold of two consecutive steps of ``recording``
    (``_adjacent``), overlapping ones included: a step that admits folding
    both its predecessor's output and feeding its successor's appears in two
    candidates, at most one of which a caller may take.
    """
    adjacent = _adjacent(recording)
    found = []
    for i, (_, at) in adjacent.items():
        step, nxt = recording.steps[i], recording.steps[i + 1]
        (buf,) = (b for b in step.op.buffers if b.drains)
        edge = Edge(i, buf.name, i + 1, nxt.op.inputs[at].name)
        found.append(Fusion(FusionKind.FOLD, (i, i + 1), (edge,)))
    return tuple(found)


def chosen_folds(recording: Recording, profile: Profile) -> tuple[Fusion, ...]:
    """``fold_candidates(recording)`` that ``profile`` names (``Profile.fused``),
    a step in at most one: first in step order wins, as ``Graph.compile``
    picks among a graph's other fusion kinds (``fusion.fusions``).
    """
    found: list[Fusion] = []
    taken: set[int] = set()
    for fusion in fold_candidates(recording):
        if taken & set(fusion.steps):
            continue
        steps = [recording.steps[i].op.resolved() for i in fusion.steps]
        local = {step: i for i, step in enumerate(fusion.steps)}
        edges = tuple(
            (local[e.producer], e.output, local[e.consumer], e.input)
            for e in fusion.edges
        )
        if not profile.fused(fusion.kind, steps, edges):
            continue
        found.append(fusion)
        taken.update(fusion.steps)
    return tuple(found)


def _rebind(
    op: Operator, fused: Operator, bindings: Sequence[Binding]
) -> list[Binding]:
    """``bindings``, each on ``op`` moved onto ``fused``, which declares the
    same per-call members (a fold only adds a ``finish`` and its input).
    """
    return [
        Binding(fused, fused.value(b.member.name), b.expression) if b.op is op else b
        for b in bindings
    ]


def _handle_at(step: Step, name: str) -> tuple[int, object]:
    """The index into ``step.slots`` and the handle there, the operand
    declared ``name``'s.
    """
    i = next(k for k, b in enumerate(step.op.buffers) if b.name == name)
    return i, step.slots[i]


def apply_folds(recording: Recording, folds: Sequence[Fusion]) -> Recording:
    """``recording`` with each of ``folds`` (``fold_candidates``'s, not
    overlapping) applied: the pair's steps collapsed into one at the
    producer's position, its operator ``Operator.fold``-ed, its slots the
    producer's with the consumer's other input appended, its output the
    consumer's.

    Raises:
        ValueError: Two of ``folds`` share a step, or a fold no longer
            admits (its operator changed since ``fold_candidates`` ran).
    """
    taken: dict[int, Fusion] = {}
    for fusion in folds:
        if fusion.kind is not FusionKind.FOLD:
            raise ValueError(f"apply_folds: {fusion.kind.value} is not a fold")
        i, j = fusion.steps
        if j != i + 1:
            raise ValueError(f"a fold's steps must be consecutive, not {fusion.steps}")
        if i in taken or j in taken:
            raise ValueError(f"step {i if i in taken else j} is folded twice")
        taken[i] = taken[j] = fusion
    steps: list[Step | None] = list(recording.steps)
    bindings = list(recording.bindings)
    for fusion in dict.fromkeys(taken.values()):
        i, j = fusion.steps
        (edge,) = fusion.edges
        step, nxt = recording.steps[i], recording.steps[j]
        at = next(k for k, b in enumerate(nxt.op.inputs) if b.name == edge.input)
        fused = step.op.fold(nxt.op, at)
        if fused is None:
            raise ValueError(f"{fusion} no longer admits: {step.op!r} refuses it")
        _, tile = _handle_at(step, edge.output)
        (result_name,) = (b.name for b in nxt.op.buffers if b.drains)
        _, result = _handle_at(nxt, result_name)
        extra = [
            h
            for b, h in zip(nxt.op.buffers, nxt.slots)
            if b.fills and b.name != edge.input
        ]
        slots = [result if h is tile else h for h in step.slots] + extra
        steps[i] = Step(
            fused, slots, [*step.inputs, *extra], [result], gather=step.gather
        )
        steps[j] = None
        bindings = _rebind(step.op, fused, bindings)
        bindings = _rebind(nxt.op, fused, bindings)
    kept = [s for s in steps if s is not None]
    return dataclasses.replace(recording, steps=kept, bindings=bindings)
