# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Layer-by-layer attention prefill, captured as one full-ELF dispatch.

GEMM, scale, causal mask, softmax and context GEMM remain separate stages.
Unlike ``MHA``'s dataflow pipeline, their intermediate scores use NPU
buffers in host memory, with no host synchronization between stages. Query
blocks bound that scratch space to O(num_heads * block_rows * seq_len).
Each stage processes all heads before the array is reconfigured.

Both graphs use the usual ``record``, ``reference`` and ``compile`` API.
``compile(full_elf=True, queries=(H, S, d), keys=(G, S, d),
values=(G, S, d))`` makes one dispatch; ``full_elf=False`` dispatches each
stage separately. Keys and values are shared by each group of query heads.
"""

import math
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron.common import Precision
from iron.common.graph import Graph, param, state
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import RowwiseMul
from iron.operators.gemm import GEMM
from iron.operators.rope import RoPE
from iron.operators.softmax import Softmax

_PROFILES = Path(__file__).parent / "profiles" / "mha_prefill_lxl"


def _gemm(a, b, *out, b_col_maj=False, accumulate_f32=False):
    # Match the original BFP multiplies, with f32 partial sums only for
    # context and output products. Geometry comes from the graph's profile.
    return GEMM.step(
        a,
        b,
        *out,
        b_col_maj=b_col_maj,
        precision=Precision.MEDIUM,
        accumulate_f32=accumulate_f32,
    )


class AttentionPrefillFused(Graph):
    """Prefill over Q ``(H, S, d)`` and K/V ``(G, S, d)``; output ``(H, S, d)``.

    ``num_heads / num_kv_groups`` adjacent query heads share one KV head.
    Inputs are already projected and rotated. ``embedding_dim`` describes
    the surrounding projections and is used by the projected variant.
    """

    profile = _PROFILES

    def __init__(
        self,
        num_heads: int,
        num_kv_groups: int,
        head_dim: int,
        embedding_dim: int,
        seq_len: int,
        causal_mask: bool = True,
    ):
        if num_heads <= 0 or num_kv_groups <= 0 or num_heads % num_kv_groups:
            raise ValueError("num_kv_groups must be positive and divide num_heads")
        if head_dim != 64:
            raise ValueError("head_dim must be 64")
        if seq_len <= 0 or seq_len % 256:
            raise ValueError("seq_len must be a positive multiple of 256")
        if embedding_dim <= 0 or embedding_dim % 64:
            raise ValueError("embedding_dim must be a positive multiple of 64")
        self.num_heads, self.num_kv_groups = num_heads, num_kv_groups
        self.head_dim, self.embedding_dim, self.seq_len = (
            head_dim,
            embedding_dim,
            seq_len,
        )
        self.causal_mask = causal_mask
        self.block_rows = seq_len if seq_len <= 1024 else math.gcd(seq_len, 512)
        self.scale = param(np.full((256,), 1 / math.sqrt(head_dim), dtype=bfloat16))
        # One diagonal mask shared across query blocks.
        self.mask = (
            param(
                np.broadcast_to(
                    np.triu(
                        np.full(
                            (self.block_rows, self.block_rows),
                            -np.inf,
                        ),
                        k=1,
                    ),
                    (num_heads, self.block_rows, self.block_rows),
                ).astype(bfloat16)
            )
            if causal_mask
            else None
        )
        self.attn_context = state((num_heads, seq_len, head_dim))
        # Sliced intermediates are pinned by the graph allocator. Reuse one
        # state for the partial writes so each block does not pin its scores.
        self.scores = state((num_heads * self.block_rows * seq_len,))

    def body(self, queries, keys, values):
        h, g, s, d = self.num_heads, self.num_kv_groups, self.seq_len, self.head_dim
        if (
            queries.shape != (h, s, d)
            or keys.shape != (g, s, d)
            or values.shape != (g, s, d)
        ):
            raise ValueError(
                f"expected queries {(h, s, d)}, keys and values {(g, s, d)}"
            )
        for start in range(0, s, self.block_rows):
            stop = start + self.block_rows
            # Causal blocks read only the prefix they can attend to. The
            # triangular addend masks the future inside the last block.
            end = stop if self.causal_mask else s
            scores = self.scores[: h * self.block_rows * end].reshape(
                h, self.block_rows, end
            )
            for head in range(h):
                group = head // (h // g)
                _gemm(
                    queries[head, start:stop],
                    keys[group, :end],
                    scores[head],
                    b_col_maj=True,
                )
            # Scale in short rows: a scalar broadcast holds one constant
            # row on each core, so a seq_len-wide row would exceed L1.
            short_rows = scores.reshape(h * self.block_rows * end // 256, 256)
            RowwiseMul.step(short_rows, self.scale, short_rows)
            if self.causal_mask:
                if start == 0:
                    # The first block is its entire diagonal, contiguous.
                    ElementwiseAdd.step(scores, self.mask, scores)
                else:
                    diagonal = Copy.step(scores[:, :, start:stop])
                    scores[:, :, start:stop] = diagonal + self.mask
            # A streamed softmax unrolls its rows on each core. Splitting at
            # 256 rows fits four channels on both NPU1 and NPU2.
            rows = h * self.block_rows
            batch = rows if end <= 4096 else 256
            flat = scores.reshape(rows, end)
            for row in range(0, rows, batch):
                part = flat[row : min(row + batch, rows)]
                Softmax.step(part, part)
            for head in range(h):
                group = head // (h // g)
                _gemm(
                    scores[head],
                    values[group, :end],
                    self.attn_context[head, start:stop],
                    accumulate_f32=True,
                )
        return Copy.step(self.attn_context)


class AttentionPrefillProjectedFused(Graph):
    """Prefill with Q/K/V projections, two-halves RoPE and output projection.

    Inputs are ``x (S, E)``, interleaved cos/sin ``rope_angles (S, d)``,
    ``w_query (E, H*d)``, ``w_key/w_value (E, G*d)`` and
    ``w_output (H*d, E)``. The output is ``(S, E)``.
    """

    profile = _PROFILES

    def __init__(
        self,
        num_heads: int,
        num_kv_groups: int,
        head_dim: int,
        embedding_dim: int,
        seq_len: int,
        causal_mask: bool = True,
    ):
        self.attention = AttentionPrefillFused(
            num_heads, num_kv_groups, head_dim, embedding_dim, seq_len, causal_mask
        )

    def body(self, x, rope_angles, w_query, w_key, w_value, w_output):
        a = self.attention
        h, g, s, d, e = (
            a.num_heads,
            a.num_kv_groups,
            a.seq_len,
            a.head_dim,
            a.embedding_dim,
        )
        expected = ((s, e), (s, d), (e, h * d), (e, g * d), (e, g * d), (h * d, e))
        actual = tuple(
            t.shape for t in (x, rope_angles, w_query, w_key, w_value, w_output)
        )
        if actual != expected:
            raise ValueError(f"expected input shapes {expected}, got {actual}")
        q = RoPE.step(_gemm(x, w_query).reshape(s * h, d), rope_angles)
        k = RoPE.step(_gemm(x, w_key).reshape(s * g, d), rope_angles)
        v = _gemm(x, w_value)
        # Copy materializes the views once; no explicit transpose or GQA repeat
        # operator is needed. The nested graph is captured in this dispatch.
        q = Copy.step(q.reshape(s, h, d).transpose(1, 0, 2))
        k = Copy.step(k.reshape(s, g, d).transpose(1, 0, 2))
        v = Copy.step(v.reshape(s, g, d).transpose(1, 0, 2))
        context = self.attention(q, k, v)
        interleaved = Copy.step(context.transpose(1, 0, 2)).reshape(s, h * d)
        return _gemm(interleaved, w_output, accumulate_f32=True)
