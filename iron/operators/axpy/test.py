#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.axpy.op import AXPY
from iron.operators.axpy.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols
    input_lengths = [1024, 2048, 4096, 8192]
    scalar_factors = [3.0, 10.0]

    params = []
    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size * num_aie_columns != input_length:
                continue
            for scalar in scalar_factors:
                # Determine if this is a regular test case
                is_regular = input_length == 2048 and scalar == 3.0
                marks = [] if is_regular else [pytest.mark.extensive]

                params.append(
                    pytest.param(
                        input_length,
                        num_aie_columns,
                        tile_size,
                        scalar,
                        marks=marks,
                    )
                )
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,tile_size,scalar_factor",
    get_params(),
)
def test_axpy(input_length, num_aie_columns, tile_size, scalar_factor, aie_context):
    golden_ref = generate_golden_reference(
        input_length=input_length, scalar=scalar_factor
    )

    operator = AXPY(
        size=input_length,
        num_aie_columns=num_aie_columns,
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
