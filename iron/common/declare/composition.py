# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""How a profile names IRON's operations composed onto the array.

One recursive entry, ``Entry``, whose root is a ``Configuration`` (designs
loaded together, run in schedule order) or a ``Region`` (parts run at once,
linked on chip by ``Edge``s). A ``Member`` is one step, named by its
operator class, dims and tunables as a profile entry names it. Beside the
entries, a profile carries per-version ``Schedule``s, per-call
``Variants`` and ``Binding``s, and one ``StateLayout`` per persistent
buffer. A composition names choices only; what the operators and the
recording already fix (an edge's tokens, lanes, type and initial values, a
dependence through memory) the dataflow analysis derives. Placement and
transport are the compiler's: a composition names counts and constraints,
never tiles or channels.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Any, Literal

from ..image.step import Edge, EdgeKind

Version = tuple[tuple[str, tuple[int, ...], str], ...]


class Hold(Enum):
    """Where an edge's value waits between its producer and its consumer.

    ``L1``: in the consumer's core, the two steps on one worker; ``MEMTILE``:
    staged through a memtile; ``DDR``: in host memory, a phase wait;
    ``LATER_PHASE``: staged, its consumer and all it feeds a phase later;
    ``MEMORY``: no edge at all, the value left where its producer writes it,
    a dependence the analysis derives.
    """

    L1 = "l1"
    MEMTILE = "memtile"
    DDR = "ddr"
    LATER_PHASE = "later_phase"
    MEMORY = "memory"


class Switch(Enum):
    """How a call enters a configuration: a full ``RELOAD``, only the ``CHANGED_CORES``, or ``OVERLAPPED`` with compute."""

    RELOAD = "reload"
    CHANGED_CORES = "changed_cores"
    OVERLAPPED = "overlapped"


class Refinement(Enum):
    """How a change relates to the untuned build.

    ``EXACT`` changes are bit-identical; ``NO_WORSE`` changes (a regrouped
    sum, a rounding moved) are admitted only where no input is worse than
    the untuned build's against the operator's reference.
    """

    EXACT = "exact"
    NO_WORSE = "no_worse"


@dataclass(frozen=True)
class Member:
    """One step, named by shape.

    Attributes:
        cls: The operator class.
        dims: The dims the step is constructed with.
        tunables: The tunables it takes here, where they differ from its own.
        runs_on: Where the step runs.
        part: For a step split by fission, ``(dimension, lo, hi)`` of its work.
    """

    cls: type
    dims: dict[str, Any]
    tunables: dict[str, Any] | None = None
    runs_on: Literal["npu", "host"] = "npu"
    part: tuple[str, int, int] | None = None

    def steps(self) -> tuple[Member, ...]:
        """Return this step, the one a tree of steps names it as."""
        return (self,)

    def wiring(
        self, first: int = 0
    ) -> tuple[tuple[tuple[Edge, int, int], ...], tuple[tuple[Inflow, int], ...]]:
        """Return no edges and no inflows: one step wires nothing."""
        return (), ()


@dataclass(frozen=True)
class RuntimePlan:
    """How a region's transfers run.

    Attributes:
        waits: A full barrier between phases, or awaits per channel.
        overlap: None, the next phase prefetched, or a software-pipelined loop.
        chunks: Phases repeated over this many chunks within one call.
        in_flight: Tasks in flight per channel; None for the channel's queue depth.
        chained: One task with chained buffer descriptors rather than many tasks.
        burst: The DDR burst length; None for mlir-aie's default.
        transfer_bytes: Bytes per transfer; None for the operator's own.
    """

    waits: Literal["barrier", "per_channel"] = "barrier"
    overlap: Literal["none", "prefetch", "pipelined"] = "none"
    chunks: int = 1
    in_flight: int | None = None
    chained: bool = False
    burst: int | None = None
    transfer_bytes: int | None = None


@dataclass(frozen=True)
class Inflow:
    """A buffer from outside a region read once and fed on chip to one of its steps.

    Inflows naming one buffer share that one read, fanned out to each consumer.

    Attributes:
        buffer: The recording's buffer.
        consumer: The consuming step.
        input: The consumer's input.
        kind: The path the objects take.
        depth: Objects in flight; None for the dataflow analysis's minimum.
    """

    buffer: str
    consumer: int
    input: str
    kind: EdgeKind = EdgeKind.STREAM
    depth: int | None = None


