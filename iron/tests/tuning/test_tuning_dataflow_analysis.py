# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The SDF analysis on textbook graphs with known exact answers, resolved for a real device."""

import pytest

from iron.common.graph.sdf import analyze
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt

pytestmark = pytest.mark.usefixtures("npu2")


@unbuilt
def test_balanced_chain_is_consistent_with_repetition_one():
    """``add -> SiLU -> mul``, every edge a whole buffer a firing: consistent, repetition vector ``(1, 1, 1)``, minimum depth 1 on each edge."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul)
    recording = toys.add_silu_mul_recording("balanced", add, silu, mul)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.consistent
    assert analysis.why is None
    assert analysis.repetition == {0: 1, 1: 1, 2: 1}
    assert all(d == 1 for d in analysis.min_depth.values())


@unbuilt
def test_inconsistent_cycle_rates_cannot_balance():
    """A two-member cycle whose edges demand incompatible repetitions.

    ``add`` and ``mul`` each move a whole buffer at their own ``tile_size``;
    at different tile sizes, the cycle's forward and backward edges need
    repetition ratios no positive integer vector satisfies, so
    ``consistent`` is False and ``why`` names the cycle.
    """
    region, add, mul = toys.mismatched_rate_cycle(add_tile=64, mul_tile=32)
    recording = toys.mismatched_rate_cycle_recording("inconsistent", add, mul)
    analysis = analyze(region, recording, toys.NPU2)
    assert not analysis.consistent
    assert analysis.why


@unbuilt
def test_cycle_without_a_delay_deadlocks_at_depth_zero():
    """A one-actor accumulate loop with no carried value: the minimum deadlock-free depth is 1, so the uncarried edge is reported as deadlocking."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("no-delay", add, carried=False)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.min_depth[region.edges[0]] == 1
    assert analysis.why


@unbuilt
def test_cycle_with_one_initial_token_runs_at_the_minimum_depth():
    """The same loop with ``acc`` carried across calls: the minimum depth is met and the analysis reports it deadlock-free."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("one-delay", add, carried=True)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.min_depth[region.edges[0]] == 1
    assert analysis.why is None


@unbuilt
def test_known_multi_rate_edge_minimum_buffer():
    """A real multi-rate edge with both sides above one: a 32-row GEMM tile feeding a 48-row GEMM tile.

    At ``M = 384`` both GEMMs resolve npu2's four core rows, so each
    firing really moves ``tile_m * n_aie_rows`` rows: 128 and 192.
    Repetition ``(3, 2)`` (``192 / gcd(128, 192)``, ``128 / gcd(128,
    192)``), minimum buffer ``128 + 192 - gcd(128, 192) = 256``.
    """
    producer, consumer = toys.gemm_into_gemm(
        M=384, width=64, producer_tile=32, consumer_tile=48
    )
    assert producer.n_aie_rows == 4
    assert consumer.n_aie_rows == 4
    region = toys.gemm_into_gemm_region(producer, consumer)
    recording = toys.gemm_into_gemm_recording("multi-rate", producer, consumer)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.consistent
    assert analysis.repetition == {0: 3, 1: 2}
    assert analysis.min_depth[region.edges[0]] == 256
