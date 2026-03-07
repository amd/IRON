#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import pytest

from iron.operators.fused_qkv_proj.op import AIEFusedQKVProj
from iron.operators.fused_qkv_proj.reference import generate_golden_reference
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    # (embedding_dim, q_dim, k_dim, v_dim, num_aie_columns, tile_size_input, tile_size_output)
    params = [
        # Llama 3.2 1B dimensions: M=3072, K=2048
        (2048, 2048, 512, 512, 4, 4, 768),
    ]
    if extensive:
        params += [
            # Llama 3.2 1B with 2 columns: M=3072, K=2048
            (2048, 2048, 512, 512, 2, 4, 1536),
        ]
    names = [
        (f"fused_qkv_proj_{q+k+v}x{emb}_" f"{tsi}tsi_{tso}tso_{cols}col")
        for emb, q, k, v, cols, tsi, tso in params
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
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "embedding_dim,q_dim,k_dim,v_dim,num_aie_columns,"
    "tile_size_input,tile_size_output",
    all_params,
)
def test_fused_qkv_proj(
    embedding_dim,
    q_dim,
    k_dim,
    v_dim,
    num_aie_columns,
    tile_size_input,
    tile_size_output,
    aie_context,
):
    golden_ref = generate_golden_reference(
        embedding_dim=embedding_dim,
        q_dim=q_dim,
        k_dim=k_dim,
        v_dim=v_dim,
    )

    operator = AIEFusedQKVProj(
        embedding_dim=embedding_dim,
        q_dim=q_dim,
        k_dim=k_dim,
        v_dim=v_dim,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        context=aie_context,
    )

    # Concatenate weights into the single matrix the GEMV expects
    w_combined = AIEFusedQKVProj.concatenate_weights(
        golden_ref["Wq"], golden_ref["Wk"], golden_ref["Wv"]
    )

    # Expected output is the concatenation of Q, K, V
    expected_output = torch.cat([golden_ref["Q"], golden_ref["K"], golden_ref["V"]])

    input_buffers = {
        "weights": w_combined.flatten(),
        "input": golden_ref["x"],
    }
    output_buffers = {"output": expected_output}

    total_out = q_dim + k_dim + v_dim

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
    )

    print(f"\nLatency (us): {latency_us:.1f}")

    gflops = (2.0 * total_out * embedding_dim) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
