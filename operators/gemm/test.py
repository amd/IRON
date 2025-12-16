#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.gemm.op import AIEGEMM
from operators.gemm.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    M_list = [2048] if not extensive else [2048]
    K_list = [2048] if not extensive else [2048, 8192, 64]
    N_list = [2048] if not extensive else [2048, 8192]
    m, k, n = 64, 64, 64
    num_aie_columns = 2
    col_maj = [(False, False), (True, False), (False, True)]
    trace_size = 0

    params = []
    names = []

    for b_col_maj, c_col_maj in col_maj:
        for M in M_list:
            for K in K_list:
                for N in N_list:
                    if N == 8192 and K == 8192:
                        continue  # Untested combination because huge & slow, unused in our application
                    params.append(
                        (
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
                        )
                    )
                    names.append(
                        f"gemm_{M}x{K}x{N}_{m}x{k}x{n}_{num_aie_columns}_cols_{int(b_col_maj)}_bcolmaj_{int(c_col_maj)}_ccolmaj_{trace_size}"
                    )

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
    "M,K,N,num_aie_columns,b_col_maj,c_col_maj,m,k,n,trace_size",
    all_params,
)
def test_gemm(
    M, K, N, num_aie_columns, b_col_maj, c_col_maj, m, k, n, trace_size, aie_context
):
    golden_ref = generate_golden_reference(
        M=M,
        K=K,
        N=N,
        b_col_maj=b_col_maj,
        c_col_maj=c_col_maj,
    )

    operator = AIEGEMM(
        M=M,
        K=K,
        N=N,
        num_aie_columns=num_aie_columns,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        b_col_maj=b_col_maj,
        c_col_maj=c_col_maj,
        context=aie_context,
    )

    input_buffers = {
        "A": golden_ref["input"].flatten(),
        "B": golden_ref["input_b"].flatten(),
    }
    output_buffers = {"C": golden_ref["output"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.005, abs_tol=0.005
    )

    gflops = (2.0 * M * K * N) / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s")
    print(f"Throughput: {gflops:.6e} GFLOP/s\n")

    assert not errors, f"Test failed with errors: {errors}"
