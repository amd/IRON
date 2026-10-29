# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A recording's admissible on-chip chains, and which a profile names."""

from __future__ import annotations

from ..declare import Operator
from ..declare.profile import Profile
from ..design import BuiltArray, OperatorDesign
from ..image.step import Chain
from .record import Recording

# Whether a producer's output can feed a consumer's input, by the pair's
# OperatorDesign identities and buffer names: layers of one shape, repeated
# down a model, build once.
_built: dict[tuple[str, str, str, str], bool] = {}


def _admits(producer: Operator, output: str, consumer: Operator, input_: str) -> bool:
    """Whether ``producer``'s resolved ``output`` can feed ``consumer``'s resolved
    ``input_`` on-chip: ``Operand.feed``'s checks pass and the pair's
    ``BuiltArray``s actually build.
    """
    try:
        producer_design = OperatorDesign(producer)
        consumer_design = OperatorDesign(consumer)
    except TypeError:  # reference-only: no kernel, so no array to feed
        return False
    key = (producer_design.identity, output, consumer_design.identity, input_)
    if key not in _built:
        try:
            producer_array = BuiltArray(producer_design)
            (source,) = (b for b in producer_array.op.buffers if b.name == output)
            BuiltArray(consumer_design, fed={input_: source})
            _built[key] = True
        except ValueError:
            _built[key] = False
    return _built[key]


def candidates(recording: Recording) -> tuple[Chain, ...]:
    """Every admissible producer -> consumer edge of ``recording``, in step
    order: a pair ``Operand.feed`` could run fused on-chip. Edges may overlap
    (a step both a producer and the next edge's consumer, as a run of chained
    steps does); the tuner prices each and ``chains`` picks among them.

    Admissible: adjacent steps whose producer's drained output is read by the
    consumer alone, nowhere else and never again, and is not a graph output,
    feedback, pinned or resident buffer; both name the whole buffer; the
    producer's buffer is a streamed output and the consumer's a streamed,
    non-``replicate`` input; and the pair's resolved designs actually build
    fused (``_admits``), which is where ``Operand.feed``'s own checks (lane
    counts, ``obj_type``, and a matching host access order per lane) are run.
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
            if not _admits(producer, buf.name, consumer, cbuf.name):
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
