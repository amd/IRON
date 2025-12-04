#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.dequant.op import AIEDequant
from operators.dequant.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    input_lengths = [2048] if not extensive else [1024, 2048, 4096, 8192]
    group_size = 32
    
    params = []
    names = []
    for input_length in input_lengths:
        for num_columns in range(1, 9):  # 1 to 8 columns
            for num_channels in range(1, 3):  # 1 or 2 channels
                total_cores = num_columns * num_channels
                tile_size = input_length // total_cores

                # Cap tile_size at 16384
                if tile_size > 16384:
                    tile_size = 16384

                # Only proceed if tile_size * total_cores == input_length (exact division)
                if tile_size * total_cores == input_length:
                    names.append(f"dequant_{num_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}")
                    params.append((input_length, num_columns, num_channels, tile_size, group_size))
    return params, names

regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s"
)
@pytest.mark.parametrize("input_length,num_aie_columns,num_channels,tile_size,group_size",
                         regular_params,
                         ids=regular_names)
def test_dequant(input_length, num_aie_columns, num_channels, tile_size, group_size, aie_context):
    golden_ref = generate_golden_reference(
        input_length=input_length,
        tile_size=tile_size,
        group_size=group_size,
    )

    operator = AIEDequant(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        group_size=group_size,
        context=aie_context,
    )

    input_buffers = {
        "input": golden_ref["input"].flatten(),
    }
    output_buffers = {"output": golden_ref["output"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.01, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s"
)
@pytest.mark.extensive
@pytest.mark.parametrize("input_length,num_aie_columns,num_channels,tile_size,group_size",
                         extensive_params,
                         ids=extensive_names)
def test_dequant_extensive(input_length, num_aie_columns, num_channels, tile_size, group_size):
    test_dequant(input_length, num_aie_columns, num_channels, tile_size, group_size)
