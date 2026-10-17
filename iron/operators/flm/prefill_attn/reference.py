# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for ``iron.operators.flm.PrefillAttention`` and
``PrefillSlidingAttention``, in float32.
"""

import numpy as np


def reference(q, kv, L_begin, L_end, max_l, num_heads, num_kv_heads, dh, window=None):
    """Attention of query tokens L_begin to L_end - 1 over the keys up to each.

    Returns an array of shape (L_end - L_begin, num_heads, dh). The README
    gives the layout of q and kv.
    """
    rows = L_end - L_begin
    q = np.asarray(q, dtype=np.float32)[: rows * num_heads * dh]
    q = q.reshape(rows, num_heads, dh)
    half = max_l * num_kv_heads * dh
    kv = np.asarray(kv, dtype=np.float32)
    k = kv[:half].reshape(max_l, num_kv_heads, dh)
    v = kv[half : 2 * half].reshape(max_l, num_kv_heads, dh)
    group = num_heads // num_kv_heads

    query_pos = L_begin + np.arange(rows)[:, None]
    key_pos = np.arange(L_end)[None, :]
    visible = key_pos <= query_pos
    if window is not None:
        visible &= key_pos > query_pos - window

    o = np.empty((rows, num_heads, dh), dtype=np.float32)
    for h in range(num_heads):
        g = h // group
        s = q[:, h] @ k[:L_end, g].T
        s = np.where(visible, s, -np.inf)
        p = np.exp(s - s.max(axis=1, keepdims=True))
        o[:, h] = (p / p.sum(axis=1, keepdims=True)) @ v[:L_end, g]
    return o
