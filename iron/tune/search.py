# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""The tuner as one search over compositions.

Each takes a graph's calls (``Timed``, every version) rather than one
recording. ``candidates`` yields every edit the calls admit, of every kind;
``fit`` refuses an edit
that cannot fit before any build (counts from the target model, then the
dataflow analysis, then the placer); ``check`` holds a built edit to the
untuned build (bit identity, or no input worse against the operators'
references); ``measure`` times a profile against another in pairs;
``search`` starts from the shipped profile, prices each edit in place
against the incumbent, and keeps the set that gains most.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from typing import Literal, Protocol

from aie.iron.device import Device

from ..common.declare import Profile
from ..common.declare.composition import Refinement
from .autotune import Timed


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


@dataclass(frozen=True)
class Measured:
    """A profile's time against a base's, from paired runs.

    Attributes:
        ratio: The median of the paired ratios, profile over base.
        seconds: The profile's median seconds a run of the calls.
        base_seconds: The base's median seconds a run of the calls.
    """

    ratio: float
    seconds: float
    base_seconds: float


PLACEMENTS: Sequence[str] = ("sequential", "sa:0", "sa:1", "sa:2")


def candidates(
    calls: Sequence[Timed], profile: Profile, device: Device
) -> Iterator[Edit]:
    """Yield every edit of ``profile`` that ``calls`` admit on ``device``.

    Raises:
        NotImplementedError: Not built yet.
    """
    raise NotImplementedError("the candidate generator is not built yet")


def fit(
    profile: Profile,
    calls: Sequence[Timed],
    device: Device,
    placements: Sequence[str] = PLACEMENTS,
    max_images: int | None = None,
) -> Fit:
    """Decide whether ``profile``'s compositions fit ``device``, before any build.

    Args:
        profile: The profile whose compositions are fitted.
        calls: The graph's calls, every version.
        device: The device.
        placements: The placer's settings a fit may try.
        max_images: The images the host may hold loaded at once; None for no limit.

    Raises:
        NotImplementedError: Not built yet.
    """
    raise NotImplementedError("the static fit is not built yet")


def check(
    profile: Profile,
    base: Profile,
    calls: Sequence[Timed],
    device: Device,
    refinement: Refinement,
    base_calls: Sequence[Timed] | None = None,
) -> Check:
    """Hold ``calls`` built under ``profile`` to ``base_calls`` built under ``base``, run in order on the same inputs.

    Args:
        profile: The profile checked.
        base: The profile it is held to.
        calls: The graph's calls, run in order, state carried between them.
        device: The device.
        refinement: The rule it is held to.
        base_calls: The calls ``base`` runs, where they are not ``calls``
            (an operator a graph replaces).

    Raises:
        NotImplementedError: Not built yet.
    """
    raise NotImplementedError("the correctness check is not built yet")


def measure(
    profile: Profile, base: Profile, calls: Sequence[Timed], device: Device
) -> Measured:
    """Time ``calls`` built under ``profile`` against them built under ``base``, in pairs.

    Raises:
        NotImplementedError: Not built yet.
    """
    raise NotImplementedError("the paired measurement is not built yet")


def search(
    calls: Sequence[Timed],
    start: Profile,
    device: Device,
    budget_s: float | None = None,
    max_images: int | None = None,
) -> Profile:
    """Return the fastest profile found from ``start`` that passes every check.

    Raises:
        NotImplementedError: Not built yet.
    """
    raise NotImplementedError("the search is not built yet")
