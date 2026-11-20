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
import math
import subprocess
import time
from collections import Counter
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Literal, Protocol

import numpy as np
from aie import ir
from aie.dialects.aie import get_target_model
from aie.iron.device import Device
from aie.utils import set_current_device

from ..common.declare import Profile
from ..common.declare.composition import (
    Configuration,
    Entry,
    Hold,
    Member,
    Refinement,
    Region,
    RuntimePlan,
    Schedule,
    Switch,
    Version,
    refinement,
)
from ..common.design import OperatorDesign
from ..common.graph.carried import CarriedLoop
from ..common.graph.compiled import _words
from ..common.graph.fold import apply_folds, composed_folds, fold_candidates
from ..common.graph.fusion import composed, memory_waits
from ..common.graph.record import Recording
from ..common.graph.sdf import Derivation
from ..common.image.compose import ANNEALED, SEQUENTIAL
from ..common.image.packaging import SCRATCHPAD_WORDS
from ..common.image.step import Edge, EdgeKind, FusionKind, HandOff
from .autotune import Point, Timed, refusal, settings
from .cli import WATCHDOG_HEADROOM, watchdog_s
from .fusions import (
    Applied,
    Compared,
    NotBitIdentical,
    _bound_points,
    _random_tensor,
    compare_graphs,
    drawn_inputs,
    group_fit_verdict,
)
from .measure import Cache, Timing


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


@dataclass(frozen=True)
class HoldEdge:
    """An edit holding one edge of a region the profile composes at another place (``Region.held``).

    Attributes:
        entry: The entry, as the profile holds it.
        index: The edge, by its index in the entry's root region.
        place: Where its value waits.
        touches: The steps the region composes, by index in the recording it
            was found in.
        refinement: How the edited build relates to the untuned build.
    """

    entry: Entry
    index: int
    place: Hold
    touches: frozenset[int]
    refinement: Refinement = Refinement.EXACT

    def apply(self, profile: Profile) -> Profile:
        """Return a copy of ``profile`` with ``entry`` replaced by itself, the edge held at ``place``."""
        edited = profile.copy()
        root = self.entry.root
        assert isinstance(root, Region), "candidates yields it for regions alone"
        held = dataclasses.replace(self.entry, root=root.held(self.index, self.place))
        edited.replace_entry(self.entry, held)
        return edited


@dataclass(frozen=True)
class DepthEdge:
    """An edit holding one edge of a region the profile composes at another depth (``Region.deepened``).

    Attributes:
        entry: The entry, as the profile holds it.
        index: The edge, by its index in the entry's root region.
        depth: The objects it holds.
        touches: The steps the region composes, by index in the recording it
            was found in.
        refinement: How the edited build relates to the untuned build.
    """

    entry: Entry
    index: int
    depth: int
    touches: frozenset[int]
    refinement: Refinement = Refinement.EXACT

    def apply(self, profile: Profile) -> Profile:
        """Return a copy of ``profile`` with ``entry`` replaced by itself, the edge ``depth`` deep."""
        edited = profile.copy()
        root = self.entry.root
        assert isinstance(root, Region), "candidates yields it for regions alone"
        deepened = dataclasses.replace(
            self.entry, root=root.deepened(self.index, self.depth)
        )
        edited.replace_entry(self.entry, deepened)
        return edited


@dataclass(frozen=True)
class PlanRegion:
    """An edit setting one field of the runtime plan of a region the profile composes (``RuntimePlan``).

    Attributes:
        entry: The entry, as the profile holds it.
        field: The ``RuntimePlan`` field set.
        value: Its value.
        touches: The steps the region composes, by index in the recording it
            was found in.
        refinement: How the edited build relates to the untuned build.
    """

    entry: Entry
    field: str
    value: object
    touches: frozenset[int]
    refinement: Refinement = Refinement.EXACT

    def apply(self, profile: Profile) -> Profile:
        """Return a copy of ``profile`` with ``entry`` replaced by itself, its plan's ``field`` at ``value``."""
        edited = profile.copy()
        root = self.entry.root
        assert isinstance(root, Region), "candidates yields it for regions alone"
        plan = dataclasses.replace(
            root.runtime or RuntimePlan(), **{self.field: self.value}
        )
        planned = dataclasses.replace(
            self.entry, root=dataclasses.replace(root, runtime=plan)
        )
        edited.replace_entry(self.entry, planned)
        return edited


@dataclass(frozen=True)
class ScheduleVersion:
    """An edit setting one field of a version's schedule (``Schedule``), the version's default schedule where the profile holds none.

    Attributes:
        version: The version scheduled.
        field: The ``Schedule`` field set.
        value: Its value.
        touches: Every step of the version's recording.
        refinement: How the edited build relates to the untuned build.
    """

    version: Version
    field: str
    value: object
    touches: frozenset[int]
    refinement: Refinement = Refinement.EXACT

    def apply(self, profile: Profile) -> Profile:
        """Return a copy of ``profile`` with ``version``'s schedule's ``field`` at ``value``."""
        edited = profile.copy()
        held = [s for s in profile.schedules() if s.version == self.version]
        schedule = held[0] if held else Schedule(self.version)
        changed = dataclasses.replace(schedule, **{self.field: self.value})
        if held:
            edited.replace_schedule(schedule, changed)
        else:
            edited.add_schedule(changed)
        return edited


# A chosen depth is an edge's minimum times a power of two up to this many
# doublings, beside its knee; past what a core or memtile holds, fit refuses.
DEPTH_DOUBLINGS = 4

# A runtime plan's chunks, and a schedule's calls a command or merged into one,
# are powers of two up to this many doublings.
SCHEDULE_DOUBLINGS = 2

logger = logging.getLogger(__name__)

# A measured ratio under this gains: past the paired timing's noise.
GAINS = 0.95
# How an edit is priced: IRON's verify timing, lighter than measure's own.
PRICING = Timing(rounds=4, calls=10)

# The seeded draws a no-worse change is held on, alternately typical and stress.
NO_WORSE_DRAWS = 4

# The |e| quantile a no-worse check compares beside the mean square.
NO_WORSE_QUANTILE = 0.999

