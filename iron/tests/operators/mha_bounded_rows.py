#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MHA under a row bound with fewer valid rows than the bound, on a device.

A prompt runs MHA over ``rows`` (the bound, a multiple of what its pipelines
take at once) of which the first ``n`` are the prompt: ``s_q = s_kv = n``.
A query row past ``n`` attends over nothing, so its row sum is 0, and it must
come out 0, not ``0 * (1 / 0)``: a NaN there reaches the next layer's K and
V through the residual, and from there every valid row. The padding holds
whatever the step before left, so here it is random rather than zeros.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.mha import MHA

# Llama 3.2 1B's heads, at half its context; eight pipelines as its profile.
HEADS, KV_HEADS, D, SEQ, PIPELINES = 32, 8, 64, 1024, 8


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_rows_past_the_valid_length_are_zero(npu_runtime):
    class Attend(iron.Graph):
        def body(self, q, k, v, *, rows: Scratchpad[np.int32], n: Scratchpad[np.int32]):
            q, k, v = q[:rows], k[:rows], v[:rows]
            return MHA(
                q, k, v, heads_interleaved=True, s_q=n, s_kv=n, num_pipelines=PIPELINES
            )

    attend = Attend()

    rng = np.random.default_rng(0)
    q = rng.standard_normal((SEQ, HEADS, D)).astype(bfloat16)
    k = rng.standard_normal((SEQ, KV_HEADS, D)).astype(bfloat16)
    v = rng.standard_normal((SEQ, KV_HEADS, D)).astype(bfloat16)
    net = attend.compile(q=q.shape, k=k.shape, v=v.shape)
    reference = MHA(
        num_heads=HEADS, num_KV_heads=KV_HEADS, seq_len=SEQ, heads_interleaved=True
    )
    for rows, n in ((512, 13), (1024, 600)):
        o = np.asarray(net(q, k, v, rows=rows, n=n), dtype=np.float32)
        o = o.reshape(SEQ, HEADS, D)
        padding = o[n:rows]
        assert np.isfinite(padding).all(), f"{rows=} {n=}: non-finite padding rows"
        assert not padding.any(), f"{rows=} {n=}: padding rows are not zero"
        expected = reference.reference(q, k, v, s_q=n, s_kv=n)
        expected = np.asarray(expected, dtype=np.float32).reshape(SEQ, HEADS, D)
        errors = verify_buffer(
            o[:n],
            "O",
            expected[:n],
            tolerance=Tolerance.relative(0.04, 0.15, max_mismatch_frac=0.005),
        )
        assert not errors, f"{rows=} {n=}: {len(errors)} valid elements differ"
