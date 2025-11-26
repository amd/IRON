# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Golden reference generator for tanh operator."""

import torch
from golden_model_lib import torch_dtype_map


def generate_golden_reference(input_length: int, dtype='bf16', seed=42):
    """
    Generate golden reference data for tanh.
    
    Returns:
        dict: Dictionary with "input" and "output" tensors (and possibly more for multi-input ops)
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(input_length, dtype=torch_dtype_map[dtype]) * val_range
    output_tensor = torch.nn.functional.tanh(input_tensor)
    return {"input": input_tensor, "output": output_tensor}
