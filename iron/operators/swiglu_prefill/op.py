# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils

from iron.common import (
    CompositeOperator,
    AIERuntimeArgSpec,
)
from iron.common.utils import get_shim_dma_limit
from iron.operators.swiglu_base import _SwiGLUCallable, chain_swiglu_artifacts
from iron.operators.gemm.op import GEMM
from iron.operators.silu.op import SiLU
from iron.operators.elementwise_mul.op import ElementwiseMul


class SwiGLUPrefillCallable(_SwiGLUCallable):
    def __init__(self, op):
        super().__init__(
            op,
            matmul_1_prefix="gemm_1",
            matmul_2_prefix="gemm_2",
            transpose_weights=True,
            intermediate_shape=(op.seq_len_padded * op.hidden_dim_padded,),
        )

    def _call_matmul(self, matmul_callable, weight, input_buf, output_buf):
        # GEMM arg order: input, weight, output
        matmul_callable(input_buf, weight, output_buf)


class SwiGLUPrefill(CompositeOperator):
    def __init__(
        self, seq_len, embedding_dim, hidden_dim, prio_accuracy=False, context=None
    ):
        self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        # weights to be set by user (e.g., assign_weights in FeedForward block)
        self.weights_1 = None
        self.weights_2 = None
        self.weights_3 = None

        self.prio_accuracy = prio_accuracy
        super().__init__(context=context)

    def set_up_artifacts(self):
        # All operators (GEMM, SiLU, ElementwiseMul) apply their own padding
        # to meet hardware alignment requirements. We store the padded dimensions
        # from GEMM and verify that all operators use consistent padded sizes.
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
        self.gemm_1 = gemm_1
        self.seq_len_padded = gemm_1.M
        self.embedding_dim_padded = gemm_1.K
        self.hidden_dim_padded = gemm_1.N

        silu = SiLU(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim_padded // n_cols,
        )
        self.silu = silu
        assert silu.size == self.seq_len_padded * self.hidden_dim_padded

        eltwise_mul = ElementwiseMul(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim_padded // n_cols,
        )
        self.eltwise_mul = eltwise_mul
        assert eltwise_mul.size == self.seq_len_padded * self.hidden_dim_padded

        gemm_2 = GEMM(
            M=self.seq_len,
            K=self.hidden_dim,
            N=self.embedding_dim,
            num_aie_columns=n_cols,
            **accuracy_flags,
        )
        self.gemm_2 = gemm_2
        assert gemm_2.M == self.seq_len_padded
        assert gemm_2.K == self.hidden_dim_padded
        assert gemm_2.N == self.embedding_dim_padded

        chain_swiglu_artifacts(
            self,
            [
                ("gemm_1", "0x901", gemm_1),
                ("silu", "0x902", silu),
                ("eltwise_mul", "0x903", eltwise_mul),
                ("gemm_2", "0x904", gemm_2),
            ],
        )

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.seq_len_padded * self.embedding_dim_padded,)),
            AIERuntimeArgSpec(
                "out", (self.seq_len_padded * self.embedding_dim_padded,)
            ),
        ]

    def get_callable(self):
        return SwiGLUPrefillCallable(self)
