# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""The tuner as one search over compositions.

Each takes a graph's calls (``Timed``, every version) rather than one
recording. ``candidates`` yields every edit the calls admit, of every kind;
``fit`` refuses an edit
that cannot fit before any build (counts from the target model, then the
dataflow analysis, then the placer); ``check`` holds a built edit to the
untuned build (bit identity, or no input worse against the operators'
references); ``measure`` times a profile against another in pairs;
``search`` starts from the shipped profile, prices each edit in place
against the incumbent, and keeps the set that gains most.
"""

from __future__ import annotations

import dataclasses
import logging
import time
from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from typing import Literal, Protocol

import numpy as np
from aie import ir
from aie.dialects.aie import get_target_model
from aie.iron.device import Device
from aie.utils import set_current_device

from ..common.declare import Profile
from ..common.declare.composition import Entry, Member, Refinement, Region
from ..common.graph.fusion import composed
from ..common.graph.sdf import Derivation
from ..common.image.step import Edge, EdgeKind, FusionKind, HandOff
from .autotune import Timed, refusal, settings
from .fusions import (
    Applied,
    Compared,
    NotBitIdentical,
    compare_graphs,
    group_fit_verdict,
)
from .measure import Timing


class Edit(Protocol):
    """One candidate change to a profile."""

    @property
    def touches(self) -> frozenset[int]:
        """The steps the edit affects, by index in the recording."""
        ...

    @property
    def refinement(self) -> Refinement:
        """How the edited build relates to the untuned build."""
        ...

    def apply(self, profile: Profile) -> Profile:
        """Return ``profile`` with the edit made."""
        ...


@dataclass(frozen=True)
class AddEntry:
    """An edit adding one composition entry to a profile.

    Attributes:
        entry: The entry added.
        touches: The steps it composes, by index in the recording it was
            found in.
        refinement: How the edited build relates to the untuned build.
    """

    entry: Entry
    touches: frozenset[int]
    refinement: Refinement = Refinement.EXACT

    def apply(self, profile: Profile) -> Profile:
        """Return a copy of ``profile`` with ``entry`` added."""
        edited = profile.copy()
        edited.add_entry(self.entry)
        return edited


logger = logging.getLogger(__name__)

# A measured ratio under this gains: past the paired timing's noise.
GAINS = 0.95
# How an edit is priced: IRON's verify timing, lighter than measure's own.
PRICING = Timing(rounds=3, calls=10)

# What candidates does not propose yet, named where it stops.
_NOT_GENERATED = (
    "regions of steps that are not consecutive",
    "chosen depths",
    "DDR and cascade edges",
    "inflows",
    "shared workers",
    "chosen phases",
    "runtime plans",
    "nested regions",
    "configurations",
    "widths differing between a region's members",
    "fission",
    "substitution",
    "scopes",
    "schedules",
    "variants and bindings",
    "state layouts",
)


@dataclass(frozen=True)
class Fit:
    """Whether a profile's compositions fit the device, decided before any build.

    Attributes:
        ok: Whether everything fits.
        stage: Where a refusal came from: the counts, the dataflow analysis,
            or the placer.
        why: The refusal, naming what does not fit.
        breakdown: The placer's penalty components, where it refused.
    """

    ok: bool
    stage: Literal["counts", "analysis", "placer"] | None = None
    why: str | None = None
    breakdown: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class Check:
    """Whether a built profile computes what the untuned build does.

    Attributes:
        ok: Whether it passed.
        refinement: The rule it was held to.
        why: The first difference, where it failed.
    """

    ok: bool
    refinement: Refinement
    why: str | None = None


@dataclass(frozen=True)
class Measured:
    """A profile's time against a base's, from paired runs.

    Attributes:
        ratio: The median of the paired ratios, profile over base, each
            point's weighed by the base's time there.
        seconds: The profile's median seconds a run of the calls.
        base_seconds: The base's median seconds a run of the calls.
    """

    ratio: float
    seconds: float
    base_seconds: float


PLACEMENTS: Sequence[str] = ("sequential", "sa:0", "sa:1", "sa:2")


def candidates(
    calls: Sequence[Timed], profile: Profile, device: Device
) -> Iterator[Edit]:
    """Yield every edit of ``profile`` that ``calls`` admit on ``device``.

    A region edit names a window of consecutive recorded steps, no host step
    inside it and no more steps than the array has cores, with an edge for
    each hand-off the recording makes inside it: one step the only writer of
    a whole, streamed buffer the host does not hold, a later step reading it
    whole, the two ends one buffer. Its edges are ordered by producer, then
    consumer, each a stream where the dataflow analysis finds the lanes meet
    as they are (an equal or broadcast hand-off) and staged otherwise, or
    where the analysis does not model the pair yet; whether the composer
    builds it is ``fit``'s to say, not this. Each member names its step's shape
    and nothing else (``Profile.dims`` of it, tunables None), so a region
    edit composes with an edit of the same steps' tunables. Each region
    follows at every column count its members' domains share, every member
    at it, whatever its call gave (a region's widths override those, as a
    fusion's tunables do). Then each shape's tunables: a one-member region per setting
    ``autotune.settings`` resolves (the recorded one first), touching every
    step of that shape. Each entry is yielded once, from the first call that
    admits it.

    Args:
        calls: The graph's calls, every version.
        profile: The profile the edits are of.
        device: The device.

    Raises:
        NotImplementedError: After every edit it yields: the kinds of edit
            it does not generate yet.
    """
    proposed: list[Entry] = []
    cores = device.cols * len(device.core_rows)
    for timed in calls:
        recording = timed.recording
        steps = recording.steps
        _, writers = recording.users()
        held = recording.held
        members = [
            Member(type(step.op), Profile.dims(type(step.op), vars(step.op)))
            for step in steps
        ]
        kinds: dict[tuple[int, str, int, str], EdgeKind | None] = {}
        columns = []
        for step in steps:
            # A region's widths override what a call gave, as a fusion's
            # tunables do, so the domain is the unpinned one.
            with set_current_device(device):
                unpinned = step.op.replace(pinned=frozenset()).resolved(device)
                domains = unpinned._domains(device)
            columns.append(set(domains.get("num_aie_columns", ())))
        for lo in range(len(steps)):
            for hi in range(lo + 1, min(lo + cores, len(steps))):
                if recording.crosses_host(lo, hi):
                    break
                edges: list[Edge] = []
                for c in range(lo + 1, hi + 1):
                    for sink, read in zip(steps[c].op.buffers, steps[c].refs()):
                        made = writers.get(read.root, [])
                        if (
                            not sink.fills
                            or not sink.streamed
                            or read.nbytes is not None
                            or read.root in held
                            or len(made) != 1
                            or not lo <= made[0] < c
                        ):
                            continue
                        p = made[0]
                        for source, wrote in zip(steps[p].op.buffers, steps[p].refs()):
                            if not (
                                source.drains
                                and source.streamed
                                and wrote.root == read.root
                                and wrote.nbytes is None
                            ):
                                continue
                            pair = (p, source.name, c, sink.name)
                            if pair not in kinds:
                                edge = Edge(0, source.name, 1, sink.name)
                                try:
                                    shape = (
                                        Derivation(
                                            Region((members[p], members[c]), (edge,)),
                                            recording,
                                            device,
                                        )
                                        .analysis()
                                        .hand_off[edge]
                                    )
                                except NotImplementedError:
                                    kinds[pair] = EdgeKind.STAGED
                                except ValueError:
                                    kinds[pair] = None
                                else:
                                    kinds[pair] = (
                                        EdgeKind.STREAM
                                        if shape in (HandOff.EQUAL, HandOff.BROADCAST)
                                        else EdgeKind.STAGED
                                    )
                            if kinds[pair] is not None:
                                edges.append(
                                    Edge(
                                        p - lo,
                                        source.name,
                                        c - lo,
                                        sink.name,
                                        kind=kinds[pair],
                                    )
                                )
                entry = Entry(
                    Region(
                        tuple(members[lo : hi + 1]),
                        tuple(
                            sorted(
                                edges,
                                key=lambda e: (
                                    e.producer,
                                    e.consumer,
                                    e.output,
                                    e.input,
                                ),
                            )
                        ),
                    )
                )
                if entry in proposed:
                    continue
                proposed.append(entry)
                touches = frozenset(range(lo, hi + 1))
                yield AddEntry(entry, touches)
                for width in sorted(set.intersection(*columns[lo : hi + 1])):
                    widened = Entry(
                        Region(
                            tuple(
                                dataclasses.replace(
                                    m, tunables={"num_aie_columns": width}
                                )
                                for m in members[lo : hi + 1]
                            ),
                            entry.root.edges,
                        )
                    )
                    if widened not in proposed:
                        proposed.append(widened)
                        yield AddEntry(widened, touches)
        shapes: dict[int, list[int]] = {}
        for i, m in enumerate(members):
            first = next(k for k in range(i + 1) if members[k] == m)
            shapes.setdefault(first, []).append(i)
        for first, at in shapes.items():
            with set_current_device(device):
                found = settings(steps[first].op, device)
            for setting in found:
                entry = Entry(
                    Region((dataclasses.replace(members[first], tunables=setting),))
                )
                if entry not in proposed:
                    proposed.append(entry)
                    yield AddEntry(entry, frozenset(at))
    raise NotImplementedError(
        "candidates does not generate yet: " + ", ".join(_NOT_GENERATED)
    )


def fit(
    profile: Profile,
    calls: Sequence[Timed],
    device: Device,
    placements: Sequence[str] = PLACEMENTS,
    max_images: int | None = None,
) -> Fit:
    """Decide whether ``profile``'s compositions fit ``device``, before any build.

    Each call's steps are first tuned as the profile's tunable entries name;
    a setting its operator cannot resolve or validate is refused by the
    counts, as is a region member's, and one that resolves is placed alone.
    Each region entry, at its first match in each call's recording, then
    passes three stages in turn. The counts are
    lower bounds from the target model, so they never refuse what fits: the
    cores its steps record (steps sharing a worker counted once, at the most
    any of them takes), and each edge held at a chosen depth against one
    tile's memory, and through a memtile against its buffer descriptors. The
    dataflow analysis then finds whether the region's steps are convex (no
    step outside it on a path between two of them), whether it balances, whether each
    stream edge's lanes meet as they are, and whether it runs at its chosen
    depths, the rest at their minimum. The placer last places the composed
    module, where the composer builds the region as IRON's fusions do.

    A refusal from any stage of any entry wins over what is not fitted yet;
    only where nothing refuses is the first of those raised.

    Args:
        profile: The profile whose compositions are fitted.
        calls: The graph's calls, every version.
        device: The device.
        placements: The placer's settings a fit may try.
        max_images: The images the host may hold loaded at once; None for no limit.

    Raises:
        ValueError: An entry matches none of the calls' steps.
        NotImplementedError: What is not fitted yet, where nothing refuses:
            images held at once, a profile's schedules, variants, bindings,
            fusion or packing entries, an entry rooted at a configuration or
            a step, scoped to some runs of its shape, splitting a step by
            fission or chaining a cascade, more fifos to or
            from the host than the shim has channels (IRON's composer gives
            each its own; mlir-aie can share them), a placer setting past the
            sequential placer, a region the composer does not build, and
            what the analysis does not model (``Derivation``).
    """
    waiting = [
        f"fitting {kind} is not built yet"
        for kind, kept in (
            ("images held at once", max_images is not None),
            ("schedule entries", profile.schedules()),
            ("variants", profile.variants()),
            ("bindings", profile.bindings()),
            ("fusion entries", profile.fusions()),
            ("packing entries", profile.packings()),
        )
        if kept
    ]
    model = get_target_model(device.resolve())
    rows = range(model.rows())
    mem_row = next(r for r in rows if model.is_mem_tile(0, r))
    cores_on_array = sum(
        model.is_core_tile(c, r) for c in range(model.columns()) for r in rows
    )
    held_in = {
        EdgeKind.STREAM: ("a core tile", model.get_local_memory_size(), None),
        EdgeKind.STAGED: (
            "a memtile",
            model.get_mem_tile_size(),
            model.get_num_bds(0, mem_row),
        ),
    }
    matched: set[int] = set()
    for timed in calls:
        recording = timed.recording
        steps = list(recording.steps)
        retuned: dict[int, list] = {}
        for i, step in enumerate(steps):
            op = step.op
            given = {n: vars(op)[n] for n in op.given}
            tunables = {
                n: v
                for n, v in profile.tunables_for(type(op), given).items()
                if n not in op.pinned and vars(op)[n] != v
            }
            if not tunables:
                continue
            try:
                with set_current_device(device):
                    tuned = op._with_tunables(**tunables).resolved(device)
            except ValueError as e:  # unresolvable or incompatible here
                return Fit(False, "counts", f"{type(op).__name__} at {tunables}: {e}")
            with set_current_device(device):
                refused = refusal(tuned)
            if refused is not None:
                return Fit(
                    False, "placer", f"{type(op).__name__} at {tunables}: {refused}"
                )
            retuned.setdefault(id(op), []).append(tuned)
            steps[i] = dataclasses.replace(step, op=tuned)
        if retuned:
            recording = dataclasses.replace(recording, steps=steps)
            recording.rebind(retuned)
        readers, writers = recording.users()
        after = [
            {
                r
                for root, ws in writers.items()
                if s in ws
                for r in readers.get(root, [])
                if r > s
            }
            for s in range(len(recording.steps))
        ]
        for index, entry in enumerate(profile.entries()):
            region = entry.root
            if any(m.part is not None for m in region.steps()):
                matched.add(index)
                waiting.append(
                    "a step split by fission (Member.part) is not matched or "
                    "built yet"
                )
                continue
            if any(e.kind is EdgeKind.CASCADE for e, _, _ in region.wiring()[0]):
                matched.add(index)
                waiting.append(
                    "a cascade chain, which rewrites a reduction rather than "
                    "naming recorded hand-offs, is not matched or built yet"
                )
                continue
            found = recording.occurrences(entry)
            if not found:
                continue
            matched.add(index)
            inside = set(found[0])
            frontier = [o for s in inside for o in after[s] if o not in inside]
            seen = set(frontier)
            while frontier:
                o = frontier.pop()
                if after[o] & inside:
                    return Fit(
                        False,
                        "analysis",
                        f"its steps are not convex: step {o} "
                        f"({type(recording.steps[o].op).__name__}), outside it, lies "
                        f"on a path between two of them",
                    )
                frontier += [n for n in after[o] - inside if n not in seen]
                seen |= after[o] - inside
            if not isinstance(region, Region):
                waiting.append(
                    f"fitting an entry rooted at a {type(region).__name__} is not "
                    f"built yet"
                )
                continue
            if entry.scope.occurrences is not None:
                waiting.append(
                    "an entry scoped to some runs of its shape is not built yet: "
                    "IRON applies an entry to every run"
                )
                continue
            for s, m in zip(found[0], region.steps()):
                if not m.tunables:
                    continue
                try:
                    with set_current_device(device):
                        recording.steps[s].op._with_tunables(**m.tunables).resolved(
                            device
                        )
                except ValueError as e:  # unresolvable or incompatible here
                    return Fit(
                        False, "counts", f"{m.cls.__name__} at {m.tunables}: {e}"
                    )
            try:
                derivation = Derivation(region, recording, device)
            except NotImplementedError as e:
                waiting.append(str(e))
                continue
            cores = [len(recorded.cores) for _, recorded in derivation.recorded]
            shared = {s for worker in region.workers for s in worker}
            needed = sum(k for s, k in enumerate(cores) if s not in shared) + sum(
                max(cores[s] for s in worker) for worker in region.workers
            )
            if needed > cores_on_array:
                return Fit(
                    False,
                    "counts",
                    f"its steps take {needed} cores; {device.resolve()} has "
                    f"{cores_on_array}",
                )
            on_chip = {(p, e.output) for e, p, _ in derivation.wired} | {
                (c, e.input) for e, _, c in derivation.wired
            }
            moved = set()
            for s, ((_, recorded), lanes) in enumerate(
                zip(derivation.recorded, derivation.lanes)
            ):
                owner = {f: name for name, fifos in lanes.items() for f in fifos}
                moved |= {
                    (t.kind, t.fifo)
                    for t in recorded.transfers
                    if (s, owner.get(t.fifo)) not in on_chip
                }
            unplaceable = [
                f"its steps {kind} {taken} fifos from the host, and "
                f"{device.resolve()} has {budget} shim channels: IRON's composer "
                f"gives each its own, and sharing them is not built yet"
                for kind, budget in (
                    ("fill", device.shim_dma_channels_in),
                    ("drain", device.shim_dma_channels_out),
                )
                for taken in [sum(k == kind for k, _ in moved)]
                if taken > budget
            ]
            for edge, p, _ in derivation.wired:
                elements = derivation.obj_elements[p].get(edge.output)
                if edge.depth is None or edge.kind not in held_in or elements is None:
                    continue
                tile, memory, bds = held_in[edge.kind]
                (source,) = [
                    b for b in derivation.ops[p].buffers if b.name == edge.output
                ]
                held = edge.depth * elements * np.dtype(source.dtype).itemsize
                if held > memory:
                    return Fit(
                        False,
                        "counts",
                        f"{edge} holds {edge.depth} objects, {held} bytes; {tile} "
                        f"holds {memory}",
                    )
                if bds is not None and edge.depth > bds:
                    return Fit(
                        False,
                        "counts",
                        f"{edge} holds {edge.depth} objects, a buffer descriptor "
                        f"each; {tile} has {bds}",
                    )
            try:
                analysis = derivation.analysis()
            except NotImplementedError as e:
                waiting.append(str(e))
                continue
            if analysis.why is not None:
                return Fit(False, "analysis", analysis.why)
            for edge, p, c in derivation.wired:
                shape = analysis.hand_off[edge]
                if edge.kind is not EdgeKind.STREAM:
                    continue
                if shape not in (HandOff.EQUAL, HandOff.BROADCAST):
                    return Fit(
                        False,
                        "analysis",
                        f"{edge} is a stream, whose lanes meet as they are; its "
                        f"{shape.value} hand-off needs a restage",
                    )
            why = analysis.deadlock(
                {e: e.depth for e, _, _ in derivation.wired if e.depth is not None}
            )
            if why is not None:
                return Fit(False, "analysis", f"at its chosen depths, it {why}")
            for edge, p, _ in derivation.wired:
                root_name = derivation.refs[p][edge.output].root
                if (
                    set(readers.get(root_name, [])) - inside
                    or root_name in recording.held
                ):
                    unplaceable.append(
                        f"{edge}: an edge out of {root_name!r}, which steps past "
                        f"the region or the host also read, is not built yet (a "
                        f"tee keeping the host's copy)"
                    )
            for edge, p, c in derivation.wired:
                made = derivation.obj_elements[p].get(edge.output)
                taken = derivation.obj_elements[c].get(edge.input)
                if (
                    edge.kind is EdgeKind.STREAM
                    and made is not None
                    and taken is not None
                    and made != taken
                ):
                    unplaceable.append(
                        f"{edge}: a stream whose ends' objects differ ({made} "
                        f"elements and {taken}) is not built yet; the composer "
                        f"gives a fifo one object size"
                    )
            kinds = {e.kind for e in region.edges}
            if (
                region.inflows
                or region.workers
                or region.phases is not None
                or region.runtime is not None
                or not all(isinstance(part, Member) for part in region.parts)
                or any(e.depth is not None for e in region.edges)
                or len(kinds) > 1
                or not kinds <= {EdgeKind.STREAM, EdgeKind.STAGED}
            ):
                unplaceable.append(
                    "placing a region the composer does not build yet (inflows, "
                    "shared workers, chosen phases or depths, a runtime plan, "
                    "nesting, or edges of several kinds or of DDR or the cascade)"
                )
            if "sequential" not in placements:
                unplaceable.append(
                    "placing with anything but the sequential placer is not built yet"
                )
            if not unplaceable:
                alone = Profile()
                alone.add_entry(entry)
                try:
                    with set_current_device(device):
                        composed(recording, alone)
                except NotImplementedError as e:
                    unplaceable.append(str(e))
            if unplaceable:
                waiting += unplaceable
                continue
            with set_current_device(device):
                refused = group_fit_verdict(
                    derivation.ops,
                    kind=FusionKind(kinds.pop().value) if kinds else None,
                    edges=[
                        (e.producer, e.output, e.consumer, e.input)
                        for e in region.edges
                    ],
                )
            if refused is not None and set(placements) != {"sequential"}:
                waiting.append(
                    f"the sequential placer refuses it ({refused}); trying "
                    f"{', '.join(s for s in placements if s != 'sequential')} is not "
                    f"built yet"
                )
            elif refused is not None:
                return Fit(False, "placer", refused)
    unmatched = [e for n, e in enumerate(profile.entries()) if n not in matched]
    if unmatched:
        raise ValueError(f"{unmatched[0]} matches none of the calls' steps")
    if waiting:
        raise NotImplementedError(waiting[0])
    return Fit(True)


def check(
    profile: Profile,
    base: Profile,
    calls: Sequence[Timed],
    device: Device,
    refinement: Refinement,
    base_calls: Sequence[Timed] | None = None,
) -> Check:
    """Hold ``calls`` built under ``profile`` to ``base_calls`` built under ``base``, run on the NPU on the same inputs.

    ``profile`` must fit first (``fit``). Each call is built both ways
    (``Applied``, the profile's composition entries included) and run on the
    same seeded inputs and states at its values and at each of its bounds
    halved; every output within its bound, carried buffer and state must be
    bit-identical (``compare_graphs``, every point marked known so nothing
    is timed).

    Args:
        profile: The profile checked.
        base: The profile it is held to.
        calls: The graph's calls.
        device: The device.
        refinement: The rule it is held to.
        base_calls: The calls ``base`` runs, where they are not ``calls``
            (an operator a graph replaces), by version.

    Raises:
        ValueError: ``profile`` does not fit, an entry matches none of the
            calls (``fit``), or a call leaves the host nothing to compare.
        NotImplementedError: What is not checked yet: a no-worse rule (against
            the operators' references), state carried from one call into the
            next, and what ``fit`` or the composer (``composed``) does not
            take yet.
    """
    if refinement is not Refinement.EXACT:
        raise NotImplementedError(
            "holding a change no worse than the untuned build, against the "
            "operators' references, is not built yet"
        )
    fitted = fit(profile, calls, device)
    if not fitted.ok:
        raise ValueError(f"the profile does not fit ({fitted.stage}): {fitted.why}")
    for call in calls:
        recording = call.recording
        if not (recording.outputs or recording.feedback or recording.states):
            raise ValueError(
                f"{recording.name} leaves the host no output, carried buffer or "
                f"state to compare"
            )
    if len(calls) > 1 and any(c.recording.states for c in calls):
        raise NotImplementedError(
            "carrying state from one call into the next is not built yet: each "
            "call is checked on states of its own"
        )
    olds = {
        c.recording.version: c for c in (calls if base_calls is None else base_calls)
    }
    for call in calls:
        old = olds[call.recording.version]
        with set_current_device(device):
            before = Applied.of(old, base, device).built(device)
            after = Applied.of(call, profile, device).built(device)
            known = Compared(
                {tuple(sorted(v.items())): (0.0, None) for _, v in old.timed_points()}
            )
            try:
                compare_graphs(
                    old,
                    before,
                    after,
                    timing=Timing(rounds=1, calls=1),
                    known=known,
                    log=logger.info,
                )
            except NotBitIdentical as e:
                return Check(False, refinement, str(e))
    return Check(True, refinement)


def measure(
    profile: Profile,
    base: Profile,
    calls: Sequence[Timed],
    device: Device,
    timing: Timing = Timing(),
) -> Measured:
    """Time ``calls`` built under ``profile`` against them built under ``base``, in pairs.

    ``profile`` must fit (``fit``). Each call is built both ways and timed
    interleaved on the NPU at each of its points, checked bit-identical as
    it goes (``compare_graphs``). A call's time is its points' medians,
    weighted; ``ratio`` weighs each point's median paired ratio by the
    base's time there.

    Args:
        profile: The profile timed.
        base: The profile it is timed against.
        calls: The graph's calls.
        device: The device.
        timing: How long each call is timed.

    Raises:
        ValueError: ``profile`` does not fit.
        NotBitIdentical: A call is not bit-identical built both ways.
        NotImplementedError: What ``fit`` or the composer does not take yet.
    """
    fitted = fit(profile, calls, device)
    if not fitted.ok:
        raise ValueError(f"the profile does not fit ({fitted.stage}): {fitted.why}")
    seconds = base_seconds = weighted = 0.0
    for call in calls:
        known = Compared()
        with set_current_device(device):
            before = Applied.of(call, base, device).built(device)
            after = Applied.of(call, profile, device).built(device)
            compare_graphs(
                call, before, after, timing=timing, known=known, log=logger.info
            )
        for weight, values in call.timed_points():
            point = tuple(sorted(values.items()))
            was, now = known.medians[point]
            base_seconds += weight * was / 1e6
            seconds += weight * now / 1e6
            weighted += weight * was * known.ratios[point] / 1e6
    return Measured(weighted / base_seconds, seconds, base_seconds)


def search(
    calls: Sequence[Timed],
    start: Profile,
    device: Device,
    budget_s: float | None = None,
    max_images: int | None = None,
) -> Profile:
    """Return the fastest profile found from ``start`` that passes every check.

    Each edit ``candidates`` yields is applied to ``start``, fitted
    (``fit``; one that waits or is refused is passed over) and measured in
    place against ``start`` (``measure``); one under ``GAINS`` gains, and one
    that does not build, or builds wrong, is refused and logged. The gainers are
    then taken best first, each touching no step a taken one
    touches: a take is checked bit-identical against ``start`` (``check``)
    and measured against the profile so far, and kept where it still gains.
    Pricing stops at ``budget_s``.

    Args:
        calls: The graph's calls, every version.
        start: The profile searched from.
        device: The device.
        budget_s: The most the pricing takes, in seconds; None for no limit.
        max_images: The images the host may hold loaded at once; None for no limit.

    Raises:
        NotImplementedError: ``max_images`` is given (counting the images a
            profile loads is not built yet).
    """
    if max_images is not None:
        raise NotImplementedError(
            "counting the images a profile loads is not built yet"
        )
    begun = time.perf_counter()
    priced: list[tuple[float, Edit]] = []
    edits = candidates(calls, start, device)
    while budget_s is None or time.perf_counter() - begun < budget_s:
        try:
            edit = next(edits)
        except StopIteration:
            break
        except NotImplementedError as e:
            logger.info("search: %s", e)
            break
        edited = edit.apply(start)
        try:
            fitted = fit(edited, calls, device)
        except NotImplementedError as e:
            logger.info("search: waits: %s", e)
            continue
        if not fitted.ok:
            logger.info("search: refused at %s: %s", fitted.stage, fitted.why)
            continue
        if edit.refinement is not Refinement.EXACT:
            logger.info("search: waits: a no-worse edit is not checked yet")
            continue
        try:
            ratio = measure(edited, start, calls, device, timing=PRICING).ratio
        except NotBitIdentical as e:
            logger.warning("search: refused, built wrong: %s: %s", edit, e)
            continue
        except NotImplementedError as e:
            logger.info("search: waits: %s", e)
            continue
        except (ValueError, RuntimeError, ir.MLIRError) as e:
            logger.warning("search: refused, does not build: %s: %s", edit, e)
            continue
        logger.info("search: %.3f for %s", ratio, edit)
        if ratio < GAINS:
            priced.append((ratio, edit))
    incumbent = start
    taken: set[int] = set()
    for ratio, edit in sorted(priced, key=lambda pair: pair[0]):
        if taken & edit.touches:
            continue
        edited = edit.apply(incumbent)
        checked = check(edited, start, calls, device, edit.refinement)
        if not checked.ok:
            logger.info("search: %s is not bit-identical: %s", edit, checked.why)
            continue
        if measure(edited, incumbent, calls, device, timing=PRICING).ratio >= GAINS:
            continue
        incumbent = edited
        taken |= edit.touches
    return incumbent
