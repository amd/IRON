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
from dataclasses import dataclass, field
from fractions import Fraction

from aie.iron.device import Device

from ..declare.composition import Region
from ..image.step import Edge, HandOff
from .record import Recording


@dataclass(frozen=True)
class Firing:
    """One firing of an actor: the objects it holds on each edge it reads, and what it gives up and writes.

    Attributes:
        holds: Per edge read, the objects held while it fires (an objectFIFO
            acquire, counting those still held from the last firing).
        releases: Per edge read, the objects given up when it ends.
        writes: Per edge written, the objects it fills.
    """

    holds: dict[int, int] = field(default_factory=dict)
    releases: dict[int, int] = field(default_factory=dict)
    writes: dict[int, int] = field(default_factory=dict)


@dataclass(frozen=True)
class Channel:
    """An edge between two actors.

    Attributes:
        producer: The writing actor.
        consumer: The reading actor.
        initial: Tokens on it before the first firing (a carried value).
        phase: The runtime phase its transfer runs in: it is read only once
            every edge of an earlier phase has had all it moves written.
    """

    producer: int
    consumer: int
    initial: int = 0
    phase: int = 0


class Flow:
    """One call of a region as actors firing over bounded channels.

    Each actor fires a finite sequence, as its core program does in one call
    (a ramp-up, its steady firing repeated, a drain), so a sliding window or
    a first firing unlike the rest is exact rather than averaged. A firing
    is atomic: it may start when every edge it reads holds what it needs and
    every edge it writes has room, counting what it gives up on an edge it
    also writes (a carried value).

    Args:
        channels: The edges.
        firings: Per actor, its firings in order.
    """

    def __init__(
        self, channels: Sequence[Channel], firings: Sequence[Sequence[Firing]]
    ) -> None:
        self.channels = tuple(channels)
        self.firings = tuple(tuple(f) for f in firings)

    def repetition(self) -> dict[int, int]:
        """Return each actor's firings in the call."""
        return {a: len(f) for a, f in enumerate(self.firings)}

    def balance(self) -> str | None:
        """Return why the call leaves an edge with other than its initial tokens, or None where every edge balances."""
        for e, channel in enumerate(self.channels):
            written = sum(f.writes.get(e, 0) for f in self.firings[channel.producer])
            released = sum(f.releases.get(e, 0) for f in self.firings[channel.consumer])
            if written != released:
                return (
                    f"edge {e} (actor {channel.producer} to {channel.consumer}): "
                    f"{written} objects written a call, {released} read"
                )
        return None

    def runs(self, depths: Mapping[int, int]) -> str | None:
        """Return why the call deadlocks with each edge ``depths`` deep, or None where it completes.

        Firing order does not change whether a call completes: an enabled
        firing stays enabled until it fires.
        """
        filled = [c.initial for c in self.channels]
        next_firing = [0] * len(self.firings)
        totals = [
            sum(f.writes.get(e, 0) for f in self.firings[c.producer])
            for e, c in enumerate(self.channels)
        ]
        written = [0] * len(self.channels)
        while True:
            open_phase = min(
                (
                    c.phase
                    for e, c in enumerate(self.channels)
                    if written[e] < totals[e]
                ),
                default=max((c.phase for c in self.channels), default=0),
            )
            fired = False
            for a, firings in enumerate(self.firings):
                k = next_firing[a]
                if k == len(firings):
                    continue
                firing = firings[k]
                after = list(filled)
                for e, held in firing.holds.items():
                    if filled[e] < held or self.channels[e].phase > open_phase:
                        break
                else:
                    for e, released in firing.releases.items():
                        after[e] -= released
                    if all(
                        after[e] + count <= depths[e]
                        for e, count in firing.writes.items()
                    ):
                        for e, count in firing.writes.items():
                            after[e] += count
                            written[e] += count
                        filled = after
                        next_firing[a] += 1
                        fired = True
            if all(n == len(f) for n, f in zip(next_firing, self.firings)):
                return None
            if not fired:
                waiting = [
                    f"actor {a} at firing {n} of {len(f)}"
                    for a, (n, f) in enumerate(zip(next_firing, self.firings))
                    if n < len(f)
                ]
                return "deadlocks: " + ", ".join(waiting)

    def minimum_depths(self) -> tuple[dict[int, int], str | None]:
        """Return each edge's smallest deadlock-free depth, every other edge as deep as a call could fill it, and why none exists where one does not.

        A depth below the most a firing holds or writes on the edge, or below
        its initial tokens, cannot run; past what a call ever has on it,
        more depth cannot matter.
        """
        ceiling = {
            e: c.initial
            + sum(f.writes.get(e, 0) for f in self.firings[c.producer])
            + max((f.holds.get(e, 0) for f in self.firings[c.consumer]), default=0)
            for e, c in enumerate(self.channels)
        }
        why = self.runs(ceiling)
        if why is not None:
            return {}, why
        depths = {}
        for e, c in enumerate(self.channels):
            low = max(
                [c.initial, 1]
                + [f.holds.get(e, 0) for f in self.firings[c.consumer]]
                + [f.writes.get(e, 0) for f in self.firings[c.producer]]
            )
            high = ceiling[e]
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
