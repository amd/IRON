#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.softmax.op import Softmax
from iron.operators.softmax.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_optimal_columns_channels(input_length, tile_size, max_columns):
    """Helper function to determine optimal columns and channels for a given input length and tile size"""
    total_cores = input_length // tile_size

    if total_cores == 4:
        return 2, 2  # 4 cores: use 2x2 configuration
    elif total_cores == 8:
        return 2, 2  # 8 cores: use 2x2 configuration (N_div_n=2 iterations per core)
    elif total_cores == 2:
        return 1, 2  # 2 cores: use 1x2 configuration
    elif total_cores == 1:
        return 1, 1  # 1 core: use 1x1 configuration
    elif total_cores == 16:
        # For 16 cores, use 2x2 to avoid exceeding device capabilities
        # The 4x4 configuration causes placement issues on Phoenix
        return 2, 2  # Use 2x2, each core handles more iterations
    else:
        return 2, 2  # Default fallback


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols
    input_lengths = [32768]
    tile_sizes = [1024, 512, 2048]

    params = []
    for input_length in input_lengths:
        for tile_size in tile_sizes:
            optimal_columns, optimal_channels = get_optimal_columns_channels(
                input_length, tile_size, max_aie_columns
            )
            # Skip if configuration exceeds device capabilities
            if optimal_columns > max_aie_columns:
                continue

            params.append(
                pytest.param(input_length, optimal_columns, optimal_channels, tile_size)
            )
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size",
    get_params(),
)
def test_softmax(input_length, num_aie_columns, num_channels, tile_size, aie_context):

    rows = input_length // tile_size
    cols = tile_size

    golden_ref = generate_golden_reference(rows=rows, cols=cols)

    operator = Softmax(
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
