# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One call of actors firing over bounded channels: balance, deadlock and the smallest depths."""

from iron.common.graph.sdf import Channel, Firing, Flow


def test_a_two_to_three_edge_needs_p_plus_q_minus_their_gcd():
    """Three firings writing two objects into two reading three: depth 2 + 3 - gcd(2, 3) = 4."""
    flow = Flow(
        [Channel(0, 1)],
        [
            [Firing(writes={0: 2})] * 3,
            [Firing(holds={0: 3}, releases={0: 3})] * 2,
        ],
    )
    assert flow.balance() is None
    assert flow.repetition() == {0: 3, 1: 2}
    assert flow.minimum_depths() == ({0: 4}, None)
    assert flow.runs({0: 3}) is not None
    assert flow.runs({0: 4}) is None


def test_a_one_to_one_chain_runs_one_object_deep():
    """A chain moving one object a firing never needs more than one in flight."""
    one = Firing(holds={0: 1}, releases={0: 1}, writes={1: 1})
    flow = Flow(
        [Channel(0, 1), Channel(1, 2)],
        [
            [Firing(writes={0: 1})] * 4,
            [one] * 4,
            [Firing(holds={1: 1}, releases={1: 1})] * 4,
        ],
    )
    assert flow.minimum_depths() == ({0: 1, 1: 1}, None)


def test_a_carried_value_needs_its_initial_token():
    """A running sum: with its one carried token it runs one deep; without it, it never starts."""
    step = Firing(holds={0: 1}, releases={0: 1}, writes={0: 1})
    carried = Flow([Channel(0, 0, initial=1)], [[step] * 4])
    assert carried.balance() is None
    assert carried.minimum_depths() == ({0: 1}, None)
    missing = Flow([Channel(0, 0)], [[step] * 4])
    depths, why = missing.minimum_depths()
    assert depths == {}
    assert why is not None and "actor 0 at firing 0 of 4" in why


def test_rates_that_do_not_balance_name_the_edge():
    """Six objects written a call and four read leave the edge unbalanced."""
    flow = Flow(
        [Channel(0, 1)],
        [
            [Firing(writes={0: 2})] * 3,
            [Firing(holds={0: 1}, releases={0: 1})] * 4,
        ],
    )
    why = flow.balance()
    assert why is not None and "6 objects written a call, 4 read" in why


def test_a_sliding_window_needs_its_window_deep():
    """DepthwiseConv1d's core: hold 1 to 4 rows ramping up, then 5 releasing 1 a row, then drop the last 4.

    The window holds five rows at once, so five deep is the least that runs
    and four deadlocks.
    """
    rows, taps = 12, 5
    ramp = [Firing(holds={0: held}) for held in range(1, taps)]
    steady = [Firing(holds={0: taps}, releases={0: 1})] * (rows - (taps - 1))
    drain = [Firing(holds={0: taps - 1}, releases={0: taps - 1})]
    flow = Flow(
        [Channel(0, 1)], [[Firing(writes={0: 1})] * rows, ramp + steady + drain]
    )
    assert flow.balance() is None
    assert flow.minimum_depths() == ({0: taps}, None)
    assert flow.runs({0: taps - 1}) is not None


def _diamond(skip_phase: int) -> Flow:
    """Return a producer feeding a two-step path and, by a skip edge, the step joining them, four objects a call."""
    return Flow(
        [
            Channel(0, 1),
            Channel(1, 2),
            Channel(2, 3),
            Channel(0, 3, phase=skip_phase),
        ],
        [
            [Firing(writes={0: 1, 3: 1})] * 4,
            [Firing(holds={0: 1}, releases={0: 1}, writes={1: 1})] * 4,
            [Firing(holds={1: 1}, releases={1: 1}, writes={2: 1})] * 4,
            [Firing(holds={2: 1, 3: 1}, releases={2: 1, 3: 1})] * 4,
        ],
    )


def test_a_diamond_in_one_phase_runs_one_object_deep():
    """Each step waits on the one before it, so the skip edge's reader drains it before the producer writes again."""
    assert _diamond(skip_phase=0).minimum_depths() == ({0: 1, 1: 1, 2: 1, 3: 1}, None)


def test_a_skip_edge_read_a_phase_later_holds_the_whole_call():
    """Its reader starts only once the earlier phase has written everything, so the skip edge and the join's other input each hold all four objects."""
    flow = _diamond(skip_phase=1)
    assert flow.minimum_depths() == ({0: 1, 1: 1, 2: 4, 3: 4}, None)
    assert flow.runs({0: 1, 1: 1, 2: 4, 3: 3}) is not None
    assert flow.runs({0: 1, 1: 1, 2: 2, 3: 4}) is not None
