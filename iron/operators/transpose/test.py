#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.transpose.op import Transpose
from iron.operators.transpose.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols
    input_lengths = [64, 2048]
    n_list = [64, 128, 256, 512]
    s_list = [8]
    m = 64
    n = 64

    params = []
    for M in input_lengths:
        for N in n_list:
            for s in s_list:
                for num_aie_columns in range(1, max_aie_columns + 1):
                    for num_channels in [1, 2]:
                        row_part = M // num_channels
                        col_part = N // num_aie_columns
                        if row_part % m != 0 or col_part % n != 0:
                            continue
                        check_length = (
                            row_part * col_part * num_channels * num_aie_columns
                        )
                        length = M * N
                        if check_length != length:
                            continue

                        is_regular = M == 2048 and N == 64
                        marks = [] if is_regular else [pytest.mark.extensive]

                        params.append(
                            pytest.param(
                                M,
                                N,
                                num_aie_columns,
                                num_channels,
                                m,
                                n,
                                s,
                                1,
                                marks=marks,
                            )
                        )

    # num_batches>1: batch B independent same-shape transposes into one dispatch
    # (regular shape, single column/channel). num_batches=2 runs in the default
    # suite; the larger batch is extensive.
    for nb in (2, 4):
        params.append(
            pytest.param(
                2048,
                64,
                1,
                1,
                m,
                n,
                8,
                nb,
                marks=[] if nb == 2 else [pytest.mark.extensive],
            )
        )

    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("M,N,aie_columns,channels,m,n,s,num_batches", get_params())
def test_transpose(M, N, aie_columns, channels, m, n, s, num_batches, aie_context):
    golden_ref = generate_golden_reference(rows=M, cols=N, num_batches=num_batches)

    operator = Transpose(
        M=M,
        N=N,
        num_aie_columns=aie_columns,
        num_channels=channels,
        m=m,
        n=n,
        s=s,
        num_batches=num_batches,
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
