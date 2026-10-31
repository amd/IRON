# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pricing on-chip fusions: grouping the fusions a tuner's calls admit, and
choosing among them cheapest first. No device below the line.
"""

import getpass
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common.design import OperatorDesign
from iron.common.graph.fusion import candidates
from iron.common.graph.record import Recording
from iron.common.image.step import Edge, Fusion, FusionKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.relu import ReLU
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.graphs import Chain as ChainGraph
from iron.tests.support.graphs import Rotate
from iron.tests.support.llama_model import small
from iron.lm.generation import Sampler
from iron.lm.tune import calls
from iron.operators.mha import MHA
from iron.tune.autotune import Point, Timed, Trial
from iron.tune.fusions import (
    PRICED_KINDS,
    FusionGroup,
    NARROWING_EXHAUSTIVE,
    _bound_points,
    _checkpoint,
    _device_timeout,
    _dominates,
    _fed_widths,
    _gather_table_rows,
    _load_refused,
    _refused_key,
    _save_refused,
    _widths,
    confirm_fusions,
    fusion_groups,
    group_fit_verdict,
    narrow_group,
    narrowings,
    price_fusions,
    select_rewrites,
)
from iron.tune import measure as tune_measure
from iron.tune.measure import (
    Cache,
    Standalone,
    Timing,
    _rewrite_mismatch,
    npu_lock,
    platform,
    repeat_fusion,
    written_steps,
)

pytestmark = pytest.mark.usefixtures("npu2")

LLAMA_NPU2_PROFILE = Profile.load(
    Path(__file__).resolve().parents[2] / "applications/llama/profiles/npu2.json"
)
LLAMA_NPU1_PROFILE = Profile.load(
    Path(__file__).resolve().parents[2] / "applications/llama/profiles/npu1.json"
)

W = np.zeros(2048, bfloat16)


def _fused_graph():
    """A graph recording ``ElementwiseMul(SiLU(x), W)``, fusable at size=2048."""

    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=2048, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=2048, num_aie_columns=1)

    return Fused()


def _group(dev, first: int, rid: int = 0) -> FusionGroup:
    """A ``FusionGroup`` of SiLU -> ElementwiseMul, occurring once starting
    at ``first`` of recording ``rid``: enough for ``select_rewrites``.
    """
    silu = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    mul = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    group = FusionGroup(FusionKind.STREAM, [silu, mul], [(0, "y", 1, "a")])
    group.occurrences = [(rid, first)]
    return group


# ---------------------------------------------------------------------------
# fusion_groups: grouping and weights
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def llama_recordings():
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    C = model.config.prefill_chunk
    decode = Timed(model.record(**decode_shapes), values=dict(position=0, token=0))
    prompt = Timed(
        model.record(**prompt_shapes),
        values=dict(position=C - 1, token=0, start=0, rows=C, rope_start=0),
    )
    return decode, prompt


def test_fusion_groups_merges_identical_shapes_across_llama_layers(llama_recordings):
    decode, prompt = llama_recordings
    dev = aie_utils.ensure_current_device()
    groups = fusion_groups([decode, prompt], dev)

    def silu_group(recording):
        rid = id(recording)
        return next(
            g
            for g in groups
            if g.kind is FusionKind.STREAM
            and len(g.steps) == 2
            and type(g.steps[0]) is SiLU
            and type(g.steps[1]) is ElementwiseMul
            and g.occurrences[0][0] == rid
        )

    def silu_pairs(recording):
        return [
            f
            for f in candidates(recording)
            if len(f.steps) == 2
            and type(recording.steps[f.steps[0]].op.resolved(dev)) is SiLU
            and type(recording.steps[f.steps[1]].op.resolved(dev)) is ElementwiseMul
        ]

    decode_group = silu_group(decode.recording)
    prompt_group = silu_group(prompt.recording)
    assert (
        len(decode_group.occurrences) == len(silu_pairs(decode.recording)) == 2
    )  # per layer
    assert len(prompt_group.occurrences) == len(silu_pairs(prompt.recording)) == 2
    # Every layer shares one identity: its points are not counted per layer.
    assert len(decode_group.points) == 1
    assert len(prompt_group.points) == 1


def test_fusion_groups_merges_repeated_shapes_and_tracks_every_occurrence():
    dev = aie_utils.ensure_current_device()
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    groups = [
        g
        for g in fusion_groups([Timed(recording)], dev)
        if g.kind is FusionKind.STREAM and len(g.steps) == 2
    ]
    assert len(groups) == 3

    add_to_silu = next(g for g in groups if type(g.steps[0]) is ElementwiseAdd)
    assert sorted(p for _, p in add_to_silu.occurrences) == [0, 3]
    assert len(add_to_silu.points) == 1  # both occurrences share one identity

    silu_to_mul = next(g for g in groups if type(g.steps[1]) is ElementwiseMul)
    assert sorted(p for _, p in silu_to_mul.occurrences) == [1]

    mul_to_add = next(g for g in groups if type(g.steps[0]) is ElementwiseMul)
    assert sorted(p for _, p in mul_to_add.occurrences) == [2]


def test_fusion_groups_carries_each_points_weight():
    dev = aie_utils.ensure_current_device()
    recording = _fused_graph().record(x=(2048,))
    calls = [Timed(recording, points=[Point(0.3, {}), Point(0.7, {})])]
    [group] = [
        g
        for g in fusion_groups(calls, dev)
        if g.kind is FusionKind.STREAM and len(g.steps) == 2
    ]
    assert [weight for weight, _ in group.points] == [0.3, 0.7]


def test_op_values_falls_back_to_the_calls_own_value_a_point_does_not_give():
    """A point need not repeat every per-call value the call itself already
    gives: ``n``, which ``RoPE``'s one step binds its rows to, comes from
    ``Timed.values`` alone since neither point moves it, both points
    folding into the one identity it gives.
    """
    dev = aie_utils.ensure_current_device()
    recording = Rotate().record(x=(256, 64), angles=(256, 64))
    call = Timed(recording, values={"n": 128}, points=[Point(0.4, {}), Point(0.6, {})])
    [op] = {s.op for s in recording.steps}
    assert call.op_points(op) == [(1.0, {"valid": 128, "valid_angles": 128})]


# ---------------------------------------------------------------------------
# select_rewrites: cheapest first, never two sharing a step
# ---------------------------------------------------------------------------


def test_select_rewrites_takes_every_non_overlapping_gain():
    dev = aie_utils.ensure_current_device()
    a, b = _group(dev, 0), _group(dev, 4)
    priced = [(a, Trial({}, -10.0, 1.0)), (b, Trial({}, -5.0, 1.0))]
    assert set(select_rewrites(priced, log=lambda _: None)) == {a, b}


def test_select_rewrites_prefers_the_cheaper_of_two_overlapping_gains():
    dev = aie_utils.ensure_current_device()
    costlier, cheaper = _group(dev, 0), _group(dev, 0)
    # The cheaper is priced second: cost, not discovery order, decides.
    priced = [
        (costlier, Trial({}, -5.0, 1.0)),
        (cheaper, Trial({}, -20.0, 1.0)),
    ]
    assert select_rewrites(priced, log=lambda _: None) == [cheaper]


def test_select_rewrites_excludes_a_trial_that_does_not_gain():
    dev = aie_utils.ensure_current_device()
    gains, flat = _group(dev, 0), _group(dev, 4)
    priced = [(gains, Trial({}, -10.0, 1.0)), (flat, Trial({}, 2.0, 1.0))]
    assert select_rewrites(priced, log=lambda _: None) == [gains]


def test_select_rewrites_excludes_a_refused_trial():
    dev = aie_utils.ensure_current_device()
    group = _group(dev, 0)
    priced = [(group, Trial({}, -10.0, 1.0, refused="not bit-identical"))]
    assert select_rewrites(priced, log=lambda _: None) == []


# ---------------------------------------------------------------------------
# measure_fusion: wiring and output comparison kept kind-agnostic, for a
# fan-out's several edges and several host-visible outputs
# ---------------------------------------------------------------------------


def test_repeat_fusion_keeps_edges_for_a_kind_other_than_stream():
    """A staged fan-out's edges stay wired: ``Fusion`` itself refuses any
    only for ``PACK`` and ``MERGE``.
    """
    fusion = repeat_fusion(FusionKind.STAGED, 3, 2, [(0, "y", 1, "a")])
    assert fusion.steps == (3, 4)
    assert fusion.edges == (Edge(3, "y", 4, "a"),)


def test_repeat_fusion_takes_no_edges_for_pack_or_merge():
    fusion = repeat_fusion(FusionKind.PACK, 0, 2, [])
    assert fusion.edges == ()


def test_written_steps_keys_by_step_so_same_named_outputs_do_not_collide():
    dev = aie_utils.ensure_current_device()
    a = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    b = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved(dev)
    run = Standalone("two_silus", [a, b], full_elf=True)
    assert set(written_steps(run)) == {"0.y", "1.y"}


def test_rewrite_mismatch_is_none_when_every_key_matches_bit_for_bit():
    out = {"0.y": np.arange(4, dtype=np.float32)}
    assert _rewrite_mismatch(out, dict(out)) is None


def test_rewrite_mismatch_names_the_differing_key_count_and_max_diff():
    recorded = {"0.y": np.array([1.0, 2.0, 3.0], dtype=np.float32)}
    rewritten = {"0.y": np.array([1.0, 2.0, 3.5], dtype=np.float32)}
    reason = _rewrite_mismatch(recorded, rewritten)
    assert reason is not None
    assert "0.y: 1/3 elements differ, max abs diff 0.5" in reason


def test_rewrite_mismatch_names_missing_and_extra_keys():
    reason = _rewrite_mismatch({"0.y": np.zeros(2)}, {"1.y": np.zeros(2)})
    assert reason == "keys differ: missing ['0.y'], extra ['1.y']"


def test_npu_lock_is_a_noop_unless_told_to_lock():
    """Every existing caller (every test run under ``coord/npu``) passes no
    ``lock``, taking none here at all; only a long sweep run without that
    wrapper passes ``lock=True``, taking the same lock per measurement
    instead.
    """
    with npu_lock():
        pass
    with npu_lock(False):
        pass


def test_npu_lock_nested_reenters_without_a_second_flock(tmp_path):
    """A caller already holding this lock (an outer ``npu_lock(lock=True)``
    spanning a whole measurement's loaded images) enters it again
    (``time_interleaved``'s own, say) without blocking on itself: only the
    outermost entry takes the real flock, over a private file here, not the
    shared ``coord`` one.
    """
    path = tmp_path / "test.lock"
    old_path = tune_measure.NPU_LOCK_PATH
    tune_measure.NPU_LOCK_PATH = path
    try:
        with npu_lock(True):
            assert tune_measure._LOCK_DEPTH == 1
            with npu_lock(True):
                assert tune_measure._LOCK_DEPTH == 2
            assert tune_measure._LOCK_DEPTH == 1
        assert tune_measure._LOCK_DEPTH == 0
    finally:
        tune_measure.NPU_LOCK_PATH = old_path


def test_other_user_on_npu_ignores_a_run_on_npu_under_my_own_name():
    """Parses real ``ps`` output: a ``run_on_npu.py`` under a name that isn't
    mine is someone else on the device; the same process under my own name
    (what ``ps`` reports me spawning it as) is not.
    """
    proc = subprocess.Popen(
        ["python3", "-c", "import time; time.sleep(5)", "run_on_npu.py"]
    )
    try:
        assert tune_measure._other_user_on_npu("a-name-nobody-has") is True
        assert tune_measure._other_user_on_npu(getpass.getuser()) is False
    finally:
        proc.terminate()
        proc.wait()


def test_standalone_refuses_shared_buffers_for_a_fused_edge():
    """Not distinct, a repeat past the first resolves an edge's buffer name
    from another repeat's canonical slot, silently unwiring the feed; a
    pack or a merge takes no edges, so it is spared the refusal below.
    """
    dev = aie_utils.ensure_current_device()
    silu = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    mul = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    fusion = Fusion(FusionKind.STREAM, (0, 1), (Edge(0, "y", 1, "a"),))
    with pytest.raises(ValueError, match="distinct=True"):
        Standalone("x", [silu, mul], distinct=False, fusions=[fusion], full_elf=True)


def test_standalone_allows_shared_buffers_for_a_pack():
    dev = aie_utils.ensure_current_device()
    a = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    b = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved(dev)
    fusion = Fusion(FusionKind.PACK, (0, 1))
    Standalone("x", [a, b], distinct=False, fusions=[fusion], full_elf=True)


# ---------------------------------------------------------------------------
# Joint narrowing: searching the fused form's tunables, and sharing a
# member's shape safely with an occurrence a fusion does not narrow
# ---------------------------------------------------------------------------


def _merge_members(dev, add_cols=None):
    """RMSNorm -> GEMV -> ElementwiseAdd at Llama 1B decode's own shape
    (``rows=1``, ``M=K=2048``): the profile's own widths do not co-reside
    (GEMV and ElementwiseAdd both the whole chip wide); narrowing
    ElementwiseAdd alone lets them.
    """
    rms = LLAMA_NPU2_PROFILE.make(RMSNorm, rows=1, tile_size=2048, weighted=True)
    gemv = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048)
    add = LLAMA_NPU2_PROFILE.make(ElementwiseAdd, size=2048)
    if add_cols is not None:
        add = add._with_tunables(num_aie_columns=add_cols)
    return rms.resolved(dev), gemv.resolved(dev), add.resolved(dev)


def test_widths_orders_widest_first_and_keeps_its_own_setting():
    dev = aie_utils.ensure_current_device()
    gemv = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048)
    found = _widths(gemv, dev)
    cols = [w["num_aie_columns"] for w in found]
    assert cols == sorted(cols, reverse=True)
    own = vars(gemv.resolved(dev))["num_aie_columns"]
    assert any(w["num_aie_columns"] == own for w in found)


def test_fed_widths_only_tries_feed_b_true():
    """A member fed into its ``B`` may only admit the edge at ``feed_b``
    true, a setting its own (unfused, ``feed_b=False``) width never takes;
    ``feed_b=False`` never builds for it, so it is never even tried (a
    large group's exhaustive cap would otherwise crowd the only
    combinations that can work out with ones that never can).
    """
    dev = aie_utils.ensure_current_device()
    gemv = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048)
    found = _fed_widths(gemv, dev)
    assert found and all(w["feed_b"] for w in found)


def test_fed_widths_offers_only_widths_that_resolve_fed(npu1):
    """On npu1 a fed B is one more shim stream: q's own four columns at two
    channels no longer fit, so narrowing never builds them (it raised)."""
    gemv = LLAMA_NPU1_PROFILE.make(GEMV, M=2048, K=2048).resolved(npu1)
    found = _fed_widths(gemv, npu1)
    assert found
    for s in found:
        gemv._with_tunables(**s).resolved(npu1)
    assert vars(gemv)["num_aie_columns"] not in [s["num_aie_columns"] for s in found]


def test_fed_widths_is_plain_widths_without_feed_b():
    dev = aie_utils.ensure_current_device()
    rms = LLAMA_NPU2_PROFILE.make(RMSNorm, rows=1, tile_size=2048, weighted=True)
    assert _fed_widths(rms, dev) == _widths(rms, dev)


def test_dominates_requires_every_member_at_least_as_wide():
    wide = [{"num_aie_columns": 8}, {"num_aie_columns": 4}]
    narrower = [{"num_aie_columns": 4}, {"num_aie_columns": 4}]
    assert _dominates(wide, narrower)
    assert not _dominates(narrower, wide)
    assert not _dominates(wide, wide)


def test_group_fit_verdict_finds_the_merge_that_only_fits_narrowed(tmp_path):
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    kind = FusionKind.MERGE
    assert group_fit_verdict([rms, gemv, add], tmp_path, kind=kind) is not None
    _, _, narrow_add = _merge_members(dev, add_cols=2)
    assert group_fit_verdict([rms, gemv, narrow_add], tmp_path, kind=kind) is None


def test_group_fit_verdict_misses_a_record_keyed_on_recipes_alone(tmp_path):
    """A verdict cached by recipe hash alone, as a key that composed
    nothing and so could not reflect how ``iron.common.image.compose``
    actually built these designs together, is never read: the real key is
    the composed module's own text plus each design's build, which cannot
    collide with a recipe-only one.
    """
    dev = aie_utils.ensure_current_device()
    ops = [
        SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev),
        ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev),
    ]
    designs = [OperatorDesign(op.resolved()) for op in ops]
    recipe_only_key = hashlib.sha256(
        repr(sorted(d.compilable().recipe_hash for d in designs)).encode()
    ).hexdigest()[:24]
    (tmp_path / recipe_only_key).write_text(
        "refused: a verdict from a key that never composed these designs"
    )

    # These two co-reside; a verdict read from the stale record above would
    # wrongly refuse them. The real key is the composed module's own text,
    # which cannot be the recipe-only one above.
    assert group_fit_verdict(ops, tmp_path, kind=FusionKind.MERGE) is None


def test_group_fit_verdict_caches_a_different_record_for_a_different_kind(tmp_path):
    """The module ``fits`` composes differs by kind even over the same
    designs (a pack gives each member its own array, fuse=True; a merge
    shares one by identity), so each kind gets its own cache record, never
    reusing the other's verdict.
    """
    dev = aie_utils.ensure_current_device()
    a = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    b = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    group_fit_verdict([a, b], tmp_path, kind=FusionKind.PACK)
    group_fit_verdict([a, b], tmp_path, kind=FusionKind.MERGE)
    assert len(list(tmp_path.iterdir())) == 2


def test_narrowings_tries_every_combination_for_a_fan_out_not_just_the_widest():
    """A fan-out's all-widest combination dominates every other
    (``_dominates``) but, with no feasibility check behind it
    (``group_fit_verdict`` does not model a feed's shared buffer), that
    gives dominance nothing to prune on: pruning it anyway would collapse
    the search to that one combination alone, which rarely co-resides,
    and never discover a narrower one (q/k/v at (8,4,2) columns, say) that
    does.
    """
    dev = aie_utils.ensure_current_device()
    rms = LLAMA_NPU2_PROFILE.make(RMSNorm, rows=1, tile_size=2048, weighted=True)
    q = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048, num_batches=1, num_matrices=1)
    k = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048, num_batches=1, num_matrices=1)
    v = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048, num_batches=1, num_matrices=1)
    group = FusionGroup(
        FusionKind.STAGED,
        [rms.resolved(dev), q.resolved(dev), k.resolved(dev), v.resolved(dev)],
        [(0, "y", 1, "B"), (0, "y", 2, "B"), (0, "y", 3, "B")],
    )
    combos = narrowings(group, dev)
    found = [tuple(s.get("num_aie_columns") for s in c) for c in combos]
    assert len(found) > 1
    assert (1, 8, 4, 2) in found
    assert all(s["feed_b"] for c in combos for s in c[1:])


def test_narrowings_narrows_only_the_member_that_needs_it(tmp_path):
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    group = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    combos = narrowings(group, dev, fit_cache=tmp_path)
    assert combos, "expected at least one combination that co-resides"
    cols = [s.get("num_aie_columns") for s in combos[0]]
    assert cols[1] == vars(gemv)["num_aie_columns"]  # GEMV never narrows
    assert cols[2] < vars(add)["num_aie_columns"]  # ElementwiseAdd does


def test_a_fusion_entry_names_no_dimension_a_host_sizes():
    """A host fits its own context, which sizes the decode step's KV cache
    and so MHA and the cache copies: a fusion entry found at one context
    names none of those dimensions, so the model fitted to another fuses
    the same steps."""
    dev = aie_utils.ensure_current_device()
    model, sibling = small(), small(max_seq_len=512)
    [decode] = calls(
        model, 0, 0, 256, 1, Sampler(0.7, 50), sibling, versions=["decode"]
    )
    named = [
        dims
        for g in fusion_groups([decode], dev)
        for cls, dims, _ in g.dims()
        if cls is MHA
    ]
    assert named and not any("kv_len" in dims for dims in named)


def test_group_dims_carries_the_narrowed_combos_tunables():
    """``FusionGroup.dims(combo)`` names each step's tunables for
    ``Profile.add_fusion``, so a member narrowed to co-reside takes that
    setting only inside this fusion, not wherever its shape runs unfused.
    """
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    group = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    combo = ({}, {}, {"num_aie_columns": 2})
    dims = group.dims(combo)
    assert [t for _, _, t in dims] == list(combo)
    assert group.dims(None) == [(cls, d, None) for cls, d, _ in dims]


# ---------------------------------------------------------------------------
# price_fusions: the profile it returns
# ---------------------------------------------------------------------------


def test_price_fusions_with_no_candidates_keeps_tunables_and_fusion_entries():
    dev = aie_utils.ensure_current_device()
    profile = Profile()
    profile.add(SiLU, num_aie_columns=1)
    profile.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=4096)), (ElementwiseMul, dict(size=4096))],
        [(0, "y", 1, "a")],
    )
    out = price_fusions([], dev, profile, full_elf=True, log=lambda _: None)
    assert out.tunables_for(SiLU, {}) == {"num_aie_columns": 1}
    gate = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    assert out.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])


@pytest.mark.parametrize("full_elf", [True, False])
def test_price_fusions_prices_merges_only_on_an_xclbin_per_step(npu1, full_elf):
    """On an xclbin per step nothing packs, so a merge, consecutive steps as
    one dispatch, is priced there; a full ELF leaves it to packings."""
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    calls = [Timed(recording)]
    every = len(fusion_groups(calls, npu1, tuple(FusionKind)))
    assert every > len(fusion_groups(calls, npu1, PRICED_KINDS))
    expected = every if not full_elf else len(fusion_groups(calls, npu1, PRICED_KINDS))
    logs: list[str] = []
    out = price_fusions(calls, npu1, full_elf=full_elf, max_price=0, log=logs.append)
    assert out is None
    assert f"{expected} group(s) left unpriced this batch" in logs[-1]


# ---------------------------------------------------------------------------
# A device command timeout refuses a group outright, never retried; and
# price_fusions checkpoints its decisions so far as it goes
# ---------------------------------------------------------------------------


def test_device_timeout_recognizes_the_drivers_own_error():
    hung = RuntimeError(
        "fuse_rewritten1: the run ended in ert_cmd_state.ERT_CMD_STATE_TIMEOUT"
    )
    assert _device_timeout(hung)


def test_device_timeout_is_false_for_an_ordinary_build_failure():
    assert not _device_timeout(ValueError("GEMV: B is fed 1 lane(s), but ..."))
    assert not _device_timeout(
        RuntimeError("[aiecc] Compilation failed with exit code 1")
    )


def test_checkpoint_writes_the_fusions_taken_so_far(tmp_path):
    dev = aie_utils.ensure_current_device()
    gaining, flat = _group(dev, 0), _group(dev, 4)
    priced = [(gaining, Trial({}, -10.0, 1.0)), (flat, Trial({}, 2.0, 1.0))]
    checkpoint = tmp_path / "profile.progress.json"
    _checkpoint(None, priced, {gaining: None, flat: None}, checkpoint)

    loaded = Profile.load(checkpoint)
    silu = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    mul = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    assert loaded.fused(FusionKind.STREAM, [silu, mul], [(0, "y", 1, "a")])


def test_checkpoint_overwrites_the_previous_one_atomically(tmp_path):
    dev = aie_utils.ensure_current_device()
    gaining = _group(dev, 0)
    checkpoint = tmp_path / "profile.progress.json"
    _checkpoint(None, [], {}, checkpoint)
    assert Profile.load(checkpoint).fusions() == []

    _checkpoint(None, [(gaining, Trial({}, -10.0, 1.0))], {gaining: None}, checkpoint)
    assert len(Profile.load(checkpoint).fusions()) == 1
    # Only the final, whole file is ever on disk at that name: no partial
    # left behind beside it.
    assert list(tmp_path.iterdir()) == [checkpoint]


def test_refused_round_trips_through_its_file_atomically(tmp_path):
    dev = aie_utils.ensure_current_device()
    group = _group(dev, 0)
    path = tmp_path / "profile.progress.refused.json"
    assert _load_refused(path) == {}

    _save_refused({_refused_key(group): "hung on the device: ..."}, path)
    loaded = _load_refused(path)
    assert loaded == {_refused_key(group): "hung on the device: ..."}
    # Only the final, whole file is ever on disk at that name.
    assert list(tmp_path.iterdir()) == [path]


def test_price_fusions_skips_a_group_already_refused_as_hung(tmp_path):
    """A group a prior call's device timeout refused is never retried: its
    key, persisted beside the checkpoint, is loaded back and the group
    dropped before ``narrow_group`` (and so the device) ever sees it again.
    Every group the graph admits is pre-refused, so ``narrow_group`` is
    never called at all here: device-free by construction, not by luck.
    """
    dev = aie_utils.ensure_current_device()
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    calls = [Timed(recording)]
    groups = fusion_groups(calls, dev, PRICED_KINDS)
    assert groups

    checkpoint = tmp_path / "profile.progress.json"
    refused_path = checkpoint.with_suffix(".refused.json")
    refused_path.write_text(
        json.dumps(
            {
                _refused_key(g): "hung on the device: ERT_CMD_STATE_TIMEOUT"
                for g in groups
            }
        )
    )

    logs: list[str] = []
    profile = price_fusions(
        calls,
        dev,
        full_elf=True,
        checkpoint=checkpoint,
        confirm=False,
        log=logs.append,
    )
    assert profile is not None
    assert profile.fusions() == []
    assert len([line for line in logs if "skipped, refused earlier" in line]) == len(
        groups
    )
    assert not any(" us" in line for line in logs)  # narrow_group's own price line


# ---------------------------------------------------------------------------
# On the device: a gaining fusion is written and runs bit-identically.
# ---------------------------------------------------------------------------

FUSION_SIZE, FUSION_TILE, FUSION_COLS = 2**22, 4096, 8
W_BIG = np.zeros(FUSION_SIZE, bfloat16)


def _big_fused_graph():
    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS)
            return ElementwiseMul.step(
                gate, W_BIG, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS
            )

    return Fused()


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_max_price_prices_a_batch_then_stops_until_every_group_is_priced(tmp_path):
    """A caller holding the device lock for one call, not a whole sweep,
    calls again for the rest: ``max_price`` below the groups found returns
    None without selecting, confirming or saving; at or above it, the
    profile.
    """
    dev = aie_utils.ensure_current_device()
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    calls = [Timed(recording)]
    n = len(fusion_groups(calls, dev))
    assert n > 1
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    kwargs = dict(
        full_elf=True, timing=Timing(rounds=2, calls=5), cache=cache, log=lambda _: None
    )
    assert price_fusions(calls, dev, max_price=1, **kwargs) is None
    assert price_fusions(calls, dev, max_price=n, **kwargs) is not None


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_pricing_a_gaining_fusion_writes_an_entry_that_runs_bit_identically(tmp_path):
    recording = _big_fused_graph().record(x=(FUSION_SIZE,))
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_fusions(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        log=lambda _: None,
    )
    gate = SiLU(
        size=FUSION_SIZE, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS
    ).resolved()
    up = ElementwiseMul(
        size=FUSION_SIZE, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS
    ).resolved()
    assert profile.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])

    fused_graph = _big_fused_graph()
    fused_graph.profile = profile
    fused = fused_graph.compile(full_elf=True, x=(FUSION_SIZE,))
    plain = _big_fused_graph().compile(full_elf=True, x=(FUSION_SIZE,))

    rng = np.random.default_rng(0)
    x = (rng.random(FUSION_SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(x).numpy()[:FUSION_SIZE])
    got = np.array(fused(x).numpy()[:FUSION_SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


# ---------------------------------------------------------------------------
# On the device: the fixed frame against an independent in-image measurement.
# ---------------------------------------------------------------------------

_END_TO_END = re.compile(r"([-+]\d+\.\d+) ± (\?|\d+\.\d+) us end to end")


def test_confirm_fusions_drops_the_worst_group_on_a_build_failure(llama_recordings):
    """A version (this particular combination of active groups' fusions)
    that fails to BUILD is a real aiecc compile error, device-free to hit:
    decode's GEMV -> ElementwiseAdd -> RMSNorm merge, every member at its
    own (unnarrowed) width, does not place (confirmed by this same failure
    in the real sweep that crashed it). This must drop the one candidate
    and return no fusion taken, not crash the whole sweep.
    """
    decode, _ = llama_recordings
    dev = aie_utils.ensure_current_device()
    group = next(
        g
        for g in fusion_groups([decode], dev)
        if g.kind is FusionKind.MERGE
        and [type(s).__name__ for s in g.steps] == ["GEMV", "ElementwiseAdd", "RMSNorm"]
    )
    logged = []
    taken = confirm_fusions(
        [decode],
        dev,
        [group],
        {group: Trial({}, -1e6, 1.0)},
        Profile(),
        {group: None},  # no narrowing: its own (recorded, non-co-resident) width
        full_elf=True,
        log=logged.append,
    )
    assert taken == []
    assert any("does not build fused" in line for line in logged)


class BoundedReLUs(iron.Graph):
    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(ReLU.step(x[:n], num_aie_columns=4), num_aie_columns=4)


@pytest.mark.supported_devices("npu2")
def test_confirm_fusions_holds_a_narrowed_merge_bit_identical_at_partial_bounds():
    """A merge narrowing two bounded ReLUs, confirmed against them unfused
    at the full bound and at half of it: a narrowed design whose per-call
    values went unwritten agrees at the full bound but not at half.
    """
    dev = aie_utils.ensure_current_device()
    call = Timed(BoundedReLUs().record(x=(4096,)), values=dict(n=4096))
    assert _bound_points(call.recording, call.values) == [dict(n=2048)]
    [group] = fusion_groups([call], dev, kinds=(FusionKind.MERGE,))
    logged = []
    confirm_fusions(
        [call],
        dev,
        [group],
        {group: Trial({}, -1e6, 1.0)},
        Profile(),
        {group: ({"num_aie_columns": 2}, {"num_aie_columns": 2})},
        full_elf=True,
        timing=Timing(rounds=1, calls=2),
        log=logged.append,
    )
    assert any("end to end" in line for line in logged)


def test_bound_points_confirm_a_prompt_chunk_at_partial_rows(llama_recordings):
    """A full chunk runs every bound at its largest, where a design reading
    its rows wrongly still agrees: confirmation also runs each bound
    halved, a partial chunk among them, each within the recording's limits
    and each a call its operators take: a full chunk's rows ending at half
    the position would be queries past their keys, which MHA refuses.
    """
    _, prompt = llama_recordings
    recording, values = prompt.recording, prompt.values
    points = _bound_points(recording, values)
    assert {**values, "rows": values["rows"] // 2} in points
    assert {**values, "position": values["position"] // 2} not in points
    assert dict(values) not in points
    for point in points:
        recording.check_limits(point)


def test_gather_table_rows_names_an_input_roles_ids_handle(llama_recordings):
    """The prompt chunk's embedding reads its ``ids`` input through a
    ``Gather``; its table row count is what ``confirm_fusions`` draws
    random ids within, not raw bytes (which range over the whole dtype,
    past any real vocabulary, and ``Gather.control_words`` refuses them).
    """
    _, prompt = llama_recordings
    recording = prompt.recording
    table_rows = _gather_table_rows(recording)
    [ids] = [h for h in recording.inputs if h.role == "input"]
    assert table_rows == {ids.name: 1024}

    gather = next(s for s in recording.steps if s.gather is not None)
    rng = np.random.default_rng(0)
    bounded = rng.integers(0, table_rows[ids.name], ids.shape).astype(ids.dtype)
    gather.op.control_words(bounded, address=0)  # must not raise

    raw = rng.integers(0, 2**31, ids.shape, dtype=np.int64).astype(ids.dtype)
    with pytest.raises(IndexError, match="gathering"):
        gather.op.control_words(raw, address=0)


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_fixed_frame_agrees_with_decode_groups_priced_in_the_whole_step(
    llama_recordings, tmp_path
):
    """Each of decode's own 2-step fusion groups (SiLU -> ElementwiseMul,
    both residual adds' GEMV -> ElementwiseAdd, and RMSNorm -> GEMV, whose
    vector input streams only with ``feed_b`` forced true), ``narrow_group``'s
    standalone price against an independent figure for the same shape: timed
    compiled into the whole decode step against the same step unfused
    (``confirm_fusions``, whose own log line carries it, given the same
    narrowing ``narrow_group`` found) and divided by its occurrences (2 per
    group, one per layer, down Llama's small shape).

    The band is each side's own standard error, summed in quadrature (the
    two are independent interleaved timings of one shape) and multiplied by
    3, not the 2 standard errors ``Trial.gains`` takes elsewhere, floored at
    half the bug's own size (~165 us, one reconfigure): GEMV -> Add's
    standalone price and its in-image one agree only to 10-30 us (its own
    placement is not pinned, so a probe alone and one among decode's other
    designs need not place it alike), well inside a regression back to the
    old frame's bias but outside 3 standard errors most rounds. This runs
    beside other agents' own NPU runs too, whose jitter this test's own
    rounds do not sample.
    """
    decode, _ = llama_recordings
    dev = aie_utils.ensure_current_device()
    groups = [
        g
        for g in fusion_groups([decode], dev)
        if g.kind is FusionKind.STREAM and len(g.steps) == 2
    ]
    assert len(groups) >= 2, "expected at least SiLU -> Mul and a GEMV -> Add shape"

    timing = Timing(rounds=8, calls=10)
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    # decode's own Timed, for pricing alone, gives no per-call values; a
    # decode step CompiledGraph dispatches, so needs one.
    dispatched = Timed(decode.recording, values=dict(position=0, token=0))

    for group in groups:
        trial, combo = narrow_group(
            group,
            dev,
            full_elf=True,
            timing=timing,
            cache=cache,
            fit_cache=tmp_path / "fits",
            log=lambda _: None,
        )
        assert trial.refused is None and trial.noise_us is not None

        logged = []
        confirm_fusions(
            [dispatched],
            dev,
            [group],
            {group: Trial({}, -1e6, 1.0)},  # the only candidate: its figure unread
            Profile(),
            {group: combo},  # its own setting where it builds so, else narrow_group's
            full_elf=True,
            timing=timing,
            log=logged.append,
        )
        [line] = [m for m in logged if "end to end" in m]
        delta_s, noise_s = _END_TO_END.search(line).groups()
        occurrences = len(group.occurrences)
        in_image = float(delta_s) / occurrences
        in_image_noise = float(noise_s) / occurrences

        band = max(3 * math.hypot(trial.noise_us, in_image_noise), 80.0)
        assert abs(trial.delta_us - in_image) < band, (
            f"{group}: standalone {trial.delta_us:+.1f} us vs in-image "
            f"{in_image:+.1f} us, band {band:.1f} us"
        )


# ---------------------------------------------------------------------------
# On the device: a pack that already co-resides, and a merge that only
# fits its members narrowed.
# ---------------------------------------------------------------------------


def _qkv_recording(dev):
    """Llama decode's q/k/v GEMVs (M=2048/512/512, K=2048), independent:
    co-reside at the profile's own width, so packing them needs no
    narrowing.
    """
    q = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048).resolved(dev)
    k = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    v = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    steps = sequences.steps(
        (q, "Aq", "x", "oq"), (k, "Ak", "x", "ok"), (v, "Av", "x", "ov")
    )
    return Recording.of_steps("qkv", steps, ["Aq", "Ak", "Av", "x"], ["oq", "ok", "ov"])


def _short_decode_recording(dev):
    rms, gemv, add = _merge_members(dev)
    steps = sequences.steps(
        (rms, "x", "w", "n"), (gemv, "A", "n", "c"), (add, "r", "c", "out")
    )
    return Recording.of_steps("short_decode", steps, ["x", "w", "A", "r"], ["out"])


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_narrow_group_narrows_the_qkv_pack_to_fit(tmp_path):
    """q, k and v each resolve to 8 columns alone, one output DMA channel a
    column; three such streams want 24 of npu2's 16, so the pack never
    co-resides at the profile's own width (``group_fit_verdict`` composes
    the real fused module, each member its own array, since
    ``d9a96bf8``'s fix: the earlier, unfused check shared the three by
    identity and missed this). ``narrow_group`` finds the Pareto-maximal
    combination that does co-reside instead.
    """
    dev = aie_utils.ensure_current_device()
    q = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048).resolved(dev)
    k = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    v = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    group = FusionGroup(FusionKind.PACK, [q, k, v], [])
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    trial, combo = narrow_group(
        group,
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        fit_cache=tmp_path / "fits",
        log=lambda _: None,
    )
    assert trial.refused is None
    assert combo is not None, "q/k/v at 8/8/8 columns want 24 output channels of 16"
    assert [s["num_aie_columns"] for s in combo] == [8, 4, 4]


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_price_fusions_takes_the_qkv_pack_without_confirming_end_to_end(tmp_path):
    """Three GEMVs alone, with no other step around them to amortize a
    configure the way Llama's own decode step's other designs do, do not
    gain from packing end to end (``confirm_fusions`` correctly drops this
    isolated recording's pack, as it should); ``confirm=False`` checks only
    that ``price_fusions`` finds and takes a pack on its own standalone
    price. ``candidates`` proposes every sub-window too (q&k, k&v), each a
    step cheaper than the full triple might overlap and take instead
    (``select_rewrites``); any of them, narrowed or not, is this test's own.
    """
    dev = aie_utils.ensure_current_device()
    recording = _qkv_recording(dev)
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_fusions(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=4, calls=10),
        cache=cache,
        fit_cache=tmp_path / "fits",
        confirm=False,
        log=lambda _: None,
    )
    kinds = [kind for kind, _, _, _ in profile.fusions()]
    assert kinds == [FusionKind.PACK]


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_narrow_group_prices_the_merge_that_only_fits_narrowed(tmp_path):
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    group = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    trial, combo = narrow_group(
        group,
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        fit_cache=tmp_path / "fits",
        log=lambda _: None,
    )
    assert combo is not None, "the profile's own width should not co-reside"
    assert combo[1]["num_aie_columns"] == vars(gemv)["num_aie_columns"]
    assert combo[2]["num_aie_columns"] < vars(add)["num_aie_columns"]
    assert trial.refused is None


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_price_fusions_takes_the_cheaper_of_two_overlapping_fusions(tmp_path):
    """RMSNorm -> GEMV -> ElementwiseAdd admits a GEMV -> ElementwiseAdd
    stream, an RMSNorm -> GEMV merge, and, since ``candidates`` also proposes
    an edge into an input that streams only with a reader's bool tunable
    flipped (``iron.common.graph.fusion``, GEMV's ``B`` under ``feed_b``),
    the whole chain as one RMSNorm -> GEMV -> ElementwiseAdd stream too, all
    three overlapping at GEMV. The whole-chain stream prices cheapest (one
    reconfigure instead of two), so ``select_rewrites`` takes it and skips
    both the plain stream and the merge, each only a part of what it already
    claims (``confirm_fusions`` would raise were it not bit-identical to the
    same steps unfused).
    """
    dev = aie_utils.ensure_current_device()
    recording = _short_decode_recording(dev)
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_fusions(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        fit_cache=tmp_path / "fits",
        kinds=tuple(FusionKind),
        log=lambda _: None,
    )
    rms, gemv, add = _merge_members(dev)
    assert profile.fused(
        FusionKind.STREAM, [rms, gemv, add], [(0, "y", 1, "B"), (1, "C", 2, "b")]
    )
    assert not profile.fused(FusionKind.MERGE, [rms, gemv], ())
    assert not profile.fused(FusionKind.STREAM, [gemv, add], [(0, "C", 1, "b")])
