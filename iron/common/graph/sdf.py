# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""The dataflow analysis of a composed region, before any build.

A region's steps fire as actors and its edges carry tokens. What an edge
carries is the operators' and the recording's, not the composition's: the
analysis derives each edge's tokens per firing at both ends (from the
operands' objects and the operators' programs), how the lanes hand off, the
type, and the initial tokens a carried value puts on it. From those it says
whether the rates balance, how often each step fires per iteration, the
smallest depth per edge that cannot deadlock, the depth past which
throughput stops growing, and the time per iteration a cycle bounds. Every
limit comes from the device's target model.
"""

from __future__ import annotations

import math
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any

import numpy as np
from aie.dialects._aie_enum_gen import ObjectFifoLinkMode, ObjectFifoPort
from aie.iron.dataflow.objectfifo import ObjectFifo, ObjectFifoLink
from aie.iron.device import Device
from aie.iron.trace import Access, Scope, record
from aie.iron.trace import Recording as Recorded
from aie.utils import set_current_device

from ..declare import Operator
from ..declare.composition import Entry, Region
from ..design import BuiltArray, OperatorDesign
from ..image.step import BufferRef, Edge, HandOff
from .record import Recording


@dataclass(frozen=True)
class Event:
    """One objectFIFO acquire or release an actor makes, in program order.

    Attributes:
        channel: The edge it names.
        producer: It is made at the edge's writing end.
        acquire: It acquires (False: it releases).
        count: The objects. An acquire holds that many in all, counting
            those still held; a release gives that many up.
    """

    channel: int
    producer: bool
    acquire: bool
    count: int


@dataclass(frozen=True)
class Channel:
    """An edge between two actors.

    Attributes:
        producer: The writing actor.
        consumer: The reading actor.
        initial: Objects on it before the call starts (a carried value).
        phase: The runtime phase its transfer runs in: it is read only once
            every edge of an earlier phase has had all it moves written.
    """

    producer: int
    consumer: int
    initial: int = 0
    phase: int = 0


class Flow:
    """One call of a region as actors replaying their objectFIFO accesses over bounded channels.

    Each actor runs its accesses in program order, as its core does in one
    call, loops unrolled. A reader's acquire waits until the edge holds as
    many objects as it asks to hold; a writer's acquire waits until as many
    slots are free; releases free them or fill them. A core may hold an
    output slot while it waits on an input, as the hardware does. An
    enabled access stays enabled until it runs, since only its own actor
    takes from what it waits on, so whether a call completes does not
    depend on the order actors run in.

    Args:
        channels: The edges.
        programs: Per actor, its accesses in order.
    """

    def __init__(
        self, channels: Sequence[Channel], programs: Sequence[Sequence[Event]]
    ) -> None:
        self.channels = tuple(channels)
        self.programs = tuple(tuple(p) for p in programs)

    def written(self, channel: int) -> int:
        """Return the objects a call writes on ``channel``."""
        producer = self.channels[channel].producer
        return sum(
            e.count
            for e in self.programs[producer]
            if e.channel == channel and e.producer and not e.acquire
        )

    def read(self, channel: int) -> int:
        """Return the objects a call gives up on ``channel`` once read."""
        consumer = self.channels[channel].consumer
        return sum(
            e.count
            for e in self.programs[consumer]
            if e.channel == channel and not e.producer and not e.acquire
        )

    def balance(self) -> str | None:
        """Return why the call leaves an edge with other than its initial objects, or None where every edge balances."""
        for e, channel in enumerate(self.channels):
            if self.written(e) != self.read(e):
                return (
                    f"edge {e} (actor {channel.producer} to {channel.consumer}): "
                    f"{self.written(e)} objects written a call, {self.read(e)} read"
                )
        return None

    def runs(self, depths: Mapping[int, int]) -> str | None:
        """Return why the call deadlocks with each edge ``depths`` deep, or None where it completes."""
        filled = [c.initial for c in self.channels]
        totals = [self.written(e) for e in range(len(self.channels))]
        written = [0] * len(self.channels)
        at = [0] * len(self.programs)
        while True:
            open_phase = min(
                (
                    c.phase
                    for e, c in enumerate(self.channels)
                    if written[e] < totals[e]
                ),
                default=max((c.phase for c in self.channels), default=0),
            )
            ran = False
            for a, program in enumerate(self.programs):
                while at[a] < len(program):
                    event = program[at[a]]
                    e = event.channel
                    if event.producer and event.acquire:
                        if depths[e] - filled[e] < event.count:
                            break
                    elif event.producer:
                        filled[e] += event.count
                        written[e] += event.count
                    elif event.acquire:
                        if (
                            filled[e] < event.count
                            or self.channels[e].phase > open_phase
                        ):
                            break
                    else:
                        filled[e] -= event.count
                    at[a] += 1
                    ran = True
            if all(n == len(p) for n, p in zip(at, self.programs)):
                return None
            if not ran:
                waiting = [
                    f"actor {a} at access {n} of {len(p)}"
                    for a, (n, p) in enumerate(zip(at, self.programs))
                    if n < len(p)
                ]
                return "deadlocks: " + ", ".join(waiting)

    def minimum_depths(
        self, fixed: Mapping[int, int] | None = None
    ) -> tuple[dict[int, int], str | None]:
        """Return each searched edge's smallest deadlock-free depth, and why none exists where one does not.

        Every other searched edge is as deep as a call could fill it. A depth
        below the most an access holds on the edge, or below its initial
        objects, cannot run; past what a call ever has on it, more depth
        cannot matter.

        Args:
            fixed: Edges held at a given depth and not searched (an
                operator's own fifos, at the depths its build chose).
        """
        fixed = dict(fixed or {})
        holds = {
            e: max(
                [c.initial, 1]
                + [
                    ev.count
                    for program in self.programs
                    for ev in program
                    if ev.channel == e and ev.acquire
                ]
            )
            for e, c in enumerate(self.channels)
        }
        ceiling = {
            e: fixed.get(e, c.initial + self.written(e) + holds[e])
            for e, c in enumerate(self.channels)
        }
        why = self.runs(ceiling)
        if why is not None:
            return {}, why
        depths = {}
        for e in range(len(self.channels)):
            if e in fixed:
                continue
            low, high = holds[e], ceiling[e]
            while low < high:
                middle = (low + high) // 2
                if self.runs({**ceiling, e: middle}) is None:
                    high = middle
                else:
                    low = middle + 1
            depths[e] = low
        return depths, None


@dataclass(frozen=True)
class Analysis:
    """What the dataflow analysis finds for one region.

    Attributes:
        tokens: Per edge, the objects each firing moves at the producer and
            at the consumer, one count where every firing moves the same.
        hand_off: Per edge, how the producer's lanes map onto the consumer's.
        dtype: Per edge, the type it carries.
        initial: Per edge, the objects on it before the first firing.
        consistent: Whether every edge balances over a call.
        repetition: Per step, the firings of its first core's outermost loop
            in a call.
        min_depth: The smallest depth per edge that cannot deadlock.
        why: The deadlock or imbalance, where there is one.
        flow: The call's actors and channels.
        channels: Per edge, the channels its depth sizes.
        fixed: The channels an operator's own build holds at a depth.
    """

    tokens: dict[Edge, tuple[tuple[int, ...], tuple[int, ...]]]
    hand_off: dict[Edge, HandOff]
    dtype: dict[Edge, str]
    initial: dict[Edge, int]
    consistent: bool
    repetition: dict[int, int]
    min_depth: dict[Edge, int]
    why: str | None
    flow: Flow = field(repr=False, compare=False)
    channels: dict[Edge, list[int]] = field(repr=False, compare=False)
    fixed: dict[int, int] = field(repr=False, compare=False)

    def deadlock(self, depths: Mapping[Edge, int]) -> str | None:
        """Return why the region deadlocks with ``depths`` on the edges it names and the minimum on every other, or None where it runs.

        Raises:
            ValueError: The region cannot run at any depth (``why``).
        """
        if self.why is not None:
            raise ValueError(f"the region cannot run at any depth: {self.why}")
        held = dict(self.fixed)
        for edge, es in self.channels.items():
            held.update((e, depths.get(edge, self.min_depth[edge])) for e in es)
        return self.flow.minimum_depths(held)[1]

    @property
    def knee_depth(self) -> dict[Edge, int]:
        """The depth per edge past which throughput stops growing.

        Raises:
            NotImplementedError: Not built yet: it needs each actor's time.
        """
        raise NotImplementedError("the knee needs each actor's time, not modelled yet")

    @property
    def period(self) -> Fraction:
        """The time per iteration a cycle bounds, in the device's cycles.

        Raises:
            NotImplementedError: Not built yet: it needs each actor's time.
        """
        raise NotImplementedError(
            "the period needs each actor's time, not modelled yet"
        )


class Derivation:
    """A region's steps, built with their cores recorded, as one call's actors and channels.

    Each step's operator is built on the host with ``aie.iron.trace``
    recording: its cores' acquires and releases in program order, its memtile
    links, and which fifo is which operand lane. A loop's trip count is a
    per-call value the build does not hold, so it is solved from what the
    call moves: the objects the runtime sequence fills or drains on each
    fifo (an operand riding another's fifo, GEMV's B in its A, counted with
    it), carried through the links to the fifos the cores touch. A region edge joins the producer's output lanes to the
    consumer's input lanes as searched channels; a step's own fifos keep the
    depth its build chose; a lane fed from or drained to outside the region
    is unbounded.

    A buffer the recording carries from one call to the next (its feedback,
    or a state the graph holds) arrives whole, so its edge starts the call
    holding every object the call moves on it.

    Args:
        region: The composed region.
        recording: The recording its steps are matched in.
        device: The device every operator is built for.

    Raises:
        NotImplementedError: What the analysis does not model yet: a
            run-time branch or a ``forever_`` in a core, a per-call count, a
            slice, a restaging IRON's ``Staging`` cannot plan, or a loop no
            fifo's objects settle.
        ValueError: The region matches none of the recording's steps, or
            an edge's two ends are not one buffer.
    """

    def __init__(self, region: Region, recording: Recording, device: Device) -> None:
        matches = recording.occurrences(Entry(region))
        if not matches:
            raise ValueError("the region matches none of the recording's steps")
        self.region = region
        self.device = device
        self.wired, _ = region.wiring()
        self.ops: list[Operator] = []
        self.recorded: list[tuple[Any, Recorded]] = []
        self.refs: list[dict[str, BufferRef]] = []
        for s, member in zip(matches[0], region.steps()):
            step = recording.steps[s]
            op = step.op.replace(**(member.tunables or {}))
            if op.bound_extents:
                raise NotImplementedError(
                    f"{type(op).__name__} is bounded per call "
                    f"({', '.join(op.bound_extents)}); analysing a call at "
                    f"its own values is not modelled yet"
                )
            self.ops.append(op)
            self.refs.append({b.name: ref for ref, b in zip(step.refs(), op.buffers)})
            with set_current_device(device), record() as recorded:
                array = BuiltArray(OperatorDesign(op))
                array.program().resolve_program()
            self.recorded.append((array, recorded))
        self.carried = set(recording.feedback) | {
            h.ref().root for _, h in recording.states.values()
        }
        self.objects: dict[ObjectFifo, int] = {}
        self.lanes: list[dict[str, list[ObjectFifo]]] = []
        self.obj_elements: list[dict[str, int]] = []
        for array, recorded in self.recorded:
            lanes: dict[str, list[ObjectFifo]] = {}
            obj_elements: dict[str, int] = {}
            for b in array.op.buffers:
                if not b.streamed or not b.lane_handles:
                    continue
                lanes[b.name] = [h.object_fifo for h in b.lane_handles]
                obj_elements[b.name] = math.prod(b.obj_shape)
            moved: dict[ObjectFifo, int] = {}
            for transfer in recorded.transfers:
                if transfer.elements is None:
                    site = transfer.site
                    raise NotImplementedError(
                        f"{type(array.op).__name__}'s {transfer.kind} of "
                        f"{transfer.fifo.name} is sized per call"
                        + (f" ({site.filename}:{site.line})" if site else "")
                        + "; analysing a call at its own values is not modelled yet"
                    )
                moved[transfer.fifo] = moved.get(transfer.fifo, 0) + -(
                    -transfer.elements // math.prod(transfer.fifo.shape)
                )
            self.objects.update(moved)
            self.lanes.append(lanes)
            self.obj_elements.append(obj_elements)
            self._through_links(recorded.links)

    def _through_links(self, links: Sequence[ObjectFifoLink]) -> None:
        """Carry the objects a call moves across ``links``, from the fifos that know them to those that do not."""
        changed = True
        while changed:
            changed = False
            for link in links:
                srcs = [h.object_fifo for h in link.srcs]
                dsts = [h.object_fifo for h in link.dsts]
                time = link.mode == ObjectFifoLinkMode.Time
                for side, other in ((dsts, srcs), (srcs, dsts)):
                    known = [self.objects[f] for f in other if f in self.objects]
                    if len(known) != len(other):
                        continue
                    if time and len(other) == 1:
                        each = known[0] // len(side)
                    elif time:
                        each = sum(known)
                    else:
                        each = known[0]
                    for f in side:
                        if f not in self.objects:
                            self.objects[f] = each
                            changed = True

    def _trips(self, core: Scope) -> dict[int, int]:
        """Return each loop of ``core``'s trip count, by ``id`` of its scope, solved from the objects its fifos move.

        Each fifo whose objects a call moves is known gives one equation: its
        releases' counts, each times the trips of the loops it sits in, add
        to those objects. A loop with every bound an ``int`` is fixed; the
        rest are solved together, outermost first, each trying the values
        every equation it is in admits, so a loop no fifo is released in
        directly (GEMV's batches around its head tiles and rows) is still
        settled.

        Raises:
            NotImplementedError: A run-time branch or ``forever_``, or loops
                no assignment, or more than one, settles.
        """
        loops: list[Scope] = []
        releases: list[tuple[Access, tuple[Scope, ...]]] = []
        stack: list[tuple[Scope, tuple[Scope, ...]]] = [(core, ())]
        while stack:
            scope, outer = stack.pop()
            for node in reversed(scope.body):
                if isinstance(node, Scope):
                    if node.kind != "for":
                        where = (
                            f"{node.site.filename}:{node.site.line}"
                            if node.site
                            else "a core"
                        )
                        raise NotImplementedError(
                            f"a {node.kind} scope in a core (at {where}) is "
                            f"not modelled yet"
                        )
                    loops.append(node)
                    stack.append((node, outer + (node,)))
                elif node.kind == "release":
                    releases.append((node, outer))
        fixed = {
            id(loop): len(range(*loop.owner))
            for loop in loops
            if loop.owner and all(isinstance(b, int) for b in loop.owner)
        }
        equations: list[tuple[int, list[tuple[int, tuple[int, ...]]]]] = [
            (
                self.objects[fifo],
                [
                    (a.count, tuple(id(s) for s in o))
                    for a, o in releases
                    if a.fifo is fifo
                ],
            )
            for fifo in {a.fifo for a, _ in releases}
            if fifo in self.objects
        ]
        free = [id(loop) for loop in loops if id(loop) not in fixed]
        found: list[dict[int, int]] = []
        assigned = [dict(fixed)]
        while assigned and len(found) < 2:
            trips = assigned.pop()
            settled = [
                sum(c * math.prod(trips[s] for s in path) for c, path in terms)
                == objects
                for objects, terms in equations
                if all(s in trips for _, path in terms for s in path)
            ]
            if not all(settled):
                continue
            unset = [s for s in free if s not in trips]
            if not unset:
                found.append(trips)
                continue
            loop = unset[0]
            values = None
            for objects, terms in equations:
                if {s for _, path in terms for s in path if s not in trips} != {loop}:
                    continue
                known = sum(
                    c * math.prod(trips[s] for s in path)
                    for c, path in terms
                    if loop not in path
                )
                per = sum(
                    c * math.prod(trips[s] for s in path if s != loop)
                    for c, path in terms
                    if loop in path
                )
                left = objects - known
                values = [left // per] if left > 0 and left % per == 0 else []
                break
            if values is None:
                bound = max((objects for objects, _ in equations), default=0)
                values = range(bound, 0, -1)
            assigned += [{**trips, loop: v} for v in values]
        if len(found) != 1:
            where = (
                f"{loops[0].site.filename}:{loops[0].site.line}"
                if loops and loops[0].site
                else "a core"
            )
            raise NotImplementedError(
                f"no fifo's objects settle the loop at {where}"
                if not found
                else f"the objects a call moves settle the loops at {where} more "
                f"than one way"
            )
        return found[0]

    def _events(
        self, body: Sequence[Access | Scope], trips: Mapping[int, int]
    ) -> list[Access]:
        """Return ``body``'s accesses in program order, each loop unrolled ``trips`` times."""
        out: list[Access] = []
        for node in body:
            if isinstance(node, Scope):
                out += self._events(node.body, trips) * trips[id(node)]
            else:
                out.append(node)
        return out

    def _link_events(
        self, link: ObjectFifoLink
    ) -> list[tuple[ObjectFifo, bool, bool, int]]:
        """Return a memtile link's accesses over a call: an object read from its sources and written to its destinations at a time."""
        srcs = [h.object_fifo for h in link.srcs]
        dsts = [h.object_fifo for h in link.dsts]
        time = link.mode == ObjectFifoLinkMode.Time
        unsettled = [f.name for f in srcs + dsts if f not in self.objects]
        if unsettled:
            raise NotImplementedError(
                f"a link of {', '.join(unsettled)}, whose objects a call moves no "
                f"fill, drain or other link settles, is not modelled yet"
            )
        events: list[tuple[ObjectFifo, bool, bool, int]] = []
        if time and len(srcs) == 1:
            for k in range(self.objects[srcs[0]]):
                dst = dsts[k % len(dsts)]
                events += [(srcs[0], False, True, 1), (dst, True, True, 1)]
                events += [(srcs[0], False, False, 1), (dst, True, False, 1)]
        elif time:
            for k in range(self.objects[dsts[0]]):
                src = srcs[k % len(srcs)]
                events += [(src, False, True, 1), (dsts[0], True, True, 1)]
                events += [(src, False, False, 1), (dsts[0], True, False, 1)]
        else:
            for _ in range(max(self.objects[f] for f in srcs + dsts)):
                events += [(f, False, True, 1) for f in srcs]
                events += [(f, True, True, 1) for f in dsts]
                events += [(f, False, False, 1) for f in srcs]
                events += [(f, True, False, 1) for f in dsts]
        return events

    def _channel(
        self,
        built: tuple,
        edge: Edge,
        writing: int,
        reading: int,
        phase: int,
        producer_side: bool,
    ) -> int:
        """Add a channel from actor ``writing`` to ``reading``, and return it.

        A channel on the producer's side is the edge's own depth, objects in
        flight from its producer; a memtile's storage and its channels out
        are part of the restaging, not the edge's depth.
        """
        channels, edge_channels = built[1], built[4]
        channels.append(Channel(writing, reading, phase=phase))
        if producer_side:
            edge_channels.setdefault(edge, []).append(len(channels) - 1)
        return len(channels) - 1

    def _streams(self, operand: Any) -> list[np.ndarray]:
        """Return each of ``operand``'s lanes' elements, in the order the lane moves them."""
        taps = {lane: tap for lane, tap, _, _ in operand.transfers()}
        index = np.arange(operand.elements)
        return [taps[lane].gather(index) for lane in range(operand.lanes)]

    def _restaged(
        self,
        edge: Edge,
        sizes: tuple[int, int],
        streams: tuple[list[np.ndarray], list[np.ndarray]],
        lanes: tuple[list[ObjectFifo], list[ObjectFifo]],
        phase: int,
        built: tuple,
        ends: tuple[dict[ObjectFifo, int], dict[ObjectFifo, list[int]]],
    ) -> HandOff:
        """Model ``edge``'s memtile restaging, and return its hand-off.

        Each element is in one producer lane's object and one consumer lane's
        object. A memtile takes each producer lane's objects once, an ingest
        actor a lane, passing each object on to the consumer lanes whose
        elements it holds; an emit actor a consumer lane, for each object it
        writes, holds the objects passed to it that hold its elements (in
        order, so every one up to the last it needs), writes the object, and
        frees what no later object of its lane needs. A memtile must do that
        much for any restaging; IRON's ``Staging`` plans the whole-lane joins
        and splits among them, and whether IRON builds one is a capability of
        its own. The producer's channels into the memtile are the edge's depth.
        """
        programs, _, writes, reads, _ = built
        writer, readers = ends
        produce, consume = sizes
        produced, consumed = streams
        outs, ins = lanes
        lane_of = np.empty(sum(len(s) for s in produced), dtype=np.int64)
        obj_of = np.empty_like(lane_of)
        for lane, stream in enumerate(produced):
            lane_of[stream] = lane
            obj_of[stream] = np.arange(len(stream)) // produce
        # Per consumer lane, per producer lane, the producer objects it takes, in order.
        taken = [
            {
                lane: np.unique(obj_of[stream][lane_of[stream] == lane])
                for lane in np.unique(lane_of[stream]).tolist()
            }
            for stream in consumed
        ]
        for lane, out in enumerate(outs):
            ingest = len(programs)
            to = [j for j, t in enumerate(taken) if lane in t]
            passed = {j: set(taken[j][lane].tolist()) for j in to}
            events: list[tuple[Any, bool, bool, int]] = []
            for k in range(len(produced[lane]) // produce):
                gets = [j for j in to if k in passed[j]]
                events.append((out, False, True, 1))
                events += [((edge, lane, j), True, True, 1) for j in gets]
                events.append((out, False, False, 1))
                events += [((edge, lane, j), True, False, 1) for j in gets]
            programs.append(events)
            e = self._channel(built, edge, writer[out], ingest, phase, True)
            writes.setdefault(out, []).append(e)
            reads[(out, ingest)] = e
        ingests = {lane: len(programs) - len(outs) + lane for lane in range(len(outs))}
        for j, stream in enumerate(consumed):
            emit = len(programs)
            rank = {
                lane: {int(k): r for r, k in enumerate(objs)}
                for lane, objs in taken[j].items()
            }
            objects = stream.reshape(-1, consume)
            needs = [
                {
                    lane: rank[lane][int(obj_of[o][lane_of[o] == lane].max())]
                    for lane in np.unique(lane_of[o]).tolist()
                }
                for o in objects
            ]
            firsts = [
                {
                    lane: rank[lane][int(obj_of[o][lane_of[o] == lane].min())]
                    for lane in np.unique(lane_of[o]).tolist()
                }
                for o in objects
            ]
            later: list[dict[int, int]] = [{} for _ in needs]
            for k in range(len(needs) - 2, -1, -1):
                later[k] = dict(later[k + 1])
                for lane, first in firsts[k + 1].items():
                    later[k][lane] = min(later[k].get(lane, first), first)
            released = dict.fromkeys(taken[j], 0)
            held_to = dict.fromkeys(taken[j], -1)
            events = []
            for k, need in enumerate(needs):
                for lane, last in need.items():
                    held_to[lane] = max(held_to[lane], last)
                    count = held_to[lane] + 1 - released[lane]
                    events.append(((edge, lane, j), False, True, count))
                events.append(((edge, "emit", j), True, True, 1))
                for lane in need:
                    keep = later[k].get(lane, held_to[lane] + 1)
                    if keep > released[lane]:
                        count = keep - released[lane]
                        events.append(((edge, lane, j), False, False, count))
                        released[lane] = keep
                events.append(((edge, "emit", j), True, False, 1))
            programs.append(events)
            for lane in taken[j]:
                e = self._channel(built, edge, ingests[lane], emit, phase, False)
                writes.setdefault((edge, lane, j), []).append(e)
                reads[((edge, lane, j), emit)] = e
            for reader in readers[ins[j]]:
                e = self._channel(built, edge, emit, reader, phase, False)
                writes.setdefault((edge, "emit", j), []).append(e)
                reads[(ins[j], reader)] = e
        fed = [set(t) for t in taken]
        feeds = [sum(lane in f for f in fed) for lane in range(len(produced))]
        if all(len(f) == 1 for f in fed) and all(n == 1 for n in feeds):
            in_order = len(produced) == len(consumed) and all(
                np.array_equal(a, b) for a, b in zip(produced, consumed)
            )
            return HandOff.EQUAL if in_order else HandOff.LAYOUT
        if all(n == 1 for n in feeds):
            return HandOff.JOIN
        if all(len(f) == 1 for f in fed):
            return HandOff.SPLIT
        return HandOff.RATIO

    def analysis(self) -> Analysis:
        """Return what the call's actors and channels say about the region's edges.

        Raises:
            NotImplementedError: What the analysis does not model yet (see the class).
        """
        programs: list[list[tuple[ObjectFifo, bool, bool, int]]] = []
        repetition: dict[int, int] = {}
        for i, (_, recorded) in enumerate(self.recorded):
            for k, core in enumerate(recorded.cores):
                trips = self._trips(core)
                programs.append(
                    [
                        (
                            a.fifo,
                            a.port == ObjectFifoPort.Produce,
                            a.kind == "acquire",
                            a.count,
                        )
                        for a in self._events(core.body, trips)
                    ]
                )
                if k == 0:
                    outermost = [s for s in core.body if isinstance(s, Scope)]
                    repetition[i] = trips[id(outermost[0])] if outermost else 1
            for link in recorded.links:
                programs.append(self._link_events(link))
        writer: dict[ObjectFifo, int] = {}
        readers: dict[ObjectFifo, list[int]] = {}
        for actor, program in enumerate(programs):
            for fifo, producer, _, _ in program:
                if producer:
                    writer[fifo] = actor
                elif actor not in readers.setdefault(fifo, []):
                    readers[fifo].append(actor)
        channels: list[Channel] = []
        fixed: dict[int, int] = {}
        writes: dict[ObjectFifo, list[int]] = {}
        reads: dict[tuple[ObjectFifo, int], int] = {}
        edge_channels: dict[Edge, list[int]] = {}
        hand_off: dict[Edge, HandOff] = {}
        feeds = Counter((p, edge.output) for edge, p, _ in self.wired)
        phases = self.region.phases
        for n, (edge, p, c) in enumerate(self.wired):
            outs = self.lanes[p].get(edge.output, [])
            ins = self.lanes[c].get(edge.input, [])
            sizes = (
                self.obj_elements[p].get(edge.output),
                self.obj_elements[c].get(edge.input),
            )
            made, read = self.refs[p][edge.output], self.refs[c][edge.input]
            if (read.start, read.nbytes) != (made.start, made.nbytes):
                raise NotImplementedError(
                    f"{edge}: reading part of what its producer makes (slices) "
                    f"is not modelled yet"
                )
            source = next(
                b for b in self.recorded[p][0].op.buffers if b.name == edge.output
            )
            sink = next(
                b for b in self.recorded[c][0].op.buffers if b.name == edge.input
            )
            if source.elements != sink.elements or source.dtype != sink.dtype:
                raise ValueError(
                    f"{edge}: {source.name}'s {source.elements} elements and "
                    f"{sink.name}'s {sink.elements} are not one buffer"
                )
            if (
                sizes[1] is not None
                and all(f in self.objects for f in ins)
                and sum(self.objects[f] for f in ins) != sink.elements // sizes[1]
            ):
                raise NotImplementedError(
                    f"{edge}: {sink.name}'s fifos carry another buffer's objects "
                    f"too (it rides them); an edge into it is not modelled yet"
                )
            produced, consumed = self._streams(source), self._streams(sink)
            if (
                len(outs) != len(ins)
                or sizes[0] != sizes[1]
                or not all(np.array_equal(a, b) for a, b in zip(produced, consumed))
            ):
                hand_off[edge] = self._restaged(
                    edge,
                    (sizes[0], sizes[1]),
                    (produced, consumed),
                    (outs, ins),
                    phases[n] if phases else 0,
                    (programs, channels, writes, reads, edge_channels),
                    (writer, readers),
                )
                continue
            shared = feeds[(p, edge.output)] > 1 or any(
                len(readers.get(inp, [])) > 1 for inp in ins
            )
            hand_off[edge] = HandOff.BROADCAST if shared else HandOff.EQUAL
            carried = made.root in self.carried
            for out, inp in zip(outs, ins):
                for actor in readers[inp]:
                    channels.append(
                        Channel(
                            writer[out],
                            actor,
                            initial=self.objects[inp] if carried else 0,
                            phase=phases[n] if phases else 0,
                        )
                    )
                    e = len(channels) - 1
                    writes.setdefault(out, []).append(e)
                    reads[(inp, actor)] = e
                    edge_channels.setdefault(edge, []).append(e)
        for fifo in writer.keys() & readers.keys():
            if fifo in writes or any((fifo, a) in reads for a in readers[fifo]):
                continue
            for actor in readers[fifo]:
                channels.append(Channel(writer[fifo], actor))
                e = len(channels) - 1
                writes.setdefault(fifo, []).append(e)
                reads[(fifo, actor)] = e
                if fifo.depth is not None:
                    fixed[e] = fifo.depth
        flow = Flow(
            channels,
            [
                [
                    Event(e, producer, acquire, count)
                    for fifo, producer, acquire, count in program
                    for e in (
                        writes.get(fifo, [])
                        if producer
                        else [reads[(fifo, actor)]] if (fifo, actor) in reads else []
                    )
                ]
                for actor, program in enumerate(programs)
            ],
        )
        why = flow.balance()
        depths, deadlock = flow.minimum_depths(fixed)
        tokens = {}
        for edge, es in edge_channels.items():
            written = tuple(
                ev.count
                for ev in flow.programs[flow.channels[es[0]].producer]
                if ev.channel == es[0] and ev.producer and not ev.acquire
            )
            read = tuple(
                ev.count
                for ev in flow.programs[flow.channels[es[0]].consumer]
                if ev.channel == es[0] and not ev.producer and not ev.acquire
            )
            tokens[edge] = (
                written[:1] if len(set(written)) == 1 else written,
                read[:1] if len(set(read)) == 1 else read,
            )
        return Analysis(
            tokens=tokens,
            hand_off=hand_off,
            dtype={
                edge: np.dtype(
                    next(
                        b.dtype
                        for b in self.recorded[p][0].op.buffers
                        if b.name == edge.output
                    )
                ).name
                for edge, p, _ in self.wired
            },
            initial={
                edge: flow.channels[es[0]].initial for edge, es in edge_channels.items()
            },
            consistent=why is None,
            repetition=repetition,
            min_depth={
                edge: max(depths[e] for e in es)
                for edge, es in edge_channels.items()
                if depths
            },
            why=why or deadlock,
            flow=flow,
            channels=edge_channels,
            fixed=fixed,
        )


def analyze(region: Region, recording: Recording, device: Device) -> Analysis:
    """Analyze ``region`` of ``recording`` on ``device``, the device every operator is built for.

    Raises:
        NotImplementedError: What the analysis does not model yet
            (``Derivation``).
        ValueError: The region matches none of the recording's steps.
    """
    return Derivation(region, recording, device).analysis()
