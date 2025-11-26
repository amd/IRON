# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Golden reference generator for rms_norm operator."""

import torch
from golden_model_lib import torch_dtype_map


def generate_golden_reference(rows: int, cols: int, dtype='bf16', seed=42):
    """
    Generate golden reference data for rms_norm.
    
    Returns:
        dict: Dictionary with tensors for inputs and outputs
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    rms = torch.sqrt(torch.mean(input_tensor**2, dim=-1, keepdim=True))
    output_tensor = input_tensor / (rms + 1e-8)
    return {"input": input_tensor, "output": output_tensor}
