#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from pathlib import Path


import pytest
from iron.common.aie_device_manager import AIEDeviceManager
from iron.operators.transpose.op import AIETranspose
from iron.common.aie_device_manager import AIEDeviceManager
from iron.operators.transpose.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    # Detect device and set max columns accordingly
    # NPU1 (Phoenix) has 4 columns, NPU2 (Strix) has 8 columns
    device_type = AIEDeviceManager().device_str()
    max_aie_columns = 4 if device_type == "npu1" else 8
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
                        name = f"transpose_{M}_M_{N}_N_{num_aie_columns}_cols_{num_channels}_channels_{m}_m_{n}_n_{s}_s"

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
                                id=name,
                                marks=marks,
                            )
                        )

    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("M,N,aie_columns,channels,m,n,s", get_params())
def test_transpose(M, N, aie_columns, channels, m, n, s, aie_context):
    golden_ref = generate_golden_reference(rows=M, cols=N)

    operator = AIETranspose(
        M=M,
        N=N,
        num_aie_columns=aie_columns,
        num_channels=channels,
        m=m,
        n=n,
        s=s,
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
