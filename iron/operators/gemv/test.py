#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.operators.gemv.op import AIEGEMV
from iron.operators.gemv.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    params_list = [
        (128, 128, 1, 32, 128),
        (2048, 8192, 1, 1, 2048),
        (8192, 2048, 1, 4, 1024),
        (2048, 8192, 2, 1, 1024),
        (8192, 2048, 2, 4, 1024),
        (2048, 8192, 4, 1, 512),
        (8192, 2048, 4, 4, 1024),
        (2048, 8192, 8, 1, 256),
        (8192, 2048, 8, 4, 1024),
    ]

    params = []
    for p in params_list:
        M, K, num_aie_columns, tile_size_input, tile_size_output = p
        name = f"matrix_vector_mul_{M}x{K}_{tile_size_input}tsi_{tile_size_output}tso_{num_aie_columns}col"

        # All tests are considered regular here as per original code structure
        # (original code returned same list for both regular and extensive)
        params.append(pytest.param(*p, id=name))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output", get_params()
)
def test_gemv(M, K, num_aie_columns, tile_size_input, tile_size_output, aie_context):
    golden_ref = generate_golden_reference(M=M, K=K)

    operator = AIEGEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        context=aie_context,
    )

    input_buffers = {"matrix": golden_ref["A"].flatten(), "vector": golden_ref["B"]}
    output_buffers = {"output": golden_ref["C"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
    )

    print(f"\nLatency: {latency_us:.1f} us")

    gflops = (2.0 * M * K) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
