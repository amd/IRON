# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""The dataflow analysis of a composed region, before any build.

A region's parts fire as actors and its edges carry tokens at their rates. The
analysis says whether the rates balance, how often each part fires per
iteration, the smallest depth per edge that cannot deadlock, the depth past
which throughput stops growing, and the time per iteration a cycle bounds.
Every limit comes from the device's target model.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from aie.iron.device import Device

from ..declare.composition import Region
from ..image.step import Edge
from .record import Recording


@dataclass(frozen=True)
class Analysis:
    """What the dataflow analysis finds for one region.

    Attributes:
        consistent: Whether the edges' rates balance.
        repetition: Firings per part per iteration.
        min_depth: The smallest depth per edge that cannot deadlock.
        knee_depth: The depth per edge past which throughput stops growing.
        period: The time per iteration a cycle bounds, in the device's cycles.
        why: The deadlock or imbalance, where there is one.
    """

    consistent: bool
    repetition: dict[int, int]
    min_depth: dict[Edge, int]
    knee_depth: dict[Edge, int]
    period: Fraction
    why: str | None


def analyze(region: Region, recording: Recording, device: Device) -> Analysis:
    """Analyze ``region`` of ``recording`` on ``device``.

    Raises:
        NotImplementedError: Not built yet (plan step 1).
    """
    raise NotImplementedError("the dataflow analysis (plan step 1)")
