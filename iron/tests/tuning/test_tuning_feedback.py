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

import dataclasses

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Hold, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.tests.support import sequences
from iron.tests.support.toys_edges import (
    cross_call_trail,
    member,
    sample_token_cycle,
    scan_state_cycle,
)
from iron.tests.support.tuning import reached_by_candidates, unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, search

_ACCUMULATOR_SIZE = 256


def _scan_region():
    recording, members, forward, cycle = scan_state_cycle()
    # By producer, then consumer: the self-loop first.
    return recording, Region(members, (cycle,) + forward)


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
        [] if carried else ["acc"],
        feedback=["acc"] if carried else [],
    )
    region = Region((member(add),), (Edge(0, "y", 0, "a"),))
    return recording, region


def _accumulator_into_mul():
    """Return ``acc = acc + x`` carried, streamed on chip into a multiply by ``up``; the self-loop is edge 0."""
    add = ElementwiseAdd(
        size=_ACCUMULATOR_SIZE, num_aie_columns=1, tile_size=_ACCUMULATOR_SIZE
    )
    mul = ElementwiseMul(
        size=_ACCUMULATOR_SIZE, num_aie_columns=1, tile_size=_ACCUMULATOR_SIZE
    )
    steps = sequences.steps((add, "acc", "x", "acc"), (mul, "acc", "up", "out"))
    recording = Recording.of_steps(
        "toy_accumulator_into_mul", steps, ["x", "up"], ["out"], feedback=["acc"]
    )
    region = Region(
        (member(add), member(mul)), (Edge(0, "y", 0, "a"), Edge(0, "y", 1, "a"))
    )
    return recording, region


CYCLES = {
    "scan_running_state": _scan_region,
    "sample_drawn_token": _sample_region,
    "trail_across_calls": cross_call_trail,
}

# Each cycle whose carry is one buffer the recording carries: its self-loop
# is edge 0.
CARRIED = {
    "running_accumulator": lambda: _running_accumulator(carried=True),
    "accumulator_into_mul": _accumulator_into_mul,
    "scan_running_state": _scan_region,
}


@pytest.mark.parametrize(
    "cycle",
    [
        # The drawn token's carry into tokens is no recorded buffer, so no
        # candidate edit reaches the cycle.
        (pytest.param(c, marks=unbuilt) if c == "sample_drawn_token" else c)
        for c in sorted(CYCLES)
    ],
)
def test_a_cycle_with_its_initial_values_round_trips(cycle, tmp_path, device):
    """A cycle with its initial values round-trips through the profile, and composing ``candidates``' edits reaches it."""
    recording, region = CYCLES[cycle]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / f"feedback_{cycle}.json")
    loaded = Profile.load(tmp_path / f"feedback_{cycle}.json")
    assert loaded.entries() == [entry]
    reached = reached_by_candidates(region, [Timed(recording)], device)
    assert reached.entries() == [entry]


@pytest.mark.parametrize(
    "cycle",
    [
        (
            pytest.param(
                c,
                marks=pytest.mark.xfail(
                    strict=True,
                    raises=ValueError,
                    reason="Sample's token reaches the next call's tokens through "
                    "a carry no step-level recording names, so its self-loop "
                    "matches no recorded buffer",
                ),
            )
            if c == "sample_drawn_token"
            else pytest.param(c, marks=unbuilt)
        )
        # Trail's carry is checked on its own below.
        for c in sorted(CYCLES)
        if c != "trail_across_calls"
    ],
)
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_cycle_is_bit_identical_to_the_steps_or_calls_run_apart(cycle, device):
    """A cycle's output is bit-identical to the same steps, or calls, run apart one after another."""
    recording, region = CYCLES[cycle]()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


# Its steps depend through memory, so they run a phase apart: a full ELF's.
@pytest.mark.supported_devices("npu2")
def test_a_carry_no_caller_starts_is_bit_identical_from_each_end_of_its_range(
    device,
):
    """Trail's walk, its node and step count carried to the next call and given by no caller, is bit-identical started at each end of their recorded ranges."""
    recording, region = cross_call_trail()
    assert recording.carry, "the toy carries values across calls"
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_a_carry_with_no_recorded_range_is_refused_by_name(device):
    """A call checked apart that carries a value no caller starts and no recorded range bounds is not checked: nothing says where a first call starts it."""
    recording, region = cross_call_trail()
    unbounded = dataclasses.replace(
        recording,
        limits=[
            limit for limit in recording.limits if limit.expression.value.name != "node"
        ],
    )
    profile = Profile()
    profile.add_entry(Entry(region))
    with pytest.raises(NotImplementedError, match="no recorded range"):
        check(profile, Profile(), [Timed(unbounded)], device, Refinement.EXACT)


@pytest.mark.extensive
@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="candidates does not propose a self-loop over a carried buffer yet",
)
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_keeps_the_cycle_where_it_pays(device):
    """The tuner, on the scan-state toy alone, keeps the cycle where it pays (fewer dispatches per token)."""
    recording, _ = _scan_region()
    start = Profile()
    found = search([Timed(recording)], start, device, budget_s=60.0)
    assert any(
        isinstance(e.root, Region)
        and any(edge.producer == edge.consumer for edge in e.root.edges)
        for e in found.entries()
    )


def test_a_cycle_without_enough_initial_values_is_refused_before_any_build(device):
    """A cycle whose recording carries no initial value for the accumulator is refused before any build: the deadlock the analysis catches."""
    recording, region = _running_accumulator(carried=False)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "deadlock" in (result.why or "") or "initial" in (result.why or "")


@pytest.mark.parametrize("cycle", sorted(CARRIED))
@pytest.mark.supported_devices("npu2")
def test_a_carry_held_in_host_memory_is_bit_identical_to_the_calls_run_apart(
    cycle, device
):
    """A cycle whose carry across calls waits in host memory builds, its other edges on chip, bit-identical to its steps run apart."""
    recording, region = CARRIED[cycle]()
    profile = Profile()
    profile.add_entry(Entry(region.held(0, Hold.DDR)))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_a_carry_through_host_memory_with_no_initial_value_is_refused(device):
    """A self-loop held in host memory over a buffer the recording does not carry is refused before any build: the first call has nothing to read."""
    recording, region = _running_accumulator(carried=False)
    profile = Profile()
    profile.add_entry(Entry(region.held(0, Hold.DDR)))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "no initial value" in (result.why or "")


@pytest.mark.parametrize("hold", [Hold.L1, Hold.MEMTILE])
def test_a_carry_held_on_chip_between_calls_waits_on_residency(hold, device):
    """A carry across calls held on chip is not built: it stays resident between commands, which nothing loads or keeps yet."""
    recording, region = _running_accumulator(carried=True)
    profile = Profile()
    profile.add_entry(Entry(region.held(0, hold)))
    with pytest.raises(NotImplementedError, match="resident between calls"):
        fit(profile, [Timed(recording)], device)


@unbuilt
def test_the_recorded_initial_value_fits(device):
    """The same accumulator, its recording carrying the accumulator's initial value, is not refused by the analysis."""
    recording, region = _running_accumulator(carried=True)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert result.ok, result.why


@unbuilt
def test_the_analysis_bounds_the_cycles_throughput(device):
    """The analysis's bound on a cycle's throughput (one trip around the loop) is recorded alongside the fit."""
    recording, region = _scan_region()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert result.ok
