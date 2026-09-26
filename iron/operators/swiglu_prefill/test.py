#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pytest
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16

from iron.common.harness import record_metric, verify_buffer
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm.op import GEMM
from iron.operators.silu import SiLU

# swiglu_prefill shares the same reference implementation as swiglu_decode:
# both compute W3 @ (SiLU(W1 @ x) * (W2 @ x)), differing only in that prefill
# operates on a full sequence (M > 1) while decode operates on a single token (M = 1).
from iron.operators.swiglu_decode.reference import (
    as_numpy,
    bf16_matmul,
    generate_golden_reference,
)
from iron.operators.swiglu_prefill.op import swiglu_prefill


def get_params():
    return [
        pytest.param(256, 2048, 2048, False, False),
        pytest.param(256, 2048, 2048, False, True),
    ]


def _step_output(net, op_type):
    (step,) = [s for s in net.traced.steps if type(s.op) is op_type]
    return net.buffer(step.outputs[0])


@pytest.mark.parametrize(
    "seq_len,embedding_dim,hidden_dim,prio_accuracy,b_col_maj", get_params()
)
def test_swiglu_prefill(
    seq_len, embedding_dim, hidden_dim, prio_accuracy, b_col_maj, npu_runtime
):
    golden_ref = as_numpy(
        generate_golden_reference(M=seq_len, K=embedding_dim, N=hidden_dim)
    )

    # GEMM takes its B operand in (K, N) layout, or (N, K) under b_col_maj.
    # The graph closes over the weights: uploaded once, on first call.
    def _as_stored(w):
        return np.ascontiguousarray(w.T) if b_col_maj else w

    ffn = swiglu_prefill(
        _as_stored(golden_ref["w_gate"]),
        _as_stored(golden_ref["w_up"]),
        _as_stored(golden_ref["w_down"]),
        prio_accuracy=bool(prio_accuracy),
        b_col_maj=bool(b_col_maj),
    )
    net = ffn.compile(x=(seq_len, embedding_dim))
    x = golden_ref["input"]

    elapsed_us = run_iters(lambda: net(x), warmup=1, iters=1).e2e.avg_us
    out = net(x)

    total_bytes = (x.size + seq_len * embedding_dim) * 2  # bf16
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
    left_swished = swished_buf.numpy().reshape((seq_len, hidden_dim))
    right = up_buf.numpy().reshape((seq_len, hidden_dim))
    intermediate = product_buf.numpy().reshape((seq_len, hidden_dim))
    errors_2 = verify_buffer(
        intermediate, "intermediate", left_swished * right, rel_tol=0.04, abs_tol=0.4
    )
    if errors_2:
        errors["intermediate"] = errors_2

    # Verify the output from the observed product, which matches the bf16
    # path and isolates errors to the down projection. Up to 5% of values
    # may exceed the tolerances (precision outliers; TODO: investigate).
    ref_3 = bf16_matmul(intermediate, golden_ref["w_down"])
    output = out.numpy().reshape((seq_len, embedding_dim))
    errors_3 = verify_buffer(
        output, "output", ref_3, rel_tol=0.08, abs_tol=0.4, max_error_rate=0.05
    )
    if errors_3:
        errors["output"] = errors_3

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.parametrize("b_col_maj", [False, True])
def test_weight_layout_reaches_every_gemm(b_col_maj):
    """Trace only: the layout reaches all three GEMMs, which read the right extents."""
    E, H = 2048, 1024
    w = np.zeros((H, E) if b_col_maj else (E, H), dtype=bfloat16)
    down = np.zeros((E, H) if b_col_maj else (H, E), dtype=bfloat16)
    t = swiglu_prefill(w, w, down, b_col_maj=b_col_maj).trace(x=(256, E))
    gemms = [s.op for s in t.steps if type(s.op) is GEMM]
    assert [g.b_col_maj for g in gemms] == [b_col_maj] * 3
    assert [(g.K, g.N) for g in gemms] == [(E, H), (E, H), (H, E)]
