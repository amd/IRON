# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The multi-rate family: single rate, multi-rate ``p : 1``, and rates that cannot balance."""

import pytest

from iron import Precision
from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.graph.record import Recording
from iron.common.graph.sdf import analyze
from iron.common.image.step import Edge
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, search

pytestmark = pytest.mark.usefixtures("npu2")


@unbuilt
def test_single_rate_edge_round_trips():
    """``add -> SiLU -> mul`` at an equal-width edge: the candidate generator proposes it unchanged among its own edits."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul)
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    recording = toys.add_silu_mul_recording("single-rate", add, silu, mul)
    assert any(
        entry in edit.apply(profile).entries()
        for edit in candidates([Timed(recording)], profile, toys.NPU2)
    )


@unbuilt
def test_gemm_tiles_into_rowwise_op_is_a_multi_rate_edge():
    """A GEMM's 64-row tile into a per-row op: repetition ``(1, 64)``, minimum buffer ``64 + 1 - gcd(64, 1) = 64``."""
    gemm, norm = toys.gemm_rowwise(row_tile=64)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    recording = toys.gemm_rowwise_recording("gemm-rows", gemm, norm)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 64}
    assert analysis.min_depth[region.edges[0]] == 64


@unbuilt
def test_limbs_expansion_is_a_real_six_to_one_multi_rate_edge():
    """``Limbs`` writes six bf16 planes a row (``tile_size = 6 * line``) into a plane-sized consumer.

    A real 6 : 1 edge, repetition ``(1, 6)``, minimum buffer
    ``6 + 1 - gcd(6, 1) = 6``.

    No catalogued operator pair gives a clean 2 : 1 pooling or 1 : 2
    upsampling edge (no pooling or upsampling operator exists, and
    ``Resample``/``ResampleTaps`` change row count by a declared
    ``in_size``/``out_size`` ratio as a whole-call anti-aliased resize
    governed by a filter window, not a fixed per-firing streaming rate);
    ``Limbs``' row-to-six-planes expansion is the real multi-rate edge this
    toy builds instead.
    """
    limbs = Limbs(rows=64, line=160, num_aie_columns=1)
    consumer = ElementwiseAdd(
        size=limbs.rows * limbs.line, tile_size=limbs.line, num_aie_columns=1
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
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 6}
    assert analysis.min_depth[edge] == 6


@unbuilt
def test_per_call_bounded_token_count_is_a_valid_kv_length():
    """A GEMM producing a per-call-bounded number of rows (a valid KV length short of ``M``).

    Still balances at the bound: repetition ``(1, 16)`` for a 16-row
    tile (``tile_m = 16``). ``M = 48`` keeps the row split npu2's array
    resolves at one (``M / tile_m`` odd), so the real per-firing count is
    ``tile_m`` alone.
    """
    gemm = GEMM(
        M=48, K=64, N=64, precision=Precision.MEDIUM, num_aie_columns=1, tile_m=16
    ).resolved(toys.NPU2)
    assert gemm.n_aie_rows == 1
    norm = RMSNorm(rows=48, tile_size=64, num_aie_columns=1)
    edge = Edge(0, "C", 1, "x")
    region = Region(
        parts=(
            Member(cls=GEMM, dims={"M": gemm.M, "K": gemm.K, "N": gemm.N}),
            Member(cls=RMSNorm, dims={"rows": norm.rows}),
        ),
        edges=(edge,),
    )
    recording = toys.gemm_rowwise_recording("kv-length", gemm, norm)
    analysis = analyze(region, recording, toys.NPU2)
    assert analysis.consistent
    assert analysis.repetition == {0: 1, 1: 16}


@unbuilt
def test_rates_that_cannot_balance_are_refused_before_any_build():
    """A cycle whose two edges demand incompatible repetition ratios.

    The same toy as the dataflow analysis's inconsistent case, refused by
    ``fit`` at the ``"analysis"`` stage, before any build.
    """
    region, add, mul = toys.mismatched_rate_cycle(add_tile=64, mul_tile=32)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.mismatched_rate_cycle_recording("unbalanced", add, mul)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "analysis"


@unbuilt
def test_buffer_below_the_computed_minimum_is_refused():
    """A multi-rate edge (rate ``16 : 1``, minimum buffer 16) at depth 15 is refused by ``fit`` at stage ``"analysis"``, before any build."""
    gemm, norm = toys.gemm_rowwise(M=16, K=64, N=64, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm, depth=15)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("below-minimum", gemm, norm)
    result = fit(profile, [Timed(recording)], toys.NPU2)
    assert not result.ok
    assert result.stage == "analysis"


@unbuilt
def test_tuner_picks_token_sizes_that_pay():
    """``search``, run on the multi-rate toy alone, keeps a depth at or past the analysis's minimum and passes ``check`` against the start, exact."""
    gemm, norm = toys.gemm_rowwise(M=48, row_tile=16)
    assert gemm.n_aie_rows == 1
    region = toys.gemm_rowwise_region(gemm, norm)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.gemm_rowwise_recording("searched-rates", gemm, norm)
    calls = [Timed(recording)]
    tuned = search(calls, profile, toys.NPU2)
    verdict = check(tuned, profile, calls, toys.NPU2, Refinement.EXACT)
    assert verdict.ok, verdict.why
    tuned_entry = tuned.entries()[0]
    tuned_edge = tuned_entry.root.edges[0]
    analysis = analyze(tuned_entry.root, recording, toys.NPU2)
    assert tuned_edge.depth is not None
    assert tuned_edge.depth >= analysis.min_depth[tuned_edge]
