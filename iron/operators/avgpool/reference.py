# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for AveragePool Operator
"""

import torch
import torch.nn.functional as F
from typing import Union, Tuple


def avg_pool2d_cpu(
    x: torch.Tensor,
    kernel_size: Union[int, Tuple[int, int]],
    stride: Union[int, Tuple[int, int]],
    padding: Union[int, Tuple[int, int]],
    ceil_mode: bool = False,
    count_include_pad: bool = True,
    divisor_override: int = None,
) -> torch.Tensor:
    """
    CPU reference implementation of 2D average pooling.

    Args:
        x: Input tensor of shape (N, C, H_in, W_in)
        kernel_size: Size of pooling window
        stride: Stride of pooling window
        padding: Zero padding
        ceil_mode: Ceil vs floor for output dim calculation
        count_include_pad: Whether to include padding in average
        divisor_override: Override for divisor (default: kernel_size)

    Returns:
        Output tensor of shape (N, C, H_out, W_out)
    """
    result = F.avg_pool2d(
        x,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        ceil_mode=ceil_mode,
        count_include_pad=count_include_pad,
        divisor_override=divisor_override,
    )
    return result


def calculate_output_dim(
    input_dim: int,
    kernel_dim: int,
    stride: int,
    padding: int,
    dilation: int = 1,
    ceil_mode: bool = False,
) -> int:
    """
    Calculate output dimension for pooling operation.

    Args:
        input_dim: Input dimension
        kernel_dim: Kernel dimension
        stride: Stride
        padding: Padding
        dilation: Dilation
        ceil_mode: Use ceil instead of floor

    Returns:
        Output dimension
    """
    import math
    out_dim = (input_dim + 2 * padding - dilation * (kernel_dim - 1) - 1) / stride + 1
    if ceil_mode:
        return math.ceil(out_dim)
    else:
        return math.floor(out_dim)


def generate_golden_reference(
    batch_size: int,
    channels: int,
    in_height: int,
    in_width: int,
    kernel_size: Union[int, Tuple[int, int]],
    stride: Union[int, Tuple[int, int]] = None,
    padding: Union[int, Tuple[int, int]] = 0,
    ceil_mode: bool = False,
    count_include_pad: bool = True,
):
    """
    Generate golden reference for AveragePool operator testing.

    Args:
        batch_size: Batch size
        channels: Number of channels
        in_height: Input height
        in_width: Input width
        kernel_size: Size of pooling window
        stride: Stride of pooling window (defaults to kernel_size)
        padding: Zero padding
        ceil_mode: Use ceil for output dim calculation
        count_include_pad: Include padding in average calculation

    Returns:
        Dictionary with input, output tensors and parameters
    """
    # Normalize kernel_size, stride, padding to tuples
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if stride is None:
        stride = kernel_size
    elif isinstance(stride, int):
        stride = (stride, stride)
    if isinstance(padding, int):
        padding = (padding, padding)

    # Calculate output dimensions
    out_height = calculate_output_dim(
        in_height, kernel_size[0], stride[0], padding[0], ceil_mode=ceil_mode
    )
    out_width = calculate_output_dim(
        in_width, kernel_size[1], stride[1], padding[1], ceil_mode=ceil_mode
    )

    # Create random input tensor
    input_tensor = torch.randn(
        batch_size, channels, in_height, in_width, dtype=torch.bfloat16
    )

    # Compute reference output
    output_tensor = avg_pool2d_cpu(
        input_tensor,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        ceil_mode=ceil_mode,
        count_include_pad=count_include_pad,
    )

    return {
        "input": input_tensor,
        "output": output_tensor,
        "kernel_size": kernel_size,
        "stride": stride,
        "padding": padding,
        "out_height": out_height,
        "out_width": out_width,
    }
