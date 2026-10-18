# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for ``iron.operators.flm.LMHead``, in float64."""

import numpy as np

from iron.operators.flm import q4nx
from iron.operators.flm.q4nx import BLOCK_BYTES, K_TILE, M_TILE


def dequantize(w, dim, vocab, rows):
    """The whole q4nx vocabulary buffer to its (vocab, dim) weights.

    Out-feature ``n`` is ``(slice * rows + row) * M_TILE + m``, where slice
    ``round * cols + col`` is one core column's share of a round. Its k-th
    block has block index
    ``(slice * k_blocks + k) * rows + row``.
    """
    k_blocks = dim // K_TILE
    blocks = np.asarray(w).view(np.uint8)[
        : vocab * dim // (M_TILE * K_TILE) * BLOCK_BYTES
    ]
    grid = blocks.reshape(-1, k_blocks, rows, BLOCK_BYTES).transpose(0, 2, 1, 3)
    return q4nx.dequantize(grid.reshape(vocab // M_TILE, k_blocks, BLOCK_BYTES))


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
