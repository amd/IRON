# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A recording's admissible on-chip chains, and which a profile names."""

from __future__ import annotations

from ..declare.profile import Profile
from ..elementwise import Elementwise
from ..image.step import Chain
from .record import Recording


def candidates(recording: Recording) -> tuple[Chain, ...]:
    """Every admissible producer -> consumer edge of ``recording``, in step
    order: a pair ``Operand.feed`` could run fused on-chip. Edges may overlap
    (a step both a producer and the next edge's consumer, as a run of chained
    steps does); the tuner prices each and ``chains`` picks among them.

    Admissible: adjacent steps whose producer's drained output is read by the
    consumer alone, nowhere else and never again, and is not a graph output,
    feedback, pinned or resident buffer; both name the whole buffer; the
    producer's buffer is a streamed output and the consumer's a streamed,
    non-``replicate`` input; both operators resolve to ``Elementwise``, with
    no ``sequence()`` override; and their ``layout()`` buffers agree in lanes
    and ``obj_type``, as ``Operand.feed`` requires.
    """
    excluded = (
        {h.name for h in recording.outputs}
        | set(recording.feedback)
        | set(recording.pinned)
        | set(recording.residents)
    )
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

    found: list[Chain] = []
    for i in range(len(recording.steps) - 1):
        step, nxt = recording.steps[i], recording.steps[i + 1]
        producer, consumer = step.op.resolved(), nxt.op.resolved()
        if not (
            isinstance(producer, Elementwise) and isinstance(consumer, Elementwise)
        ):
            continue
        if producer.has_sequence_override() or consumer.has_sequence_override():
            continue
        for buf, ref in zip(step.op.buffers, step.refs()):
            if not buf.drains or ref.nbytes is not None or ref.root in excluded:
                continue
            if readers.get(ref.root) != [i + 1] or writers.get(ref.root) != [i]:
                continue
            match = next(
                (
                    (cbuf, cref)
                    for cbuf, cref in zip(nxt.op.buffers, nxt.refs())
                    if cbuf.fills and cref.root == ref.root and cref.nbytes is None
                ),
                None,
            )
            if match is None:
                continue
            cbuf, _ = match
            if not (buf.streamed and cbuf.streamed) or cbuf.replicate:
                continue
            src = next(b for b in producer.layout().buffers if b.name == buf.name)
            dst = next(b for b in consumer.layout().buffers if b.name == cbuf.name)
            if src.lanes != dst.lanes or src.obj_type != dst.obj_type:
                continue
            found.append(Chain(i, buf.name, cbuf.name))
            break
    return tuple(found)


def chains(recording: Recording, profile: Profile) -> tuple[Chain, ...]:
    """``candidates(recording)`` that ``profile`` names (``Profile.chained``),
    a step in at most one: first in step order wins.
    """
    found: list[Chain] = []
    taken: set[int] = set()
    for edge in candidates(recording):
        if edge.producer in taken or edge.producer + 1 in taken:
            continue
        producer = recording.steps[edge.producer].op.resolved()
        consumer = recording.steps[edge.producer + 1].op.resolved()
        if not profile.chained(producer, consumer, edge.input):
            continue
        found.append(edge)
        taken.update((edge.producer, edge.producer + 1))
    return tuple(found)
