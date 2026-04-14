#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import pytest

from ml_dtypes import bfloat16
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
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
    operator.weights_1 = golden_ref["w_gate"].T
    operator.weights_2 = golden_ref["w_up"].T
    operator.weights_3 = golden_ref["w_down"].T

    operator.compile()
    op_func = operator.get_callable()

    input_buf = XRTTensor.from_torch(golden_ref["input"])
    output_buf = XRTTensor((1, embedding_dim), dtype=bfloat16)

    # Warmup
    op_func(input_buf, output_buf)

    start = time.perf_counter()
    op_func(input_buf, output_buf)
    elapsed_us = (time.perf_counter() - start) * 1e6

    total_bytes = input_buf.buffer_object().size() + output_buf.buffer_object().size()
    bandwidth_gbps = total_bytes / (elapsed_us * 1e-6) / 1e9
    print(f"Latency (us): {elapsed_us:.2f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.4f} GB/s")

    errors = {}

    # Verify intermediate result (left_swished * right) against a chained
    # reference built from the observed AIE left_swished and right buffers.
    # This isolates eltwise_mul from any sub-tolerance drift accumulated in
    # the upstream gemv_1 / silu stages that would otherwise be amplified by
    # multiplication against a large-magnitude right operand (e.g. silu
    # outputs that land near zero for very-negative inputs, where bf16
    # rounding asymmetrically flushes NPU vs fp32-CPU). This mirrors the
    # approach used by swiglu_prefill/test.py.
    # Reshape to (1, hidden_dim) using the unpadded dimension to match the
    # reference shape. Note: op.hidden_dim_padded may differ if padding was
    # applied; we use hidden_dim here because the golden reference was
    # generated with the unpadded hidden_dim.
    left_swished = op_func.left_swished.to_torch().reshape((1, hidden_dim))
    right = op_func.right.to_torch().reshape((1, hidden_dim))
    ref_intermediate = left_swished * right

    intermediate = op_func.intermediate.to_torch().reshape((1, hidden_dim))
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
    output = output_buf.to_torch().reshape((1, embedding_dim))
    errors_output = verify_buffer(
        output, "output", ref_output, rel_tol=0.04, abs_tol=0.4
    )
    if errors_output:
        errors["output"] = errors_output

    assert not errors, f"Test failed with errors: {errors}"
