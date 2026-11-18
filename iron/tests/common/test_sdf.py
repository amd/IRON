# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One call of actors replaying their objectFIFO accesses: balance, deadlock and the smallest depths."""

from iron.common.graph.sdf import Channel, Event, Flow


def test_a_two_to_three_edge_needs_p_plus_q_minus_their_gcd():
    """Three firings writing two objects into two reading three: depth 2 + 3 - gcd(2, 3) = 4."""
    write = [Event(0, True, True, 2), Event(0, True, False, 2)]
    read = [Event(0, False, True, 3), Event(0, False, False, 3)]
    flow = Flow([Channel(0, 1)], [write * 3, read * 2])
    assert flow.balance() is None
    assert flow.minimum_depths() == ({0: 4}, None)
    assert flow.runs({0: 3}) is not None


def test_a_one_to_one_chain_runs_one_object_deep():
    """A middle core holding its input while it takes an output slot still needs one object an edge."""
    middle = [
        Event(0, False, True, 1),
        Event(1, True, True, 1),
        Event(0, False, False, 1),
        Event(1, True, False, 1),
    ]
    flow = Flow(
        [Channel(0, 1), Channel(1, 2)],
        [
            [Event(0, True, True, 1), Event(0, True, False, 1)] * 4,
            middle * 4,
            [Event(1, False, True, 1), Event(1, False, False, 1)] * 4,
        ],
    )
    assert flow.minimum_depths() == ({0: 1, 1: 1}, None)


def test_a_carried_value_held_while_its_slot_is_taken_needs_two():
    """A core reading its carried value and taking the slot for the next before freeing the first needs two objects; freeing first needs one."""
    held = [
        Event(0, False, True, 1),
        Event(0, True, True, 1),
        Event(0, False, False, 1),
        Event(0, True, False, 1),
    ]
    freed_first = [
        Event(0, False, True, 1),
        Event(0, False, False, 1),
        Event(0, True, True, 1),
        Event(0, True, False, 1),
    ]
    assert Flow([Channel(0, 0, initial=1)], [held * 4]).minimum_depths() == (
        {0: 2},
        None,
    )
    assert Flow([Channel(0, 0, initial=1)], [freed_first * 4]).minimum_depths() == (
        {0: 1},
        None,
    )
    depths, why = Flow([Channel(0, 0)], [held * 4]).minimum_depths()
    assert depths == {}
    assert why is not None and "actor 0 at access 0 of 16" in why


def test_rates_that_do_not_balance_name_the_edge():
    """Six objects written a call and four read leave the edge unbalanced."""
    flow = Flow(
        [Channel(0, 1)],
        [
            [Event(0, True, True, 2), Event(0, True, False, 2)] * 3,
            [Event(0, False, True, 1), Event(0, False, False, 1)] * 4,
        ],
    )
    why = flow.balance()
    assert why is not None and "6 objects written a call, 4 read" in why


def test_a_sliding_window_needs_its_window_deep():
    """DepthwiseConv1d's core as recorded: ramp up holding one to four rows, then hold five releasing one a row, then drop four.

    Five deep is the least that runs, and four deadlocks.
    """
    rows, taps = 12, 5
    out = [Event(1, True, True, 1), Event(1, True, False, 1)]
    ramp = [e for held in range(1, taps) for e in [Event(0, False, True, held), *out]]
    window = [
        Event(0, False, True, taps),
        Event(1, True, True, 1),
        Event(0, False, False, 1),
        Event(1, True, False, 1),
    ]
    conv = ramp + window * (rows - (taps - 1)) + [Event(0, False, False, taps - 1)]
    flow = Flow(
        [Channel(0, 1), Channel(1, 2)],
        [
            [Event(0, True, True, 1), Event(0, True, False, 1)] * rows,
            conv,
            [Event(1, False, True, 1), Event(1, False, False, 1)] * rows,
        ],
    )
    assert flow.balance() is None
    assert flow.minimum_depths() == ({0: taps, 1: 1}, None)
    assert flow.runs({0: taps - 1, 1: 1}) is not None


def _diamond(skip_phase: int) -> Flow:
    """Return a producer feeding a two-step path and, by a skip edge, the step joining them, four objects a call."""
    return Flow(
        [Channel(0, 1), Channel(1, 2), Channel(2, 3), Channel(0, 3, phase=skip_phase)],
        [
            [
                Event(0, True, True, 1),
                Event(3, True, True, 1),
                Event(0, True, False, 1),
                Event(3, True, False, 1),
            ]
            * 4,
            [
                Event(0, False, True, 1),
                Event(1, True, True, 1),
                Event(0, False, False, 1),
                Event(1, True, False, 1),
            ]
            * 4,
            [
                Event(1, False, True, 1),
                Event(2, True, True, 1),
                Event(1, False, False, 1),
                Event(2, True, False, 1),
            ]
            * 4,
            [
                Event(2, False, True, 1),
                Event(3, False, True, 1),
                Event(2, False, False, 1),
                Event(3, False, False, 1),
            ]
            * 4,
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


def test_a_fixed_edge_is_held_at_its_depth_and_not_searched():
    """An operator's own fifo, held at the depth its build chose, is left out of the search and constrains the rest."""
    flow = _diamond(skip_phase=1)
    assert flow.minimum_depths(fixed={3: 4}) == ({0: 1, 1: 1, 2: 4}, None)
    depths, why = flow.minimum_depths(fixed={3: 3})
    assert depths == {} and why is not None
