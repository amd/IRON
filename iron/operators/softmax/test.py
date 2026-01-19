#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from iron.operators.softmax.op import AIESoftmax
from iron.operators.softmax.reference import generate_golden_reference
from iron.operators.common.test_utils import run_test


def get_optimal_columns_channels(input_length, tile_size):
    """Helper function to determine optimal columns and channels for a given input length and tile size"""
    total_cores = input_length // tile_size

    if total_cores == 4:
        return 2, 2  # 4 cores: use 2x2 configuration
    elif total_cores == 8:
        return 2, 2  # 8 cores: use 2x2 configuration (each core handles 2 iterations)
    elif total_cores == 2:
        return 1, 2  # 2 cores: use 1x2 configuration
    elif total_cores == 1:
        return 1, 1  # 1 core: use 1x1 configuration
    elif total_cores == 16:
        return 4, 4  # 16 cores: use 4x4 configuration
    else:
        return 2, 2  # Default fallback


def generate_test_params(extensive=False):
    max_aie_columns = 8
    num_channels = 2
    input_lengths = [4096] if not extensive else []
    tile_sizes = [1024, 512, 2048]

    params = []
    names = []
    for input_length in input_lengths:
        for tile_size in tile_sizes:
            optimal_columns, optimal_channels = get_optimal_columns_channels(
                input_length, tile_size
            )
            names.append(
                f"softmax_{optimal_columns}_cols_{optimal_channels}_channels_{input_length}_tile_{tile_size}"
            )
            params.append((input_length, optimal_columns, optimal_channels, tile_size))
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
    "input_length,num_aie_columns,num_channels,tile_size",
    all_params,
)
def test_softmax(input_length, num_aie_columns, num_channels, tile_size, aie_context):

    rows = input_length // tile_size
    cols = tile_size

    golden_ref = generate_golden_reference(rows=rows, cols=cols)

    operator = AIESoftmax(
        rows=rows,
        cols=cols,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        context=aie_context,
    )

    input_buffers = {"in": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
