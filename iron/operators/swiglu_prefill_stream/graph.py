# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import iron

from .op import (
    DOWN,
    GATE,
    PARTITIONS,
    POST_OP_PARTITIONS,
    UP,
    SwiGLUFusedStream,
    SwiGLUGatedStream,
    SwiGLUMulStream,
    SwiGLUProjectionStream,
    SwiGLUSiLUStream,
    _SwiGLUStream,
)


class SwiGLUPrefillStream(iron.Graph):
    """``(SiLU(x @ w_gate) * (x @ w_up)) @ w_down``, as stream-dse partitions it.

    Over the ``(in, out)`` weights it holds. stream-dse chooses the
    partition and the GEMM block (``k`` and ``gemm_block`` narrow the
    choice, as ``_SwiGLUStream``'s): one fused group is one step; split per
    layer, each group is a step and the full ELF dispatches them in turn.
    """

    def __init__(self, w_gate, w_up, w_down, *, k=None, gemm_block=None):
        self.w_gate, self.w_up, self.w_down = map(iron.param, (w_gate, w_up, w_down))
        self.k, self.gemm_block = k, gemm_block

    def body(self, x):
        shape = dict(
            embedding_dim=x.shape[1],
            hidden_dim=self.w_gate.shape[1],
            k=self.k,
            gemm_block=self.gemm_block,
        )
        explorer = _SwiGLUStream(seq_len=x.shape[0], **shape).resolved()
        if explorer.solution().groups == PARTITIONS[1]:
            return SwiGLUFusedStream.step(
                x, self.w_gate, self.w_up, self.w_down, **shape
            )
        if explorer.solution().groups in POST_OP_PARTITIONS.values():
            hidden = SwiGLUGatedStream.step(x, self.w_gate, self.w_up, **shape)
            return SwiGLUProjectionStream.step(hidden, self.w_down, layer=DOWN, **shape)
        gate = SwiGLUProjectionStream.step(x, self.w_gate, layer=GATE, **shape)
        up = SwiGLUProjectionStream.step(x, self.w_up, layer=UP, **shape)
        hidden = SwiGLUMulStream.step(SwiGLUSiLUStream.step(gate, **shape), up, **shape)
        return SwiGLUProjectionStream.step(hidden, self.w_down, layer=DOWN, **shape)
