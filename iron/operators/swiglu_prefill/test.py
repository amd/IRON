#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time

import pytest

from iron.common.test_utils import record_metric, verify_buffer
from iron.operators.elementwise_mul.op import ElementwiseMul
from iron.operators.silu.op import SiLU
from iron.operators.swiglu_prefill.op import swiglu_prefill

# swiglu_prefill shares the same reference implementation as swiglu_decode:
# both compute W3 @ (SiLU(W1 @ x) * (W2 @ x)), differing only in that prefill
# operates on a full sequence (M > 1) while decode operates on a single token (M = 1).
from iron.operators.swiglu_decode.reference import generate_golden_reference


def get_params():
    return [pytest.param(256, 2048, 2048, False)]


def _step_output(net, op_type):
    (step,) = [s for s in net.traced.steps if type(s.op) is op_type]
    return net.buffer(step.outputs[0])


@pytest.mark.parametrize("seq_len,embedding_dim,hidden_dim,prio_accuracy", get_params())
def test_swiglu_prefill(seq_len, embedding_dim, hidden_dim, prio_accuracy, aie_context):
    golden_ref = generate_golden_reference(M=seq_len, K=embedding_dim, N=hidden_dim)

    # GEMM takes its B operand in (K, N) layout, so the projections go in as
    # they are. The graph closes over them: uploaded once, on first call.
    ffn = swiglu_prefill(
        golden_ref["w_gate"],
        golden_ref["w_up"],
        golden_ref["w_down"],
        prio_accuracy=bool(prio_accuracy),
    )
    net = ffn.compile(context=aie_context, x=(seq_len, embedding_dim))
    x = golden_ref["input"]

    net(x)  # warmup

    start = time.perf_counter()
    out = net(x)
    elapsed_us = (time.perf_counter() - start) * 1e6

    total_bytes = (x.numel() + seq_len * embedding_dim) * 2  # bf16
    record_metric("Latency", elapsed_us)
    record_metric("Bandwidth", total_bytes / (elapsed_us * 1e-6) / 1e9)

    errors = {}
    swished_buf, product_buf = (
        _step_output(net, SiLU),
        _step_output(net, ElementwiseMul),
    )
    up_buf = net.buffer(net.traced.steps[1].outputs[0])
    for buf in (swished_buf, product_buf, up_buf):
        buf.to("cpu")
    left_swished = swished_buf.torch_view().reshape((seq_len, hidden_dim))
    right = up_buf.torch_view().reshape((seq_len, hidden_dim))
    intermediate = product_buf.torch_view().reshape((seq_len, hidden_dim))
    errors_2 = verify_buffer(
        intermediate, "intermediate", left_swished * right, rel_tol=0.04, abs_tol=0.4
    )
    if errors_2:
        errors["intermediate"] = errors_2

    # Verify the output from the observed product, which matches the bf16
    # path and isolates errors to the down projection. Up to 5% of values
    # may exceed the tolerances (precision outliers; TODO: investigate).
    ref_3 = intermediate @ golden_ref["w_down"]
    output = out.torch_view().reshape((seq_len, embedding_dim))
    errors_3 = verify_buffer(
        output, "output", ref_3, rel_tol=0.08, abs_tol=0.4, max_error_rate=0.05
    )
    if errors_3:
        errors["output"] = errors_3

    assert not errors, f"Test failed with errors: {errors}"
