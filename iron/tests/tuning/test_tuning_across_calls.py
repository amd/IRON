# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Across calls: several calls per command, overlap between them, and state carried from one to the next."""

from __future__ import annotations

import pytest

from iron.common.declare.composition import Configuration, Entry, Refinement, Schedule
from iron.common.declare.profile import Profile
from iron.tests.support import toys_schedule
from iron.tests.support.toys_edges import kv_write_then_read
from iron.tests.support.tuning import scheduled_by_candidates, unbuilt
from iron.tune.autotune import Timed
from iron.tune.cli import watchdog_s
from iron.tune.measure import Timing
from iron.tune.search import check, fit, measure, search

_DECODE_STEPS = 16


def _decode_recording():
    gemv, add = toys_schedule.decode_step()
    return toys_schedule.decode_step_recording("across_calls_decode", gemv, add)


def _kv_recording():
    write, read = toys_schedule.kv_write_read(width=64)
    return toys_schedule.kv_write_read_recording("across_calls_kv", write, read)


def test_calls_per_command_round_trips_and_is_proposed(tmp_path, device):
    """``Schedule.calls_per_command`` (1, 2, 4) round-trips through a profile and is a candidate."""
    recording = _decode_recording()
    for calls_per_command in (1, 2, 4):
        schedule = Schedule(
            version=recording.version, calls_per_command=calls_per_command
        )
        profile = Profile()
        profile.add_schedule(schedule)
        profile.save(tmp_path / f"calls_per_command_{calls_per_command}.json")
        loaded = Profile.load(tmp_path / f"calls_per_command_{calls_per_command}.json")
        assert loaded.schedules() == [schedule]
        assert scheduled_by_candidates(
            schedule, [Timed(recording)], device
        ).schedules() == [schedule]


def test_calls_overlapped_round_trips_and_is_proposed(tmp_path, device):
    """``Schedule.calls_overlapped`` (calls in flight inside one command) round-trips and is a candidate."""
    recording = _decode_recording()
    schedule = Schedule(
        version=recording.version, calls_per_command=2, calls_overlapped=1
    )
    profile = Profile()
    profile.add_schedule(schedule)
    profile.save(tmp_path / "calls_overlapped.json")
    loaded = Profile.load(tmp_path / "calls_overlapped.json")
    assert loaded.schedules() == [schedule]
    assert scheduled_by_candidates(
        schedule, [Timed(recording)], device
    ).schedules() == [schedule]


@unbuilt
def test_interleave_with_decode_and_prefill_round_trips_and_is_proposed(
    tmp_path, device
):
    """``Schedule.interleave_with`` (decode interleaved with prefill) round-trips and is a candidate."""
    decode = _decode_recording()
    prefill = _decode_recording()
    schedule = Schedule(version=decode.version, interleave_with=(prefill.version,))
    profile = Profile()
    profile.add_schedule(schedule)
    profile.save(tmp_path / "interleave.json")
    loaded = Profile.load(tmp_path / "interleave.json")
    assert loaded.schedules() == [schedule]
    assert scheduled_by_candidates(
        schedule, [Timed(decode), Timed(prefill)], device
    ).schedules() == [schedule]


def test_derived_size_merging_two_calls_round_trips_and_is_proposed(tmp_path, device):
    """``Schedule.size`` naming a derived version (two prefill chunks as one) round-trips and is a candidate."""
    recording = _decode_recording()
    schedule = Schedule(version=recording.version, size="merged_2x")
    profile = Profile()
    profile.add_schedule(schedule)
    profile.save(tmp_path / "derived_size.json")
    loaded = Profile.load(tmp_path / "derived_size.json")
    assert loaded.schedules() == [schedule]
    assert scheduled_by_candidates(
        schedule, [Timed(recording)], device
    ).schedules() == [schedule]


