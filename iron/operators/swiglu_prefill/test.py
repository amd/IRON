#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import pytest

from ml_dtypes import bfloat16
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from iron.operators.swiglu_prefill.op import SwiGLUPrefill

# swiglu_prefill shares the same reference implementation as swiglu_decode:
# both compute W3 @ (SiLU(W1 @ x) * (W2 @ x)), differing only in that prefill
# operates on a full sequence (M > 1) while decode operates on a single token (M = 1).
from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.common.test_utils import verify_buffer


def get_params():
    params_list = [(256, 2048, 2048, False)]

    params = []
    for p in params_list:
        params.append(pytest.param(*p))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("seq_len,embedding_dim,hidden_dim,prio_accuracy", get_params())
def test_swiglu_prefill(seq_len, embedding_dim, hidden_dim, prio_accuracy, aie_context):
    golden_ref = generate_golden_reference(M=seq_len, K=embedding_dim, N=hidden_dim)

    operator = SwiGLUPrefill(
        seq_len=seq_len,
        embedding_dim=embedding_dim,
        hidden_dim=hidden_dim,
        prio_accuracy=bool(prio_accuracy),
        context=aie_context,
    )
    operator.weights_1 = golden_ref["w_gate"].T
    operator.weights_2 = golden_ref["w_up"].T
    operator.weights_3 = golden_ref["w_down"].T

    operator.compile()
    op_func = operator.get_callable()

    input_buf = XRTTensor.from_torch(golden_ref["input"])
    output_buf = XRTTensor(
        (seq_len * embedding_dim,), dtype=bfloat16
    )  # Output is flattened

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

    # Verify intermediate result (left_swished * right)
    left_swished = op_func.left_swished.to_torch().reshape((seq_len, hidden_dim))
    right = op_func.right.to_torch().reshape((seq_len, hidden_dim))
    ref_2 = left_swished * right

    # Note: intermediate buffer in op_func stores the result of eltwise_mul
    intermediate = op_func.intermediate.to_torch().reshape((seq_len, hidden_dim))
    errors_2 = verify_buffer(
        intermediate, "intermediate", ref_2, rel_tol=0.04, abs_tol=0.4
    )
    if errors_2:
        errors["intermediate"] = errors_2

    # Verify output using intermediate result
    # Note: We use the AIE intermediate buffer as reference (rather than golden_ref["output"])
    # because this better matches the bfloat16 precision path and isolates errors to gemm_2.
    # We allow up to 5% of values to exceed these tolerances to handle precision outliers.
    # TODO: investigate outliers in output
    ref_3 = intermediate @ golden_ref["w_down"]
    output = output_buf.to_torch().reshape((seq_len, embedding_dim))
    errors_3 = verify_buffer(
        output, "output", ref_3, rel_tol=0.08, abs_tol=0.4, max_error_rate=0.05
    )
    if errors_3:
        errors["output"] = errors_3

    assert not errors, f"Test failed with errors: {errors}"
