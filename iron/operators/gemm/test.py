#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.operators.gemm.op import AIEGEMM
from iron.operators.gemm.reference import generate_golden_reference
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    # fmt: off
    params = [
        #   M,     K,     N, num_aie_columns, b_col_maj, c_col_maj,   m,   k,   n, trace_size, partition_N
        (2048,  2048,  2048,               1,     False,     False,  64,  64,  64,          0,           1),
        (2048,  2048,  2048,               2,      True,     False,  64,  64,  64,          0,           1),
        (2048,  2048,  2048,               8,      True,      True,  64,  64,  64,          0,           1),
        ( 384,  1536,  1792,               4,      True,     False,  32,  48,  64,          0,           1),
        (1792,   896,  1152,               8,     False,      True,  64,  32,  48,          0,           1),
        ( 896,  1792,   640,               8,     False,      True,  32,  64,  80,          0,           1),
        ( 192,   384,    64,               4,     False,     False,  48,  96,  16,          0,           1),
        ( 192,   384,    64,               4,      True,      True,  48,  96,  16,          0,           1),
    ]                                                                                          
    extensive_params = [                                                                       
        (2048,  2048,  2048,               8,     False,     False,  32,  32, 128,          0,           1),
        (2048,  2048,  8192,               2,     False,     False,  64,  64,  64,          0,           1),
        (2048,  8192,  2048,               2,     False,     False,  64,  64,  64,          0,           1),
        (2048,    64,  2048,               2,     False,     False,  64,  64,  64,          0,           1),
        (2048,    64,  8192,               2,     False,     False,  64,  64,  64,          0,           1),
        (2048,  2048,  2048,               8,      True,     False, 128,  32,  32,          0,           1),
        (2048,  2048,  8192,               2,      True,     False,  64,  64,  64,          0,           1),
        (2048,  8192,  2048,               2,      True,     False,  64,  64,  64,          0,           1),
        (2048,    64,  2048,               2,      True,     False,  64,  64,  64,          0,           1),
        (2048,    64,  8192,               2,      True,     False,  64,  64,  64,          0,           1),
        (2048,  2048,  2048,               2,     False,      True,   8,  16,  32,          0,           1),
        (2048,  2048,  8192,               2,     False,      True,  64,  64,  64,          0,           1),
        (2048,  8192,  2048,               2,     False,      True,  64,  64,  64,          0,           1),
        (2048,    64,  2048,               2,     False,      True,  64,  64,  64,          0,           1),
        (2048,    64,  8192,               2,     False,      True,  64,  64,  64,          0,           1),
    ]
    # fmt: on

    if extensive:
        params = extensive_params

    names = []
    for (
        M,
        K,
        N,
        num_aie_columns,
        b_col_maj,
        c_col_maj,
        m,
        k,
        n,
        trace_size,
        partition_N,
    ) in params:
        name = f"gemm_{M}x{K}x{N}_{m}x{k}x{n}_{num_aie_columns}cols"
        if b_col_maj:
            name += "_bcolmaj"
        if c_col_maj:
            name += "_ccolmaj"
        if partition_N > 1:
            name += f"_{partition_N}npart"
        if trace_size > 0:
            name += f"_{trace_size}trace"
        names.append(name)

    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

# Combine params with marks - extensive params get pytest.mark.extensive
all_params = [
    pytest.param(*params, id=name)
    for params, name in zip(regular_params, regular_names)
] + [
    pytest.param(*params, marks=pytest.mark.extensive, id=name)
    for params, name in zip(extensive_params, extensive_names)
]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,N,num_aie_columns,b_col_maj,c_col_maj,m,k,n,trace_size,partition_N",
    all_params,
)
def test_gemm(
    M,
    K,
    N,
    num_aie_columns,
    b_col_maj,
    c_col_maj,
    m,
    k,
    n,
    trace_size,
    partition_N,
    aie_context,
):
    golden_ref = generate_golden_reference(
        M=M,
        K=K,
        N=N,
        partition_N=partition_N,
        b_col_maj=b_col_maj,
        c_col_maj=c_col_maj,
    )

    operator = AIEGEMM(
        M=M,
        K=K,
        N=N,
        tile_m=m,
        tile_k=k,
        tile_n=n,
        num_aie_columns=num_aie_columns,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        b_col_maj=b_col_maj,
        c_col_maj=c_col_maj,
        partition_N=partition_N,
        context=aie_context,
    )

    input_buffers = {
        "A": golden_ref["input"].flatten(),
    }
    output_buffers = {}

    # Create A, B, C dictionaries from the partitioned buffers
    for i in range(partition_N):
        input_buffers[f"B_{i}"] = golden_ref["input_b"][i].flatten()
        output_buffers[f"C_{i}"] = golden_ref["output"][i].flatten()
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.005, abs_tol=0.005
    )

    gflops = (2.0 * M * K * N) / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s")
    print(f"Throughput: {gflops:.6e} GFLOP/s\n")

    assert not errors, f"Test failed"
