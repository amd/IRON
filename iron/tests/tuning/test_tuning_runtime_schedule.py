# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Runtime schedule: how a region's transfers run, and what waits for what."""

from __future__ import annotations

from aie.dialects.aie import get_target_model

from iron.common.declare.composition import (
    Edge as CompositionEdge,
)
from iron.common.declare.composition import (
    Entry,
    Member,
    Refinement,
    Region,
    RuntimePlan,
    Schedule,
)
from iron.common.declare.profile import Profile
from iron.common.image.step import EdgeKind
from iron.tests.support import toys_schedule
from iron.tests.support.fusable import gemv_silu_mul, gemv_silu_mul_recording
from iron.tests.support.tools import DEVICES
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

DEVICE = DEVICES["npu2"]()


def _window_region(
    waits="barrier", overlap="none", chunks=1, in_flight=None, chained=False
):
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    members = (
        Member(type(gemv), {"M": gemv.M, "K": gemv.K}),
        Member(type(silu), {"size": silu.size}),
        Member(type(mul), {"size": mul.size}),
    )
    edges = (
        CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STREAM),
        CompositionEdge(1, "y", 2, "a", kind=EdgeKind.STREAM),
    )
    runtime = RuntimePlan(
        waits=waits,
        overlap=overlap,
        chunks=chunks,
        in_flight=in_flight,
        chained=chained,
    )
    region = Region(parts=members, edges=edges, runtime=runtime)
    recording = gemv_silu_mul_recording("runtime_window", gemv, silu, mul)
    return region, recording


def _skip_region(phases=None):
    add, norm, proj, add2 = toys_schedule.skip()
    members = (
        Member(type(add), {"size": add.size}),
        Member(type(norm), {"rows": norm.rows}),
        Member(type(proj), {"M": proj.M, "K": proj.K}),
        Member(type(add2), {"size": add2.size}),
    )
    edges = (
        CompositionEdge(0, "y", 1, "x", kind=EdgeKind.STAGED),
        CompositionEdge(1, "y", 2, "B", kind=EdgeKind.STAGED),
        CompositionEdge(2, "C", 3, "a", kind=EdgeKind.STAGED),
        CompositionEdge(0, "y", 3, "b", kind=EdgeKind.STAGED),
    )
    region = Region(parts=members, edges=edges, phases=phases)
    recording = toys_schedule.skip_recording("runtime_skip", add, norm, proj, add2)
    return region, recording


