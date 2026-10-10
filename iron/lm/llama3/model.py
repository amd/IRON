#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 over the shared decoder (``iron.lm``): its
layer and head on the NPU (``Llama``) and on the CPU in float32
(``LlamaOracle``, the reference it is judged by), where its
checkpoint keeps each weight, its tokenizer, and Llama 3.2 1B's shape.
Run it with ``python -m iron.lm.llama3.model``.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Llama 3.2 1B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone. A call site gives a tunable only where two operators of
one shape want different ones.
"""

import dataclasses
from pathlib import Path

import numpy as np
import tiktoken
import tiktoken.load

from iron import lm
from iron.lm import CausalLM, Config, Layout, Oracle, project, swiglu
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE


@dataclasses.dataclass(frozen=True)
class Llama3RopeScaling:
    """Llama 3's RoPE frequency scaling (``"rope_type": "llama3"``).

    How Llama 3.1 and later stretch a model trained at
    ``original_max_position_embeddings`` to a longer context, by frequency:
    one whose wavelength is under ``original / high_freq_factor`` positions
    is kept, one over ``original / low_freq_factor`` is divided by
    ``factor``, and one between is interpolated between the two by where its
    wavelength falls. The fields are the checkpoint's ``rope_scaling``.
    """

    factor: float
    low_freq_factor: float
    high_freq_factor: float
    original_max_position_embeddings: int

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        """``inv_freq`` (radians per position, per frequency), scaled."""
        original = self.original_max_position_embeddings
        wavelen = 2 * np.pi / inv_freq
        smooth = (original / wavelen - self.low_freq_factor) / (
            self.high_freq_factor - self.low_freq_factor
        )
        between = (1 - smooth) * inv_freq / self.factor + smooth * inv_freq
        return np.where(
            wavelen < original / self.high_freq_factor,
            inv_freq,
            np.where(
                wavelen > original / self.low_freq_factor,
                inv_freq / self.factor,
                between,
            ),
        )


#: Llama 3.2's scaling, as its checkpoints' ``rope_scaling`` gives it.
LLAMA_3_2 = Llama3RopeScaling(
    factor=32.0,
    low_freq_factor=1.0,
    high_freq_factor=4.0,
    original_max_position_embeddings=8192,
)


LLAMA_3_2_1B = Config(
    vocab_size=128256,
    emb_dim=2048,
    n_layers=16,
    n_heads=32,
    n_kv_groups=8,
    head_dim=64,
    hidden_dim=8192,
    max_seq_len=32768,
    rope_base=500000.0,
    rope_scaling=LLAMA_3_2,
)

# Llama's RMSNorm epsilon.
EPS = np.float32(1e-5)


class LlamaOracle(Oracle):
    """Llama 3's forward pass in float32, on the host."""

    norm: np.ndarray

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = rms_norm(x, w.norm1)
        q = self.rotate((h @ w.q.T).reshape(n, H, D), angles)
        k = self.rotate((h @ w.k.T).reshape(n, G, D), angles)
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
    return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + EPS) * w


class Llama(CausalLM):
    """Llama 3 on ``config``'s shape and ``weights`` (``embedding``, which is
    the output head too, ``norm`` and ``layers``). Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = LlamaOracle
    norm: np.ndarray

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        h = RMSNorm(x, weight=w.norm1)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (project(h, p, tile_size_output=D // 2) for p in (w.q, w.k, w.v))
        # One angle row per position, applied to that position's heads.
        q = RoPE(q.reshape(n * H, D), step.angles)
        k = RoPE(k.reshape(n * G, D), step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), w.o))
        h = RMSNorm(x, weight=w.norm2)
        return ElementwiseAdd(x, swiglu(h, w.gate, w.up, w.down))

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, weight=self.norm))


def layout(config: Config) -> Layout:
    """Each weight's place in ``Llama``, its name in a Hugging Face
    checkpoint and its shape. The output head is the embedding, tied.
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
        "layers.{i}.k": (f"{layer}.self_attn.k_proj.weight", (KV, E)),
        "layers.{i}.v": (f"{layer}.self_attn.v_proj.weight", (KV, E)),
        "layers.{i}.o": (f"{layer}.self_attn.o_proj.weight", (E, Q)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
    }


SPECIAL_TOKENS = {
    name: 128000 + i
    for i, name in enumerate(
        [
            "<|begin_of_text|>",
            "<|end_of_text|>",
            "<|reserved_special_token_0|>",
            "<|reserved_special_token_1|>",
            "<|finetune_right_pad_id|>",
            "<|step_id|>",
            "<|start_header_id|>",
            "<|end_header_id|>",
            "<|eom_id|>",
            "<|eot_id|>",
            "<|python_tag|>",
            "<|image|>",
            *(f"<|reserved_special_token_{i}|>" for i in range(2, 246)),
        ]
    )
}


def tokenizer(path) -> tiktoken.Encoding:
    """Llama 3's tokenizer, from its ``tokenizer.model``."""
    return tiktoken.Encoding(
        name="llama3.2-1b",
        pat_str=r"(?i:'s|'t|'re|'ve|'m|'ll|'d)"
        r"|[^\r\n\p{L}\p{N}]?\p{L}+"
        r"|\p{N}{1,3}"
        r"| ?[^\s\p{L}\p{N}]+[\r\n]*"
        r"|\s*[\r\n]+"
        r"|\s+(?!\S)"
        r"|\s+",
        mergeable_ranks=tiktoken.load.load_tiktoken_bpe(str(path)),
        special_tokens=SPECIAL_TOKENS,
    )


class Runner(lm.Runner):
    """Llama 3.2 1B, from its checkpoint and ``tokenizer.model``."""

    config = LLAMA_3_2_1B
    layout = staticmethod(layout)
    model = Llama
    open_tokenizer = staticmethod(tokenizer)
    bos = SPECIAL_TOKENS["<|begin_of_text|>"]


if __name__ == "__main__":
    lm.main(Runner, "Llama 3.2 1B on the NPU")
