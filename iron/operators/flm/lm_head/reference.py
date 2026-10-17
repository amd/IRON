# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for ``iron.operators.flm.LMHead``, in float64."""

import numpy as np

from iron.operators.flm import q4nx
from iron.operators.flm.q4nx import BLOCK_BYTES, GROUP, K_TILE, M_TILE


def dequantize(w, dim, vocab, cols, rows):
    """The whole q4nx vocabulary buffer to its (vocab, dim) weights.

    Out-feature ``n`` is ``((round * cols + col) * rows + row) * M_TILE + m``.
    Its k-th block has block index
    ``((round * cols + col) * k_blocks + k) * rows + row``.
    """
    k_blocks = dim // K_TILE
    n_blocks = vocab // M_TILE * k_blocks
    codes, scales, mins = q4nx.parts(
        np.asarray(w).view(np.uint8)[: n_blocks * BLOCK_BYTES]
    )
    k_group = np.arange(K_TILE) // GROUP
    blocks = (
        mins.astype(np.float64)[..., k_group]
        + scales.astype(np.float64)[..., k_group] * codes
    )
    out = np.empty((vocab, dim), np.float64)
    for index, block in enumerate(blocks):
        rows_k, row = divmod(index, rows)
        slice_, k = divmod(rows_k, k_blocks)
        n0 = (slice_ * rows + row) * M_TILE
        out[n0 : n0 + M_TILE, k * K_TILE : (k + 1) * K_TILE] = block
    return out


def reference(weights, x, softcap, eps=1e-6):
    """Softcapped logits of the RMS-normalized token.

    ``weights`` is the (vocab, dim) matrix from ``dequantize``. ``x`` has the
    layout of LMHead's X.
    """
    x = np.asarray(x, np.float64)
    dim = weights.shape[1]
    token, rms_w = x[:dim], x[dim : 2 * dim]
    normed = token / np.sqrt(np.mean(token**2) + eps) * rms_w
    return softcap * np.tanh(weights @ normed / softcap)
