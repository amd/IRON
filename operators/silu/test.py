#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.silu.op import AIESiLU
from operators.silu.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    max_aie_columns = 8
    num_channels = 1  # 1 channel for 1 input
    input_lengths = [2048] if not extensive else [1024, 4096, 8192]

    params = []
    names = []
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size > 4096:
                tile_size = 4096
            check_length = tile_size * num_aie_columns
            if check_length == input_length:
                names.append(
                    f"silu_{num_aie_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}"
                )
                params.append((input_length, num_aie_columns, num_channels, tile_size))
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size",
    regular_params,
    ids=regular_names,
)
def test_silu(input_length, num_aie_columns, num_channels, tile_size, aie_context):
    golden_ref = generate_golden_reference(input_length=input_length)

    operator = AIESiLU(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.extensive
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size",
    extensive_params,
    ids=extensive_names,
)
def test_silu_extensive(
    input_length, num_aie_columns, num_channels, tile_size, aie_context
):
    test_silu(input_length, num_aie_columns, num_channels, tile_size, aie_context)
