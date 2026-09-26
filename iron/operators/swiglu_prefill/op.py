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
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm.op import GEMM
from iron.operators.silu import SiLU


def swiglu_prefill(
    w_gate, w_up, w_down, *, prio_accuracy=False, b_col_maj=False, num_aie_columns=None
):
    """The graph function for a sequence.

    ``b_col_maj`` selects the layout all three weights are stored in. When
    False, ``w_gate`` and ``w_up`` are ``(embedding_dim, hidden_dim)`` and
    ``w_down`` is ``(hidden_dim, embedding_dim)``: the ``(K, N)`` layout
    GEMM's ``B`` takes, so a checkpoint's projection weights go in as they
    are. When True each is stored transposed, the layout the decode-side
    GEMV reads, so a pipeline running both against the same weight buffers
    does not need a second copy of each.
    """
    if b_col_maj:
        hidden_dim, embedding_dim = w_gate.shape
    else:
        embedding_dim, hidden_dim = w_gate.shape
    expected_down = (
        (embedding_dim, hidden_dim) if b_col_maj else (hidden_dim, embedding_dim)
    )
    if tuple(w_up.shape) != tuple(w_gate.shape) or tuple(w_down.shape) != expected_down:
        raise ValueError(
            f"swiglu_prefill: w_gate {tuple(w_gate.shape)}, w_up {tuple(w_up.shape)} "
            f"and w_down {tuple(w_down.shape)} do not agree on (embedding, hidden) "
            f"at b_col_maj={b_col_maj}"
        )
    accuracy = (
        dict(
            emulate_bf16_mmul_with_bfp16=False, prio_accuracy=True, round_conv_even=True
        )
        if prio_accuracy
        else {}
    )
    projection = dict(b_col_maj=b_col_maj, **accuracy)

    @iron.graph
    def prefill(x):
        cols = num_aie_columns or GEMM.shim_columns(aie_utils.get_current_device())
        gate = GEMM(x, w_gate, num_aie_columns=cols, **projection)
        up = GEMM(x, w_up, num_aie_columns=cols, **projection)
        swished = SiLU(gate, num_aie_columns=cols, tile_size=hidden_dim // cols)
        act = ElementwiseMul(
            swished, up, num_aie_columns=cols, tile_size=hidden_dim // cols
        )
        return GEMM(act, w_down, num_aie_columns=cols, **projection)

    return prefill


SwiGLUPrefill = swiglu_prefill
