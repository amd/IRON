#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 over the shared decoder (:mod:`iron.lm`): its
layer and head on the NPU (:class:`Llama`) and on the CPU in float32
(:class:`LlamaOracle`, the reference it is judged by), where its
checkpoint keeps each weight, its tokenizer, and Llama 3.2 1B's shape.
Run it with ``python -m iron.lm.llama3.model``.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Llama 3.2 1B's shape and a ``max_seq_len`` of
2048. A call site gives a tunable only where two operators of one shape want
different ones.
"""

from pathlib import Path

import numpy as np
import tiktoken
import tiktoken.load

from iron import lm
from iron.lm import CausalLM, Config, Layout, Oracle, project
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv.op import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import LLAMA_3_2, RoPE
from iron.operators.silu import SiLU

LLAMA_3_2_1B = Config(
    vocab_size=128256,
    emb_dim=2048,
    n_layers=16,
    n_heads=32,
    n_kv_groups=8,
    head_dim=64,
    hidden_dim=8192,
    max_seq_len=2048,
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
        gate = h @ w.gate.T
        # SiLU, with the sigmoid as a tanh, which does not overflow.
        silu = gate * np.float32(0.5) * (1 + np.tanh(gate * np.float32(0.5)))
        return x + (silu * (h @ w.up.T)) @ w.down.T

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
        h = RMSNorm(x, w.norm1)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (project(h, p, tile_size_output=D // 2) for p in (w.q, w.k, w.v))
        # One angle row per position, applied to that position's heads.
        q = RoPE(q.reshape(n * H, D), step.angles)
        k = RoPE(k.reshape(n * G, D), step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), w.o))
        h = RMSNorm(x, w.norm2)
        gate, up = project(h, w.gate), project(h, w.up)
        return ElementwiseAdd(x, project(ElementwiseMul(SiLU(gate), up), w.down))

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, self.norm))


def layout(config: Config) -> Layout:
    """Each weight's place in :class:`Llama`, its name in a Hugging Face
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
    "<|begin_of_text|>": 128000,
    "<|end_of_text|>": 128001,
    "<|start_header_id|>": 128006,
    "<|end_header_id|>": 128007,
    "<|eot_id|>": 128009,
    **{
        f"<|reserved_{i}|>": i for i in [*range(128002, 128006), *range(128009, 128256)]
    },
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
