# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np


def generate_golden_reference(input_length, tile_size, group_size):
    """Generate test data and reference output for i32 -> bf16 dequantization.

    Simulates the output of an INT8 GEMM: generates random int32 values
    in a realistic accumulator range, with per-group bf16 scale factors.
    The reference output is: bf16(int32_val * scale).
    """
    torch.manual_seed(42)

    if input_length % tile_size != 0:
        raise ValueError("Input length must be a multiple of tile size.")
    if tile_size % group_size != 0:
        raise ValueError("Tile size must be a multiple of group size.")

    num_groups = input_length // group_size

    # Generate int32 values in realistic INT8 GEMM accumulator range
    i32_values = torch.randint(-100000, 100001, (input_length,), dtype=torch.int32)

    # Generate per-group scale factors in a realistic range
    # Combined scale = scale_activations * scale_weights
    scales = (0.0001 + 0.01 * torch.rand(num_groups, dtype=torch.float32)).to(
        torch.bfloat16
    )

    # Compute reference output: float(i32) * scale -> bf16
    output = torch.zeros(input_length, dtype=torch.bfloat16)
    for g in range(num_groups):
        start = g * group_size
        end = start + group_size
        output[start:end] = (
            i32_values[start:end].to(torch.float32) * scales[g].to(torch.float32)
        ).to(torch.bfloat16)

    # Pack input buffer as uint8: per-tile layout of int32 data followed by scale factors
    num_tiles = input_length // tile_size
    scales_per_tile = tile_size // group_size
    tile_input_bytes = tile_size * 4 + scales_per_tile * 2

    packed_input = np.zeros(num_tiles * tile_input_bytes, dtype=np.uint8)
    for t in range(num_tiles):
        tile_start = t * tile_size
        tile_end = tile_start + tile_size
        byte_offset = t * tile_input_bytes

        # Pack int32 data as bytes
        i32_bytes = i32_values[tile_start:tile_end].numpy().view(np.uint8)
        packed_input[byte_offset : byte_offset + tile_size * 4] = i32_bytes

        # Pack bf16 scale factors as bytes
        scale_start = t * scales_per_tile
        scale_end = scale_start + scales_per_tile
        scale_bytes = (
            scales[scale_start:scale_end].view(torch.uint16).numpy().view(np.uint8)
        )
        packed_input[byte_offset + tile_size * 4 : byte_offset + tile_input_bytes] = (
            scale_bytes
        )

    return {
        "input": torch.from_numpy(packed_input),
        "output": output,
    }
