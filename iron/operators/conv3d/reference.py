# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for 3D Convolution

Supports standard 3D convolution with configurable:
- kernel_size (t, h, w)
- stride (t, h, w)
- padding (t, h, w)
- dilation (t, h, w)
- groups (including depthwise convolution)

Input/Output format: (N, C, T, H, W) where:
- N = Batch
- C = Channels
- T = Temporal/Depth
- H = Height
- W = Width
"""

import torch
import torch.nn.functional as F
from typing import Tuple, Union


def conv3d_cpu(
    input: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor = None,
    stride: Union[int, Tuple[int, int, int]] = 1,
    padding: Union[int, Tuple[int, int, int]] = 0,
    dilation: Union[int, Tuple[int, int, int]] = 1,
    groups: int = 1,
) -> torch.Tensor:
    """
    CPU reference implementation of 3D convolution.

    This is the authoritative golden math reference (torch F.conv3d) used to
    validate the AIE implementation (bf16 vectorized kernels + MLIR dataflow).
    Any mismatch beyond tolerance in test indicates a real bug in op/design/kernel.

    Args:
        input: Input tensor of shape (N, C_in, T_in, H_in, W_in)
        weight: Weight tensor of shape (C_out, C_in/groups, kT, kH, kW)
        bias: Optional bias tensor of shape (C_out,)
        stride: Stride of the convolution (default: 1)
        padding: Zero padding added to both sides of input (default: 0)
        dilation: Spacing between kernel elements (default: 1)
        groups: Number of blocked connections from input to output channels (default: 1)

    Returns:
        Convolved output tensor of shape (N, C_out, T_out, H_out, W_out)
    """
    output = F.conv3d(
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
    in_t: int = 16,
    in_h: int = 32,
    in_w: int = 32,
    out_channels: int = 16,
    kernel_size: Union[int, Tuple[int, int, int]] = 3,
    stride: Union[int, Tuple[int, int, int]] = 1,
    padding: Union[int, Tuple[int, int, int]] = 0,
    dilation: Union[int, Tuple[int, int, int]] = 1,
    groups: int = 1,
    use_bias: bool = True,
    dtype: torch.dtype = torch.bfloat16,
    seed: int = 42,
):
    """
    Generate golden reference data for testing conv3d.

    Args:
        batch_size: Batch size (N)
        in_channels: Number of input channels (C_in)
        in_t: Input temporal dimension (T_in)
        in_h: Input height (H_in)
        in_w: Input width (W_in)
        out_channels: Number of output channels (C_out)
        kernel_size: Size of the convolving kernel (kT, kH, kW)
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
        kernel_size = (kernel_size, kernel_size, kernel_size)
    if isinstance(stride, int):
        stride = (stride, stride, stride)
    if isinstance(padding, int):
        padding = (padding, padding, padding)
    if isinstance(dilation, int):
        dilation = (dilation, dilation, dilation)

    # Validate groups
    assert in_channels % groups == 0, "in_channels must be divisible by groups"
    assert out_channels % groups == 0, "out_channels must be divisible by groups"

    # Compute expected output spatial dims using the reference formula (self-check)
    # This validates both our formula and that F.conv3d produces matching shape.
    # Formula: out = floor( (in + 2*pad - dil*(k-1) - 1) / s ) + 1
    out_t = calculate_output_dim(
        in_t, kernel_size[0], stride[0], padding[0], dilation[0]
    )
    out_h = calculate_output_dim(
        in_h, kernel_size[1], stride[1], padding[1], dilation[1]
    )
    out_w = calculate_output_dim(
        in_w, kernel_size[2], stride[2], padding[2], dilation[2]
    )

    # Create input tensor - direct in target dtype (modern main-tree pattern).
    # *2.0 scaling ensures good dynamic range for bf16 ( ~7-8 bit mantissa)
    # so accumulated MAC errors are measurable and test is sensitive to bugs.
    if dtype == torch.bfloat16:
        input_tensor = (
            torch.randn(batch_size, in_channels, in_t, in_h, in_w, dtype=dtype) * 2.0
        )
    else:
        input_tensor = (
            torch.randn(batch_size, in_channels, in_t, in_h, in_w, dtype=dtype) * 2.0
        )

    # Create weight tensor
    weight_shape = (
        out_channels,
        in_channels // groups,
        kernel_size[0],
        kernel_size[1],
        kernel_size[2],
    )
    if dtype == torch.bfloat16:
        weight_tensor = torch.randn(weight_shape, dtype=dtype) * 2.0
    else:
        weight_tensor = torch.randn(weight_shape, dtype=dtype) * 2.0

    # Create bias tensor (if used)
    bias_tensor = None
    if use_bias:
        if dtype == torch.bfloat16:
            bias_tensor = torch.randn(out_channels, dtype=dtype) * 2.0
        else:
            bias_tensor = torch.randn(out_channels, dtype=dtype) * 2.0

    # Compute expected output via authoritative CPU path
    expected_output = conv3d_cpu(
        input=input_tensor,
        weight=weight_tensor,
        bias=bias_tensor,
        stride=stride,
        padding=padding,
        dilation=dilation,
        groups=groups,
    )

    # Self-validation: F.conv3d output shape must match our dim formula exactly.
    # Catches any divergence in padding/stride/dilation math between test ref and op.
    computed_shape = (batch_size, out_channels, out_t, out_h, out_w)
    assert (
        expected_output.shape == computed_shape
    ), f"Golden shape mismatch: F.conv3d gave {expected_output.shape}, formula gave {computed_shape}"

    return {
        "input": input_tensor,
        "weight": weight_tensor,
        "bias": bias_tensor,
        "output": expected_output,
        "config": {
            "batch_size": batch_size,
            "in_channels": in_channels,
            "in_t": in_t,
            "in_h": in_h,
            "in_w": in_w,
            "out_channels": out_channels,
            "kernel_size": kernel_size,
            "stride": stride,
            "padding": padding,
            "dilation": dilation,
            "groups": groups,
            "use_bias": use_bias,
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
    Calculate output dimension for 3D convolution (exact match to op.py and torch).

    Formula (dilation-aware):
    output = floor( (input + 2*padding - dilation*(kernel-1) - 1) / stride + 1 )

    Used in generate_golden_reference for self-validation of shapes against F.conv3d.
    This makes the CPU reference path robust and able to catch formula bugs early.
    """
    return (input_dim + 2 * padding - dilation * (kernel_dim - 1) - 1) // stride + 1


if __name__ == "__main__":
    # Quick test with simple configuration
    print("Testing Conv3D CPU Reference Implementation...")

    # Test 1: Basic 3x3x3 convolution
    golden = generate_golden_reference(
        batch_size=1,
        in_channels=3,
        in_t=8,
        in_h=16,
        in_w=16,
        out_channels=16,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
    )

    print(f"\nTest 1: Basic 3x3x3 Conv")
    print(f"  Input shape: {golden['input'].shape}")
    print(f"  Weight shape: {golden['weight'].shape}")
    print(f"  Output shape: {golden['output'].shape}")
    print(f"  Config: {golden['config']}")

    # Test 2: Depthwise convolution
    golden_dw = generate_golden_reference(
        batch_size=1,
        in_channels=16,
        in_t=8,
        in_h=16,
        in_w=16,
        out_channels=16,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=16,  # Depthwise
    )

    print(f"\nTest 2: Depthwise 3x3x3 Conv")
    print(f"  Input shape: {golden_dw['input'].shape}")
    print(f"  Weight shape: {golden_dw['weight'].shape}")
    print(f"  Output shape: {golden_dw['output'].shape}")
    print(f"  Groups: {golden_dw['config']['groups']}")

    # Test 3: Strided convolution
    golden_stride = generate_golden_reference(
        batch_size=1,
        in_channels=3,
        in_t=16,
        in_h=32,
        in_w=32,
        out_channels=32,
        kernel_size=3,
        stride=2,
        padding=1,
        groups=1,
    )

    print(f"\nTest 3: Strided 3x3x3 Conv (stride=2)")
    print(f"  Input shape: {golden_stride['input'].shape}")
    print(f"  Output shape: {golden_stride['output'].shape}")
    print(f"  Config: {golden_stride['config']}")

    # Test 4: Pointwise convolution (1x1x1) - for compute primitive use
    golden_pw = generate_golden_reference(
        batch_size=1,
        in_channels=64,
        in_t=4,
        in_h=8,
        in_w=8,
        out_channels=128,
        kernel_size=1,
        stride=1,
        padding=0,
        groups=1,
    )

    print(f"\nTest 4: Pointwise 1x1x1 Conv (Linear layer equivalent)")
    print(f"  Input shape: {golden_pw['input'].shape}")
    print(f"  Weight shape: {golden_pw['weight'].shape}")
    print(f"  Output shape: {golden_pw['output'].shape}")
    print(f"  Config: {golden_pw['config']}")

    print("\nAll tests passed!")
