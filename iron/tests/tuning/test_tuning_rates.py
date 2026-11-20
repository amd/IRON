# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The multi-rate family: single rate, multi-rate ``p : 1``, and rates that cannot balance."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.graph.sdf import analyze
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.limbs import Limbs
from iron.tests.support import sequences
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

pytestmark = pytest.mark.usefixtures("device")


def test_single_rate_edge_round_trips(device):
    """``add -> SiLU -> mul`` at an equal-width edge: the candidate generator proposes it unchanged among its own edits."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul)
    entry = Entry(root=region)
    recording = toys.add_silu_mul_recording("single-rate", add, silu, mul)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


def test_gemm_tiles_into_rowwise_op_is_a_multi_rate_edge(device):
    """A GEMM's 64-row tile into a per-row op: one object a call into 64, and one object of buffer.

    The tile is the GEMM's whole 64-row output, so its lane moves one object
    a call; the memtile that restages it into the norm's rows takes that one
    object a round, so the producer's side of the edge holds one, not the
    ``64 + 1 - gcd(64, 1)`` rows a shared row-by-row buffer would.
    """
    gemm, norm = toys.gemm_rowwise(device, row_tile=64)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    recording = toys.gemm_rowwise_recording("gemm-rows", gemm, norm)
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 64}
    assert analysis.min_depth[region.edges[0]] == 1


def test_limbs_expansion_is_a_real_six_to_one_multi_rate_edge(device):
    """``Limbs`` writes six bf16 planes a row into a plane-sized consumer: one object a firing into six.

    ``Limbs`` fires once a row and writes one object of six planes; the
    consumer reads one plane an object, so it fires six times a ``Limbs``
    firing over the same 61,440 elements. A memtile re-chunks each six-plane
    object into planes, so the producer's side holds one object.
    """
    limbs = Limbs(rows=64, line=160, num_aie_columns=1)
    planes = 6 * limbs.rows
    consumer = ElementwiseAdd(
        size=planes * limbs.line, tile_size=limbs.line, num_aie_columns=1
    )
    edge = Edge(0, "y", 1, "a")
    region = Region(
        parts=(
            Member(cls=Limbs, dims={"rows": limbs.rows, "line": limbs.line}),
            Member(cls=ElementwiseAdd, dims={"size": consumer.size}),
        ),
        edges=(edge,),
    )
    steps = sequences.steps((limbs, "x", "mid"), (consumer, "mid", "w", "out"))
    recording = Recording.of_steps("limbs-expansion", steps, ["x", "w"], ["out"])
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert analysis.repetition == {0: limbs.rows, 1: planes}
    assert analysis.tokens[edge] == ((1,), (1,))
    assert analysis.min_depth[edge] == 1


@unbuilt
def test_per_call_bounded_token_count_is_a_valid_kv_length(device):
    """A GEMM over the first ``n`` of 48 rows (a valid KV length short of ``M``), each row then normalized.

    At ``n = 16`` with a 16-row tile, a call fires the GEMM once and the
    norm 16 times: the analysis is held to the call's own values, not the
    48 rows recorded.
    """
    recording = toys.BoundedRows(tile_m=16).record(a=(48, 64), b=(64, 64))
    region = Region(
        tuple(
            Member(cls=type(s.op), dims=Profile.dims(type(s.op), vars(s.op)))
            for s in recording.steps
        ),
        (Edge(0, "C", 1, "x"),),
    )
    analysis = analyze(region, recording, device)
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 16}


@unbuilt
def test_buffer_below_the_computed_minimum_is_refused(device):
    """A multi-rate edge (rate ``16 : 1``, minimum buffer 16) at depth 15 is refused by ``fit`` at stage ``"analysis"``, before any build."""
    gemm, norm = toys.gemm_rowwise(device, M=16, K=64, N=64, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm, depth=15)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("below-minimum", gemm, norm)
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"


@pytest.mark.extensive
@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_picks_token_sizes_that_pay(device):
    """``search``, run on the multi-rate toy alone, keeps a depth at or past the analysis's minimum and passes ``check`` against the start, exact."""
    gemm, norm = toys.gemm_rowwise(device, M=48, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("searched-rates", gemm, norm)
    calls = [Timed(recording)]
    tuned = search(calls, profile, device)
    verdict = check(tuned, profile, calls, device, Refinement.EXACT)
    assert verdict.ok, verdict.why
    tuned_entry = tuned.entries()[0]
    tuned_edge = tuned_entry.root.edges[0]
    analysis = analyze(tuned_entry.root, recording, device)
    assert tuned_edge.depth is not None
    assert tuned_edge.depth >= analysis.min_depth[tuned_edge]
