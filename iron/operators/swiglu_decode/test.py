#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import pytest

from iron.operators.swiglu_decode.op import SwiGLUDecode
from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.common.test_utils import verify_buffer


def get_params():
    # (embedding_dim, hidden_dim)
    # Square shape is the historical smoke-test config; the rectangular
    # shape reflects real decoder-model FFN dims (e.g. Qwen3.5-0.8B
    # embedding=1024, hidden=3584) that downstream runtimes actually hit.
    params_list = [
        (2048, 2048),
        (1024, 3584),
    ]

    params = []
    for p in params_list:
        params.append(pytest.param(*p))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("embedding_dim,hidden_dim", get_params())
def test_swiglu_decode(embedding_dim, hidden_dim, aie_context):
    golden_ref = generate_golden_reference(M=1, K=embedding_dim, N=hidden_dim)

    operator = SwiGLUDecode(
        embedding_dim=embedding_dim, hidden_dim=hidden_dim, context=aie_context
    )
    operator.compile()
    fc = operator.get_callable()

    # Upload the persistent weight buffers. GEMV takes its matrix in (M, K)
    # layout, so the projection weights go in transposed.
    fc.get_buffer("w_gate").torch_view()[:] = golden_ref["w_gate"].T.reshape(-1)
    fc.get_buffer("w_up").torch_view()[:] = golden_ref["w_up"].T.reshape(-1)
    fc.get_buffer("w_down").torch_view()[:] = golden_ref["w_down"].T.reshape(-1)
    # Push the persistent weight buffers to the device.
    for name in ("w_gate", "w_up", "w_down"):
        fc.get_buffer(name).to("npu")

    # Set the per-invocation input.
    fc.get_buffer("in").torch_view()[:] = golden_ref["input"].reshape(-1)

    # Warmup
    fc()

    start = time.perf_counter()
    fc()
    elapsed_us = (time.perf_counter() - start) * 1e6

    total_bytes = (golden_ref["input"].numel() + embedding_dim) * 2  # bf16
    bandwidth_gbps = total_bytes / (elapsed_us * 1e-6) / 1e9
    print(f"Latency (us): {elapsed_us:.2f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.4f} GB/s")

    errors = {}

    # Bring the buffers we verify back to the host.
    for name in ("left_swished", "right", "intermediate", "out"):
        fc.get_buffer(name).to("cpu")

    # Verify intermediate result (left_swished * right) against a chained
    # reference built from the observed AIE left_swished and right buffers.
    # This isolates eltwise_mul from any sub-tolerance drift accumulated in
    # the upstream gemv_1 / silu stages that would otherwise be amplified by
    # multiplication against a large-magnitude right operand (e.g. silu
    # outputs that land near zero for very-negative inputs, where bf16
    # rounding asymmetrically flushes NPU vs fp32-CPU). This mirrors the
    # approach used by swiglu_prefill/test.py.
    left_swished = fc.get_buffer("left_swished").torch_view().reshape((1, hidden_dim))
    right = fc.get_buffer("right").torch_view().reshape((1, hidden_dim))
    ref_intermediate = left_swished * right

    intermediate = fc.get_buffer("intermediate").torch_view().reshape((1, hidden_dim))
    errors_intermediate = verify_buffer(
        intermediate,
        "intermediate",
        ref_intermediate,
        rel_tol=0.04,
        abs_tol=0.4,
    )
    if errors_intermediate:
        errors["intermediate"] = errors_intermediate

    # Verify output using intermediate result.
    # Note: we use the AIE intermediate buffer as reference (rather than
    # golden_ref["output"]) because this better matches the bfloat16 precision
    # path and isolates errors to gemv_2.
    ref_output = intermediate @ golden_ref["w_down"]
    output = fc.get_buffer("out").torch_view().reshape((1, embedding_dim))
    errors_output = verify_buffer(
        output, "output", ref_output, rel_tol=0.04, abs_tol=0.4
    )
    if errors_output:
        errors["output"] = errors_output

    assert not errors, f"Test failed with errors: {errors}"
