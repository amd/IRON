# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for Reduction Operations

Supports: sum, mean, max, min along specified dimensions
"""

import torch
from typing import Literal


ReductionOp = Literal["sum", "mean", "max", "min"]


def reduction_cpu(
    input: torch.Tensor,
    dim: int = -1,
    keepdim: bool = False,
    reduction_op: ReductionOp = "sum",
) -> torch.Tensor:
    """
    CPU reference implementation of reduction operation.

    Args:
        input: Input tensor of any shape
        dim: Dimension to reduce along (default: -1, the last dimension)
        keepdim: Whether to keep the reduced dimension as size 1
        reduction_op: Type of reduction: "sum", "mean", "max", or "min"

    Returns:
        Reduced tensor
    """
    if reduction_op == "sum":
        result = torch.sum(input, dim=dim, keepdim=keepdim)
    elif reduction_op == "mean":
        result = torch.mean(input, dim=dim, keepdim=keepdim)
    elif reduction_op == "max":
        result = torch.max(input, dim=dim, keepdim=keepdim)[0]
    elif reduction_op == "min":
        result = torch.min(input, dim=dim, keepdim=keepdim)[0]
    else:
        raise ValueError(f"Unknown reduction op: {reduction_op}")

    return result


def generate_golden_reference(
    input_shape: tuple,
    dim: int = -1,
    reduction_op: ReductionOp = "sum",
    dtype=torch.bfloat16,
    seed: int = 42,
):
    """
    Generate golden reference data for testing.

    Args:
        input_shape: Shape of input tensor
        dim: Dimension to reduce along
        reduction_op: Type of reduction
        dtype: Data type for tensors
        seed: Random seed for reproducibility

    Returns:
        Dictionary with input tensor and expected output
    """
    torch.manual_seed(seed)

    # Create random input
    if dtype == torch.bfloat16:
        # For bf16, create in fp32 then convert
        input_tensor = torch.randn(input_shape, dtype=torch.float32) * 2.0
        input_tensor = input_tensor.to(dtype)
    else:
        input_tensor = torch.randn(input_shape, dtype=dtype) * 2.0

    # Compute expected output
    expected_output = reduction_cpu(input_tensor, dim=dim, keepdim=False, reduction_op=reduction_op)

    return {
        "input": input_tensor,
        "output": expected_output,
        "dim": dim,
        "reduction_op": reduction_op,
    }


if __name__ == "__main__":
    # Quick test
    test_shape = (4, 8, 64)
    golden = generate_golden_reference(test_shape, dim=-1, reduction_op="sum")

    print(f"Input shape: {golden['input'].shape}")
    print(f"Output shape: {golden['output'].shape}")
    print(f"Reduction op: {golden['reduction_op']}")
    print(f"Dim: {golden['dim']}")
    print(f"Input dtype: {golden['input'].dtype}")
    print(f"Output dtype: {golden['output'].dtype}")
