#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct over the shared decoder (``iron.lm``): its layer and
head on the NPU (``Phi4``) and on the CPU in float32 (``Phi4Oracle``, the
reference it is judged by), its checkpoint layout, its tokenizer and its
shape. Run it with ``python -m iron.applications.phi3.model``.

Two things are new here over Llama 3.2 1B's port, neither needing a new
operator (``iron.lm``'s ``Config``/``CausalLM`` grew ``rotary_dim``
and ``rope_attention_scaling`` for this; see their docstrings):

* **Partial rotary.** Only the first ``rotary_dim`` (96 of 128) dimensions
  of each head rotate; the rest pass through unrotated
  (``partial_rotary_factor`` in the checkpoint's config). ``q``/``k`` are
  projected as separate rotary and pass-through weight slices (a free
  host-side reshape of the checkpoint's fused ``qkv_proj`` at load, not a
  device op), so only the rotary slice goes through ``RoPE``, still fully
  contiguous. ``k``'s two slices are written into the existing KV cache's
  own column ranges (the same total bytes the cache write always moved,
  now in two transfers instead of one); ``q`` has no cache to double as
  that assembly point, so a small per-layer scratch state (``q_merge``)
  holds the one place its rotary and pass-through projections are written
  before ``MHA`` reads it whole -- the one place this port moves a query's
  bytes that a whole-head rotary model would not.
* **LongRoPE.** This port runs at ``max_seq_len=4096``, within the
  checkpoint's ``original_max_position_embeddings``: every position takes
  the config's ``short_factor`` (every entry 1.0, so the frequencies are
  plain ``rope_theta=10000`` unscaled) and the constant post-trig
  amplitude scale LongRoPE always applies (``rope_attention_scaling``,
  derived below). The ``long_factor`` branch, for context past 4096, is
  future work -- a second compiled version at a longer ``max_seq_len``
  with its own angle table, not implemented here.

