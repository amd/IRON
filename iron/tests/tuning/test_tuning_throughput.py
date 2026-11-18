# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Throughput: the bottleneck actor and one trip around a cycle, from the analysis and measured runs."""

import dataclasses
from fractions import Fraction

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Region
from iron.common.graph.sdf import analyze
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import measure

pytestmark = pytest.mark.usefixtures("npu2")


@unbuilt
def test_unbalanced_pipeline_period_is_the_bottleneck_actors():
    """``add -> SiLU -> mul`` at uneven widths, ``mul`` at one column against the others' two: a positive period, bounded by the narrower, slower actor."""
    add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=512, tile_size=128, num_aie_columns=2)
    mul = ElementwiseMul(size=512, tile_size=128, num_aie_columns=1)
    region = toys.add_silu_mul_region(add, silu, mul)
    recording = toys.add_silu_mul_recording("bottleneck", add, silu, mul)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.consistent
    assert isinstance(analysis.period, Fraction)
    assert analysis.period > 0


@unbuilt
def test_narrowing_the_bottleneck_actor_raises_the_period():
    """Narrowing ``mul``, the bottleneck, from two columns to one raises the period; it no longer merely has to be positive."""
    add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=512, tile_size=128, num_aie_columns=2)
    wide = ElementwiseMul(size=512, tile_size=128, num_aie_columns=2)
    narrow = ElementwiseMul(size=512, tile_size=128, num_aie_columns=1)
    wide_region = toys.add_silu_mul_region(add, silu, wide)
    narrow_region = toys.add_silu_mul_region(add, silu, narrow)
    wide_recording = toys.add_silu_mul_recording("wide-bottleneck", add, silu, wide)
    narrow_recording = toys.add_silu_mul_recording(
        "narrow-bottleneck", add, silu, narrow
    )
    wide_period = analyze(wide_region, wide_recording, toys.NPU2).period
    narrow_period = analyze(narrow_region, narrow_recording, toys.NPU2).period
    assert narrow_period > wide_period


@unbuilt
def test_widening_a_non_bottleneck_actor_leaves_the_period_unchanged():
    """Widening ``add``, which is not the bottleneck, from one column to two leaves the period unchanged; ``mul`` alone still bounds it."""
    narrow_add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=1)
    wide_add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=512, tile_size=128, num_aie_columns=1)
    mul = ElementwiseMul(size=512, tile_size=128, num_aie_columns=1)
    narrow_region = toys.add_silu_mul_region(narrow_add, silu, mul)
    wide_region = toys.add_silu_mul_region(wide_add, silu, mul)
    narrow_recording = toys.add_silu_mul_recording("narrow-add", narrow_add, silu, mul)
    wide_recording = toys.add_silu_mul_recording("wide-add", wide_add, silu, mul)
    narrow_period = analyze(narrow_region, narrow_recording, toys.NPU2).period
    wide_period = analyze(wide_region, wide_recording, toys.NPU2).period
    assert narrow_period == wide_period


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_measured_seconds_a_call_tracks_the_analyzed_period():
    """Narrowing the bottleneck's tunable, as a profile edit over one recorded toy, raises both the analyzed period and the measured seconds a call.

    ``measure``'s paired runs against a ``base`` profile are how the
    analysis's period is held to a real clock; this is the timing half of
    the bottleneck check above, restored once ``measure`` names what to
    pair against what.
    """
    add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=512, tile_size=128, num_aie_columns=2)
    mul = ElementwiseMul(size=512, tile_size=128, num_aie_columns=2)
    recording = toys.add_silu_mul_recording("measured-period", add, silu, mul)
    wide_region = toys.add_silu_mul_region(add, silu, mul)
    narrow_region = Region(
        parts=(
            wide_region.parts[0],
            wide_region.parts[1],
            dataclasses.replace(
                wide_region.parts[2],
                tunables={"num_aie_columns": 1, "tile_size": mul.tile_size},
            ),
        ),
        edges=wide_region.edges,
    )
    wide_period = analyze(wide_region, recording, toys.NPU2).period
    narrow_period = analyze(narrow_region, recording, toys.NPU2).period
    assert narrow_period > wide_period
    wide_profile = Profile()
    wide_profile.add_entry(Entry(root=wide_region))
    narrow_profile = Profile()
    narrow_profile.add_entry(Entry(root=narrow_region))
    measured = measure(narrow_profile, wide_profile, [Timed(recording)], toys.NPU2)
    assert measured.ratio > 1.0
    assert measured.seconds > measured.base_seconds


@unbuilt
def test_feedback_loop_period_is_one_trip_around_the_cycle():
    """The running-sum loop: a positive period, the time one trip around the cycle takes, independent of how many cycles the call runs."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("cycle-period", add, carried=True)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.period > 0
