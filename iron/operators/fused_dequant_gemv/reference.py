# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def quantize_and_pack(M, K, group_size=32, m_input=1, cols=4):
    """Generate quantized INT4 weights and pack for the fused dequant-GEMV kernel.

    Uses the same quantization scheme as the existing dequant operator
    (iron/operators/dequant/reference.py): unsigned INT4 values with per-group
    bf16 scale factors, zero-point fixed at 0.

    The DDR buffer is laid out per-tile, where each tile corresponds to
    ``m_input`` matrix rows.  Tiles for column 0 come first, then column 1,
    etc.  Within each tile the layout is:

        [m_input * K / 2 bytes]  packed uint4 weights (2 values per byte,
                                  low nibble first in little-endian order)
        [m_input * (K / group_size) * 2 bytes]  bf16 scale factors

    This is the exact layout that ``fused_dequant_matvec_bf16`` in the AIE
    kernel expects: the kernel computes ``scales = a_in + m * k / 2`` to find
    the scale-factor region.

    Args:
        M: Number of rows in the weight matrix.
        K: Number of columns in the weight matrix.
        group_size: Number of elements per quantization group (default 32).
        m_input: Number of rows per kernel tile invocation.
        cols: Number of AIE columns the work is split across.

    Returns:
        packed: numpy uint8 array with the complete packed DDR buffer.
        W_dequant: torch.bfloat16 (M, K) tensor of dequantized weights.
    """
    assert K % group_size == 0, "K must be a multiple of group_size"
    assert M % cols == 0, "M must be a multiple of cols"
    rows_per_col = M // cols
    assert rows_per_col % m_input == 0, "rows_per_col must be a multiple of m_input"

    num_groups_per_row = K // group_size
    val_range = 3.75
    r1, r2 = 1 / val_range, 1.0

    # Generate per-group scale factors in [r1, r2)
    total_groups = M * num_groups_per_row
    scales_flat = r1 + (r2 - r1) * torch.rand(total_groups, dtype=torch.bfloat16)
    zero_points = torch.zeros(total_groups, dtype=torch.bfloat16)

    # Generate random data in [0, val_range) shaped for per-group quantization
    W_grouped = torch.rand(total_groups, group_size, dtype=torch.bfloat16) * val_range

    # Quantize with PyTorch per-channel (per-group) quantization
    A_quant = torch.quantize_per_channel(
        W_grouped.to(torch.float32),
        scales=scales_flat.to(torch.float32),
        zero_points=zero_points.to(torch.float32),
        axis=0,
        dtype=torch.quint8,
    )
    W_dequant = torch.dequantize(A_quant).to(torch.bfloat16).reshape(M, K)
    A_int = A_quant.int_repr()  # (total_groups, group_size) with values in [0,15]

    # Now pack into the tile-based DDR layout.
    # Tile order: column 0 tiles first, then column 1, etc.
    packed_bytes_per_tile = m_input * K // 2 + m_input * num_groups_per_row * 2
    tiles_per_col = rows_per_col // m_input
    total_tiles = cols * tiles_per_col
    total_bytes = total_tiles * packed_bytes_per_tile

    packed = np.zeros(total_bytes, dtype=np.uint8)

    for col in range(cols):
        for tile_idx in range(tiles_per_col):
            # Global row range for this tile
            row_start = col * rows_per_col + tile_idx * m_input
            # Offset into the packed buffer
            flat_tile = col * tiles_per_col + tile_idx
            tile_offset = flat_tile * packed_bytes_per_tile

            # 1) Pack uint4 weights for m_input rows
            for r in range(m_input):
                global_row = row_start + r
                for grp in range(num_groups_per_row):
                    flat_grp = global_row * num_groups_per_row + grp
                    for k in range(group_size // 2):
                        val_lo = int(A_int[flat_grp, 2 * k].item()) & 0x0F
                        val_hi = int(A_int[flat_grp, 2 * k + 1].item()) & 0x0F
                        byte_idx = (
                            tile_offset + r * (K // 2) + grp * (group_size // 2) + k
                        )
                        packed[byte_idx] = val_lo | (val_hi << 4)

            # 2) Pack bf16 scale factors for m_input rows
            scale_region_start = tile_offset + m_input * K // 2
            for r in range(m_input):
                global_row = row_start + r
                for grp in range(num_groups_per_row):
                    flat_grp = global_row * num_groups_per_row + grp
                    sf_val = scales_flat[flat_grp]
                    sf_uint16 = sf_val.view(torch.uint16).item()
                    sf_offset = scale_region_start + (r * num_groups_per_row + grp) * 2
                    packed[sf_offset] = sf_uint16 & 0xFF
                    packed[sf_offset + 1] = (sf_uint16 >> 8) & 0xFF

    return packed, W_dequant


def generate_golden_reference(
    M=2048, K=2048, group_size=32, m_input=1, cols=4, seed=42
):
    """Generate golden reference for fused dequant-GEMV.

    Creates random weights, quantizes to INT4, packs into the tile-based
    DDR layout, and computes the reference matrix-vector product using
    the dequantized weights.

    Args:
        M: Number of rows in the weight matrix.
        K: Number of columns (== input vector length).
        group_size: Quantization group size.
        m_input: Number of rows per kernel tile invocation.
        cols: Number of AIE columns.
        seed: Random seed for reproducibility.

    Returns:
        dict with:
          packed_weights: numpy uint8 array (DDR buffer).
          x: torch.bfloat16 input vector of length K.
          output: torch.bfloat16 reference output of length M.
          W_dequant: torch.bfloat16 dequantized weight matrix.
    """
    torch.manual_seed(seed)

    # Generate random input vector
    val_range = 4
    x = torch.randn(K, dtype=torch.bfloat16) * val_range

    # Generate quantized + packed weights
    packed_weights, W_dequant = quantize_and_pack(M, K, group_size, m_input, cols)

    # Reference output: dequantized_weights @ x
    output = W_dequant @ x

    return {
        "packed_weights": packed_weights,
        "x": x,
        "output": output,
        "W_dequant": W_dequant,
    }