The checkpoint's other fused weight, ``mlp.gate_up_proj``, is a plain row
split (``gate`` first, then ``up``, Hugging Face's own ``chunk(2)`` order);
``qkv_proj``'s three pieces are query rows, then key, then value. Every
other shape is Llama's: GQA, RMSNorm, SwiGLU, a tied output head.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer

import iron
from iron import lm
from iron.lm import CausalLM, Config, Layout, Oracle, project, swiglu
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.copy import Copy

# Phi-4-mini-instruct's config.json: head_dim = hidden_size // num_attention_heads
# (3072 // 24), partial_rotary_factor = 0.75.
_HEAD_DIM = 128
_ROTARY_DIM = int(_HEAD_DIM * 0.75)  # 96; the rest of each head passes through

# LongRoPE's constant post-trig amplitude scale ("attention_factor"/mscale),
# transformers.modeling_rope_utils._compute_longrope_parameters: factor is
# the ratio of the checkpoint's max_position_embeddings (131072, the
# expanded, long-context length) to original_max_position_embeddings (4096,
# the pretrained length); the scale depends on this ratio alone, not on
# which regime a given sequence length falls into, confirmed empirically
# against transformers 5.19.0's own Phi3RotaryEmbedding at seq_len 1 through
# 8192 (iron-next-shared/skill-ports/phi-4-mini-instruct/skill-gaps.md).
_LONGROPE_FACTOR = 131072 / 4096
ATTENTION_SCALING = math.sqrt(1 + math.log(_LONGROPE_FACTOR) / math.log(4096))

PHI_4_MINI = Config(
    vocab_size=200064,
    emb_dim=3072,
    n_layers=32,
    n_heads=24,
    n_kv_groups=8,
    head_dim=_HEAD_DIM,
    hidden_dim=8192,
    # Within original_max_position_embeddings: the short_factor (identity)
    # LongRoPE regime. See the module docstring.
    max_seq_len=4096,
    rope_base=10000.0,
    rotary_dim=_ROTARY_DIM,
    rope_attention_scaling=ATTENTION_SCALING,
    prefill_chunk=2048,
)

# Phi-4-mini-instruct's RMSNorm epsilon (config.json's rms_norm_eps),
# RMSNorm's own default: no override needed, named here for the oracle.
EPS = np.float32(1e-5)


def _split_fused_weights(weights, config: Config):
    """``weights``, Phi-4-mini-instruct's fused ``qkv_proj``/``gate_up_proj``
    per layer split into the pieces ``Phi4``/``Phi4Oracle`` project
    separately. A free host-side reshape at load, once; nothing on the
    per-call path reads ``qkv``/``gate_up`` again.

    Args:
        weights: The tree ``layout`` places a checkpoint in, before
            splitting: each layer holds ``qkv`` and ``gate_up`` whole.
        config: Phi-4-mini-instruct's shape; ``rope_width`` is the rotary
            prefix of ``head_dim``.

    Returns:
        ``weights``, each layer now holding ``q_rot``, ``q_pass``,
        ``k_rot``, ``k_pass``, ``v``, ``gate`` and ``up`` in place of
        ``qkv`` and ``gate_up``.
    """
    c = config
    H, G, D, A, F, E = (
        c.n_heads,
        c.n_kv_groups,
        c.head_dim,
        c.rope_width,
        c.hidden_dim,
        c.emb_dim,
    )
    for w in weights.layers:
        qkv = w.qkv
        q, k, v = qkv[: H * D], qkv[H * D : H * D + G * D], qkv[H * D + G * D :]
        q3, k3 = q.reshape(H, D, E), k.reshape(G, D, E)
        w.q_rot = q3[:, :A, :].reshape(H * A, E)
        w.q_pass = q3[:, A:, :].reshape(H * (D - A), E)
        w.k_rot = k3[:, :A, :].reshape(G * A, E)
        w.k_pass = k3[:, A:, :].reshape(G * (D - A), E)
        w.v = v
        del w.qkv
        gate_up = w.gate_up
        w.gate, w.up = gate_up[:F], gate_up[F:]
        del w.gate_up
    return weights


class Phi4Oracle(Oracle):
    """Phi-4-mini-instruct's forward pass in float32, on the host."""

    norm: np.ndarray

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D, A = c.n_heads, c.n_kv_groups, c.head_dim, c.rope_width
        h = rms_norm(x, w.norm1)
        q_rot = self.rotate((h @ w.q_rot.T).reshape(n, H, A), angles)
        q_pass = (h @ w.q_pass.T).reshape(n, H, D - A)
        q = np.concatenate([q_rot, q_pass], axis=-1)
        k_rot = self.rotate((h @ w.k_rot.T).reshape(n, G, A), angles)
        k_pass = (h @ w.k_pass.T).reshape(n, G, D - A)
        k = np.concatenate([k_rot, k_pass], axis=-1)
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


class Phi4(CausalLM):
    """Phi-4-mini-instruct on ``config``'s shape and ``weights`` (already
    split by ``_split_fused_weights``): ``embedding``, which is the output
    head too, ``norm`` and ``layers``. Every matrix is read ``(out, in)``,
    as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Phi4Oracle
    norm: np.ndarray

    def __init__(self, config: Config, weights):
        super().__init__(config, weights)
        c = self.config
        # q has no cache of its own to double as the place its rotary and
        # pass-through projections land together; this one small per-layer
        # scratch state is that place, MHA reading it whole.
        self.q_merge = [
            iron.state((c.prefill_chunk, c.n_heads, c.head_dim)) for _ in self.layers
        ]

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, G, D, A = c.n_heads, c.n_kv_groups, c.head_dim, c.rope_width
        h = RMSNorm(x, weight=w.norm1)
        q_rot, q_pass = project(h, w.q_rot), project(h, w.q_pass)
        k_rot, k_pass = project(h, w.k_rot), project(h, w.k_pass)
        v = project(h, w.v)
        q_rot = RoPE(q_rot.reshape(n * H, A), step.angles)
        k_rot = RoPE(k_rot.reshape(n * G, A), step.angles)
        attended = self.attend(step, i, q_rot, q_pass, k_rot, k_pass, v)
        x = ElementwiseAdd(x, project(attended, w.o))
        h = RMSNorm(x, weight=w.norm2)
        return ElementwiseAdd(x, swiglu(h, w.gate, w.up, w.down))

    def attend(self, step, i, q_rot, q_pass, k_rot, k_pass, v):
        """Write k's rotary and pass-through columns into layer ``i``'s
        cache (the same total bytes one whole-head write always moved,
        now in two transfers), merge q's into its scratch state, and
        attend causally over the cache, as ``CausalLM.attend`` does for a
        whole, unsplit head.
        """
        c = self.config
        H, G, D, A = c.n_heads, c.n_kv_groups, c.head_dim, c.rope_width
        L, C = c.max_seq_len, c.prefill_chunk
        keys, values = self.keys[i], self.values[i]
        n = q_rot.shape[0] // H
        merge = self.q_merge[i]
        if step.prompt:
            kv_shape = keys.reshape(L // C, C, G, D)
            v_shape = values.reshape(L // C, C, G, D)
            Copy(k_rot.reshape(n, G, A), kv_shape[step.chunk, : step.rows, :, :A])
            Copy(k_pass.reshape(n, G, D - A), kv_shape[step.chunk, : step.rows, :, A:])
            Copy(v.reshape(n, G, D), v_shape[step.chunk, : step.rows])
            Copy(q_rot.reshape(n, H, A), merge[: step.rows, :, :A])
            Copy(q_pass.reshape(n, H, D - A), merge[: step.rows, :, A:])
            q = merge[: step.rows]
        else:
            Copy(k_rot.reshape(G, A), keys[step.position, :, :A])
            Copy(k_pass.reshape(G, D - A), keys[step.position, :, A:])
            Copy(v.reshape(G, D), values[step.position])
            Copy(q_rot.reshape(H, A), merge[0, :, :A])
            Copy(q_pass.reshape(H, D - A), merge[0, :, A:])
            q = merge[:1]
        span = np.s_[: step.position + 1]
        o = MHA(
            q,
            keys[span],
            values[span],
            heads_interleaved=True,
            kv_interleaved=True,
        )
        return o.reshape(n, H * D)

    def head(self, x):
        return GEMV(self.embedding, RMSNorm(x, weight=self.norm))


def layout(config: Config) -> Layout:
    """Each weight's place in ``Phi4``, its name in a Hugging Face checkpoint
    and its shape. ``qkv``/``gate_up`` are the checkpoint's own fused
    weights, split by ``_split_fused_weights`` after loading; the output
    head is the embedding, tied.
    """
    c = config
    E, F, V = c.emb_dim, c.hidden_dim, c.vocab_size
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    layer = "model.layers.{i}"
    return {
        "embedding": ("model.embed_tokens.weight", (V, E)),
        "norm": ("model.norm.weight", (E,)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.qkv": (f"{layer}.self_attn.qkv_proj.weight", (Q + 2 * KV, E)),
        "layers.{i}.o": (f"{layer}.self_attn.o_proj.weight", (E, Q)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.gate_up": (f"{layer}.mlp.gate_up_proj.weight", (2 * F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
    }


class Phi4Tokenizer:
    """Phi-4-mini-instruct's tokenizer, Hugging Face's ``tokenizers`` over
    its ``tokenizer.json`` (an auto-converted GPT-4o-style BPE, not a
    tiktoken ``.model`` file: no chat template or added-token handling
    beyond plain encode/decode, enough for a teacher-forced oracle check
    and a raw continuation).
    """

    def __init__(self, path):
        self._tokenizer = Tokenizer.from_file(str(path))

    def encode(self, text: str) -> list[int]:
        return self._tokenizer.encode(text).ids

    def decode(self, tokens) -> str:
        return self._tokenizer.decode(list(tokens))


#: ``<|endoftext|>``, the checkpoint's bos_token, eos_token and pad_token alike.
BOS = 199999


class Runner(lm.Runner):
    """Phi-4-mini-instruct, from its checkpoint (one file, or a sharded
    index) and ``tokenizer.json``.
    """

    config = PHI_4_MINI
    layout = staticmethod(layout)
    model = Phi4
    open_tokenizer = Phi4Tokenizer
    bos = BOS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weights = _split_fused_weights(self.weights, self.config)


if __name__ == "__main__":
    lm.main(Runner, "Phi-4-mini-instruct on the NPU")
