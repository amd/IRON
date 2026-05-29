# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for Reduction Operations

Supports: sum, mean, max, min along specified dimensions
"""

import torch
import numpy as np
from typing import Literal

from iron.common.utils import torch_to_numpy, numpy_to_torch
from ml_dtypes import bfloat16 as bfloat16_np

ReductionOp = Literal["sum", "mean", "max", "min"]


def _emulate_bf16_reduction(
    input_tensor: torch.Tensor,
    dim: int = -1,
    reduction_op: ReductionOp = "sum",
    keepdim: bool = False,
) -> torch.Tensor:
    """
    Emulate AIE bf16 reduction semantics exactly using ml_dtypes bfloat16
    for accumulation. This ensures the golden reference matches the
    low-precision arithmetic performed by the AIE kernels (bf16 add/reduce
    for sum/mean; exact comparisons for max/min).

    Critical for test reliability: catches real kernel bugs rather than
    masking them behind higher-precision torch accum.
    """
    if input_tensor.dtype != torch.bfloat16:
        # Fall back for non-bf16
        if reduction_op == "sum":
            return torch.sum(input_tensor, dim=dim, keepdim=keepdim)
        elif reduction_op == "mean":
            return torch.mean(input_tensor, dim=dim, keepdim=keepdim)
        elif reduction_op == "max":
            return torch.max(input_tensor, dim=dim, keepdim=keepdim)[0]
        else:
            return torch.min(input_tensor, dim=dim, keepdim=keepdim)[0]

    np_in = torch_to_numpy(input_tensor)
    orig_ndim = np_in.ndim
    if dim < 0:
        dim = orig_ndim + dim

    # Move reduction dim to last for processing
    if dim != orig_ndim - 1:
        np_in = np.moveaxis(np_in, dim, -1)

    red_size = np_in.shape[-1]
    leading_shape = np_in.shape[:-1]

    flat_groups = np_in.reshape(-1, red_size)
    n_groups = flat_groups.shape[0]

    np_out = np.empty((n_groups,), dtype=bfloat16_np)

    for g in range(n_groups):
        group = flat_groups[g]
        if reduction_op == "sum":
            acc = bfloat16_np(0.0)
            for v in group:
                acc = acc + v  # exact bf16 addition
            np_out[g] = acc
        elif reduction_op == "mean":
            acc = bfloat16_np(0.0)
            for v in group:
                acc = acc + v
            np_out[g] = acc / bfloat16_np(float(red_size))
        elif reduction_op == "max":
            # Exact match to torch for comparisons; use native for speed
            m = group[0]
            for v in group[1:]:
                if v > m:
                    m = v
            np_out[g] = m
        elif reduction_op == "min":
            m = group[0]
            for v in group[1:]:
                if v < m:
                    m = v
            np_out[g] = m

    out = np_out.reshape(leading_shape)

    if keepdim:
        # Insert singleton at original dim position
        out = np.expand_dims(out, axis=dim)

    if dim != orig_ndim - 1 and not keepdim:
        # For non-last dim without keep, shape already correct after reshape
        pass

    return numpy_to_torch(out)


def reduction_cpu(
    input: torch.Tensor,
    dim: int = -1,
    keepdim: bool = False,
    reduction_op: ReductionOp = "sum",
) -> torch.Tensor:
    """
    CPU reference implementation of reduction operation.

    For bfloat16 + sum/mean, uses precise bf16 emulation to match AIE kernel
    arithmetic exactly. For max/min and other dtypes, uses torch which is
    semantically identical.

    This makes the reference trustworthy for validating the AIE implementation.
    """
    if reduction_op not in ("sum", "mean", "max", "min"):
        raise ValueError(f"Unknown reduction op: {reduction_op}")

    # Use emulation for bf16 sum/mean to match AIE exactly (accum in bf16)
    if input.dtype == torch.bfloat16 and reduction_op in ("sum", "mean"):
        return _emulate_bf16_reduction(
            input, dim=dim, reduction_op=reduction_op, keepdim=keepdim
        )

    if reduction_op == "sum":
        result = torch.sum(input, dim=dim, keepdim=keepdim)
    elif reduction_op == "mean":
        result = torch.mean(input, dim=dim, keepdim=keepdim)
    elif reduction_op == "max":
        result = torch.max(input, dim=dim, keepdim=keepdim)[0]
    else:  # min
        result = torch.min(input, dim=dim, keepdim=keepdim)[0]

    return result


def generate_golden_reference(
    input_shape: tuple,
    dim: int = -1,
    reduction_op: ReductionOp = "sum",
    dtype=torch.bfloat16,
    seed: int = 42,
    val_range: float = 4.0,
):
    """
    Generate golden reference data for testing. Follows modern patterns from
    other high-quality IRON operator tests (axpy, gemm, softmax, etc.).

    Uses torch_dtype_map when dtype specified as string for consistency.
    For bf16 inputs, the expected output for sum/mean is computed with
    precise bf16 emulation to match AIE kernel behavior.

    Args:
        input_shape: Shape of input tensor
        dim: Dimension to reduce along
        reduction_op: Type of reduction
        dtype: Data type (torch dtype or "bf16"/"f32" string)
        seed: Random seed for reproducibility
        val_range: Scaling for input data magnitude (higher exercises more bits)

    Returns:
        Dictionary with input tensor and expected output (faithful to AIE)
    """
    from iron.common.utils import torch_dtype_map

    torch.manual_seed(seed)

    if isinstance(dtype, str):
        dtype = torch_dtype_map.get(dtype, torch.bfloat16)

    # Create random input directly with target dtype (matches main tree patterns)
    input_tensor = torch.randn(input_shape, dtype=dtype) * val_range

    # Compute expected output using the accurate (emulated where needed) CPU ref
    expected_output = reduction_cpu(
        input_tensor, dim=dim, keepdim=False, reduction_op=reduction_op
    )

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