@dataclass(frozen=True)
class Region:
    """Parts that run at once, linked on chip.

    Indices name the region's steps depth-first through its nested regions.

    Attributes:
        parts: Steps or nested regions.
        edges: Edges between steps; none for parts that share no data and are
            issued at once.
        inflows: Outside buffers read once and fed on chip.
        workers: Steps composed onto one worker, each tuple in firing order.
        phases: A phase per edge; None for one phase.
        runtime: How the region's transfers run; None for one task group.
    """

    parts: tuple[Member | Region, ...]
    edges: tuple[Edge, ...] = ()
    inflows: tuple[Inflow, ...] = ()
    workers: tuple[tuple[int, ...], ...] = ()
    phases: tuple[int, ...] | None = None
    runtime: RuntimePlan | None = None

    def steps(self) -> tuple[Member, ...]:
        """Return its steps depth-first through nested regions, the order its indices name them in."""
        return tuple(m for part in self.parts for m in part.steps())

    def deepened(self, index: int, depth: int | None) -> Region:
        """Return this region with edge ``index`` held ``depth`` objects deep; None, the analysis's minimum."""
        edges = tuple(
            replace(e, depth=depth) if i == index else e
            for i, e in enumerate(self.edges)
        )
        return replace(self, edges=edges)

    def held(self, index: int, place: Hold) -> Region:
        """Return this region with edge ``index`` held at ``place``.

        ``L1`` makes the edge a stream and puts its two steps on one worker,
        with any each already shares one with. ``MEMTILE`` and
        ``LATER_PHASE`` make it staged, ``DDR`` a DDR edge. ``LATER_PHASE``
        runs its consumer, and every step downstream of it, in phase 1: a
        step's phase is the largest of its producers' and 1 where a later
        edge feeds it. ``MEMORY`` drops the edge (and its phase), so the
        edges after it move down one index.
        """
        if place is Hold.MEMORY:
            return replace(
                self,
                edges=self.edges[:index] + self.edges[index + 1 :],
                phases=(
                    None
                    if self.phases is None
                    else self.phases[:index] + self.phases[index + 1 :]
                ),
            )
        kinds = {
            Hold.L1: EdgeKind.STREAM,
            Hold.MEMTILE: EdgeKind.STAGED,
            Hold.DDR: EdgeKind.DDR,
            Hold.LATER_PHASE: EdgeKind.STAGED,
        }
        edge = self.edges[index]
        edges = tuple(
            replace(e, kind=kinds[place]) if i == index else e
            for i, e in enumerate(self.edges)
        )
        workers = self.workers
        if place is Hold.L1 and edge.producer != edge.consumer:
            joined = {edge.producer, edge.consumer}
            apart = []
            for group in self.workers:
                if joined & set(group):
                    joined |= set(group)
                else:
                    apart.append(group)
            workers = tuple(sorted([*apart, tuple(sorted(joined))]))
        phases = self.phases
        if place is Hold.LATER_PHASE:
            step = {e.consumer: p for e, p in zip(self.edges, self.phases or ())}
            # A self-loop's later read is its step's next firing, not a phase.
            if edge.producer != edge.consumer:
                step[edge.consumer] = max(step.get(edge.consumer, 0), 1)
            for e in sorted(self.edges, key=lambda e: e.consumer):
                if e.producer != e.consumer:
                    step[e.consumer] = max(
                        step.get(e.consumer, 0), step.get(e.producer, 0)
                    )
            phases = tuple(step.get(e.consumer, 0) for e in edges)
        return replace(self, edges=edges, workers=workers, phases=phases)

    def wiring(
        self, first: int = 0
    ) -> tuple[tuple[tuple[Edge, int, int], ...], tuple[tuple[Inflow, int], ...]]:
        """Return every edge and inflow under it, each with its steps' indices in the whole tree.

        Args:
            first: The index of its first step in the whole tree.

        Returns:
            Each edge with its producer's and consumer's indices, and each
            inflow with its consumer's.
        """
        edges = tuple((e, first + e.producer, first + e.consumer) for e in self.edges)
        inflows = tuple((i, first + i.consumer) for i in self.inflows)
        at = first
        for part in self.parts:
            part_edges, part_inflows = part.wiring(at)
            edges += part_edges
            inflows += part_inflows
            at += len(part.steps())
        return edges, inflows


