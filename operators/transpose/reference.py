# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Golden reference generator for transpose operator."""

import torch
from golden_model_lib import torch_dtype_map


def generate_golden_reference(rows: int, cols: int, dtype='bf16', seed=42):
    """
    Generate golden reference data for transpose.
    
    Returns:
        dict: Dictionary with "input" and "output" tensors (and possibly more for multi-input ops)
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    output_tensor = torch.transpose(input_tensor, 0, 1)
    return {"input": input_tensor, "output": output_tensor}
