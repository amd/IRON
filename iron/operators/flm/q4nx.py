# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The q4nx weight format that FastFlowLM quantizes Gemma 4 into.

A block holds M_TILE out-features by K_TILE in-features: bf16 scales, then
bf16 minima, one each per GROUP in-features of an out-feature, then 4-bit
codes. A weight is ``min + scale * code``.
"""

import numpy as np
from ml_dtypes import bfloat16

M_TILE, K_TILE, GROUP = 32, 256, 32

BITS_PER_WEIGHT = 4 + 2 * 16 // GROUP
BLOCK_BYTES = M_TILE * K_TILE * BITS_PER_WEIGHT // 8


def packed_bytes(n_weights: int) -> int:
    """Bytes holding n_weights in q4nx packing."""
    return n_weights * BITS_PER_WEIGHT // 8


def unpack(grid):
    """Return a weight's codes ``(rows, cols)`` uint8 and its scales/minima ``(rows, cols // GROUP)`` float32.

    From blocks laid out as a ``(rows // M_TILE, cols // K_TILE)`` grid:
    each block stores scales then minima at ``[k // GROUP, m]`` and codes
    at ``[m // 16, k, m % 16]``, the lower index in a byte's low nibble.
    """
    grid = np.asarray(grid, np.uint8)
    nb_r, nb_c = grid.shape[:2]
    b = grid.reshape(-1, BLOCK_BYTES)
    groups = K_TILE // GROUP
    params = b[:, : 4 * groups * M_TILE].copy().view(bfloat16).astype(np.float32)
    scales, mins = params.reshape(-1, 2, groups, M_TILE).transpose(1, 0, 3, 2)
    packed = b[:, 4 * groups * M_TILE :]
    codes = np.empty((len(b), M_TILE * K_TILE), np.uint8)
    codes[:, 0::2], codes[:, 1::2] = packed & 15, packed >> 4
    codes = codes.reshape(-1, M_TILE // 16, K_TILE, 16).transpose(0, 1, 3, 2)
    return tuple(
        part.reshape(nb_r, nb_c, M_TILE, -1)
        .transpose(0, 2, 1, 3)
        .reshape(nb_r * M_TILE, -1)
        for part in (codes, scales, mins)
    )


def dequantize(grid):
    """Return the ``(rows, cols)`` float64 weights of a grid of blocks, as ``unpack``'s."""
    codes, scales, mins = unpack(grid)
    group = np.arange(codes.shape[1]) // GROUP
    w = scales.astype(np.float64)[:, group]
    w *= codes
    w += mins[:, group]
    return w
