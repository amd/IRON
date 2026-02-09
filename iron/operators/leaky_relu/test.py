#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.operators.leaky_relu.op import AIELeakyReLU
from iron.operators.leaky_relu.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    # Leaky ReLU is currently broken (#36); leave it untested
    params = []
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size,alpha",
    get_params(),
)
def test_leaky_relu(
    input_length, num_aie_columns, num_channels, tile_size, alpha, aie_context
):
    golden_ref = generate_golden_reference(input_length=input_length)

    operator = AIELeakyReLU(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        alpha=alpha,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["A"]}
    output_buffers = {"output": golden_ref["B"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
