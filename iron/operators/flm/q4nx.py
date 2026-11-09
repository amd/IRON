# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The q4nx weight format that FastFlowLM quantizes Gemma 4 into.

A block holds M_TILE out-features by K_TILE in-features: bf16 scales, then
bf16 minima, one each per GROUP in-features of an out-feature, then 4-bit
codes. A weight is ``min + scale * code``.
"""

import numpy as np
from aie.iron.kernels.quant import Q4NX_BLOCK_BYTES as BLOCK_BYTES
from aie.iron.kernels.quant import Q4NX_GROUP as GROUP
from aie.iron.kernels.quant import Q4NX_K_TILE as K_TILE
from aie.iron.kernels.quant import Q4NX_M_TILE as M_TILE
from aie.iron.kernels.quant import q4nx_unpack


def packed_bytes(n_weights: int) -> int:
    """Bytes holding n_weights in q4nx packing."""
    return n_weights * BLOCK_BYTES // (M_TILE * K_TILE)


def unpack(grid):
    """Return a weight's codes ``(rows, cols)`` uint8 and its scales/minima ``(rows, cols // GROUP)`` float32.

    From blocks laid out as a ``(rows // M_TILE, cols // K_TILE)`` grid:
    each block stores scales then minima at ``[k // GROUP, m]`` and codes
    at ``[m // 16, k, m % 16]``, the lower index in a byte's low nibble.
    """
    grid = np.asarray(grid, np.uint8)
    nb_r = grid.shape[0]
    codes, scales, mins = (
        part.transpose(0, 3, 1, 2).reshape(nb_r * M_TILE, -1)
        for part in q4nx_unpack(grid)
    )
    return codes, scales, mins


def dequantize(grid):
    """Return the ``(rows, cols)`` float64 weights of a grid of blocks, as ``unpack``'s."""
    codes, scales, mins = unpack(grid)
    group = np.arange(codes.shape[1]) // GROUP
    w = scales.astype(np.float64)[:, group]
    w *= codes
    w += mins[:, group]
    return w
