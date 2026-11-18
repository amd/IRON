# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Skip connections and reconvergent paths (diamonds).

Every check calls the composition contract before any compile, build or
device use, so nothing here touches the NPU; ``candidates``, ``fit``,
``check`` and ``search`` all raise ``NotImplementedError`` (not built yet),
so every test is ``@unbuilt``.
"""

from __future__ import annotations

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    HELDS,
    diamond_qkv_merge,
    realize_helds,
    skip_add_gemv_add,
    skip_add_gemv_add_edge,
    skip_edge,
    window_with_outside_reader,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

DEVICE = DEVICES["npu2"]()


def _residual_region(held: str | None = None):
    """Return the two-transformer-layer-ish residual (add, norm, proj, add2), its skip edge held one way."""
    recording, members, forward = window_with_outside_reader()
    edges = forward + (skip_edge(depth=4),)
    if held is None:
        return recording, Region(members, edges)
    edges, workers, phases = realize_helds(edges, {len(edges) - 1: held})
    return recording, Region(members, edges, workers=workers, phases=phases)


def _short_skip_region(held: str | None = None, depth: int = 4):
    recording, members, forward = skip_add_gemv_add()
    edges = forward + (skip_add_gemv_add_edge(depth=depth),)
    if held is None:
        return recording, Region(members, edges)
    edges, workers, phases = realize_helds(edges, {len(edges) - 1: held})
    return recording, Region(members, edges, workers=workers, phases=phases)


@unbuilt
@pytest.mark.parametrize("held", HELDS)
def test_a_residual_skip_round_trips_for_every_way_of_holding_it(held, tmp_path):
    """A region with a skip edge, its depth and held place realized, round-trips; ``candidates`` proposes each feasible holding."""
    recording, region = _residual_region(held=held)
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / f"skip_{held}.json")
    loaded = Profile.load(tmp_path / f"skip_{held}.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
def test_a_reconvergent_diamond_round_trips():
    """Attention's Q/K/V branches rejoining (a diamond) round-trips, and ``candidates`` proposes the fan-out and the merge."""
    recording, region = diamond_qkv_merge()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
@pytest.mark.parametrize("held", HELDS)
@pytest.mark.supported_devices("npu2")
def test_a_residual_skip_is_bit_identical_for_every_way_of_holding_it(held):
    """The residual window, held each way, is bit-identical to the same steps run apart."""
    recording, region = _residual_region(held=held)
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_reconvergent_diamond_is_bit_identical():
    """The Q/K/V diamond is bit-identical to the norm, the two projections and the merge run apart."""
    recording, region = diamond_qkv_merge()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_tuner_picks_the_way_of_holding_that_pays():
    """The tuner, on the residual toy alone, picks the held place that pays."""
    recording, _ = _residual_region()
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(
        isinstance(e.root, Region)
        and (
            e.root.workers or any(edge.kind.value != "stream" for edge in e.root.edges)
        )
        for e in found.entries()
    )


@unbuilt
def test_a_depth_below_the_analyzed_minimum_is_refused_before_any_build():
    """A skip edge shallower than the dataflow analysis's minimum is refused before any build.

    Add -> GEMV -> Add held on a 2-deep broadcast edge hangs the device; a
    skip held 4 deep runs where a 2-deep hold deadlocks.
    """
    recording, region = _short_skip_region(depth=1)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "depth" in (result.why or "") or "deadlock" in (result.why or "")


@unbuilt
def test_the_recorded_safe_depth_fits():
    """The same skip edge at a depth of 4, which runs safely, is not refused by the analysis."""
    recording, region = _short_skip_region(depth=4)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert result.ok, result.why
