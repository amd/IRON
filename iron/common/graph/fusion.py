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

# How a producer's output can feed a consumer's input, by the pair's
# OperatorDesign identities and buffer names: layers of one shape, repeated
# down a model, build once.
_built: dict[tuple[str, str, str, str], FusionKind | None] = {}


def _admits(
    producer: Operator, output: str, consumer: Operator, input_: str
) -> FusionKind | None:
    """How ``producer``'s resolved ``output`` can feed ``consumer``'s resolved
    ``input_`` on-chip: ``STREAM`` where the pair's ``BuiltArray``s build fed
    directly (``Operand.feed``'s checks pass), else ``STAGED`` where they build
    staged through memtiles and the pair places so (``fits``); None where
    neither does.
    """
    try:
        producer_design = OperatorDesign(producer)
        consumer_design = OperatorDesign(consumer)
    except TypeError:  # reference-only: no kernel, so no array to feed
        return None
    key = (producer_design.identity, output, consumer_design.identity, input_)
    if key in _built:
        return _built[key]
    _built[key] = None
    for kind in (FusionKind.STREAM, FusionKind.STAGED):
        try:
            producer_array = BuiltArray(producer_design)
            (source,) = (b for b in producer_array.op.buffers if b.name == output)
            BuiltArray(
                consumer_design,
                fed={input_: source},
                staged=kind is FusionKind.STAGED,
            )
        except ValueError:
            continue
        pair = Fusion(kind, (0, 1), (Edge(0, output, 1, input_),))
        designs = {"0": producer_design, "1": consumer_design}
        if kind is FusionKind.STREAM or fits(designs, fusion=pair) is None:
            _built[key] = kind
        break
    return _built[key]


# Bounds a stream window's length: each start tries every window up to it.
_STREAM_MAX_RUN = 8

_placed: dict[tuple, bool] = {}


