#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.benchmark import run_iters
from aie.utils.hostruntime.hostruntime import HostRuntimeError
from ml_dtypes import bfloat16

from iron.common.image import OperatorImage
from iron.operators.flm.prefill_attn.op import (
    PrefillAttention,
    PrefillSlidingAttention,
)
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
    """Draw q and a KV cache whose scores stay in softmax's useful range."""
    rng = np.random.default_rng(seed)
    dh = op.head_dim
    q = (rng.standard_normal(op.max_context * NUM_HEADS * dh) * 0.2).astype(bfloat16)
    half = max_l * op.num_kv_heads * dh
    kv = np.zeros(2 * op.max_context * op.num_kv_heads * dh, dtype=bfloat16)
    kv[:half] = (rng.standard_normal(half) * 0.2).astype(bfloat16)
    kv[half : 2 * half] = rng.standard_normal(half).astype(bfloat16)
    return q, kv


def _record(op, image, bufs, L_begin, L_end, max_l, record):
    """Time one more dispatch and record its latency, bandwidth and throughput.

    The bytes count the query and output rows of the range and the K and V rows
    that its queries read. The FLOPs count the scores and the weighted sum of V.
    """
    dh = op.head_dim
    keys = np.arange(L_begin, L_end) + 1
    if op.window is not None:
        keys = np.minimum(keys, op.window)
    rows_read = L_end if op.window is None else L_end - max(L_begin - op.window, 0)
    total_bytes = (
        2 * dh * (2 * (L_end - L_begin) * NUM_HEADS + 2 * rows_read * op.num_kv_heads)
    )
    flops = 4 * NUM_HEADS * dh * int(keys.sum())
    latency_us = run_iters(
        image, *bufs, warmup=1, iters=1, L_begin=L_begin, L_end=L_end, max_l=max_l
    ).npu.avg_us
    record("Latency", latency_us)
    record("Bandwidth", total_bytes / latency_us / 1e3)
    record("Throughput", flops / latency_us / 1e3)


def _check(op, image, L_begin, L_end, max_l, seed, record=None):
    q, kv = _inputs(op, max_l, seed)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    bufs = (tensor(np.full(q.size, SENTINEL, dtype=bfloat16)), tensor(q), tensor(kv))
    image(*bufs, L_begin=L_begin, L_end=L_end, max_l=max_l)

    o = bufs[0].numpy().astype(np.float32)
    n = (L_end - L_begin) * NUM_HEADS * op.head_dim
    expected = op.reference(q, kv, L_begin, L_end, max_l)
    error = np.abs(o[:n] - expected)
    label = f"L=[{L_begin},{L_end}) max_l={max_l}"
    assert not np.isnan(error).any(), f"{label}: NaN in the output"
    assert error.max() <= MAX_ERROR, f"{label}: max |error| {error.max():.3f}"
    assert error.mean() <= MEAN_ERROR, f"{label}: mean |error| {error.mean():.4f}"
    assert np.all(o[n:] == SENTINEL), f"{label}: wrote past its rows"
    if record is not None:
        _record(op, image, bufs, L_begin, L_end, max_l, record)


def _build(kind, **overrides):
    cls, kwargs, _ = OPERATORS[kind]
    return cls(num_heads=NUM_HEADS, **{**kwargs, **overrides})


# One 512-token prompt chunk per operator, the chunk length of Gemma 4's engine.
# The sliding-window chunk starts past the window, so the window cuts its keys.
BENCH = {("attn", 0, 512, 1024, 1), ("swa", 512, 1024, 2048, 1)}


@requires_aie2p
@pytest.mark.parametrize(
    "kind, L_begin, L_end, max_l, num_kv_heads",
    [
        pytest.param(
            kind,
            *r,
            kv,
            marks=[pytest.mark.bench] if (kind, *r, kv) in BENCH else [],
        )
        for kv in (1, 2)
        for kind, (_, _, ranges) in OPERATORS.items()
        for r in ranges
    ],
)
def test_matches_reference(
    kind, L_begin, L_end, max_l, num_kv_heads, npu_runtime, record_property
):
    op = _build(kind, num_kv_heads=num_kv_heads)
    _check(
        op, OperatorImage(op), L_begin, L_end, max_l, seed=L_end, record=record_property
    )


@requires_aie2p
@pytest.mark.parametrize("kind", OPERATORS)
def test_one_image_serves_every_range(kind, npu_runtime):
    """Check that each dispatch runs its own token range.

    The ranges run back to back on one loaded xclbin: growing, shrinking and
    repeated. A stale range appears only from the second dispatch after a load.
    """
    op = _build(kind, num_kv_heads=1)
    image = OperatorImage(op)
    ranges = OPERATORS[kind][2]
    for seed, i in enumerate((0, 1, 1, 2, 4, 3, 0)):
        L_begin, L_end, max_l = ranges[i]
        _check(op, image, L_begin, L_end, max_l, seed)


@requires_aie2p
@pytest.mark.parametrize(
    "L_begin, L_end, max_l, match",
    [
        (0, 200, 1024, "L_end must be a multiple of 128"),
        (64, 256, 1024, "L_begin must be a multiple of 128"),
        (-128, 256, 1024, "L_begin must be >= 0"),
        (0, 256, 2048, "max_l exceeds max_context"),
        (0, 512, 256, "slice stop exceeds the dimension"),
    ],
)
def test_refuses_unservable_ranges(L_begin, L_end, max_l, match, npu_runtime):
    """The dispatch checks the token range before the array runs."""
    op = _build("attn", num_kv_heads=1)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    bufs = [
        tensor(np.zeros(n, dtype=bfloat16)) for n in (op.qo_len, op.qo_len, op.kv_len)
    ]
    with pytest.raises(HostRuntimeError, match=match):
        OperatorImage(op)(*bufs, L_begin=L_begin, L_end=L_end, max_l=max_l)


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize("num_kv_heads", [1, 2])
@pytest.mark.parametrize("kind", OPERATORS)
def test_gemma4_cache_bound(kind, num_kv_heads, npu_runtime):
    """Check the cache bound of Gemma 4's engine: 32768 rows."""
    op = _build(kind, num_kv_heads=num_kv_heads, max_context=32768)
    image = OperatorImage(op)
    for seed, (L_begin, L_end, max_l) in enumerate(
        [(0, 2048, 4096), (2048, 2304, 4096), (0, 1024, 32768)]
    ):
        _check(op, image, L_begin, L_end, max_l, seed)


@pytest.mark.parametrize(
    "cls, kwargs, match",
    [
        (PrefillAttention, dict(num_kv_heads=3), "multiple of"),
        (PrefillAttention, dict(num_kv_heads=0), "must be positive"),
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
def test_rejects_unservable_shapes(cls, kwargs, match):
    with pytest.raises(ValueError, match=match):
        cls(**{"max_context": 1024, "num_heads": 8, **kwargs})
