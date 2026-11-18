# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A composition entry matched onto a recording's steps."""

import pytest

from iron.common.declare.composition import Entry, Inflow, Member, Region, Scope
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.fusable import gemv_silu_mul

M = 256

pytestmark = pytest.mark.usefixtures("npu2")


def _two_layers() -> Recording:
    """Return GEMV -> SiLU -> Mul twice over, the second layer reading the first's output."""
    gemv, silu, mul = gemv_silu_mul(M=M, cols=1, tile=64)
    steps = sequences.steps(
        (gemv, "A0", "x", "c0"),
        (silu, "c0", "s0"),
        (mul, "s0", "up0", "h"),
        (gemv, "A1", "h", "c1"),
        (silu, "c1", "s1"),
        (mul, "s1", "up1", "out"),
    )
    return Recording.of_steps(
        "two_layers", steps, ["A0", "x", "up0", "A1", "up1"], ["out"]
    )


def _chain() -> Region:
    return Region(
        (
            Member(GEMV, {"M": M, "K": M}),
            Member(SiLU, {"size": M}),
            Member(ElementwiseMul, {"size": M}),
        ),
        (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "a")),
    )


def test_a_region_matches_each_run_of_its_steps_and_wiring():
    assert _two_layers().occurrences(Entry(_chain())) == ((0, 1, 2), (3, 4, 5))


def test_a_scope_keeps_the_runs_it_names():
    recording = _two_layers()
    assert recording.occurrences(Entry(_chain(), Scope(occurrences=(1,)))) == (
        (3, 4, 5),
    )
    other = ((("x", (1,), "bfloat16"),),)
    assert (
        recording.occurrences(Entry(_chain(), Scope(versions=frozenset(other)))) == ()
    )


def test_an_edge_the_recording_does_not_wire_matches_nothing():
    region = Region(_chain().parts, (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "b")))
    assert _two_layers().occurrences(Entry(region)) == ()


def test_a_dim_the_recording_does_not_have_matches_nothing():
    region = Region(
        (Member(GEMV, {"M": 2 * M, "K": M}),) + _chain().parts[1:], _chain().edges
    )
    assert _two_layers().occurrences(Entry(region)) == ()


def test_one_step_matches_every_step_of_its_shape():
    assert _two_layers().occurrences(Entry(Member(GEMV, {"M": M, "K": M}))) == (
        (0,),
        (3,),
    )


def test_an_edge_joins_steps_of_different_nested_regions():
    gemv, silu, mul = _chain().parts
    layer_end = Region((gemv, silu, mul), (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "a")))
    next_start = Region((Member(GEMV, {"M": M, "K": M}),))
    outer = Region((layer_end, next_start), (Edge(2, "y", 3, "B"),))
    assert _two_layers().occurrences(Entry(outer)) == ((0, 1, 2, 3),)


def test_inflows_name_the_one_buffer_their_steps_share():
    gemv = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=64)
    steps = sequences.steps((gemv, "w", "x0", "y0"), (gemv, "w", "x1", "y1"))
    recording = Recording.of_steps(
        "shared_weight", steps, ["w", "x0", "x1"], ["y0", "y1"]
    )
    pair = (Member(GEMV, {"M": M, "K": M}), Member(GEMV, {"M": M, "K": M}))
    shared = Region(pair, inflows=(Inflow("w", 0, "A"), Inflow("w", 1, "A")))
    assert recording.occurrences(Entry(shared)) == ((0, 1),)
    elsewhere = Region(pair, inflows=(Inflow("v", 0, "A"), Inflow("v", 1, "A")))
    assert recording.occurrences(Entry(elsewhere)) == ()


def test_an_edge_naming_an_operand_its_step_lacks_is_refused():
    region = Region(_chain().parts, (Edge(0, "C", 1, "z"),))
    with pytest.raises(ValueError, match="no operand 'z'"):
        _two_layers().occurrences(Entry(region))
