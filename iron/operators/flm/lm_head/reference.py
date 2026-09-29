# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for :class:`iron.operators.flm.LMHead`, in float64.

The device normalizes the token in bfloat16, narrows each 32-column dot
product to bfloat16 and applies the softcap in bfloat16, so the two agree to a
tolerance, not bit for bit.
"""

import numpy as np

from iron.operators.flm.lm_head.design import BLOCK_BYTES, GROUP, K_TILE, M_TILE


def _bf16_to_f64(words):
    return (np.asarray(words, np.uint16).astype(np.uint32) << 16).view(np.float32)


def dequantize_block(block):
    """One q4nx block to its (M_TILE, K_TILE) weights.

    Bf16 scales, then bf16 minima, both indexed ``[k // GROUP, m]``, then 4-bit
    codes, low nibble first, indexed ``[m // 16, k // 32, k % 32, m % 16]``.
    A weight is ``min + scale * code``.
    """
    groups = K_TILE // GROUP
    params = _bf16_to_f64(np.frombuffer(block[: 4 * groups * M_TILE], "<u2"))
    scales, mins = params.reshape(2, groups, M_TILE).astype(np.float64)
    packed = np.frombuffer(block[4 * groups * M_TILE :], np.uint8)
    codes = np.empty(M_TILE * K_TILE, np.float64)
    codes[0::2], codes[1::2] = packed & 15, packed >> 4
    codes = codes.reshape(M_TILE // 16, K_TILE // 32, 32, 16)
    codes = codes.transpose(0, 3, 1, 2).reshape(M_TILE, K_TILE)
    k_group = np.arange(K_TILE) // GROUP
    return mins[k_group].T + scales[k_group].T * codes


def dequantize(w, dim, vocab, cols, rows):
    """The whole q4nx vocabulary buffer to its (vocab, dim) weights.

    Out-feature ``n`` is ``((round * cols + col) * rows + row) * M_TILE + m``,
    and its k-th block sits at block index
    ``((round * cols + col) * k_blocks + k) * rows + row``.
    """
    w = np.asarray(w).view(np.uint8)
    k_blocks = dim // K_TILE
    out = np.empty((vocab, dim), np.float64)
    for index in range(vocab // M_TILE * k_blocks):
        rows_k, row = divmod(index, rows)
        slice_, k = divmod(rows_k, k_blocks)
        n0 = (slice_ * rows + row) * M_TILE
        block = w[index * BLOCK_BYTES : (index + 1) * BLOCK_BYTES]
        out[n0 : n0 + M_TILE, k * K_TILE : (k + 1) * K_TILE] = dequantize_block(block)
    return out


def reference(weights, x, softcap, eps=1e-6):
    """Softcapped logits of the RMS-normalized token.

    ``weights`` is ``dequantize``'s (vocab, dim) matrix, ``x`` the token
    followed by its RMS weight.
    """
    x = np.asarray(x, np.float64)
    dim = weights.shape[1]
    token, rms_w = x[:dim], x[dim : 2 * dim]
    normed = token / np.sqrt(np.mean(token**2) + eps) * rms_w
    return softcap * np.tanh(weights @ normed / softcap)
