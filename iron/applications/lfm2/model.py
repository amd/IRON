#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B over the shared decoder (``iron.lm``): its hybrid layers on
the NPU (``Lfm2``) and in float32 (``Lfm2Oracle``), where its checkpoint
keeps each weight, its tokenizer, and LFM2-1.2B's shape. Run it with
``python -m iron.applications.lfm2.model``.

Sixteen layers, only six of them full attention (``full_attn_idxs``); the
rest are a gated short causal depth-wise convolution (``conv_L_cache=3``
taps) in place of attention, each still followed by the same SwiGLU
feed-forward every layer has. A conv layer's three per-channel taps read a
window that spans the current call and the one before it, so each conv
layer keeps a cache the same shape convention as attention's key/value
caches (``(max_seq_len, conv_dim)``, one extra leading block that is never
written and so stays zero, standing in for "before the sequence") plus a
small scratch buffer a prompt chunk assembles its window in.

The operators' tunables are the graph's profile, ``profiles/<device>.json``.
"""

import dataclasses
from pathlib import Path

import numpy as np
from aie.iron.kernels.sample import ROW_WORDS
from ml_dtypes import bfloat16
from tokenizers import Tokenizer

import iron
from iron import lm
from iron.lm import CausalLM, Config, Layout, Oracle, project, swiglu
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE

# LFM2's RMSNorm epsilon (``norm_eps`` / ``block_norm_eps`` in its config),
# the same value RMSNorm already defaults to.
EPS = np.float32(1e-5)


@dataclasses.dataclass(frozen=True)
class Lfm2Config(Config):
    #: Layer indices that are full attention; every other layer is a
    #: gated short conv.
    full_attn_idxs: tuple[int, ...] = ()
    #: The short conv's kernel width (``conv_L_cache``).
    conv_kernel: int = 3


LFM2_1_2B = Lfm2Config(
    vocab_size=65536,
    emb_dim=2048,
    n_layers=16,
    n_heads=32,
    n_kv_groups=8,
    head_dim=64,
    hidden_dim=8192,
    max_seq_len=32768,
    rope_base=1000000.0,
    full_attn_idxs=(2, 5, 8, 10, 12, 14),
)


def rms_norm(x, w):
    return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + EPS) * w


class Lfm2Oracle(Oracle):
    """LFM2-1.2B's forward pass in float32, on the host."""

    norm: np.ndarray

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        h = rms_norm(x, w.norm1)
        if "q" in vars(w):
            H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
            q = rms_norm((h @ w.q.T).reshape(n, H, D), w.q_norm)
            k = rms_norm((h @ w.k.T).reshape(n, G, D), w.k_norm)
            v = (h @ w.v.T).reshape(n, G, D)
            q, k = self.rotate(q, angles), self.rotate(k, angles)
            y = self.attend(q, k, v) @ w.o.T
        else:
            y = self._conv(h, w)
        x = x + y
        h = rms_norm(x, w.norm2)
        F = w.gate.shape[0]
        half = np.matmul(h, w.gate.T, out=self.buffer("gate", (n, F)))
        half *= np.float32(0.5)
        # SiLU, with the sigmoid as a tanh, which does not overflow.
        silu = np.tanh(half, out=self.buffer("silu", (n, F)))
        silu += 1
        silu *= half
        silu *= np.matmul(h, w.up.T, out=self.buffer("up", (n, F)))
        return x + silu @ w.down.T

    def _conv(self, h, w):
        c = self.config
        n, E, K = h.shape[0], h.shape[1], c.conv_kernel
        bcx = h @ w.conv_in.T
        b, cc, x = bcx[:, :E], bcx[:, E : 2 * E], bcx[:, 2 * E :]
        gated = b * x
        taps = w.conv_weight.reshape(E, K)
        padded = np.concatenate(
            [np.zeros((K - 1, E), dtype=np.float32), gated], axis=0
        )
        total = np.zeros((n, E), dtype=np.float32)
        for k in range(K):
            total += taps[:, k] * padded[k : k + n]
        return (cc * total) @ w.conv_out.T

    def head(self, x):
        return rms_norm(x, self.norm) @ self.embedding.T


