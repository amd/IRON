# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SwiGLU feed-forward over a sequence, as a graph function.

``W_down @ (SiLU(W_gate @ x) * (W_up @ x))`` for ``seq_len`` tokens. The
weights are closed over, so they are uploaded once; the gate and up
projections share one GEMM array and one build. Nothing is padded: a
sequence length the GEMM cannot tile is an error at trace time.
"""

import aie.utils as aie_utils

import iron
from iron.common.utils import get_shim_dma_limit
from iron.operators.elementwise_mul.op import ElementwiseMul
from iron.operators.gemm.op import GEMM
from iron.operators.silu.op import SiLU


def swiglu_prefill(w_gate, w_up, w_down, *, prio_accuracy=False, num_aie_columns=None):
    """The graph function for a sequence.

    ``w_gate`` and ``w_up`` are ``(embedding_dim, hidden_dim)`` and ``w_down``
    is ``(hidden_dim, embedding_dim)``: the ``(K, N)`` layout GEMM's ``B``
    takes, so a checkpoint's projection weights go in as they are.
    """
    embedding_dim, hidden_dim = w_gate.shape
    if tuple(w_up.shape) != (embedding_dim, hidden_dim) or tuple(w_down.shape) != (
        hidden_dim,
        embedding_dim,
    ):
        raise ValueError(
            f"swiglu_prefill: w_gate {tuple(w_gate.shape)}, w_up {tuple(w_up.shape)} "
            f"and w_down {tuple(w_down.shape)} do not agree on (embedding, hidden)"
        )
    accuracy = (
        dict(
            emulate_bf16_mmul_with_bfp16=False, prio_accuracy=True, round_conv_even=True
        )
        if prio_accuracy
        else {}
    )

    @iron.graph
    def prefill(x):
        cols = (
            num_aie_columns or get_shim_dma_limit(aie_utils.get_current_device()) // 2
        )
        gate = GEMM(x, w_gate, num_aie_columns=cols, **accuracy)
        up = GEMM(x, w_up, num_aie_columns=cols, **accuracy)
        swished = SiLU(gate, num_aie_columns=cols, tile_size=hidden_dim // cols)
        act = ElementwiseMul(
            swished, up, num_aie_columns=cols, tile_size=hidden_dim // cols
        )
        return GEMM(act, w_down, num_aie_columns=cols, **accuracy)

    return prefill


SwiGLUPrefill = swiglu_prefill
