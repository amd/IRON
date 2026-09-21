# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama decode as a graph function.

One token through every transformer block, the final norm and the output
head, with the KV caches as device-resident state and the weights closed
over from the module tree. The cache position and the softmax's valid row
length are per-call scratchpad values. Traced here on handles; compiled
by ``llama_npu.py`` against a device, or by a test against nothing.
"""

import math

import numpy as np

import iron
from iron.common.declare import Scratchpad
from iron.operators.elementwise_add.op import ElementwiseAdd
from iron.operators.elementwise_mul.op import ElementwiseMul
from iron.operators.gemv.op import GEMV
from iron.operators.repeat.op import Repeat
from iron.operators.rms_norm.op import RMSNorm
from iron.operators.rope.op import RoPE
from iron.operators.silu.op import SiLU
from iron.operators.softmax.op import Softmax
from iron.operators.strided_copy.op import StridedCopy
from iron.operators.transpose.op import Transpose


class DecodeGraph:
    """The decode graph function and the state it closes over.

    ``keys[i]`` and ``values[i]`` are the layer caches, each ``(n_kv_groups,
    max_seq_len * head_dim)``: the flat per-group layout the strided copy
    writes and the repeat reads. ``scale`` is the attention scale as a
    tensor, since the elementwise multiply takes one.
    """

    def __init__(self, config, max_seq_len, *, num_aie_columns=None, tensor=None):
        model = config.model
        H, G, D = config.n_heads, config.n_kv_groups, config.head_dim
        E, F = config.emb_dim, config.hidden_dim
        if num_aie_columns is None:
            # The device's width: eight on NPU2, four on NPU1. The tile sizes
            # below divide by it, so it is fixed when the graph is written.
            import aie.utils as aie_utils

            from iron.common.utils import device_columns

            dev = aie_utils.get_current_device()
            num_aie_columns = device_columns(dev) if dev is not None else 8
        L, cols = max_seq_len, num_aie_columns
        self.max_seq_len = L
        self.keys = [
            iron.state((G, L * D), name=f"keys_cache_{i}")
            for i in range(config.n_layers)
        ]
        self.values = [
            iron.state((G, L * D), name=f"values_cache_{i}")
            for i in range(config.n_layers)
        ]
        # 1/sqrt(head_dim) over every score, as the elementwise multiply wants it.
        make = tensor or _numpy_bf16
        self.scale = make(np.full((H, L), 1.0 / math.sqrt(D), dtype=np.float32))
        keys, values, scale = self.keys, self.values, self.scale

        # Matrices are read as the checkpoint ships them, (out, in): GEMV's
        # (M, K). Tile choices are the ones decode ran with before.
        def proj(weight, x, *, tile_in=4, tile_out):
            return GEMV(
                weight,
                x,
                num_aie_columns=cols,
                tile_size_input=tile_in,
                tile_size_output=tile_out,
            )

        copy_into_cache = dict(
            input_sizes=(G, D),
            input_strides=(D, 1),
            input_offset=0,
            output_sizes=(1, G, D),
            output_strides=(0, L * D, 1),
            output_offset=0,  # base; the per-call addend is cache_offset
            num_aie_channels=1,
        )

        @iron.graph(names_from=model)
        def decode(
            x,
            angles,
            *,
            cache_offset: Scratchpad[np.int32],
            vector_size: Scratchpad[np.int32],
        ):
            for i, blk in enumerate(model.layers):
                # <transformer block>
                h = RMSNorm(x, blk.norm1.weight)
                # <grouped query attention>
                q = proj(blk.attn.q.weight, h, tile_out=D // 2)
                k = proj(blk.attn.k.weight, h, tile_out=D // 2)
                v = proj(blk.attn.v.weight, h, tile_out=D // 2)
                q = RoPE(q.reshape(H, D), angles)
                k = RoPE(k.reshape(G, D), angles)
                StridedCopy(k, keys[i], out_offset=cache_offset, **copy_into_cache)
                StridedCopy(
                    v.reshape(G, D),
                    values[i],
                    out_offset=cache_offset,
                    **copy_into_cache,
                )
                # Every head sees its group's keys and values.
                k_all = Repeat(keys[i], repeat=H // G, transfer_size=D)
                v_all = Repeat(values[i], repeat=H // G, transfer_size=D)
                scores = proj(k_all.reshape(H, L, D), q, tile_out=L // cols)
                scores = ElementwiseMul(
                    scores, scale, num_aie_columns=cols, tile_size=L // cols
                )
                weights = Softmax(scores, vector_size=vector_size)
                v_t = Transpose(
                    v_all.reshape(H, L, D),
                    num_aie_columns=2,
                    num_channels=1,
                    m=256,
                    n=32,
                    s=8,
                )
                ctx = proj(v_t, weights, tile_out=4)
                o = proj(blk.attn.o.weight, ctx.reshape(H * D), tile_out=E // cols)
                # </grouped query attention>
                x = ElementwiseAdd(x, o, num_aie_columns=cols, tile_size=E // cols)
                h = RMSNorm(x, blk.norm2.weight)
                gate = proj(blk.ffn.gate.weight, h, tile_out=F // cols)
                up = proj(blk.ffn.up.weight, h, tile_out=F // cols)
                act = ElementwiseMul(
                    SiLU(gate, num_aie_columns=cols, tile_size=F // cols),
                    up,
                    num_aie_columns=cols,
                    tile_size=F // cols,
                )
                down = proj(blk.ffn.down.weight, act, tile_in=1, tile_out=E // cols)
                x = ElementwiseAdd(x, down, num_aie_columns=cols, tile_size=E // cols)
                # </transformer block>
            x = RMSNorm(x, model.norm.weight)
            return proj(model.out_head.weight, x, tile_out=32)

        self.graph = decode

    def trace(self, config):
        return self.graph.trace(x=(1, config.emb_dim), angles=(1, config.head_dim))

    def compile(self, config, **kwargs):
        return self.graph.compile(
            x=(1, config.emb_dim), angles=(1, config.head_dim), **kwargs
        )


def _numpy_bf16(array):
    from ml_dtypes import bfloat16

    return np.asarray(array, dtype=bfloat16)
