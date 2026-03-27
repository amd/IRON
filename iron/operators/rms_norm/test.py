#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.common.aie_device_manager import AIEDeviceManager
from iron.operators.rms_norm.op import AIERMSNorm
from iron.common.aie_device_manager import AIEDeviceManager
from iron.operators.rms_norm.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    # Detect device and set max columns accordingly
    # NPU1 (Phoenix) has 4 columns, NPU2 (Strix) has 8 columns
    device_type = AIEDeviceManager().device_str()
    max_aie_columns = 4 if device_type == "npu1" else 8
    num_channels = 2
    input_lengths = [1024, 2048, 4096, 8192]

    params = []
    for weighted in [False, True]:
        for input_length in input_lengths:
            for num_aie_columns in range(1, max_aie_columns + 1):
                num_channels_options = range(1, 3) if not weighted else [num_channels]
                for num_channels_rms in num_channels_options:  # 1 or 2
                    if not weighted:
                        total_cores = num_aie_columns * num_channels_rms
                        tile_size = input_length // total_cores
                        if tile_size > 8192:
                            tile_size = 8192
                        check_length = tile_size * total_cores
                    else:
                        tile_size = input_length // num_aie_columns
                        if tile_size > 4096:
                            tile_size = 4096
                        check_length = tile_size * num_aie_columns
                    if check_length == input_length:
                        if not weighted:
                            name = f"rms_norm_{num_aie_columns}_cols_{num_channels_rms}_channels_{input_length}_tile_{tile_size}"
                        else:
                            name = f"weighted_rms_norm_{num_aie_columns}_cols_{num_channels_rms}_channels_{input_length}_weights_{tile_size}"

                        is_regular = input_length == 2048
                        marks = [] if is_regular else [pytest.mark.extensive]

                        params.append(
                            pytest.param(
                                input_length,
                                num_aie_columns,
                                num_channels_rms,
                                tile_size,
                                weighted,
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
    "input_length,num_aie_columns,num_channels,tile_size,weighted",
    get_params(),
)
def test_rms_norm(
    input_length, num_aie_columns, num_channels, tile_size, weighted, aie_context
):
    rows = input_length // tile_size
    cols = tile_size
    golden_ref = generate_golden_reference(rows=rows, cols=cols, weighted=weighted)

    operator = AIERMSNorm(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        weighted=weighted,
        context=aie_context,
    )

    input_buffers = {"input1": golden_ref["input"]}
    if weighted:
        operator.weight = golden_ref["weight"]
        input_buffers["weight"] = golden_ref["weight"]
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
