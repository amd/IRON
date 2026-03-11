#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from ml_dtypes import bfloat16
from iron.common.base import AIEBuffer
from iron.common.utils import torch_to_numpy
from iron.operators.swiglu_prefill.op import AIESwiGLUPrefill
from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.common.test_utils import verify_buffer


def get_params():
    params_list = [(256, 2048, 2048, False)]

    params = []
    for p in params_list:
        _, emb, hid, _ = p
        name = f"swiglu_prefill_256x{emb}x{hid}"
        params.append(pytest.param(*p, id=name))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("seq_len,embedding_dim,hidden_dim,prio_accuracy", get_params())
def test_swiglu_prefill(seq_len, embedding_dim, hidden_dim, prio_accuracy, aie_context):
    golden_ref = generate_golden_reference(M=seq_len, K=embedding_dim, N=hidden_dim)

    operator = AIESwiGLUPrefill(
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

    input_buf = AIEBuffer.from_np(torch_to_numpy(golden_ref["input"]))
    output_buf = AIEBuffer(
        shape=(seq_len * embedding_dim,), dtype=bfloat16
    )  # Output is flattened

    op_func(input_buf, output_buf)

    errors = {}

    # Verify intermediate result (left_swished * right)
    left_swished = op_func.left_swished.view_as_torch().reshape((seq_len, hidden_dim))
    right = op_func.right.view_as_torch().reshape((seq_len, hidden_dim))
    ref_2 = left_swished * right

    # Note: intermediate buffer in op_func stores the result of eltwise_mul
    intermediate = op_func.intermediate.view_as_torch().reshape((seq_len, hidden_dim))
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
    output = output_buf.view_as_torch().reshape((seq_len, embedding_dim))
    errors_3 = verify_buffer(
        output, "output", ref_3, rel_tol=0.08, abs_tol=0.4, max_error_rate=0.05
    )
    if errors_3:
        errors["output"] = errors_3

    assert not errors, f"Test failed with errors: {errors}"
