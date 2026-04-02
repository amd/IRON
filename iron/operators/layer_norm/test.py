#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.common.aie_device_manager import AIEDeviceManager
from iron.common.device_utils import DEVICE_CONFIGS
from iron.operators.layer_norm.op import AIELayerNorm
from iron.operators.layer_norm.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    device_type = AIEDeviceManager().device_str()
    max_aie_columns = DEVICE_CONFIGS[device_type]["max_columns"]
    input_lengths = [1024, 2048, 4096, 8192]
    params = []
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            for num_channels_layer in range(1, 3):  # 1 or 2
                total_cores = num_aie_columns * num_channels_layer
                tile_size = input_length // total_cores
                if tile_size > 8192:
                    tile_size = 8192
                check_length = tile_size * total_cores
                if check_length == input_length:
                    name = f"layer_norm_{num_aie_columns}_cols_{num_channels_layer}_channels_{input_length}_tile_{tile_size}"

                    is_regular = input_length == 2048
                    marks = [] if is_regular else [pytest.mark.extensive]

                    params.append(
                        pytest.param(
                            input_length,
                            num_aie_columns,
                            num_channels_layer,
                            tile_size,
                            id=name,
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
def test_layer_norm(
    input_length, num_aie_columns, num_channels, tile_size, aie_context
):

    rows = input_length // tile_size
    cols = tile_size
    golden_ref = generate_golden_reference(rows=rows, cols=cols)

    operator = AIELayerNorm(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.1, abs_tol=0.1
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
