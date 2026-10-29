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


def _bounds_match(a: Operator, b: Operator) -> bool:
    """Whether ``a`` and ``b`` are bound to the same per-call extent, or
    neither is bound at all: a fold then walks the same tiles this call,
    a prompt chunk's row count included (``bound_extents``, each operator's
    own per-call ``Binding`` already carries).
    """
    return set(a.bound_extents.values()) == set(b.bound_extents.values())


def _buffer_adjacent(recording: Recording) -> dict[int, tuple[str, str]]:
    """Index ``i``'s (producer's output operand name, consumer's input
    operand name) where step ``i``'s one output is read only by step
    ``i + 1``, never again, is not a graph output, feedback, pinned or
    resident buffer, and names its whole buffer; step ``i + 1`` has one
    output, and its matching input, and every other input it fills, do too,
    of the tile's element count and dtype; and the two operators are bound
    to the same per-call extent, or neither is (``_bounds_match``) -- a
    prompt chunk's own row count folds, its buffers walking it alike.
    Independent of any fold already taken: the buffer graph these read is
    the recording's own, unaffected by ``Operator.fold`` replacing an
    operator.
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

    found: dict[int, tuple[str, str]] = {}
    for i in range(len(recording.steps) - 1):
        step, nxt = recording.steps[i], recording.steps[i + 1]
        if not _bounds_match(step.op, nxt.op):
            continue
        # Handle-level shapes, not the (possibly unresolved) Operand's: a
        # Select()-shaped operand (GEMM's bfp16_b) needs its tunable
        # resolved before its own elements/dtype read.
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
        if len(matches) != 1 or matches[0][1].nbytes is not None:
            continue
        cbuf, _, _ = matches[0]
        if len([b for b in nxt.op.buffers if b.drains]) != 1:
            continue
        others = [
            (b, r, h)
            for b, r, h in zip(nxt.op.buffers, nxt.refs(), nxt.slots)
            if b.fills and b.name != cbuf.name
        ]
        if any(
            r.nbytes is not None or h.elements != tile.elements or h.dtype != tile.dtype
            for _, r, h in others
        ):
            continue
        found[i] = (buf.name, cbuf.name)
    return found


def _chain_from(
    recording: Recording, lo: int, buffer_adjacent: dict[int, tuple[str, str]]
) -> list[tuple[int, Operator, int]]:
    """The admissible chain folding into step ``lo``: each entry (the index
    folded in, the fused operator after it, the input its tile entered at),
    in order, stopping at the first hop the buffers (``buffer_adjacent``) or
    ``producer.fold(consumer, at)`` (``_admits``, where the channel budget,
    the shapes and dtypes, and a tile a later call reads are refused) does
    not admit.
    """
    chain: list[tuple[int, Operator, int]] = []
    current = recording.steps[lo].op
    k = lo
    while True:
        names = buffer_adjacent.get(k)
        if names is None:
            break
        _, in_name = names
        nxt = recording.steps[k + 1].op
        at = next((i for i, b in enumerate(nxt.inputs) if b.name == in_name), None)
        if at is None:
            break
        fused = _admits(current, nxt, at)
        if fused is None:
            break
        current = fused
        k += 1
        chain.append((k, current, at))
    return chain


def fold_candidates(recording: Recording) -> tuple[Fusion, ...]:
    """Every admissible fold of a run of two or more consecutive steps
    (``_chain_from``), overlapping ones included: a maximal chain from
    ``lo`` of length ``n`` admits every depth from 1 to ``n``, and a step
    that admits folding both its predecessor's output and feeding its
    successor's starts a chain of its own, found separately.
    """
    buffer_adjacent = _buffer_adjacent(recording)
    calls = Counter(id(s.op) for s in recording.steps)
    found = []
    for lo in range(len(recording.steps) - 1):
        if calls[id(recording.steps[lo].op)] != 1:
            continue
        chain = _chain_from(recording, lo, buffer_adjacent)
        for depth in range(1, len(chain) + 1):
            hi = chain[depth - 1][0]
            edges = tuple(
                Edge(i, buffer_adjacent[i][0], i + 1, buffer_adjacent[i][1])
                for i in range(lo, hi)
            )
            found.append(Fusion(FusionKind.FOLD, tuple(range(lo, hi + 1)), edges))
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
    overlapping) applied: a run's steps collapsed into one at its first's
    position, its operator ``Operator.fold``-ed in at each edge in turn,
    its slots the running operator's with each hop's other input appended,
    its output the run's last step's.

    Raises:
        ValueError: Two of ``folds`` share a step, or a hop no longer
            admits (its operator changed since ``fold_candidates`` ran).
    """
    taken: dict[int, Fusion] = {}
    for fusion in folds:
        if fusion.kind is not FusionKind.FOLD:
            raise ValueError(f"apply_folds: {fusion.kind.value} is not a fold")
        if list(fusion.steps) != list(range(fusion.steps[0], fusion.steps[-1] + 1)):
            raise ValueError(f"a fold's steps must be consecutive, not {fusion.steps}")
        for s in fusion.steps:
            if s in taken:
                raise ValueError(f"step {s} is folded twice")
            taken[s] = fusion
    steps: list[Step | None] = list(recording.steps)
    bindings = list(recording.bindings)
    for fusion in dict.fromkeys(taken.values()):
        lo = fusion.steps[0]
        start = recording.steps[lo]
        current = start.op
        (out_name,) = (b.name for b in current.buffers if b.drains)
        out_idx = next(k for k, b in enumerate(current.buffers) if b.name == out_name)
        slots = list(start.slots)
        inputs = list(start.inputs)
        result = None
        for edge in fusion.edges:
            nxt = recording.steps[edge.consumer]
            at = next(k for k, b in enumerate(nxt.op.inputs) if b.name == edge.input)
            fused = current.fold(nxt.op, at)
            if fused is None:
                raise ValueError(f"{fusion} no longer admits: {current!r} refuses it")
            current = fused
            (result_name,) = (b.name for b in nxt.op.buffers if b.drains)
            _, result = _handle_at(nxt, result_name)
            extra = [
                h
                for b, h in zip(nxt.op.buffers, nxt.slots)
                if b.fills and b.name != edge.input
            ]
            slots[out_idx] = result
            slots += extra
            inputs += extra
        steps[lo] = Step(current, slots, inputs, [result], gather=start.gather)
        for s in fusion.steps[1:]:
            steps[s] = None
        for s in fusion.steps:
            bindings = _rebind(recording.steps[s].op, current, bindings)
    kept = [s for s in steps if s is not None]
    return dataclasses.replace(recording, steps=kept, bindings=bindings)
