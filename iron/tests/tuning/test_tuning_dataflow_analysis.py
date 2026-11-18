# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The SDF analysis on textbook graphs with known exact answers, resolved for a real device."""

import pytest

from iron.common.graph.sdf import analyze
from iron.tests.support import toys_dataflow as toys

pytestmark = pytest.mark.usefixtures("npu2")


def test_balanced_chain_is_consistent_firing_once_a_tile():
    """``add -> SiLU -> mul``, a tile an object: consistent, each core firing once a tile in a call, minimum depth 1 on each edge."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul)
    recording = toys.add_silu_mul_recording("balanced", add, silu, mul)
    analysis = analyze(region, recording, toys.NPU2)
    tiles = add.size // add.tile_size
    assert analysis.consistent
    assert analysis.why is None
    assert analysis.repetition == {0: tiles, 1: tiles, 2: tiles}
    assert all(d == 1 for d in analysis.min_depth.values())


def test_cycle_without_a_carried_value_deadlocks_at_any_depth():
    """A one-actor accumulate loop with nothing carried: its first read waits on its own write, so no depth runs."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("no-delay", add, carried=False)
    analysis = analyze(region, recording, toys.NPU2)
    assert region.edges[0] not in analysis.min_depth
    assert analysis.why is not None and "deadlocks" in analysis.why


def test_cycle_with_its_value_carried_holds_the_call_plus_one():
    """The same loop with ``acc`` carried across calls needs the carried objects plus one.

    The edge starts holding every object the last call left, and the core
    takes a slot for each new one while it still holds the old.
    """
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("one-delay", add, carried=True)
    analysis = analyze(region, recording, toys.NPU2)
    carried = add.size // add.tile_size
    assert analysis.initial[region.edges[0]] == carried
    assert analysis.min_depth[region.edges[0]] == carried + 1
    assert analysis.why is None


def test_known_multi_rate_edge_minimum_buffer():
    """A real multi-rate edge with both sides above one: a 32-row GEMM tile feeding a 48-row GEMM tile.

    At ``M = 384`` both GEMMs resolve npu2's four core rows, so each
    firing really moves ``tile_m * n_aie_rows`` rows: 128 and 192.
    Repetition ``(3, 2)`` (``192 / gcd(128, 192)``, ``128 / gcd(128,
    192)``). A memtile restages whole objects in whole rounds, and the
    smallest round both sides divide is ``lcm(128, 192) = 384`` rows, the
    whole call, so the producer's side holds all three of its objects, not
    the ``128 + 192 - gcd(128, 192)`` rows a shared row-by-row buffer would.
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
    assert analysis.min_depth[region.edges[0]] == 3
