# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama as one graph function over one set of weights and caches.

:class:`LlamaGraph` holds ``forward(x=None, *, token, position)``. Given
``x``, the embedded tokens of a prompt, ``(rows, emb_dim)``, it is a prompt:
GEMM projections, causal MHA over the rows, the caches written in full from
row zero, and the final norm and output head for row ``position`` alone.
Without ``x`` it is a decode step on ``token`` at ``position``: the token's
embedding row and the position's RoPE row gathered on the device, GEMV
projections, attention against the KV caches, the row written into them at
the position, the softmax masked to the ``position + 1`` keys so far. Both
end in the same norm and head, and draw the next token from its logits on
the device (:class:`~iron.operators.Sample`). They return the logits and
carry the token and ``position + 1`` into the next call, so a decode step
can start another with nothing from the host
(:class:`~iron.common.graph.carried.CarriedLoop`).

Each shape compiles its own version of the one function, and every version
runs in the function's one scratch arena (:mod:`iron.common.graph.compiled`):
the weights and the caches -- the caches are :func:`iron.state`, the weights
closed over from ``config.weights`` -- sit at one offset in every image and
are uploaded once, so the caches a prompt writes are the ones the next
decode step reads, and there is nothing to hand over.

``config`` is the model's shape (``n_heads``, ``n_kv_groups``, ``head_dim``,
``emb_dim``, ``hidden_dim``) with the parameters as ``config.weights``
(:class:`.weights.LlamaWeights`); the depth is the number of layers it
holds. Each array is closed over as-is, so the tracer names and pins it by
identity. Traced here on handles; compiled by ``npu.py`` against a device,
or by a test against nothing.
"""

import math

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.kernels.sample import ROW_WORDS

import iron
from iron.common.declare import Carried
from iron.common.graph import Value, handle_of
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm.op import GEMM
from iron.operators.gemv.op import GEMV
from iron.operators.mha.op import MHA
from iron.operators.repeat import Repeat
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope.op import RoPE
from iron.operators.sample import Sample
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.operators.strided_copy import StridedCopy
from iron.operators.transpose import Transpose

from .weights import LlamaWeights


class _Parameters:
    """The names the tracer gives the arrays ``forward`` closes over: the
    checkpoint's weights under theirs, and the tables derived from the
    config under the given ones."""

    def __init__(self, weights: LlamaWeights, **tables: np.ndarray):
        self.weights = weights
        self.tables = tables

    def named_parameters(self):
        yield from self.weights.named_parameters()
        yield from self.tables.items()


class LlamaGraph:
    """The graph function and the state it closes over.

    ``keys[i]`` and ``values[i]`` are the layer caches, each ``(n_kv_groups,
    max_seq_len * head_dim)``: the flat per-group layout both phases write
    and decode's repeat reads. ``scale`` is the attention scale as a tensor,
    since the elementwise multiply takes one.

    A prompt of ``rows`` rows needs ``rows`` a multiple of 64 times
    ``num_of_pipelines`` (MHA's) and of four times ``tile_m`` (the GEMMs'
    row tile), and at most ``max_seq_len``.
    """

    def __init__(
        self,
        config,
        max_seq_len,
        *,
        num_aie_columns=None,
        num_of_pipelines=8,
        tile_m=64,
    ):
        W = config.weights
        H, G, D = config.n_heads, config.n_kv_groups, config.head_dim
        E, F = config.emb_dim, config.hidden_dim
        if num_aie_columns is None:
            # The device's width: eight on NPU2, four on NPU1. The tile sizes
            # below divide by it, so it is fixed when the graph is written.
            dev = aie_utils.get_current_device()
            num_aie_columns = dev.cols if dev is not None else 8
        L, cols = max_seq_len, num_aie_columns
        self.max_seq_len = L
        # The largest top-k the device draws with.
        self.k_max = 64
        self.num_aie_columns = cols
        self.keys = [
            iron.state((G, L * D), name=f"keys_cache_{i}") for i in range(len(W.layers))
        ]
        self.values = [
            iron.state((G, L * D), name=f"values_cache_{i}")
            for i in range(len(W.layers))
        ]
        # The draws, one four-word row per position (``Sampler.rows``), and
        # the tokens drawn, each recorded at its position: the host writes
        # the one before a prompt and reads the other after the loop.
        self.draws = iron.state((L, ROW_WORDS), np.int32, name="sample_draws")
        self.tokens = iron.state((L,), np.int32, name="sampled_tokens")
        # 1/sqrt(head_dim) over every score, as the elementwise multiply wants it.
        self.scale = np.full((H, L), 1.0 / math.sqrt(D), dtype=bfloat16)
        # The RoPE table, one row per position, in the images' dtype: a prompt
        # reads its first rows, a decode step gathers its position's.
        self.rope = config.angles[:L].astype(bfloat16)
        keys, values, scale, rope = self.keys, self.values, self.scale, self.rope
        draws, tokens = self.draws, self.tokens

        # -- one row: a decode step ------------------------------------------

        # Matrices are read as the checkpoint ships them, (out, in): GEMV's
        # (M, K). Tile choices are the ones decode ran with before.
        def gemv(weight, x, *, tile_in=4, tile_out):
            return GEMV(
                weight,
                x,
                num_aie_columns=cols,
                tile_size_input=tile_in,
                tile_size_output=tile_out,
            )

        row_into_cache = dict(
            input_sizes=(G, D),
            input_strides=(D, 1),
            input_offset=0,
            output_sizes=(1, G, D),
            output_strides=(0, L * D, 1),
            output_offset=0,  # base; the per-call addend is cache_offset
            num_aie_channels=1,
        )

        def gather_row(table, row: Value):
            """Row ``row`` of a ``(rows, n)`` table, copied out on the device.

            The row is a per-call value, so the copy's base address is patched
            by ``row * n`` elements. Every gather has one transfer size, so
            they are one design, and back to back they switch nothing.
            """
            n = table.shape[1]
            return StridedCopy(
                table,
                in_offset=row * n,
                input_sizes=(1, n),
                input_strides=(n, 1),
                input_offset=0,
                output_sizes=(1, n),
                output_strides=(n, 1),
                output_offset=0,
                output_buffer_size=n,
                transfer_size=D,
                num_aie_channels=1,
            ).reshape(1, n)

        def decode_block(i, lw, x, angles, cache_offset, vector_size):
            h = RMSNorm(x, lw.norm1)
            # <grouped query attention>
            q = gemv(lw.q, h, tile_out=D // 2)
            k = gemv(lw.k, h, tile_out=D // 2)
            v = gemv(lw.v, h, tile_out=D // 2)
            q = RoPE(q.reshape(H, D), angles)
            k = RoPE(k.reshape(G, D), angles)
            StridedCopy(k, keys[i], out_offset=cache_offset, **row_into_cache)
            StridedCopy(
                v.reshape(G, D), values[i], out_offset=cache_offset, **row_into_cache
            )
            # Every head sees its group's keys and values.
            k_all = Repeat(keys[i], repeat=H // G, transfer_size=D)
            v_all = Repeat(values[i], repeat=H // G, transfer_size=D)
            scores = gemv(k_all.reshape(H, L, D), q, tile_out=L // cols)
            scores = ElementwiseMul(
                scores, scale, num_aie_columns=cols, tile_size=L // cols
            )
            # The valid row length is the context length: the kernel masks
            # every column from there on, so the cache's unwritten tail
            # contributes nothing.
            weights = Softmax(scores, vector_size=vector_size)
            v_t = Transpose(
                v_all.reshape(H, L, D),
                num_aie_columns=2,
                num_channels=1,
                m=256,
                n=32,
                s=8,
            )
            ctx = gemv(v_t, weights, tile_out=4)
            o = gemv(lw.o, ctx.reshape(H * D), tile_out=E // cols)
            # </grouped query attention>
            x = ElementwiseAdd(x, o, num_aie_columns=cols, tile_size=E // cols)
            h = RMSNorm(x, lw.norm2)
            gate = gemv(lw.gate, h, tile_out=F // cols)
            up = gemv(lw.up, h, tile_out=F // cols)
            act = ElementwiseMul(
                SiLU(gate, num_aie_columns=cols, tile_size=F // cols),
                up,
                num_aie_columns=cols,
                tile_size=F // cols,
            )
            down = gemv(lw.down, act, tile_in=1, tile_out=E // cols)
            return ElementwiseAdd(x, down, num_aie_columns=cols, tile_size=E // cols)

        # -- many rows: a prompt ---------------------------------------------

        def gemm(x, weight):
            # Every projection is read as the checkpoint ships it, (out, in):
            # GEMM's column-major B, the layout the GEMVs read too.
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

        def rows_into_cache(n):
            # (n, G, D), the heads interleaved per token as the projection
            # wrote them, into the first n rows of the cache's (G, L, D).
            return dict(
                input_sizes=(G, n, D),
                input_strides=(D, G * D, 1),
                input_offset=0,
                output_sizes=(G, n, D),
                output_strides=(L * D, D, 1),
                output_offset=0,
                transfer_size=1024,
                num_aie_channels=1,
            )

        def prefill_block(i, lw, x, angles):
            n = x.shape[0]
            h = norm(x, lw.norm1)
            # <grouped query attention>
            q = gemm(h, lw.q)  # (n, H*D)
            k = gemm(h, lw.k)  # (n, G*D)
            v = gemm(h, lw.v)
            # One angle row per position, applied to that position's heads.
            q = RoPE(q.reshape(n * H, D), angles, num_aie_columns=cols)
            k = RoPE(k.reshape(n * G, D), angles, num_aie_columns=cols)
            StridedCopy(k, keys[i], **rows_into_cache(n))
            StridedCopy(v, values[i], **rows_into_cache(n))
            o = MHA(
                q.reshape(n, H, D),
                k.reshape(n, G, D),
                v.reshape(n, G, D),
                heads_interleaved=True,
                num_of_pipelines=num_of_pipelines,
            )
            o = gemm(o.reshape(n, H * D), lw.o)
            # </grouped query attention>
            x = ElementwiseAdd(x, o, num_aie_columns=cols, tile_size=E)
            h = norm(x, lw.norm2)
            gate = gemm(h, lw.gate)
            up = gemm(h, lw.up)
            act = ElementwiseMul(
                SiLU(gate, num_aie_columns=cols, tile_size=F),
                up,
                num_aie_columns=cols,
                tile_size=F,
            )
            down = gemm(act, lw.down)
            return ElementwiseAdd(x, down, num_aie_columns=cols, tile_size=E)

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

        @iron.graph(names_from=_Parameters(W, **{"rope.angles": rope}))
        def forward(
            x=None,
            *,
            token: Carried[np.int32],
            position: Carried[np.int32],
        ):
            if x is not None:
                angles = handle_of(rope)[: x.shape[0]]
                for i, lw in enumerate(W.layers):
                    x = prefill_block(i, lw, x, angles)
                # The last prompt row alone, at ``position``: its logits are
                # all the host reads.
                x = StridedCopy(x, in_offset=position * E, **last_row).reshape(1, E)
            else:
                # Both gathers first, so they run back to back as one design.
                x = gather_row(W.embedding, token)
                angles = gather_row(rope, position)
                for i, lw in enumerate(W.layers):
                    # The row lands in the caches at its position, and the
                    # softmax sees every key up to and including it.
                    x = decode_block(i, lw, x, angles, position * D, position + 1)
            x = RMSNorm(x, W.norm)
            logits = gemv(W.out_head, x, tile_out=32)
            _, sampled = Sample(
                logits.reshape(config.vocab_size),
                draws,
                tokens,
                row=position * ROW_WORDS,
                at=position,
                k_max=self.k_max,
            )
            return logits, iron.carry(token=sampled, position=position + 1)

        self.graph = forward

    def shapes(self, config, rows):
        """The input shapes of the version that runs ``rows`` tokens: none
        for a decode step, which gathers its row on the device."""
        return dict(x=(rows, config.emb_dim)) if rows > 1 else {}

    def trace(self, config, rows):
        return self.graph.trace(**self.shapes(config, rows))

    def compile(self, config, rows, **kwargs):
        return self.graph.compile(**self.shapes(config, rows), **kwargs)
