#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.axpy.op import AIEAXPY
from operators.axpy.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    max_aie_columns = 8
    num_channels = 2
    input_lengths = [2048] if not extensive else [1024, 2048, 4096, 8192]
    scalar_factors = [3.0] if not extensive else [3.0, 10.0]
    
    params = []
    names = []
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size * num_aie_columns != input_length:
                continue
            for scalar in scalar_factors:
                names.append(f"axpy_{num_aie_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}_{scalar}")
                params.append((input_length, num_aie_columns, num_channels, tile_size, scalar))
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s"
)
@pytest.mark.parametrize("input_length,num_aie_columns,num_channels,tile_size,scalar_factor",
                         regular_params,
                         ids=regular_names)
def test_axpy(input_length, num_aie_columns, num_channels, tile_size, scalar_factor, aie_context):
    golden_ref = generate_golden_reference(
        input_length=input_length,
        scalar=scalar_factor
    )

    operator = AIEAXPY(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        scalar_factor=scalar_factor,
        context=aie_context,
    )

    input_buffers = {"x": golden_ref["A"], "y": golden_ref["B"]}
    output_buffers = {"output": golden_ref["C"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s"
)
@pytest.mark.extensive
@pytest.mark.parametrize("input_length,num_aie_columns,num_channels,tile_size,scalar_factor",
                         extensive_params,
                         ids=extensive_names)
def test_axpy_extensive(input_length, num_aie_columns, num_channels, tile_size, scalar_factor, aie_context):
    test_axpy(input_length, num_aie_columns, num_channels, tile_size, scalar_factor, aie_context)
