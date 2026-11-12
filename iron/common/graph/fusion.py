# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A recording's admissible fusions, and which a profile names."""

from __future__ import annotations

import dataclasses
from collections.abc import Sequence

from ..declare import Operator, Unresolvable
from ..declare.profile import Profile
from ..design import BuiltArray, OperatorDesign
from ..image.step import Edge, Fusion, FusionKind
from .record import Recording

# How a producer's output can feed a consumer's input, by the pair's
# OperatorDesign identities and buffer names: layers of one shape, repeated
# down a model, build once.
_built: dict[tuple[str, str, str, str], FusionKind | None] = {}


def admits(producer: Operator, output: str, consumer: Operator, input_: str) -> FusionKind | None:
    """Return how ``producer``'s resolved ``output`` can feed ``consumer``'s resolved ``input_`` on-chip.

    ``STREAM`` where the pair's ``BuiltArray``s build fed directly (``Operand.feed``'s
    checks pass), else ``STAGED`` where they build staged through memtiles; None where
    neither does. Whether it places is left to the widths its members run at fused,
    which a tuner chooses.
    """
    try:
        producer_design = OperatorDesign(producer)
        consumer_design = OperatorDesign(consumer)
    except TypeError:  # reference-only: no kernel, so no array to feed
        return None
    key = (producer_design.identity, output, consumer_design.identity, input_)
    if key in _built:
        return _built[key]
    found = None
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
        found = kind
        break
    _built[key] = found
    return found


def _hand_offs(recording: Recording, ops: list[Operator]) -> dict[str, tuple[int, str, dict[int, str]]]:
    """Each buffer root one step's output can hand on-chip to every reader that admits it.

    ``{root: (writer, output, {reader: input})}``; ``ops`` the steps' resolved
    operators, updated in place where a reader's tunable must flip to admit.
    """
    excluded = recording.held
    readers, writers = recording.users()
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
            chosen: dict[int, Operator] = {}
            for j in dict.fromkeys(reads):
                nxt = recording.steps[j]
                inputs = [(cbuf, cref) for cbuf, cref in zip(nxt.op.buffers, nxt.refs()) if cbuf.fills and cref.root == root]
                if len(inputs) != 1:
                    break
                ((cbuf, cref),) = inputs
                if cref.nbytes is not None or cbuf.replicate:
                    break
                reader = ops[j]
                if not cbuf.streamed:
                    flipped = []
                    for name in type(reader).declaration.tunables:
                        if not isinstance(vars(reader)[name], bool):
                            continue
                        try:
                            flipped.append(reader._with_tunables(**{name: not vars(reader)[name]}).resolved())
                        except ValueError:  # the flip does not resolve here
                            continue
                    reader = next(
                        (
                            v
                            for v in flipped
                            if next(b for b in v.buffers if b.name == cbuf.name).streamed and admits(ops[i], buf.name, v, cbuf.name) is not None
                        ),
                        None,
                    )
                    if reader is None:
                        break
                elif admits(ops[i], buf.name, reader, cbuf.name) is None:
                    break
                chosen[j] = reader
                fed[j] = cbuf.name
            else:
                for j, reader in chosen.items():
                    ops[j] = reader
                found[root] = (i, buf.name, fed)
    return found


def _stream_runs(recording: Recording) -> list[Fusion]:
    """Every window of 2 or more consecutive steps, no host step crossing it, that runs as one stream or staged fusion, ordered by first step then length."""
    resolved = [step.op.resolved() for step in recording.steps]
    hand_offs = _hand_offs(recording, resolved)
    uses = [step.roots() for step in recording.steps]
    found: list[Fusion] = []
    n = len(recording.steps)
    if not n:
        return found
    # A stream's steps all run at once, each on cores of its own: no window
    # holds more steps than the array has cores.
    dev = resolved[0].dev
    if dev is None:
        raise Unresolvable("a stream window's length needs a bound device")
    cores = dev.cols * len(dev.core_rows)
    for lo in range(n):
        for hi in range(lo + 1, min(lo + cores, n)):
            if recording.crosses_host(lo, hi):
                break
            window = range(lo, hi + 1)
            touched: dict[str, list[int]] = {}
            for s in window:
                for root in dict.fromkeys(uses[s][0] + uses[s][1]):
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
            staged = any(admits(ops[e.producer - lo], e.output, ops[e.consumer - lo], e.input) is FusionKind.STAGED for e in edges)
            kind = FusionKind.STAGED if staged else FusionKind.STREAM
            fusion = Fusion(kind, tuple(window), tuple(edges))
            found.append(fusion)
    return found


