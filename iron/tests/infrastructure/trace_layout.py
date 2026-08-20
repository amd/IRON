# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Buffer slots for a traced fused sequence. Wrong indices hang the device silently."""

import pytest

from iron.common.compilation import trace_argument_layout


def test_untraced_keeps_the_three_consolidated_buffers_first():
    assert trace_argument_layout({"a": 5}, 0) == ([0, 1, 2], {}, 3)


def test_trace_buffer_lands_at_the_operator_argument_count():
    consolidated, slots, n_args = trace_argument_layout({"a": 5}, 65536)
    assert slots == {"a": 5}
    assert consolidated == [0, 1, 2]
    assert n_args == 6


def test_consolidated_buffers_move_aside_for_a_low_trace_slot():
    # An operator taking two arguments wants slot 2, which the scratch buffer would
    # otherwise hold.
    consolidated, slots, n_args = trace_argument_layout({"a": 2, "b": 4}, 65536)
    assert slots == {"a": 2, "b": 4}
    assert not set(consolidated) & set(slots.values())
    assert consolidated == [0, 1, 3]
    assert n_args == 5


def test_every_operator_gets_its_own_slot():
    _, slots, _ = trace_argument_layout({"a": 3, "b": 4, "c": 5}, 65536)
    assert sorted(slots.values()) == [3, 4, 5]


def test_operators_sharing_an_argument_count_are_refused():
    with pytest.raises(NotImplementedError, match=r"slots \[3\]"):
        trace_argument_layout({"a": 3, "b": 3, "c": 2}, 65536)