class Lfm2(CausalLM):
    """LFM2-1.2B on ``config``'s shape and ``weights`` (``embedding``, which
    is the output head too, ``norm`` and ``layers``, each either an
    attention layer's weights or a conv layer's). Every matrix is read
    ``(out, in)``, as the checkpoint ships it.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Lfm2Oracle
    norm: np.ndarray

    def __init__(self, config: Lfm2Config, weights):
        self.config = config
        vars(self).update(vars(weights))
        self.embedding = iron.weight(weights.embedding)
        c = config
        G, D, L, Cc = c.n_kv_groups, c.head_dim, c.max_seq_len, c.prefill_chunk
        E = c.emb_dim
        self.keys, self.values, self.window, self.conv_scratch = {}, {}, {}, {}
        for i, w in enumerate(self.layers):
            if "q" in vars(w):
                self.keys[i] = iron.state((L, G, D))
                self.values[i] = iron.state((L, G, D))
            else:
                # One extra leading block, never written, stands in for
                # "before the sequence": always zero.
                self.window[i] = iron.state((L + Cc, E))
                self.conv_scratch[i] = iron.state((Cc + c.conv_kernel - 1, E))
        self.rope = iron.weight(config.angles().astype(bfloat16))
        self.draws = iron.state((L, ROW_WORDS), np.int32)
        self.drawn = iron.state((L,), np.int32)
        self._seen = np.empty(0, dtype=np.int64)
        self._prompt = None
        self._decode = None
        self._loop = None

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        h = RMSNorm(x, weight=w.norm1)
        if "q" in vars(w):
            H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
            q, k, v = (project(h, p, tile_size_output=D // 2) for p in (w.q, w.k, w.v))
            q = RMSNorm(q.reshape(n * H, D), weight=w.q_norm)
            k = RMSNorm(k.reshape(n * G, D), weight=w.k_norm)
            q = RoPE(q, step.angles)
            k = RoPE(k, step.angles)
            y = project(self.attend(step, i, q, k, v), w.o)
        else:
            y = self.conv(step, i, w, h)
        x = ElementwiseAdd(x, y)
        h = RMSNorm(x, weight=w.norm2)
        return ElementwiseAdd(x, swiglu(h, w.gate, w.up, w.down))

    def conv(self, step, i, w, h):
        """The gated short conv in place of attention: a depth-wise causal
        FIR of ``conv_kernel`` taps over ``h``'s rows, each channel its own
        tap weights, gated on both sides by a projection of ``h``.
        """
        c, n = self.config, h.shape[0]
        E, K, Cc = c.emb_dim, c.conv_kernel, c.prefill_chunk
        # Three projections, not one split three ways: a bounded row count's
        # column range of a combined projection is a strided view no single
        # descriptor fits, where three plain projections need none.
        b = project(h, w.conv_in[:E]).reshape(n, E)
        cc = project(h, w.conv_in[E : 2 * E]).reshape(n, E)
        x = project(h, w.conv_in[2 * E : 3 * E]).reshape(n, E)
        gated = ElementwiseMul(b, x)
        taps = w.conv_weight.reshape(E, K)
        window = self.window[i]
        if step.prompt:
            blocks = c.max_seq_len // Cc + 1
            view = window.reshape(blocks, Cc, E)
            Copy(gated, view[step.chunk + 1, : step.rows])
            scratch = self.conv_scratch[i]
            Copy(view[step.chunk, Cc - (K - 1) :], scratch[: K - 1])
            Copy(view[step.chunk + 1, :], scratch[K - 1 :])
            total = RowwiseMul(scratch[0:Cc], taps[:, 0])
            for k in range(1, K):
                total = ElementwiseAdd(total, RowwiseMul(scratch[k : k + Cc], taps[:, k]))
            total = total[: step.rows]
        else:
            pos = step.position
            Copy(gated.reshape(E), window[pos + Cc])
            total = RowwiseMul(gated, taps[:, K - 1])
            for k in range(K - 1):
                prior = Copy(window[pos + Cc - (K - 1) + k]).reshape(1, E)
                total = ElementwiseAdd(total, RowwiseMul(prior, taps[:, k]))
        y = ElementwiseMul(cc, total)
        return project(y, w.conv_out)

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, weight=self.norm))


def layout(config: Lfm2Config) -> Layout:
    """Each weight's place in ``Lfm2``, its name in a Hugging Face
    checkpoint and its shape. The output head is the embedding, tied.
    Every layer carries a norm and a SwiGLU feed-forward; an attention
    layer's index (``full_attn_idxs``) additionally carries its attention
    weights, every other index its short conv's.
    """
    c = config
    E, F, V, D = c.emb_dim, c.hidden_dim, c.vocab_size, c.head_dim
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    out: Layout = {
        "embedding": ("model.embed_tokens.weight", (V, E)),
        "norm": ("model.embedding_norm.weight", (E,)),
    }
    for i in range(c.n_layers):
        prefix = f"model.layers.{i}"
        out[f"layers.{i}.norm1"] = (f"{prefix}.operator_norm.weight", (E,))
        out[f"layers.{i}.norm2"] = (f"{prefix}.ffn_norm.weight", (E,))
        out[f"layers.{i}.gate"] = (f"{prefix}.feed_forward.w1.weight", (F, E))
        out[f"layers.{i}.up"] = (f"{prefix}.feed_forward.w3.weight", (F, E))
        out[f"layers.{i}.down"] = (f"{prefix}.feed_forward.w2.weight", (E, F))
        if i in c.full_attn_idxs:
            out[f"layers.{i}.q"] = (f"{prefix}.self_attn.q_proj.weight", (Q, E))
            out[f"layers.{i}.k"] = (f"{prefix}.self_attn.k_proj.weight", (KV, E))
            out[f"layers.{i}.v"] = (f"{prefix}.self_attn.v_proj.weight", (KV, E))
            out[f"layers.{i}.o"] = (f"{prefix}.self_attn.out_proj.weight", (E, Q))
            out[f"layers.{i}.q_norm"] = (f"{prefix}.self_attn.q_layernorm.weight", (D,))
            out[f"layers.{i}.k_norm"] = (f"{prefix}.self_attn.k_layernorm.weight", (D,))
        else:
            out[f"layers.{i}.conv_in"] = (f"{prefix}.conv.in_proj.weight", (3 * E, E))
            out[f"layers.{i}.conv_out"] = (f"{prefix}.conv.out_proj.weight", (E, E))
            out[f"layers.{i}.conv_weight"] = (
                f"{prefix}.conv.conv.weight",
                (E, 1, c.conv_kernel),
            )
    return out


class _Tokenizer:
    """``tokenizers.Tokenizer``, wrapped to ``encode``/``decode`` plain
    token id lists: its own post-processor already adds BOS, which
    ``lm.Runner.encode`` adds again, so it is dropped here once.
    """

    def __init__(self, tok: Tokenizer):
        self._tok = tok

    def encode(self, text: str) -> list[int]:
        return self._tok.encode(text).ids[1:]

    def decode(self, tokens) -> str:
        return self._tok.decode(tokens)


def tokenizer(path) -> _Tokenizer:
    return _Tokenizer(Tokenizer.from_file(str(path)))


class Runner(lm.Runner):
    """LFM2-1.2B, from its checkpoint and ``tokenizer.json``."""

    config = LFM2_1_2B
    layout = staticmethod(layout)
    model = Lfm2
    open_tokenizer = staticmethod(tokenizer)
    bos = 1


if __name__ == "__main__":
    lm.main(Runner, "LFM2-1.2B on the NPU")
