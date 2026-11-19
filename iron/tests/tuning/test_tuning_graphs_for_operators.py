# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA and AXPY as graphs of IRON's existing operators, over the composition contract."""

from __future__ import annotations

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron import Precision
from iron.common.declare.composition import (
    Edge as CompositionEdge,
)
from iron.common.declare.composition import (
    Entry,
    Member,
    Refinement,
    Region,
)
from iron.common.declare.profile import Profile
from iron.common.graph.sdf import analyze
from iron.common.image.step import EdgeKind
from iron.operators import GEMM, GEMV, ElementwiseAdd, ElementwiseMul, Softmax
from iron.tests.support import toys_composition as toys
from iron.tests.support.tuning import unbuilt, waits_on_a_kernel
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, measure, search

pytestmark = pytest.mark.usefixtures("npu2")

KV_LEN, HEAD_DIM, ROWS = 128, 64, 32
SEQ = 32

# Llama 3.2 1B's shipped decode and prefill mapping, at their own sizes (no padding to a
# toy size): decode packs its 32 query heads into rows, prefill chunks 128 queries over
# its 2048-token context.
LLAMA1B_DECODE = dict(heads=32, head_dim=64, kv_len=2048)
LLAMA1B_PREFILL = dict(seq=128, head_dim=64, kv_len=2048)


def _decode_region(
    kv_len: int = KV_LEN, head_dim: int = HEAD_DIM, rows: int = ROWS
) -> Region:
    return Region(
        parts=(
            Member(GEMV, dict(M=kv_len, K=head_dim, output_dtype=np.float32)),
            Member(Softmax, dict(rows=rows, cols=kv_len, input_dtype=np.float32)),
            Member(GEMV, dict(M=head_dim, K=kv_len)),
        ),
        edges=(
            CompositionEdge(0, "C", 1, "x"),
            CompositionEdge(1, "y", 2, "B"),
        ),
    )


def _prefill_region(
    seq: int = SEQ,
    kv_len: int = KV_LEN,
    head_dim: int = HEAD_DIM,
    scores_dtype: type | None = None,
) -> Region:
    qk_dims = dict(M=seq, K=head_dim, N=kv_len)
    if scores_dtype is not None:
        qk_dims = {**qk_dims, "output_dtype": scores_dtype}
    return Region(
        parts=(
            Member(GEMM, qk_dims),
            Member(ElementwiseAdd, dict(size=seq * kv_len)),
            Member(Softmax, dict(rows=seq, cols=kv_len)),
            Member(GEMM, dict(M=seq, K=kv_len, N=head_dim)),
        ),
        # The scores' tiles reach the mask in rows (a ratio), and the
        # softmax's rows join into the GEMM's tiles: both through a memtile.
        edges=(
            CompositionEdge(0, "C", 1, "a", kind=EdgeKind.STAGED),
            CompositionEdge(1, "y", 2, "x"),
            CompositionEdge(2, "y", 3, "A", kind=EdgeKind.STAGED),
        ),
    )


def _axpy_region() -> Region:
    return Region(
        parts=(
            Member(ElementwiseMul, dict(size=2048)),
            Member(ElementwiseAdd, dict(size=2048)),
        ),
        # ElementwiseMul's y has no dtype parameter (always bf16): AXPY's
        # a*x hand-off cannot be named float32, a gap this graph reports
        # rather than works around.
        edges=(CompositionEdge(0, "y", 1, "a"),),
    )


