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

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction

from aie.iron.device import Device

from ..declare.composition import Region
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

    def minimum_depths(self) -> tuple[dict[int, int], str | None]:
        """Return each edge's smallest deadlock-free depth, every other edge as deep as a call could fill it, and why none exists where one does not.

        A depth below the most an access holds on the edge, or below its
        initial objects, cannot run; past what a call ever has on it, more
        depth cannot matter.
        """
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
            e: c.initial + self.written(e) + holds[e]
            for e, c in enumerate(self.channels)
        }
        why = self.runs(ceiling)
        if why is not None:
            return {}, why
        depths = {}
        for e in range(len(self.channels)):
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
        tokens: Per edge, the tokens each firing moves at the producer and at
            the consumer, one count per firing of a repeating cycle.
        hand_off: Per edge, how the producer's lanes map onto the consumer's.
        dtype: Per edge, the type it carries.
        initial: Per edge, the tokens on it before the first firing.
        consistent: Whether the edges' rates balance.
        repetition: Firings per step per iteration.
        min_depth: The smallest depth per edge that cannot deadlock.
        knee_depth: The depth per edge past which throughput stops growing.
        period: The time per iteration a cycle bounds, in the device's cycles.
        why: The deadlock or imbalance, where there is one.
    """

    tokens: dict[Edge, tuple[tuple[int, ...], tuple[int, ...]]]
    hand_off: dict[Edge, HandOff]
    dtype: dict[Edge, str]
    initial: dict[Edge, int]
    consistent: bool
    repetition: dict[int, int]
    min_depth: dict[Edge, int]
    knee_depth: dict[Edge, int]
    period: Fraction
    why: str | None


def analyze(region: Region, recording: Recording, device: Device) -> Analysis:
    """Analyze ``region`` of ``recording`` on ``device``.

    Raises:
        NotImplementedError: Not built yet.
    """
    raise NotImplementedError("the dataflow analysis is not built yet")
