#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 over the shared decoder (``iron.lm``): its layer and head on the
NPU (``Qwen3``) and on the CPU in float32 (``Qwen3Oracle``, the reference it
is judged by), where its checkpoint keeps each weight, its tokenizer, and
Qwen3 1.7B's shape. Run it with ``python -m iron.applications.qwen3.model``.

Qwen3 is Llama-style GQA and SwiGLU, with two differences: a per-head
RMSNorm on Q and K before RoPE (``q_norm``/``k_norm``, one weight row of
``head_dim``, shared by every head and every position -- a composition of
the existing weighted ``RMSNorm`` at a new shape, not a new operator), and
``rms_norm_eps`` of 1e-6 rather than Llama's 1e-5, passed explicitly to
every ``RMSNorm`` call since it is a ``param``, not an ``auto()`` tunable a
profile can fill. Its output head is the input embedding, tied; its
checkpoint also ships ``lm_head.weight``, confirmed byte-identical to
``model.embed_tokens.weight`` by sha256, which the layout maps but ``head()``
never reads.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen3 1.7B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone. A call site gives a tunable only where two operators of
one shape want different ones.
"""

import dataclasses
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer as HFTokenizer

from iron import lm
from iron.lm import CausalLM, Config, Layout, Oracle, project, swiglu
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE

QWEN3_1_7B = Config(
    vocab_size=151936,
    emb_dim=2048,
    n_layers=28,
    n_heads=16,
    n_kv_groups=8,
    head_dim=128,
    hidden_dim=6144,
    max_seq_len=32768,
    rope_base=1000000.0,
)

# Qwen3's RMSNorm epsilon (Llama's is 1e-5). A plain Python float: RMSNorm's
# own ``epsilon`` param is typed ``float`` and the design builder rejects an
# np.float32 scalar immediate (it is not a `float` instance).
EPS = 1e-6


class Qwen3Oracle(Oracle):
    """Qwen3's forward pass in float32, on the host."""

    norm: np.ndarray

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = rms_norm(x, w.norm1)
        q = rms_norm((h @ w.q.T).reshape(n, H, D), w.q_norm)
        q = self.rotate(q, angles)
        k = rms_norm((h @ w.k.T).reshape(n, G, D), w.k_norm)
        k = self.rotate(k, angles)
        v = (h @ w.v.T).reshape(n, G, D)
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
    return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + np.float32(EPS)) * w


class Qwen3(CausalLM):
    """Qwen3 on ``config``'s shape and ``weights`` (``embedding``, which is
    the output head too, ``norm`` and ``layers``). Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Qwen3Oracle
    norm: np.ndarray

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = RMSNorm(x, weight=w.norm1, epsilon=EPS)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (project(h, p, tile_size_output=D // 2) for p in (w.q, w.k, w.v))
        # One norm row per head, shared by every head and every position.
        q = RMSNorm(q.reshape(n * H, D), weight=w.q_norm, epsilon=EPS)
        k = RMSNorm(k.reshape(n * G, D), weight=w.k_norm, epsilon=EPS)
        # One angle row per position, applied to that position's heads.
        q = RoPE(q, step.angles)
        k = RoPE(k, step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), w.o))
        h = RMSNorm(x, weight=w.norm2, epsilon=EPS)
        return ElementwiseAdd(x, swiglu(h, w.gate, w.up, w.down))

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, weight=self.norm, epsilon=EPS))


def layout(config: Config) -> Layout:
    """Each weight's place in ``Qwen3``, its name in a Hugging Face
    checkpoint and its shape. The output head is the embedding, tied;
    ``lm_head`` is mapped only so ``load_weights``'s strict check accepts
    the checkpoint's own (byte-identical) copy of it, and is never read.
    """
    c = config
    E, F, V, D = c.emb_dim, c.hidden_dim, c.vocab_size, c.head_dim
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    layer = "model.layers.{i}"
    return {
        "embedding": ("model.embed_tokens.weight", (V, E)),
        "lm_head": ("lm_head.weight", (V, E)),
        "norm": ("model.norm.weight", (E,)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.q": (f"{layer}.self_attn.q_proj.weight", (Q, E)),
        "layers.{i}.q_norm": (f"{layer}.self_attn.q_norm.weight", (D,)),
        "layers.{i}.k": (f"{layer}.self_attn.k_proj.weight", (KV, E)),
        "layers.{i}.k_norm": (f"{layer}.self_attn.k_norm.weight", (D,)),
        "layers.{i}.v": (f"{layer}.self_attn.v_proj.weight", (KV, E)),
        "layers.{i}.o": (f"{layer}.self_attn.o_proj.weight", (E, Q)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
    }


class Tokenizer:
    """Qwen3's tokenizer, over ``tokenizers`` (Hugging Face's Rust library,
    not ``transformers``), which this venv has and torch does not.
    """

    def __init__(self, inner: HFTokenizer):
        self._inner = inner

    def encode(self, text: str) -> list[int]:
        return self._inner.encode(text, add_special_tokens=False).ids

    def decode(self, tokens: list[int]) -> str:
        return self._inner.decode(tokens, skip_special_tokens=False)


def tokenizer(path) -> Tokenizer:
    """Qwen3's tokenizer, from its ``tokenizer.json``."""
    return Tokenizer(HFTokenizer.from_file(str(path)))


class Runner(lm.Runner):
    """Qwen3 1.7B, from its checkpoint and ``tokenizer.json``.

    Qwen3's ``tokenizer_config.json`` names no ``bos_token``; its
    ``generation_config.json`` names ``<|endoftext|>`` (151643) as both
    ``bos_token_id`` and ``pad_token_id``, which is used here as every
    prompt's leading token, as ``lm.Runner`` requires one.
    """

    config = QWEN3_1_7B
    layout = staticmethod(layout)
    model = Qwen3
    open_tokenizer = staticmethod(tokenizer)
    bos = 151643


if __name__ == "__main__":
    lm.main(Runner, "Qwen3 1.7B on the NPU")
