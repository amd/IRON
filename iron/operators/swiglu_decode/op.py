# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SwiGLU feed-forward for one token, as a graph.

``W_down @ (SiLU(W_gate @ x) * (W_up @ x))``. The weights are the graph's,
so they are uploaded once; the gate and up projections share one GEMV
array and one build.
"""

import aie.utils as aie_utils

import iron
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv.op import GEMV
from iron.operators.silu import SiLU


class SwiGLUDecode(iron.Graph):
    """The feed-forward for one token.

    ``w_gate`` and ``w_up`` are ``(hidden_dim, embedding_dim)`` and ``w_down``
    is ``(embedding_dim, hidden_dim)``: the ``(M, K)`` layout GEMV takes, so
    a checkpoint's projection weights go in transposed. ``num_aie_columns``
    defaults to as many columns as GEMV's streams fit on the device.
    """

    def __init__(self, w_gate, w_up, w_down, *, num_aie_columns=None):
        hidden_dim, embedding_dim = w_gate.shape
        if tuple(w_up.shape) != (hidden_dim, embedding_dim) or tuple(w_down.shape) != (
            embedding_dim,
            hidden_dim,
        ):
            raise ValueError(
                f"SwiGLUDecode: w_gate {tuple(w_gate.shape)}, w_up "
                f"{tuple(w_up.shape)} and w_down {tuple(w_down.shape)} do not "
                f"agree on (hidden, embedding)"
            )
        self.w_gate, self.w_up, self.w_down = w_gate, w_up, w_down
        self.num_aie_columns = num_aie_columns

    def body(self, x):
        hidden_dim, embedding_dim = self.w_gate.shape
        cols = self.num_aie_columns or GEMV.shim_columns(aie_utils.get_current_device())
        gate = GEMV(
            self.w_gate,
            x,
            num_aie_columns=cols,
            tile_size_input=4,
            tile_size_output=hidden_dim // cols,
        )
        up = GEMV(
            self.w_up,
            x,
            num_aie_columns=cols,
            tile_size_input=4,
            tile_size_output=hidden_dim // cols,
        )
        swished = SiLU(gate, num_aie_columns=cols, tile_size=hidden_dim // (cols * 2))
        act = ElementwiseMul(
            swished, up, num_aie_columns=cols, tile_size=hidden_dim // cols
        )
        return GEMV(
            self.w_down,
            act,
            num_aie_columns=cols,
            tile_size_input=1,
            tile_size_output=embedding_dim // cols,
        )
