# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(input_length: int, scalar=3.0, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    A = torch.rand(input_length, dtype=dtype_torch) * val_range
    B = torch.rand(input_length, dtype=dtype_torch) * val_range
    s = torch.tensor(scalar, dtype=dtype_torch)

    # Generate golden outputs
    C = s * A + B

    return {
        "A": A,
        "B": B,
        "C": C,
    }
