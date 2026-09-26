#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.common.device import bound_device, device_name
from iron.common.harness import record_metric, run_test, vectors
from iron.operators.gemm.op import GEMM


def get_params():
    dev = bound_device()
    max_aie_columns = dev.cols
    device_type = device_name(dev)
    # fmt: off
    #   M,     K,     N, num_aie_columns, b_col_maj, c_col_maj,   m,   k,   n
    regular_params = [
        (2048,  2048,  2048,               1,     False,     False,  64,  64,  64),
        (2048,  2048,  2048,               2,      True,     False,  64,  64,  64),
        (2048,  2048,  2048,               8,      True,      True,  64,  64,  64),
        ( 384,  1536,  1792,               4,      True,     False,  32,  48,  64),
        (1792,   896,  1152,               8,     False,      True,  64,  32,  48),
        ( 896,  1792,   640,               8,     False,      True,  32,  64,  80),
        ( 192,   384,    64,               4,     False,     False,  48,  96,  16),
        ( 192,   384,    64,               4,      True,      True,  48,  96,  16),
    ]
    extensive_params = [
        (2048,  2048,  2048,               8,     False,     False,  32,  32, 128),
        (2048,  2048,  8192,               2,     False,     False,  64,  64,  64),
        (2048,  8192,  2048,               2,     False,     False,  64,  64,  64),
        (2048,    64,  2048,               2,     False,     False,  64,  64,  64),
        (2048,    64,  8192,               2,     False,     False,  64,  64,  64),
        (2048,  2048,  2048,               8,      True,     False, 128,  32,  32),
        (2048,  2048,  8192,               2,      True,     False,  64,  64,  64),
        (2048,  8192,  2048,               2,      True,     False,  64,  64,  64),
        # Llama 3.2 1B prefill's down projection, as the graph runs it.
        (2048,  8192,  2048,               8,      True,     False,  64,  64,  64),
        (2048,    64,  2048,               2,      True,     False,  64,  64,  64),
        (2048,    64,  8192,               2,      True,     False,  64,  64,  64),
        (2048,  2048,  2048,               2,     False,      True,   8,  16,  32),
        (2048,  2048,  8192,               2,     False,      True,  64,  64,  64),
        (2048,  8192,  2048,               2,     False,      True,  64,  64,  64),
        (2048,    64,  2048,               2,     False,      True,  64,  64,  64),
        (2048,    64,  8192,               2,     False,      True,  64,  64,  64),
        # N wide enough that C's row stride (mem_tile_m_C * N) overflows the
        # shim BD's 20-bit iteration step, so the drain is issued as one
        # descriptor per row-block. Cover for that split.
        (1024,  2560, 10240,               8,     False,     False,  64,  64,  64),
        (2048,  2560, 10240,               8,     False,     False,  64,  64,  64),
    ]
    # fmt: on

    params = []

    # Helper to generate name and append param
    def add_params(param_list, is_extensive):
        for p in param_list:
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
            ) = p

            # Skip tests that require more columns than available on the device
            if num_aie_columns > max_aie_columns:
                continue

            # Skip configurations with small tile sizes that don't meet AIE2 kernel constraints
            # AIE2 mm kernel requires m % (4 * r) == 0 where r=4 for bf16
            if device_type == "npu1" and m < 16:
                continue

            marks = [pytest.mark.extensive] if is_extensive else []
            params.append(pytest.param(*p, marks=marks))

    add_params(regular_params, is_extensive=False)
    add_params(extensive_params, is_extensive=True)

    return params


@pytest.mark.parametrize(
    "M,K,N,num_aie_columns,b_col_maj,c_col_maj,m,k,n",
    get_params(),
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
    npu_runtime,
):
    operator = GEMM(
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
    )

    data = vectors(operator, normal=("A",))
    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=0.005, abs_tol=0.005
    )
    record_metric("Throughput", (2.0 * M * K * N) / (latency_us * 1e-6) / 1e9)

    assert not errors, "Test failed"
