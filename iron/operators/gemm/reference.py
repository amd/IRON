# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def generate_golden_reference(
    M: int,
    K: int,
    N: int,
    dtype="bf16",
    seed=42,
    b_col_maj=False,
    c_col_maj=False,
    partition_N=1,
):
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    input_a = torch.randn(M, K, dtype=dtype_torch) * val_range
    input_b_full = torch.rand(K, N, dtype=dtype_torch) * val_range
    output_full = torch.matmul(input_a, input_b_full)
    if False:
        # The following inputs are useful for debugging;
        # the A matrix becomes a matrix where each element encodes its row and column index,
        # and the B matrix is an identity matrix.
        col_digits = len(str(K - 1)) if K > 0 else 1
        factor = 10 ** (col_digits + 1)
        row_indices = torch.arange(M, dtype=torch.int64).unsqueeze(1)
        col_indices = torch.arange(K, dtype=torch.int64).unsqueeze(0)
        input_a = (row_indices * factor + col_indices).to(dtype=dtype_torch)
        input_b_full = torch.zeros(K, N, dtype=dtype_torch)
        diag_dim = min(K, N)
        input_b_full[:diag_dim, :diag_dim] = torch.eye(diag_dim, dtype=dtype_torch)
    if b_col_maj:
        input_b_full = input_b_full.T
    if c_col_maj:
        output_full = output_full.T

    # Create partitioned buffers for B
    input_b = []
    for i in range(partition_N):
        col_start = i * (N // partition_N)
        col_end = (i + 1) * (N // partition_N)
        if b_col_maj:
            input_b.append(input_b_full[col_start:col_end, :])
        else:
            input_b.append(input_b_full[:, col_start:col_end])

    # Create partitioned buffers for C (output)
    output = []
    for i in range(partition_N):
        col_start = i * (N // partition_N)
        col_end = (i + 1) * (N // partition_N)
        if c_col_maj:
            output.append(output_full[col_start:col_end, :])
        else:
            output.append(output_full[:, col_start:col_end])

    return {"input": input_a, "input_b": input_b, "output": output}
