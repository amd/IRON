# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama's two phases as graph functions over one set of weights and caches.

:class:`DecodeGraph` runs one token through every transformer block, the
final norm and the output head, with the KV caches as device-resident
state and the weights closed over from the module tree; the cache position
and the softmax's valid row length are per-call scratchpad values.
:class:`PrefillGraph` runs the prompt, at the compile-time maximum length
with the prompt in a prefix, writes the caches and returns the last
prompt token's logits. Both are traced here on handles; compiled by
``iron/applications/llama_3.2_1b/llama_npu.py`` against a device, or by a
test against nothing. ``config`` is the model's shape (``n_layers``,
``n_heads``, ``n_kv_groups``, ``head_dim``, ``emb_dim``, ``hidden_dim``)
with the parameter tree as ``config.model`` (:class:`iron.models.llama.Llama`).
"""

import math

import numpy as np
import torch

import iron
from iron.common.declare import Scratchpad
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm.op import GEMM
from iron.operators.gemv.op import GEMV
from iron.operators.mha.op import MHA
from iron.operators.repeat import Repeat
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope.op import RoPE
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.operators.strided_copy import StridedCopy
from iron.operators.transpose import Transpose


class DecodeGraph:
    """The decode graph function and the state it closes over.

    ``keys[i]`` and ``values[i]`` are the layer caches, each ``(n_kv_groups,
    max_seq_len * head_dim)``: the flat per-group layout the strided copy
    writes and the repeat reads. ``scale`` is the attention scale as a
    tensor, since the elementwise multiply takes one.
    """

    def __init__(self, config, max_seq_len, *, num_aie_columns=None):
        model = config.model
        H, G, D = config.n_heads, config.n_kv_groups, config.head_dim
        E, F = config.emb_dim, config.hidden_dim
        if num_aie_columns is None:
            # The device's width: eight on NPU2, four on NPU1. The tile sizes
            # below divide by it, so it is fixed when the graph is written.
            import aie.utils as aie_utils

            dev = aie_utils.get_current_device()
            num_aie_columns = dev.cols if dev is not None else 8
        L, cols = max_seq_len, num_aie_columns
        self.max_seq_len = L
        self.num_aie_columns = cols
        self.keys = [
            iron.state((G, L * D), name=f"keys_cache_{i}")
            for i in range(config.n_layers)
        ]
        self.values = [
            iron.state((G, L * D), name=f"values_cache_{i}")
            for i in range(config.n_layers)
        ]
        # 1/sqrt(head_dim) over every score, as the elementwise multiply wants it.
        self.scale = torch.full((H, L), 1.0 / math.sqrt(D), dtype=torch.bfloat16)
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


class PrefillGraph:
    """The prefill graph function, over a decode graph's weights and caches.

    The length is the decode graph's maximum: the prompt occupies the first
    rows of ``x`` and ``angles``, and the rows past it compute on whatever
    is there and are never read (MHA is causal; decode masks the cache's
    tail by its ``vector_size``). One per-call value, ``last``, is the
    element offset of the last prompt row, ``(n - 1) * emb_dim``: the final
    norm and the output head run for that row alone, which is all the
    harness reads. The caches are written in full, in the layout decode
    reads them.

    ``num_of_pipelines`` is MHA's; the sequence must be a multiple of 64
    times it. ``tile_m`` is the GEMMs' row tile; the length must be a
    multiple of four times it.
    """

    def __init__(self, config, decode, *, num_of_pipelines=8, tile_m=64):
        model = config.model
        H, G, D = config.n_heads, config.n_kv_groups, config.head_dim
        E, F = config.emb_dim, config.hidden_dim
        L, cols = decode.max_seq_len, decode.num_aie_columns
        keys, values = decode.keys, decode.values
        self.max_seq_len = L

        def proj(x, weight):
            # Every projection is read as the checkpoint ships it, (out, in):
            # GEMM's column-major B, the layout decode's GEMV reads too.
            return GEMM(
                x,
                weight,
                b_col_maj=True,
                num_aie_columns=cols,
                tile_m=tile_m,
                tile_k=64,
                tile_n=64,
            )

        def norm(x, weight):
            return RMSNorm(x, weight, num_aie_columns=cols, num_channels=1)

        # (L, G, D), the heads interleaved per token as the projection wrote
        # them, into the cache's (G, L, D).
        into_cache = dict(
            input_sizes=(G, L, D),
            input_strides=(D, G * D, 1),
            input_offset=0,
            output_sizes=(G, L, D),
            output_strides=(L * D, D, 1),
            output_offset=0,
            transfer_size=1024,
            num_aie_channels=1,
        )
        last_row = dict(
            input_sizes=(1, E),
            input_strides=(E, 1),
            input_offset=0,  # base; the per-call addend is `last`
            output_sizes=(1, E),
            output_strides=(E, 1),
            output_offset=0,
            output_buffer_size=E,
            num_aie_channels=1,
        )

        @iron.graph(names_from=model)
        def prefill(x, angles, *, last: Scratchpad[np.int32]):
            for i, blk in enumerate(model.layers):
                # <transformer block>
                h = norm(x, blk.norm1.weight)
                # <grouped query attention>
                q = proj(h, blk.attn.q.weight)  # (L, H*D)
                k = proj(h, blk.attn.k.weight)  # (L, G*D)
                v = proj(h, blk.attn.v.weight)
                # One angle row per position, applied to that position's heads.
                q = RoPE(q.reshape(L * H, D), angles, num_aie_columns=cols)
                k = RoPE(k.reshape(L * G, D), angles, num_aie_columns=cols)
                StridedCopy(k, keys[i], **into_cache)
                StridedCopy(v, values[i], **into_cache)
                o = MHA(
                    q.reshape(L, H, D),
                    k.reshape(L, G, D),
                    v.reshape(L, G, D),
                    heads_interleaved=True,
                    num_of_pipelines=num_of_pipelines,
                )
                o = proj(o.reshape(L, H * D), blk.attn.o.weight)
                # </grouped query attention>
                x = ElementwiseAdd(x, o, num_aie_columns=cols, tile_size=E)
                h = norm(x, blk.norm2.weight)
                gate = proj(h, blk.ffn.gate.weight)
                up = proj(h, blk.ffn.up.weight)
                act = ElementwiseMul(
                    SiLU(gate, num_aie_columns=cols, tile_size=F),
                    up,
                    num_aie_columns=cols,
                    tile_size=F,
                )
                down = proj(act, blk.ffn.down.weight)
                x = ElementwiseAdd(x, down, num_aie_columns=cols, tile_size=E)
                # </transformer block>
            x_last = StridedCopy(x, in_offset=last, **last_row).reshape(1, E)
            h = RMSNorm(x_last, model.norm.weight)
            return GEMV(
                model.out_head.weight,
                h,
                num_aie_columns=cols,
                tile_size_input=4,
                tile_size_output=32,
            )

        self.graph = prefill

    def shapes(self, config):
        return dict(
            x=(self.max_seq_len, config.emb_dim),
            angles=(self.max_seq_len, config.head_dim),
        )

    def trace(self, config):
        return self.graph.trace(**self.shapes(config))

    def compile(self, config, **kwargs):
        return self.graph.compile(**self.shapes(config), **kwargs)
