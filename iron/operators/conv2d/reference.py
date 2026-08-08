# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU golden for AIEConv2d tests via torch F.conv2d.

``conv2d_cpu`` wraps F.conv2d; ``generate_golden_reference`` builds seeded
tensors and expected output. HW tests use bf16 tolerances (tolerances.py).
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
    """F.conv2d wrapper used as the golden for all conv2d tests."""
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
    """Seeded tensors + expected output via conv2d_cpu (bf16 drawn in fp32 then cast)."""
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

    out_height = calculate_output_dim(
        in_height, kernel_size[0], stride[0], padding[0], dilation[0]
    )
    out_width = calculate_output_dim(
        in_width, kernel_size[1], stride[1], padding[1], dilation[1]
    )

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

    expected_output = conv2d_cpu(
        input=input_tensor,
        weight=weight_tensor,
        bias=bias_tensor,
        stride=stride,
        padding=padding,
        dilation=dilation,
        groups=groups,
    )

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
    """floor((input + 2*pad - dilation*(kernel-1) - 1) / stride + 1)."""
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
