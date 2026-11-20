# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The SDF analysis on textbook graphs with known exact answers, resolved for a real device."""

import pytest
from aie.dialects.aie import get_target_model

from iron.common.graph.sdf import analyze
from iron.common.image.step import HandOff
from iron.tests.support import toys_composition
from iron.tests.support import toys_dataflow as toys

pytestmark = pytest.mark.usefixtures("device")


def test_balanced_chain_is_consistent_firing_once_a_tile(device):
    """``add -> SiLU -> mul``, a tile an object: consistent, each core firing once a tile in a call, minimum depth 1 on each edge."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul)
    recording = toys.add_silu_mul_recording("balanced", add, silu, mul)
    analysis = analyze(region, recording, device)
    tiles = add.size // add.tile_size
    assert analysis.consistent
    assert analysis.why is None
    assert analysis.repetition == {0: tiles, 1: tiles, 2: tiles}
    assert all(d == 1 for d in analysis.min_depth.values())


@pytest.mark.parametrize(("n", "tiles"), [(None, 8), (1024, 8), (512, 4), (130, 2)])
def test_a_bounded_call_fires_the_tiles_its_own_values_cover(n, tiles, device):
    """``add -> mul`` over the first ``n`` of 1024 elements, a 128-element tile an object: a call fires each core once a tile its ``n`` covers.

    A call that gives no ``n`` is a whole one, the largest the recording's
    limits admit.
    """
    recording = toys.BoundedChain().record(a=(1024,), b=(1024,), c=(1024,))
    region = toys.bounded_chain_region(recording)
    analysis = analyze(region, recording, device, None if n is None else {"n": n})
    assert analysis.consistent
    assert analysis.repetition == {0: tiles, 1: tiles}
    assert analysis.tokens[region.edges[0]] == ((1,), (1,))


def test_cycle_without_a_carried_value_deadlocks_at_any_depth(device):
    """A one-actor accumulate loop with nothing carried: its first read waits on its own write, so no depth runs."""
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("no-delay", add, carried=False)
    analysis = analyze(region, recording, device)
    assert region.edges[0] not in analysis.min_depth
    assert analysis.why is not None and "deadlocks" in analysis.why


def test_cycle_with_its_value_carried_holds_the_call_plus_one(device):
    """The same loop with ``acc`` carried across calls needs the carried objects plus one.

    The edge starts holding every object the last call left, and the core
    takes a slot for each new one while it still holds the old.
    """
    region, add = toys.running_sum()
    recording = toys.running_sum_recording("one-delay", add, carried=True)
    analysis = analyze(region, recording, device)
    carried = add.size // add.tile_size
    assert analysis.initial[region.edges[0]] == carried
    assert analysis.min_depth[region.edges[0]] == carried + 1
    assert analysis.why is None


def test_known_multi_rate_edge_minimum_buffer(device):
    """A real multi-rate edge with both sides above one: a 32-row GEMM tile feeding a 48-row GEMM tile.

    At ``M = 384`` both GEMMs resolve every core row of a column (four,
    on npu1 and npu2), so each
    firing really moves ``tile_m * n_aie_rows`` rows: 128 and 192.
    Repetition ``(3, 2)`` (``192 / gcd(128, 192)``, ``128 / gcd(128,
    192)``). A memtile restages the edge: it takes each 128-row object as
    it comes, so the producer's side holds one object, and its own storage
    holds the rows the consumer's 192-row objects need, rather than the two
    sharing the ``128 + 192 - gcd(128, 192)`` rows of one buffer.
    """
    producer, consumer = toys.gemm_into_gemm(
        device, M=384, width=64, producer_tile=32, consumer_tile=48
    )
    model = get_target_model(device.resolve())
    rows = sum(model.is_core_tile(0, row) for row in range(model.rows()))
    assert producer.n_aie_rows == rows
    assert consumer.n_aie_rows == rows
    region = toys.gemm_into_gemm_region(producer, consumer)
    recording = toys.gemm_into_gemm_recording("multi-rate", producer, consumer)
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert analysis.repetition == {0: 3, 1: 2}
    assert analysis.min_depth[region.edges[0]] == 1


def test_a_step_spliced_into_its_producers_cores_holds_each_cores_call(device):
    """A SiLU spliced into a GEMM's cores reads each core's tiles after the GEMM's body runs through the call: the edge holds every tile a core writes.

    A 64 by 128 GEMM in 32 by 32 tiles on one column takes a core a row of
    tiles, two cores, each writing four tiles a call; three deadlock.
    """
    recording, region = toys_composition.gemm_silu_splice(
        "splice", M=64, N=128, tile=32
    )
    analysis = analyze(region, recording, device)
    edge = region.edges[0]
    assert analysis.why is None
    assert analysis.hand_off[edge] is HandOff.EQUAL
    assert analysis.repetition == {0: 4, 1: 4}
    assert analysis.min_depth[edge] == 4
    assert analysis.deadlock({edge: 3}) is not None
