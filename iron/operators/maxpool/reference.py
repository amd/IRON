# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
CPU Reference Implementation for MaxPool Operator
"""

import torch
import torch.nn.functional as F
from typing import Union, Tuple


def max_pool2d_cpu(
    x: torch.Tensor,
    kernel_size: Union[int, Tuple[int, int]],
    stride: Union[int, Tuple[int, int]],
    padding: Union[int, Tuple[int, int]],
    dilation: Union[int, Tuple[int, int]] = 1,
    return_indices: bool = False,
) -> torch.Tensor:
    """
    CPU reference implementation of 2D max pooling.

    Args:
        x: Input tensor of shape (N, C, H_in, W_in)
        kernel_size: Size of pooling window
        stride: Stride of pooling window
        padding: Zero padding
        dilation: Spacing between kernel elements
        return_indices: Whether to return indices (for unpooling)

    Returns:
        Output tensor of shape (N, C, H_out, W_out)
    """
    result = F.max_pool2d(
        x,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        dilation=dilation,
        return_indices=return_indices,
    )
    return result


def calculate_output_dim(
    input_dim: int,
    kernel_dim: int,
    stride: int,
    padding: int,
    dilation: int = 1,
) -> int:
    """
    Calculate output dimension for pooling operation.

    Args:
        input_dim: Input dimension
        kernel_dim: Kernel dimension
        stride: Stride
        padding: Padding
        dilation: Dilation

    Returns:
        Output dimension
    """
    return (input_dim + 2 * padding - dilation * (kernel_dim - 1) - 1) // stride + 1


def generate_golden_reference(
    batch_size: int,
    channels: int,
    in_height: int,
    in_width: int,
    kernel_size: Union[int, Tuple[int, int]],
    stride: Union[int, Tuple[int, int]] = None,
    padding: Union[int, Tuple[int, int]] = 0,
    dilation: Union[int, Tuple[int, int]] = 1,
):
    """
    Generate golden reference for MaxPool operator testing.

    Args:
        batch_size: Batch size
        channels: Number of channels
        in_height: Input height
        in_width: Input width
        kernel_size: Size of pooling window
        stride: Stride of pooling window (defaults to kernel_size)
        padding: Zero padding
        dilation: Spacing between kernel elements

    Returns:
        Dictionary with input, output tensors and parameters
    """
    # Normalize kernel_size, stride, padding, dilation to tuples
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if stride is None:
        stride = kernel_size
    elif isinstance(stride, int):
        stride = (stride, stride)
    if isinstance(padding, int):
        padding = (padding, padding)
    if isinstance(dilation, int):
        dilation = (dilation, dilation)

    # Calculate output dimensions
    out_height = calculate_output_dim(
        in_height, kernel_size[0], stride[0], padding[0], dilation[0]
    )
    out_width = calculate_output_dim(
        in_width, kernel_size[1], stride[1], padding[1], dilation[1]
    )

    # Create random input tensor
    input_tensor = torch.randn(
        batch_size, channels, in_height, in_width, dtype=torch.bfloat16
    )

    # Compute reference output
    output_tensor = max_pool2d_cpu(
        input_tensor,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        dilation=dilation,
    )

    return {
        "input": input_tensor,
        "output": output_tensor,
        "kernel_size": kernel_size,
        "stride": stride,
        "padding": padding,
        "dilation": dilation,
        "out_height": out_height,
        "out_width": out_width,
    }
