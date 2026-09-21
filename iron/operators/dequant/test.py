#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import torch
import aie.utils as aie_utils

from iron.operators.dequant.op import Dequant
from iron.common.test_utils import golden, run_test


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols

    input_lengths = [1024, 2048, 4096, 8192]
    group_size = 32

    params = []
    for input_length in input_lengths:
        for num_columns in range(1, max_aie_columns + 1):
            for num_channels in range(1, 3):  # 1 or 2 channels
                total_cores = num_columns * num_channels
                tile_size = input_length // total_cores

                # Cap tile_size at 16384
                if tile_size > 16384:
                    tile_size = 16384

                # Only proceed if tile_size * total_cores == input_length (exact division)
                if tile_size * total_cores == input_length:
                    is_regular = input_length == 2048
                    marks = [] if is_regular else [pytest.mark.extensive]

                    params.append(
                        pytest.param(
                            input_length,
                            num_columns,
                            num_channels,
                            tile_size,
                            group_size,
                            marks=marks,
                        )
                    )
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size,group_size",
    get_params(),
)
def test_dequant(
    input_length, num_aie_columns, num_channels, tile_size, group_size, aie_context
):
    operator = Dequant(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        group_size=group_size,
        context=aie_context,
    )

    # Values in [0, 3.75) with scales in [1/3.75, 1) keep every quantized
    # value inside int4's [0, 15].
    torch.manual_seed(42)
    values = torch.rand(input_length, dtype=torch.bfloat16) * 3.75
    scales = 1 / 3.75 + (1 - 1 / 3.75) * torch.rand(
        input_length // group_size, dtype=torch.bfloat16
    )
    data = golden(operator, x=operator.pack(values, scales))

    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=0.01, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
