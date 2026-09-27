# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 on the NPU, as one graph.

:class:`Llama3_2_1b`'s body is the model over ``x``, the embedded tokens,
``(rows, emb_dim)``, and branches on that static shape. One row is a decode
step: GEMV projections, attention against the key and value caches, the row
written into them at ``cache_offset``, the softmax masked to
``vector_size`` keys. ``max_seq_len`` rows are a prompt, of which a call
runs the first ``rows`` (:func:`prompt_rows`): GEMM projections, causal MHA
masked to the ``vector_size`` tokens of the prompt, the caches written from
row zero, and the norm and head for row ``last`` alone.

Each shape compiles its own version, and every version runs in the graph's
one scratch arena (:mod:`iron.common.graph.compiled`): the weights and the
caches are uploaded once, and the caches a prompt writes are the ones the
next decode step reads.

The operators' knobs are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Llama 3.2 1B's shape and a ``max_seq_len`` of
2048. A call site gives a knob only where two operators of one shape want
different ones.
"""

import math
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.device import bound_device
from iron.operators.copy import Copy
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
from iron.operators.transpose import Transpose


def prompt_rows(n: int, max_seq_len: int) -> int:
    """The rows a prompt of ``n`` tokens runs: ``n`` rounded up to what MHA's
    pipelines take at once (64 rows each, eight of them at full length),
    which the GEMMs' row block divides, at most ``max_seq_len``.
    """
    unit = 64 * min(8, max_seq_len // 64)
    return min(-(-n // unit) * unit, max_seq_len)


class Llama3_2_1b(iron.Graph):
    """The model on ``config``'s shape and ``weights`` (``embedding``, which
    is the output head too, ``norm`` and ``layers``), with ``keys[i]`` and
    ``values[i]`` each layer's cache, ``(n_kv_groups, max_seq_len,
    head_dim)``. Every matrix is read ``(out, in)``, as the checkpoint ships
    it: GEMV's ``(M, K)`` and GEMM's column-major B.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, config, weights):
        self.config = config
        self.embedding, self.norm = weights.embedding, weights.norm
        self.layers = weights.layers
        G, L, D = config.n_kv_groups, config.max_seq_len, config.head_dim
        self.keys = [iron.state((G, L, D)) for _ in self.layers]
        self.values = [iron.state((G, L, D)) for _ in self.layers]
        # 1/sqrt(head_dim) over every score, as the elementwise multiply takes it.
        self.scale = np.full((config.n_heads, L), 1 / math.sqrt(D), dtype=bfloat16)
        # A float32 table would be another input signature, another compile.
        self.angles = config.angles().astype(bfloat16)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches

    def body(
        self,
        x,
        angles,
        *,
        rows: Scratchpad[np.int32],
        cache_offset: Scratchpad[np.int32],
        vector_size: Scratchpad[np.int32],
        last: Scratchpad[np.int32],
    ):
        prompt = x.shape[0] > 1
        if prompt:
            # Every operator below runs the rows of this call alone.
            x, angles = x[:rows], angles[:rows]
        for i, layer in enumerate(self.layers):
            h = RMSNorm(x, layer.norm1)
            if prompt:
                o = self.prompt_attention(i, layer, h, angles, rows, vector_size)
            else:
                o = self.decode_attention(
                    i, layer, h, angles, cache_offset, vector_size
                )
            x = ElementwiseAdd(x, o)
            h = RMSNorm(x, layer.norm2)
            gate = project(h, layer.gate)
            up = project(h, layer.up)
            x = ElementwiseAdd(x, project(ElementwiseMul(SiLU(gate), up), layer.down))
        if prompt:
            x = Copy(x[last]).reshape(1, self.config.emb_dim)  # all the host reads
        return GEMV(self.embedding, RMSNorm(x, self.norm))

    def decode_attention(self, i, layer, h, angles, cache_offset, vector_size):
        H, G, D = self.config.n_heads, self.config.n_kv_groups, self.config.head_dim
        # Half a head per tile; q's shape is o's when H * D == E, so it is
        # given here rather than by the profile.
        q, k, v = (
            GEMV(w, h, tile_size_output=D // 2) for w in (layer.q, layer.k, layer.v)
        )
        q = RoPE(q.reshape(H, D), angles)
        Copy(RoPE(k.reshape(G, D), angles), self.keys[i][:, cache_offset])
        Copy(v.reshape(G, D), self.values[i][:, cache_offset])
        # Every head sees its group's keys and values.
        k_all = Repeat(self.keys[i], repeat=H // G)
        v_all = Repeat(self.values[i], repeat=H // G)
        # One row of scores per column; its size is the FFN's when H * L == F.
        tile = self.config.max_seq_len // _columns()
        scores = ElementwiseMul(GEMV(k_all, q), self.scale, tile_size=tile)
        # Masked from the context length on: the cache's unwritten tail
        # contributes nothing.
        weights = Softmax(scores, vector_size=vector_size)
        ctx = GEMV(Transpose(v_all), weights)
        return GEMV(layer.o, ctx.reshape(H * D))

    def prompt_attention(self, i, layer, h, angles, rows, vector_size):
        H, G, D = self.config.n_heads, self.config.n_kv_groups, self.config.head_dim
        n = h.shape[0]
        q, k, v = (project(h, w) for w in (layer.q, layer.k, layer.v))
        # One angle row per position, applied to that position's heads.
        q = RoPE(q.reshape(n * H, D), angles)
        k = RoPE(k.reshape(n * G, D), angles)
        # The heads interleaved per token as the projection wrote them, into
        # the first rows of the cache's (G, L, D).
        for x, cache in ((k, self.keys[i]), (v, self.values[i])):
            Copy(x.reshape(n, G, D).transpose(1, 0, 2), cache[:, :rows], tile_size=1024)
        o = MHA(
            q.reshape(n, H, D),
            k.reshape(n, G, D),
            v.reshape(n, G, D),
            heads_interleaved=True,
            s_q=vector_size,
            s_kv=vector_size,
        )
        return project(o.reshape(n, H * D), layer.o)

    # -- on the host -----------------------------------------------------------

    def shapes(self, rows: int) -> dict:
        """The input shapes of the version that runs ``rows`` tokens."""
        return dict(x=(rows, self.config.emb_dim), angles=(rows, self.config.head_dim))

    def load(self, release=None) -> "Llama3_2_1b":
        """Compile and load the decode and prompt versions, weights uploaded.

        Both before the first call, so the arena is made once at its final
        size. ``release`` is given each piece of each weight once it is on
        the device, to drop the host's pages of it.
        """
        for rows in (1, self.config.max_seq_len):
            self.compile(**self.shapes(rows))
        for version in self.versions.values():
            version.load(release=release)
        return self

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, ``(vocab_size,)``.

        ``tokens`` is the whole history. One more token than the last call's
        is a decode step on the caches; anything else is a prompt.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n, seen, L = tokens.size, self._seen.size, self.config.max_seq_len
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        # Every call passes every per-call value; a version reads the ones
        # its operators bind.
        if n == seen + 1 and np.array_equal(tokens[:seen], self._seen):
            out = self(
                self.embedding[tokens[seen:]],
                self.angles[seen:n],
                rows=1,
                cache_offset=seen,
                vector_size=n,
                last=0,
            )
        else:
            x = np.zeros((L, self.config.emb_dim), dtype=bfloat16)
            x[:n] = self.embedding[tokens]
            out = self(
                x,
                self.angles,
                rows=prompt_rows(n, L),
                cache_offset=0,
                vector_size=n,
                last=n - 1,
            )
        self._seen = tokens
        # A copy: the image's output buffer is rewritten by the next call.
        return np.array(out.numpy()).reshape(-1)


def project(x, weight):
    """``x @ weight.T`` for a checkpoint's ``(out, in)`` weight: a GEMV for
    one row (a GEMV's output is a vector), else a GEMM reading it
    column-major.
    """
    if len(x.shape) == 2 and x.shape[0] > 1:
        return GEMM(x, weight, b_col_maj=True)
    return GEMV(weight, x)


def _columns() -> int:
    """The bound device's width: eight on NPU2, four on NPU1."""
    return bound_device().cols
