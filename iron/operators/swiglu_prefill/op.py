# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils

from iron.common.sequence import OperatorSequence
from iron.common.utils import get_shim_dma_limit
from iron.operators.gemm.op import GEMM
from iron.operators.silu.op import SiLU
from iron.operators.elementwise_mul.op import ElementwiseMul
from iron.operators.swiglu_prefill_front_fused.op import SwigluFrontFused
from iron.operators.swiglu_prefill_front_fused.reference import pack_weights


class SwiGLUPrefill(OperatorSequence):
    """SwiGLU feed-forward (full-sequence prefill) as an OperatorSequence.

    Computes ``W_down @ (SiLU(W_gate @ x) * (W_up @ x))`` over ``seq_len``
    tokens. Runtime buffers (via ``get_callable().get_buffer(name)``): input
    ``in``; persistent weights ``w_down`` and either ``w_gate`` / ``w_up`` or
    packed ``w_gate_up`` when ``use_fused_front=True``; output ``out``.
    """

    def __init__(
        self,
        seq_len,
        embedding_dim,
        hidden_dim,
        prio_accuracy=False,
        use_fused_front=False,
        context=None,
    ):
        self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.prio_accuracy = prio_accuracy
        self.use_fused_front = use_fused_front
        self.front = None

        accuracy_flags = {}
        if self.prio_accuracy:
            accuracy_flags = {
                "emulate_bf16_mmul_with_bfp16": False,
                "prio_accuracy": True,
                "round_conv_even": True,
            }

        dev = aie_utils.get_current_device()
        n_cols = get_shim_dma_limit(dev) // 2

        if self.use_fused_front:
            self.front = SwigluFrontFused(
                M=self.seq_len,
                K=self.embedding_dim,
                N=self.hidden_dim,
                num_aie_columns=n_cols,
                **accuracy_flags,
            )
            runlist = [
                (self.front, "in", "w_gate_up", "intermediate"),
            ]
        else:
            # TODO use other swiglu_prefill operator?
            gemm_1 = GEMM(
                M=self.seq_len,
                K=self.embedding_dim,
                N=self.hidden_dim,
                num_aie_columns=n_cols,
                **accuracy_flags,
            )
            silu = SiLU(
                size=self.seq_len * self.hidden_dim,
                num_aie_columns=n_cols,
                tile_size=self.hidden_dim // n_cols,
            )
            eltwise_mul = ElementwiseMul(
                size=self.seq_len * self.hidden_dim,
                num_aie_columns=n_cols,
                tile_size=self.hidden_dim // n_cols,
            )

            # gemm_1 is reused for both the gate and up projections.
            # GEMM arg order is (input, weight, output).
            runlist = [
                (gemm_1, "in", "w_gate", "left"),
                (gemm_1, "in", "w_up", "right"),
                (silu, "left", "left_swished"),
                (eltwise_mul, "left_swished", "right", "intermediate"),
            ]

        gemm_2 = GEMM(
            M=self.seq_len,
            K=self.hidden_dim,
            N=self.embedding_dim,
            num_aie_columns=n_cols,
            **accuracy_flags,
        )
        runlist.append((gemm_2, "intermediate", "w_down", "out"))

        super().__init__(
            name=(
                f"swiglu_prefill_s{seq_len}_e{embedding_dim}_h{hidden_dim}"
                f"_front_{'fused' if self.use_fused_front else 'sequential'}"
            ),
            runlist=runlist,
            input_args=["in"],
            output_args=["out"],
            context=context,
        )

    def pack_gate_up_weights(self, w_gate, w_up):
        """Pack gate/up weights for the fused-front persistent input buffer."""
        if self.front is None:
            raise RuntimeError(
                "Gate/up weights are separate when use_fused_front=False"
            )
        return pack_weights(
            w_gate,
            w_up,
            self.front.tile_k,
            self.front.tile_n,
            self.front.num_aie_columns,
        )
