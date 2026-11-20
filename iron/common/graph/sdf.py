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

import functools
import itertools
import math
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, get_origin

import numpy as np
from aie.dialects._aie_enum_gen import ObjectFifoLinkMode, ObjectFifoPort
from aie.iron import Program, Worker
from aie.iron.dataflow.objectfifo import ObjectFifo, ObjectFifoLink
from aie.iron.device import Device
from aie.iron.kernel import ExternalFunction
from aie.iron.kernels import Param
from aie.iron.trace import Access, Scope, record
from aie.iron.trace import Recording as Recorded
from aie.utils import set_current_device

from ..declare import Operator
from ..declare.composition import Entry, Region
from ..design import BuiltArray, OperatorDesign, configuration
from ..elementwise import Elementwise
from ..image.compose import Spliced, cascade_cores, splice
from ..image.step import BufferRef, Edge, EdgeKind, HandOff
from .clock import kernel_cycles
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
        floor: Objects it holds whatever its depth: its producer's own end
            buffers, for a core-to-core fifo. Where the two ends share
            memory the lowering makes one pool as deep as the deeper end;
            apart, each end its own pool, more again. A period counts it; a
            deadlock does not, so a depth that runs runs on either.
    """

    producer: int
    consumer: int
    initial: int = 0
    phase: int = 0
    floor: int = 0


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

    def _holds(self) -> dict[int, int]:
        return {
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

    def ceiling(self, fixed: Mapping[int, int] | None = None) -> dict[int, int]:
        """Return each edge's depth past which more cannot matter: all a call writes on it, and what it starts with and holds; ``fixed`` edges at theirs."""
        fixed = dict(fixed or {})
        holds = self._holds()
        return {
            e: fixed.get(e, c.initial + self.written(e) + holds[e])
            for e, c in enumerate(self.channels)
        }

    def period(
        self,
        depths: Mapping[int, int],
        costs: Sequence[Sequence[Fraction]],
        calls: int = 4,
    ) -> Fraction | None:
        """Return the time a call takes in steady state, ``calls`` calls run back to back, or None where they deadlock.

        Each actor spends ``costs[a][i]`` before its access ``i`` (its work
        before what it releases), and an access waits, besides on its actor,
        until what it takes is there: an acquire, until the edge last
        changed. A call's end is its last actor's; the period is the time
        between the last two calls' ends. An edge holds at least its
        ``floor``.

        Raises:
            NotImplementedError: An edge runs in a later phase: a phase
                starts empty, and its host transfers, which the analysis
                does not time, bound it where its kernels are light.
        """
        if any(c.phase for c in self.channels):
            raise NotImplementedError(
                "a period over phases is not modelled yet: a phase starts empty "
                "and its host transfers, which the analysis does not time, bound it"
            )
        depths = {e: max(depths[e], c.floor) for e, c in enumerate(self.channels)}
        filled = [c.initial for c in self.channels]
        changed = [Fraction(0)] * len(self.channels)
        clock = [Fraction(0)] * len(self.programs)
        at = [0] * len(self.programs)
        ends = [Fraction(0)] * calls
        lengths = [len(p) for p in self.programs]
        while True:
            best: tuple[Fraction, int] | None = None
            for a, program in enumerate(self.programs):
                if at[a] == lengths[a] * calls:
                    continue
                i = at[a] % lengths[a]
                event = program[i]
                e = event.channel
                cost = costs[a][i]
                if event.acquire:
                    free = (
                        depths[e] - filled[e] if event.producer else filled[e]
                    ) >= event.count
                    if not free:
                        continue
                    when = max(clock[a], changed[e]) + cost
                else:
                    when = clock[a] + cost
                if best is None or when < best[0]:
                    best = (when, a)
            if best is None:
                if all(n == length * calls for n, length in zip(at, lengths)):
                    return ends[-1] - ends[-2] if calls > 1 else ends[-1]
                return None
            when, a = best
            event = self.programs[a][at[a] % lengths[a]]
            e = event.channel
            if not event.acquire:
                filled[e] += event.count if event.producer else -event.count
                changed[e] = when
            clock[a] = when
            at[a] += 1
            if at[a] % lengths[a] == 0:
                k = at[a] // lengths[a] - 1
                ends[k] = max(ends[k], when)

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
        holds = self._holds()
        ceiling = self.ceiling(fixed)
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

    A DDR edge's consumer reads in host memory what its producer wrote there,
    a phase later: its channel runs from the shim, which fills the consumer's
    end from host memory as fast as it frees, not from the producer, and
    ``hand_off`` names only the on-chip edges.

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
        kernels: Per actor, the kernels its core calls; none for a memtile
            link, which takes no time of a core's.
        scalars: Per actor, each of its kernels' scalar arguments its
            contract leaves unbound, as its operator passes them.
        work: Per actor, the accesses its work comes before: each output
            it releases (once, not again for each reader a broadcast writes
            to), or, where it writes none, each input it frees; for steps on
            one core, each step's.
        fired: Per actor, for each access of its work, the kernels (indices
            into its ``kernels``) one of whose calls comes before it: the
            one its member calls, for steps on one core in their firing
            order; several where one core's body calls several, in an order
            its accesses do not record; none for no kernel.
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
    kernels: list[tuple[ExternalFunction, ...]] = field(repr=False, compare=False)
    scalars: list[tuple[tuple, ...]] = field(repr=False, compare=False)
    work: list[list[int]] = field(repr=False, compare=False)
    fired: list[list[tuple[int, ...]]] = field(repr=False, compare=False)

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

    @functools.cached_property
    def costs(self) -> list[list[Fraction]]:
        """Per actor, the cycles it spends before each access: one call of its kernel, traced alone on its own NPU, before each access of its work.

        Steps on one core cost each its own kernel's call, in their firing
        order.

        Raises:
            NotImplementedError: One core's body calls several kernels, in an
                order its accesses do not record, a kernel takes scalars its
                core computes at run time (its operator passes none), or a
                kernel is built for an NPU other than the one attached
                (``kernel_cycles``).
        """
        costs = []
        for kernels, scalars, work, fired, program in zip(
            self.kernels,
            self.scalars,
            self.work,
            self.fired,
            self.flow.programs,
            strict=True,
        ):
            row = [Fraction(0)] * len(program)
            for i, ks in zip(work, fired, strict=True):
                if len(ks) > 1:
                    raise NotImplementedError(
                        f"pricing a core whose body calls {len(ks)} kernels "
                        f"({', '.join(kernels[k].name for k in ks)}), in an order "
                        f"its accesses do not record, is not modelled yet"
                    )
                for k in ks:
                    contract = kernels[k].contract
                    types = kernels[k].arg_types()
                    bound = dict(contract.parameter_bindings)
                    free = sum(
                        r is Param and get_origin(types[n]) is not np.ndarray
                        for n, r in enumerate(contract.roles)
                        if n not in bound
                    )
                    if free and not scalars[k]:
                        raise NotImplementedError(
                            f"pricing {kernels[k].name}, whose {free} scalar(s) its "
                            f"core computes at run time, is not modelled yet"
                        )
                    row[i] = Fraction(kernel_cycles(kernels[k], scalars[k]))
            costs.append(row)
        return costs

    @functools.cached_property
    def period(self) -> Fraction:
        """The cycles a call takes in steady state with every edge as deep as more cannot matter: the bound its slowest actor or cycle sets.

        Raises:
            ValueError: The region cannot run at any depth (``why``).
            NotImplementedError: An edge runs in a later phase, or a core
                calls several kernels (``costs``).
        """
        if self.why is not None:
            raise ValueError(f"the region cannot run at any depth: {self.why}")
        period = self.flow.period(self.flow.ceiling(self.fixed), self.costs)
        assert period is not None, "the ceiling depths run"
        return period

    @functools.cached_property
    def knee_depth(self) -> dict[Edge, int]:
        """Per edge, the shallowest depth from its minimum at which a call takes ``period``, every other edge as deep as more cannot matter.

        A core-to-core edge holds what its producer's own end buffers too
        (``Channel.floor``), which the device runs ahead into, so a depth
        below that end's buffers gains nothing over them (``add -> SiLU ->
        mul`` at 2**18 elements: depth 2 against 1 measures 0.99 to 1.01,
        where the reading end alone says 0.81). The floor is the pool the
        two ends share, the least either placement gives, so the knee holds
        whichever the placer picks.

        Raises:
            ValueError: The region cannot run at any depth (``why``).
            NotImplementedError: As ``period``.
        """
        target = self.period
        ceiling = self.flow.ceiling(self.fixed)
        knees = {}
        for edge, es in self.channels.items():
            depth = self.min_depth[edge]
            top = max(ceiling[e] for e in es)
            while (
                depth < top
                and self.flow.period(
                    {**ceiling, **dict.fromkeys(es, depth)}, self.costs
                )
                != target
            ):
                depth += 1
            knees[edge] = depth
        return knees


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

    Steps the composer joins core to core are built as it builds them
    (``compose.splice``, ``compose.cascade_cores``) and resolved as one
    program. A step spliced into its producer's cores runs on each core
    after the producer's body, the two one actor, the core's own tile its
    edge; a cascade into or out of such cores is a channel a core pair, its
    relays the transport, not actors.

    One call is analysed, at its per-call values: a lane whose length a
    per-call word sizes moves that word's tiles at the call's extents
    (``Operand.transfers``), the one array serving every extent. A value the
    call does not give is the largest the recording's limits admit, a whole
    call.

    Args:
        region: The composed region.
        recording: The recording its steps are matched in.
        device: The device every operator is built for.
        values: The call's per-call values, by name (``Timed.values``).

    Raises:
        NotImplementedError: What the analysis does not model yet: a
            run-time branch or a ``forever_`` in a core, a transfer sized
            per call other than by a lane's length word, a slice, a
            restaging IRON's ``Staging`` cannot plan, or a loop no fifo's
            objects settle.
        ValueError: The region matches none of the recording's steps, a
            member's tunables do not resolve (``Unresolvable``), an edge's
            two ends are not one buffer, or a per-call value the call does
            not give is bounded by no limit of the recording.
    """

    def __init__(
        self,
        region: Region,
        recording: Recording,
        device: Device,
        values: Mapping[str, int] | None = None,
    ) -> None:
        matches = recording.occurrences(Entry(region))
        if not matches:
            raise ValueError("the region matches none of the recording's steps")
        self.region = region
        self.device = device
        self.values = dict(values or {})
        self.wired, _ = region.wiring()
        groups = [set(group) for group in region.workers]
        # A carry across calls is no splice within the call: its initial
        # objects model it.
        one_core = [
            (e, p, c)
            for e, p, c in self.wired
            if e.kind is EdgeKind.STREAM
            and not e.across_calls
            and any({p, c} <= g for g in groups)
        ]
        # Built as the composer builds them: an output leaving on the cascade,
        # or streaming to a step on its worker, is built to splice.
        splices: dict[int, list[str]] = {}
        for e, p, c in self.wired:
            if (e.kind is EdgeKind.CASCADE and not e.across_calls) or (
                e,
                p,
                c,
            ) in one_core:
                splices.setdefault(p, []).append(e.output)
        self.ops: list[Operator] = []
        self.recorded: list[tuple[Any, Recorded]] = []
        self.refs: list[dict[str, BufferRef]] = []
        self.spliced: dict[Edge, list[tuple[Worker, Worker, ObjectFifo]]] = {}
        self.per_core: dict[tuple[int, str], list[ObjectFifo]] = {}
        spliced_into: dict[int, tuple[int, Spliced]] = {}
        # Per step, the graph expression each of its per-call values is bound
        # to, and its extents at this call.
        bindings: list[tuple[dict[str, Any], dict[str, int]]] = []
        for i, (s, member) in enumerate(zip(matches[0], region.steps())):
            step = recording.steps[s]
            op = step.op
            bound = {
                b.member.name: b.expression for b in recording.bindings if b.op is op
            }
            if member.tunables:
                with set_current_device(device):
                    op = op._with_tunables(**member.tunables).resolved(device)
            bindings.append(
                (
                    bound,
                    {
                        name: self._evaluate(recording, bound[name])
                        for name in op.bound_extents
                    },
                )
            )
            self.ops.append(op)
            self.refs.append({b.name: ref for ref, b in zip(step.refs(), op.buffers)})
            into = [
                (e, p)
                for e, p, c in one_core
                if c == i
                and next(
                    b for b in self.recorded[p][0].op.buffers if b.name == e.output
                ).join
                is not None
            ]
            with set_current_device(device), record() as recorded:
                if not into:
                    array: BuiltArray = BuiltArray(
                        OperatorDesign(op), splices=splices.get(i, ())
                    )
                else:
                    (edge, p), *more = into
                    if more or any(i in g and g != {p, i} for g in groups):
                        raise NotImplementedError(
                            f"one core for steps {sorted(g for g in groups if i in g)} "
                            f"is not built yet: a step spliced into its producer's "
                            f"cores shares them with no other"
                        )
                    producer = self.recorded[p][0]
                    cascaded = any(
                        e.kind is EdgeKind.CASCADE and q == i for e, q, _ in self.wired
                    )
                    made = splice(
                        edge,
                        OperatorDesign(op),
                        producer,
                        [e for e, _, c in self.wired if c == i],
                        cascaded,
                    )
                    array = made.array
                    spliced_into[i] = (p, made)
                    (source,) = [
                        b for b in producer.op.buffers if b.name == edge.output
                    ]
                    self.spliced[edge] = [
                        (writer, stage.workers[0], core)
                        for (writer, stage), core in zip(
                            made.cores,
                            [f for fifos in source.core_fifos for f in fifos],
                            strict=True,
                        )
                    ]
                    for name, fifos in made.arriving.items():
                        self.per_core[(i, name)] = fifos
                    if cascaded:
                        self.per_core[(i, array.op.outputs[0].name)] = [
                            stage.op.outputs[0].lane_fifos[0] for _, stage in made.cores
                        ]
            for b in array.op.buffers:
                if b.splices and b.join is not None:
                    self.per_core[(i, b.name)] = [f for fs in b.core_fifos for f in fs]
            self.recorded.append((array, recorded))
        # The composer joins these steps' cores core to core, so each group
        # resolves as one program: a spliced step with its producer, and a
        # cascade's ends where either is per core, its relays between them. A
        # relay moves what the cascade edge's channel carries: it is no actor.
        relayed = [
            (e, p, c)
            for e, p, c in self.wired
            if e.kind is EdgeKind.CASCADE
            and ((p, e.output) in self.per_core or (c, e.input) in self.per_core)
        ]
        part = {i: frozenset([i]) for i in range(len(self.recorded))}
        for p, c in [(p, c) for c, (p, _) in spliced_into.items()] + [
            (p, c) for _, p, c in relayed
        ]:
            merged = part[p] | part[c]
            for j in merged:
                part[j] = merged
        for group in sorted(set(part.values()), key=min):
            steps = sorted(group)
            arrays = {j: self.recorded[j][0] for j in steps}
            owner = {id(w): j for j in steps for w in arrays[j].workers}
            for c, (p, made) in spliced_into.items():
                if c in group:
                    staged = [stage.workers[0] for _, stage in made.cores]
                    arrays[p].workers += staged
                    owner |= {id(w): c for w in staged}
            with set_current_device(device), record() as resolved:
                for e, p, c in relayed:
                    if p not in group:
                        continue
                    (sink,) = [b for b in arrays[c].op.buffers if b.name == e.input]
                    pairs = cascade_cores(
                        e,
                        arrays[p],
                        spliced_into[p][1] if p in spliced_into else None,
                        spliced_into[c][1] if c in spliced_into else None,
                        sink,
                        {},
                        {},
                    )
                    arrays[steps[0]].workers += [w for pair in pairs for w in pair]
                if len(steps) == 1:
                    arrays[steps[0]].program().resolve_program()
                else:
                    configured = configuration(
                        "analysed",
                        {str(j): arrays[j] for j in steps},
                        steps=[str(j) for j in steps],
                        fuse=True,
                    )
                    Program.compose(
                        [configured], entry=configured.runtimes[0]
                    ).resolve_program()
            # A spliced step's host operands move along its producer's lanes:
            # their transfers are its own.
            fifo_step = {
                h.object_fifo: j
                for j in steps
                for b in arrays[j].op.buffers
                if b.streamed
                for h in b.lane_handles
            }
            for core in resolved.cores:
                if id(core.owner) in owner:
                    self.recorded[owner[id(core.owner)]][1].cores.append(core)
            for transfer in resolved.transfers:
                step = fifo_step.get(transfer.fifo, steps[0])
                self.recorded[step][1].transfers.append(transfer)
            self.recorded[steps[0]][1].links.extend(resolved.links)
        self.carried = set(recording.feedback) | {
            h.ref().root for _, h in recording.states.values()
        }
        self.objects: dict[ObjectFifo, int] = {}
        self.lanes: list[dict[str, list[ObjectFifo]]] = []
        self.obj_elements: list[dict[str, int]] = []
        for op, (array, recorded), (bound, extents) in zip(
            self.ops, self.recorded, bindings, strict=True
        ):
            lanes: dict[str, list[ObjectFifo]] = {}
            obj_elements: dict[str, int] = {}
            # Per fifo, the elements each transfer its lane's per-call length
            # sizes moves this call, in order.
            sized: dict[ObjectFifo, list[int]] = {}
            per_call = any(t.elements is None for t in recorded.transfers)
            for b in array.op.buffers:
                if not b.streamed or not b.lane_handles:
                    continue
                lanes[b.name] = [h.object_fifo for h in b.lane_handles]
                obj_elements[b.name] = math.prod(b.obj_shape)
                for lane, _, length, unit in b.transfers() if per_call else ():
                    if length is None:
                        continue
                    tiles = (
                        self._evaluate(recording, bound[length.name])
                        if length.name in bound
                        else op.derived_at(length.name, **extents)
                    )
                    sized.setdefault(lanes[b.name][lane], []).append(tiles * unit)
            moved: dict[ObjectFifo, int] = {}
            for transfer in recorded.transfers:
                fifo = transfer.fifo
                elements = transfer.elements
                if elements is None and sized.get(fifo):
                    elements = sized[fifo].pop(0)
                if elements is None:
                    site = transfer.site
                    raise NotImplementedError(
                        f"{type(array.op).__name__}'s {transfer.kind} of "
                        f"{fifo.name} is sized per call"
                        + (f" ({site.filename}:{site.line})" if site else "")
                        + " other than by a lane's length; analysing it is not "
                        "modelled yet"
                    )
                moved[fifo] = moved.get(fifo, 0) + -(-elements // math.prod(fifo.shape))
            self.objects.update(moved)
            self.lanes.append(lanes)
            self.obj_elements.append(obj_elements)
            self._through_links(recorded.links)
        # A joined output's core fifos each move what the lane they join into
        # would drain (``Operand.moved_per_lane``), whatever reads them instead.
        for array, _ in self.recorded:
            for b in array.op.buffers:
                if b.splices and b.join is not None:
                    each = b.moved_per_lane()
                    for lane, fifos in enumerate(b.core_fifos):
                        for f in fifos:
                            self.objects.setdefault(
                                f, -(-each.get(lane, 0) // math.prod(b.obj_shape))
                            )
        self.links = [link for _, recorded in self.recorded for link in recorded.links]
        self._through_links(self.links)

    def _evaluate(self, recording: Recording, expression: Any) -> int:
        """Return graph ``expression`` at this call: its value as the call gives it, else the largest every limit of the recording on it admits.

        Raises:
            ValueError: The call does not give the value and no limit of the
                recording bounds it, or the limits do not settle one.
        """
        name = expression.value.name
        if name not in self.values:
            on = [
                limit
                for limit in recording.limits
                if limit.plus is None
                and limit.expression.value.name == name
                and limit.expression.linear
                and limit.expression.scale > 0
            ]
            if not on:
                raise ValueError(
                    f"{recording.name}: the call does not give {name}, and no limit "
                    f"of the recording bounds it"
                )
            most = min(
                (limit.hi - 1 - limit.expression.bias) // limit.expression.scale
                for limit in on
            )
            if not all(
                limit.lo <= limit.evaluate({name: most}) < limit.hi for limit in on
            ):
                raise ValueError(
                    f"{recording.name}: the limits on {name} settle no largest value"
                )
            self.values[name] = most
        return expression.evaluate(self.values)

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

    def _all_trips(self) -> dict[int, dict[int, int]]:
        """Return every core's loop trip counts (``_trips``), by ``id`` of its scope.

        A core whose fifos no fill, drain or link settles waits on others: once
        a core's loops settle, the objects it releases on a fifo no transfer
        knows are what a call moves on it, so a core whose loops read it (a
        spliced stage reading its producer's tile) settles in turn.

        Raises:
            NotImplementedError: A core no other's objects settle (``_trips``).
        """
        cores = [core for _, recorded in self.recorded for core in recorded.cores]
        solved: dict[int, dict[int, int]] = {}
        while True:
            waiting: NotImplementedError | None = None
            settled = False
            for core in cores:
                if id(core) in solved:
                    continue
                try:
                    trips = self._trips(core)
                except NotImplementedError as e:
                    waiting = waiting or e
                    continue
                solved[id(core)] = trips
                settled = True
                released: dict[tuple[ObjectFifo, bool], int] = {}
                for a in self._events(core.body, trips):
                    if a.kind == "release":
                        key = (a.fifo, a.port == ObjectFifoPort.Produce)
                        released[key] = released.get(key, 0) + a.count
                for (fifo, produced), objects in released.items():
                    if fifo not in self.objects and (
                        produced or (fifo, True) not in released
                    ):
                        self.objects[fifo] = objects
            if waiting is None:
                return solved
            if not settled:
                raise waiting
            self._through_links(self.links)

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
        much for any restaging; IRON's ``Staging`` plans the joins, splits and
        joins split again among them, and whether IRON builds one is a
        capability of its own. The producer's channels into the memtile are the edge's depth.
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
        actor_kernels: list[tuple[ExternalFunction, ...]] = []
        actor_scalars: list[tuple[tuple, ...]] = []
        # Per actor, for each access, the kernels one of which comes before it,
        # and the actor whose core makes it, before steps on one core join.
        fires: list[list[tuple[int, ...]]] = []
        made_by: list[list[int]] = []
        repetition: dict[int, int] = {}
        # Per actor, the step whose core it is; None for a link.
        actor_step: list[int | None] = []
        solved = self._all_trips()
        actor_of: dict[int, int] = {}
        for i, (array, recorded) in enumerate(self.recorded):
            given = array.op.scalars() if isinstance(array.op, Elementwise) else ()
            for k, core in enumerate(recorded.cores):
                trips = solved[id(core)]
                actor_of[id(core.owner)] = len(programs)
                actor_step.append(i)
                actor_kernels.append(
                    tuple(
                        f for f in core.owner.fn_args if isinstance(f, ExternalFunction)
                    )
                )
                actor_scalars.append((given,) * len(actor_kernels[-1]))
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
                fires.append([tuple(range(len(actor_kernels[-1])))] * len(programs[-1]))
                made_by.append([len(programs) - 1] * len(programs[-1]))
                if k == 0:
                    outermost = [s for s in core.body if isinstance(s, Scope)]
                    repetition[i] = trips[id(outermost[0])] if outermost else 1
            for link in recorded.links:
                actor_kernels.append(())
                actor_scalars.append(())
                actor_step.append(None)
                programs.append(self._link_events(link))
                fires.append([()] * len(programs[-1]))
                made_by.append([len(programs) - 1] * len(programs[-1]))
        writer: dict[ObjectFifo, int] = {}
        readers: dict[ObjectFifo, list[int]] = {}
        for actor, program in enumerate(programs):
            for fifo, producer, _, _ in program:
                if producer:
                    writer[fifo] = actor
                elif actor not in readers.setdefault(fifo, []):
                    readers[fifo].append(actor)
        # Steps on one worker: each lane's producer core and its reader are one
        # actor, running their programs in the worker's firing order.
        lead: dict[int, int] = {}
        # A step spliced into its producer's cores: each core and its stage.
        for cores in self.spliced.values():
            for writing, stage, _ in cores:
                lead[actor_of[id(stage)]] = actor_of[id(writing)]
        for group in self.region.workers:
            for edge, p, c in self.wired:
                # A carry across calls joins no actors within the call.
                if (
                    p not in group
                    or c not in group
                    or edge in self.spliced
                    or edge.across_calls
                ):
                    continue
                outs = self.lanes[p].get(edge.output, [])
                ins = self.lanes[c].get(edge.input, [])
                if (
                    len(outs) != len(ins)
                    or any(len(readers.get(f, [])) != 1 for f in ins)
                    or any(actor_step[writer[f]] is None for f in outs)
                    or any(actor_step[readers[f][0]] is None for f in ins)
                ):
                    raise NotImplementedError(
                        f"{edge}: steps on one core whose lanes do not pair one "
                        f"core to one core are not modelled yet"
                    )
                for out, inp in zip(outs, ins):
                    first = writer[out]
                    while first in lead:
                        first = lead[first]
                    lead[readers[inp][0]] = first
        joined: dict[int, list[int]] = {}
        for actor in sorted(lead):
            first = actor
            while first in lead:
                first = lead[first]
            joined.setdefault(first, [first]).append(actor)
        firing = {s: k for group in self.region.workers for k, s in enumerate(group)}
        for first, members in joined.items():
            ordered = sorted(members, key=lambda a: firing[actor_step[a]])
            programs[first] = [event for a in ordered for event in programs[a]]
            offsets = list(
                itertools.accumulate(
                    (len(actor_kernels[a]) for a in ordered), initial=0
                )
            )
            fires[first] = [
                tuple(k + at for k in ks)
                for a, at in zip(ordered, offsets)
                for ks in fires[a]
            ]
            made_by[first] = [m for a in ordered for m in made_by[a]]
            actor_kernels[first] = tuple(f for a in ordered for f in actor_kernels[a])
            actor_scalars[first] = tuple(s for a in ordered for s in actor_scalars[a])
            for a in members:
                if a != first:
                    programs[a] = []
                    fires[a] = []
                    made_by[a] = []
                    actor_kernels[a] = ()
                    actor_scalars[a] = ()
        if lead:
            writer, readers = {}, {}
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
        uncarried = [
            f"{edge} carries {self.refs[p][edge.output].root} into the next call "
            f"through host memory, but the recording carries no such buffer: the "
            f"first call has no initial value to read"
            for edge, p, _ in self.wired
            if edge.kind is EdgeKind.DDR
            and edge.across_calls
            and self.refs[p][edge.output].root not in self.carried
        ]
        for n, (edge, p, c) in enumerate(self.wired):
            phase = phases[n] if phases else 0
            # Spliced, a core's tile stays on the core: its stage reads it.
            # A cascade into or out of such cores runs core to core.
            if edge in self.spliced or (
                edge.kind is EdgeKind.CASCADE
                and (
                    (p, edge.output) in self.per_core
                    or (c, edge.input) in self.per_core
                )
            ):
                if edge in self.spliced:
                    pairs = [(core, core) for _, _, core in self.spliced[edge]]
                else:
                    sends = self.per_core.get((p, edge.output))
                    arrives = self.per_core.get((c, edge.input))
                    if sends is None or arrives is None or len(sends) != len(arrives):
                        raise NotImplementedError(
                            f"{edge}: a cascade between a step's lanes and another's "
                            f"cores, or between cores that do not pair one to one, is "
                            f"not built yet"
                        )
                    pairs = list(zip(sends, arrives))
                    for sent, arriving in pairs:
                        if sent.obj_type != arriving.obj_type:
                            raise NotImplementedError(
                                f"{edge}: a cascade from a core's {sent.obj_type} into "
                                f"a core's {arriving.obj_type} is not built yet"
                            )
                for sent, arriving in pairs:
                    for actor in readers.get(arriving, []):
                        channels.append(Channel(writer[sent], actor, phase=phase))
                        e = len(channels) - 1
                        writes.setdefault(sent, []).append(e)
                        reads[(arriving, actor)] = e
                        edge_channels.setdefault(edge, []).append(e)
                hand_off[edge] = HandOff.EQUAL
                continue
            if (p, edge.output) in self.per_core:
                raise NotImplementedError(
                    f"{edge}: an output its build joins from its cores' own fifos, "
                    f"read on its lanes, is not built yet"
                )
            if edge.kind is EdgeKind.DDR:
                for inp in self.lanes[c].get(edge.input, []):
                    if inp not in self.objects or not readers.get(inp):
                        raise NotImplementedError(
                            f"{edge}: a DDR edge into {inp.name}, whose objects a "
                            f"call moves or whose reader the build does not settle, "
                            f"is not modelled yet"
                        )
                    source = len(programs)
                    programs.append(
                        [
                            (inp, True, acquire, 1)
                            for _ in range(self.objects[inp])
                            for acquire in (True, False)
                        ]
                    )
                    writer[inp] = source
                    for actor in readers[inp]:
                        channels.append(Channel(source, actor, phase=phase))
                        e = len(channels) - 1
                        writes.setdefault(inp, []).append(e)
                        reads[(inp, actor)] = e
                        edge_channels.setdefault(edge, []).append(e)
                continue
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
                    f"{edge}: {source.name}'s {source.elements} elements of "
                    f"{np.dtype(source.dtype).name} and {sink.name}'s "
                    f"{sink.elements} of {np.dtype(sink.dtype).name} are not one "
                    f"buffer"
                )
            unstreamed = [b.name for b in (source, sink) if not b.streamed]
            if unstreamed:
                raise NotImplementedError(
                    f"{edge}: {unstreamed[0]} streams on no fifo of its own (it "
                    f"rides another's or is held whole); an edge with it is not "
                    f"modelled yet"
                )
            # More objects than its own buffer holds; a call bounded short of
            # it moves fewer.
            if (
                sizes[1] is not None
                and all(f in self.objects for f in ins)
                and sum(self.objects[f] for f in ins) > sink.elements // sizes[1]
            ):
                raise NotImplementedError(
                    f"{edge}: {sink.name}'s fifos carry another buffer's objects "
                    f"too (it rides them); an edge into it is not modelled yet"
                )
            if any(not readers.get(f) for f in ins):
                raise NotImplementedError(
                    f"{edge}: no core of {type(self.ops[c]).__name__} reads "
                    f"{sink.name}'s lanes; an edge into it is not modelled yet"
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
                    phase,
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
                            phase=phase,
                            floor=out.prod().depth,
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
        actor_kernels += [()] * (len(programs) - len(actor_kernels))
        actor_scalars += [()] * (len(programs) - len(actor_scalars))
        fires += [[()] * len(p) for p in programs[len(fires) :]]
        made_by += [[a] * len(programs[a]) for a in range(len(made_by), len(programs))]
        events: list[list[Event]] = []
        work: list[list[int]] = []
        fired: list[list[tuple[int, ...]]] = []
        for actor, program in enumerate(programs):
            expanded: list[Event] = []
            # By the core that makes them, the outputs it releases and the
            # inputs it frees.
            outputs: dict[int, list[int]] = {}
            inputs: dict[int, list[int]] = {}
            follows: list[tuple[int, ...]] = []
            for (fifo, producer, acquire, count), ks, maker in zip(
                program, fires[actor], made_by[actor], strict=True
            ):
                ends = (
                    writes.get(fifo, [])
                    if producer
                    else [reads[(fifo, actor)]] if (fifo, actor) in reads else []
                )
                if ends and not acquire:
                    (outputs if producer else inputs).setdefault(maker, []).append(
                        len(expanded)
                    )
                expanded += [Event(e, producer, acquire, count) for e in ends]
                follows += [ks] * len(ends)
            events.append(expanded)
            work.append(
                sorted(
                    i
                    for maker in dict.fromkeys(made_by[actor])
                    for i in outputs.get(maker) or inputs.get(maker, [])
                )
            )
            fired.append([follows[i] for i in work[-1]])
        flow = Flow(channels, events)
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
            why=why or deadlock or next(iter(uncarried), None),
            flow=flow,
            channels=edge_channels,
            fixed=fixed,
            kernels=actor_kernels,
            scalars=actor_scalars,
            work=work,
            fired=fired,
        )


def analyze(
    region: Region,
    recording: Recording,
    device: Device,
    values: Mapping[str, int] | None = None,
) -> Analysis:
    """Analyze ``region`` of ``recording`` on ``device``, the device every operator is built for, for one call at ``values``.

    Args:
        region: The composed region.
        recording: The recording its steps are matched in.
        device: The device.
        values: The call's per-call values, by name; one it leaves out is
            the largest the recording's limits admit (``Derivation``).

    Raises:
        NotImplementedError: What the analysis does not model yet
            (``Derivation``).
        ValueError: The region matches none of the recording's steps, or a
            per-call value the call leaves out is bounded nowhere.
    """
    return Derivation(region, recording, device, values).analysis()
