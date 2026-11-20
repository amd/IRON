# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reductions across cores, a cascade chain or a fan-in to a reducer, over the composition contract."""

from __future__ import annotations

import pytest

from iron.common.declare.composition import Entry, Hold, Refinement
from iron.common.declare.profile import Profile
from iron.tests.support import toys_composition as toys
from iron.tests.support.tuning import reached_by_candidates, unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, measure, search

pytestmark = pytest.mark.usefixtures("npu2")

M = 64
GEMV_K = 256
GEMM_M, GEMM_K, GEMM_N = 32, 512, 64

PARTIALS = [
    pytest.param(lambda n: toys.gemv_k_split_partials(M, GEMV_K, n), id="gemv"),
    pytest.param(
        lambda n: toys.gemm_k_split_partials(GEMM_M, GEMM_K, GEMM_N, n), id="gemm"
    ),
]


@pytest.mark.parametrize("splits", [2, 4, 8])
@pytest.mark.parametrize("partials", PARTIALS)
def test_a_cascade_chain_round_trips_as_an_entry(partials, splits, tmp_path, npu2):
    """The running sum on the cascade, each add on its partial's core, round-trips, and composing ``candidates``' edits reaches it."""
    recording = toys.reduction_recording(f"cascade_{splits}", partials(splits))
    region = toys.cascade_reducer_region(recording)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    reached = reached_by_candidates(region, [Timed(recording)], npu2)
    assert reached.entries() == [entry]


@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_fan_in_to_a_reducer_round_trips_as_an_entry(splits, tmp_path, npu2):
    """The partials fed to their chain of adds round-trip, and composing ``candidates``' edits reaches the region."""
    recording = toys.gemv_fan_in_recording(f"fan_in_{splits}", M, GEMV_K, splits)
    region = toys.fan_in_reducer_region(recording)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    reached = reached_by_candidates(region, [Timed(recording)], npu2)
    assert reached.entries() == [entry]


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_cascade_chain_is_bit_identical_to_its_split_run_apart(splits, npu2):
    """The cascade carries the recorded partials and sums as they are, so the chain is held to the recording's own untuned build bit for bit."""
    recording = toys.gemv_fan_in_recording(f"gemv_split_{splits}", M, GEMV_K, splits)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=toys.cascade_reducer_region(recording)))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_split_gemv_is_bit_identical_across_repeats_and_arrival_order(splits, npu2):
    """The reducer sums in a fixed order, so recordings whose partials complete in another order still match."""
    for order in (list(range(splits)), list(reversed(range(splits)))):
        recording = toys.gemv_fan_in_recording(
            f"order_{order[0]}_{splits}", M, GEMV_K, splits, order=order
        )
        profile, base = Profile(), Profile()
        profile.add_entry(Entry(root=toys.cascade_reducer_region(recording)))
        result = check(profile, base, [Timed(recording)], npu2, Refinement.EXACT)
        assert result.ok, result.why


@pytest.mark.extensive
@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_search_keeps_the_split_and_mechanism_that_pay(splits, npu2):
    recording = toys.gemv_fan_in_recording(f"search_{splits}", M, GEMV_K, splits)
    entry = Entry(root=toys.cascade_reducer_region(recording))
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, npu2).ratio
    tuned = search(calls, start, npu2)
    if ratio < 0.95:
        assert entry in tuned.entries()
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


def test_a_cascade_chain_longer_than_the_array_is_refused(npu2):
    """Sixteen partials chain sixteen cores, more than a path east and south across npu2 passes.

    A count, checked before any analysis or placement.
    """
    recording = toys.gemv_fan_in_recording("too_long", M, 2 * GEMV_K, 16)
    profile = Profile()
    profile.add_entry(Entry(root=toys.cascade_reducer_region(recording)))
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "counts"
    assert "a cascade chain of 16 cores" in (verdict.why or "")


def test_two_cascades_into_one_core_are_refused(npu2):
    """A core has one cascade input, so an add reading both partials off the cascade is refused by the counts."""
    recording = toys.gemv_fan_in_recording("two_in", M, GEMV_K, 2)
    region = toys.fan_in_reducer_region(recording)
    for index in range(len(region.edges)):
        region = region.held(index, Hold.CASCADE)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "counts"
    assert "one cascade input" in (verdict.why or "")
