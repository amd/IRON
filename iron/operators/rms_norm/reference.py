# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(
    rows: int, cols: int, dtype="bf16", seed=42, weighted=False
):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    rms = torch.sqrt(torch.mean(input_tensor**2, dim=-1, keepdim=True))
    output_tensor = input_tensor / (rms + 1e-5)

    if weighted:
        weights = torch.rand(cols, dtype=torch_dtype_map[dtype]) * val_range
        output_tensor = output_tensor * weights
        return {"input": input_tensor, "weight": weights, "output": output_tensor}
    else:
        return {"input": input_tensor, "output": output_tensor}
