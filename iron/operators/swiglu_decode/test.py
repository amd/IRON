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


def get_params():
    params_list = [(2048, 2048)]

    params = []
    for p in params_list:
        emb, hid = p
        name = f"swiglu_decode_1x{emb}x{hid}"
        params.append(pytest.param(*p, id=name))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("embedding_dim,hidden_dim", get_params())
def test_swiglu_decode(embedding_dim, hidden_dim, aie_context):
    golden_ref = generate_golden_reference(M=1, K=embedding_dim, N=hidden_dim)

    operator = AIESwiGLUDecode(
        embedding_dim=embedding_dim, hidden_dim=hidden_dim, context=aie_context
    )
    operator.weights_1 = golden_ref["w_gate"].T
    operator.weights_2 = golden_ref["w_up"].T
    operator.weights_3 = golden_ref["w_down"].T

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
