# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The q4nx weight format that FastFlowLM quantizes Gemma 4 into.

A block holds M_TILE out-features by K_TILE in-features: bf16 scales, then
bf16 minima, one each per GROUP in-features of an out-feature, then 4-bit
codes. A weight is ``min + scale * code``.
"""

import numpy as np

M_TILE, K_TILE, GROUP = 32, 256, 32

BITS_PER_WEIGHT = 4 + 2 * 16 // GROUP
BLOCK_BYTES = M_TILE * K_TILE * BITS_PER_WEIGHT // 8


def packed_bytes(n_weights: int) -> int:
    """Bytes holding n_weights in q4nx packing."""
    return n_weights * BITS_PER_WEIGHT // 8


def bf16_to_f32(u16):
    """bf16 bit patterns to their float32 values."""
    return (np.asarray(u16).astype(np.uint32) << 16).view(np.float32)
