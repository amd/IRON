#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.dual_gemv_silu_mul.op import AIEDualGEMVSiLUMul, interleave_weights
from iron.operators.dual_gemv_silu_mul.reference import generate_golden_reference
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    params = [
        # (M, K, num_aie_columns, tile_size_input, tile_size_output)
        (2048, 2048, 4, 4, 512),
    ]
    if extensive:
        params += [
            (8192, 2048, 4, 4, 2048),
        ]
    names = [
        f"dual_gemv_silu_mul_{M}x{K}_{tsi}tsi_{tso}tso_{cols}col"
        for M, K, cols, tsi, tso in params
    ]
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

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
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output",
    all_params,
)
def test_dual_gemv_silu_mul(
    M, K, num_aie_columns, tile_size_input, tile_size_output, aie_context
):
    golden_ref = generate_golden_reference(M=M, K=K)

    operator = AIEDualGEMVSiLUMul(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        context=aie_context,
    )

    rows_per_col = M // num_aie_columns
    w_interleaved = interleave_weights(
        golden_ref["W1"], golden_ref["W2"], rows_per_col, num_aie_columns
    )

    input_buffers = {
        "weights_interleaved": w_interleaved.flatten(),
        "vector": golden_ref["x"],
    }
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.07, abs_tol=1.0
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
