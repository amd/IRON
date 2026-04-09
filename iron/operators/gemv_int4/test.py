#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import torch
import aie.utils as aie_utils

from iron.operators.gemv_int4.op import GEMVInt4
from iron.operators.gemv_int4.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols

    params_list = [
        # (M, K, num_aie_columns, tile_size_input, tile_size_output, group_size)
        (2048, 2048, 4, 1, 512, 32),  # Basic, 4 cols
        (8192, 2048, 4, 1, 2048, 32),  # Llama down_proj, 4 cols
        (2048, 8192, 4, 1, 512, 32),  # Llama up_proj, 4 cols
        (2048, 8192, 8, 1, 256, 32),  # Llama up_proj, 8 cols
        (8192, 2048, 8, 1, 1024, 32),  # Llama down_proj, 8 cols
        (2048, 8192, 4, 4, 512, 32),  # tsi=4 for better amortization
        (8192, 2048, 4, 4, 2048, 32),  # tsi=4
    ]

    params = []
    for p in params_list:
        M, K, num_aie_columns, tile_size_input, tile_size_output, group_size = p
        # Skip tests that require more columns than available on the device
        if num_aie_columns > max_aie_columns:
            continue
        params.append(
            pytest.param(
                *p,
                id=f"gemv_int4_{M}x{K}_{tile_size_input}tsi_{tile_size_output}tso_{num_aie_columns}col_g{group_size}",
            )
        )
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output,group_size", get_params()
)
def test_gemv_int4(
    M, K, num_aie_columns, tile_size_input, tile_size_output, group_size, aie_context
):
    golden_ref = generate_golden_reference(
        M=M,
        K=K,
        group_size=group_size,
        m_input=tile_size_input,
        cols=num_aie_columns,
    )

    operator = GEMVInt4(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        group_size=group_size,
        context=aie_context,
    )

    input_buffers = {
        "packed_weights": torch.from_numpy(golden_ref["packed_weights"]),
        "vector": golden_ref["x"],
    }
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.07, abs_tol=0.7
    )

    print(f"\nLatency (us): {latency_us:.1f}")

    gflops = (2.0 * M * K) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.2e} GFLOP/s")

    # INT4 weights: M*K/2 bytes + scales (bf16): M*(K//group_size)*2 bytes
    weight_bytes = M * K / 2 + M * (K // group_size) * 2
    vector_bytes = K * 2  # bf16
    output_bytes = M * 2  # bf16
    total_bytes = weight_bytes + vector_bytes + output_bytes
    bandwidth = total_bytes / (latency_us * 1e-6) / 1e9
    print(f"Effective Bandwidth: {bandwidth:.2e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
