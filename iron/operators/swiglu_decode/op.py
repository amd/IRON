# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils

from iron.common.sequence import OperatorSequence
from iron.common.utils import get_shim_dma_limit
from iron.operators.gemv.op import GEMV
from iron.operators.silu.op import SiLU
from iron.operators.elementwise_mul.op import ElementwiseMul


class SwiGLUDecode(OperatorSequence):
    """SwiGLU feed-forward (single-token decode) as an OperatorSequence.

    Computes ``W_down @ (SiLU(W_gate @ x) * (W_up @ x))``. Runtime buffers
    (via ``get_callable().get_buffer(name)``): input ``in``; persistent weight
    scratch ``w_gate`` / ``w_up`` / ``w_down``; output ``out``.
    """

    def __init__(self, embedding_dim, hidden_dim, prio_accuracy=False, context=None):
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.prio_accuracy = prio_accuracy

        dev = aie_utils.get_current_device()
        n_cols = get_shim_dma_limit(dev) // 2

        gemv_1 = GEMV(
            M=self.hidden_dim,
            K=self.embedding_dim,
            num_aie_columns=n_cols,
            tile_size_input=4,
            tile_size_output=self.hidden_dim // n_cols,
        )
        silu = SiLU(
            size=self.hidden_dim,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim // (n_cols * 2),
        )
        eltwise_mul = ElementwiseMul(
            size=self.hidden_dim,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim // n_cols,
        )
        gemv_2 = GEMV(
            M=self.embedding_dim,
            K=self.hidden_dim,
            num_aie_columns=n_cols,
            tile_size_input=1,
            tile_size_output=self.embedding_dim // n_cols,
        )

        # gemv_1 is reused for both the gate and up projections.
        # GEMV arg order is (matrix, vector, output).
        runlist = [
            (gemv_1, "w_gate", "in", "left"),
            (gemv_1, "w_up", "in", "right"),
            (silu, "left", "left_swished"),
            (eltwise_mul, "left_swished", "right", "intermediate"),
            (gemv_2, "w_down", "intermediate", "out"),
        ]

        super().__init__(
            name=f"swiglu_decode_e{embedding_dim}_h{hidden_dim}",
            runlist=runlist,
            input_args=["in"],
            output_args=["out"],
            context=context,
        )
