# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(input_length: int, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    input_a = torch.rand(input_length, dtype=dtype_torch) * val_range
    input_b = torch.rand(input_length, dtype=dtype_torch) * val_range
    output = input_a * input_b
    return {"A": input_a, "B": input_b, "C": output}
