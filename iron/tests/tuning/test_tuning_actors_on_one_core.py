# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Two actors on one core, over the composition contract."""

from __future__ import annotations

import pytest

from iron.common.declare.composition import (
    Edge as CompositionEdge,
)
from iron.common.declare.composition import (
    Entry,
    Member,
    Refinement,
    Region,
)
from iron.common.declare.profile import Profile
from iron.operators import (
    GEMV,
    Decode,
    ElementwiseAdd,
    ElementwiseMul,
    RMSNorm,
    SiLU,
    Softmax,
)
from iron.tests.support import toys_composition as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

pytestmark = pytest.mark.usefixtures("npu2")

M = 64

# (producer dims, consumer dims), producer output, consumer input: the fold hook
# replacements, each its own toy (``iron.tests.support.toys_composition.PAIR_TOYS``).
PAIR_REGIONS = {
    "gemv_silu": (Member(GEMV, dict(M=M, K=M)), Member(SiLU, dict(size=M))),
    "decode_gemv": (
        Member(Decode, dict(M=256, K=192)),
        Member(GEMV, dict(M=256, K=192)),
    ),
    "add_softmax": (
        Member(ElementwiseAdd, dict(size=32 * 64)),
        Member(Softmax, dict(rows=32, cols=64)),
    ),
    "rmsnorm_mul": (
        Member(RMSNorm, dict(rows=1)),
        Member(ElementwiseMul, dict(size=M)),
    ),
}


def _joined_region(
    producer: Member, consumer: Member, output: str, input: str
) -> Region:
    return Region(
        parts=(producer, consumer),
        edges=(CompositionEdge(0, output, 1, input),),
        workers=((0, 1),),
    )


def _named_region_and_recording(name: str) -> tuple[Region, object]:
    producer, consumer = PAIR_REGIONS[name]
    pair_fn, recording_fn, output, input = toys.PAIR_TOYS[name]
    region = _joined_region(producer, consumer, output, input)
    recording = recording_fn(name, *pair_fn())
    return region, recording


@unbuilt
@pytest.mark.parametrize("name", list(PAIR_REGIONS))
def test_two_actors_on_one_core_round_trip_as_an_entry(name, tmp_path, npu2):
    region, recording = _named_region_and_recording(name)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
@pytest.mark.parametrize(
    "recording_fn, topology",
    [
        (lambda: toys.fan_in_recording("fan_in"), "fan-in"),
        (lambda: toys.fan_out_recording("fan_out"), "fan-out"),
        (
            lambda: toys.partner_and_outside_recording("partner_outside"),
            "partner-and-outside",
        ),
        (
            lambda: toys.output_also_read_outside_recording("output_outside"),
            "output-also-outside",
        ),
        (lambda: toys.multi_output_recording("multi_output"), "multi-output"),
    ],
    ids=[
        "fan_in",
        "fan_out",
        "partner_and_outside",
        "output_also_outside",
        "multi_output",
    ],
)
def test_every_topology_is_proposed_on_its_producer_s_core(
    recording_fn, topology, npu2
):
    recording = recording_fn()
    composed = [
        edit.apply(Profile())
        for edit in candidates([Timed(recording)], Profile(), npu2)
    ]
    assert any(
        toys.has_worker_group(e) for profile in composed for e in profile.entries()
    )


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("name", list(PAIR_REGIONS))
def test_two_actors_on_one_core_is_bit_identical_to_the_steps_run_apart(name, npu2):
    region, recording = _named_region_and_recording(name)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_per_call_size_below_the_recorded_one_still_runs_on_one_core(npu2):
    """A valid KV length or a partial prompt chunk below the recorded size still joins."""
    small = _joined_region(
        Member(ElementwiseAdd, dict(size=16 * 64)),
        Member(Softmax, dict(rows=16, cols=64)),
        "y",
        "x",
    )
    add, softmax = toys.add_softmax_pair(rows=16, cols=64)
    recording = toys.add_softmax_recording("small_call", add, softmax)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=small))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("name", list(PAIR_REGIONS))
def test_search_keeps_the_pair_joined_where_it_pays(name, npu2):
    region, recording = _named_region_and_recording(name)
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
    result = check(tuned, start, calls, npu2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_a_pair_over_a_core_s_memory_is_refused(npu2):
    region = _joined_region(
        Member(GEMV, dict(M=16384, K=16384)), Member(SiLU, dict(size=16384)), "C", "x"
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.fan_out_recording("oversized", M=16384)
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "counts"


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_mismatched_tile_sizes_are_refused(npu2):
    """AXPY's kernel takes tiles of a multiple of 64; a GEMV writing 2 at a time cannot carry it onto one worker."""
    recording = toys.mismatched_tile_recording("mismatched")
    composed = [
        edit.apply(Profile())
        for edit in candidates([Timed(recording)], Profile(), npu2)
    ]
    assert not any(
        toys.has_worker_group(e) for profile in composed for e in profile.entries()
    )


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_more_than_a_core_s_two_input_channels_is_refused(npu2):
    """A binary consumer needs a free input channel; both of a core's are already the producer's."""
    region = _joined_region(
        Member(ElementwiseMul, dict(size=M)),
        Member(ElementwiseAdd, dict(size=M)),
        "y",
        "a",
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.fan_in_recording("no_channel")
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "counts"


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_gemv_refuses_under_repeat(npu2):
    """GEMV's ``repeat`` keeps its own channel state across calls, which a fold cannot share."""
    region = _joined_region(
        Member(GEMV, dict(M=M, K=M, repeat=2)),
        Member(ElementwiseAdd, dict(size=M)),
        "C",
        "b",
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemv_add_recording("repeat_refused", M=M, K=M, repeat=2)
    verdict = fit(profile, [Timed(recording)], npu2)
    assert not verdict.ok and verdict.stage == "analysis"