@unbuilt
def test_the_decode_graph_round_trips_as_an_entry_and_is_proposed(tmp_path, npu2):
    region = _decode_region()
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    qk, softmax, pv = toys.decode_attention_ops(KV_LEN, HEAD_DIM, ROWS)
    recording = toys.decode_attention_recording("decode", qk, softmax, pv)
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
def test_the_prefill_graph_round_trips_as_an_entry_and_is_proposed(tmp_path, npu2):
    region = _prefill_region()
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    qk, add_mask, softmax, pv = toys.prefill_attention_ops(SEQ, KV_LEN, HEAD_DIM)
    recording = toys.prefill_attention_recording("prefill", qk, add_mask, softmax, pv)
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
def test_the_axpy_graph_round_trips_as_an_entry_and_is_proposed(tmp_path, npu2):
    region = _axpy_region()
    entry = Entry(root=region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == profile.entries()
    mul, add = toys.axpy_ops()
    recording = toys.axpy_recording("axpy", mul, add)
    calls = [Timed(recording)]
    assert any(
        entry in edit.apply(Profile()).entries()
        for edit in candidates(calls, Profile(), npu2)
    )


@unbuilt
def test_every_known_mha_mapping_composes_as_the_graph(npu2):
    """Replaces ``tests/applications/test_attention_shapes.py``: every known mapping composes, decode and prefill."""
    decode_entry = Entry(
        root=_decode_region(
            LLAMA1B_DECODE["kv_len"],
            LLAMA1B_DECODE["head_dim"],
            LLAMA1B_DECODE["heads"],
        )
    )
    qk, softmax, pv = toys.decode_attention_ops(
        LLAMA1B_DECODE["kv_len"], LLAMA1B_DECODE["head_dim"], LLAMA1B_DECODE["heads"]
    )
    decode_recording = toys.decode_attention_recording(
        "llama1b_decode", qk, softmax, pv
    )
    assert any(
        decode_entry in edit.apply(Profile()).entries()
        for edit in candidates([Timed(decode_recording)], Profile(), npu2)
    )

    prefill_entry = Entry(
        root=_prefill_region(
            LLAMA1B_PREFILL["seq"],
            LLAMA1B_PREFILL["kv_len"],
            LLAMA1B_PREFILL["head_dim"],
        )
    )
    qk, add_mask, softmax, pv = toys.prefill_attention_ops(
        LLAMA1B_PREFILL["seq"], LLAMA1B_PREFILL["kv_len"], LLAMA1B_PREFILL["head_dim"]
    )
    prefill_recording = toys.prefill_attention_recording(
        "llama1b_prefill", qk, add_mask, softmax, pv
    )
    assert any(
        prefill_entry in edit.apply(Profile()).entries()
        for edit in candidates([Timed(prefill_recording)], Profile(), npu2)
    )


def test_prefill_s_float32_scores_do_not_fit_the_bf16_mask_add(npu2):
    """GEMM can keep ``Q K^T`` in float32 (``output_dtype``), but the mask's ElementwiseAdd reads only bf16.

    The two ends are then not one buffer, which the analysis refuses: the
    prefill graph cannot keep its scores in float32 into the mask until an
    elementwise operator reads float32.
    """
    qk = GEMM(
        M=SEQ,
        K=HEAD_DIM,
        N=KV_LEN,
        b_col_maj=True,
        precision=Precision.MEDIUM,
        output_dtype=np.float32,
    )
    _, add_mask, softmax, pv = toys.prefill_attention_ops(SEQ, KV_LEN, HEAD_DIM)
    recording = toys.prefill_attention_recording(
        "prefill_f32_scores", qk, add_mask, softmax, pv
    )
    region = _prefill_region(SEQ, KV_LEN, HEAD_DIM, scores_dtype=np.float32)
    with pytest.raises(ValueError, match="not one buffer"):
        analyze(region, recording, npu2)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "rows, kv_len",
    [
        (
            32,
            128,
        ),  # padding rows free of NaN (iron/tests/operators/test_mha_bounded_rows.py)
        (16, 128),  # NaN or stale data past the bound
        (32, 96),  # a call whose queries start mid-block
    ],
    ids=["padding_free_of_nan", "stale_past_bound", "mid_block_start"],
)
@unbuilt
def test_decode_graph_is_no_worse_than_its_own_untuned_build(rows, kv_len, npu2):
    qk, softmax, pv = toys.decode_attention_ops(kv_len, HEAD_DIM, rows)
    recording = toys.decode_attention_recording("decode_bounded", qk, softmax, pv)
    region = _decode_region(kv_len, HEAD_DIM, rows)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "position",
    [
        pytest.param(1023, id="position_1023", marks=unbuilt),
        # A whole 32704-key row fits no core: a split-KV merge kernel.
        pytest.param(32703, id="position_32703", marks=waits_on_a_kernel),
    ],
)
def test_decode_graph_holds_deep_cache_accuracy(position, npu2):
    """Ports the deep-cache positions of ``iron/tests/operators/test_mha_long_context.py``: ``kv_len`` is the cache read up to ``position``."""
    kv_len = position + 1
    qk, softmax, pv = toys.decode_attention_ops(kv_len, HEAD_DIM, ROWS)
    recording = toys.decode_attention_recording(
        f"decode_at_{position}", qk, softmax, pv
    )
    region = _decode_region(kv_len, HEAD_DIM, ROWS)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
