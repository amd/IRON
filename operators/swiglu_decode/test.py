#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.swiglu_decode.op import AIESwiGLUDecode
from operators.swiglu_decode.reference import generate_golden_reference
from operators.common.test_utils import run_test, verify_buffer


def generate_test_params(extensive=False):
    params = [(2048, 2048)]
    names = [f"swiglu_decode_1x{emb}x{hid}" for emb, hid in params]
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("embedding_dim,hidden_dim", regular_params, ids=regular_names)
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

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {}
    intermediate_buffers = {
        "left": golden_ref["left"],
        "left_swished": golden_ref["left_swished"],
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

    ref_2 = (
        operator.read_buffer_as_torch("intermediate", (1, hidden_dim))
        @ golden_ref["w_down"]
    )
    errors_2 = verify_buffer(operator, "output", ref_2, rel_tol=0.04, abs_tol=0.4)
    if errors_2:
        errors["output"] = errors_2

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.extensive
@pytest.mark.parametrize(
    "embedding_dim,hidden_dim", extensive_params, ids=extensive_names
)
def test_swiglu_decode_extensive(embedding_dim, hidden_dim, aie_context):
    test_swiglu_decode(embedding_dim, hidden_dim, aie_context)
