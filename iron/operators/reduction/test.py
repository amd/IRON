# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test suite for AIE Reduction Operator
"""

import sys
import pytest
from pathlib import Path

from iron.operators.reduction.op import AIEReduction
from iron.operators.reduction.reference import generate_golden_reference, reduction_cpu
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    """Generate test parameters for reduction operator tests."""
    max_aie_columns = 8
    input_sizes = [4096] if not extensive else [2048, 4096, 8192]
    reduction_sizes = [64] if not extensive else [32, 64, 128]
    reduction_ops = ["sum", "max", "min"]  # mean only for AIE2P

    params = []
    names = []
    for input_size in input_sizes:
        for reduction_size in reduction_sizes:
            if input_size % reduction_size != 0:
                continue
            for num_aie_columns in range(1, max_aie_columns + 1):
                tile_size = input_size // num_aie_columns
                if tile_size * num_aie_columns != input_size:
                    continue
                for op in reduction_ops:
                    names.append(
                        f"reduction_{op}_{input_size}_{reduction_size}_"
                        f"{num_aie_columns}cols_{tile_size}tile"
                    )
                    params.append(
                        (input_size, reduction_size, op, num_aie_columns, tile_size)
                    )
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

# Combine params with marks - extensive params get pytest.mark.extensive
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
    "input_size,reduction_size,reduction_op,num_aie_columns,tile_size",
    all_params,
)
def test_reduction(
    input_size, reduction_size, reduction_op, num_aie_columns, tile_size, aie_context
):
    """Test reduction operator against CPU reference."""
    # Calculate output size
    output_size = input_size // reduction_size

    # Generate golden reference
    # Create input shape that flattens to input_size
    input_shape = (output_size, reduction_size)
    golden_ref = generate_golden_reference(
        input_shape, dim=-1, reduction_op=reduction_op
    )

    # Create operator
    operator = AIEReduction(
        input_size=input_size,
        reduction_size=reduction_size,
        reduction_op=reduction_op,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    # Prepare input/output
    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    # Run test
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.05, abs_tol=1e-5
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.parametrize(
    "input_size,reduction_size,reduction_op,num_aie_columns,tile_size",
    regular_params[:4],  # Test first few cases
)
def test_reduction_forward(
    input_size, reduction_size, reduction_op, num_aie_columns, tile_size, aie_context
):
    """Test reduction operator forward pass with various tensor shapes."""
    # Create operator
    operator = AIEReduction(
        input_size=input_size,
        reduction_size=reduction_size,
        reduction_op=reduction_op,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    # Test with 2D tensor
    output_size = input_size // reduction_size
    x = torch.randn(output_size, reduction_size, dtype=torch.bfloat16) * 2.0

    # Run operator
    result = operator(x)

    # Compare with CPU reference
    expected = reduction_cpu(x, dim=-1, reduction_op=reduction_op)

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


# Import torch at module level (after pytest imports)
import torch


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
