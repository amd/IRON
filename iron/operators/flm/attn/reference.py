# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for :class:`iron.operators.flm.PrefillAttention`, in float32.

The device rounds the scores, the probabilities and the output to bfloat16, so
the two agree to a tolerance, not bit for bit.
"""

import numpy as np

from iron.operators.flm.attn.design import DH


def split_kv(kv, max_l, num_kv_heads):
    """K and V of a KV cache buffer, each shaped (max_l, num_kv_heads, DH)."""
    half = max_l * num_kv_heads * DH
    kv = np.asarray(kv, dtype=np.float32)
    return (
        kv[:half].reshape(max_l, num_kv_heads, DH),
        kv[half : 2 * half].reshape(max_l, num_kv_heads, DH),
    )


def reference(q, kv, L_begin, L_end, max_l, num_heads, num_kv_heads):
    """Attention of query tokens L_begin to L_end - 1 over the keys up to each.

    q holds one row of num_heads heads per query token, starting at L_begin.
    Returns the output in the same layout, (L_end - L_begin, num_heads, DH).
    The scores carry no 1/sqrt(DH) scale.
    """
    rows = L_end - L_begin
    q = np.asarray(q, dtype=np.float32)[: rows * num_heads * DH]
    q = q.reshape(rows, num_heads, DH)
    k, v = split_kv(kv, max_l, num_kv_heads)
    group = num_heads // num_kv_heads

    query_pos = L_begin + np.arange(rows)[:, None]
    visible = np.arange(L_end)[None, :] <= query_pos

    o = np.empty((rows, num_heads, DH), dtype=np.float32)
    for h in range(num_heads):
        g = h // group
        s = q[:, h] @ k[:L_end, g].T
        s = np.where(visible, s, -np.inf)
        p = np.exp(s - s.max(axis=1, keepdims=True))
        o[:, h] = (p / p.sum(axis=1, keepdims=True)) @ v[:L_end, g]
    return o
