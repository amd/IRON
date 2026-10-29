# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A recording's admissible fusions, and which a profile names."""

from __future__ import annotations

from collections.abc import Sequence

from ..declare import Operator
from ..declare.profile import Profile
from ..design import BuiltArray, OperatorDesign
from ..image.compose import fits
from ..image.step import Edge, Fusion, FusionKind
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


def _adjacent(recording: Recording) -> dict[int, tuple[str, str]]:
    """Index ``i`` admissible to feed step ``i + 1`` on-chip: its ``(output,
    input)`` buffer names, the first found, where step ``i``'s drained
    output is read by step ``i + 1`` alone, nowhere else and never again,
    and is not a graph output, feedback, pinned or resident buffer; both
    name the whole buffer; the producer's buffer is a streamed output and
    the consumer's a streamed, non-``replicate`` input; and the pair's
    resolved designs actually build fused (``_admits``), which is where
    ``Operand.feed``'s own checks (lane counts, ``obj_type``, and a matching
    host access order per lane) are run.
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

    found: dict[int, tuple[str, str]] = {}
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
            found[i] = (buf.name, cbuf.name)
            break
    return found


def _stream_runs(recording: Recording) -> list[Fusion]:
    """Every admissible stream fusion of 2+ consecutive steps of
    ``recording``: the longest admissible runs (``_adjacent``) and all of
    their contiguous sub-runs, overlapping ones included, ordered by first
    step, then by length.
    """
    adjacent = _adjacent(recording)
    found: list[Fusion] = []
    n = len(recording.steps)
    start = 0
    while start < n:
        end = start
        while end in adjacent:
            end += 1
        if end > start:
            for lo in range(start, end + 1):
                for hi in range(lo + 1, end + 1):
                    steps = tuple(range(lo, hi + 1))
                    edges = tuple(
                        Edge(i, adjacent[i][0], i + 1, adjacent[i][1])
                        for i in range(lo, hi)
                    )
                    found.append(Fusion(FusionKind.STREAM, steps, edges))
            start = end + 1
        else:
            start += 1
    return found


def _crosses_host(recording: Recording, lo: int, hi: int) -> bool:
    """Whether a host step runs between steps ``lo`` and ``hi`` (inclusive):
    host code the model's own graph runs between two device dispatches,
    which neither packing concurrently nor merging back to back may skip
    past.
    """
    return any(lo < s.at <= hi for s in recording.host)


def _pack_conflicts(recording: Recording) -> set[tuple[int, int]]:
    """Index pairs ``(i, j)``, ``i < j``, whose steps are not independent:
    one writes a host buffer root the other reads or writes too (root-level,
    so a byte-range part of a buffer stands for the whole of it).
    """
    reads: list[set[str]] = []
    writes: list[set[str]] = []
    for step in recording.steps:
        r, w = set(), set()
        for buf, ref in zip(step.op.buffers, step.refs()):
            if buf.fills:
                r.add(ref.root)
            if buf.drains:
                w.add(ref.root)
        reads.append(r)
        writes.append(w)
    conflicts: set[tuple[int, int]] = set()
    for i in range(len(recording.steps)):
        for j in range(i + 1, len(recording.steps)):
            if writes[i] & (reads[j] | writes[j]) or writes[j] & reads[i]:
                conflicts.add((i, j))
    return conflicts


def _pack_runs(recording: Recording) -> list[Fusion]:
    """Every maximal run of consecutive, pairwise independent steps
    (``_pack_conflicts``, no host step crossing it) and all of their
    contiguous sub-runs of 2+, overlapping ones included.
    """
    conflicts = _pack_conflicts(recording)
    n = len(recording.steps)
    found: list[Fusion] = []
    start = 0
    while start < n:
        end = start
        while (
            end + 1 < n
            and not any((i, end + 1) in conflicts for i in range(start, end + 1))
            and not _crosses_host(recording, start, end + 1)
        ):
            end += 1
        if end > start:
            for lo in range(start, end + 1):
                for hi in range(lo + 1, end + 1):
                    found.append(Fusion(FusionKind.PACK, tuple(range(lo, hi + 1))))
            start = end + 1
        else:
            start += 1
    return found


# Bounds merge's window enumeration: each window past the first needs its own
# fits() (an MLIR placement pass), and the reconfigure a merge saves is one
# regardless of how many steps share it, so a handful is where the search
# stops paying for itself.
_MERGE_MAX_RUN = 4

_coresident: dict[tuple[str, ...], bool] = {}


def _co_fits(designs: Sequence[OperatorDesign]) -> bool:
    """Whether ``designs`` place and allocate in one device configuration
    (``fits``), cached by their identities: a shape repeated down a model
    checks once.
    """
    key = tuple(d.identity for d in designs)
    if key not in _coresident:
        _coresident[key] = fits({str(i): d for i, d in enumerate(designs)}) is None
    return _coresident[key]


def _merge_runs(recording: Recording) -> list[Fusion]:
    """Every consecutive run of 2 to ``_MERGE_MAX_RUN`` steps, no host step
    crossing it (``_crosses_host``), whose designs co-fit (``_co_fits``),
    overlapping ones included. A longer run only adds designs to place, so
    the first window from a start that does not fit ends the search there.
    """
    n = len(recording.steps)
    found: list[Fusion] = []
    for lo in range(n):
        designs: list[OperatorDesign] = []
        for hi in range(lo, min(lo + _MERGE_MAX_RUN, n)):
            if _crosses_host(recording, lo, hi):
                break
            try:
                designs.append(OperatorDesign(recording.steps[hi].op.resolved()))
            except TypeError:  # reference-only: no kernel, so no array to place
                break
            if len(designs) < 2:
                continue
            if not _co_fits(designs):
                break
            found.append(Fusion(FusionKind.MERGE, tuple(range(lo, hi + 1))))
    return found


def candidates(
    recording: Recording, kinds: Sequence[FusionKind] = (FusionKind.STREAM,)
) -> tuple[Fusion, ...]:
    """Every admissible fusion of ``kinds`` (default the stream kind alone,
    what every caller but ``fusions`` asks for): stream runs
    (``_stream_runs``), pack runs (``_pack_runs``) and merge runs
    (``_merge_runs``), each ordered by first step, then by length. The tuner
    prices each and ``fusions`` picks among them.
    """
    found: list[Fusion] = []
    if FusionKind.STREAM in kinds:
        found.extend(_stream_runs(recording))
    if FusionKind.PACK in kinds:
        found.extend(_pack_runs(recording))
    if FusionKind.MERGE in kinds:
        found.extend(_merge_runs(recording))
    return tuple(found)


_EVERY_KIND = (FusionKind.STREAM, FusionKind.PACK, FusionKind.MERGE)


def fusions(recording: Recording, profile: Profile) -> tuple[Fusion, ...]:
    """``candidates(recording, kinds)`` of every kind that ``profile`` names
    (``Profile.fused``), a step in at most one fusion: first in step order
    wins.
    """
    found: list[Fusion] = []
    taken: set[int] = set()
    for fusion in candidates(recording, _EVERY_KIND):
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
