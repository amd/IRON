# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""The tuner as one search over compositions.

``candidates`` yields every edit IRON's graph admits, of every kind;
``fit`` refuses an edit that cannot fit before any build (counts from the
target model, then the dataflow analysis, then the placer); ``check`` holds
a built edit to the untuned build (bit identity, or no input worse against
the operators' references); ``search`` starts from the shipped profile,
prices each edit in place against the incumbent, and keeps the set that
gains most.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from typing import Literal, Protocol

from aie.iron.device import Device

from ..common.declare import Profile
from ..common.declare.composition import Refinement
from ..common.graph.record import Recording


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


PLACEMENTS: Sequence[str] = ("sequential", "sa:0", "sa:1", "sa:2")


def candidates(
    recording: Recording, profile: Profile, device: Device
) -> Iterator[Edit]:
    """Yield every edit of ``profile`` that ``recording`` admits on ``device``.

    Raises:
        NotImplementedError: Not built yet (plan step 1).
    """
    raise NotImplementedError("the candidate generator (plan step 1)")


def fit(
    profile: Profile,
    recording: Recording,
    device: Device,
    placements: Sequence[str] = PLACEMENTS,
) -> Fit:
    """Decide whether ``profile``'s compositions fit ``device``, before any build.

    Raises:
        NotImplementedError: Not built yet (plan step 1).
    """
    raise NotImplementedError("the static fit (plan step 1)")


def check(
    profile: Profile,
    base: Profile,
    recording: Recording,
    device: Device,
    refinement: Refinement,
) -> Check:
    """Hold ``recording`` built under ``profile`` to it built under ``base``, on ``device``.

    Raises:
        NotImplementedError: Not built yet (plan step 1).
    """
    raise NotImplementedError("the correctness check (plan step 1)")


def search(
    recording: Recording, start: Profile, device: Device, budget_s: float | None = None
) -> Profile:
    """Return the fastest profile found from ``start`` that passes every check.

    Raises:
        NotImplementedError: Not built yet (plan step 1).
    """
    raise NotImplementedError("the search (plan step 1)")
