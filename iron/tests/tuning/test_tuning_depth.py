# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The depth family: the minimum deadlock-free depth, below it, and past the knee, for every edge role, hand-off shape and rate."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement
from iron.common.graph.sdf import analyze
from iron.common.image.step import HandOff
from iron.tests.support import toys_dataflow as toys
from iron.tests.support import toys_edges
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit, measure, search

pytestmark = pytest.mark.usefixtures("npu2")


def _held_where_it_can_be(role, shape, depth, rate):
    """Return the combination toy, its distinguished edge held in L1 where its derived hand-off streams as is, else in a memtile, and the edge's minimum depth.

    A stream edge's lanes meet as they are, so only an equal or broadcast
    hand-off can be held in L1; the analysis, not the toy's name, says which.
    """
    _, recording, region, index = toys_edges.combination_toy(
        shape, role, "l1", depth, rate, "recorded"
    )
    analysis = analyze(region, recording, toys.NPU2)
    if analysis.hand_off[region.edges[index]] not in (
        HandOff.EQUAL,
        HandOff.BROADCAST,
    ):
        _, recording, region, index = toys_edges.combination_toy(
            shape, role, "memtile", depth, rate, "recorded"
        )
        analysis = analyze(region, recording, toys.NPU2)
    return recording, region, index, analysis.min_depth[region.edges[index]]


@unbuilt
@pytest.mark.parametrize("rate", toys_edges.RATES)
@pytest.mark.parametrize("shape", toys_edges.SHAPES)
@pytest.mark.parametrize("role", toys_edges.ROLES)
def test_minimum_depth_runs_bit_identical(role, shape, rate):
    """Every role, shape and rate, at its distinguished edge's minimum depth: ``check`` holds it bit-identical to the steps run apart."""
    recording, region, index, minimum = _held_where_it_can_be(role, shape, "min", rate)
    region = toys_edges.with_resolved_depth(region, index, minimum)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.parametrize("rate", toys_edges.RATES)
@pytest.mark.parametrize("shape", toys_edges.SHAPES)
@pytest.mark.parametrize("role", toys_edges.ROLES)
def test_depth_below_minimum_is_refused_before_any_build(role, shape, rate):
    """Every role, shape and rate, one short of the minimum: ``fit`` refuses it at stage ``"analysis"``, before any build, and at the minimum it does not."""
    recording, region, index, minimum = _held_where_it_can_be(
        role, shape, "min_minus_one", rate
    )
    at_minimum = Profile()
    at_minimum.add_entry(
        Entry(root=toys_edges.with_resolved_depth(region, index, minimum))
    )
    try:
        result = fit(at_minimum, [Timed(recording)], toys.NPU2)
        assert result.ok, result.why
    except NotImplementedError:
        pass  # Not built yet, which is no refusal.
    profile = Profile()
    profile.add_entry(
        Entry(root=toys_edges.with_resolved_depth(region, index, minimum - 1))
    )
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "analysis"
    assert "deadlock" in (result.why or "")


@pytest.mark.parametrize("role", toys_edges.ROLES)
def test_depth_over_l1_or_memtile_is_refused(role):
    """Every role, at an implausibly deep hold: ``fit`` refuses it at stage ``"counts"``, before any build."""
    _, recording, region, index = toys_edges.combination_toy(
        toys_edges.SHAPES[0], role, "memtile", "more", "same", "recorded"
    )
    region = toys_edges.with_resolved_depth(region, index, 1 << 20)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "counts"


def test_skip_diamond_minimum_depth_is_one():
    """The residual-add skip/broadcast window, its skip read through an end one deep, runs on npu2: the analysis's minimum is that one.

    Measured: the skip's fifo lowers as ``[2, 2, 1]`` (the add's own two,
    the norm's end and the skip's) and runs bit-identical, as it does at
    two, three and four.
    """
    region, first, norm, second = toys.broadcast_skip(depth=None)
    recording = toys.broadcast_skip_recording("known-answer", first, norm, second)
    analysis = analyze(region, recording, toys.NPU2)
    skip_edge = region.edges[1]
    assert analysis.min_depth[skip_edge] == 1


def test_skip_diamond_minimum_depth_runs_bit_identical():
    """The residual-add skip/broadcast window, its skip at its minimum: ``check`` holds it bit-identical to the steps run apart."""
    region, first, norm, second = toys.broadcast_skip(depth=1)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.broadcast_skip_recording("depth-one", first, norm, second)
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.skip(
    reason="this window runs at every skip depth down to one on npu2, so it "
    "has no deadlocking depth to confirm; the tightness check needs a window "
    "whose minimum exceeds one (a diamond through a whole-call reader)"
)
@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
def test_skip_diamond_deadlock_below_its_minimum_opt_in_device_check():
    """A depth below the analysis's minimum really deadlocks on the device, confirming the analysis is tight and not merely safe."""


@pytest.mark.extensive
@unbuilt
def test_tuner_keeps_a_depth_at_or_past_the_minimum():
    """``search``, run on the chain toy alone, keeps a depth at or past the analysis's minimum and passes ``check`` against the start, exact."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul, depth=1)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording("searched-depth", add, silu, mul)
    calls = [Timed(recording)]
    tuned = search(calls, profile, toys.NPU2)
    verdict = check(tuned, profile, calls, toys.NPU2, Refinement.EXACT)
    assert verdict.ok, verdict.why
    tuned_entry = tuned.entries()[0]
    tuned_edge = tuned_entry.root.edges[0]
    analysis = analyze(tuned_entry.root, recording, toys.NPU2)
    assert tuned_edge.depth is not None
    assert tuned_edge.depth >= analysis.min_depth[tuned_edge]


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_each_depth_up_to_the_knee_is_measured_against_the_next():
    """The chain toy at every depth from the analysis's minimum to its knee, each measured against the next by ``measure``'s paired runs.

    The measured knee (the depth past which a further measured pair gains
    nothing more) is the one ``analyze`` itself reports as ``knee_depth``.
    """
    add, silu, mul = toys.add_silu_mul()
    recording = toys.add_silu_mul_recording("measured-depth", add, silu, mul)
    calls = [Timed(recording)]
    base_region = toys.add_silu_mul_region(add, silu, mul)
    analysis = analyze(base_region, recording, toys.NPU2)
    minimum = min(analysis.min_depth.values())
    knee = min(analysis.knee_depth.values())
    for depth in range(minimum, knee):
        shallower = Profile()
        shallower.add_entry(
            Entry(root=toys.add_silu_mul_region(add, silu, mul, depth=depth))
        )
        deeper = Profile()
        deeper.add_entry(
            Entry(root=toys.add_silu_mul_region(add, silu, mul, depth=depth + 1))
        )
        measured = measure(deeper, shallower, calls, toys.NPU2)
        assert measured.ratio <= 1.0
    at_knee = toys.add_silu_mul_region(add, silu, mul, depth=knee)
    assert analyze(at_knee, recording, toys.NPU2).knee_depth == analysis.knee_depth