def _hand_offs(
    recording: Recording, ops: Sequence[Operator]
) -> dict[str, tuple[int, str, dict[int, str]]]:
    """Each buffer root one step's output can hand on-chip to every step that
    reads it, ``ops`` the steps' resolved operators: ``(writer, output,
    {reader: input})``. The output is a streamed drain of the whole root,
    which only that step writes and is not a graph output, feedback, pinned
    or resident buffer; each reader comes later and reads the whole root
    through one streamed, non-``replicate`` input, no host step reads it,
    and every reader's edge admits (``_admits``).
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

    found: dict[str, tuple[int, str, dict[int, str]]] = {}
    for i, step in enumerate(recording.steps):
        for buf, ref in zip(step.op.buffers, step.refs()):
            root = ref.root
            if not buf.drains or not buf.streamed or ref.nbytes is not None:
                continue
            if root in excluded or writers.get(root) != [i]:
                continue
            reads = readers.get(root, [])
            if not reads or min(reads) <= i:
                continue
            fed: dict[int, str] = {}
            for j in dict.fromkeys(reads):
                nxt = recording.steps[j]
                inputs = [
                    (cbuf, cref)
                    for cbuf, cref in zip(nxt.op.buffers, nxt.refs())
                    if cbuf.fills and cref.root == root
                ]
                if len(inputs) != 1:
                    break
                ((cbuf, cref),) = inputs
                if cref.nbytes is not None or not cbuf.streamed or cbuf.replicate:
                    break
                if _admits(ops[i], buf.name, ops[j], cbuf.name) is None:
                    break
                fed[j] = cbuf.name
            else:
                found[root] = (i, buf.name, fed)
    return found


def _stream_runs(recording: Recording) -> list[Fusion]:
    """Every window of 2 to ``_STREAM_MAX_RUN`` consecutive steps, no host step
    crossing it, that runs as one stream or staged fusion: each root two of
    its steps share, one writing, is a hand-off (``_hand_offs``) whose writer
    and every reader are in it, an edge each; every step is on an edge. The
    fusion is staged where an edge admits only staged; one fanning out, or
    staged, must place (``fits``). Ordered by first step, then by length.
    """
    resolved = [step.op.resolved() for step in recording.steps]
    hand_offs = _hand_offs(recording, resolved)
    uses: list[tuple[set[str], set[str]]] = []
    for step in recording.steps:
        reads, writes = set(), set()
        for buf, ref in zip(step.op.buffers, step.refs()):
            if buf.fills:
                reads.add(ref.root)
            if buf.drains:
                writes.add(ref.root)
        uses.append((reads, writes))
    found: list[Fusion] = []
    n = len(recording.steps)
    for lo in range(n):
        for hi in range(lo + 1, min(lo + _STREAM_MAX_RUN, n)):
            if _crosses_host(recording, lo, hi):
                break
            window = range(lo, hi + 1)
            touched: dict[str, list[int]] = {}
            for s in window:
                for root in uses[s][0] | uses[s][1]:
                    touched.setdefault(root, []).append(s)
            edges: list[Edge] = []
            valid = True
            for root, steps in touched.items():
                if len(steps) < 2 or not any(root in uses[s][1] for s in steps):
                    continue
                if root not in hand_offs:
                    valid = False
                    break
                writer, output, fed = hand_offs[root]
                if set(steps) != {writer, *fed}:
                    valid = False
                    break
                edges.extend(Edge(writer, output, j, fed[j]) for j in sorted(fed))
            on_edge = {e.producer for e in edges} | {e.consumer for e in edges}
            if not valid or set(window) != on_edge:
                continue
            edges.sort(key=lambda e: (e.producer, e.consumer))
            ops = resolved[lo : hi + 1]
            staged = any(
                _admits(ops[e.producer - lo], e.output, ops[e.consumer - lo], e.input)
                is FusionKind.STAGED
                for e in edges
            )
            kind = FusionKind.STAGED if staged else FusionKind.STREAM
            fusion = Fusion(kind, tuple(window), tuple(edges))
            fans = len(edges) > len({(e.producer, e.output) for e in edges})
            if (staged or fans) and not _fused_fits(fusion, ops, lo):
                continue
            found.append(fusion)
    return found


def _fused_fits(fusion: Fusion, ops: Sequence[Operator], lo: int) -> bool:
    """Whether ``fusion``, over ``ops`` (its steps' resolved operators, the
    first at step ``lo``), places and allocates built fused (``fits``),
    cached by its designs and wiring.
    """
    designs = [OperatorDesign(op) for op in ops]
    local = Fusion(
        fusion.kind,
        tuple(s - lo for s in fusion.steps),
        tuple(
            Edge(e.producer - lo, e.output, e.consumer - lo, e.input)
            for e in fusion.edges
        ),
    )
    key = (local, tuple(d.identity for d in designs))
    if key not in _placed:
        named = {str(i): d for i, d in enumerate(designs)}
        _placed[key] = fits(named, fusion=local) is None
    return _placed[key]


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
    recording: Recording,
    kinds: Sequence[FusionKind] = (FusionKind.STREAM, FusionKind.STAGED),
) -> tuple[Fusion, ...]:
    """Every admissible fusion of ``kinds`` (default the on-chip edge kinds,
    stream and staged, what every caller but ``fusions`` asks for): stream
    and staged runs (``_stream_runs``), pack runs (``_pack_runs``) and merge
    runs (``_merge_runs``), each ordered by first step, then by length. The
    tuner prices each and ``fusions`` picks among them.
    """
    found: list[Fusion] = []
    if FusionKind.STREAM in kinds or FusionKind.STAGED in kinds:
        found.extend(f for f in _stream_runs(recording) if f.kind in kinds)
    if FusionKind.PACK in kinds:
        found.extend(_pack_runs(recording))
    if FusionKind.MERGE in kinds:
        found.extend(_merge_runs(recording))
    return tuple(found)


_EVERY_KIND = (
    FusionKind.STREAM,
    FusionKind.STAGED,
    FusionKind.PACK,
    FusionKind.MERGE,
)


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
