#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SwiGLU on a device, one token and a sequence.

The product and the down projection are each judged against their
operator's reference, under its own tolerance, on the inputs the device
gave them, so a drift within tolerance upstream is not amplified into a
failure downstream.
"""

import numpy as np
import pytest
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16

from iron.common.harness import record_metric, verify_buffer
from iron.lm.layers import SwiGLU
from iron.operators.elementwise_mul import ElementwiseMul

# (rows, embedding_dim, hidden_dim). Qwen3.5-0.8B's FFN is 1024 by 3584.
SHAPES = [(1, 2048, 2048), (1, 1024, 3584), (256, 2048, 2048)]


def _weight(rng, rows, cols):
    """``(out, in)``, scaled so a projection keeps its input's magnitude:
    the gate stays where SiLU does not saturate.
    """
    return (rng.standard_normal((rows, cols)) / np.sqrt(cols)).astype(bfloat16)


def _read(net, handle):
    buf = net.buffer(handle)
    buf.to("cpu")
    return buf.numpy().reshape(tuple(handle.shape))


def _errors(net, step):
    """The step's output against its operator's reference on the inputs
    the device gave it.
    """
    inputs = [_read(net, h) for h in step.inputs]
    (output,) = [_read(net, h) for h in step.outputs]
    tolerance = step.op.reference_tolerance()
    bound = tolerance.bound(*inputs) if tolerance.kind == "bound" else None
    name = type(step.op).__name__
    expected = step.op.reference(*inputs)
    return verify_buffer(output, name, expected, tolerance, bound=bound)


@pytest.mark.parametrize("rows,embedding_dim,hidden_dim", SHAPES, ids=lambda v: str(v))
def test_swiglu(rows, embedding_dim, hidden_dim, npu_runtime):
    rng = np.random.default_rng(0)
    ffn = SwiGLU(
        _weight(rng, hidden_dim, embedding_dim),
        _weight(rng, hidden_dim, embedding_dim),
        _weight(rng, embedding_dim, hidden_dim),
    )
    net = ffn.compile(x=(rows, embedding_dim))
    x = rng.standard_normal((rows, embedding_dim)).astype(bfloat16)

    elapsed_us = run_iters(lambda: net(x), warmup=1, iters=1).e2e.avg_us
    net(x)
    record_metric("Latency", elapsed_us)
    record_metric("Bandwidth", 2 * x.nbytes / (elapsed_us * 1e-6) / 1e9)
    ops = sum(s.op.op_count() for s in net.traced.steps)
    record_metric("Throughput", ops / (elapsed_us * 1e-6) / 1e9)

    # The gate's buffer is dead once SiLU has read it, so the planner may
    # reuse it; the product's inputs and the down projection's are intact.
    (product,) = [s for s in net.traced.steps if type(s.op) is ElementwiseMul]
    down = net.traced.steps[-1]
    errors = {"product": _errors(net, product), "down": _errors(net, down)}
    assert not any(errors.values()), errors
