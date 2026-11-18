# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Initial tokens on feedback edges, pipeline fill and drain, and a partial last token."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.graph.sdf import analyze
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.tests.support import sequences
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check, fit

pytestmark = pytest.mark.usefixtures("npu2")


@unbuilt
def test_running_sum_with_one_initial_token_loses_nothing_over_several_calls():
    """A running-sum loop (``acc`` carried across calls) over several calls: ``check`` holds it to the same accumulation run one call at a time."""
    region, add = toys.running_sum()
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.running_sum_recording("fill", add, carried=True)
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_running_max_and_sum_carries_both_accumulators():
    """Two parallel carried accumulators (running max, running sum) on one edge pair, both carried: neither is lost or doubled."""
    maxacc = ElementwiseAdd(size=128, tile_size=128)
    sumacc = ElementwiseAdd(size=128, tile_size=128)
    members = (
        Member(cls=type(maxacc), dims={"size": maxacc.size}),
        Member(cls=type(sumacc), dims={"size": sumacc.size}),
    )
    edges = (
        Edge(0, "y", 0, "a"),
        Edge(1, "y", 1, "a"),
    )
    region = Region(parts=members, edges=edges)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    steps = sequences.steps(
        (maxacc, "running_max", "x", "running_max"),
        (sumacc, "running_sum", "x", "running_sum"),
    )
    recording = Recording.of_steps(
        "max-and-sum",
        steps,
        ["x"],
        ["running_max", "running_sum"],
        feedback=["running_max", "running_sum"],
    )
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_partial_last_token_is_neither_lost_nor_duplicated():
    """128 elements at a 32-element tile, called at a per-call bound of 100.

    Four whole tiles are built; the per-call bound leaves a four-element
    partial last tile: no lost or extra tokens across the boundary.
    """
    add = ElementwiseAdd(size=128, tile_size=32, num_aie_columns=1)
    region = Region(
        parts=(Member(cls=type(add), dims={"size": add.size}),),
        edges=(),
    )
    profile = Profile()
    profile.add_entry(Entry(root=region))
    steps = sequences.steps((add, "a", "b", "out"))
    recording = Recording.of_steps("partial-last", steps, ["a", "b"], ["out"])
    result = check(profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT)
    assert result.ok, result.why


def test_feedback_cycle_analysis_reports_its_carried_objects():
    """``analyze`` on the running-sum cycle: the carried value's objects start on the edge, and with them the cycle runs."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("delay-reported", add, carried=True)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.initial[region.edges[0]] == add.size // add.tile_size
    assert analysis.why is None


def test_a_cycle_without_enough_initial_values_is_refused_before_any_build():
    """The same cycle with ``acc`` not carried across calls.

    Refused by ``fit`` at stage ``"analysis"``, the deadlock a missing
    initial token on a feedback edge causes.
    """
    region, add = toys.running_sum()
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.running_sum_recording("delay-missing", add, carried=False)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "analysis"
