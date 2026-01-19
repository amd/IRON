#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.operators.dequant.op import AIEDequant
from iron.operators.dequant.reference import generate_golden_reference
from iron.operators.common.test_utils import run_test


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
                    names.append(
                        f"dequant_{num_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}"
                    )
                    params.append(
                        (input_length, num_columns, num_channels, tile_size, group_size)
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
    "input_length,num_aie_columns,num_channels,tile_size,group_size",
    all_params,
)
def test_dequant(
    input_length, num_aie_columns, num_channels, tile_size, group_size, aie_context
):
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
