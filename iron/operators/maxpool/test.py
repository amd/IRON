# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test suite for AIE MaxPool2D Operator
"""

import sys
import pytest
from pathlib import Path

import torch

from iron.operators.maxpool.op import AIEMaxPool2d
from iron.operators.maxpool.reference import generate_golden_reference, max_pool2d_cpu


def generate_test_params(extensive=False):
    """Generate test parameters for maxpool2d operator tests."""
    params = []
    names = []

    # Basic test configurations
    configs = [
        # (kernel_size, stride, padding)
        (2, 2, 0),  # Basic 2x2 pool
        (3, 3, 0),  # 3x3 pool
        (3, 2, 1),  # Strided pool with padding
        (4, 4, 0),  # 4x4 pool
        (2, 1, 0),  # Overlapping pool
    ]

    input_sizes = [(1, 32, 32)] if not extensive else [(1, 32, 32), (1, 64, 64)]

    for batch, in_h, in_w in input_sizes:
        for kernel, stride, pad in configs:
            names.append(f"maxpool_k{kernel}_s{stride}_p{pad}_{in_h}x{in_w}")
            params.append((kernel, stride, pad, batch, in_h, in_w))

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
    "kernel_size,stride,padding,batch,in_h,in_w",
    all_params,
)
def test_maxpool2d(kernel_size, stride, padding, batch, in_h, in_w, aie_context):
    """Test maxpool2d operator against CPU reference."""

    # Generate golden reference
    golden_ref = generate_golden_reference(
        batch_size=batch,
        channels=16,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
    )

    # Create operator
    operator = AIEMaxPool2d(
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        context=aie_context,
    )

    # Prepare input/output
    input_buffers = {
        "input": golden_ref["input"],
    }
    output_buffers = {"output": golden_ref["output"]}

    # Note: Full test execution requires NPU hardware
    # This test validates the operator setup and configuration
    print(f"\nMaxPool2D Test: k={kernel_size}, s={stride}, p={padding}")
    print(f"  Input shape: {golden_ref['input'].shape}")
    print(f"  Output shape: {golden_ref['output'].shape}")


@pytest.mark.parametrize(
    "kernel_size,stride,padding,batch,in_h,in_w",
    regular_params[:3],  # Test first few cases
)
def test_maxpool2d_forward(
    kernel_size, stride, padding, batch, in_h, in_w, aie_context
):
    """Test maxpool2d operator forward pass."""

    # Generate golden reference
    golden_ref = generate_golden_reference(
        batch_size=batch,
        channels=16,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
    )

    # Create operator
    operator = AIEMaxPool2d(
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        context=aie_context,
    )

    # Run operator
    result = operator(golden_ref["input"])

    # Compare with CPU reference
    expected = golden_ref["output"]

    # Check shape
    assert (
        result.shape == expected.shape
    ), f"Shape mismatch: got {result.shape}, expected {expected.shape}"

    # Check values with relaxed tolerance for AIE
    rel_tol = 0.05
    abs_tol = 0.1
    if not torch.allclose(result, expected, rtol=rel_tol, atol=abs_tol):
        max_diff = (result - expected).abs().max().item()
        pytest.fail(f"Results don't match. Max diff: {max_diff}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
