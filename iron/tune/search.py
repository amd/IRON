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
from collections import Counter
from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from typing import Literal, Protocol

import numpy as np
from aie import ir
from aie.dialects.aie import get_target_model
from aie.iron.device import Device
from aie.utils import set_current_device

from ..common.declare import Profile
from ..common.declare.composition import (
    Entry,
    Hold,
    Member,
    Refinement,
    Region,
    refinement,
)
from ..common.graph.fold import apply_folds, composed_folds, fold_candidates
from ..common.graph.fusion import composed
from ..common.graph.sdf import Derivation
from ..common.image.step import Edge, EdgeKind, FusionKind, HandOff
from .autotune import Timed, refusal, settings
from .fusions import (
    Applied,
    Compared,
    NotBitIdentical,
    _random_tensor,
    compare_graphs,
    drawn_inputs,
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


# A chosen depth is an edge's minimum times a power of two up to this many
# doublings, beside its knee; past what a core or memtile holds, fit refuses.
DEPTH_DOUBLINGS = 4

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
    several; the analysis's own kind and minimum are the region edit's.

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
    cores = device.cols * len(device.core_rows)
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
            try:
                analysis = Derivation(root, recording, device).analysis()
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
    stream edge's lanes meet as they are (a cascade's one to one), and
    whether it runs at its chosen
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
            fission, more fifos to or
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
            on_chip = {
                (p, e.output)
                for e, p, _ in derivation.wired
                if e.kind is not EdgeKind.DDR
            } | {
                (c, e.input)
                for e, _, c in derivation.wired
                if e.kind is not EdgeKind.DDR
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
                    shape = analysis.hand_off[edge]
                    if shape not in (
                        (HandOff.EQUAL, HandOff.BROADCAST)
                        if edge.kind is EdgeKind.STREAM
                        else (HandOff.EQUAL,)
                    ):
                        return Fit(
                            False,
                            "analysis",
                            f"{edge} is a {edge.kind.value}, whose lanes meet one to "
                            f"one as they are; its {shape.value} hand-off needs a "
                            f"restage",
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
                or region.phases is not None
                or region.runtime is not None
                or not all(isinstance(part, Member) for part in region.parts)
                or not kinds <= {EdgeKind.STREAM, EdgeKind.STAGED, EdgeKind.DDR}
            ):
                unplaceable.append(
                    "placing a region the composer does not build yet (inflows, "
                    "chosen phases, a runtime plan, nesting, or cascade edges)"
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
                    kind=(
                        (
                            FusionKind.STAGED
                            if EdgeKind.STAGED in kinds
                            else FusionKind.STREAM
                        )
                        if kinds
                        else None
                    ),
                    edges=[
                        (e.producer, e.output, e.consumer, e.input)
                        for e in region.edges
                        if e.kind is not EdgeKind.DDR
                    ],
                    kept=kept,
                    depths={
                        (e.producer, e.output): e.depth
                        for e in region.edges
                        if e.depth is not None and e.kind is not EdgeKind.DDR
                    },
                    waits=[
                        (e.producer, e.consumer)
                        for e in region.edges
                        if e.kind is EdgeKind.DDR
                    ],
                    workers=region.workers,
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
    is timed). Calls that hold state run in order instead, each side's
    states carried into its next call (``_in_order``). Held to ``NO_WORSE``,
    each call is instead no worse than the base's against its reference
    (``_no_worse``).

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
        NotImplementedError: What is not checked yet: a no-worse call that
            carries state (``_no_worse``), and what ``fit`` or the composer
            (``composed``) does not take yet.
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
    olds = {
        c.recording.version: c for c in (calls if base_calls is None else base_calls)
    }
    if refinement is Refinement.NO_WORSE:
        for call in calls:
            why = _no_worse(profile, base, call, olds[call.recording.version], device)
            if why is not None:
                return Check(False, refinement, why)
        return Check(True, refinement)
    if len(calls) > 1 and any(c.recording.states for c in calls):
        why = _in_order(profile, base, calls, olds, device)
        return Check(why is None, refinement, why)
    for call in calls:
        why = _bit_identical(profile, base, call, olds[call.recording.version], device)
        if why is not None:
            return Check(False, refinement, why)
    return Check(True, refinement)


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
    untuned build's.

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
            if draw % 2:
                for h in recording.inputs:
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
    calls: Sequence[Timed],
    olds: dict,
    device: Device,
) -> str | None:
    """Run ``calls`` in order built under ``profile`` and under ``base``, each side's states carried into its next call; return the first difference, or None.

    Each version is built once each way, so a repeated call keeps what it
    carries. The calls start from one set of seeded states, shared by name
    across versions, and each takes seeded inputs at its own values; after
    each, every output within its bound, carried buffer and state must be
    bit-identical.
    """
    rng = np.random.default_rng(0)
    seeded: dict[str, np.ndarray] = {}
    for call in calls:
        for _, h in call.recording.states.values():
            seeded.setdefault(h.name, _random_tensor(h, rng))
    sides = [dict(seeded), dict(seeded)]
    built: dict = {}
    try:
        for k, call in enumerate(calls):
            recording = call.recording
            version = recording.version
            if version not in built:
                with set_current_device(device):
                    built[version] = (
                        Applied.of(olds[version], base, device).built(device),
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
                    f"{recording.name}, call {k} of {len(calls)}: "
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
    it goes where ``refinement`` is exact (``compare_graphs``). A call's time is its points' medians,
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
            before = Applied.of(call, base, device).built(device)
            after = Applied.of(call, profile, device).built(device)
            compare_graphs(
                call,
                before,
                after,
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
    then taken best first, each applied to the profile so far (a region and
    a tunable edit of the same steps compose; a region over steps an earlier
    one holds gives way to it, as a tunable an earlier one sets does): one
    that builds what the profile so far builds is passed over; a take is
    checked against ``start`` by its refinement (``check``) and measured
    against the profile so far, and kept where it still gains.
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
        try:
            ratio = measure(
                edited, start, calls, device, timing=PRICING, refinement=edit.refinement
            ).ratio
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
    for ratio, edit in sorted(priced, key=lambda pair: pair[0]):
        edited = edit.apply(incumbent)
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
    return incumbent
