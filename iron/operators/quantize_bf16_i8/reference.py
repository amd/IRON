# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np


def generate_golden_reference(input_length, tile_size, group_size):
    """Generate test data and reference output for bf16 -> int8 quantization.

    Generates random bfloat16 values, computes per-group symmetric quantization
    to int8, and packs the output per-tile as [int8_data | bf16_scale_factors].
    """
    torch.manual_seed(42)

    if input_length % tile_size != 0:
        raise ValueError("Input length must be a multiple of tile size.")
    if tile_size % group_size != 0:
        raise ValueError("Tile size must be a multiple of group size.")

    num_groups = input_length // group_size

    # Generate random bf16 input (range similar to model activations)
    bf16_input = torch.randn(input_length, dtype=torch.bfloat16)

    # Per-group symmetric quantization
    i8_output = torch.zeros(input_length, dtype=torch.int8)
    scales = torch.zeros(num_groups, dtype=torch.bfloat16)

    for g in range(num_groups):
        start = g * group_size
        end = start + group_size
        group = bf16_input[start:end]

        max_abs = group.float().abs().max()
        if max_abs > 0:
            scale = (max_abs / 127.0).to(torch.bfloat16)
            inv_scale = 127.0 / max_abs.float()
            # Use round-half-away-from-zero to match AIE kernel rounding
            scaled = group.float().mul(inv_scale)
            quantized = torch.sign(scaled) * torch.floor(torch.abs(scaled) + 0.5)
            quantized = quantized.clamp(-128, 127)
        else:
            scale = torch.tensor(0.0, dtype=torch.bfloat16)
            quantized = torch.zeros(group_size, dtype=torch.float32)

        i8_output[start:end] = quantized.to(torch.int8)
        scales[g] = scale

    # Pack output per-tile: [i8_data | bf16_scale_factors] as uint8
    num_tiles = input_length // tile_size
    scales_per_tile = tile_size // group_size
    tile_output_bytes = tile_size + scales_per_tile * 2

    packed_output = np.zeros(num_tiles * tile_output_bytes, dtype=np.uint8)
    for t in range(num_tiles):
        tile_start = t * tile_size
        tile_end = tile_start + tile_size
        byte_offset = t * tile_output_bytes

        # Pack int8 data as bytes
        i8_bytes = i8_output[tile_start:tile_end].numpy().view(np.uint8)
        packed_output[byte_offset : byte_offset + tile_size] = i8_bytes

        # Pack bf16 scale factors as bytes
        scale_start = t * scales_per_tile
        scale_end = scale_start + scales_per_tile
        scale_bytes = (
            scales[scale_start:scale_end].view(torch.uint16).numpy().view(np.uint8)
        )
        packed_output[byte_offset + tile_size : byte_offset + tile_output_bytes] = (
            scale_bytes
        )

    return {
        "input": bf16_input,
        "output": torch.from_numpy(packed_output),
    }