def _pack_conflicts(recording: Recording) -> set[tuple[int, int]]:
    """Index pairs ``(i, j)``, ``i < j``, whose steps are not independent: one writes a host buffer root the other reads or writes too."""
    uses = [step.roots() for step in recording.steps]
    reads = [set(r) for r, _ in uses]
    writes = [set(w) for _, w in uses]
    conflicts: set[tuple[int, int]] = set()
    for i in range(len(recording.steps)):
        for j in range(i + 1, len(recording.steps)):
            if writes[i] & (reads[j] | writes[j]) or writes[j] & reads[i]:
                conflicts.add((i, j))
    return conflicts


def _pack_runs(recording: Recording) -> list[Fusion]:
    """Every maximal run of consecutive, pairwise independent steps.

    ``_pack_conflicts``, no host step crossing it, and all of their contiguous
    sub-runs of 2+, overlapping ones included.
    """
    conflicts = _pack_conflicts(recording)
    n = len(recording.steps)
    found: list[Fusion] = []
    start = 0
    while start < n:
        end = start
        while end + 1 < n and not any((i, end + 1) in conflicts for i in range(start, end + 1)) and not recording.crosses_host(start, end + 1):
            end += 1
        if end > start:
            for lo in range(start, end + 1):
                for hi in range(lo + 1, end + 1):
                    found.append(Fusion(FusionKind.PACK, tuple(range(lo, hi + 1))))
            start = end + 1
        else:
            start += 1
    return found


def candidates(
    recording: Recording,
    kinds: Sequence[FusionKind] = (FusionKind.STREAM, FusionKind.STAGED),
) -> tuple[Fusion, ...]:
    """Return every admissible fusion of ``kinds`` (default the on-chip edge kinds, stream and staged).

    Stream and staged runs (``_stream_runs``) and pack runs (``_pack_runs``), ordered by
    first step then length. The tuner prices each and ``fusions`` picks among them. A
    merge is not one: it is what a packing runs as on an xclbin (``packing.merges``).
    """
    found: list[Fusion] = []
    if FusionKind.STREAM in kinds or FusionKind.STAGED in kinds:
        found.extend(f for f in _stream_runs(recording) if f.kind in kinds)
    if FusionKind.PACK in kinds:
        found.extend(_pack_runs(recording))
    return tuple(found)


_EVERY_KIND = (
    FusionKind.STREAM,
    FusionKind.STAGED,
    FusionKind.PACK,
)


def named(recording: Recording, profile: Profile, ordered: Sequence[Fusion]) -> tuple[Fusion, ...]:
    """Return the fusions of ``ordered`` that ``profile`` names (``Profile.fused``) in ``recording.version``, a step in at most one.

    The first of ``ordered`` wins; a stream or staged candidate is matched as it is or, failing
    that, phased (``Fusion.phased``), so a profile naming the phased form of an admissible
    window is honoured without ``candidates`` itself doubling every stream and staged run (which
    would otherwise reach IRON's own fusion search, ``tune.fusions.fusion_groups``, whose
    ``FusionGroup`` key does not carry ``phased`` and would double-count one occurrence).
    """
    found: list[Fusion] = []
    taken: set[int] = set()
    version = recording.version
    for fusion in ordered:
        if taken & set(fusion.steps):
            continue
        steps = [recording.steps[i].op.resolved() for i in fusion.steps]
        forms = (fusion, dataclasses.replace(fusion, phased=True)) if (fusion.kind in (FusionKind.STREAM, FusionKind.STAGED)) else (fusion,)
        form = next(
            (f for f in forms if profile.fused(f.kind, steps, f.local_edges, version, f.phased)),
            None,
        )
        if form is None:
            continue
        found.append(form)
        taken.update(form.steps)
    return tuple(found)


def fusions(recording: Recording, profile: Profile) -> tuple[Fusion, ...]:
    """Return ``candidates(recording, kinds)`` of every kind that ``profile`` names, a step in at most one fusion (``named``).

    First in step order wins: the earliest first step, at a tie a stream or staged run
    before a pack, then the shorter.
    """
    return named(
        recording,
        profile,
        sorted(candidates(recording, _EVERY_KIND), key=lambda f: f.steps[0]),
    )
