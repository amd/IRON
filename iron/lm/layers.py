# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The layers a decoder builds from operators, for a graph's body.

``project`` is a weight's projection at either row count. ``swiglu``
is the SwiGLU feed-forward, ``W_down @ (SiLU(W_gate @ x) * (W_up @ x))``,
for one token or a sequence, and ``SwiGLU`` is it as a graph of its
own, holding the weights, so they are uploaded once.

The weights are a checkpoint's ``(out, in)``: SwiGLU's ``w_gate`` and
``w_up`` are ``(hidden_dim, embedding_dim)`` and ``w_down`` is
``(embedding_dim, hidden_dim)``. One row projects with GEMV, more with
GEMM; the gate and up projections share one array and one build. Nothing
is padded: a row count the GEMM cannot tile is an error at trace time.
"""

import iron
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU


def project(x, weight, **gemv):
    """``x @ weight.T`` for a checkpoint's ``(out, in)`` weight: a GEMV for
    one row (a GEMV's output is a vector), else a GEMM reading it
    column-major. ``gemv`` are the GEMV's tunables, where the profile cannot
    tell it from another of its shape.
    """
    if len(x.shape) == 2 and x.shape[0] > 1:
        return GEMM(x, weight, b_col_maj=True)
    return GEMV(weight, x, **gemv)


def swiglu(x, w_gate, w_up, w_down):
    """The feed-forward of ``x``, ``(rows, embedding_dim)``."""
    gate, up = project(x, w_gate), project(x, w_up)
    return project(ElementwiseMul(SiLU(gate), up), w_down)


class SwiGLU(iron.Graph):
    """The feed-forward as a graph, over the ``(out, in)`` weights it holds."""

    def __init__(self, w_gate, w_up, w_down):
        hidden_dim, embedding_dim = w_gate.shape
        if tuple(w_up.shape) != (hidden_dim, embedding_dim) or tuple(w_down.shape) != (
            embedding_dim,
            hidden_dim,
        ):
            raise ValueError(
                f"SwiGLU: w_gate {tuple(w_gate.shape)}, w_up {tuple(w_up.shape)} "
                f"and w_down {tuple(w_down.shape)} do not agree on (hidden, "
                "embedding)"
            )
        self.w_gate, self.w_up, self.w_down = w_gate, w_up, w_down

    def body(self, x):
        return swiglu(x, self.w_gate, self.w_up, self.w_down)
