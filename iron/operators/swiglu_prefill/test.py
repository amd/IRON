#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import pytest

from iron.operators.gemm.op import GEMM
from iron.operators.swiglu_prefill.op import SwiGLUPrefill

# swiglu_prefill shares the same reference implementation as swiglu_decode:
# both compute W3 @ (SiLU(W1 @ x) * (W2 @ x)), differing only in that prefill
# operates on a full sequence (M > 1) while decode operates on a single token (M = 1).
from iron.operators.swiglu_decode.reference import generate_golden_reference
from iron.common.test_utils import verify_buffer


def get_params():
    params_list = [
        (256, 2048, 2048, False, False),
        (256, 2048, 2048, False, True),
    ]

    params = []
    for p in params_list:
        params.append(pytest.param(*p))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "seq_len,embedding_dim,hidden_dim,prio_accuracy,b_col_maj", get_params()
)
def test_swiglu_prefill(
    seq_len, embedding_dim, hidden_dim, prio_accuracy, b_col_maj, aie_context
):
    golden_ref = generate_golden_reference(M=seq_len, K=embedding_dim, N=hidden_dim)

    operator = SwiGLUPrefill(
        seq_len=seq_len,
        embedding_dim=embedding_dim,
        hidden_dim=hidden_dim,
        prio_accuracy=bool(prio_accuracy),
        b_col_maj=bool(b_col_maj),
        context=aie_context,
    )
    operator.compile()
    fc = operator.get_callable()

    # GEMM takes its ``B`` operand in (K, N) layout, or (N, K) under b_col_maj.
    def _as_stored(w):
        return (w.t().contiguous() if b_col_maj else w).reshape(-1)

    fc.get_buffer("w_gate").torch_view()[:] = _as_stored(golden_ref["w_gate"])
    fc.get_buffer("w_up").torch_view()[:] = _as_stored(golden_ref["w_up"])
    fc.get_buffer("w_down").torch_view()[:] = _as_stored(golden_ref["w_down"])
    # Push the persistent weight buffers to the device.
    for name in ("w_gate", "w_up", "w_down"):
        fc.get_buffer(name).to("npu")

    # Set the per-invocation input.
    fc.get_buffer("in").torch_view()[:] = golden_ref["input"].reshape(-1)

    # Warmup
    fc()

    start = time.perf_counter()
    fc()
    elapsed_us = (time.perf_counter() - start) * 1e6

    total_bytes = (golden_ref["input"].numel() + seq_len * embedding_dim) * 2  # bf16
    bandwidth_gbps = total_bytes / (elapsed_us * 1e-6) / 1e9
    print(f"Latency (us): {elapsed_us:.2f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.4f} GB/s")

    errors = {}

    # Bring the buffers we verify back to the host.
    for name in ("left_swished", "right", "intermediate", "out"):
        fc.get_buffer(name).to("cpu")

    # Verify intermediate result (left_swished * right)
    left_swished = (
        fc.get_buffer("left_swished").torch_view().reshape((seq_len, hidden_dim))
    )
    right = fc.get_buffer("right").torch_view().reshape((seq_len, hidden_dim))
    ref_2 = left_swished * right

    # Note: intermediate buffer stores the result of eltwise_mul
    intermediate = (
        fc.get_buffer("intermediate").torch_view().reshape((seq_len, hidden_dim))
    )
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
    output = fc.get_buffer("out").torch_view().reshape((seq_len, embedding_dim))
    errors_3 = verify_buffer(
        output, "output", ref_3, rel_tol=0.08, abs_tol=0.4, max_error_rate=0.05
    )
    if errors_3:
        errors["output"] = errors_3

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.parametrize("b_col_maj", [False, True])
def test_weight_layout_reaches_both_gemms(b_col_maj):
    """Construction only: the layout must reach every GEMM and the design name."""
    op = SwiGLUPrefill(
        seq_len=256, embedding_dim=2048, hidden_dim=2048, b_col_maj=b_col_maj
    )
    gemms = [step[0] for step in op.runlist if isinstance(step[0], GEMM)]
    assert gemms and all(g.b_col_maj == b_col_maj for g in gemms)
    assert op.name.endswith("_bc") == b_col_maj
