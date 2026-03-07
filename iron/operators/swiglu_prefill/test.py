#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.operators.swiglu_prefill.op import AIESwiGLUPrefill
from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.common.test_utils import run_test, verify_buffer


def generate_test_params(extensive=False):
    # This operation is currently untested except for the integrated llama application tests.
    params = []
    names = []
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

    input_buffers = {"input": golden_ref["input"]}
    # output_buffers = {'output': golden_ref['output']}
    output_buffers = {}
    intermediate_buffers = {
        "left": golden_ref["left"],
        "right": golden_ref["right"],
        "intermediate": golden_ref["intermediate"],
    }

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        intermediate_buffers,
        rel_tol=0.07,
        abs_tol=0.7,
    )

    ref_3 = (
        operator.read_buffer_as_torch("intermediate", (seq_len, hidden_dim))
        @ golden_ref["w_down"]
    )
    errors_3 = verify_buffer(operator, "output", ref_3, rel_tol=0.04, abs_tol=0.4)
    if errors_3:
        errors["output"] = errors_3

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
