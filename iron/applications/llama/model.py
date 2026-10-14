#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 over the shared decoder and block (``iron.lm``): its
head on the NPU (``Llama``) and on the CPU in float32 (``LlamaOracle``,
the reference it is judged by), its tokenizer, and Llama 3.2 1B's shape.
Run it with ``python -m iron.applications.llama.model``.

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
from iron.lm import Block, CausalLM, DecoderConfig, Oracle, widen
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm


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

    @classmethod
    def from_dict(cls, data: dict) -> "Llama3RopeScaling":
        """``data`` as the checkpoint's own ``rope_scaling``, its
        ``rope_type`` (every size's is ``"llama3"``) dropped.
        """
        return cls(**{k: v for k, v in data.items() if k != "rope_type"})


@dataclasses.dataclass(frozen=True)
class LlamaConfig(DecoderConfig):
    """``DecoderConfig`` and Llama 3's own ``rope_scaling``."""

    rope_scaling: Llama3RopeScaling | None = dataclasses.field(
        default=None,
        metadata={"json": "rope_scaling", "convert": Llama3RopeScaling.from_dict},
    )


class LlamaOracle(Oracle):
    """Llama 3's forward pass in float32, on the host; its layer is
    ``Block``'s shape, shared with Granite 4.2 3B, in numpy.
    """

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        a, mlp = w.self_attn, w.mlp
        h = self.rms_norm(x, w.input_layernorm.weight)
        q = self.rotate((h @ a.q_proj.weight.T).reshape(n, H, D), angles)
        k = self.rotate((h @ a.k_proj.weight.T).reshape(n, G, D), angles)
        v = (h @ a.v_proj.weight.T).reshape(n, G, D)
        x = x + self.attend(q, k, v, causal=True) @ a.o_proj.weight.T
        h = self.rms_norm(x, w.post_attention_layernorm.weight)
        F = mlp.gate_proj.weight.shape[0]
        half = np.matmul(h, mlp.gate_proj.weight.T, out=self.buffer("gate", (n, F)))
        half *= np.float32(0.5)
        # SiLU, with the sigmoid as a tanh, which does not overflow.
        silu = np.tanh(half, out=self.buffer("silu", (n, F)))
        silu += 1
        silu *= half
        silu *= np.matmul(h, mlp.up_proj.weight.T, out=self.buffer("up", (n, F)))
        return x + silu @ mlp.down_proj.weight.T

    def head(self, x):
        norm = widen(self.weights.model.norm.weight)
        return self.rms_norm(x, norm) @ self.embedding.T


class Llama(Block, CausalLM):
    """Llama 3 on ``config``'s shape and a checkpoint's ``weights``, by its
    names. The embedding is the output head too. Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = LlamaOracle

    def head(self, x):
        norm = self.weights.model.norm.weight
        return GEMV(self.embedding, RMSNorm(x, weight=norm, epsilon=self.config.eps))


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

    config = LlamaConfig
    model = Llama
    open_tokenizer = staticmethod(tokenizer)
    bos = SPECIAL_TOKENS["<|begin_of_text|>"]


if __name__ == "__main__":
    lm.main(Runner, "Llama 3.2 1B on the NPU")
