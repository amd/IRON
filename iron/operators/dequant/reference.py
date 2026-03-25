# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def generate_golden_reference(input_length, tile_size, group_size):
    torch.manual_seed(42)

    if input_length % tile_size != 0:
        raise ValueError("Input length must be a multiple of tile size.")
    if tile_size % group_size != 0:
        raise ValueError("Tile size must be a multiple of group size.")

    num_tiles = input_length // tile_size
    num_scale_factors = tile_size // group_size
    scale_size = num_scale_factors * 2  # Total bytes (uint8 elements) for scale factors
    per_tile_size = tile_size // 2
    per_tile_bytes = (
        scale_size + per_tile_size
    )  # Total bytes (uint8 elements) after processing each tile
    val_range = 3.75  # Values in [0, 3.75)

    # Generate golden output with uniform distribution between 0 and val_range
    # This output will be quantized to be used as the input
    A = (
        torch.rand(num_tiles * num_scale_factors, group_size, dtype=torch.bfloat16)
        * val_range
    )

    # Generate scale factors in [0.25, 1) for each tile
    # The quantized values will thus be within [0,15], which is the range of int4
    # Zero points for each tile are fixed to 0 since the kernel only uses the scale factors
    r1, r2 = 1 / val_range, 1
    scales = r1 + (r2 - r1) * torch.rand(
        num_tiles * num_scale_factors, dtype=torch.bfloat16
    )
    zero_points = torch.zeros(num_tiles * num_scale_factors, dtype=torch.bfloat16)

    A = torch.quantize_per_channel(
        A.to(torch.float32),
        scales=scales.to(torch.float32),
        zero_points=zero_points.to(torch.float32),
        axis=0,
        dtype=torch.quint8,
    )
    B = torch.dequantize(A)

    # Convert A from a quantized tensor type to regular tensor type for data packing
    # We do the data packing here instead of the host to show how the data would need to be
    # manipulated from a PyTorch standpoint in order to use the dequant kernel.
    A = A.int_repr()

    # Concatenate the bottom four bits of every two elements across the tiles in A to generate
    # an 8-bit value (little endian order). This is because there's no native 4-bit datatype in C++.
    # At the end of each tile, concatenate the bf16 scale factor, which comes out to two int8 values.
    A_concat = torch.zeros(num_tiles, per_tile_bytes, dtype=torch.uint8)
    for i in range(num_tiles):
        for j in range(num_scale_factors):
            for k in range(group_size // 2):
                A_concat[i, j * (group_size // 2) + k] = torch.bitwise_or(
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k], 0x0F),
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k + 1], 0x0F)
                    * 2**4,
                )
        for j in range(num_scale_factors):
            A_concat[i, per_tile_size + 2 * j] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.uint16), 0xFF
            )
            # Extract high byte (bits 15-8) of the bfloat16 bit pattern.
            # View as int16 (same width), promote to int32 for bitwise_right_shift
            # support, shift right 8, then mask to 8 bits. The & 0xFF also
            # handles sign-extension from int32 arithmetic right shift.
            A_concat[i, per_tile_size + 2 * j + 1] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.int16).to(torch.int32)
                >> 8,
                0xFF,
            )

    return {
        "input": A_concat,
        "output": B,
    }
