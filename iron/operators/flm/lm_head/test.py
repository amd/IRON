#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16

from iron.common.image import OperatorImage
from iron.operators.flm.lm_head.op import LMHead
from iron.operators.flm.q4nx import GROUP, K_TILE, M_TILE
from iron.operators.flm.testing import requires_aie2p

# The initial value of y. No logit of the test inputs reaches it, so an
# unwritten output fails the check.
SENTINEL = 99.0

# Error bounds from README.md's Numerics section.
PROJECTION_ERROR = 0.025
TANH_ERROR = 0.04

GEMMA4_SOFTCAP = 30.0


def _inputs(dim, vocab, seed):
    """A q4nx vocabulary and a token with its RMS weight.

    Negative minima and small scales keep the logits in the range a softcap
    of 30 bends.
    """
    rng = np.random.default_rng(seed)
    groups = K_TILE // GROUP
    n_blocks = vocab * dim // (M_TILE * K_TILE)
    params = np.concatenate(
        [
            rng.uniform(0, 0.02, (n_blocks, groups * M_TILE)),
            rng.uniform(-0.15, 0, (n_blocks, groups * M_TILE)),
        ],
        axis=1,
    )
    params = params.astype(bfloat16).view(np.uint16).astype("<u2").view(np.uint8)
    codes = rng.integers(0, 256, (n_blocks, M_TILE * K_TILE // 2), dtype=np.uint8)
    w = np.concatenate([params, codes], axis=1).reshape(-1)
    x = np.concatenate([rng.standard_normal(dim), rng.uniform(0.5, 1.5, dim)])
    return w, x.astype(bfloat16)


def _check(dim, vocab, softcap, seed=0, tanh_error=True, record=None):
    """Compare the device's logits for seed's inputs with the reference."""
    op = LMHead(dim=dim, vocab=vocab, softcap=softcap)
    w, x = _inputs(dim, vocab, seed)
    image = OperatorImage(op)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    bufs = (
        tensor(np.full(vocab, SENTINEL, dtype=bfloat16)),
        tensor(w.view(np.uint32)),
        tensor(x),
    )
    image(*bufs)
    got = bufs[0].numpy().astype(np.float64)
    if record is not None:
        latency_us = run_iters(image, *bufs, warmup=1, iters=1).npu.avg_us
        record("Latency", latency_us)
        record("Bandwidth", sum(b.numpy().nbytes for b in bufs) / latency_us / 1e3)
        record("Throughput", op.ops() / latency_us / 1e3)
    expected = op.reference(w, x)
    # The logits before the softcap set the projection's error scale.
    uncapped = LMHead(dim=dim, vocab=vocab, softcap=1e30).reference(w, x)
    bound = PROJECTION_ERROR * np.abs(uncapped).max()
    if tanh_error:
        bound += TANH_ERROR * softcap
    error = np.abs(got - expected)
    label = f"dim={dim} vocab={vocab} softcap={softcap}"
    assert error.max() <= bound, f"{label}: max |error| {error.max():.3f} > {bound:.3f}"
    return got


@requires_aie2p
@pytest.mark.parametrize("dim", [1536, 2560])
def test_projection_matches_reference(dim, npu_runtime):
    """A softcap of 1000 keeps each tanh argument near zero.

    The test therefore checks the projection alone.

    1536 and 2560 are Gemma 4 E2B's and E4B's hidden sizes.
    """
    _check(dim, 4096, 1000.0, tanh_error=False)


@requires_aie2p
@pytest.mark.parametrize("dim", [1536, 2560])
def test_gemma4_softcap(dim, npu_runtime):
    _check(dim, 4096, GEMMA4_SOFTCAP, seed=1)


@requires_aie2p
def test_softcap_bounds_the_logits(npu_runtime):
    """A softcap of 5 saturates most logits. No logit may exceed the softcap."""
    got = _check(1536, 1024, 5.0, seed=2)
    assert np.abs(got).max() <= 5.0


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize("dim", [pytest.param(1536, marks=pytest.mark.bench), 2560])
def test_gemma4_vocabulary(dim, npu_runtime, record_property):
    """Gemma 4's whole vocabulary of 262144 logits."""
    _check(dim, 262144, GEMMA4_SOFTCAP, seed=3, record=record_property)


@requires_aie2p
@pytest.mark.parametrize(
    "dim, vocab, softcap, match",
    [
        (1000, 4096, 30.0, "multiple of"),
        (1536, 1000, 30.0, "multiple of"),
        (1536, 4096, 0.0, "finite and positive"),
        (1536, 4096, float("inf"), "finite and positive"),
    ],
)
def test_rejects_unservable_shapes(dim, vocab, softcap, match):
    with pytest.raises(ValueError, match=match):
        LMHead(dim=dim, vocab=vocab, softcap=softcap).resolved()