@unbuilt
def test_prefill_graph_is_no_worse_than_its_own_untuned_build(npu2):
    qk, add_mask, softmax, pv = toys.prefill_attention_ops(SEQ, KV_LEN, HEAD_DIM)
    recording = toys.prefill_attention_recording("prefill", qk, add_mask, softmax, pv)
    profile, base = Profile(), Profile()
    profile.add_entry(Entry(root=_prefill_region()))
    result = check(profile, base, [Timed(recording)], npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
@unbuilt
def test_decode_graph_is_no_worse_than_the_fused_mha_it_replaces(npu2):
    """Held to the fused ``MHA`` operator it replaces, at the same sizes, the graph's float32 scores are no worse."""
    qk, softmax, pv = toys.decode_attention_ops(KV_LEN, HEAD_DIM, ROWS)
    graph_recording = toys.decode_attention_recording("decode_vs_mha", qk, softmax, pv)
    mha = toys.decode_attention_operator(KV_LEN, HEAD_DIM, ROWS)
    operator_recording = toys.decode_attention_operator_recording("decode_mha", mha)
    profile = Profile()
    profile.add_entry(Entry(root=_decode_region()))
    result = check(
        profile,
        Profile(),
        [Timed(graph_recording)],
        npu2,
        Refinement.NO_WORSE,
        base_calls=[Timed(operator_recording)],
    )
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
@unbuilt  # GEMM's float32 scores staged into the mask add
def test_prefill_graph_is_no_worse_than_the_fused_mha_it_replaces(npu2):
    """Held to the fused ``MHA`` operator it replaces, scores matched to its own float32 setting, the graph is no worse."""
    qk, add_mask, softmax, pv = toys.prefill_attention_ops(
        SEQ, KV_LEN, HEAD_DIM, scores=np.float32
    )
    graph_recording = toys.prefill_attention_recording(
        "prefill_vs_mha", qk, add_mask, softmax, pv
    )
    mha = toys.prefill_attention_operator(SEQ, KV_LEN, HEAD_DIM)
    operator_recording = toys.prefill_attention_operator_recording("prefill_mha", mha)
    profile = Profile()
    profile.add_entry(
        Entry(root=_prefill_region(SEQ, KV_LEN, HEAD_DIM, scores_dtype=np.float32))
    )
    result = check(
        profile,
        Profile(),
        [Timed(graph_recording)],
        npu2,
        Refinement.NO_WORSE,
        base_calls=[Timed(operator_recording)],
    )
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
@unbuilt
def test_a_bf16_mul_then_add_hand_off_is_refused_against_the_fused_axpy(npu2):
    """``AXPY`` keeps ``scalar_factor * x`` at float32 before the add; the graph's bf16 ``mid`` is refused against it."""
    mul, add = toys.axpy_ops()
    graph_recording = toys.axpy_recording("axpy_vs_fused", mul, add)
    axpy = toys.axpy_operator(size=mul.size, tile=mul.tile_size)
    operator_recording = toys.axpy_operator_recording("axpy_fused", axpy)
    constant_a = np.full(mul.size, axpy.scalar_factor, dtype=bfloat16)
    profile = Profile()
    profile.add_entry(Entry(root=_axpy_region()))
    result = check(
        profile,
        Profile(),
        [Timed(graph_recording, contents={"a": constant_a})],
        npu2,
        Refinement.NO_WORSE,
        base_calls=[Timed(operator_recording)],
    )
    assert not result.ok


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
@unbuilt  # a batched GEMV's B streams on no fifo of its own
def test_search_composes_the_decode_graph_where_it_pays(npu2):
    region = _decode_region()
    entry = Entry(root=region)
    qk, softmax, pv = toys.decode_attention_ops(KV_LEN, HEAD_DIM, ROWS)
    recording = toys.decode_attention_recording("decode_search", qk, softmax, pv)
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, npu2).ratio
    tuned = search(calls, start, npu2)
    if ratio < 0.95:
        assert entry in tuned.entries()
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
@unbuilt
def test_search_composes_the_prefill_graph_where_it_pays(npu2):
    region = _prefill_region()
    entry = Entry(root=region)
    qk, add_mask, softmax, pv = toys.prefill_attention_ops(SEQ, KV_LEN, HEAD_DIM)
    recording = toys.prefill_attention_recording(
        "prefill_search", qk, add_mask, softmax, pv
    )
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, npu2).ratio
    tuned = search(calls, start, npu2)
    if ratio < 0.95:
        assert entry in tuned.entries()
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, npu2, Refinement.NO_WORSE)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
@unbuilt
def test_search_composes_the_axpy_graph_where_it_pays(npu2):
    region = _axpy_region()
    entry = Entry(root=region)
    mul, add = toys.axpy_ops()
    recording = toys.axpy_recording("axpy_search", mul, add)
    calls = [Timed(recording)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(entry)
    ratio = measure(with_entry, start, calls, npu2).ratio
    tuned = search(calls, start, npu2)
    if ratio < 0.95:
        assert entry in tuned.entries()
    if ratio > 1.05:
        assert entry not in tuned.entries()
    result = check(tuned, start, calls, npu2, Refinement.NO_WORSE)
    assert result.ok, result.why
