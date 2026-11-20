# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reductions across cores, a cascade chain or a fan-in to a reducer, over the composition contract."""

from __future__ import annotations

import pytest
from aie.dialects.aie import get_target_model

from iron.common.declare.composition import Entry, Hold, Refinement
from iron.common.declare.profile import Profile
from iron.common.graph.sdf import analyze
from iron.common.image.step import HandOff
from iron.tests.support import toys_composition as toys
from iron.tests.support.tools import DEVICES
from iron.tests.support.tuning import reached_by_candidates
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, measure, search

pytestmark = pytest.mark.usefixtures("device")

M = 64
GEMV_K = 256
GEMM_M, GEMM_K, GEMM_N = 32, 512, 64


def _chain_splits(name: str) -> list[int]:
    """Return the splits, powers of two from 2, whose cascade chain the device's array holds: a path east and south."""
    model = get_target_model(DEVICES[name]().resolve())
    rows = sum(model.is_core_tile(0, row) for row in range(model.rows()))
    reach = model.columns() + rows - 1
    return [2**k for k in range(1, reach.bit_length()) if 2**k <= reach]


# Each device's GEMM cascade reducers, by the splits its array chains.
GEMM_CHAINS = [
    pytest.param(name, splits, id=f"device_{name}-splits_{splits}")
    for name in sorted(DEVICES)
    for splits in _chain_splits(name)
]

PARTIALS = [
    pytest.param(lambda n: toys.gemv_k_split_partials(M, GEMV_K, n), id="gemv"),
    pytest.param(
        lambda n: toys.gemm_k_split_partials(GEMM_M, GEMM_K, GEMM_N, n), id="gemm"
    ),
]


@pytest.mark.parametrize("splits", [2, 4, 8])
@pytest.mark.parametrize("partials", PARTIALS)
def test_a_cascade_chain_round_trips_as_an_entry(partials, splits, tmp_path, device):
    """The running sum on the cascade, each add on its partial's core, round-trips, and composing ``candidates``' edits reaches it."""
    recording = toys.reduction_recording(f"cascade_{splits}", partials(splits))
    region = toys.cascade_reducer_region(recording)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    reached = reached_by_candidates(region, [Timed(recording)], device)
    assert reached.entries() == [entry]


@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_fan_in_to_a_reducer_round_trips_as_an_entry(splits, tmp_path, device):
    """The partials fed to their chain of adds round-trip, and composing ``candidates``' edits reaches the region."""
    recording = toys.gemv_fan_in_recording(f"fan_in_{splits}", M, GEMV_K, splits)
    region = toys.fan_in_reducer_region(recording)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    reached = reached_by_candidates(region, [Timed(recording)], device)
    assert reached.entries() == [entry]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_cascade_chain_is_bit_identical_to_its_split_run_apart(splits, device):
    """The cascade carries the recorded partials and sums as they are, so the chain is held to the recording's own untuned build bit for bit."""
    recording = toys.gemv_fan_in_recording(f"gemv_split_{splits}", M, GEMV_K, splits)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=toys.cascade_reducer_region(recording)))
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_a_split_gemv_is_bit_identical_across_repeats_and_arrival_order(splits, device):
    """The reducer sums in a fixed order, so recordings whose partials complete in another order still match."""
    for order in (list(range(splits)), list(reversed(range(splits)))):
        recording = toys.gemv_fan_in_recording(
            f"order_{order[0]}_{splits}", M, GEMV_K, splits, order=order
        )
        profile, base = Profile(), Profile()
        profile.add_entry(Entry(root=toys.cascade_reducer_region(recording)))
        result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_a_partial_on_the_cascade_and_streamed_elsewhere_is_bit_identical(device):
    """A partial the cascade carries to the add and a stream to a SiLU: the relay is one more reader of its lane."""
    recording, region = toys.partial_read_twice("read_twice", M, GEMV_K)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("splits", [2, 4, 8])
def test_search_keeps_the_split_and_mechanism_that_pay(splits, device):
    recording = toys.gemv_fan_in_recording(f"search_{splits}", M, GEMV_K, splits)
    entry = Entry(root=toys.cascade_reducer_region(recording))
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, device).ratio
    tuned = search(calls, start, device)
    # Where the chain pays, what search keeps is at least as fast (it may sum
    # the partials otherwise, as a stream, and pass this one over).
    if ratio < 0.95:
        assert measure(tuned, with_entry, calls, device).ratio < 1.05
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, device, Refinement.EXACT)
    assert result.ok, result.why


def test_a_cascade_chain_longer_than_the_array_is_refused(device):
    """Sixteen partials chain sixteen cores, more than a path east and south across npu2 passes.

    A count, checked before any analysis or placement.
    """
    recording = toys.gemv_fan_in_recording("too_long", M, 2 * GEMV_K, 16)
    profile = Profile()
    profile.add_entry(Entry(root=toys.cascade_reducer_region(recording)))
    verdict = fit(profile, [Timed(recording)], device)
    assert not verdict.ok and verdict.stage == "counts"
    assert "a cascade chain of 16 cores" in (verdict.why or "")


def test_two_cascades_into_one_core_are_refused(device):
    """A core has one cascade input, so an add reading both partials off the cascade is refused by the counts."""
    recording = toys.gemv_fan_in_recording("two_in", M, GEMV_K, 2)
    region = toys.fan_in_reducer_region(recording)
    for index in range(len(region.edges)):
        region = region.held(index, Hold.CASCADE)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    verdict = fit(profile, [Timed(recording)], device)
    assert not verdict.ok and verdict.stage == "counts"
    assert "one cascade input" in (verdict.why or "")


@pytest.mark.parametrize(("device", "splits"), GEMM_CHAINS, indirect=["device"])
def test_the_gemm_cascade_reducer_runs_core_to_core(splits, device):
    """Each add spliced into its partial's GEMM cores, the running sum carried on the cascade core to core: every edge meets as it is."""
    recording = toys.reduction_recording(
        f"gemm_cascade_{splits}",
        toys.gemm_k_split_partials(GEMM_M, GEMM_K, GEMM_N, splits),
    )
    region = toys.cascade_reducer_region(recording)
    analysis = analyze(region, recording, device)
    assert analysis.why is None
    assert all(analysis.hand_off[e] is HandOff.EQUAL for e in region.edges)

