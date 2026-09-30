#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils

from iron.operators.flm.prefill_attn.op import (
    PrefillAttention,
    PrefillSlidingAttention,
)
from iron.operators.flm.prefill_attn.reference import reference
from iron.operators.flm.testing import requires_aie2p

NUM_HEADS = 8
# The operator cannot produce this value from the inputs below. The rows past
# L_end - L_begin must keep it.
SENTINEL = 7.0

# The outputs are of order 1. The gate therefore bounds the absolute error. A
# stale token range gives a mean error of 0.03 or more.
MAX_ERROR = 0.25
MEAN_ERROR = 0.02

# Per operator: its class, the arguments of the build under test, and token
# ranges (L_begin, L_end, max_l).
OPERATORS = {
    "attn": (
        PrefillAttention,
        dict(max_context=1024),
        [
            (0, 128, 1024),
            (0, 512, 1024),
            (128, 384, 1024),
            (256, 1024, 1024),
            # max_l below max_context.
            (0, 256, 512),
        ],
    ),
    "swa": (
        PrefillSlidingAttention,
        dict(max_context=2048, window=512),
        [
            (0, 128, 2048),
            # Queries past token 512 lose their oldest keys to the window.
            (0, 1024, 2048),
            # The window moves the k/v reads past token 0.
            (512, 1024, 2048),
            (1024, 2048, 2048),
            (0, 512, 1024),
        ],
    ),
}


def _inputs(op, max_l, seed):
    """q and a KV cache whose scores stay in softmax's useful range."""
    rng = np.random.default_rng(seed)
    dh = op.variant.dh
    q = (rng.standard_normal(op.max_context * NUM_HEADS * dh) * 0.2).astype(bfloat16)
    half = max_l * op.num_kv_heads * dh
    kv = np.zeros(2 * op.max_context * op.num_kv_heads * dh, dtype=bfloat16)
    kv[:half] = (rng.standard_normal(half) * 0.2).astype(bfloat16)
    kv[half : 2 * half] = rng.standard_normal(half).astype(bfloat16)
    return q, kv


def _check(op, run, L_begin, L_end, max_l, seed):
    q, kv = _inputs(op, max_l, seed)
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
    dh = op.variant.dh
    n = (L_end - L_begin) * NUM_HEADS * dh
    expected = reference(
        q, kv, L_begin, L_end, max_l, NUM_HEADS, op.num_kv_heads, dh, op.window
    ).reshape(-1)
    error = np.abs(o[:n] - expected)
    label = f"L=[{L_begin},{L_end}) max_l={max_l}"
    assert not np.isnan(error).any(), f"{label}: NaN in the output"
    assert error.max() <= MAX_ERROR, f"{label}: max |error| {error.max():.3f}"
    assert error.mean() <= MEAN_ERROR, f"{label}: mean |error| {error.mean():.4f}"
    assert np.all(o[n:] == SENTINEL), f"{label}: wrote past its rows"


def _build(kind, aie_context, **overrides):
    cls, kwargs, _ = OPERATORS[kind]
    op = cls(num_heads=NUM_HEADS, context=aie_context, **{**kwargs, **overrides})
    op.compile()
    return op


@requires_aie2p
@pytest.mark.parametrize("num_kv_heads", [1, 2])
@pytest.mark.parametrize(
    "kind, L_begin, L_end, max_l",
    [(kind, *r) for kind, (_, _, ranges) in OPERATORS.items() for r in ranges],
)
def test_matches_reference(kind, L_begin, L_end, max_l, num_kv_heads, aie_context):
    op = _build(kind, aie_context, num_kv_heads=num_kv_heads)
    _check(op, op.get_callable(), L_begin, L_end, max_l, seed=L_end)


@requires_aie2p
@pytest.mark.parametrize("kind", OPERATORS)
def test_one_callable_serves_every_range(kind, aie_context):
    """Check that each dispatch runs its own token range.

    The ranges run back to back on one loaded xclbin: growing, shrinking and
    repeated. A stale range appears only from the second dispatch after a load.
    """
    op = _build(kind, aie_context, num_kv_heads=1)
    run = op.get_callable()
    ranges = OPERATORS[kind][2]
    for seed, i in enumerate((0, 1, 1, 2, 4, 3, 0)):
        _check(op, run, *ranges[i], seed)


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize("num_kv_heads", [1, 2])
@pytest.mark.parametrize("kind", OPERATORS)
def test_gemma4_cache_bound(kind, num_kv_heads, aie_context):
    """Check the cache bound of Gemma 4's engine: 32768 rows."""
    op = _build(kind, aie_context, num_kv_heads=num_kv_heads, max_context=32768)
    run = op.get_callable()
    for seed, (L_begin, L_end, max_l) in enumerate(
        [(0, 2048, 4096), (2048, 2304, 4096), (0, 1024, 32768)]
    ):
        _check(op, run, L_begin, L_end, max_l, seed)


@pytest.mark.parametrize(
    "cls, kwargs, match",
    [
        (PrefillAttention, dict(num_kv_heads=3), "multiple of"),
        (PrefillAttention, dict(num_kv_heads=8), "query heads"),
        (PrefillSlidingAttention, dict(num_kv_heads=3), "multiple of"),
        (PrefillSlidingAttention, dict(num_kv_heads=4), "query heads"),
        (
            PrefillAttention,
            dict(max_context=1000, num_kv_heads=1),
            "multiple of 128",
        ),
        (
            PrefillSlidingAttention,
            dict(max_context=1000, num_kv_heads=1),
            "multiple of 128",
        ),
        (
            PrefillSlidingAttention,
            dict(num_kv_heads=1, window=500),
            "multiple of 128",
        ),
    ],
)
@requires_aie2p
def test_rejects_unservable_shapes(cls, kwargs, match, aie_context):
    with pytest.raises(ValueError, match=match):
        cls(**{"max_context": 1024, "num_heads": 8, **kwargs}, context=aie_context)
