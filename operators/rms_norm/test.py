#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.rms_norm.op import AIERMSNorm
from operators.rms_norm.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    max_aie_columns = 8
    num_channels = 2
    input_lengths = [2048] if not extensive else [1024, 4096, 8192]

    params = []
    names = []
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
                            names.append(
                                f"rms_norm_{num_aie_columns}_cols_{num_channels_rms}_channels_{input_length}_tile_{tile_size}"
                            )
                        else:
                            names.append(
                                f"weighted_rms_norm_{num_aie_columns}_cols_{num_channels_rms}_channels_{input_length}_weights_{tile_size}"
                            )
                        params.append(
                            (
                                input_length,
                                num_aie_columns,
                                num_channels_rms,
                                tile_size,
                                weighted,
                            )
                        )

    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size,weighted",
    regular_params,
    ids=regular_names,
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
    "input_length,num_aie_columns,num_channels,tile_size,weighted",
    extensive_params,
    ids=extensive_names,
)
def test_rms_norm_extensive(
    input_length, num_aie_columns, num_channels, tile_size, weighted, aie_context
):
    test_rms_norm(
        input_length, num_aie_columns, num_channels, tile_size, weighted, aie_context
    )
