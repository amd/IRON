#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from aie.utils.benchmark import run_iters

from iron.common.harness import record_metric, verify_buffer
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv.op import GEMV
from iron.operators.silu import SiLU
from iron.operators.swiglu_decode.op import swiglu_decode
from iron.operators.swiglu_decode.reference import (
    as_numpy,
    bf16_matmul,
    generate_golden_reference,
)


def get_params():
    # (embedding_dim, hidden_dim)
    # Square shape is the historical smoke-test config; the rectangular
    # shape reflects real decoder-model FFN dims (e.g. Qwen3.5-0.8B
    # embedding=1024, hidden=3584) that downstream runtimes actually hit.
    return [pytest.param(2048, 2048), pytest.param(1024, 3584)]


def _step_output(net, op_type):
    """The device buffer holding the output of the graph's one ``op_type`` step."""
    (step,) = [s for s in net.traced.steps if type(s.op) is op_type]
    return net.buffer(step.outputs[0])


@pytest.mark.parametrize("embedding_dim,hidden_dim", get_params())
def test_swiglu_decode(embedding_dim, hidden_dim, npu_runtime):
    golden_ref = as_numpy(generate_golden_reference(M=1, K=embedding_dim, N=hidden_dim))

    # GEMV takes its matrix in (M, K) layout, so the projections go in
    # transposed. The graph closes over them: uploaded once, on first call.
    ffn = swiglu_decode(
        np.ascontiguousarray(golden_ref["w_gate"].T),
        np.ascontiguousarray(golden_ref["w_up"].T),
        np.ascontiguousarray(golden_ref["w_down"].T),
    )
    net = ffn.compile(x=(1, embedding_dim))
    x = golden_ref["input"]

    elapsed_us = run_iters(lambda: net(x), warmup=1, iters=1).e2e.avg_us
    out = net(x)

    total_bytes = (x.size + embedding_dim) * 2  # bf16
    record_metric("Latency", elapsed_us)
    record_metric("Bandwidth", total_bytes / (elapsed_us * 1e-6) / 1e9)

    errors = {}

    # Verify the elementwise product against a chained reference built from
    # the observed SiLU and up-projection buffers. This isolates it from any
    # sub-tolerance drift accumulated upstream that multiplication against a
    # large-magnitude operand would amplify.
    swished_buf = _step_output(net, SiLU)
    product_buf = _step_output(net, ElementwiseMul)
    # The second GEMV is the up projection; the gate's buffer is dead by the
    # time the product is written, so the planner may reuse it.
    up_step = [s for s in net.traced.steps if type(s.op) is GEMV][1]
    for buf in (swished_buf, product_buf):
        buf.to("cpu")
    up_buf = net.buffer(up_step.outputs[0])
    up_buf.to("cpu")
    left_swished = swished_buf.numpy().reshape((1, hidden_dim))
    right = up_buf.numpy().reshape((1, hidden_dim))
    intermediate = product_buf.numpy().reshape((1, hidden_dim))
    errors_intermediate = verify_buffer(
        intermediate, "intermediate", left_swished * right, rel_tol=0.04, abs_tol=0.4
    )
    if errors_intermediate:
        errors["intermediate"] = errors_intermediate

    # Verify the output from the observed product, which matches the bf16
    # path and isolates errors to the down projection.
    ref_output = bf16_matmul(intermediate, golden_ref["w_down"])
    output = out.numpy().reshape((1, embedding_dim))
    errors_output = verify_buffer(
        output, "output", ref_output, rel_tol=0.04, abs_tol=0.4
    )
    if errors_output:
        errors["output"] = errors_output

    assert not errors, f"Test failed with errors: {errors}"
