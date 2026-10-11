#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2 over the shared decoder (``iron.lm``): its layer and head on the
NPU (``Qwen2``) and on the CPU in float32 (``Qwen2Oracle``, the reference it
is judged by), where its checkpoint keeps each weight, its tokenizer, and
Qwen 2.5 1.5B Instruct's shape. Run it with ``python -m iron.applications.qwen2.model``.

Qwen 2 is Llama-style (RMSNorm, RoPE, SwiGLU, grouped-query attention) with
one difference a Llama checkpoint has no place for: its q/k/v projections
each carry a bias, added once per output column across every row
(``project(..., bias=...)``, folded with ``RowwiseAdd``). It ties its
embedding and output head, as Llama does, and takes no RoPE frequency
scaling (``rope_scaling`` is absent from its checkpoint's ``config.json``).

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen 2.5 1.5B Instruct's shape: a decode step's
and a 2048-row prompt chunk's, at any ``max_seq_len``, which sizes the
caches and the RoPE table alone. A call site gives a tunable only where two
operators of one shape want different ones.
"""

from pathlib import Path

import numpy as np
from tokenizers import Tokenizer

from iron import lm
from iron.lm import CausalLM, Config, Layout, Oracle, project, swiglu
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE

QWEN2_5_1_5B_INSTRUCT = Config(
    vocab_size=151936,
    emb_dim=1536,
    n_layers=28,
    n_heads=12,
    n_kv_groups=2,
    head_dim=128,
    hidden_dim=8960,
    max_seq_len=32768,
    rope_base=1000000.0,
)

# Qwen 2.5's RMSNorm epsilon.
EPS = np.float32(1e-6)


class Qwen2Oracle(Oracle):
    """Qwen 2.5's forward pass in float32, on the host."""

    norm: np.ndarray

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = rms_norm(x, w.norm1)
        q = self.rotate((h @ w.q.T + w.q_bias).reshape(n, H, D), angles)
        k = self.rotate((h @ w.k.T + w.k_bias).reshape(n, G, D), angles)
        v = (h @ w.v.T + w.v_bias).reshape(n, G, D)
        x = x + self.attend(q, k, v) @ w.o.T
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

    def head(self, x):
        return rms_norm(x, self.norm) @ self.embedding.T


def rms_norm(x, w):
    return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + EPS) * w


class Qwen2(CausalLM):
    """Qwen 2.5 on ``config``'s shape and ``weights`` (``embedding``, which is
    the output head too, ``norm`` and ``layers``). Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Qwen2Oracle
    norm: np.ndarray

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = RMSNorm(x, weight=w.norm1)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (
            project(h, p, bias=b, tile_size_output=D // 2)
            for p, b in ((w.q, w.q_bias), (w.k, w.k_bias), (w.v, w.v_bias))
        )
        # One angle row per position, applied to that position's heads.
        q = RoPE(q.reshape(n * H, D), step.angles)
        k = RoPE(k.reshape(n * G, D), step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), w.o))
        h = RMSNorm(x, weight=w.norm2)
        # 256 divides both emb_dim and hidden_dim, past flm.GEMM's default
        # k_tile (512, not a multiple of hidden_dim's 8960).
        return ElementwiseAdd(x, swiglu(h, w.gate, w.up, w.down, k_tile=256))

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, weight=self.norm))


def layout(config: Config) -> Layout:
    """Each weight's place in ``Qwen2``, its name in a Hugging Face
    checkpoint and its shape. The output head is the embedding, tied; q, k
    and v each carry a bias the checkpoint keeps beside their weight.
    """
    c = config
    E, F, V = c.emb_dim, c.hidden_dim, c.vocab_size
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    layer = "model.layers.{i}"
    return {
        "embedding": ("model.embed_tokens.weight", (V, E)),
        "norm": ("model.norm.weight", (E,)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.q": (f"{layer}.self_attn.q_proj.weight", (Q, E)),
        "layers.{i}.q_bias": (f"{layer}.self_attn.q_proj.bias", (Q,)),
        "layers.{i}.k": (f"{layer}.self_attn.k_proj.weight", (KV, E)),
        "layers.{i}.k_bias": (f"{layer}.self_attn.k_proj.bias", (KV,)),
        "layers.{i}.v": (f"{layer}.self_attn.v_proj.weight", (KV, E)),
        "layers.{i}.v_bias": (f"{layer}.self_attn.v_proj.bias", (KV,)),
        "layers.{i}.o": (f"{layer}.self_attn.o_proj.weight", (E, Q)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
    }


class Qwen2Tokenizer:
    """A Hugging Face ``tokenizer.json``'s ``encode``/``decode``, as plain
    token ids and text.
    """

    def __init__(self, inner: Tokenizer):
        self._inner = inner

    def encode(self, text: str) -> list[int]:
        return self._inner.encode(text).ids

    def decode(self, tokens) -> str:
        return self._inner.decode(tokens)


def tokenizer(path) -> Qwen2Tokenizer:
    """Qwen 2.5's tokenizer, from its ``tokenizer.json``."""
    return Qwen2Tokenizer(Tokenizer.from_file(str(path)))


class Runner(lm.Runner):
    """Qwen 2.5 1.5B Instruct, from its checkpoint and ``tokenizer.json``."""

    config = QWEN2_5_1_5B_INSTRUCT
    layout = staticmethod(layout)
    model = Qwen2
    open_tokenizer = staticmethod(tokenizer)
    # "<|endoftext|>": every prompt's lead token, as Qwen 2.5's own generation
    # config gives it; it carries no chat template of its own.
    bos = 151643


if __name__ == "__main__":
    lm.main(Runner, "Qwen 2.5 1.5B Instruct on the NPU")
