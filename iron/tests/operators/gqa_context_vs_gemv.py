#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GQAContext against the context path it replaces in decode, on a device.

Decode computed each head's attention context by repeating the value cache
per head, transposing it, and a batched GEMV over the transpose; GQAContext
reads the cache in place and must give the same bits. Its declared cases
check it against an IEEE float32 model of its order on non-negative data.
With mixed signs the core's float adder departs from IEEE on some
cancelling adds, and the model then misses an output bit now and then; the
GEMV runs on the same adder in the same order, so this compares the two on
the device, at the decode shape, on what decode feeds them: a cache of
signed values and softmax rows masked to the positions so far.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.operators.gemv import GEMV
from iron.operators.gqa_context import GQAContext
from iron.operators.repeat import Repeat
from iron.operators.transpose import Transpose

# Llama 3.2 1B decode: 8 KV groups of 4 heads, head_dim 64, 2048 positions.
G, H, D, L = 8, 32, 64, 2048


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


class Before(iron.Graph):
    def body(self, values, weights):
        return GEMV(Transpose(Repeat(values, repeat=H // G)), weights)


class After(iron.Graph):
    def body(self, values, weights):
        return GQAContext(values, weights.reshape(G, H // G, L))


def _weights(rng, valid: int) -> np.ndarray:
    """Softmax rows over the first ``valid`` positions, zero after them."""
    scores = rng.normal(0.0, 3.0, (H, L)).astype(np.float32)
    scores[:, valid:] = -np.inf
    e = np.exp(scores - scores.max(axis=1, keepdims=True))
    return (e / e.sum(axis=1, keepdims=True)).astype(bfloat16)


@pytest.mark.supported_devices("npu2")
def test_gqa_context_is_the_repeat_transpose_gemv_bit_for_bit(npu_runtime):
    shapes = dict(values=(G, L, D), weights=(H, L))
    before = Before().compile(**shapes)
    after = After().compile(**shapes)
    rng = np.random.default_rng(7)
    failures = []
    for valid in (1, 2, 37, 64, 65, 500, 1999, L):
        values = rng.normal(0.0, 1.0, (G, L, D)).astype(bfloat16)
        weights = _weights(rng, valid)
        want = np.asarray(before(values, weights)).reshape(H, D).view(np.int16)
        got = np.asarray(after(values, weights)).reshape(H, D).view(np.int16)
        wrong = np.argwhere(got != want)
        if len(wrong):
            failures.append(
                f"{valid} positions: {len(wrong)} differ, first {wrong[:4]}"
            )
    assert not failures, "\n".join(failures)
