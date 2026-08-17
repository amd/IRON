#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.swiglu_fused_front.reference import generate_golden_reference
from iron.common.test_utils import run_test
from iron.operators.swiglu_fused_front.op import SwigluFront


def get_params():
    dev = aie_utils.get_current_device()
    max_aie_columns = dev.cols
    device_type = dev.resolve().name
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
        (  64,   512,   256,               4,      True,     False,  16,  64,  64),
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
        (2048,    64,  2048,               2,      True,     False,  64,  64,  64),
        (2048,    64,  8192,               2,      True,     False,  64,  64,  64),
        (2048,  2048,  2048,               2,     False,      True,   8,  16,  32),
        (2048,  2048,  8192,               2,     False,      True,  64,  64,  64),
        (2048,  8192,  2048,               2,     False,      True,  64,  64,  64),
        (2048,    64,  2048,               2,     False,      True,  64,  64,  64),
        (2048,    64,  8192,               2,     False,      True,  64,  64,  64),
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


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,N,num_aie_columns,b_col_maj,c_col_maj,m,k,n",
    get_params(),
)
def test_swiglu_front(
    M,
    K,
    N,
    num_aie_columns,
    b_col_maj,
    c_col_maj,
    m,
    k,
    n,
    aie_context,
):
    golden_ref = generate_golden_reference(
        M=M,
        K=K,
        N=N,
        b_col_maj=b_col_maj,
        c_col_maj=c_col_maj,
    )

    operator = SwigluFront(
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
        context=aie_context,
    )

    input_buffers = {
        "A": golden_ref["input"].flatten(),
        "B": golden_ref["input_b"][0].flatten(),
    }
    output_buffers = {
        "C": golden_ref["output"][0].flatten(),
    }
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.005, abs_tol=0.005
    )

    gflops = (2.0 * M * K * N) / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s")
    print(f"Throughput: {gflops:.6e} GFLOP/s\n")

    assert not errors, "Test failed"
