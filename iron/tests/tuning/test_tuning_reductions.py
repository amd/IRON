# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reductions across cores, a cascade chain or a fan-in to a reducer, over the composition contract."""

from __future__ import annotations

import pytest

from iron.common.declare.composition import (
    Entry,
    Member,
    Refinement,
)
from iron.common.declare.profile import Profile
from iron.operators import GEMM, GEMV, RMSNorm, Softmax
from iron.tests.support import toys_composition as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

pytestmark = pytest.mark.usefixtures("npu2")

M = 64
GEMV_K = 256
GEMM_K, GEMM_N = 512, 64


def _gemv_members(splits: int) -> list[Member]:
    return [Member(GEMV, dict(M=M, K=GEMV_K // splits)) for _ in range(splits)]


def _gemm_members(splits: int) -> list[Member]:
    return [
        Member(GEMM, dict(M=32, K=GEMM_K // splits, N=GEMM_N)) for _ in range(splits)
    ]


@unbuilt
@pytest.mark.parametrize("splits", [2, 4, 8])
@pytest.mark.parametrize(
    "members_fn, kind", [(_gemv_members, "gemv"), (_gemm_members, "gemm")]
)
def test_a_cascade_chain_round_trips_as_an_entry(
    members_fn, kind, splits, tmp_path, npu2
):
    members = members_fn(splits)
    region = toys.cascade_region(members, "C", "B")
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    recording = toys.gemv_fan_in_recording(f"{kind}_{splits}", M, GEMV_K, splits)
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_fan_in_to_a_reducer_round_trips_as_an_entry(splits, tmp_path, npu2):
    members = _gemv_members(splits)
    reducer = Member(type("Reducer", (), {}), dict())
    region = toys.fan_in_reducer_region(members, reducer, "C", "a", "b")
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    recording = toys.gemv_fan_in_recording(f"fan_in_{splits}", M, GEMV_K, splits)
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
@pytest.mark.parametrize(
    "cls, dim_name",
    [(Softmax, "cols"), (RMSNorm, "tile_size")],
    ids=["softmax", "rmsnorm"],
)
def test_a_row_sum_reduction_shape_round_trips_as_an_entry(cls, dim_name, tmp_path):
    """Neither operator exposes a partial-sum output to fan a split into, so this names the shape, not a working recording (a reported gap)."""
    splits = 4
    members = [Member(cls, {dim_name: 64 // splits}) for _ in range(splits)]
    reducer = Member(type("Reducer", (), {}), dict())
    region = toys.fan_in_reducer_region(members, reducer, "y", "a", "b")
    profile = Profile()
    profile.add_entry(Entry(root=region))
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_split_gemv_is_no_worse_than_its_own_untuned_build(splits, npu2):
    """Splitting reassociates the sum, so the cascade-composed split is held to no-worse, not bit-identical, against the recording's own untuned build."""
    recording = toys.gemv_fan_in_recording(f"gemv_split_{splits}", M, GEMV_K, splits)
    region = toys.cascade_region(_gemv_members(splits), "C", "B")
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.REASSOCIATION)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_split_gemv_is_bit_identical_across_repeats_and_arrival_order(splits, npu2):
    """The reducer sums in a fixed order, so recordings whose partials complete in another order still match."""
    recording_a = toys.gemv_fan_in_recording(
        f"order_a_{splits}", M, GEMV_K, splits, order=list(range(splits))
    )
    recording_b = toys.gemv_fan_in_recording(
        f"order_b_{splits}", M, GEMV_K, splits, order=list(reversed(range(splits)))
    )
    region = toys.cascade_region(_gemv_members(splits), "C", "B")
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    first = check(profile, base, [Timed(recording_a)], npu2, Refinement.EXACT)
    second = check(profile, base, [Timed(recording_b)], npu2, Refinement.EXACT)
    assert first.ok and second.ok


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_search_keeps_the_split_and_mechanism_that_pay(splits, npu2):
    recording = toys.gemv_fan_in_recording(f"search_{splits}", M, GEMV_K, splits)
    region = toys.cascade_region(_gemv_members(splits), "C", "B")
    entry = Entry(root=region)
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
    result = check(tuned, start, calls, npu2, Refinement.REASSOCIATION)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_cascade_chain_longer_than_the_array_is_refused(npu2):
    """A chain longer than npu2's 8 columns is more cores than the device has, a count checked before any analysis or placement."""
    members = _gemv_members(8) + _gemv_members(8)  # 16 members, past npu2's width
    region = toys.cascade_region(members, "C", "B")
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemv_fan_in_recording("too_long", M, GEMV_K, 8)
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "counts"
