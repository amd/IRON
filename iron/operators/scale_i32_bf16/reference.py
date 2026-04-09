# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def generate_golden_reference(input_length, tile_size, num_aie_columns, num_channels):
    """Generate test data and golden reference for scale_i32_bf16 operator.

    Returns dict with:
        input_i32: flat int32 tensor (simulating GEMM output)
        scale: scalar float scale value
        scale_buffer: bf16 buffer with scale repeated (total_cores * 16)
        expected_output: flat bf16 tensor
    """
    total_cores = num_aie_columns * num_channels

    # Random int32 values in typical GEMM accumulator range
    input_i32 = torch.randint(-200000, 200000, (input_length,), dtype=torch.int32)

    # Random scale in typical range (scale_A * scale_W)
    scale = np.random.uniform(1e-6, 1e-3)

    # Scale buffer: same value repeated, 16 per core for DMA alignment
    scale_buffer = np.full(total_cores * 16, scale, dtype=np.float32).astype(bfloat16)

    # Reference computation: float(i32) * scale -> bf16
    # Use the bf16 scale value (after conversion) for the reference to match hardware
    scale_as_bf16 = float(bfloat16(np.float32(scale)))
    expected = (input_i32.float() * scale_as_bf16).to(torch.bfloat16)

    return {
        "input_i32": input_i32,
        "scale": scale,
        "scale_buffer": torch.from_numpy(scale_buffer.view(np.uint16)).view(
            torch.bfloat16
        ),
        "expected_output": expected,
    }
