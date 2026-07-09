# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils

from iron.common.sequence import OperatorSequence
from iron.common.utils import get_shim_dma_limit
from iron.operators.gemm.op import GEMM
from iron.operators.silu.op import SiLU
from iron.operators.elementwise_mul.op import ElementwiseMul


class SwiGLUPrefill(OperatorSequence):
    """SwiGLU feed-forward (full-sequence prefill) as an OperatorSequence.

    Computes ``W_down @ (SiLU(W_gate @ x) * (W_up @ x))`` over ``seq_len``
    tokens. Runtime buffers (via ``get_callable().get_buffer(name)``): input
    ``in``; persistent weight scratch ``w_gate`` / ``w_up`` / ``w_down``;
    output ``out``.
    """

    def __init__(
        self, seq_len, embedding_dim, hidden_dim, prio_accuracy=False, context=None
    ):
        self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.prio_accuracy = prio_accuracy

        # All operators (GEMM, SiLU, ElementwiseMul) apply their own padding
        # to meet hardware alignment requirements. We store the padded dimensions
        # from GEMM and size SiLU/ElementwiseMul to match.
        accuracy_flags = {}
        if self.prio_accuracy:
            accuracy_flags = {
                "emulate_bf16_mmul_with_bfp16": False,
                "prio_accuracy": True,
                "round_conv_even": True,
            }

        dev = aie_utils.get_current_device()
        n_cols = get_shim_dma_limit(dev) // 2

        gemm_1 = GEMM(
            M=self.seq_len,
            K=self.embedding_dim,
            N=self.hidden_dim,
            num_aie_columns=n_cols,
            **accuracy_flags,
        )
        self.seq_len_padded = gemm_1.M
        self.embedding_dim_padded = gemm_1.K
        self.hidden_dim_padded = gemm_1.N

        silu = SiLU(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim_padded // n_cols,
        )
        eltwise_mul = ElementwiseMul(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim_padded // n_cols,
        )
        gemm_2 = GEMM(
            M=self.seq_len,
            K=self.hidden_dim,
            N=self.embedding_dim,
            num_aie_columns=n_cols,
            **accuracy_flags,
        )

        # gemm_1 is reused for both the gate and up projections.
        # GEMM arg order is (input, weight, output).
        runlist = [
            (gemm_1, "in", "w_gate", "left"),
            (gemm_1, "in", "w_up", "right"),
            (silu, "left", "left_swished"),
            (eltwise_mul, "left_swished", "right", "intermediate"),
            (gemm_2, "intermediate", "w_down", "out"),
        ]

        super().__init__(
            name=f"swiglu_prefill_s{seq_len}_e{embedding_dim}_h{hidden_dim}",
            runlist=runlist,
            input_args=["in"],
            output_args=["out"],
            context=context,
        )
