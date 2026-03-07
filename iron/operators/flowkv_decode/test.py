#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.flowkv_decode.op import AIEFlowKVDecode, pack_q_with_angles
from iron.operators.flowkv_decode.reference import generate_golden_reference
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    params = [
        # (num_heads, num_kv_heads, head_dim, seq_len, chunk_size, num_cols)
        (32, 8, 64, 128, 32, 4),
    ]
    if extensive:
        params += [
            (32, 8, 64, 256, 32, 4),
            (32, 8, 64, 512, 32, 8),
            (32, 8, 64, 1024, 32, 4),
        ]
    names = [
        f"flowkv_decode_{nh}h_{nkv}kv_{d}d_{s}s_{cs}cs_{nc}col"
        for nh, nkv, d, s, cs, nc in params
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
    "num_heads,num_kv_heads,head_dim,seq_len,chunk_size,num_cols",
    all_params,
)
def test_flowkv_decode(
    num_heads,
    num_kv_heads,
    head_dim,
    seq_len,
    chunk_size,
    num_cols,
    aie_context,
):
    golden_ref = generate_golden_reference(
        num_heads=num_heads,
        num_kv_heads=num_kv_heads,
        head_dim=head_dim,
        seq_len=seq_len,
    )

    operator = AIEFlowKVDecode(
        num_heads=num_heads,
        num_kv_heads=num_kv_heads,
        head_dim=head_dim,
        seq_len=seq_len,
        chunk_size=chunk_size,
        num_cols=num_cols,
        context=aie_context,
    )

    group_size = num_heads // num_kv_heads
    q_packed = pack_q_with_angles(
        golden_ref["Q"],
        golden_ref["q_angles"],
        group_size,
        num_kv_heads,
    )

    input_buffers = {
        "kv_cache": golden_ref["KV_interleaved"],
        "queries": q_packed,
    }
    output_buffers = {"output": golden_ref["O"]}

    # Online softmax + bf16 GEMV accumulates rounding error across chunks.
    # Tolerance ladder: standalone ops use 0.04/1e-6, composed operators
    # like SwiGLU use 0.07/1.0. FlowKV is similarly composed.
    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.07,
        abs_tol=1.0,
    )

    print(f"\nLatency (us): {latency_us:.1f}")

    # Compute throughput: 2 * num_heads * seq_len * head_dim FLOPs (Q@K + attn@V)
    flops = 2.0 * 2 * num_heads * seq_len * head_dim
    gflops = flops / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
