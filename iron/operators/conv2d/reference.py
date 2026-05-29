# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for 2D Convolution

This module is the single source of truth for golden reference data used by
Conv2D tests (test.py). It provides:

- conv2d_cpu: thin, faithful wrapper around torch.nn.functional.conv2d.
  Used identically for ALL golden generation passed to run_test (HW verification)
  and to the Python forward path. This ensures the CPU reference semantics
  match PyTorch exactly for the tested dtypes (primarily bfloat16).

- generate_golden_reference: produces deterministic (seeded) input/weight/bias
  tensors + the expected output computed via conv2d_cpu. Supports full
  coverage of bias/no-bias, depthwise, pointwise, strided, grouped cases.

The reference does NOT attempt low-level bf16 accumulation emulation (unlike
reduction ops) because Conv2D MAC accumulation order/precision on AIE is
vectorized and kernel-specific; instead, tolerances in tests account for
bf16 numerical sensitivity (see test.py for rationale).

Supports standard 2D convolution with configurable:
- kernel_size
- stride
- padding
- dilation (currently only 1 supported by AIE op)
- groups (including depthwise convolution)
"""

import torch
import torch.nn.functional as F
from typing import Tuple, Union


def conv2d_cpu(
    input: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor = None,
    stride: Union[int, Tuple[int, int]] = 1,
    padding: Union[int, Tuple[int, int]] = 0,
    dilation: Union[int, Tuple[int, int]] = 1,
    groups: int = 1,
) -> torch.Tensor:
    """
    CPU reference implementation of 2D convolution.

    This is a *thin, direct* wrapper around torch.nn.functional.conv2d using
    identical argument passing. It is the canonical definition of "correct"
    output for all golden data in test.py (both the metrics run_test path
    and the explicit forward batch>1 path).

    IMPORTANT FOR ACCURACY: Any change here affects every Conv2D test's
    expected values. It must remain a pure pass-through to F.conv2d.

    Args:
        input: Input tensor of shape (N, C_in, H_in, W_in)
        weight: Weight tensor of shape (C_out, C_in/groups, kH, kW)
        bias: Optional bias tensor of shape (C_out,)
        stride: Stride of the convolution (default: 1)
        padding: Zero padding added to both sides of input (default: 0)
        dilation: Spacing between kernel elements (default: 1)
        groups: Number of blocked connections from input to output channels (default: 1)

    Returns:
        Convolved output tensor of shape (N, C_out, H_out, W_out)
    """
    # Single source of truth: identical F.conv2d call used for golden
    # in generate_golden_reference for both CPU-path validation and HW.
    output = F.conv2d(
        input=input,
        weight=weight,
        bias=bias,
        stride=stride,
        padding=padding,
        dilation=dilation,
        groups=groups,
    )
    return output


def generate_golden_reference(
    batch_size: int = 1,
    in_channels: int = 3,
    in_height: int = 32,
    in_width: int = 32,
    out_channels: int = 16,
    kernel_size: Union[int, Tuple[int, int]] = 3,
    stride: Union[int, Tuple[int, int]] = 1,
    padding: Union[int, Tuple[int, int]] = 0,
    dilation: Union[int, Tuple[int, int]] = 1,
    groups: int = 1,
    use_bias: bool = True,
    dtype: torch.dtype = torch.bfloat16,
    seed: int = 42,
):
    """
    Generate golden reference data for testing conv2d.

    Deterministic via explicit torch.manual_seed(seed) at entry.
    Input/weight/bias creation for bf16 uses fp32 randn scaled then cast
    (best-practice for stable dynamic range in low-precision tests).

    The "output" is *always* produced by calling conv2d_cpu(...) which is
    the thin F.conv2d wrapper. This golden dict (input/weight/bias/output)
    is passed verbatim to run_test verification and forward() tests.

    This function + conv2d_cpu together define the CPU/reference accuracy
    contract for the entire Conv2D operator test suite.

    Args:
        batch_size: Batch size (N)
        in_channels: Number of input channels (C_in)
        in_height: Input height (H_in)
        in_width: Input width (W_in)
        out_channels: Number of output channels (C_out)
        kernel_size: Size of the convolving kernel (kH, kW)
        stride: Stride of the convolution
        padding: Zero padding added to input
        dilation: Spacing between kernel elements
        groups: Number of blocked connections
        use_bias: Whether to use bias
        dtype: Data type for tensors
        seed: Random seed for reproducibility

    Returns:
        Dictionary with input, weight, bias (if used), and expected output
    """
    torch.manual_seed(seed)

    # Normalize kernel_size, stride, padding, dilation to tuples
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if isinstance(stride, int):
        stride = (stride, stride)
    if isinstance(padding, int):
        padding = (padding, padding)
    if isinstance(dilation, int):
        dilation = (dilation, dilation)

    # Validate groups
    assert in_channels % groups == 0, "in_channels must be divisible by groups"
    assert out_channels % groups == 0, "out_channels must be divisible by groups"

    # Compute expected output spatial dimensions using the standard formula.
    # This cross-validates against F.conv2d and against the operator implementation.
    out_height = calculate_output_dim(
        in_height, kernel_size[0], stride[0], padding[0], dilation[0]
    )
    out_width = calculate_output_dim(
        in_width, kernel_size[1], stride[1], padding[1], dilation[1]
    )

    # Create input tensor (use fp32 intermediate for stable bf16 generation range)
    if dtype == torch.bfloat16:
        input_tensor = (
            torch.randn(
                batch_size, in_channels, in_height, in_width, dtype=torch.float32
            )
            * 2.0
        )
        input_tensor = input_tensor.to(dtype)
    else:
        input_tensor = (
            torch.randn(batch_size, in_channels, in_height, in_width, dtype=dtype) * 2.0
        )

    # Create weight tensor
    weight_shape = (out_channels, in_channels // groups, kernel_size[0], kernel_size[1])
    if dtype == torch.bfloat16:
        weight_tensor = torch.randn(weight_shape, dtype=torch.float32) * 2.0
        weight_tensor = weight_tensor.to(dtype)
    else:
        weight_tensor = torch.randn(weight_shape, dtype=dtype) * 2.0

    # Create bias tensor (if used)
    bias_tensor = None
    if use_bias:
        if dtype == torch.bfloat16:
            bias_tensor = torch.randn(out_channels, dtype=torch.float32) * 2.0
            bias_tensor = bias_tensor.to(dtype)
        else:
            bias_tensor = torch.randn(out_channels, dtype=dtype) * 2.0

    # Compute expected output using the canonical CPU reference (F.conv2d).
    # This ensures the golden matches PyTorch semantics for the given dtype (bf16 primary).
    expected_output = conv2d_cpu(
        input=input_tensor,
        weight=weight_tensor,
        bias=bias_tensor,
        stride=stride,
        padding=padding,
        dilation=dilation,
        groups=groups,
    )

    # Self-check: F.conv2d output shape must match the formula used by operator and calculate.
    assert (
        expected_output.shape[2] == out_height and expected_output.shape[3] == out_width
    ), (
        f"Output shape mismatch in golden ref: F.conv2d gave {expected_output.shape[2:]} "
        f"but formula gave ({out_height}, {out_width})"
    )

    return {
        "input": input_tensor,
        "weight": weight_tensor,
        "bias": bias_tensor,
        "output": expected_output,
        "config": {
            "batch_size": batch_size,
            "in_channels": in_channels,
            "in_height": in_height,
            "in_width": in_width,
            "out_channels": out_channels,
            "kernel_size": kernel_size,
            "stride": stride,
            "padding": padding,
            "dilation": dilation,
            "groups": groups,
            "use_bias": use_bias,
            "out_height": out_height,
            "out_width": out_width,
        },
    }


def calculate_output_dim(
    input_dim: int,
    kernel_dim: int,
    stride: int,
    padding: int,
    dilation: int,
) -> int:
    """
    Calculate output dimension for convolution.

    Formula:
    output = floor((input + 2*padding - dilation*(kernel-1) - 1) / stride + 1)
    """
    return (input_dim + 2 * padding - dilation * (kernel_dim - 1) - 1) // stride + 1


if __name__ == "__main__":
    # Quick test with simple configuration
    print("Testing Conv2D CPU Reference Implementation...")

    # Test 1: Basic 3x3 convolution
    golden = generate_golden_reference(
        batch_size=1,
        in_channels=3,
        in_height=32,
        in_width=32,
        out_channels=16,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
    )

    print(f"\nTest 1: Basic 3x3 Conv")
    print(f"  Input shape: {golden['input'].shape}")
    print(f"  Weight shape: {golden['weight'].shape}")
    print(f"  Output shape: {golden['output'].shape}")
    print(f"  Config: {golden['config']}")

    # Test 2: Depthwise convolution
    golden_dw = generate_golden_reference(
        batch_size=1,
        in_channels=16,
        in_height=32,
        in_width=32,
        out_channels=16,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=16,  # Depthwise
    )

    print(f"\nTest 2: Depthwise 3x3 Conv")
    print(f"  Input shape: {golden_dw['input'].shape}")
    print(f"  Weight shape: {golden_dw['weight'].shape}")
    print(f"  Output shape: {golden_dw['output'].shape}")
    print(f"  Groups: {golden_dw['config']['groups']}")

    # Test 3: Strided convolution
    golden_stride = generate_golden_reference(
        batch_size=1,
        in_channels=3,
        in_height=64,
        in_width=64,
        out_channels=32,
        kernel_size=3,
        stride=2,
        padding=1,
        groups=1,
    )

    print(f"\nTest 3: Strided 3x3 Conv (stride=2)")
    print(f"  Input shape: {golden_stride['input'].shape}")
    print(f"  Output shape: {golden_stride['output'].shape}")
    print(f"  Config: {golden_stride['config']}")

    print("\nAll tests passed!")
