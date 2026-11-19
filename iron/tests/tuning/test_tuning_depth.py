# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The depth family: the minimum deadlock-free depth, below it, and past the knee, for every edge role, hand-off shape and rate."""

import multiprocessing

import numpy as np
import pytest
from aie.utils import set_current_device

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement
from iron.common.graph.sdf import analyze
from iron.common.image.step import HandOff
from iron.tests.support import toys_dataflow as toys
from iron.tests.support import toys_edges
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.fusions import Applied
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


# Each role, shape and rate whose toy the composer builds at its minimum.
_BUILT_MINIMUMS = {
    ("chain", HandOff.SPLIT, "same"),
    ("chain", HandOff.BROADCAST, "same"),
    ("chain", HandOff.SLICES, "same"),
    ("chain", HandOff.LAYOUT, "same"),
    ("chain", HandOff.LAYOUT, "different"),
    *(
        ("fan_out", shape, rate)
        for shape in (
            HandOff.EQUAL,
            HandOff.JOIN,
            HandOff.SPLIT,
            HandOff.RATIO,
            HandOff.LAYOUT,
        )
        for rate in toys_edges.RATES
    ),
    ("fan_in", HandOff.JOIN, "same"),
    ("fan_in", HandOff.JOIN, "different"),
    ("fan_in", HandOff.SPLIT, "same"),
    ("fan_in", HandOff.BROADCAST, "same"),
    ("fan_in", HandOff.SLICES, "same"),
    ("fan_in", HandOff.LAYOUT, "same"),
    ("fan_in", HandOff.LAYOUT, "different"),
    ("skip", HandOff.BROADCAST, "same"),
    ("skip", HandOff.SLICES, "same"),
    ("skip", HandOff.LAYOUT, "same"),
    ("skip", HandOff.LAYOUT, "different"),
    ("diamond", HandOff.JOIN, "same"),
    ("diamond", HandOff.JOIN, "different"),
    ("diamond", HandOff.SPLIT, "same"),
    ("diamond", HandOff.BROADCAST, "same"),
    ("diamond", HandOff.SLICES, "same"),
    ("diamond", HandOff.LAYOUT, "same"),
    ("diamond", HandOff.LAYOUT, "different"),
}


@pytest.mark.parametrize(
    ("role", "shape", "rate"),
    [
        pytest.param(
            role,
            shape,
            rate,
            id=f"role_{role}-shape_{shape}-rate_{rate}",
            marks=() if (role, shape, rate) in _BUILT_MINIMUMS else unbuilt,
        )
        for role in toys_edges.ROLES
        for shape in toys_edges.SHAPES
        for rate in toys_edges.RATES
    ],
)
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


_HANG_S = 60


def _run_rate_skip(depth: int) -> None:
    """Build ``toys.rate_skip`` at skip depth ``depth`` and run it once on npu2: the target a hang-safe child runs."""
    region, recording = toys.rate_skip(depth=depth)
    profile = Profile()
    profile.add_entry(Entry(region))
    rng = np.random.default_rng(0)
    inputs = [rng.standard_normal(h.shape).astype(h.dtype) for h in recording.inputs]
    with set_current_device(toys.NPU2):
        graph = Applied.of(Timed(recording), profile, toys.NPU2).built(toys.NPU2)
        graph(*inputs)
        graph.release()


def test_rate_skip_runs_bit_identical_at_its_minimum():
    """A skip around a norm that takes four of its producer's tiles a row: the analysis's minimum (four) is safe, the window bit-identical there."""
    region, recording = toys.rate_skip()
    minimum = analyze(region, recording, toys.NPU2).min_depth[region.edges[1]]
    assert minimum == 4
    region, recording = toys.rate_skip(depth=minimum)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="the analysis counts a reading end alone, not its producer's own "
    "buffers: on npu2 this skip runs read three deep and hangs at two, one "
    "below the analysis's minimum of four",
)
@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
def test_rate_skip_deadlocks_one_below_its_minimum_opt_in_device_check():
    """One below the analysis's minimum really deadlocks on the device, confirming the analysis is tight and not merely safe.

    Run in a spawned child killed past ``_HANG_S``: the deliberate exception
    to "a hang always fails a test".
    """
    region, recording = toys.rate_skip()
    minimum = analyze(region, recording, toys.NPU2).min_depth[region.edges[1]]
    child = multiprocessing.get_context("spawn").Process(
        target=_run_rate_skip, args=(minimum - 1,)
    )
    child.start()
    child.join(_HANG_S)
    hung = child.is_alive()
    if hung:
        child.kill()
    assert hung, f"skip depth {minimum - 1} ran; the analysis's minimum is {minimum}"


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
    One depth names every edge, so its bounds are the deepest edge's. Large
    enough that the cores' work, not the call's dispatch, sets its time.
    """
    add, silu, mul = toys.add_silu_mul(size=1 << 18, cols=2)
    recording = toys.add_silu_mul_recording("measured-depth", add, silu, mul)
    calls = [Timed(recording)]
    base_region = toys.add_silu_mul_region(add, silu, mul)
    analysis = analyze(base_region, recording, toys.NPU2)
    minimum = max(analysis.min_depth.values())
    knee = max(analysis.knee_depth.values())
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
    assert list(analyze(at_knee, recording, toys.NPU2).knee_depth.values()) == list(
        analysis.knee_depth.values()
    )