@unbuilt
def test_waits_axis_round_trips_and_is_proposed(tmp_path):
    """``RuntimePlan.waits`` (barrier, per_channel) round-trips through a profile and is a candidate."""
    for waits in ("barrier", "per_channel"):
        region, recording = _window_region(waits=waits)
        entry = Entry(root=region)
        profile = Profile()
        profile.add_entry(entry)
        profile.save(tmp_path / f"waits_{waits}.json")
        loaded = Profile.load(tmp_path / f"waits_{waits}.json")
        assert loaded.entries() == [entry]
        start = Profile()
        assert any(
            entry in edit.apply(start).entries()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_overlap_axis_round_trips_and_is_proposed(tmp_path):
    """``RuntimePlan.overlap`` (none, prefetch, pipelined) round-trips and is a candidate."""
    for overlap in ("none", "prefetch", "pipelined"):
        region, recording = _window_region(overlap=overlap)
        entry = Entry(root=region)
        profile = Profile()
        profile.add_entry(entry)
        profile.save(tmp_path / f"overlap_{overlap}.json")
        loaded = Profile.load(tmp_path / f"overlap_{overlap}.json")
        assert loaded.entries() == [entry]
        start = Profile()
        assert any(
            entry in edit.apply(start).entries()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_chunks_axis_round_trips_and_is_proposed(tmp_path):
    """``RuntimePlan.chunks`` (phases repeated within one call) round-trips and is a candidate."""
    for chunks in (1, 2, 4):
        region, recording = _window_region(chunks=chunks)
        entry = Entry(root=region)
        profile = Profile()
        profile.add_entry(entry)
        profile.save(tmp_path / f"chunks_{chunks}.json")
        loaded = Profile.load(tmp_path / f"chunks_{chunks}.json")
        assert loaded.entries() == [entry]
        start = Profile()
        assert any(
            entry in edit.apply(start).entries()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_in_flight_axis_round_trips_and_is_proposed(tmp_path):
    """``RuntimePlan.in_flight`` (tasks per channel; None for the queue depth) round-trips and is a candidate."""
    depth = get_target_model(DEVICE.resolve()).get_dma_task_queue_depth()
    for in_flight in (1, depth // 2 or 1, depth):
        region, recording = _window_region(in_flight=in_flight)
        entry = Entry(root=region)
        profile = Profile()
        profile.add_entry(entry)
        profile.save(tmp_path / f"in_flight_{in_flight}.json")
        loaded = Profile.load(tmp_path / f"in_flight_{in_flight}.json")
        assert loaded.entries() == [entry]
        start = Profile()
        assert any(
            entry in edit.apply(start).entries()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_chained_axis_round_trips_and_is_proposed(tmp_path):
    """``RuntimePlan.chained`` (one task with chained BDs vs many tasks) round-trips and is a candidate."""
    for chained in (False, True):
        region, recording = _window_region(chained=chained)
        entry = Entry(root=region)
        profile = Profile()
        profile.add_entry(entry)
        profile.save(tmp_path / f"chained_{chained}.json")
        loaded = Profile.load(tmp_path / f"chained_{chained}.json")
        assert loaded.entries() == [entry]
        start = Profile()
        assert any(
            entry in edit.apply(start).entries()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_burst_and_transfer_bytes_round_trip_and_are_proposed(tmp_path):
    """``RuntimePlan.burst`` and ``transfer_bytes`` (DDR access shape) round-trip and are candidates."""
    for burst, transfer_bytes in ((None, None), (256, 4096), (512, 8192)):
        gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
        runtime = RuntimePlan(burst=burst, transfer_bytes=transfer_bytes)
        members = (
            Member(type(gemv), {"M": gemv.M, "K": gemv.K}),
            Member(type(silu), {"size": silu.size}),
            Member(type(mul), {"size": mul.size}),
        )
        edges = (
            CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STREAM),
            CompositionEdge(1, "y", 2, "a", kind=EdgeKind.STREAM),
        )
        region = Region(parts=members, edges=edges, runtime=runtime)
        entry = Entry(root=region)
        recording = gemv_silu_mul_recording("runtime_burst", gemv, silu, mul)
        profile = Profile()
        profile.add_entry(entry)
        profile.save(tmp_path / f"burst_{burst}_{transfer_bytes}.json")
        loaded = Profile.load(tmp_path / f"burst_{burst}_{transfer_bytes}.json")
        assert loaded.entries() == [entry]
        start = Profile()
        assert any(
            entry in edit.apply(start).entries()
            for edit in candidates([Timed(recording)], start, DEVICE)
        )


@unbuilt
def test_phase_boundaries_round_trip_and_are_proposed(tmp_path):
    """``Region.phases`` boundaries on the skip toy (one phase a GEMV's row, two past it) round-trip and are candidates."""
    region, recording = _skip_region(phases=(0, 1, 2, 2))
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "phases.json")
    loaded = Profile.load(tmp_path / "phases.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
def test_window_schedule_is_bit_identical_with_no_hang():
    """The window at every ``RuntimePlan`` setting is bit-identical to the steps run apart, and does not hang."""
    base_region, recording = _window_region()
    base_profile = Profile()
    base_profile.add_entry(Entry(root=base_region))
    for waits in ("barrier", "per_channel"):
        region, _ = _window_region(waits=waits)
        profile = Profile()
        profile.add_entry(Entry(root=region))
        result = check(
            profile, base_profile, [Timed(recording)], DEVICE, Refinement.EXACT
        )
        assert result.ok, result.why


@unbuilt
def test_skip_phases_are_bit_identical_with_no_hang():
    """The skip toy at a phase boundary past its held edge is bit-identical to the steps run apart, and does not hang."""
    base_region, recording = _skip_region()
    base_profile = Profile()
    base_profile.add_entry(Entry(root=base_region))
    region, _ = _skip_region(phases=(0, 1, 2, 2))
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base_profile, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_tuner_keeps_the_schedule_that_pays():
    """The tuner, on the window toy alone, keeps the ``RuntimePlan`` setting that pays."""
    _, recording = _window_region()
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(
        isinstance(e.root, Region) and e.root.runtime is not None
        for e in found.entries()
    )


@unbuilt
def test_a_consumer_scheduled_before_its_producer_is_refused():
    """A schedule ordering a consumer before its producer is refused before any build."""
    region, recording = _window_region()
    profile = Profile()
    profile.add_entry(Entry(root=region))
    # Order the multiply (part 2) before the GEMV (part 0) it depends on.
    profile.add_schedule(Schedule(version=recording.version, order=((2, 0),)))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "before" in (result.why or "")


@unbuilt
def test_a_channel_reused_before_a_sure_await_is_refused():
    """A channel reused before its task's await is refused before any build, not left to hang the command."""
    region, recording = _window_region(waits="per_channel", in_flight=1, chained=False)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage in ("counts", "analysis")
    assert "reused" in (result.why or "") or "await" in (result.why or "")


@unbuilt
def test_more_tasks_in_flight_than_a_channels_queue_is_refused():
    """``in_flight`` past the channel's task queue depth is refused by counts, before any build."""
    depth = get_target_model(DEVICE.resolve()).get_dma_task_queue_depth()
    region, recording = _window_region(in_flight=depth + 1)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "queue" in (result.why or "")


@unbuilt
def test_more_buffer_descriptors_than_a_tile_has_is_refused():
    """A chunked, chained schedule past a tile's buffer-descriptor budget is refused by counts."""
    region, recording = _window_region(chunks=4096, chained=True)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "descriptor" in (result.why or "") or "BD" in (result.why or "")


@unbuilt
def test_a_skip_crossing_a_phase_boundary_unheld_is_refused():
    """A skip edge on the stream, held in no memtile or DDR, crossing a phase boundary is refused before any build."""
    add, norm, proj, add2 = toys_schedule.skip()
    members = (
        Member(type(add), {"size": add.size}),
        Member(type(norm), {"rows": norm.rows}),
        Member(type(proj), {"M": proj.M, "K": proj.K}),
        Member(type(add2), {"size": add2.size}),
    )
    edges = (
        CompositionEdge(0, "y", 1, "x", kind=EdgeKind.STAGED),
        CompositionEdge(1, "y", 2, "B", kind=EdgeKind.STAGED),
        CompositionEdge(2, "C", 3, "a", kind=EdgeKind.STAGED),
        CompositionEdge(0, "y", 3, "b", kind=EdgeKind.STREAM),
    )
    region = Region(parts=members, edges=edges, phases=(0, 1, 2, 2))
    recording = toys_schedule.skip_recording(
        "runtime_skip_unheld", add, norm, proj, add2
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "phase" in (result.why or "")
