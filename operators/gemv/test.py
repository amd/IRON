#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.gemv.op import AIEGEMV
from operators.gemv.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    params = [
        (128, 128, 1, 32),
        (2048, 8192, 1, 1),
        (8192, 2048, 1, 4),
        (2048, 8192, 2, 1),
        (8192, 2048, 2, 4),
        (2048, 8192, 4, 1),
        (8192, 2048, 4, 4),
        (2048, 8192, 8, 1),
        (8192, 2048, 8, 4),
    ]
    names = [
        f"matrix_vector_mul_{M}x{K}_{tile_size}_{num_aie_columns}col"
        for M, K, num_aie_columns, tile_size in params
    ]
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size", regular_params, ids=regular_names
)
def test_gemv(M, K, num_aie_columns, tile_size, aie_context):
    golden_ref = generate_golden_reference(M=M, K=K)

    operator = AIEGEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
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


@pytest.mark.metrics(
    Latency=r"Latency: (?P<value>[\d\.]+) us",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.extensive
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size", extensive_params, ids=extensive_names
)
def test_gemv_extensive(M, K, num_aie_columns, tile_size, aie_context):
    test_gemv(M, K, num_aie_columns, tile_size, aie_context)
