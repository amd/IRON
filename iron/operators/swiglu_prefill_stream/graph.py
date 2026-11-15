# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import iron

from .op import (
    DOWN,
    FUSED_PARTITION,
    GATE,
    PARTITIONS,
    POST_OP_PARTITION,
    UP,
    SwiGLUFusedStream,
    SwiGLUGatedStream,
    SwiGLUMulStream,
    SwiGLUProjectionStream,
    SwiGLUSiLUStream,
    solution,
)


class SwiGLUPrefillStream(iron.Graph):
    """``(SiLU(x @ w_gate.T) * (x @ w_up.T)) @ w_down.T``, as stream-dse partitions it.

    Over ``(out, in)`` weights, as ``nn.Linear`` holds them. stream-dse
    chooses the partition and the GEMM block (``partition`` and
    ``gemm_block`` narrow the choice, as the operators'), and each
    fused group of the partition it chooses is one step. Recording the body
    therefore runs the solve, or reads it from the cache.
    """

    def __init__(self, w_gate, w_up, w_down, *, partition=None, gemm_block=None):
        self.w_gate, self.w_up, self.w_down = map(iron.param, (w_gate, w_up, w_down))
        self.partition, self.gemm_block = partition, gemm_block

    def body(self, x):
        shape = dict(
            embedding_dim=x.shape[1],
            hidden_dim=self.w_gate.shape[0],
            partition=self.partition,
            gemm_block=self.gemm_block,
        )
        design = solution(seq_len=x.shape[0], **shape)
        if design.groups == PARTITIONS[FUSED_PARTITION]:
            return SwiGLUFusedStream.step(
                x, self.w_gate, self.w_up, self.w_down, **shape
            )
        if design.groups == PARTITIONS[POST_OP_PARTITION]:
            hidden = SwiGLUGatedStream.step(x, self.w_gate, self.w_up, **shape)
            return SwiGLUProjectionStream.step(hidden, self.w_down, layer=DOWN, **shape)
        gate = SwiGLUProjectionStream.step(x, self.w_gate, layer=GATE, **shape)
        up = SwiGLUProjectionStream.step(x, self.w_up, layer=UP, **shape)
        hidden = SwiGLUMulStream.step(SwiGLUSiLUStream.step(gate, **shape), up, **shape)
        return SwiGLUProjectionStream.step(hidden, self.w_down, layer=DOWN, **shape)
