# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils

from iron.common import (
    CompositeOperator,
    AIERuntimeArgSpec,
)
from iron.common.utils import get_shim_dma_limit
from iron.operators.swiglu_base import _SwiGLUCallable, chain_swiglu_artifacts
from iron.operators.gemv.op import GEMV
from iron.operators.silu.op import SiLU
from iron.operators.elementwise_mul.op import ElementwiseMul


class SwiGLUDecodeCallable(_SwiGLUCallable):
    def __init__(self, op):
        super().__init__(
            op,
            matmul_1_prefix="gemv_1",
            matmul_2_prefix="gemv_2",
            transpose_weights=False,
            intermediate_shape=(op.hidden_dim_padded,),
        )

    def _call_matmul(self, matmul_callable, weight, input_buf, output_buf):
        # GEMV arg order: weight, input, output
        matmul_callable(weight, input_buf, output_buf)


class SwiGLUDecode(CompositeOperator):
    def __init__(self, embedding_dim, hidden_dim, prio_accuracy=False, context=None):
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.prio_accuracy = prio_accuracy
        # weights to be set by user (e.g., assign_weights in FeedForward block)
        self.weights_1 = None
        self.weights_2 = None
        self.weights_3 = None

        super().__init__(context=context)

    def set_up_artifacts(self):
        dev = aie_utils.get_current_device()
        n_cols = get_shim_dma_limit(dev) // 2

        gemv_1 = GEMV(
            M=self.hidden_dim,
            K=self.embedding_dim,
            num_aie_columns=n_cols,
            tile_size_input=4,
            tile_size_output=self.hidden_dim // n_cols,
        )
        self.gemv_1 = gemv_1

        silu = SiLU(
            size=self.hidden_dim,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim // (n_cols * 2),
        )
        self.silu = silu
        self.hidden_dim_padded = silu.size

        eltwise_mul = ElementwiseMul(
            size=self.hidden_dim,
            num_aie_columns=n_cols,
            tile_size=self.hidden_dim // n_cols,
        )
        self.eltwise_mul = eltwise_mul
        assert self.hidden_dim <= eltwise_mul.size <= self.hidden_dim_padded

        gemv_2 = GEMV(
            M=self.embedding_dim,
            K=self.hidden_dim,
            num_aie_columns=n_cols,
            tile_size_input=1,
            tile_size_output=self.embedding_dim // n_cols,
        )
        self.gemv_2 = gemv_2

        chain_swiglu_artifacts(
            self,
            [
                ("gemv_1", "0x901", gemv_1),
                ("silu", "0x902", silu),
                ("eltwise_mul", "0x903", eltwise_mul),
                ("gemv_2", "0x904", gemv_2),
            ],
        )

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.embedding_dim,)),
            AIERuntimeArgSpec("out", (self.embedding_dim,)),
        ]

    def get_callable(self):
        return SwiGLUDecodeCallable(self)
