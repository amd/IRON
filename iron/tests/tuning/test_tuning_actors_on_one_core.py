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
from iron.common.graph.record import Recording
from iron.operators import (
    GEMV,
    ElementwiseAdd,
    ElementwiseMul,
    SiLU,
    Softmax,
)
from iron.tests.support import sequences
from iron.tests.support import toys_composition as toys
from iron.tests.support.toys_edges import member
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

pytestmark = pytest.mark.usefixtures("device")

M = 64


# (producer dims, consumer dims), producer output, consumer input: the fold hook
# replacements, each its own toy (``iron.tests.support.toys_composition.PAIR_TOYS``).
def _joined_region(
    producer: Member, consumer: Member, output: str, input: str
) -> Region:
    return Region(
        parts=(producer, consumer),
        edges=(CompositionEdge(0, output, 1, input),),
        workers=((0, 1),),
    )


def _named_region_and_recording(name: str) -> tuple[Region, object]:
    pair_fn, recording_fn, output, input = toys.PAIR_TOYS[name]
    producer, consumer = pair_fn()
    region = _joined_region(member(producer), member(consumer), output, input)
    recording = recording_fn(name, producer, consumer)
    return region, recording


@pytest.mark.parametrize(
    "name",
    [
        # IRON folds neither of these pairs (Operator.fold refuses them).
        (pytest.param(n, marks=unbuilt) if n in ("decode_gemv", "add_softmax") else n)
        for n in toys.PAIR_TOYS
    ],
)
def test_two_actors_on_one_core_round_trip_as_an_entry(name, tmp_path, device):
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
        for edit in candidates(calls, Profile(), device)
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
    recording_fn, topology, device
):
    recording = recording_fn()
    composed = [
        edit.apply(Profile())
        for edit in candidates([Timed(recording)], Profile(), device)
    ]
    assert any(
        toys.has_worker_group(e) for profile in composed for e in profile.entries()
    )


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "name",
    [
        # Decode's A rides another buffer's fifos: an edge into it waits.
        (pytest.param(n, marks=unbuilt) if n == "decode_gemv" else n)
        for n in toys.PAIR_TOYS
    ],
)
def test_two_actors_on_one_core_is_bit_identical_to_the_steps_run_apart(name, device):
    region, recording = _named_region_and_recording(name)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_per_call_size_below_the_recorded_one_still_runs_on_one_core(device):
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
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "name",
    [
        # Decode's A rides another buffer's fifos: an edge into it waits.
        (pytest.param(n, marks=unbuilt) if n == "decode_gemv" else n)
        for n in toys.PAIR_TOYS
    ],
)
def test_search_keeps_the_pair_joined_where_it_pays(name, device):
    region, recording = _named_region_and_recording(name)
    entry = Entry(root=region)
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, device).ratio
    tuned = search(calls, start, device)
    # Where the pair joined pays, what search keeps is at least as fast (it may
    # join the pair otherwise, as a stream window, and pass this one over).
    if ratio < 0.95:
        assert measure(tuned, with_entry, calls, device).ratio < 1.05
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_pair_over_a_core_s_memory_is_refused(device):
    """A GEMV and a SiLU that each fit a core's memory alone, but not together on one worker.

    On one worker the SiLU folds into the GEMV, its kernel run on each
    1024-element output tile. The GEMV alone holds 64640 of a core's 65536
    bytes (npu1's and npu2's alike) (one A tile of 4 rows of 5952, a line, its double-buffered output
    and the stack) and builds; the fold's scratch tile adds 2048.
    """
    gemv = GEMV(M=6144, K=5952, tile_size_input=4, tile_size_output=1024)
    silu = SiLU(size=6144, tile_size=1024)
    region = _joined_region(member(gemv), member(silu), "C", "x")
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = Recording.of_steps(
        "oversized",
        sequences.steps((gemv, "A", "B", "mid"), (silu, "mid", "out")),
        ["A", "B"],
        ["out"],
    )
    verdict = fit(profile, [Timed(recording)], device)
    assert not verdict.ok and verdict.stage == "counts"


@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_mismatched_tile_sizes_are_refused(device):
    """AXPY's kernel takes tiles of a multiple of 64; a GEMV writing 2 at a time cannot carry it onto one worker."""
    recording = toys.mismatched_tile_recording("mismatched")
    composed = [
        edit.apply(Profile())
        for edit in candidates([Timed(recording)], Profile(), device)
    ]
    assert not any(
        toys.has_worker_group(e) for profile in composed for e in profile.entries()
    )


@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_more_than_a_core_s_two_input_channels_is_refused(device):
    """A binary consumer needs a free input channel; both of a core's are already the producer's.

    ``gate``'s GEMV reads ``A`` and ``B`` through the core's two input
    channels, so the multiply on its worker has none left for ``up``'s output.
    """
    region = _joined_region(
        Member(GEMV, dict(M=M, K=M)),
        Member(ElementwiseMul, dict(size=M)),
        "C",
        "a",
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.fan_in_recording("no_channel")
    verdict = fit(profile, [Timed(recording)], device)
    assert not verdict.ok and verdict.stage == "counts"


@pytest.mark.xfail(
    strict=True,
    reason="fit has no rule for repeat's channel state yet; it refuses this "
    "pair only because GEMV's batch-major lanes need a restage into Add's",
)
@pytest.mark.supported_devices("npu1", "npu2")
def test_gemv_refuses_under_repeat(device):
    """GEMV's ``repeat`` keeps its own channel state across calls, which a fold cannot share."""
    region = _joined_region(
        Member(GEMV, dict(M=2048, K=2048, repeat=2)),
        Member(ElementwiseAdd, dict(size=2 * 2048)),
        "C",
        "b",
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemv_add_recording("repeat_refused", M=2048, K=2048, repeat=2)
    verdict = fit(profile, [Timed(recording)], device)
    assert not verdict.ok and verdict.stage == "analysis"
    assert "repeat" in (verdict.why or "")
