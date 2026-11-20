# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A recording's admissible fusions, and which a profile names."""

from __future__ import annotations

import dataclasses
import itertools
from collections.abc import Sequence
from typing import Any

from ..declare import Operator, Unresolvable
from ..declare.composition import (
    Configuration,
    Member,
    Region,
    RuntimePlan,
    Schedule,
    Switch,
)
from ..declare.profile import Profile
from ..design import BuiltArray, OperatorDesign
from ..image.step import Edge, EdgeKind, Fusion, FusionKind
from .record import Recording

# How a producer's output can feed a consumer's input, by the pair's
# OperatorDesign identities and buffer names: layers of one shape, repeated
# down a model, build once.
_built: dict[tuple[str, str, str, str], FusionKind | None] = {}


def admits(
    producer: Operator, output: str, consumer: Operator, input_: str
) -> FusionKind | None:
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


def _hand_offs(
    recording: Recording, ops: list[Operator]
) -> dict[str, tuple[int, str, dict[int, str]]]:
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
                inputs = [
                    (cbuf, cref)
                    for cbuf, cref in zip(nxt.op.buffers, nxt.refs())
                    if cbuf.fills and cref.root == root
                ]
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
                            flipped.append(
                                reader._with_tunables(
                                    **{name: not vars(reader)[name]}
                                ).resolved()
                            )
                        except ValueError:  # the flip does not resolve here
                            continue
                    reader = next(
                        (
                            v
                            for v in flipped
                            if next(
                                b for b in v.buffers if b.name == cbuf.name
                            ).streamed
                            and admits(ops[i], buf.name, v, cbuf.name) is not None
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
    """Every window of 2 or more consecutive steps, no host step crossing it, that runs as one stream or staged fusion, ordered by first step then length.

    At least one on-chip hand-off, not every member on one: a member no edge touches may
    still be in the window, independent of its neighbours (``_validate_fusions`` holds it
    at build).
    """
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
            # A member the edges never touch rides beside the chain: _validate_fusions
            # holds it independent of every other member at build, the same way a
            # pack's members are, since nothing here records why it is safe.
            if not valid or not edges:
                continue
            edges.sort(key=lambda e: (e.producer, e.consumer))
            ops = resolved[lo : hi + 1]
            staged = any(
                admits(ops[e.producer - lo], e.output, ops[e.consumer - lo], e.input)
                is FusionKind.STAGED
                for e in edges
            )
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


def memory_waits(
    recording: Recording, match: Sequence[int], edges: Sequence[Edge]
) -> tuple[tuple[int, int], ...]:
    """Each pair of a region's steps that depend through host memory with no edge between them.

    Two steps depend where one writes a host buffer root the other reads or
    writes too. With no edge of the region joining them, the later in
    recorded order runs a phase after the earlier (``Fusion.waits``), so a
    reader sees the write landed and a writer does not overwrite what is
    still to be read.

    Args:
        recording: The recording ``match`` is a match in.
        match: The region's steps, as indices into ``recording.steps``.
        edges: The region's edges, indexing ``match``.

    Returns:
        Each such pair ``(earlier, later)``, as indices into ``recording.steps``.
    """
    joined = {(match[e.producer], match[e.consumer]) for e in edges}
    uses = {s: recording.steps[s].roots() for s in match}
    return tuple(
        (a, b)
        for a, b in itertools.combinations(sorted(match), 2)
        if (a, b) not in joined
        and (
            set(uses[a][1]) & {*uses[b][0], *uses[b][1]}
            or set(uses[b][1]) & set(uses[a][0])
        )
    )


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
        while (
            end + 1 < n
            and not any((i, end + 1) in conflicts for i in range(start, end + 1))
            and not recording.crosses_host(start, end + 1)
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


def named(
    recording: Recording, profile: Profile, ordered: Sequence[Fusion]
) -> tuple[Fusion, ...]:
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
        forms = (
            (fusion, dataclasses.replace(fusion, phased=True))
            if (fusion.kind in (FusionKind.STREAM, FusionKind.STAGED))
            else (fusion,)
        )
        form = next(
            (
                f
                for f in forms
                if profile.fused(f.kind, steps, f.local_edges, version, f.phased)
            ),
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


def composed(
    recording: Recording, profile: Profile
) -> tuple[dict[int, dict[str, Any]], tuple[Fusion, ...]]:
    """Return what ``profile``'s composition entries build in ``recording``: each step's tunables, by index, and each region of two or more steps as a fusion.

    At every match (``Recording.occurrences``) of a region of steps, the
    first entry naming a step wins. A member's tunables are its step's, the
    first entry naming each one winning. A
    region of consecutive steps runs as one stream or staged fusion where
    its on-chip edges are all streams, as one staged fusion where any is
    staged (its stream edges fed as they are), and as a pack where it has no
    edge and no two of its steps depend. A DDR edge's consumer reads what its
    producer wrote to host memory a phase or more later (a phased fusion,
    ``Fusion.waits``), and so does the later of two steps that depend
    through host memory with no edge between them (``memory_waits``). A cascade
    edge carries its producer's output to its consumer's core over the
    cascade (``Operand.cascade_to``). Chosen phases run each step in its in-edges'
    phase (``Fusion.phases``). An edge across calls (``Edge.across_calls``)
    held in DDR is the recording's own carry of the buffer it names, read by
    the next call from host memory, so it adds nothing to the fusion.

    A configuration of steps gives each its member's tunables; which
    designs it loads together is the packing's (``packing.configured``). The
    steps of the configurations concurrent under one id, at every match, run
    at once as one pack where they are consecutive and no region holds them.

    Raises:
        NotImplementedError: What the composer does not build yet: a
            profile's schedules beyond their packaging, calls a command
            (``Recording.repeated``), merged calls (``Recording.merged``) and
            commands in flight (the host's, ``CarriedLoop``), variants,
            bindings or
            state layouts, steps run at once that are not consecutive, a
            configuration at a partial width, keeping buffers resident, switched other than by a
            reload or holding regions, a runtime plan other than one task
            group, chosen phases a fusion's demands do not meet
            (``compose.phases``, at build), or an entry rooted at a step,
            with nested regions, inflows, shared workers, fission, an edge
            across calls held on chip (the carry resident between calls),
            cascades beside staged or DDR edges, a DDR
            edge's chosen depth, matching steps that are not consecutive, or
            an edge the composer does not build as its kind (``admits``). An edge out of a buffer steps past
            the region, a DDR edge or the host also read keeps its drain to
            host (a tee, ``Fusion.kept``).
        ValueError: An edge across calls names a buffer the recording does
            not carry, or one other than its consumer reads.
    """
    for kind, kept in (
        (
            "schedules beyond their packaging, calls a command, merged calls "
            "and commands in flight",
            [
                s
                for s in profile.schedules()
                if dataclasses.replace(
                    s,
                    packaging=None,
                    commands_in_flight=1,
                    calls_per_command=1,
                    size=None,
                )
                != Schedule(s.version)
            ],
        ),
        ("variants", profile.variants()),
        ("bindings", profile.bindings()),
        ("state layouts", profile.state_layouts()),
    ):
        if kept:
            raise NotImplementedError(f"building a profile's {kind} is not built yet")
    tunables: dict[int, dict[str, Any]] = {}
    fused: list[Fusion] = []
    taken: set[int] = set()
    readers, _ = recording.users()
    # The steps of the configurations concurrent under each id, run as one pack.
    at_once: dict[int, set[int]] = {}
    for entry in profile.entries():
        root = entry.root
        if isinstance(root, Configuration):
            unbuilt = [
                what
                for what, kept in (
                    ("a partial width", root.columns is not None),
                    ("buffers resident into the next", root.resident),
                    (
                        "a switch other than a reload",
                        root.switch not in (None, Switch.RELOAD),
                    ),
                    (
                        "regions among its parts",
                        not all(isinstance(p, Member) for p in root.parts),
                    ),
                )
                if kept
            ]
            if unbuilt:
                raise NotImplementedError(
                    f"building {entry} is not built yet: a configuration with "
                    f"{unbuilt[0]}"
                )
            for match in recording.occurrences(entry):
                for s, m in zip(match, root.steps()):
                    for name, value in (m.tunables or {}).items():
                        tunables.setdefault(s, {}).setdefault(name, value)
                if root.concurrent is not None:
                    at_once.setdefault(root.concurrent, set()).update(match)
            continue
        if (
            not isinstance(root, Region)
            or not all(isinstance(part, Member) for part in root.parts)
            or root.inflows
            or any(m.part is not None for m in root.steps())
        ):
            raise NotImplementedError(
                f"building {entry} is not built yet: the composer builds a "
                f"region of steps with no inflow"
            )
        across = [e for e in root.edges if e.across_calls]
        resident = [e for e in across if e.kind is not EdgeKind.DDR]
        if resident:
            raise NotImplementedError(
                f"building {entry} is not built yet: {resident[0]} holds what one "
                f"call carries to the next on chip, resident between calls"
            )
        within = [e for e in root.edges if not e.across_calls]
        kinds = {e.kind for e in within}
        chosen = root.step_phases()
        phased = any(e.kind is EdgeKind.DDR for e in within) or chosen is not None
        plan = root.runtime or RuntimePlan()
        # One task group: every task issued at once, then each awaited. In one
        # phase a barrier and per-channel awaits are the same awaits.
        unbuilt = [
            what
            for what, kept in (
                (
                    "per-channel awaits between phases",
                    plan.waits == "per_channel" and phased,
                ),
                (f"{plan.overlap} overlap", plan.overlap != "none"),
                (f"{plan.chunks} chunks", plan.chunks != 1),
                ("a chosen count of tasks in flight", plan.in_flight is not None),
                ("chained buffer descriptors", plan.chained),
                ("a chosen burst length", plan.burst is not None),
                ("a chosen transfer size", plan.transfer_bytes is not None),
            )
            if kept
        ]
        if unbuilt:
            raise NotImplementedError(
                f"building {entry} is not built yet: a runtime plan with "
                f"{unbuilt[0]}"
            )
        if root.workers and kinds - {EdgeKind.STREAM, EdgeKind.CASCADE}:
            raise NotImplementedError(
                f"building {entry} is not built yet: steps on one core joined "
                f"by edges other than streams and cascades"
            )
        if EdgeKind.CASCADE in kinds and kinds - {EdgeKind.STREAM, EdgeKind.CASCADE}:
            raise NotImplementedError(
                f"building {entry} is not built yet: cascades beside staged or "
                f"DDR edges"
            )
        if any(e.kind is EdgeKind.DDR and e.depth is not None for e in root.edges):
            raise NotImplementedError(
                f"building {entry} is not built yet: a DDR edge's chosen depth"
            )
        on_chip = [e for e in within if e.kind is not EdgeKind.DDR]
        through_memory = [e for e in within if e.kind is EdgeKind.DDR]
        carried = set(recording.feedback) | {
            h.ref().root for _, h in recording.states.values()
        }
        for match in recording.occurrences(entry):
            if taken & set(match):
                continue
            if len(match) > 1 and match != tuple(range(match[0], match[-1] + 1)):
                raise NotImplementedError(
                    f"building a region of steps {match}, which are not "
                    f"consecutive, is not built yet"
                )
            # Held in host memory, a carry across calls is the recording's own
            # round trip of a carried buffer: the step reads what the call
            # before wrote, as it does with no edge.
            for e in across:
                made, read = (
                    {
                        ref.root
                        for ref, b in zip(step.refs(), step.op.buffers)
                        if b.name == name
                    }
                    for step, name in (
                        (recording.steps[match[e.producer]], e.output),
                        (recording.steps[match[e.consumer]], e.input),
                    )
                )
                if made != read or not made <= carried:
                    raise ValueError(
                        f"{e} carries {sorted(made)} into the next call, which "
                        f"reads {sorted(read)}: a carry across calls is a buffer "
                        f"the recording carries, read where it was written"
                    )
            ordered = memory_waits(recording, match, root.edges)
            kept: list[tuple[int, str]] = []
            for e in on_chip:
                made = recording.steps[match[e.producer]]
                (root_name,) = {
                    ref.root
                    for ref, b in zip(made.refs(), made.op.buffers)
                    if b.name == e.output
                }
                if (
                    set(readers.get(root_name, [])) - set(match)
                    or root_name in recording.held
                    or any(
                        (d.producer, d.output) == (e.producer, e.output)
                        for d in through_memory
                    )
                ) and (match[e.producer], e.output) not in kept:
                    kept.append((match[e.producer], e.output))
                p, c = (
                    recording.steps[match[i]].op.resolved()
                    for i in (e.producer, e.consumer)
                )
                built = admits(p, e.output, c, e.input)
                if built is None or (
                    e.kind in (EdgeKind.STREAM, EdgeKind.CASCADE)
                    and built is not FusionKind.STREAM
                ):
                    raise NotImplementedError(
                        f"building {type(p).__name__}.{e.output} -> "
                        f"{type(c).__name__}.{e.input} as a {e.kind.value} edge is "
                        f"not built yet: the composer builds it "
                        + ("neither way" if built is None else f"only {built.value}")
                    )
            # The first entry naming a step's tunable wins, as for its region.
            for s, m in zip(match, root.parts):
                for name, value in (m.tunables or {}).items():
                    tunables.setdefault(s, {}).setdefault(name, value)
            if len(match) > 1:
                fused.append(
                    Fusion(
                        (
                            (
                                FusionKind.STAGED
                                if EdgeKind.STAGED in kinds
                                else FusionKind.STREAM
                            )
                            if kinds or ordered
                            else FusionKind.PACK
                        ),
                        match,
                        tuple(
                            Edge(
                                match[e.producer],
                                e.output,
                                match[e.consumer],
                                e.input,
                                kind=(
                                    EdgeKind.CASCADE
                                    if e.kind is EdgeKind.CASCADE
                                    else EdgeKind.STREAM
                                ),
                                depth=e.depth,
                            )
                            for e in on_chip
                        ),
                        phased=phased or bool(ordered),
                        kept=tuple(kept),
                        waits=(
                            *(
                                (match[e.producer], match[e.consumer])
                                for e in through_memory
                            ),
                            *ordered,
                        ),
                        workers=tuple(
                            tuple(match[i] for i in group) for group in root.workers
                        ),
                        phases=chosen,
                    )
                )
                taken.update(match)
    for group, together in at_once.items():
        steps = tuple(sorted(together))
        if len(steps) < 2 or taken & together:
            continue
        if steps != tuple(range(steps[0], steps[-1] + 1)):
            raise NotImplementedError(
                f"building steps {steps} at once (configurations concurrent as "
                f"{group}), which are not consecutive, is not built yet"
            )
        fused.append(Fusion(FusionKind.PACK, steps))
        taken.update(steps)
    return tunables, tuple(fused)
