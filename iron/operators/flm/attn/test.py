#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch

from iron.operators.flm.attn.design import DH
from iron.operators.flm.attn.op import PrefillAttention
from iron.operators.flm.attn.reference import reference

NUM_HEADS = 8
MAX_CONTEXT = 1024
# A value the operator cannot produce from the inputs below, in the rows past
# L_end - L_begin, which it must leave alone.
SENTINEL = 7.0

# The device rounds scores, probabilities and output to bfloat16. Outputs are
# O(1), so the gate is an absolute distance. A stale token range, the failure
# these tests exist for, measures a mean of 0.03 or more.
MAX_ERROR = 0.25
MEAN_ERROR = 0.02


def _on_aie2p():
    dev = aie_utils.get_current_device()
    return dev is not None and dev.arch == AIEArch.AIE2p


requires_aie2p = pytest.mark.skipif(
    not _on_aie2p(), reason="the attn_prefill kernel is AIE2P only"
)


def _inputs(max_context, num_kv_heads, max_l, seed):
    """q and a KV cache whose scores stay in softmax's useful range."""
    rng = np.random.default_rng(seed)
    q = (rng.standard_normal(max_context * NUM_HEADS * DH) * 0.2).astype(bfloat16)
    half = max_l * num_kv_heads * DH
    kv = np.zeros(2 * max_context * num_kv_heads * DH, dtype=bfloat16)
    kv[:half] = (rng.standard_normal(half) * 0.2).astype(bfloat16)
    kv[half : 2 * half] = rng.standard_normal(half).astype(bfloat16)
    return q, kv


def _check(op, run, L_begin, L_end, max_l, seed):
    q, kv = _inputs(op.max_context, op.num_kv_heads, max_l, seed)
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    q_buf = tensor_class((q.size,), dtype=bfloat16)
    q_buf.numpy_view()[:] = q
    kv_buf = tensor_class((kv.size,), dtype=bfloat16)
    kv_buf.numpy_view()[:] = kv
    o_buf = tensor_class((q.size,), dtype=bfloat16)
    o_buf.numpy_view()[:] = bfloat16(SENTINEL)

    run.set_parameters(L_begin=L_begin, L_end=L_end, max_l=max_l)
    run(o_buf, q_buf, kv_buf)

    o = o_buf.numpy().astype(np.float32)
    n = (L_end - L_begin) * NUM_HEADS * DH
    expected = reference(
        q, kv, L_begin, L_end, max_l, NUM_HEADS, op.num_kv_heads
    ).reshape(-1)
    error = np.abs(o[:n] - expected)
    label = f"L=[{L_begin},{L_end}) max_l={max_l}"
    assert not np.isnan(error).any(), f"{label}: NaN in the output"
    assert error.max() <= MAX_ERROR, f"{label}: max |error| {error.max():.3f}"
    assert error.mean() <= MEAN_ERROR, f"{label}: mean |error| {error.mean():.4f}"
    assert np.all(o[n:] == SENTINEL), f"{label}: wrote past its rows"


RANGES = [
    (0, 128, MAX_CONTEXT),
    (0, 512, MAX_CONTEXT),
    (128, 384, MAX_CONTEXT),
    (256, 1024, MAX_CONTEXT),
    # A cache shorter than the build's bound moves V to row max_l.
    (0, 256, MAX_CONTEXT // 2),
]


@requires_aie2p
@pytest.mark.parametrize("num_kv_heads", [1, 2])
@pytest.mark.parametrize("L_begin, L_end, max_l", RANGES)
def test_matches_reference(L_begin, L_end, max_l, num_kv_heads, aie_context):
    op = PrefillAttention(
        max_context=MAX_CONTEXT,
        num_heads=NUM_HEADS,
        num_kv_heads=num_kv_heads,
        context=aie_context,
    )
    op.compile()
    _check(op, op.get_callable(), L_begin, L_end, max_l, seed=L_end)


@requires_aie2p
def test_one_callable_serves_every_range(aie_context):
    """Ranges back to back on one loaded xclbin, growing, shrinking and
    repeated. Each core reads the token range from its RTPs, so a core that
    reads them before the sequence writes them runs the previous dispatch's
    range. The first dispatch after a load cannot show that."""
    op = PrefillAttention(
        max_context=MAX_CONTEXT,
        num_heads=NUM_HEADS,
        num_kv_heads=1,
        context=aie_context,
    )
    op.compile()
    run = op.get_callable()
    ranges = [RANGES[i] for i in (0, 1, 1, 2, 4, 3, 0)]
    for seed, (L_begin, L_end, max_l) in enumerate(ranges):
        _check(op, run, L_begin, L_end, max_l, seed)


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize("num_kv_heads", [1, 2])
def test_gemma4_cache_bound(num_kv_heads, aie_context):
    """The bound Gemma 4's engine builds for: 32768 rows."""
    op = PrefillAttention(
        max_context=32768,
        num_heads=NUM_HEADS,
        num_kv_heads=num_kv_heads,
        context=aie_context,
    )
    op.compile()
    run = op.get_callable()
    for seed, (L_begin, L_end, max_l) in enumerate(
        [(0, 2048, 4096), (2048, 2304, 4096), (0, 1024, 32768)]
    ):
        _check(op, run, L_begin, L_end, max_l, seed)


@pytest.mark.parametrize(
    "kwargs, match",
    [
        (dict(max_context=1024, num_heads=8, num_kv_heads=3), "multiple of"),
        (dict(max_context=1024, num_heads=8, num_kv_heads=8), "query heads"),
        (dict(max_context=1000, num_heads=8, num_kv_heads=1), "multiple of 128"),
    ],
)
@requires_aie2p
def test_rejects_unservable_shapes(kwargs, match, aie_context):
    with pytest.raises(ValueError, match=match):
        PrefillAttention(context=aie_context, **kwargs)
