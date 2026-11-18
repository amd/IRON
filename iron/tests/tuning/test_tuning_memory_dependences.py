# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Dependences through memory, no edge between the steps.

A KV-style write (a ``Copy`` at a per-call position) and a read of the cache
share one buffer in the recording; the dataflow analysis is what derives
their order (no ``Region`` field names it). Every check calls the
composition contract before any compile, build or device use; a test is ``@unbuilt`` while what it calls raises ``NotImplementedError`` (not built yet).
"""

from __future__ import annotations

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Configuration, Entry, Refinement, Region
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import interleaved_kv_write, kv_write_then_read
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

DEVICE = DEVICES["npu2"]()

TABLE_ROWS = 8
POSITIONS = {
    "first": 0,
    "middle": TABLE_ROWS // 2,
    "last": TABLE_ROWS - 1,
}


def _region(position: int):
    recording, members = kv_write_then_read(position, table_rows=TABLE_ROWS)
    region = Region(members, ())
    return recording, region


@unbuilt
@pytest.mark.parametrize("position", sorted(POSITIONS))
def test_a_write_then_read_region_round_trips_at_every_position(position, tmp_path):
    """A region holding the writer and the reader, sharing the cache buffer the analysis orders them by.

    Round-trips at the first, a middle and the last position.
    """
    recording, region = _region(POSITIONS[position])
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / f"kv_{position}.json")
    loaded = Profile.load(tmp_path / f"kv_{position}.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
@pytest.mark.parametrize(
    "footprint", ["lo", "lo_plus_one", "hi_minus_one", "hi", "recorded"]
)
def test_footprints_round_trip_at_the_boundary_positions_and_as_a_hull(
    footprint, tmp_path
):
    """Footprints checked at lo, lo+1, hi-1, hi, the recorded value, and as a hull over the whole per-call range."""
    at = {
        "lo": 0,
        "lo_plus_one": 1,
        "hi_minus_one": TABLE_ROWS - 2,
        "hi": TABLE_ROWS - 1,
        "recorded": TABLE_ROWS - 1,
    }[footprint]
    recording, region = _region(at)
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
def test_two_interleaved_writers_round_trip_with_element_disjointness_named():
    """Paired K and V writers at interleaved elements: their hulls overlap, so disjointness is named element by element."""
    recording, members = interleaved_kv_write(position=1, table_rows=TABLE_ROWS)
    region = Region(members, ())
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
@pytest.mark.parametrize("position", sorted(POSITIONS))
@pytest.mark.supported_devices("npu2")
def test_write_then_read_is_bit_identical_to_the_steps_run_apart(position):
    """The write-then-read region is bit-identical to the same steps run apart, at each position."""
    recording, region = _region(POSITIONS[position])
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_tuner_keeps_the_region_where_it_pays():
    """The tuner, on the write-then-read toy alone, keeps the region (no host round trip between the steps) where it pays."""
    recording, _ = _region(POSITIONS["middle"])
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(isinstance(e.root, Region) for e in found.entries())


@unbuilt
def test_two_configurations_sharing_a_memory_dependence_at_once_is_refused():
    """A writer and a reader of the same cache buffer, named concurrent across two configurations, are refused before any build.

    The dependence through the shared buffer is no longer a ``Region.order``
    choice to omit: it is the recording's own fact. Disregarding it (running
    the writer and the reader "at once" in ``Configuration.concurrent``
    slots, as if they were independent) is what the analysis refuses.
    """
    recording, members = kv_write_then_read(POSITIONS["middle"], table_rows=TABLE_ROWS)
    write, read = members
    profile = Profile()
    profile.add_entry(Entry(Configuration(parts=(write,), concurrent=1)))
    profile.add_entry(Entry(Configuration(parts=(read,), concurrent=1)))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "independent" in (result.why or "") or "shared" in (result.why or "")
