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
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

import numpy as np
from aie.dialects._aie_enum_gen import ObjectFifoLinkMode, ObjectFifoPort
from aie.iron.dataflow.objectfifo import ObjectFifo, ObjectFifoLink
from aie.iron.device import Device
from aie.iron.trace import Access, Scope, record
from aie.iron.trace import Recording as Recorded
from aie.utils import set_current_device

from ..declare.composition import Entry, Region
from ..design import BuiltArray, OperatorDesign
from ..image.step import Edge, HandOff
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
    """

    tokens: dict[Edge, tuple[tuple[int, ...], tuple[int, ...]]]
    hand_off: dict[Edge, HandOff]
    dtype: dict[Edge, str]
    initial: dict[Edge, int]
    consistent: bool
    repetition: dict[int, int]
    min_depth: dict[Edge, int]
    why: str | None

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
    call moves: the objects each lane moves, through the links to the fifos
    the cores touch. A region edge joins the producer's output lanes to the
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
            run-time branch or a ``forever_`` in a core, a hand-off whose
            lanes or objects differ (memtile restaging), or a loop no fifo's
            objects settle.
        ValueError: The region matches none of the recording's steps.
    """

    def __init__(self, region: Region, recording: Recording, device: Device) -> None:
        matches = recording.occurrences(Entry(region))
        if not matches:
            raise ValueError("the region matches none of the recording's steps")
        self.region = region
        self.wired, _ = region.wiring()
        self.recorded: list[tuple[Any, Recorded]] = []
        self.roots: list[dict[str, str]] = []
        for s in matches[0]:
            step = recording.steps[s]
            self.roots.append(
                {b.name: ref.root for ref, b in zip(step.refs(), step.op.buffers)}
            )
            with set_current_device(device), record() as recorded:
                array = BuiltArray(OperatorDesign(step.op))
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
                moved = b.moved_per_lane()
                for lane, fifo in enumerate(lanes[b.name]):
                    self.objects[fifo] = -(-moved.get(lane, 0) // obj_elements[b.name])
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

        Raises:
            NotImplementedError: A run-time branch or ``forever_``, or a loop
                no fifo's objects settle.
        """
        loops: list[tuple[Scope, tuple[Scope, ...]]] = []
        stack: list[tuple[Scope, tuple[Scope, ...]]] = [(core, ())]
        while stack:
            scope, outer = stack.pop()
            for node in scope.body:
                if isinstance(node, Scope):
                    if node.kind != "for":
                        raise NotImplementedError(
                            f"a {node.kind} scope in a core (at {node.site}) is "
                            f"not modelled yet"
                        )
                    loops.append((node, outer + (node,)))
                    stack.append((node, outer + (node,)))
        trips: dict[int, int] = {}
        releases: list[tuple[Access, tuple[Scope, ...]]] = []
        stack = [(core, ())]
        while stack:
            scope, outer = stack.pop()
            for node in scope.body:
                if isinstance(node, Scope):
                    stack.append((node, outer + (node,)))
                elif node.kind == "release":
                    releases.append((node, outer))
        for loop, path in sorted(loops, key=lambda lp: len(lp[1])):
            if loop.owner and all(isinstance(b, int) for b in loop.owner):
                trips[id(loop)] = len(range(*loop.owner))
                continue
            for fifo in {a.fifo for a, _ in releases}:
                if fifo not in self.objects:
                    continue
                on = [(a, o) for a, o in releases if a.fifo is fifo]
                if any(
                    id(s) not in trips and s is not loop for _, o in on for s in o
                ) or not any(o and o[-1] is loop for _, o in on):
                    continue
                known = sum(
                    a.count * math.prod(trips[id(s)] for s in o)
                    for a, o in on
                    if loop not in o
                )
                inside = sum(
                    a.count * math.prod(trips[id(s)] for s in o if s is not loop)
                    for a, o in on
                    if loop in o
                )
                left = self.objects[fifo] - known
                if inside and left > 0 and left % inside == 0:
                    trips[id(loop)] = left // inside
                    break
            else:
                raise NotImplementedError(
                    f"no fifo's objects settle the loop at {loop.site}"
                )
        return trips

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
        reader: dict[ObjectFifo, int] = {}
        for actor, program in enumerate(programs):
            for fifo, producer, _, _ in program:
                (writer if producer else reader)[fifo] = actor
        channels: list[Channel] = []
        fixed: dict[int, int] = {}
        of: dict[tuple[ObjectFifo, bool], list[int]] = {}
        edge_channels: dict[Edge, list[int]] = {}
        phases = self.region.phases
        for n, (edge, p, c) in enumerate(self.wired):
            outs = self.lanes[p].get(edge.output, [])
            ins = self.lanes[c].get(edge.input, [])
            sizes = (
                self.obj_elements[p].get(edge.output),
                self.obj_elements[c].get(edge.input),
            )
            if len(outs) != len(ins) or sizes[0] != sizes[1]:
                raise NotImplementedError(
                    f"{edge}: {len(outs)} lanes of {sizes[0]} elements into "
                    f"{len(ins)} of {sizes[1]} needs the memtile restaging the "
                    f"analysis does not model yet"
                )
            carried = self.roots[p][edge.output] in self.carried
            for out, inp in zip(outs, ins):
                channels.append(
                    Channel(
                        writer[out],
                        reader[inp],
                        initial=self.objects[inp] if carried else 0,
                        phase=phases[n] if phases else 0,
                    )
                )
                e = len(channels) - 1
                of.setdefault((out, True), []).append(e)
                of.setdefault((inp, False), []).append(e)
                edge_channels.setdefault(edge, []).append(e)
        for fifo in writer.keys() & reader.keys():
            if (fifo, True) in of or (fifo, False) in of:
                continue
            channels.append(Channel(writer[fifo], reader[fifo]))
            e = len(channels) - 1
            of[(fifo, True)] = [e]
            of[(fifo, False)] = [e]
            if fifo.depth is not None:
                fixed[e] = fifo.depth
        flow = Flow(
            channels,
            [
                [
                    Event(e, producer, acquire, count)
                    for fifo, producer, acquire, count in program
                    for e in of.get((fifo, producer), [])
                ]
                for program in programs
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
            hand_off={edge: HandOff.EQUAL for edge in edge_channels},
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
        )


def analyze(region: Region, recording: Recording, device: Device) -> Analysis:
    """Analyze ``region`` of ``recording`` on ``device``, the device every operator is built for.

    Raises:
        NotImplementedError: What the analysis does not model yet
            (``Derivation``).
        ValueError: The region matches none of the recording's steps.
    """
    return Derivation(region, recording, device).analysis()
