#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.rms_norm.op import RMSNorm
from iron.operators.rms_norm.reference import generate_golden_reference
from iron.common.test_utils import run_test
from iron.common.utils import get_shim_dma_limit


def get_params():
    dev = aie_utils.get_current_device()
    max_aie_columns = dev.cols
    shim_dma_limit = get_shim_dma_limit(dev)
    input_lengths = [1024, 2048, 4096, 8192]

    params = []
    for weighted in [False, True]:
        for input_length in input_lengths:
            for num_aie_columns in range(1, max_aie_columns + 1):
                num_channels_options = range(1, 3)
                for num_channels_rms in num_channels_options:  # 1 or 2
                    # Skip configs that exceed device limits.
                    if num_aie_columns * num_channels_rms > shim_dma_limit:
                        continue
                    # Weighted design uses one weight FIFO per channel shared across
                    # columns; ShimDMA output budget = num_channels * (num_aie_columns + 1).
                    if (
                        weighted
                        and num_channels_rms * (num_aie_columns + 1) > shim_dma_limit
                    ):
                        continue
                    total_cores = num_aie_columns * num_channels_rms
                    if not weighted:
                        tile_size = input_length // total_cores
                        if tile_size > 8192:
                            tile_size = 8192
                        check_length = tile_size * total_cores
                    else:
                        tile_size = input_length // total_cores
                        if tile_size > 4096:
                            tile_size = 4096
                        check_length = tile_size * total_cores
                    if check_length == input_length:
                        is_regular = input_length == 2048
                        marks = [] if is_regular else [pytest.mark.extensive]

                        params.append(
                            pytest.param(
                                input_length,
                                num_aie_columns,
                                num_channels_rms,
                                tile_size,
                                weighted,
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

    operator = RMSNorm(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        weighted=weighted,
        context=aie_context,
    )

    input_buffers = {"input1": golden_ref["input"]}
    if weighted:
        input_buffers["weight"] = golden_ref["weight"]
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
