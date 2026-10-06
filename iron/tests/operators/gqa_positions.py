#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Grouped-query decode attention at a per-call context, on a device.

``GQAScores``, ``Softmax`` and ``GQAContext`` over ``(seq_len, groups,
head_dim)`` caches bounded to ``n`` positions, as decode on NPU1 runs them:
one compiled graph is driven across positions on both sides of a chunk and
a softmax block boundary, long ones before short ones, so a block a longer
call wrote must not leak into a shorter one. Each product is checked: the
scores against ``GQAScores.reference``, the weights against the softmax of
the device's own scores (and zero past ``n`` to the end of the block), the
context exactly against ``GQAContext``'s reference on the device's weights.
"""

import numpy as np
import pytest
from aie.iron.kernels import activation
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.gqa import GQAContext, GQAScores, reference
from iron.operators.softmax import Softmax

# Llama 3.2 1B decode: 8 KV groups of 4 heads, head_dim 64.
G, H, D, L = 8, 32, 64, 2048
POSITIONS = (L, 300, 1, 2047, 127, 128, 129, 1000, 1024, 1025, 64, 2)


NPU2 = pytest.mark.supported_devices("npu2")


@pytest.mark.parametrize(
    "boundaries,columns",
    [
        pytest.param(None, None, id="full_elf-widest", marks=NPU2),
        pytest.param(None, 4, id="full_elf-npu1_columns", marks=NPU2),
        pytest.param(
            iron.each_step,
            None,
            id="xclbin-widest",
            marks=pytest.mark.supported_devices("npu1", "npu2"),
        ),
        pytest.param(iron.each_step, 4, id="xclbin-npu1_columns", marks=NPU2),
    ],
)
def test_attention_follows_the_per_call_context(npu_runtime, boundaries, columns):
    class Attend(iron.Graph):
        def body(self, keys, values, q, *, n: Scratchpad[np.int32]):
            scores = GQAScores(keys[:n], q, num_aie_columns=columns)
            weights = Softmax(scores)
            ctx = GQAContext(values[:n], weights, num_aie_columns=columns)
            return scores, weights, ctx

    attend = Attend().compile(
        keys=(L, G, D), values=(L, G, D), q=(H, D), boundaries=boundaries
    )
    scores_tol = GQAScores(heads=H, groups=G, seq_len=L).tolerance()
    softmax_tol = Softmax(rows=H, cols=L).tolerance()
    block = Softmax(rows=H, cols=L, block=1024).block

    rng = np.random.default_rng(0)
    for n in POSITIONS:
        keys = rng.standard_normal((L, G, D)).astype(bfloat16)
        values = rng.uniform(0.0, 1.0, (L, G, D)).astype(bfloat16)
        q = (rng.standard_normal((H, D)) / 8).astype(bfloat16)
        got_s, got_w, got_c = attend(keys, values, q, n=n)
        got_s = np.asarray(got_s).reshape(H, L)
        got_w = np.asarray(got_w).reshape(H, L)
        got_c = np.asarray(got_c).reshape(H, D)

        want_s = GQAScores(heads=H, groups=G, seq_len=n).reference(keys[:n], q)
        verdict = verify_buffer(got_s[:, :n], "scores", want_s, scores_tol)
        assert verdict, f"n={n} scores: {verdict.detail}"

        end = -(-n // block) * block
        tail = got_w[:, n:end].view(np.uint16)
        assert not tail.any(), f"n={n}: {np.count_nonzero(tail)} weights past n not +0"
        want_w = activation.softmax_ref(got_s[:, :n], tile_size=n)
        verdict = verify_buffer(got_w[:, :n], "weights", want_w, softmax_tol)
        assert verdict, f"n={n} weights: {verdict.detail}"

        want_c = reference(values[:n], got_w[:, :n])
        wrong = np.argwhere(got_c.view(np.uint16) != want_c.view(np.uint16))
        assert not len(wrong), f"n={n} ctx: {len(wrong)} differ, first {wrong[:4]}"
