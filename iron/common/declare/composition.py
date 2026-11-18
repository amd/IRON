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

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Literal

from ..image.step import Edge, EdgeKind

Version = tuple[tuple[str, tuple[int, ...], str], ...]


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
        size: A derived version to run instead, by name.
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
        NotImplementedError: Not built yet: the pinned mlir-aie's ``tunable()``
            takes no ``exact=``.
    """
    raise NotImplementedError("tunable(exact=) is not in the pinned mlir-aie yet")
