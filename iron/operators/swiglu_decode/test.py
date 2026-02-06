#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from ml_dtypes import bfloat16
from iron.common.base import AIEBuffer
from iron.common.utils import torch_to_numpy
from iron.operators.swiglu_decode.op import AIESwiGLUDecode
from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.common.test_utils import verify_buffer


def generate_test_params(extensive=False):
    params = [(2048, 2048)]
    names = [f"swiglu_decode_1x{emb}x{hid}" for emb, hid in params]
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
@pytest.mark.parametrize("embedding_dim,hidden_dim", all_params)
def test_swiglu_decode(embedding_dim, hidden_dim, aie_context):
    golden_ref = generate_golden_reference(M=1, K=embedding_dim, N=hidden_dim)

    operator = AIESwiGLUDecode(
        embedding_dim=embedding_dim, hidden_dim=hidden_dim, context=aie_context
    )
    operator.weights_1 = golden_ref["w_gate"].T
    operator.weights_2 = golden_ref["w_up"].T
    operator.weights_3 = golden_ref["w_down"].T

    # In the following, some buffers are commented out.
    # Because this operator calls multiple kernels in sequence, rounding errors due to the smaller bf16 data type accumulate, which can cause it to fail verification.
    # So, instead of verifying the final output buffers against the float32-calculated reference, we calculate another reference for the final output:
    # This reference is based on the previous intermediate result read back from the AIE operator, "resetting"  the accumulated error to zero.
    # Note that the previous intermediate result _is_ still verified up to the given tolerance.

    operator.compile()
    op_func = operator.get_callable()

    input_buf = AIEBuffer.from_np(torch_to_numpy(golden_ref["input"]))
    output_buf = AIEBuffer(shape=(1, embedding_dim), dtype=bfloat16)

    op_func(input_buf, output_buf)

    errors = {}
    # Verify intermediate result
    intermediate = op_func.intermediate.view_as_torch().reshape((1, hidden_dim))
    errors_intermediate = verify_buffer(
        intermediate,
        "intermediate",
        golden_ref["intermediate"],
        rel_tol=0.07,
        abs_tol=0.7,
    )
    if errors_intermediate:
        errors["intermediate"] = errors_intermediate

    # Verify output using intermediate result
    ref_2 = intermediate @ golden_ref["w_down"]
    output = output_buf.view_as_torch().reshape((1, embedding_dim))
    errors_output = verify_buffer(output, "output", ref_2, rel_tol=0.04, abs_tol=0.4)
    if errors_output:
        errors["output"] = errors_output

    assert not errors, f"Test failed with errors: {errors}"
