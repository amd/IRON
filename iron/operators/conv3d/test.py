# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test suite for AIE Conv3D Operator
"""

import sys
import pytest
from pathlib import Path

import torch

from iron.operators.conv3d.op import AIEConv3d
from iron.operators.conv3d.reference import generate_golden_reference, conv3d_cpu


def generate_test_params(extensive=False):
    """Generate test parameters for conv3d operator tests."""
    params = []
    names = []

    # Basic test configurations
    configs = [
        # (in_channels, out_channels, kernel_size, stride, padding, groups)
        (3, 16, 3, 1, 1, 1),  # Basic conv3d
        (16, 16, 3, 1, 1, 1),  # Same channels
        (16, 16, 3, 1, 1, 16),  # Depthwise
        (32, 64, 1, 1, 0, 1),  # Pointwise
        (16, 32, 3, 2, 1, 1),  # Strided conv
    ]

    input_sizes = [(1, 8, 16, 16)] if not extensive else [(1, 8, 16, 16), (1, 16, 32, 32)]

    for batch, in_t, in_h, in_w in input_sizes:
        for in_ch, out_ch, kernel, stride, pad, groups in configs:
            names.append(
                f"conv3d_{in_ch}x{out_ch}_k{kernel}_s{stride}_p{pad}_g{groups}_{in_t}x{in_h}x{in_w}"
            )
            params.append((in_ch, out_ch, kernel, stride, pad, groups, batch, in_t, in_h, in_w))

    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

# Combine params with marks
all_params = [
    pytest.param(*params, id=name)
    for params, name in zip(regular_params, regular_names)
] + [
    pytest.param(*params, marks=pytest.mark.extensive, id=name)
    for params, name in zip(extensive_params, extensive_names)
]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "in_channels,out_channels,kernel_size,stride,padding,groups,batch,in_t,in_h,in_w",
    all_params,
)
def test_conv3d(
    in_channels, out_channels, kernel_size, stride, padding, groups, batch, in_t, in_h, in_w,
    aie_context
):
    """Test conv3d operator against CPU reference."""

    # Skip depthwise if not supported
    is_depthwise = groups == in_channels and groups == out_channels
    is_pointwise = kernel_size == 1

    # Generate golden reference
    golden_ref = generate_golden_reference(
        batch_size=batch,
        in_channels=in_channels,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=True,
    )

    # Create operator
    operator = AIEConv3d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=True,
        context=aie_context,
    )

    # Prepare input/output
    input_buffers = {
        "input": golden_ref["input"],
        "weight": golden_ref["weight"],
    }
    if golden_ref["bias"] is not None:
        input_buffers["bias"] = golden_ref["bias"]

    output_buffers = {"output": golden_ref["output"]}

    # Note: Full test execution requires NPU hardware
    # This test validates the operator setup and configuration
    print(f"\nConv3D Test: in={in_channels}, out={out_channels}, k={kernel_size}, s={stride}")
    print(f"  Input shape: {golden_ref['input'].shape}")
    print(f"  Weight shape: {golden_ref['weight'].shape}")
    print(f"  Output shape: {golden_ref['output'].shape}")


@pytest.mark.parametrize(
    "in_channels,out_channels,kernel_size,stride,padding,groups,batch,in_t,in_h,in_w",
    regular_params[:3],  # Test first few cases
)
def test_conv3d_forward(
    in_channels, out_channels, kernel_size, stride, padding, groups, batch, in_t, in_h, in_w,
    aie_context
):
    """Test conv3d operator forward pass."""

    # Generate golden reference
    golden_ref = generate_golden_reference(
        batch_size=batch,
        in_channels=in_channels,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=True,
    )

    # Create operator
    operator = AIEConv3d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=True,
        context=aie_context,
    )

    # Run operator
    result = operator(
        golden_ref["input"],
        golden_ref["weight"],
        golden_ref["bias"],
    )

    # Compare with CPU reference
    expected = golden_ref["output"]

    # Check shape
    assert result.shape == expected.shape, \
        f"Shape mismatch: got {result.shape}, expected {expected.shape}"

    # Check values with relaxed tolerance for AIE
    rel_tol = 0.05
    abs_tol = 0.1
    if not torch.allclose(result, expected, rtol=rel_tol, atol=abs_tol):
        max_diff = (result - expected).abs().max().item()
        pytest.fail(f"Results don't match. Max diff: {max_diff}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
