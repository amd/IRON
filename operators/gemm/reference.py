# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Golden reference generator for gemm operator."""

import torch
from golden_model_lib import torch_dtype_map


def generate_golden_reference(M: int, K: int, N: int, dtype='bf16', seed=42, b_col_maj=False, c_col_maj=False):
    """
    Generate golden reference data for gemm.
    
    Returns:
        dict: Dictionary with tensors for inputs and outputs
    """
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    input_a = torch.randn(M, K, dtype=dtype_torch) * val_range
    input_b = torch.rand(K, N, dtype=dtype_torch) * val_range
    output = torch.matmul(input_a, input_b)
    if b_col_maj:
        input_b = input_b.T
    if c_col_maj:
        output = output.T
    return {"input": input_a, "input_b": input_b, "output": output}