# What candidates does not propose yet, named where it stops.
_NOT_GENERATED = (
    "regions of steps that are not consecutive",
    "inflows",
    "a runtime plan's DDR burst lengths and transfer sizes",
    "nested regions",
    "a configuration of one design, and its concurrency, width, residency, "
    "switch and teardown",
    "widths differing between a region's members",
    "fission",
    "substitution",
    "scopes",
    "a schedule's order and recomputed steps",
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


PLACEMENTS: Sequence[str] = ("sequential", "sa:1", "sa:2", "sa:3")

# The placer settings a build takes: the sequential placer, else the annealing
# one at mlir-aie's default seed (``Composition.placed``). ``sa:N`` is seed N.
BUILT_PLACERS: Mapping[str, str] = {"sequential": SEQUENTIAL, "sa:1": ANNEALED}


def candidates(
    calls: Sequence[Timed], profile: Profile, device: Device
) -> Iterator[Edit]:
    """Yield every edit of ``profile`` that ``calls`` admit on ``device``.

    A region edit names a window of consecutive recorded steps, no host step
    inside it and no more steps than the array has cores, with an edge for
    each hand-off the recording makes inside it: one step the only writer of
    a whole, streamed buffer, a later step reading it whole, the two ends one
    buffer; or, the buffer state the graph holds, any step of the window
    reading it, the writer itself (a self-loop) or one before it in the
    window reading what it wrote the call before. Its edges are ordered by producer, then
    consumer, each a stream where the dataflow analysis finds the lanes meet
    as they are (an equal or broadcast hand-off, one object size at both
    ends) and staged otherwise, or
    where the analysis does not model the pair yet; whether the composer
    builds it is ``fit``'s to say, not this. Each member names its step's shape
    and nothing else (``Profile.dims`` of it, tunables None), so a region
    edit composes with an edit of the same steps' tunables. Each region
    follows at every other column count its members' domains share, every
    member at it, whatever its call gave (a region's widths override those, as a
    fusion's tunables do). Then each fold IRON admits (``fold_candidates``),
    its steps on one worker. Then each shape's tunables: a one-member region per setting
    ``autotune.settings`` resolves (the recorded one first), touching every
    step of that shape. Each entry is yielded once, from the first call that
    admits it. First, for each region ``profile`` composes that a call's
    recording runs, each edge held at each other place (``HoldEdge``) and at
    each chosen depth, its analysis minimum times 2 to 2**DEPTH_DOUBLINGS
    and its knee (``DepthEdge``): one edge an edit, so the search composes
    several; the analysis's own kind and minimum are the region edit's. With
    them, each other value of each field of its runtime plan (``PlanRegion``):
    its awaits, its overlap, its chunks (powers of two up to
    2**SCHEDULE_DOUBLINGS), its tasks in flight (one up to the target model's
    task queue depth) and its chaining. Last, for each call's version, each
    other value of each field of its schedule (``ScheduleVersion``): its calls a
    command, calls overlapped (fewer than its calls a command), commands in
    flight, calls merged into one (``"merged_<k>x"``), each other version
    interleaved, and its packaging; ``fit`` refuses one that breaks a
    dependence.

    Before the schedules, after each call's tunables, its configurations:
    each window of consecutive steps a region's window may be, of two or
    more designs, as one ``Configuration`` loaded together, each region the
    profile composes inside it (at its first match) one part, every other
    step a member.

    Args:
        calls: The graph's calls, every version.
        profile: The profile the edits are of.
        device: The device.

    Raises:
        NotImplementedError: After every edit it yields: the kinds of edit
            it does not generate yet.
    """
    proposed: list[Entry] = []
    holds: list[tuple[Entry, int, Hold]] = []
    deepened: list[tuple[Entry, int, int]] = []
    planned: list[tuple[Entry | Version, str, object]] = []
    cores = device.cols * len(device.core_rows)
    queue = get_target_model(device.resolve()).get_dma_task_queue_depth()
    for timed in calls:
        recording = timed.recording
        for entry in profile.entries():
            root = entry.root
            if not isinstance(root, Region):
                continue
            found = recording.occurrences(entry)
            if not found:
                continue
            touches = frozenset(s for match in found for s in match)
            for index in range(len(root.edges)):
                for place in Hold:
                    if (entry, index, place) in holds:
                        continue
                    if root.held(index, place) == root:
                        continue
                    holds.append((entry, index, place))
                    yield HoldEdge(entry, index, place, touches)
            plan = root.runtime or RuntimePlan()
            for name, values in (
                ("waits", ("barrier", "per_channel")),
                ("overlap", ("none", "prefetch", "pipelined")),
                ("chunks", [1 << k for k in range(SCHEDULE_DOUBLINGS + 1)]),
                ("in_flight", range(1, queue + 1)),
                ("chained", (False, True)),
            ):
                for value in values:
                    if value == vars(plan)[name] or (entry, name, value) in planned:
                        continue
                    planned.append((entry, name, value))
                    yield PlanRegion(entry, name, value, touches)
            try:
                analysis = Derivation(root, recording, device, timed.values).analysis()
            except (NotImplementedError, ValueError):
                continue  # depths wait on the analysis modelling the region
            for index, edge in enumerate(root.edges):
                least = analysis.min_depth.get(edge)
                if least is None:
                    continue
                depths = [least << k for k in range(1, DEPTH_DOUBLINGS + 1)]
                try:
                    depths.append(analysis.knee_depth[edge])
                except (NotImplementedError, KeyError):
                    pass  # no knee yet: the doublings alone
                for depth in sorted(set(depths)):
                    if depth == edge.depth or (entry, index, depth) in deepened:
                        continue
                    deepened.append((entry, index, depth))
                    yield DepthEdge(entry, index, depth, touches)
        steps = recording.steps
        _, writers = recording.users()
        held = recording.held
        members = [
            Member(type(step.op), Profile.dims(type(step.op), vars(step.op)))
            for step in steps
        ]
        kinds: dict[tuple[int, str, int, str], EdgeKind | None] = {}
        columns = []
        recorded = []
        for step in steps:
            # A region's widths override what a call gave, as a fusion's
            # tunables do, so the domain is the unpinned one.
            with set_current_device(device):
                unpinned = step.op.replace(pinned=frozenset()).resolved(device)
                domains = unpinned._domains(device)
                recorded.append(vars(step.op.resolved(device)).get("num_aie_columns"))
            columns.append(set(domains.get("num_aie_columns", ())))
        for lo in range(len(steps)):
            for hi in range(lo + 1, min(lo + cores, len(steps))):
                if recording.crosses_host(lo, hi):
                    break
                edges: list[Edge] = []
                for c in range(lo, hi + 1):
                    for sink, read in zip(steps[c].op.buffers, steps[c].refs()):
                        made = writers.get(read.root, [])
                        if (
                            not sink.fills
                            or not sink.streamed
                            or read.nbytes is not None
                            or len(made) != 1
                        ):
                            continue
                        p = made[0]
                        # State a step of the window writes is carried: read
                        # from its writer earlier this call, or (the writer
                        # itself or later) from the call before.
                        if not (
                            lo <= p < c if read.root not in held else lo <= p <= hi
                        ):
                            continue
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
                                loop = p == c
                                edge = Edge(0, source.name, int(not loop), sink.name)
                                try:
                                    pair_of = Derivation(
                                        Region(
                                            (
                                                (members[p],)
                                                if loop
                                                else (members[p], members[c])
                                            ),
                                            (edge,),
                                        ),
                                        recording,
                                        device,
                                        timed.values,
                                    )
                                    shape = pair_of.analysis().hand_off[edge]
                                except NotImplementedError:
                                    kinds[pair] = EdgeKind.STAGED
                                except ValueError:
                                    kinds[pair] = None
                                else:
                                    sizes = (
                                        pair_of.obj_elements[0].get(source.name),
                                        pair_of.obj_elements[int(not loop)].get(
                                            sink.name
                                        ),
                                    )
                                    kinds[pair] = (
                                        EdgeKind.STREAM
                                        if shape in (HandOff.EQUAL, HandOff.BROADCAST)
                                        and sizes[0] == sizes[1]
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
                    if all(w == width for w in recorded[lo : hi + 1]):
                        continue  # the region as recorded, built once already
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
        with set_current_device(device):
            folds = fold_candidates(recording)
        for fold in folds:
            lo = fold.steps[0]
            entry = Entry(
                Region(
                    tuple(members[s] for s in fold.steps),
                    tuple(
                        Edge(e.producer - lo, e.output, e.consumer - lo, e.input)
                        for e in fold.edges
                    ),
                    workers=(tuple(range(len(fold.steps))),),
                )
            )
            if entry not in proposed:
                proposed.append(entry)
                yield AddEntry(entry, frozenset(fold.steps))
        shapes: dict[int, list[int]] = {}
        for i, m in enumerate(members):
            first = next(k for k in range(i + 1) if members[k] == m)
            shapes.setdefault(first, []).append(i)
        for first, at in shapes.items():
            with set_current_device(device):
                found = settings(steps[first].op, device)
            recorded = steps[first].op
            for setting in found:
                entry = Entry(
                    Region((dataclasses.replace(members[first], tunables=setting),))
                )
                if entry not in proposed:
                    proposed.append(entry)
                    moved = [n for n, v in setting.items() if vars(recorded)[n] != v]
                    yield AddEntry(
                        entry,
                        frozenset(at),
                        (
                            Refinement.NO_WORSE
                            if any(
                                refinement(type(recorded), n) is Refinement.NO_WORSE
                                for n in moved
                            )
                            else Refinement.EXACT
                        ),
                    )
        # Each region the profile composes, by its first match's first step.
        pieces: dict[int, tuple[Region, tuple[int, ...]]] = {}
        for entry in profile.entries():
            root = entry.root
            if not isinstance(root, Region):
                continue
            for match in recording.occurrences(entry)[:1]:
                if match == tuple(range(match[0], match[0] + len(match))):
                    pieces.setdefault(match[0], (root, match))
        for lo in range(len(steps)):
            for hi in range(lo + 1, min(lo + cores, len(steps))):
                if recording.crosses_host(lo, hi):
                    break
                if all(m == members[lo] for m in members[lo : hi + 1]):
                    continue  # one design: its own configuration already
                parts: list[Region | Member] = []
                s = lo
                while s <= hi:
                    piece = pieces.get(s)
                    if piece is not None and piece[1][-1] <= hi:
                        parts.append(piece[0])
                        s += len(piece[1])
                    else:
                        parts.append(members[s])
                        s += 1
                entry = Entry(Configuration(tuple(parts)))
                if len(parts) > 1 and entry not in proposed:
                    proposed.append(entry)
                    yield AddEntry(entry, frozenset(range(lo, hi + 1)))
    versions = [t.recording.version for t in calls]
    for timed in calls:
        version = timed.recording.version
        held = [s for s in profile.schedules() if s.version == version]
        schedule = held[0] if held else Schedule(version)
        doublings = [1 << k for k in range(SCHEDULE_DOUBLINGS + 1)]
        for name, values in (
            ("calls_per_command", doublings),
            ("calls_overlapped", range(schedule.calls_per_command)),
            ("commands_in_flight", doublings),
            ("size", [None, *(f"merged_{k}x" for k in doublings[1:])]),
            (
                "interleave_with",
                [(), *((v,) for v in dict.fromkeys(versions) if v != version)],
            ),
            (
                "packaging",
                [
                    None,
                    "xclbin",
                    *(["full_elf"] if device.can_dispatch_full_elf else []),
                ],
            ),
        ):
            for value in values:
                if value == vars(schedule)[name] or (version, name, value) in planned:
                    continue
                planned.append((version, name, value))
                yield ScheduleVersion(
                    version, name, value, frozenset(range(len(timed.recording.steps)))
                )
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
    The rest holds the version the call's schedule builds
    (``Recording.scheduled``): several calls a command, or calls merged into
    one, composed and placed as built.
    A region whose steps share one worker is IRON's fold of them
    (``composed_folds``), placed as the one operator it folds into. Each other
    region entry, at its first match in each call's recording, then passes
    three stages in turn. The counts are
    lower bounds from the target model, so they never refuse what fits: the
    cores its steps record (steps sharing a worker counted once, at the most
    any of them takes), each edge held at a chosen depth against one
    tile's memory, and through a memtile against its buffer descriptors, and
    its cascades: each from one core to another, at most one into and one
    out of a core, and a chain no longer than a path east and south across
    the array. The
    dataflow analysis then finds whether the region's steps are convex (no
    step outside it on a path between two of them), whether it balances, whether each
    stream or cascade edge's lanes meet as they are, and
    whether it runs at its chosen
    depths, the rest at their minimum. The placer last places the composed
    module, where the composer builds the region as IRON's fusions do: under
    each of ``placements`` the build takes in turn (``BUILT_PLACERS``), the
    sequential placer, then the annealing one where it refuses.

    Before any call, each entry's own choices: a configuration resident into
    the next across its own teardown, or wider than the array; a runtime
    plan keeping more tasks in flight than a channel's queue holds, or
    chaining more chunks than a shim tile has buffer descriptors; chosen
    phases that put a consumer before its producer, or a stream across a
    phase boundary. A configuration at its first match (``_configuration_fit``)
    has parts run at once independent, its cores counted and its steps placed
    as one device configuration; configurations concurrent under one id must
    be independent of each other, their chosen columns disjoint, and are
    placed as one pack. A plan's per-channel awaits must not reuse a channel
    the host fills in more tasks than it keeps in flight: a fill reports
    done before its data leaves the shim. A version's schedule must not run a part before one it reads, nor
    overlap or merge calls where a step writes a buffer that outlasts the
    call, and on an xclbin per step it takes no phased region and no
    teardown; its calls a command (``Recording.repeated``) must write no
    more scratchpad words than a command holds, nor, where the driver's
    watchdog is readable and every step has a cached standalone time
    (``measure.Cache``), outrun the watchdog over ``WATCHDOG_HEADROOM`` as
    the tuner's preflight holds a command; where either is unknown, as
    there, nothing is refused and the log says which.

    A refusal from any stage of any entry wins over what is not fitted yet;
    only where nothing refuses is the first of those raised.

    Args:
        profile: The profile whose compositions are fitted.
        calls: The graph's calls, every version.
        device: The device.
        placements: The placer's settings a fit may try.
        max_images: The images the host may hold loaded at once; None for no limit.

    Raises:
        ValueError: An entry matches none of the calls' steps, a schedule
            none of their versions, a schedule orders a part its entries do
            not name, or a region names other than a phase per edge.
        NotImplementedError: What is not fitted yet, where nothing refuses:
            images held at once, a schedule's choices past its packaging,
            variants, bindings, fusion or packing entries, a configuration
            the composer does not build, an entry rooted at a step, scoped
            to some runs of its shape, splitting a step by
            fission, a placer setting the build does not take
            (``BUILT_PLACERS``), a region the composer does not build, and
            what the analysis does not model (``Derivation``).
    """
    waiting = [
        f"fitting {kind} is not built yet"
        for kind, kept in (
            ("images held at once", max_images is not None),
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
    cascade_cols = model.columns()
    cascade_rows = sum(model.is_core_tile(0, r) for r in rows)
    held_in = {
        EdgeKind.STREAM: ("a core tile", model.get_local_memory_size(), None),
        EdgeKind.STAGED: (
            "a memtile",
            model.get_mem_tile_size(),
            model.get_num_bds(0, mem_row),
        ),
    }
    shim_row = next(r for r in rows if model.is_shim_noc_tile(0, r))
    queue = model.get_dma_task_queue_depth()
    entries = profile.entries()
    concurrent: dict[int, list[Configuration]] = {}
    for entry in entries:
        root = entry.root
        if isinstance(root, Configuration):
            if root.teardown and root.resident:
                return Fit(
                    False,
                    "analysis",
                    f"it keeps {', '.join(root.resident)} on chip into the next "
                    f"configuration, across its own teardown",
                )
            if root.columns is not None and root.columns > model.columns():
                return Fit(
                    False,
                    "counts",
                    f"it takes {root.columns} columns; {device.resolve()} has "
                    f"{model.columns()}",
                )
            if root.concurrent is not None:
                concurrent.setdefault(root.concurrent, []).append(root)
        parts: list[Configuration | Region | Member] = [root]
        while parts:
            part = parts.pop()
            if isinstance(part, Member):
                continue
            parts += part.parts
            if not isinstance(part, Region):
                continue
            plan = part.runtime
            if plan is not None and (plan.in_flight or 0) > queue:
                return Fit(
                    False,
                    "counts",
                    f"its runtime plan keeps {plan.in_flight} tasks in flight a "
                    f"channel; a channel's task queue holds {queue}",
                )
            if (
                plan is not None
                and plan.chained
                and plan.chunks > model.get_num_bds(0, shim_row)
            ):
                return Fit(
                    False,
                    "counts",
                    f"its runtime plan chains {plan.chunks} chunks into one task, a "
                    f"buffer descriptor each; a shim tile has "
                    f"{model.get_num_bds(0, shim_row)}",
                )
            if part.phases is None:
                continue
            if len(part.phases) != len(part.edges):
                raise ValueError(
                    f"{part} names {len(part.phases)} phases for "
                    f"{len(part.edges)} edges, a phase per edge"
                )
            phase: dict[int, int] = {}
            for e, p in zip(part.edges, part.phases):
                if phase.setdefault(e.consumer, p) != p:
                    return Fit(
                        False,
                        "analysis",
                        f"step {e.consumer}'s edges name phases "
                        f"{phase[e.consumer]} and {p}; a step runs in one phase",
                    )
            for e, p in zip(part.edges, part.phases):
                made = phase.get(e.producer, 0)
                if not e.across_calls and made > p:
                    return Fit(
                        False,
                        "analysis",
                        f"{e} runs its consumer in phase {p}, before its producer "
                        f"in phase {made}",
                    )
                if e.kind is EdgeKind.STREAM and made < p:
                    return Fit(
                        False,
                        "analysis",
                        f"{e} is a stream from phase {made} into phase {p}: a value "
                        f"crossing a phase boundary waits in a memtile or DDR, "
                        f"and a stream holds it in neither",
                    )
    for schedule in profile.schedules():
        if schedule.packaging == "full_elf" and not device.can_dispatch_full_elf:
            return Fit(
                False,
                "counts",
                f"its schedule packages a full ELF; {device.resolve()} has no "
                f"full-ELF dispatch",
            )
    matched: set[int] = set()
    scheduled: set[int] = set()
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
        # The rest is fitted as built: its version as its schedule runs it.
        single = recording
        try:
            with set_current_device(device):
                recording = single.scheduled(profile)
        except NotImplementedError as e:
            waiting.append(str(e))
        except ValueError as e:
            return Fit(False, "counts", f"{single.name} as its schedule builds it: {e}")
        readers, writers = recording.users()
        spans: list[tuple[int, ...]] = []
        applied: list[Configuration | Region | Member] = []
        together: dict[int, list[tuple[tuple[int, ...], Entry]]] = {}
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
            found = recording.occurrences(entry)
            if not found:
                continue
            matched.add(index)
            inside = set(found[0])
            applied.append(region)
            xclbin = any(
                s.version == recording.version and s.packaging == "xclbin"
                for s in profile.schedules()
            )
            for part in (region, *(() if isinstance(region, Member) else region.parts)):
                if xclbin and isinstance(part, Configuration) and part.teardown:
                    return Fit(
                        False,
                        "analysis",
                        "a configuration torn down after use on an xclbin per "
                        "step, which leaves no configuration to undo",
                    )
                if (
                    xclbin
                    and isinstance(part, Region)
                    and (
                        part.phases is not None
                        or any(
                            e.kind is EdgeKind.DDR and not e.across_calls
                            for e in part.edges
                        )
                        or (
                            part is region
                            and memory_waits(recording, found[0], part.edges)
                        )
                    )
                ):
                    return Fit(
                        False,
                        "analysis",
                        "a phased region on an xclbin per step: phases run in turn "
                        "as a full ELF's sequences",
                    )
            at = 0
            for part in region.parts if not isinstance(region, Member) else (region,):
                spans.append(found[0][at : at + len(part.steps())])
                at += len(part.steps())
            frontier = [o for s in inside for o in after[s] if o not in inside]
            seen = set(frontier)
            # A configuration's parts run in turn, steps outside it between them.
            while frontier and not (
                isinstance(region, Configuration) and region.concurrent is None
            ):
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
            if isinstance(region, Member):
                waiting.append("fitting an entry rooted at a Member is not built yet")
                continue
            if isinstance(region, Configuration) and region.concurrent is not None:
                together.setdefault(region.concurrent, []).append((found[0], entry))
            if isinstance(region, Configuration):
                verdict = _configuration_fit(
                    region,
                    found[0],
                    recording,
                    timed.values,
                    after,
                    device,
                    cores_on_array // model.columns(),
                    placements,
                )
                if isinstance(verdict, Fit):
                    return verdict
                waiting += verdict
                continue
            if entry.scope.occurrences is not None:
                waiting.append(
                    "an entry scoped to some runs of its shape is not built yet: "
                    "IRON applies an entry to every run"
                )
                continue
            if region.workers:
                alone = Profile()
                alone.add_entry(entry)
                try:
                    with set_current_device(device):
                        folds = composed_folds(recording, alone)
                except ValueError as e:  # IRON's fold, unresolvable here
                    return Fit(False, "counts", f"the fold of its steps: {e}")
                # Not a fold: the composer joins its cores, counted below.
                fold = folds[0] if folds else None
                if fold is not None:
                    folded = apply_folds(recording, [fold]).steps[fold.steps[0]].op
                    with set_current_device(device):
                        refused = refusal(folded)
                    if refused is not None and set(placements) != {"sequential"}:
                        waiting.append(
                            f"the sequential placer refuses the fold ({refused}); "
                            f"trying the others is not built yet"
                        )
                    elif refused is not None:
                        return Fit(False, "placer", refused)
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
            core = {s: min(worker) for worker in region.workers for s in worker}
            links = [
                (core.get(e.producer, e.producer), core.get(e.consumer, e.consumer))
                for e in region.edges
                if e.kind is EdgeKind.CASCADE
            ]
            for p, c in links:
                if p == c:
                    return Fit(
                        False,
                        "counts",
                        f"a cascade runs from one core to the next; steps "
                        f"{p} and {c} share one",
                    )
            for end, side in ((0, "output"), (1, "input")):
                ends = Counter(link[end] for link in links)
                if ends and max(ends.values()) > 1:
                    step, n = ends.most_common(1)[0]
                    return Fit(
                        False,
                        "counts",
                        f"a core has one cascade {side}; step {step}'s takes {n}",
                    )
            following = dict(links)
            reach = cascade_cols + cascade_rows - 1
            for first in following:
                chain, at = [first], first
                while at in following and following[at] not in chain:
                    at = following[at]
                    chain.append(at)
                if at in following or len(chain) > reach:
                    return Fit(
                        False,
                        "counts",
                        f"a cascade chain of {len(chain)} cores"
                        + (", closing a cycle," if at in following else "")
                        + f" runs only east or south, through at most {reach} "
                        f"cores of {device.resolve()}'s {cascade_cols} columns and "
                        f"{cascade_rows} rows",
                    )
            try:
                derivation = Derivation(region, recording, device, timed.values)
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
            plan = region.runtime
            if plan is not None and plan.waits == "per_channel" and not plan.chained:
                on_chip = {
                    (p, e.output)
                    for e, p, _ in derivation.wired
                    if e.kind is not EdgeKind.DDR
                } | {
                    (c, e.input)
                    for e, _, c in derivation.wired
                    if e.kind is not EdgeKind.DDR
                }
                for s, ((_, recorded), lanes) in enumerate(
                    zip(derivation.recorded, derivation.lanes)
                ):
                    owner = {f: name for name, fifos in lanes.items() for f in fifos}
                    tasks = Counter(
                        t.fifo
                        for t in recorded.transfers
                        if t.kind == "fill" and (s, owner.get(t.fifo)) not in on_chip
                    )
                    for fifo, n in tasks.items():
                        if n * plan.chunks > (plan.in_flight or queue):
                            return Fit(
                                False,
                                "analysis",
                                f"step {s} ({type(derivation.ops[s]).__name__}) "
                                f"fills {fifo.name} from the host in "
                                f"{n * plan.chunks} tasks a call, "
                                f"{plan.in_flight or queue} in flight, each "
                                f"awaited on its own channel: the channel is "
                                f"reused once a fill reports done, which it does "
                                f"before its data leaves the shim, not a sure await",
                            )
            unplaceable = []
            for edge, p, _ in derivation.wired:
                # Spliced, an edge holds each core's own tile.
                elements = (
                    int(np.prod(derivation.spliced[edge][0][2].shape))
                    if edge in derivation.spliced
                    else derivation.obj_elements[p].get(edge.output)
                )
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
            # A region with no edge hands nothing on-chip: nothing to analyse.
            if region.edges:
                try:
                    analysis = derivation.analysis()
                except NotImplementedError as e:
                    waiting.append(str(e))
                    continue
                if analysis.why is not None:
                    return Fit(False, "analysis", analysis.why)
                for edge, p, c in derivation.wired:
                    if edge.kind not in (EdgeKind.STREAM, EdgeKind.CASCADE):
                        continue
                    # A broadcast's lanes meet as they are, each read by
                    # several: a cascade's relay is one of them.
                    shape = analysis.hand_off[edge]
                    if shape not in (HandOff.EQUAL, HandOff.BROADCAST):
                        return Fit(
                            False,
                            "analysis",
                            f"{edge} is a {edge.kind.value}, whose lanes meet as "
                            f"they are; its {shape.value} hand-off needs a restage",
                        )
                why = analysis.deadlock(
                    {e: e.depth for e, _, _ in derivation.wired if e.depth is not None}
                )
                if why is not None:
                    return Fit(False, "analysis", f"at its chosen depths, it {why}")
            kept = sorted(
                {
                    (p, edge.output)
                    for edge, p, _ in derivation.wired
                    if edge.kind is not EdgeKind.DDR
                    and (
                        set(readers.get(derivation.refs[p][edge.output].root, []))
                        - inside
                        or derivation.refs[p][edge.output].root in recording.held
                        or any(
                            (d.producer, d.output) == (edge.producer, edge.output)
                            and d.kind is EdgeKind.DDR
                            for d in region.edges
                        )
                    )
                }
            )
            for edge, p, c in derivation.wired:
                made = derivation.obj_elements[p].get(edge.output)
                taken = derivation.obj_elements[c].get(edge.input)
                if (
                    edge.kind in (EdgeKind.STREAM, EdgeKind.CASCADE)
                    and made is not None
                    and taken is not None
                    and made != taken
                ):
                    unplaceable.append(
                        f"{edge}: a {edge.kind.value} whose ends' objects differ "
                        f"({made} elements and {taken}) is not built yet; the "
                        f"composer gives a fifo one object size"
                    )
            kinds = {e.kind for e in region.edges if not e.across_calls}
            unplaceable += [
                f"placing a region with {what} is not built yet: the composer "
                f"does not build it"
                for what, named in (
                    ("inflows", region.inflows),
                    (
                        "nested regions",
                        not all(isinstance(part, Member) for part in region.parts),
                    ),
                )
                if named
            ]
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
            position = {s: i for i, s in enumerate(found[0])}
            ordered = [
                (position[a], position[b])
                for a, b in memory_waits(recording, found[0], region.edges)
            ]
            tried = [s for s in placements if s in BUILT_PLACERS]
            refusals: list[str] = []
            with set_current_device(device):
                try:
                    for setting in tried:
                        refused = group_fit_verdict(
                            derivation.ops,
                            kind=(
                                (
                                    FusionKind.STAGED
                                    if EdgeKind.STAGED in kinds
                                    else FusionKind.STREAM
                                )
                                if kinds or ordered
                                else None
                            ),
                            edges=[
                                (e.producer, e.output, e.consumer, e.input)
                                for e in region.edges
                                if e.kind in (EdgeKind.STREAM, EdgeKind.STAGED)
                            ],
                            cascades=[
                                (e.producer, e.output, e.consumer, e.input)
                                for e in region.edges
                                if e.kind is EdgeKind.CASCADE
                            ],
                            kept=kept,
                            depths={
                                (e.producer, e.output): e.depth
                                for e in region.edges
                                if e.depth is not None and e.kind is not EdgeKind.DDR
                            },
                            waits=[
                                *(
                                    (e.producer, e.consumer)
                                    for e in region.edges
                                    if e.kind is EdgeKind.DDR and not e.across_calls
                                ),
                                *ordered,
                            ],
                            workers=region.workers,
                            phases=region.step_phases(),
                            placer=BUILT_PLACERS[setting],
                        )
                        if refused is None:
                            break
                        refusals.append(refused)
                except NotImplementedError as e:
                    waiting.append(str(e))
                    continue
            if len(refusals) < len(tried):
                continue
            untried = [s for s in placements if s not in BUILT_PLACERS]
            if untried:
                waiting.append(
                    f"the placer refuses it under {', '.join(tried)} ({refusals[0]}); "
                    f"trying {', '.join(untried)} is not built yet: the build places "
                    f"only as {', '.join(BUILT_PLACERS)} do"
                )
            else:
                return Fit(False, "placer", refusals[0])
        for group, at_once in together.items():
            refused = _independent(
                [span for span, _ in at_once],
                after,
                recording,
                f"configurations concurrent as {group}",
            )
            if refused is not None:
                return refused
            alone = Profile()
            for _, entry in at_once:
                alone.add_entry(entry)
            try:
                with set_current_device(device):
                    tunables, packs = composed(recording, alone)
            except NotImplementedError as e:
                waiting.append(str(e))
                continue
            for pack in packs:
                with set_current_device(device):
                    ops = [
                        recording.steps[s]
                        .op._with_tunables(**tunables.get(s, {}))
                        .resolved(device)
                        for s in pack.steps
                    ]
                    refused = group_fit_verdict(ops, kind=FusionKind.PACK)
                if refused is not None and set(placements) != {"sequential"}:
                    waiting.append(
                        f"the sequential placer refuses steps {pack.steps} at once "
                        f"({refused}); trying the others is not built yet"
                    )
                elif refused is not None:
                    return Fit(False, "placer", refused)
        persist = (
            set(recording.feedback)
            | {h.ref().root for _, h in recording.states.values()}
            | {h.ref().root for h in recording.inputs}
            | set(recording.pinned)
            | set(recording.residents)
        )
        carried = [
            (root, w)
            for root, ws in writers.items()
            if root in persist
            for w in sorted(set(ws) - {-1})[:1]
        ]
        for number, schedule in enumerate(profile.schedules()):
            if schedule.version != recording.version:
                continue
            scheduled.add(number)
            for a, b in schedule.order:
                if not 0 <= min(a, b) <= max(a, b) < len(spans):
                    raise ValueError(
                        f"{schedule} orders part {max(a, b)}; the entries in "
                        f"{recording.name} name {len(spans)} parts"
                    )
                reads = sorted(_reached(spans[b], after) & set(spans[a]))
                if reads:
                    return Fit(
                        False,
                        "analysis",
                        f"its schedule runs part {a} (step {reads[0]}, "
                        f"{type(recording.steps[reads[0]].op).__name__}) before part "
                        f"{b}, whose output it reads",
                    )
            for what, kept in (
                ("overlapping calls", schedule.calls_overlapped),
                (f"a merge of calls into {schedule.size!r}", schedule.size),
            ):
                if kept and carried:
                    root, w = carried[0]
                    return Fit(
                        False,
                        "analysis",
                        f"{what} breaks a dependence: step {w} "
                        f"({type(recording.steps[w].op).__name__}) writes {root}, "
                        f"which outlasts the call, so a call depends on the one "
                        f"before",
                    )
            if schedule.calls_per_command > 1:
                if recording.calls > 1:
                    words, _ = _words(recording, share=True, extents=False)
                    if len(words) > SCRATCHPAD_WORDS:
                        return Fit(
                            False,
                            "counts",
                            f"its {schedule.calls_per_command} calls a command "
                            f"write {len(words)} scratchpad words; a command's "
                            f"scratchpad holds {SCRATCHPAD_WORDS}",
                        )
                limit = watchdog_s()
                unknown = (
                    "the driver's watchdog is not readable" if limit is None else None
                )
                total_us = 0.0
                if unknown is None:
                    try:
                        cache = Cache.here()
                    except (OSError, subprocess.CalledProcessError, RuntimeError):
                        unknown = "xrt-smi reports no platform to key cached times"
                for i, step in enumerate(single.steps if unknown is None else ()):
                    with set_current_device(device):
                        measured = cache.get(cache.key(step.op, dict(timed.values)))
                    if measured is None:
                        unknown = f"step {i} has no cached standalone time"
                        break
                    total_us += measured.t_step_us
                if unknown is not None:
                    logger.info(
                        "fit: %s's %d calls a command are not held to the "
                        "watchdog: %s",
                        recording.name,
                        schedule.calls_per_command,
                        unknown,
                    )
                elif (
                    limit is not None
                    and limit
                    < WATCHDOG_HEADROOM * schedule.calls_per_command * total_us / 1e6
                ):
                    return Fit(
                        False,
                        "counts",
                        f"its {schedule.calls_per_command} calls a command take "
                        f"about {schedule.calls_per_command * total_us / 1e6:.2f} "
                        f"s; the driver's watchdog ({limit:g} s) allows "
                        f"1/{WATCHDOG_HEADROOM:g} of it",
                    )
            waiting += [
                f"building a schedule's {what} is not built yet"
                for what, kept in (
                    ("order beyond dependences", schedule.order),
                    ("recomputed steps", schedule.recompute),
                    ("calls overlapped", schedule.calls_overlapped),
                    (
                        "several calls a command, merged calls or commands in "
                        "flight on an xclbin per step",
                        (
                            schedule.commands_in_flight != 1
                            or schedule.calls_per_command != 1
                            or schedule.size is not None
                        )
                        and (
                            schedule.packaging == "xclbin"
                            or not device.can_dispatch_full_elf
                        ),
                    ),
                    ("versions interleaved", schedule.interleave_with),
                )
                if kept
            ]
    # A width left to the placer was placed with its pack, above.
    for group, at_once in concurrent.items():
        taken = sum(c.columns for c in at_once if c.columns is not None)
        if len(at_once) > 1 and taken > model.columns():
            return Fit(
                False,
                "placer",
                f"the configurations running at once as {group} take {taken} "
                f"columns; {device.resolve()} has {model.columns()}, so they cannot "
                f"be disjoint",
            )
    unmatched = [e for n, e in enumerate(profile.entries()) if n not in matched]
    if unmatched:
        raise ValueError(f"{unmatched[0]} matches none of the calls' steps")
    unscheduled = [s for n, s in enumerate(profile.schedules()) if n not in scheduled]
    if unscheduled:
        raise ValueError(f"{unscheduled[0]} schedules none of the calls' versions")
    if waiting:
        raise NotImplementedError(waiting[0])
    return Fit(True)


def _reached(steps: Sequence[int], after: Sequence[set[int]]) -> set[int]:
    """Return ``steps`` and every step on a path (``after``, each step's later readers) from one of them."""
    reached = set(steps)
    frontier = list(steps)
    while frontier:
        found = after[frontier.pop()] - reached
        reached |= found
        frontier += found
    return reached


def _independent(
    spans: Sequence[tuple[int, ...]],
    after: Sequence[set[int]],
    recording: Recording,
    what: str,
) -> Fit | None:
    """Return the refusal of ``spans``, steps run at once as ``what``, where a step of one is on a path from another's; None where they are independent."""
    for k, span in enumerate(spans):
        reached = _reached(span, after)
        for j, other in enumerate(spans):
            depends = sorted(reached & set(other)) if j != k else []
            if depends:
                return Fit(
                    False,
                    "analysis",
                    f"{what} run at once, but step {depends[0]} "
                    f"({type(recording.steps[depends[0]].op).__name__}) depends on "
                    f"steps {span}: what runs at once must be independent, no "
                    f"written data shared",
                )
    return None


def _configuration_fit(
    configuration: Configuration,
    match: tuple[int, ...],
    recording: Recording,
    values: Mapping[str, int],
    after: Sequence[set[int]],
    device: Device,
    core_rows: int,
    placements: Sequence[str],
) -> Fit | list[str]:
    """Return ``configuration``'s refusal at ``match``, its steps in ``recording``, or what is not fitted of it yet.

    Parts that run at once (``Configuration.concurrent``) must be
    independent: no step of one on a path (``after``) from another's. The
    cores its steps take are then counted against the array, or the
    ``columns`` it is given, ``core_rows`` cores each: steps of one array
    share its cores unless they run at once, and a region's steps each take
    their own, as a fusion's members do, steps sharing a worker counted once.
    A configuration of steps alone is placed last, as one device
    configuration, as a packing is.

    Args:
        configuration: The configuration fitted.
        match: The recording's step each of its steps is, depth-first.
        recording: The recording it is matched in.
        values: The call's per-call values (``Timed.values``).
        after: Each step's readers later in the recording.
        device: The device.
        core_rows: The core tiles a column holds.
        placements: The placer's settings a fit may try.

    Returns:
        A ``Fit`` refusing it, or each thing not fitted yet.
    """
    spans = []
    at = 0
    for part in configuration.parts:
        spans.append(match[at : at + len(part.steps())])
        at += len(part.steps())
    if configuration.concurrent is not None:
        refused = _independent(spans, after, recording, "its parts")
        if refused is not None:
            return refused
    try:
        derivation = Derivation(Region(configuration.parts), recording, device, values)
    except NotImplementedError as e:
        return [str(e)]
    cores = [len(recorded.cores) for _, recorded in derivation.recorded]
    arrays: dict[object, int] = {}
    own = 0
    at = 0
    for part in configuration.parts:
        steps = range(at, at + len(part.steps()))
        at += len(part.steps())
        if isinstance(part, Member) and configuration.concurrent is None:
            key = derivation.ops[steps[0]].array_key()
            arrays[key] = max(arrays.get(key, 0), cores[steps[0]])
            continue
        workers = part.workers if isinstance(part, Region) else ()
        shared = {s for worker in workers for s in worker}
        own += sum(cores[s] for k, s in enumerate(steps) if k not in shared)
        own += sum(max(cores[steps[k]] for k in worker) for worker in workers)
    needed = own + sum(arrays.values())
    width = device.cols if configuration.columns is None else configuration.columns
    if needed > width * core_rows:
        return Fit(
            False,
            "counts",
            f"its steps take {needed} cores; "
            + (
                f"{device.resolve()} has {width * core_rows}"
                if configuration.columns is None
                else f"its {width} columns hold {width * core_rows}"
            ),
        )
    unbuilt = [
        f"building a configuration with {what} is not built yet"
        for what, kept in (
            ("a partial width", configuration.columns is not None),
            ("buffers resident into the next", configuration.resident),
            (
                "a switch other than a reload",
                configuration.switch not in (None, Switch.RELOAD),
            ),
            (
                "regions among its parts",
                not all(isinstance(p, Member) for p in configuration.parts),
            ),
        )
        if kept
    ]
    if unbuilt or configuration.concurrent is not None:
        return unbuilt  # parts run at once are placed as their pack, in fit
    with set_current_device(device):
        designs = {OperatorDesign(op).name: op for op in derivation.ops}
        refused = group_fit_verdict(list(designs.values()))
    if refused is not None and set(placements) != {"sequential"}:
        return [
            f"the sequential placer refuses it ({refused}); trying "
            f"{', '.join(s for s in placements if s != 'sequential')} is not "
            f"built yet"
        ]
    if refused is not None:
        return Fit(False, "placer", refused)
    return []


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
    is timed). A version whose schedule runs several calls a command or
    keeps commands in flight runs its draws so batched instead, against them
    called one at a time (``_batched``). Calls that hold state run in order
    instead, each side's
    states carried into its next call (``_in_order``). A call checked apart
    that carries values to the next (``Recording.carry``) and is not given
    them starts each at both ends of its recorded range (``Recording.limits``),
    as a first call may. Held to ``NO_WORSE``,
    each call is instead no worse than the base's against its reference
    (``_no_worse``).

    Args:
        profile: The profile checked.
        base: The profile it is held to.
        calls: The graph's calls.
        device: The device.
        refinement: The rule it is held to.
        base_calls: The calls ``base`` runs, where they are not ``calls``
            (the operator a graph replaces): one for each of ``calls``, in
            their order. Each returns its call's outputs; held ``EXACT`` it
            takes its call's inputs as they are, held ``NO_WORSE`` it reads
            some of them, by name.

    Raises:
        ValueError: ``profile`` does not fit, an entry matches none of the
            calls (``fit``), a call leaves the host nothing to compare, or
            ``base_calls`` does not pair with ``calls`` as above (or pairs
            calls of one version with base calls of several).
        NotImplementedError: What is not checked yet: a no-worse call that
            carries state (``_no_worse``), a call checked apart that carries
            a value to the next with no range recorded to start it in, and
            what ``fit`` or the composer (``composed``) does not take yet.
    """
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
    olds = list(calls if base_calls is None else base_calls)
    if len(olds) != len(calls):
        raise ValueError(
            f"{len(calls)} calls and {len(olds)} base calls: base_calls holds one "
            f"for each call, in their order"
        )
    pairs = list(zip(calls, olds, strict=True))
    versions: dict[Version, Version] = {}
    for call, old in pairs:
        new, was = call.recording, old.recording
        if versions.setdefault(new.version, was.version) != was.version:
            raise ValueError(
                f"{new.name}: calls of its version pair with base calls of several "
                f"versions, so neither side builds the version once"
            )
        takes, gives = (
            [(h.name, tuple(h.shape), np.dtype(h.dtype)) for h in r.inputs]
            for r in (was, new)
        )
        if refinement is Refinement.NO_WORSE:
            unread = [t[0] for t in takes if t not in gives]
        else:
            unread = [] if takes == gives else [t[0] for t in takes]
        if unread:
            raise ValueError(
                f"{was.name} is held against {new.name}, which does not give it "
                f"{', '.join(unread)} by name, shape and dtype"
                + ("" if refinement is Refinement.NO_WORSE else ", in order")
            )
        returns, returned = (
            {(h.name, tuple(h.shape), np.dtype(h.dtype)) for h in r.returned}
            for r in (was, new)
        )
        if returns != returned:
            raise ValueError(
                f"{was.name} returns {sorted(n for n, *_ in returns)} and "
                f"{new.name} {sorted(n for n, *_ in returned)}: not one result to "
                f"hold them to"
            )
    if refinement is Refinement.NO_WORSE:
        for call, old in pairs:
            why = _no_worse(profile, base, call, old, device)
            if why is not None:
                return Check(False, refinement, why)
        return Check(True, refinement)
    apart = []
    for call, old in pairs:
        batching = [
            s
            for s in profile.schedules()
            if s.version == call.recording.version
            and (
                s.commands_in_flight > 1
                or s.calls_per_command > 1
                or s.size is not None
            )
        ]
        if not batching:
            apart.append((call, old))
            continue
        why = _batched(profile, base, call, old, device, batching[0])
        if why is not None:
            return Check(False, refinement, why)
    started = []
    for call, old in apart:
        recording = call.recording
        unfed = sorted(set(recording.carry) - set(call.values))
        # A carry no caller starts starts at each end of its recorded range, so
        # an offset read wrongly at one end shows at the other.
        ends = {
            name: sorted(
                {
                    k
                    for limit in recording.limits
                    if limit.plus is None and limit.expression.value.name == name
                    for k in (limit.lo, limit.hi - 1)
                    if limit.evaluate({name: k}) == k
                }
            )
            for name in unfed
        }
        bare = [name for name, at in ends.items() if not at]
        if bare:
            raise NotImplementedError(
                f"{recording.name}: checking calls that carry {', '.join(bare)} "
                f"from one to the next, one call apart, is not built yet: no first "
                f"call starts the carry, and no recorded range says where it may"
            )
        if unfed:
            points = [
                {**call.values, **{name: at[k] for name, at in ends.items()}}
                for k in (0, -1)
            ]
            for point in points:
                recording.check_limits(point)
            call, old = (
                dataclasses.replace(
                    side,
                    values=points[0],
                    points=tuple(Point(1 / len(points), p) for p in points),
                )
                for side in (call, old)
            )
        started.append((call, old))
    apart = started
    if len(apart) > 1 and any(call.recording.states for call, _ in apart):
        why = _in_order(profile, base, apart, device)
        return Check(why is None, refinement, why)
    for call, old in apart:
        why = _bit_identical(profile, base, call, old, device)
        if why is not None:
            return Check(False, refinement, why)
    return Check(True, refinement)


def _batched(
    profile: Profile,
    base: Profile,
    call: Timed,
    old: Timed,
    device: Device,
    schedule: Schedule,
) -> str | None:
    """Return how ``call``'s draws, run as ``schedule`` batches them under ``profile``, first differ from them called one at a time under ``base``, or None.

    ``calls * (2 * commands_in_flight + 1)`` calls, ``calls`` the version's
    a command (``Recording.calls``: back to back, or merged into one), each on
    its seeded draw, in turn at the call's values and at each of its bounds
    halved (``_bound_points``), so calls of one command differ, from one set
    of seeded states:
    batched through ``CarriedLoop.calls`` (where the version carries values,
    the first call's, the Emit giving the rest), ``calls`` a command and
    ``commands_in_flight`` commands in flight; apart each an ordinary call.
    Every returned output of each call, and every state after the last, must
    be bit-identical.

    Raises:
        NotImplementedError: ``base`` batches the version's calls too.
    """
    recording = call.recording
    points = [dict(call.values), *_bound_points(recording, dict(call.values))]
    with set_current_device(device):
        graphs = (
            Applied.of(old, base, device).built(device),
            Applied.of(call, profile, device).built(device),
        )
    if graphs[0].recording.calls > 1:
        raise NotImplementedError(
            "checking a batched schedule against a base that batches too is not "
            "built yet"
        )
    per, depth = graphs[1].recording.calls, schedule.commands_in_flight
    draws = [drawn_inputs(recording, seed) for seed in range(per * (2 * depth + 1))]
    at = [points[k % len(points)] for k in range(len(draws))]
    rng = np.random.default_rng(len(draws))
    states = {h.name: _random_tensor(h, rng) for _, h in recording.states.values()}
    owns = [{h.name: s for s, h in g.recording.states.values()} for g in graphs]
    try:
        for graph, own in zip(graphs, owns, strict=True):
            for name, content in states.items():
                graph.write(own[name], content)
        apart = []
        for tensors, values in zip(draws, at, strict=True):
            graphs[0](*tensors, **values)
            apart.append(graphs[0].returned())
        with set_current_device(device):
            loop = CarriedLoop(graphs[1], graphs[1], depth)
            batched = loop.calls(
                [
                    (tensors, values) if k == 0 or graphs[1].emit is None else ((), {})
                    for k, (tensors, values) in enumerate(zip(draws, at, strict=True))
                ]
            )
        for k, (want, got) in enumerate(zip(apart, batched, strict=True)):
            differ = [n for n in want if not np.array_equal(want[n], got[n])]
            if differ:
                return (
                    f"{recording.name}: call {k} of {len(draws)}, {per} a command "
                    f"and {depth} in flight: {', '.join(differ)} not bit-identical"
                )
        differ = [
            name
            for name in states
            if not np.array_equal(
                graphs[0].read(owns[0][name]), graphs[1].read(owns[1][name])
            )
        ]
        if differ:
            return (
                f"{recording.name}: after {len(draws)} calls, {per} a command and "
                f"{depth} in flight: {', '.join(differ)} not bit-identical"
            )
    finally:
        for graph in graphs:
            graph.release()
    return None


def _bit_identical(
    profile: Profile, base: Profile, call: Timed, old: Timed, device: Device
) -> str | None:
    """Return how ``call`` under ``profile`` first differs from ``old`` under ``base`` (``compare_graphs``), or None."""
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
            return str(e)
    return None


def _no_worse(
    profile: Profile, base: Profile, call: Timed, old: Timed, device: Device
) -> str | None:
    """Return why ``call`` under ``profile`` is worse than ``old`` under ``base`` against the recording's reference, or None where it is no worse.

    A change upstream of a step that ``selects`` is held bit-identical
    instead, in what the selecting step reads as in every output: an error
    there, however small, can flip a choice. Otherwise, on each of
    ``NO_WORSE_DRAWS`` seeded draws (odd ones stress, their floats scaled
    over four decades), each returned output's error against
    ``Recording.reference`` must be no larger than ``old``'s in mean square
    and in its ``NO_WORSE_QUANTILE`` quantile of |e|, and finite; a
    bit-identical output ties. The reference is ``old``'s recording's, the
    untuned build's. An input whose contents ``call`` gives
    (``Timed.contents``) holds them on every draw, unscaled, and ``old``
    reads the inputs it takes by name.

    Raises:
        NotImplementedError: The call carries a buffer or a state to the
            next, or the host writes coded rows, which this does not hold
            yet.
    """
    recording = call.recording
    if recording.states or recording.feedback:
        raise NotImplementedError(
            "holding a call that carries state to no-worse is not built yet"
        )
    hosted = {h.ref().root for h in recording.inputs}
    if any(
        b.coded and h.ref().root in hosted
        for step in recording.steps
        for b, h in zip(step.op.buffers, step.slots, strict=True)
    ):
        raise NotImplementedError(
            "holding coded rows the host writes to no-worse (drawn as codes, "
            "their reference decoding them) is not built yet"
        )
    with set_current_device(device):
        before, after = Applied.of(old, base, device), Applied.of(call, profile, device)
        olds, news = before.fingerprint(device), after.fingerprint(device)
    if old.recording is recording:
        changed = {
            i for i, (a, b) in enumerate(zip(olds[0], news[0], strict=True)) if a != b
        } | {i for f in set(olds[1]) ^ set(news[1]) for i in f.steps}
    else:
        changed = set(range(len(recording.steps)))
    readers, _ = recording.users()
    reached = set(changed)
    frontier = list(changed)
    while frontier:
        for root in recording.steps[frontier.pop()].roots()[1]:
            for j in readers.get(root, []):
                if j >= 0 and j not in reached:
                    reached.add(j)
                    frontier.append(j)
    selecting = sorted(j for j in reached if recording.steps[j].op.selects)
    # Each buffer a selecting step reads, by root: held bit-identical, as
    # every output then is.
    watched = {
        slot.ref().root
        for j in selecting
        for b, slot in zip(
            recording.steps[j].op.buffers, recording.steps[j].slots, strict=True
        )
        if b.fills
    }
    values = dict(call.values)
    given = {
        h.name: call.contents[h.ref().root]
        for h in recording.inputs
        if h.ref().root in call.contents
    }
    with set_current_device(device):
        graphs = before.built(device), after.built(device)
    try:
        for draw in range(NO_WORSE_DRAWS):
            rng = np.random.default_rng(draw)
            tensors = {
                h.name: t
                for h, t in zip(
                    recording.inputs, drawn_inputs(recording, draw), strict=True
                )
            }
            tensors.update(given)
            if draw % 2:
                for h in recording.inputs:
                    if h.name in given:
                        continue
                    if np.dtype(h.dtype).kind == "f" or np.dtype(h.dtype).name == (
                        "bfloat16"
                    ):
                        scale = 10.0 ** rng.uniform(-2, 2, h.shape)
                        tensors[h.name] = (
                            tensors[h.name].astype(np.float64) * scale
                        ).astype(h.dtype)
            got = []
            for graph, side in zip(graphs, (old, call), strict=True):
                graph(*(tensors[h.name] for h in side.recording.inputs), **values)
                read = {
                    h.name: np.array(graph.read(h)[h.valid_index(values)])
                    for h in side.recording.returned
                }
                for step in side.recording.steps:
                    for slot in step.slots:
                        if slot.ref().root in watched and slot.ref().nbytes is None:
                            read.setdefault(
                                f"{slot.ref().root} (selected from)",
                                np.array(graph.read(slot)),
                            )
                got.append(read)
            if watched:
                differ = sorted(
                    name
                    for name in got[0].keys() | got[1].keys()
                    if name not in got[0]
                    or name not in got[1]
                    or got[0][name].view(np.uint8).tobytes()
                    != got[1][name].view(np.uint8).tobytes()
                )
                if differ:
                    return (
                        f"{recording.name}: the change reaches step {selecting[0]} "
                        f"({type(recording.steps[selecting[0]].op).__name__}), "
                        f"which selects, so only an exact change is taken there; "
                        f"on draw {draw} {', '.join(differ)} differ"
                    )
                continue
            want, _ = old.recording.reference(tensors, values)
            for h, ref in zip(old.recording.returned, want, strict=True):
                u, t = got[0][h.name], got[1][h.name]
                if np.array_equal(u.view(np.uint8), t.view(np.uint8)):
                    continue
                exact = np.asarray(ref, dtype=np.float64)
                errors = [np.abs(x.astype(np.float64) - exact) for x in (u, t)]
                ms = [float(np.mean(e**2)) for e in errors]
                tail = [float(np.quantile(e, NO_WORSE_QUANTILE)) for e in errors]
                if (
                    not np.isfinite([*ms, *tail]).all()
                    or ms[1] > ms[0]
                    or tail[1] > tail[0]
                ):
                    return (
                        f"{recording.name}: {h.name} is worse than before on draw "
                        f"{draw}: mean square {ms[1]:.3g} against {ms[0]:.3g}, "
                        f"{NO_WORSE_QUANTILE} |e| {tail[1]:.3g} against {tail[0]:.3g}"
                    )
    finally:
        for graph in graphs:
            graph.release()
    return None


def _in_order(
    profile: Profile,
    base: Profile,
    pairs: Sequence[tuple[Timed, Timed]],
    device: Device,
) -> str | None:
    """Run each pair's call under ``profile`` and its base call under ``base``, in order, states carried; return the first difference, or None.

    Each side carries its states into its next call. Each version is built once each way, so a repeated call keeps what it
    carries. The calls start from one set of seeded states, shared by name
    across versions, and each takes seeded inputs at its own values; after
    each, every output within its bound, carried buffer and state must be
    bit-identical.
    """
    rng = np.random.default_rng(0)
    seeded: dict[str, np.ndarray] = {}
    for call, _ in pairs:
        for _, h in call.recording.states.values():
            seeded.setdefault(h.name, _random_tensor(h, rng))
    sides = [dict(seeded), dict(seeded)]
    built: dict = {}
    try:
        for k, (call, old) in enumerate(pairs):
            recording = call.recording
            version = recording.version
            if version not in built:
                with set_current_device(device):
                    built[version] = (
                        Applied.of(old, base, device).built(device),
                        Applied.of(call, profile, device).built(device),
                    )
            graphs = built[version]
            inputs = drawn_inputs(recording, k)
            owns = [{h.name: s for s, h in g.recording.states.values()} for g in graphs]
            for graph, own, states in zip(graphs, owns, sides):
                for name, state in own.items():
                    graph.write(state, states[name])
                graph(*inputs, **call.values)
            before, after = graphs
            carried = [
                h
                for step in recording.steps
                for h in step.slots
                if h.ref().root in recording.feedback and h.ref().nbytes is None
            ]
            differ = [
                h.name
                for h in recording.outputs
                if not np.array_equal(
                    before.read(h)[h.valid_index(call.values)],
                    after.read(h)[h.valid_index(call.values)],
                )
            ] + [
                h.name
                for h in carried
                if not np.array_equal(before.read(h), after.read(h))
            ]
            for graph, own, states in zip(graphs, owns, sides):
                states.update((n, graph.read(s).copy()) for n, s in own.items())
            differ += [
                n for n in owns[0] if not np.array_equal(sides[0][n], sides[1][n])
            ]
            if differ:
                return (
                    f"{recording.name}, call {k} of {len(pairs)}: "
                    f"{', '.join(dict.fromkeys(differ))} not bit-identical"
                )
    finally:
        for graphs in built.values():
            for graph in graphs:
                graph.release()
    return None


def measure(
    profile: Profile,
    base: Profile,
    calls: Sequence[Timed],
    device: Device,
    timing: Timing = Timing(),
    refinement: Refinement = Refinement.EXACT,
) -> Measured:
    """Time ``calls`` built under ``profile`` against them built under ``base``, in pairs.

    ``profile`` must fit (``fit``). Each call is built both ways and timed
    interleaved on the NPU at each of its points, checked bit-identical as
    it goes where ``refinement`` is exact (``compare_graphs``); where either
    way batches the call's version (several calls a command, or commands in
    flight), batched, a call's time its batch's over its calls
    (``_time_batched``). A call's time is its points' medians,
    weighted; ``ratio`` weighs each point's median paired ratio by the
    base's time there.

    Args:
        profile: The profile timed.
        base: The profile it is timed against.
        calls: The graph's calls.
        device: The device.
        timing: How long each call is timed.
        refinement: How ``profile`` relates to ``base``: a no-worse one is
            timed without holding it bit-identical (``check`` holds it).

    Raises:
        ValueError: ``profile`` does not fit.
        NotBitIdentical: An exact call is not bit-identical built both ways.
        NotImplementedError: What ``fit`` or the composer does not take yet.
    """
    fitted = fit(profile, calls, device)
    if not fitted.ok:
        raise ValueError(f"the profile does not fit ({fitted.stage}): {fitted.why}")
    seconds = base_seconds = weighted = 0.0
    for call in calls:
        known = Compared()
        with set_current_device(device):
            applied = (
                Applied.of(call, base, device),
                Applied.of(call, profile, device),
            )
        if any(a.recording.calls > 1 or a.commands_in_flight > 1 for a in applied):
            _time_batched(
                call, applied, device, timing, known, refinement is Refinement.EXACT
            )
        else:
            with set_current_device(device):
                compare_graphs(
                    call,
                    applied[0].built(device),
                    applied[1].built(device),
                    timing=timing,
                    known=known,
                    log=logger.info,
                    exact=refinement is Refinement.EXACT,
                )
        for weight, values in call.timed_points():
            point = tuple(sorted(values.items()))
            was, now = known.medians[point]
            base_seconds += weight * was / 1e6
            seconds += weight * now / 1e6
            weighted += weight * was * known.ratios[point] / 1e6
    return Measured(weighted / base_seconds, seconds, base_seconds)


def _time_batched(
    call: Timed,
    applied: tuple[Applied, Applied],
    device: Device,
    timing: Timing,
    known: Compared,
    exact: bool,
) -> None:
    """Time ``call`` as each of ``applied`` (before, after) dispatches it, a call's time its batch's over its calls, into ``known``.

    At each of the call's points (``Timed.timed_points``), one batch of at
    least ``timing.calls`` calls, whole commands of both
    (``Recording.repeated``), each on its own seeded draw, runs through
    ``CarriedLoop.calls`` with each one's commands in flight, ``timing.rounds``
    rounds interleaved, half each way round, each from the same seeded states.
    A round before them is not timed: it makes each loop's runs, and where
    ``exact`` every call's returned outputs, within their bounds, must be
    bit-identical between the two. ``known`` takes each point's two medians,
    their difference and the median of the paired ratios.

    Raises:
        NotBitIdentical: ``exact``, and a call's returned output differs.
        NotImplementedError: One carries values, so its later calls take the
            Emit's values rather than the batch's.
    """
    recording = call.recording
    with set_current_device(device):
        graphs = [a.built(device) for a in applied]
    try:
        if any(g.emit is not None for g in graphs):
            raise NotImplementedError(
                f"{recording.name}: pricing batched calls of a version that carries "
                f"values is not built yet"
            )
        per = math.lcm(*(g.recording.calls for g in graphs))
        count = per * max(1, math.ceil(timing.calls / per))
        draws = [drawn_inputs(recording, seed) for seed in range(count)]
        rng = np.random.default_rng(count)
        states = {h.name: _random_tensor(h, rng) for _, h in recording.states.values()}
        owns = [{h.name: s for s, h in g.recording.states.values()} for g in graphs]
        with set_current_device(device):
            loops = [
                CarriedLoop(g, g, a.commands_in_flight)
                for g, a in zip(graphs, applied, strict=True)
            ]
            for _, values in call.timed_points():
                batch = [(tensors, values) for tensors in draws]
                seconds: tuple[list[float], list[float]] = ([], [])
                for r in range(timing.rounds + 1):
                    got = {}
                    for side in (1, 0) if r % 2 else (0, 1):
                        for name, content in states.items():
                            graphs[side].write(owns[side][name], content)
                        begun = time.perf_counter()
                        got[side] = loops[side].calls(batch)
                        seconds[side].append((time.perf_counter() - begun) / count)
                    if r or not exact:
                        continue
                    for k, (want, have) in enumerate(zip(got[0], got[1], strict=True)):
                        differ = [
                            h.name
                            for h in recording.returned
                            if not np.array_equal(
                                want[h.name][h.valid_index(values)],
                                have[h.name][h.valid_index(values)],
                            )
                        ]
                        if differ:
                            raise NotBitIdentical(
                                f"{recording.name}: call {k} of {count} batched at "
                                f"{values}: {', '.join(differ)} not bit-identical"
                            )
                was, now = (np.array(s[1:]) * 1e6 for s in seconds)
                point = tuple(sorted(values.items()))
                known.medians[point] = (float(np.median(was)), float(np.median(now)))
                known.ratios[point] = float(np.median(now / was))
                known.points[point] = (
                    known.medians[point][1] - known.medians[point][0],
                    None,
                )
                logger.info(
                    "measure: %s batched at %s: %.1f us a call before, %.1f after "
                    "(%d calls a command and %d in flight against %d and %d)",
                    recording.name,
                    values,
                    *known.medians[point],
                    graphs[1].recording.calls,
                    applied[1].commands_in_flight,
                    graphs[0].recording.calls,
                    applied[0].commands_in_flight,
                )
    finally:
        for graph in graphs:
            graph.release()


def search(
    calls: Sequence[Timed],
    start: Profile,
    device: Device,
    budget_s: float | None = None,
    max_images: int | None = None,
) -> Profile:
    """Return the fastest profile found from ``start`` that passes every check.

    In rounds, each from the profile the last one kept (``start`` first):
    each edit ``candidates`` yields from it is applied to it, fitted
    (``fit``; one that waits or is refused is passed over) and measured in
    place against it (``measure``); one under ``GAINS`` gains, and one
    that does not build, or builds wrong, is refused and logged. The gainers are
    then taken best first, each applied to the profile so far (a region and
    a tunable edit of the same steps compose; a region over steps an earlier
    one holds gives way to it, as a tunable an earlier one sets does): one
    the profile so far does not fit with (``fit``), or that builds what it
    builds, is passed over; a take is
    checked against ``start`` by its refinement (``check``) and measured
    against the profile so far, and kept where it still gains. The next
    round's ``candidates`` reach what composes on a take (a hold of an edge
    of a region it adds); an edit an earlier round priced is not priced
    again. The search ends at a round that keeps nothing, or at
    ``budget_s``.

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
    incumbent = start
    tried: set[str] = set()
    while budget_s is None or time.perf_counter() - begun < budget_s:
        base = incumbent
        priced: list[tuple[float, Edit]] = []
        edits = candidates(calls, base, device)
        while budget_s is None or time.perf_counter() - begun < budget_s:
            try:
                edit = next(edits)
            except StopIteration:
                break
            except NotImplementedError as e:
                logger.info("search: %s", e)
                break
            # Entry is unhashable, so an edit is known by its repr.
            if repr(edit) in tried:
                continue
            tried.add(repr(edit))
            edited = edit.apply(base)
            try:
                fitted = fit(edited, calls, device)
            except NotImplementedError as e:
                logger.info("search: %s waits: %s", edit, e)
                continue
            if not fitted.ok:
                logger.info(
                    "search: %s refused at %s: %s", edit, fitted.stage, fitted.why
                )
                continue
            try:
                ratio = measure(
                    edited,
                    base,
                    calls,
                    device,
                    timing=PRICING,
                    refinement=edit.refinement,
                ).ratio
            except NotBitIdentical as e:
                logger.warning("search: refused, built wrong: %s: %s", edit, e)
                continue
            except NotImplementedError as e:
                logger.info("search: %s waits: %s", edit, e)
                continue
            except (ValueError, RuntimeError, ir.MLIRError) as e:
                logger.warning("search: refused, does not build: %s: %s", edit, e)
                continue
            logger.info("search: %.3f for %s", ratio, edit)
            if ratio < GAINS:
                priced.append((ratio, edit))
        for ratio, edit in sorted(priced, key=lambda pair: pair[0]):
            try:
                edited = edit.apply(incumbent)
            except ValueError as e:
                # An earlier take replaced the entry it edits; the next round
                # proposes it again on what that take left.
                logger.info("search: %s gives way: %s", edit, e)
                continue
            # Priced against the round's base, it joins what the takes before
            # it left, which may not fit with it.
            try:
                fitted = fit(edited, calls, device)
            except NotImplementedError as e:
                logger.info("search: %s waits on what it joins: %s", edit, e)
                continue
            if not fitted.ok:
                logger.info(
                    "search: %s refused on what it joins at %s: %s",
                    edit,
                    fitted.stage,
                    fitted.why,
                )
                continue
            with set_current_device(device):
                same = all(
                    Applied.of(c, edited, device).fingerprint(device)
                    == Applied.of(c, incumbent, device).fingerprint(device)
                    for c in calls
                )
            if same:
                continue  # an earlier take decides what it names
            checked = check(edited, start, calls, device, edit.refinement)
            if not checked.ok:
                logger.info("search: %s is not bit-identical: %s", edit, checked.why)
                continue
            if (
                measure(
                    edited,
                    incumbent,
                    calls,
                    device,
                    timing=PRICING,
                    refinement=edit.refinement,
                ).ratio
                >= GAINS
            ):
                continue
            incumbent = edited
        if incumbent is base:
            break
    return incumbent
