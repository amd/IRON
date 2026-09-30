#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils

from iron.operators.flm.dataflow import grid
from iron.operators.flm.lm_head.op import LMHead
from iron.operators.flm.lm_head.reference import dequantize, reference
from iron.operators.flm.q4nx import GROUP, K_TILE, M_TILE
from iron.operators.flm.testing import requires_aie2p

# The initial value of y. No logit of the test inputs reaches it, so an
# unwritten output fails the check.
SENTINEL = 99.0

# Error bounds from README.md's Numerics section. PROJECTION_ERROR scales
# with the largest logit. The softcap scales TANH_ERROR.
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


def _run(op, w, x):
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    w_buf = tensor_class((w.size // 4,), dtype=np.uint32)
    w_buf.numpy_view()[:] = w.view(np.uint32)
    x_buf = tensor_class((x.size,), dtype=bfloat16)
    x_buf.numpy_view()[:] = x
    y_buf = tensor_class((op.vocab,), dtype=bfloat16)
    y_buf.numpy_view()[:] = bfloat16(SENTINEL)
    op.get_callable()(y_buf, w_buf, x_buf)
    return y_buf.numpy().astype(np.float64)


def _check(dim, vocab, softcap, aie_context, seed=0):
    op = LMHead(dim=dim, vocab=vocab, softcap=softcap, context=aie_context)
    op.compile()
    w, x = _inputs(dim, vocab, seed)
    got = _run(op, w, x)
    cols, rows = grid(aie_utils.get_current_device())
    weights = dequantize(w, dim, vocab, cols, rows)
    x64 = x.astype(np.float64)
    expected = reference(weights, x64, softcap)
    # The logits before the softcap set the projection's error scale.
    uncapped = reference(weights, x64, 1e30)
    bound = PROJECTION_ERROR * np.abs(uncapped).max()
    if softcap < 1e3:
        bound += TANH_ERROR * softcap
    error = np.abs(got - expected)
    label = f"dim={dim} vocab={vocab} softcap={softcap}"
    assert error.max() <= bound, f"{label}: max |error| {error.max():.3f} > {bound:.3f}"
    return got


@requires_aie2p
@pytest.mark.parametrize("dim", [1536, 2560])
def test_projection_matches_reference(dim, aie_context):
    """A cap of 1000 keeps tanh near zero, so this judges the projection alone.

    1536 and 2560 are Gemma 4 E2B's and E4B's hidden sizes.
    """
    _check(dim, 4096, 1000.0, aie_context)


@requires_aie2p
@pytest.mark.parametrize("dim", [1536, 2560])
def test_gemma4_softcap(dim, aie_context):
    _check(dim, 4096, GEMMA4_SOFTCAP, aie_context, seed=1)


@requires_aie2p
def test_softcap_bounds_the_logits(aie_context):
    """A small cap saturates most logits; none may pass it."""
    got = _check(1536, 1024, 5.0, aie_context, seed=2)
    assert np.abs(got).max() <= 5.0


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize("dim", [1536, 2560])
def test_gemma4_vocabulary(dim, aie_context):
    """Gemma 4's whole vocabulary of 262144 logits."""
    _check(dim, 262144, GEMMA4_SOFTCAP, aie_context, seed=3)


@requires_aie2p
@pytest.mark.parametrize(
    "dim, vocab, match",
    [(1000, 4096, "multiple of"), (1536, 1000, "multiple of")],
)
def test_rejects_unservable_shapes(dim, vocab, match, aie_context):
    with pytest.raises(ValueError, match=match):
        LMHead(dim=dim, vocab=vocab, softcap=30.0, context=aie_context)
