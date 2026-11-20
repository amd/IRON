# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One call of actors replaying their objectFIFO accesses: balance, deadlock, the smallest depths, and a period over phases at a device's host streams."""

import dataclasses
from fractions import Fraction

import pytest

from iron.common.graph.sdf import Ceiling, Channel, Event, Flow

# A ceiling shaped as npu2's (Strix Halo) measures: flat to eight streams,
# shared past them.
CEILING = Ceiling(
    core_mhz=1800.0,
    mixed={2: 4.0, 8: 4.0, 16: 3.0},
    objects={256: 4.4, 4096: 4.0},
    read={1: 7.3},
    boundary=3600.0,
)


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


def _timed_pair(objects: int = 4) -> tuple[Flow, list[list[Fraction]]]:
    """Return a producer spending two before each object it writes and a consumer spending three before each it frees."""
    write = [Event(0, True, True, 1), Event(0, True, False, 1)]
    read = [Event(0, False, True, 1), Event(0, False, False, 1)]
    flow = Flow([Channel(0, 1)], [write * objects, read * objects])
    costs = [
        [Fraction(0), Fraction(2)] * objects,
        [Fraction(0), Fraction(3)] * objects,
    ]
    return flow, costs


def test_one_object_deep_the_two_ends_take_turns():
    """One deep, the producer cannot write the next object until the consumer frees the last: five an object, twenty a call."""
    flow, costs = _timed_pair()
    assert flow.period({0: 1}, costs) == 20


def test_two_objects_deep_the_slower_end_sets_the_period():
    """Two deep, the producer works while the consumer does: the consumer's three an object, twelve a call, and no deeper is faster."""
    flow, costs = _timed_pair()
    assert flow.period({0: 2}, costs) == 12
    assert flow.period({0: 4}, costs) == 12


def test_a_deadlocking_depth_has_no_period():
    """A writer acquiring two objects at once on an edge one deep never proceeds."""
    flow = Flow(
        [Channel(0, 1)],
        [
            [Event(0, True, True, 2), Event(0, True, False, 2)],
            [Event(0, False, True, 2), Event(0, False, False, 2)],
        ],
    )
    costs = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]]
    assert flow.period({0: 1}, costs) is None


def test_a_later_phase_starts_once_the_earlier_one_has_finished():
    """A host drain after the producer, then a host fill before the consumer a phase later: the call is the two phases end to end, once.

    The producer writes four objects at two each, drained at one each; the
    fill, a phase later, writes them at one each, read at three each.
    """
    write = [Event(0, True, True, 1), Event(0, True, False, 1)] * 4
    drain = [Event(0, False, True, 1), Event(0, False, False, 1)] * 4
    fill = [Event(1, True, True, 1), Event(1, True, False, 1)] * 4
    read = [Event(1, False, True, 1), Event(1, False, False, 1)] * 4
    flow = Flow(
        [Channel(0, 1), Channel(2, 3, phase=1)],
        [write, drain, fill, read],
        phases=[0, 0, 1, 1],
    )
    costs = [[Fraction(0), Fraction(c)] * 4 for c in (2, 1, 1, 3)]
    assert flow.period({0: 2, 1: 2}, costs) == (2 * 4 + 1) + (1 + 3 * 4)


def test_edges_of_a_later_phase_without_the_actors_phases_are_not_timed():
    flow = Flow([Channel(0, 1, phase=1)], _timed_pair()[0].programs)
    with pytest.raises(NotImplementedError, match="the composer does not group"):
        flow.period({0: 2}, _timed_pair()[1])


def test_each_boundary_a_phased_call_crosses_pays_its_fixed_cost():
    """Three phases, a producer and its reader each: the call is the phases end to end and two boundaries."""
    programs, channels, costs = [], [], []
    for phase, (write_cost, read_cost) in enumerate(((2, 1), (1, 1), (1, 3))):
        channels.append(Channel(2 * phase, 2 * phase + 1, phase=phase))
        programs += [
            [Event(phase, True, True, 1), Event(phase, True, False, 1)] * 4,
            [Event(phase, False, True, 1), Event(phase, False, False, 1)] * 4,
        ]
        costs += [[Fraction(0), Fraction(c)] * 4 for c in (write_cost, read_cost)]
    flow = Flow(channels, programs, phases=[0, 0, 1, 1, 2, 2])
    depths = {0: 2, 1: 2, 2: 2}
    phases_alone = (2 * 4 + 1) + (1 + 1 * 4) + (1 + 3 * 4)
    assert flow.period(depths, costs) == phases_alone
    assert flow.period(depths, costs, boundary=Fraction(5)) == phases_alone + 2 * 5


def test_streams_between_two_measured_counts_move_at_a_rate_between_theirs():
    assert CEILING.rate(1) == pytest.approx(4.0)
    assert CEILING.rate(4) == pytest.approx(4.0)
    assert CEILING.rate(12) == pytest.approx(3.5)


def test_streams_past_the_largest_measured_count_share_its_bandwidth():
    assert CEILING.rate(32) == pytest.approx(1.5)


@pytest.mark.parametrize("boundary", [3600.0, None])
def test_a_ceiling_round_trips_through_what_the_store_keeps(boundary):
    ceiling = dataclasses.replace(CEILING, boundary=boundary)
    assert Ceiling.from_json(ceiling.as_json()) == ceiling


def test_a_ceiling_stored_before_the_boundary_was_measured_keeps_its_rates():
    kept = CEILING.as_json()
    del kept["boundary"]
    assert Ceiling.from_json(kept) == dataclasses.replace(CEILING, boundary=None)
