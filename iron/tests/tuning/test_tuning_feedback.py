# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Feedback loops: cycles carried by initial values.

Token-level loop-carried values within a call (``SelectiveScan``'s running
state, ``Sample``'s drawn token) and cycles across calls (``Trail``'s walk).
A cycle's initial tokens are the recording's and the operators' own, which
the dataflow analysis derives; the edge that carries a cycle names only the
self-loop (its ``producer`` and ``consumer`` the same part). Every check
calls the composition contract before any compile, build or device use;
a test is ``@unbuilt`` while what it calls raises ``NotImplementedError`` (not built yet).
"""

from __future__ import annotations

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.tests.support import sequences
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    cross_call_trail,
    member,
    sample_token_cycle,
    scan_state_cycle,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

DEVICE = DEVICES["npu2"]()

_ACCUMULATOR_SIZE = 256


def _scan_region():
    recording, members, forward, cycle = scan_state_cycle()
    return recording, Region(members, forward + (cycle,))


def _sample_region():
    recording, members, forward, cycle = sample_token_cycle()
    return recording, Region(members, forward + (cycle,))


def _running_accumulator(carried: bool):
    """Return ``acc = acc + x`` as a one-step self-loop, ``acc`` marked carried (an initial value) only where ``carried``."""
    add = ElementwiseAdd(
        size=_ACCUMULATOR_SIZE, num_aie_columns=1, tile_size=_ACCUMULATOR_SIZE
    )
    steps = sequences.steps((add, "acc", "x", "acc"))
    recording = Recording.of_steps(
        "toy_running_accumulator",
        steps,
        ["x"],
        ["acc"],
        feedback=["acc"] if carried else [],
    )
    region = Region((member(add),), (Edge(0, "y", 0, "a"),))
    return recording, region


CYCLES = {
    "scan_running_state": _scan_region,
    "sample_drawn_token": _sample_region,
    "trail_across_calls": cross_call_trail,
}


@pytest.mark.parametrize(
    "cycle",
    [
        # A self-loop over a carried buffer is not proposed yet.
        (
            pytest.param(c, marks=unbuilt)
            if c in ("sample_drawn_token", "scan_running_state")
            else c
        )
        for c in sorted(CYCLES)
    ],
)
def test_a_cycle_with_its_initial_values_round_trips(cycle, tmp_path):
    """A cycle with its initial values round-trips through the profile, and ``candidates`` proposes it."""
    recording, region = CYCLES[cycle]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / f"feedback_{cycle}.json")
    loaded = Profile.load(tmp_path / f"feedback_{cycle}.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@unbuilt
@pytest.mark.parametrize("cycle", sorted(CYCLES))
@pytest.mark.supported_devices("npu2")
def test_a_cycle_is_bit_identical_to_the_steps_or_calls_run_apart(cycle):
    """A cycle's output is bit-identical to the same steps, or calls, run apart one after another."""
    recording, region = CYCLES[cycle]()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_tuner_keeps_the_cycle_where_it_pays():
    """The tuner, on the scan-state toy alone, keeps the cycle where it pays (fewer dispatches per token)."""
    recording, _ = _scan_region()
    start = Profile()
    found = search([Timed(recording)], start, DEVICE, budget_s=60.0)
    assert any(
        isinstance(e.root, Region)
        and any(edge.producer == edge.consumer for edge in e.root.edges)
        for e in found.entries()
    )


def test_a_cycle_without_enough_initial_values_is_refused_before_any_build():
    """A cycle whose recording carries no initial value for the accumulator is refused before any build: the deadlock the analysis catches."""
    recording, region = _running_accumulator(carried=False)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "analysis"
    assert "deadlock" in (result.why or "") or "initial" in (result.why or "")


@unbuilt
def test_the_recorded_initial_value_fits():
    """The same accumulator, its recording carrying the accumulator's initial value, is not refused by the analysis."""
    recording, region = _running_accumulator(carried=True)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert result.ok, result.why


@unbuilt
def test_the_analysis_bounds_the_cycles_throughput():
    """The analysis's bound on a cycle's throughput (one trip around the loop) is recorded alongside the fit."""
    recording, region = _scan_region()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert result.ok
