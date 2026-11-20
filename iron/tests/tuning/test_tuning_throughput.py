# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Throughput: the bottleneck actor and one trip around a cycle, from the analysis and measured runs."""

import dataclasses
from fractions import Fraction

import aie.utils as aie_utils
import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Region
from iron.common.graph.clock import kernel_cycles
from iron.common.graph.sdf import analyze
from iron.common.image.step import Edge, EdgeKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU
from iron.tests.support import toys_dataflow as toys
from iron.tests.support import toys_schedule
from iron.tests.support.toys_edges import member
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import measure

pytestmark = pytest.mark.usefixtures("device")

# Elements a measured toy moves: its cores' work, not a call's dispatch, sets its time.
MEASURED = 1 << 18


def test_a_kernel_is_priced_only_on_the_npu_it_is_built_for(device):
    """A kernel's cycles are traced on its own NPU: built for any other than the one attached, or with none attached, its pricing waits.

    So the analysis has no knee there, and candidates proposes the depth
    doublings alone rather than failing on the device.
    """
    runtime = aie_utils.DefaultNPURuntime
    attached = None if runtime is None else runtime.device().resolve().name
    if device.resolve().name == attached:
        pytest.skip(f"{attached} is attached, so its kernels are traced")
    add = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    with pytest.raises(NotImplementedError, match="it is built for attached"):
        kernel_cycles(add.kernel(), add.scalars())


# npu1's waits on host 203.
@pytest.mark.supported_devices("npu2")
def test_every_core_is_priced_its_kernels_own_scalars_and_calls(device):
    """A norm feeding two GEMVs: every core is priced by its kernel's traced cycles.

    RMSNorm's kernel takes its epsilon at run time, the norm's own; GEMV's
    writes a slice of its output tile a call, so it is traced over the
    calls that fill the tile.
    """
    norm, gate, up = toys_schedule.two_gemv_window(columns=1, channels=1)
    recording = toys_schedule.two_gemv_window_recording("priced", norm, gate, up)
    region = Region(
        (member(norm), member(gate), member(up)),
        (
            Edge(0, "y", 1, "B", kind=EdgeKind.STREAM),
            Edge(0, "y", 2, "B", kind=EdgeKind.STREAM),
        ),
    )
    analysis = analyze(region, recording, device)
    priced = [
        max(costs)
        for costs, kernels in zip(analysis.costs, analysis.kernels, strict=True)
        if kernels
    ]
    assert len(priced) == 3
    assert all(cycles > 0 for cycles in priced)
    assert ((norm.epsilon,),) in analysis.scalars


@pytest.mark.supported_devices("npu1", "npu2")
def test_unbalanced_pipeline_period_is_the_bottleneck_actors(device):
    """``add -> SiLU -> mul`` at uneven widths, SiLU at one column against the others' two: a positive period, bounded by the narrower, slower actor."""
    add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=512, tile_size=128, num_aie_columns=1)
    mul = ElementwiseMul(size=512, tile_size=128, num_aie_columns=2)
    region = toys.add_silu_mul_region(add, silu, mul)
    recording = toys.add_silu_mul_recording("bottleneck", add, silu, mul)
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert isinstance(analysis.period, Fraction)
    assert analysis.period > 0


@pytest.mark.supported_devices("npu1", "npu2")
def test_narrowing_the_bottleneck_actor_raises_the_period(device):
    """Narrowing SiLU, the bottleneck (several times add's cycles a call), from two columns to one raises the period."""
    add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    wide = SiLU(size=512, tile_size=128, num_aie_columns=2)
    narrow = SiLU(size=512, tile_size=128, num_aie_columns=1)
    mul = ElementwiseMul(size=512, tile_size=128, num_aie_columns=2)
    wide_region = toys.add_silu_mul_region(add, wide, mul)
    narrow_region = toys.add_silu_mul_region(add, narrow, mul)
    wide_recording = toys.add_silu_mul_recording("wide-bottleneck", add, wide, mul)
    narrow_recording = toys.add_silu_mul_recording(
        "narrow-bottleneck", add, narrow, mul
    )
    wide_period = analyze(wide_region, wide_recording, device).period
    narrow_period = analyze(narrow_region, narrow_recording, device).period
    assert narrow_period > wide_period


@pytest.mark.supported_devices("npu1", "npu2")
def test_widening_a_non_bottleneck_actor_leaves_the_period_unchanged(device):
    """Widening ``add``, which is not the bottleneck, from one column to two leaves the period unchanged; SiLU alone still bounds it."""
    narrow_add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=1)
    wide_add = ElementwiseAdd(size=512, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=512, tile_size=128, num_aie_columns=1)
    mul = ElementwiseMul(size=512, tile_size=128, num_aie_columns=1)
    narrow_region = toys.add_silu_mul_region(narrow_add, silu, mul)
    wide_region = toys.add_silu_mul_region(wide_add, silu, mul)
    narrow_recording = toys.add_silu_mul_recording("narrow-add", narrow_add, silu, mul)
    wide_recording = toys.add_silu_mul_recording("wide-add", wide_add, silu, mul)
    narrow_period = analyze(narrow_region, narrow_recording, device).period
    wide_period = analyze(wide_region, wide_recording, device).period
    assert narrow_period == wide_period


@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_measured_seconds_a_call_tracks_the_analyzed_period(device):
    """Narrowing the bottleneck's tunable, as a profile edit over one recorded toy, raises both the analyzed period and the measured seconds a call.

    ``measure``'s paired runs against a ``base`` profile are how the
    analysis's period is held to a real clock; this is the timing half of
    the bottleneck check above, restored once ``measure`` names what to
    pair against what. Large enough that the cores' work, not the call's
    dispatch, sets the time a call; staged, as a two-column lane meeting a
    one-column one needs.
    """
    add = ElementwiseAdd(size=MEASURED, tile_size=128, num_aie_columns=2)
    silu = SiLU(size=MEASURED, tile_size=128, num_aie_columns=2)
    mul = ElementwiseMul(size=MEASURED, tile_size=128, num_aie_columns=2)
    recording = toys.add_silu_mul_recording("measured-period", add, silu, mul)
    wide_region = toys.add_silu_mul_region(add, silu, mul, kind=EdgeKind.STAGED)
    narrow_region = Region(
        parts=(
            wide_region.parts[0],
            dataclasses.replace(
                wide_region.parts[1],
                tunables={"num_aie_columns": 1, "tile_size": silu.tile_size},
            ),
            wide_region.parts[2],
        ),
        edges=wide_region.edges,
    )
    wide_period = analyze(wide_region, recording, device).period
    narrow_period = analyze(narrow_region, recording, device).period
    assert narrow_period > wide_period
    wide_profile = Profile()
    wide_profile.add_entry(Entry(root=wide_region))
    narrow_profile = Profile()
    narrow_profile.add_entry(Entry(root=narrow_region))
    measured = measure(narrow_profile, wide_profile, [Timed(recording)], device)
    assert measured.ratio > 1.0
    assert measured.seconds > measured.base_seconds


@pytest.mark.supported_devices("npu1", "npu2")
def test_feedback_loop_period_is_one_trip_around_the_cycle(device):
    """The running-sum loop: a positive period, the time one trip around the cycle takes, independent of how many cycles the call runs."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("cycle-period", add, carried=True)
    analysis = analyze(region, recording, device)
    assert analysis.period > 0
