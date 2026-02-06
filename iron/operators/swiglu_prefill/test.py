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


def generate_test_params(extensive=False):
    # This operation is currently untested except for the integrated llama application tests.
    params = [(256, 2048, 2048, False)]
    names = [f"swiglu_prefill_256x{emb}x{hid}" for _, emb, hid, _ in params]
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

# Combine params with marks - extensive params get pytest.mark.extensive
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
@pytest.mark.parametrize("seq_len,embedding_dim,hidden_dim,prio_accuracy", all_params)
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
    ref_3 = intermediate @ golden_ref["w_down"]
    output = output_buf.view_as_torch().reshape((seq_len, embedding_dim))
    errors_3 = verify_buffer(output, "output", ref_3, rel_tol=0.04, abs_tol=0.4)
    if errors_3:
        errors["output"] = errors_3

    assert not errors, f"Test failed with errors: {errors}"
