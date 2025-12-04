#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.swiglu_prefill.op import AIESwiGLUPrefill
from operators.swiglu_decode.reference import generate_golden_reference
from operators.common.test_utils import run_test, verify_buffer


def generate_test_params(extensive=False):
    # This operation is currently untested except for the integrated llama application tests.
    params = []
    names = []
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s"
)
@pytest.mark.parametrize("seq_len,embedding_dim,hidden_dim,prio_accuracy", 
                         regular_params,
                         ids=regular_names)
def test_swiglu_prefill(seq_len, embedding_dim, hidden_dim, prio_accuracy, aie_context):
    golden_ref = generate_golden_reference(
        M=seq_len, K=embedding_dim, N=hidden_dim
    )

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
        "left_swished": golden_ref["left_swished"],
        "right": golden_ref["right"],
        # 'intermediate': golden_ref['intermediate']
    }

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        intermediate_buffers,
        rel_tol=0.07,
        abs_tol=0.7,
    )

    ref_2 = operator.read_buffer_as_torch(
        "left_swished", (seq_len, hidden_dim)
    ) * operator.read_buffer_as_torch("right", (seq_len, hidden_dim))
    errors_2 = verify_buffer(operator, "intermediate", ref_2, rel_tol=0.04, abs_tol=0.4)
    if errors_2:
        errors["intermediate"] = errors_2

    ref_3 = (
        operator.read_buffer_as_torch("intermediate", (seq_len, hidden_dim))
        @ golden_ref["w_down"]
    )
    errors_3 = verify_buffer(operator, "output", ref_3, rel_tol=0.04, abs_tol=0.4)
    if errors_3:
        errors["output"] = errors_2

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.extensive
@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s"
)
@pytest.mark.parametrize("seq_len,embedding_dim,hidden_dim,prio_accuracy", 
                         extensive_params,
                         ids=extensive_names)
def test_swiglu_prefill_extensive(seq_len, embedding_dim, hidden_dim, prio_accuracy, aie_context):
    test_swiglu_prefill(seq_len, embedding_dim, hidden_dim, prio_accuracy, aie_context)

