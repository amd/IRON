# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Across calls: several calls per command, overlap between them, and state carried from one to the next."""

from __future__ import annotations

from iron.common.declare.composition import Configuration, Entry, Refinement, Schedule
from iron.common.declare.profile import Profile
from iron.tests.support import toys_schedule
from iron.tests.support.tools import DEVICES
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

DEVICE = DEVICES["npu2"]()

_DECODE_STEPS = 16


def _decode_recording():
    gemv, add = toys_schedule.decode_step()
    return toys_schedule.decode_step_recording("across_calls_decode", gemv, add)


def _kv_recording():
    write, read = toys_schedule.kv_write_read(width=64)
    return toys_schedule.kv_write_read_recording("across_calls_kv", write, read)


@unbuilt
def test_calls_per_command_round_trips_and_is_proposed(tmp_path):
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
        start = Profile()
        assert any(
            schedule in edit.apply(start).schedules()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_calls_overlapped_round_trips_and_is_proposed(tmp_path):
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


@unbuilt
def test_interleave_with_decode_and_prefill_round_trips_and_is_proposed(tmp_path):
    """``Schedule.interleave_with`` (decode interleaved with prefill) round-trips and is a candidate."""
    decode = _decode_recording()
    prefill = _decode_recording()
    schedule = Schedule(version=decode.version, interleave_with=(str(prefill.version),))
    profile = Profile()
    profile.add_schedule(schedule)
    profile.save(tmp_path / "interleave.json")
    loaded = Profile.load(tmp_path / "interleave.json")
    assert loaded.schedules() == [schedule]


@unbuilt
def test_derived_size_merging_two_calls_round_trips_and_is_proposed(tmp_path):
    """``Schedule.size`` naming a derived version (two prefill chunks as one) round-trips and is a candidate."""
    recording = _decode_recording()
    schedule = Schedule(version=recording.version, size="merged_2x")
    profile = Profile()
    profile.add_schedule(schedule)
    profile.save(tmp_path / "derived_size.json")
    loaded = Profile.load(tmp_path / "derived_size.json")
    assert loaded.schedules() == [schedule]


@unbuilt
def test_several_calls_per_command_are_bit_identical_to_one_per_command():
    """Two and four calls per command are bit-identical to the same calls run one per command, one command at a time."""
    recording = _decode_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=1))
    for calls_per_command in (2, 4):
        profile = Profile()
        profile.add_schedule(
            Schedule(version=recording.version, calls_per_command=calls_per_command)
        )
        result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
        assert result.ok, result.why


@unbuilt
def test_a_merge_into_a_larger_shape_is_no_worse_where_it_reorders_a_reduction():
    """Two decode steps merged into one larger GEMV call (GEMV becoming GEMM-shaped) is no-worse against the reference.

    The reduction order changes, so this is held to ``NO_WORSE``, not bit identity.
    """
    recording = _decode_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=1))
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="merged_2x"))
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.NO_WORSE)
    assert result.ok, result.why


@unbuilt
def test_residency_across_calls_is_bit_identical_to_reloading():
    """State (KV tail) kept resident across calls is bit-identical to reloading it each call."""
    recording = _kv_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version))
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=2))
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_per_call_parameters_updated_inside_one_command_are_bit_identical():
    """Per-call parameters (position, valid length) updated between calls inside one command, no new dispatch, are bit-identical to a dispatch each."""
    recording = _kv_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, calls_per_command=1))
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=3))
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_commands_in_flight_are_bit_identical_to_one_at_a_time():
    """1, 2 and 3 commands in flight from the host are bit-identical to one command finishing before the next is submitted."""
    recording = _decode_recording()
    base = Profile()
    base.add_schedule(Schedule(version=recording.version, commands_in_flight=1))
    for commands_in_flight in (2, 3):
        profile = Profile()
        profile.add_schedule(
            Schedule(version=recording.version, commands_in_flight=commands_in_flight)
        )
        result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
        assert result.ok, result.why


@unbuilt
def test_tuner_keeps_the_call_schedule_that_pays():
    """The tuner, on the decode-step toy alone, keeps the call schedule that pays."""
    recording = _decode_recording()
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(
        s.calls_per_command > 1 or s.commands_in_flight > 1 for s in found.schedules()
    )


@unbuilt
def test_an_overlap_breaking_a_dependence_is_refused():
    """Overlapping a KV write-then-read dependence across calls is refused before any build."""
    recording = _kv_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_overlapped=1))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "depend" in (result.why or "") or "overlap" in (result.why or "")


@unbuilt
def test_a_merge_breaking_a_dependence_is_refused():
    """Merging calls whose carried state the merge would reorder past a feedback cycle's initial values is refused before any build."""
    recording = _kv_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="merged_broken"))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "depend" in (result.why or "") or "merge" in (result.why or "")


@unbuilt
def test_state_resident_across_a_teardown_is_refused():
    """State kept resident into a command that tears its configuration down is refused before any build."""
    recording = _kv_recording()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, calls_per_command=2))
    profile.add_entry(
        Entry(root=Configuration(parts=(), teardown=True, resident=("cache",)))
    )
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "teardown" in (result.why or "")


@unbuilt
def test_a_command_longer_than_the_watchdog_is_refused():
    """A command whose calls_per_command exceeds the driver's watchdog (IRON's preflight checks 2x the longest) is refused before any build."""
    recording = _decode_recording()
    profile = Profile()
    profile.add_schedule(
        Schedule(version=recording.version, calls_per_command=_DECODE_STEPS * 1024)
    )
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "watchdog" in (result.why or "") or "timeout" in (result.why or "")
