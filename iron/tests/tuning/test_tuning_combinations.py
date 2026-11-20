# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Combinations: an all-pairs cover over the edge axes."""

from __future__ import annotations

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement
from iron.common.graph.sdf import analyze
from iron.common.image.step import HandOff
from iron.tests.support.toys_edges import (
    all_combinations,
    combination_toy,
    depth_from_bounds,
    with_resolved_depth,
)
from iron.tests.support.tuning import reached_by_candidates, unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, search

COMBOS = all_combinations()
AXES = ("shape", "role", "held", "depth", "rate", "size")


def _combo_id(combo: tuple) -> str:
    """Return a readable parametrize id for one combo tuple."""
    shape, role, held, depth, rate, size = combo
    return f"{role}_{shape.value}_{held}_{depth}_{rate}_{size}"


def test_the_cover_covers_every_axis_pair_and_the_known_triple():
    """Every pair of values from two different axes appears in at least one combo, computed from the combos themselves."""
    from iron.tests.support.toys_edges import DEPTHS, HELDS, RATES, ROLES, SHAPES, SIZES

    axes = [SHAPES, ROLES, HELDS, DEPTHS, RATES, SIZES]
    seen = {
        (i, j, combo[i], combo[j])
        for combo in COMBOS
        for i in range(len(axes))
        for j in range(i + 1, len(axes))
    }
    missing = [
        (AXES[i], AXES[j], a, b)
        for i in range(len(axes))
        for j in range(i + 1, len(axes))
        for a in axes[i]
        for b in axes[j]
        if (i, j, a, b) not in seen
    ]
    assert not missing, missing
    assert any(
        role == "skip" and shape == HandOff.SPLIT and held == "l1"
        for shape, role, held, _, _, _ in COMBOS
    )


def test_varying_one_axis_yields_distinct_toys_for_every_role(device):
    """For each role, varying shape, held, rate or size alone yields distinct (recorded operators, Region) pairs.

    ``depth`` is excluded here: a combo's depth is a name (min−1, min, knee,
    more), resolved against ``analyze``'s real ``min_depth``/``knee_depth``
    only inside a test body (never here, since nothing may call the stubbed
    analysis at collection); the device-free distinctness this test checks
    is over the axes a toy's builder encodes directly.
    """
    roles = sorted({role for _, role, _, _, _, _ in COMBOS})
    from iron.tests.support.toys_edges import HELDS, RATES, SHAPES, SIZES

    for role in roles:
        for axis_name, axis_values, fixed in [
            ("shape", SHAPES, dict(held=HELDS[0], rate="same", size="recorded")),
            ("held", HELDS, dict(shape=SHAPES[0], rate="same", size="recorded")),
            ("rate", RATES, dict(shape=SHAPES[0], held=HELDS[0], size="recorded")),
            ("size", SIZES, dict(shape=SHAPES[0], held=HELDS[0], rate="same")),
        ]:
            seen = []
            for value in axis_values:
                kwargs = dict(fixed, **{axis_name: value})
                _, recording, region, _ = combination_toy(
                    device,
                    kwargs["shape"],
                    role,
                    kwargs["held"],
                    "min",
                    kwargs["rate"],
                    kwargs["size"],
                )
                key = (tuple(s.op for s in recording.steps), region)
                assert not any(
                    key == other for other in seen
                ), f"{role}: varying {axis_name} did not change the toy at {value!r}"
                seen.append(key)


@pytest.mark.parametrize("combo", COMBOS, ids=_combo_id)
def test_each_toys_region_matches_its_own_recording(combo, device):
    """Each toy's region matches exactly one run of its own recording's steps, so a test of it tests the steps it names."""
    _, recording, region, _ = combination_toy(device, *combo)
    assert len(recording.occurrences(Entry(region))) == 1


@pytest.mark.parametrize("combo", COMBOS, ids=_combo_id)
def test_each_toy_round_trips_and_is_reached_by_candidate_edits(
    combo, tmp_path, device
):
    """Each toy's region round-trips through the profile, and composing ``candidates``' edits reaches it.

    First the region's own edit, every hand-off an edge of the analysis's
    kind, then one edge's hold at a time, each an edit ``candidates`` yields
    for the profile as it then stands.
    """
    _, recording, region, _ = combination_toy(device, *combo)
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "combination.json")
    loaded = Profile.load(tmp_path / "combination.json")
    assert loaded.entries() == [entry]
    reached = reached_by_candidates(region, [Timed(recording)], device)
    assert reached.entries() == [entry]


@unbuilt
@pytest.mark.parametrize("combo", COMBOS, ids=_combo_id)
@pytest.mark.supported_devices("npu1", "npu2")
def test_each_toy_is_bit_identical_or_refused_below_the_minimum_depth(combo, device):
    """Each toy, at its depth resolved from the analysis, is bit-identical to the steps run apart; below the minimum it is refused.

    The depth is resolved from ``analyze`` inside this test body, never at
    collection or in the toy builder: a hard-coded depth is not the minimum
    for every edge, so only the analysis, run on this toy's own region and
    recording, says what minimum/knee are here.
    """
    shape, role, held, depth, rate, size = combo
    _, recording, region, index = combination_toy(device, *combo)
    analysis = analyze(region, recording, device)
    edge = region.edges[index]
    value = depth_from_bounds(
        depth, analysis.min_depth[edge], analysis.knee_depth[edge]
    )
    resolved = with_resolved_depth(region, index, value)
    profile = Profile()
    profile.add_entry(Entry(resolved))
    verdict = fit(profile, [Timed(recording)], device)
    if depth == "min_minus_one":
        assert not verdict.ok
        assert verdict.stage == "analysis"
        return
    assert verdict.ok, verdict.why
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.parametrize("combo", COMBOS, ids=_combo_id)
@pytest.mark.supported_devices("npu1", "npu2")
def test_each_toy_is_searched_and_the_result_passes_check(combo, device):
    """The tuner, run on each toy alone, keeps a profile that passes ``check`` against the start, exact."""
    _, recording, _, _ = combination_toy(device, *combo)
    # A bounded toy runs at the most its per-call value may be.
    call = Timed(
        recording,
        values={
            v.name: limit.hi - 1 for v, limit in zip(recording.values, recording.limits)
        },
    )
    start = Profile()
    found = search([call], start, device, budget_s=10.0)
    result = check(found, start, [call], device, Refinement.EXACT)
    assert result.ok, result.why
