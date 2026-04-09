#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.scale_i32_bf16.op import ScaleI32
from iron.operators.scale_i32_bf16.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols

    input_lengths = [1024, 2048, 4096, 8192]

    params = []
    for input_length in input_lengths:
        for num_columns in range(1, max_aie_columns + 1):
            for num_channels in range(1, 3):  # 1 or 2 channels
                total_cores = num_columns * num_channels
                # 3 ObjectFIFOs per core (data_in, scale, data_out) limits placement
                if total_cores > 8:
                    continue
                if input_length % total_cores != 0:
                    continue

                tile_size = input_length // total_cores

                # Cap tile_size at 8192
                if tile_size > 8192:
                    tile_size = 8192

                # Only proceed if exact division
                if tile_size * total_cores != input_length:
                    continue

                # Ensure tile_size is a multiple of 16
                if tile_size % 16 != 0:
                    continue

                is_regular = input_length == 2048
                marks = [] if is_regular else [pytest.mark.extensive]

                params.append(
                    pytest.param(
                        input_length,
                        num_columns,
                        num_channels,
                        tile_size,
                        marks=marks,
                    )
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
def test_scale_i32_bf16(
    input_length, num_aie_columns, num_channels, tile_size, aie_context
):
    golden_ref = generate_golden_reference(
        input_length=input_length,
        tile_size=tile_size,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
    )

    operator = ScaleI32(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    input_buffers = {
        "data": golden_ref["input_i32"].flatten(),
        "scale": golden_ref["scale_buffer"].flatten(),
    }
    output_buffers = {"output": golden_ref["expected_output"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.01, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