@pytest.mark.supported_devices("npu1", "npu2")
def test_several_calls_per_command_are_bit_identical_to_one_per_command(device):
    """Two and four calls per command are bit-identical to the same calls run one per command, one command at a time."""
    recording = _decode_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=1))
    for calls_per_command in (2, 4):
        profile = Profile()
        profile.add_schedule(
            Schedule(version=recording.version, calls_per_command=calls_per_command)
        )
        result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_calls_merged_into_one_are_bit_identical_to_one_a_command(device):
    """Two and four calls of an elementwise step merged into one call at that many times the size are bit-identical to them one a command."""
    add, mul = toys_schedule.residual_step()
    recording = toys_schedule.residual_step_recording("across_calls_merged", add, mul)
    for calls in (2, 4):
        profile = Profile()
        profile.add_schedule(
            Schedule(version=recording.version, size=f"merged_{calls}x")
        )
        assert fit(profile, [Timed(recording)], device).ok
        result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_merge_into_a_larger_shape_is_no_worse_where_it_reorders_a_reduction(device):
    """Two decode steps merged into one larger GEMV call (GEMV becoming GEMM-shaped) is no-worse against the reference.

    The reduction order changes, so this is held to ``NO_WORSE``, not bit identity.
    """
    recording = _decode_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=1))
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="merged_2x"))
    result = check(profile, base, [Timed(recording)], device, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_residency_across_calls_is_bit_identical_to_reloading(device):
    """State (KV tail) kept resident across calls is bit-identical to reloading it each call."""
    recording = _kv_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version))
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=2))
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_per_call_parameters_updated_inside_one_command_are_bit_identical(device):
    """Per-call parameters (position, valid length) updated between calls inside one command, no new dispatch, are bit-identical to a dispatch each."""
    recording = _kv_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=1))
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=3))
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.parametrize("calls_per_command", [2, 3])
@pytest.mark.supported_devices("npu1", "npu2")
def test_per_call_values_of_calls_in_one_command_are_each_their_own(
    calls_per_command, device
):
    """A cache write then a read bounded per call, several calls a command, bit-identical to a command each.

    Each call reads its own count (the call's and its bound halved, in
    turn), from a cache state the calls before wrote on the device.
    """
    recording, _ = kv_write_then_read(3)
    call = Timed(recording, values={"n": 4})
    base = Profile()
    profile = Profile()
    profile.add_schedule(
        Schedule(version=recording.version, calls_per_command=calls_per_command)
    )
    assert fit(profile, [call], device).ok
    result = check(profile, base, [call], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_commands_in_flight_are_bit_identical_to_one_at_a_time(device):
    """1, 2 and 3 commands in flight from the host are bit-identical to one command finishing before the next is submitted."""
    recording = _decode_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, commands_in_flight=1))
    for commands_in_flight in (2, 3):
        profile = Profile()
        profile.add_schedule(
            Schedule(version=recording.version, commands_in_flight=commands_in_flight)
        )
        result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_several_calls_a_command_are_priced_a_call_at_a_time(device):
    """Four calls a command are timed per call against one a command, not as one command against one call.

    Priced per command, four calls would take about four times one.
    """
    recording = _decode_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=4))
    measured = measure(
        profile, Profile(), [Timed(recording)], device, timing=Timing(rounds=2, calls=8)
    )
    assert measured.ratio < 2, measured


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_keeps_the_call_schedule_that_pays(device):
    """The tuner, on the decode-step toy alone, keeps the call schedule that pays."""
    recording = _decode_recording()
    start = Profile()
    found = search([Timed(recording)], start, device, budget_s=60.0)
    assert any(
        s.calls_per_command > 1 or s.commands_in_flight > 1 for s in found.schedules()
    )


def test_an_overlap_breaking_a_dependence_is_refused(device):
    """Overlapping a KV write-then-read dependence across calls is refused before any build."""
    recording = _kv_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_overlapped=1))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "depend" in (result.why or "") or "overlap" in (result.why or "")


def test_a_merge_breaking_a_dependence_is_refused(device):
    """Merging calls whose carried state the merge would reorder past a feedback cycle's initial values is refused before any build."""
    recording = _kv_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="merged_broken"))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "depend" in (result.why or "") or "merge" in (result.why or "")


def test_state_resident_across_a_teardown_is_refused(device):
    """State kept resident into a command that tears its configuration down is refused before any build."""
    recording = _kv_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=2))
    profile.add_entry(
        Entry(root=Configuration(parts=(), teardown=True, resident=("cache",)))
    )
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "teardown" in (result.why or "")


@unbuilt
def test_a_command_longer_than_the_watchdog_is_refused(device):
    """A command whose calls_per_command exceeds the driver's watchdog (IRON's preflight checks 2x the longest) is refused before any build."""
    if watchdog_s() is None:
        pytest.skip(
            "the driver's watchdog is not readable, so fit holds no command to it"
        )
    recording = _decode_recording()
    profile = Profile()
    profile.add_schedule(
        Schedule(version=recording.version, calls_per_command=_DECODE_STEPS * 1024)
    )
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "watchdog" in (result.why or "") or "timeout" in (result.why or "")
