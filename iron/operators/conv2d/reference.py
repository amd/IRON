# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for 2D Convolution

Supports standard 2D convolution with configurable:
- kernel_size
- stride
- padding
- dilation
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

    # Create input tensor
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

    # Compute expected output
    expected_output = conv2d_cpu(
        input=input_tensor,
        weight=weight_tensor,
        bias=bias_tensor,
        stride=stride,
        padding=padding,
        dilation=dilation,
        groups=groups,
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
