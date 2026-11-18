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

from dataclasses import dataclass
from fractions import Fraction

from aie.iron.device import Device

from ..declare.composition import Region
from ..image.step import Edge, HandOff
from .record import Recording


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