@dataclass(frozen=True)
class Configuration:
    """Designs loaded together, their parts run in schedule order.

    Attributes:
        parts: Regions or steps.
        teardown: Tear the configuration down after use; None for the build's default.
        resident: Buffers kept on chip into the next configuration.
        columns: A partial width as a column count; the placer chooses which.
        concurrent: Configurations sharing this id run at once, on disjoint columns.
        switch: How a call enters it; None for a full reload.
    """

    parts: tuple[Region | Member, ...]
    teardown: bool | None = None
    resident: tuple[str, ...] = ()
    columns: int | None = None
    concurrent: int | None = None
    switch: Switch | None = None

    def steps(self) -> tuple[Member, ...]:
        """Return its steps depth-first through its parts."""
        return tuple(m for part in self.parts for m in part.steps())

    def wiring(
        self, first: int = 0
    ) -> tuple[tuple[tuple[Edge, int, int], ...], tuple[tuple[Inflow, int], ...]]:
        """Return every edge and inflow in its regions, each with its steps' indices in the whole tree.

        Args:
            first: The index of its first step in the whole tree.

        Returns:
            Each edge with its producer's and consumer's indices, and each
            inflow with its consumer's.
        """
        edges: tuple[tuple[Edge, int, int], ...] = ()
        inflows: tuple[tuple[Inflow, int], ...] = ()
        at = first
        for part in self.parts:
            part_edges, part_inflows = part.wiring(at)
            edges += part_edges
            inflows += part_inflows
            at += len(part.steps())
        return edges, inflows


@dataclass(frozen=True)
class Scope:
    """Where an entry applies.

    Attributes:
        versions: The versions' input shapes it is limited to; None for all.
        occurrences: The runs of its shape it is limited to; None for all.
        device_part: The device part it is limited to; None for every part.
    """

    versions: frozenset[Version] | None = None
    occurrences: tuple[int, ...] | None = None
    device_part: str | None = None


@dataclass(frozen=True)
class Entry:
    """A profile's composition entry: a tree of configurations, regions and steps, or one step."""

    root: Configuration | Region | Member
    scope: Scope = field(default_factory=Scope)


@dataclass(frozen=True)
class Schedule:
    """How a version's parts and calls are ordered.

    Attributes:
        version: The version it schedules.
        order: A partial order between top-level parts beyond their dependences.
        recompute: Steps run again inside a later part.
        calls_per_command: Calls dispatched in one command.
        calls_overlapped: Calls in flight inside one command.
        commands_in_flight: Commands submitted before the previous completes.
        interleave_with: Versions mixed into the same command.
        size: A derived version to run instead, by name: ``"merged_<k>x"``,
            ``k`` calls merged into one.
        packaging: One full ELF, or an xclbin per step; None for the device's default.
    """

    version: Version
    order: tuple[tuple[int, int], ...] = ()
    recompute: tuple[int, ...] = ()
    calls_per_command: int = 1
    calls_overlapped: int = 0
    commands_in_flight: int = 1
    interleave_with: tuple[Version, ...] = ()
    size: str | None = None
    packaging: Literal["full_elf", "xclbin"] | None = None


@dataclass(frozen=True)
class Variants:
    """A design per range of one or more per-call values.

    Attributes:
        values: The per-call values the ranges are over.
        ranges: Each range, one ``(lo, hi)`` per value, with its entry.
        selected: Chosen by the host per command, or inside the runtime sequence.
    """

    values: tuple[str, ...]
    ranges: tuple[tuple[tuple[tuple[int, int], ...], Entry], ...]
    selected: Literal["host", "sequence"] = "host"


@dataclass(frozen=True)
class Binding:
    """How a per-call value reaches a design: baked in, read per call, or specialized per range."""

    value: str
    how: Literal["compile", "runtime", "per_range"]


@dataclass(frozen=True)
class StateLayout:
    """One layout for a persistent buffer, in every version that writes or reads it.

    Attributes:
        buffer: The persistent buffer.
        order: Its dimensions' order in memory.
        tile: The tile its elements are grouped in, if any.
    """

    buffer: str
    order: tuple[str, ...]
    tile: tuple[int, ...] | None = None


def refinement(cls: type, tunable: str) -> Refinement:
    """Return how moving ``cls``'s ``tunable`` off its value relates to the untuned build.

    ``EXACT`` unless the tunable is declared ``tunable(exact=False)``.

    Raises:
        ValueError: ``tunable`` is not one of ``cls``'s tunables.
    """
    declaration = cls.declaration
    if tunable not in declaration.tunables:
        raise ValueError(f"{cls.__name__} has no tunable {tunable!r}")
    return (
        Refinement.EXACT if declaration.params[tunable].exact else Refinement.NO_WORSE
    )
