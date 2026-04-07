#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.leaky_relu.op import LeakyReLU
from iron.operators.leaky_relu.reference import generate_golden_reference
from iron.common.test_utils import run_test, make_channeled_unary_params


def get_params():
    alphas = [0.01]
    return [
        pytest.param(
            il, nac, nc, ts, alpha, marks=[] if not ext else [pytest.mark.extensive]
        )
        for il, nac, nc, ts, ext in make_channeled_unary_params(
            [1024, 2048, 4096, 8192], 4096, [1, 2]
        )
        for alpha in alphas
    ]


@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size,alpha", get_params()
)
@pytest.mark.skip(reason="Leaky ReLU is currently broken (#36)")
@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
def test_leaky_relu(
    input_length, num_aie_columns, num_channels, tile_size, alpha, aie_context
):
    golden_ref = generate_golden_reference(input_length=input_length, alpha=alpha)

    operator = LeakyReLU(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        alpha=alpha,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
