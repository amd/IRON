#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GEMM's per-call bound on K, on a device.

Attention over a padded prompt bounds its weights to the ``n`` valid keys,
``GEMM(Softmax(s[:, :n]), v[:n])``: the cores reduce over the K tiles ``n``
covers, the last of them with its columns of A and rows of B past ``n``
zeroed, and pass the rest through.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.gemm import GEMM
from iron.operators.softmax import Softmax

ROWS, SEQ, D = 128, 2048, 128
POSITIONS = (SEQ, 300, 1, 63, 64, 65, 1024, 1025, 2047, 1000)
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)
MODES = {
    "accurate": ACCURATE,
    "default": dict(),
    "b_col_maj": dict(ACCURATE, b_col_maj=True),
    "scalar": dict(ACCURATE, use_scalar=True),
}

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("mode", MODES)
def test_the_reduction_stops_at_the_per_call_length(npu_runtime, mode):
    """A and B are NaN past ``n``: a column or row past the bound that were
    multiplied, in the last K tile or past it, would bring a NaN into every
    element. Each micro-tile layout the cores zero it in is covered: A's,
    B's by rows and by columns, and the scalar kernel's plain one.
    """
    b_col_maj = MODES[mode].get("b_col_maj", False)

    class Product(iron.Graph):
        def body(self, a, b, *, n: Scratchpad[np.int32]):
            return GEMM(a[:, :n], b[:, :n] if b_col_maj else b[:n], **MODES[mode])

    product = Product()
    net = product.compile(a=(ROWS, SEQ), b=(D, SEQ) if b_col_maj else (SEQ, D))
    tile_k = GEMM(M=ROWS, K=SEQ, N=D, **MODES[mode]).tile_k

    # bfp16's shared exponents hold a one-term product to past its tolerance,
    # which is measured on dense sums.
    positions = [n for n in POSITIONS if n > 1 or mode != "default"]
    rng = np.random.default_rng(0)
    for n in positions:
        k = -(-n // tile_k) * tile_k
        a = rng.standard_normal((ROWS, SEQ)).astype(bfloat16)
        b = rng.standard_normal((SEQ, D)).astype(bfloat16)
        a[:, n:], b[n:] = np.nan, np.nan
        given = np.ascontiguousarray(b.T) if b_col_maj else b
        got = np.asarray(net(a, given, n=n)).reshape(ROWS, D)
        want = product.reference(a, given, n=n)
        tolerance = GEMM(M=ROWS, K=k, N=D, **MODES[mode]).tolerance()
        a_k, b_k = np.zeros_like(a[:, :k]), np.zeros_like(b[:k])
        a_k[:, :n], b_k[:n] = a[:, :n], b[:n]
        bound = tolerance.bound(a_k, b_k.T if b_col_maj else b_k)
        verdict = verify_buffer(got, "C", want, tolerance, bound=bound)
        assert verdict, f"n={n}: {verdict.detail}"


@pytest.mark.supported_devices("npu2")
def test_attention_reduces_over_the_valid_keys(npu_runtime):
    """The Softmax writes only the blocks ``n`` covers, so the calls run
    long before short: a block a longer call wrote holds its weights, and a
    GEMM that reduced over it would add them in. ``v`` is NaN past ``n``,
    as stale rows of a cache may be anything. The product is checked
    against the weights the device computed.
    """

    class Attend(iron.Graph):
        def body(self, s, v, *, n: Scratchpad[np.int32]):
            weights = Softmax(s[:, :n])
            return weights, GEMM(weights, v[:n], **ACCURATE)

    net = Attend().compile(s=(ROWS, SEQ), v=(SEQ, D))
    tile_k = GEMM(M=ROWS, K=SEQ, N=D, **ACCURATE).tile_k

    rng = np.random.default_rng(0)
    for n in POSITIONS:
        k = -(-n // tile_k) * tile_k
        s = rng.standard_normal((ROWS, SEQ)).astype(bfloat16)
        v = rng.standard_normal((SEQ, D)).astype(bfloat16)
        v[n:] = np.nan
        weights, got = net(s, v, n=n)
        weights = np.asarray(weights).reshape(ROWS, SEQ)[:, :k]
        got = np.asarray(got).reshape(ROWS, D)
        v_k = np.zeros_like(v[:k])
        v_k[:n] = v[:n]
        gemm = GEMM(M=ROWS, K=k, N=D, **ACCURATE)
        tolerance = gemm.tolerance()
        bound = tolerance.bound(weights, v_k)
        want = gemm.reference(weights, v_k)
        verdict = verify_buffer(got, "C", want, tolerance, bound=bound)
        assert verdict, f"n={n}: {verdict.detail}"


@pytest.mark.supported_devices("npu2")
def test_an_xclbin_refuses_a_bound_on_k():
    class Attend(iron.Graph):
        def body(self, a, b, *, n: Scratchpad[np.int32]):
            return GEMM(a[:, :n], b[:n])

    with pytest.raises(ValueError, match="a per-call bound on K needs a full ELF"):
        Attend().compile(a=(ROWS, SEQ), b=(SEQ, D), boundaries=iron.each_step)
