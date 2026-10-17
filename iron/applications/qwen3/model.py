#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 over the shared decoder and layer (``iron.lm``): its head on the
NPU (``Qwen3``) and on the CPU in float32 (``Qwen3Oracle``, the reference it
is judged by), its tokenizer, and Qwen3 1.7B's shape, read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen3.model``.

Qwen3 is Llama's layer plus a per-head RMSNorm on q and k before RoPE,
which ``Layer`` reads from ``self_attn.q_norm`` and ``k_norm``. Its output
head is the input embedding, tied; its checkpoint also ships
``lm_head.weight``, byte-identical to ``model.embed_tokens.weight``, which
``head()`` never reads.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen3 1.7B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone.
"""

from pathlib import Path

from tokenizers import Tokenizer as HFTokenizer

from iron import lm
from iron.lm import CausalLM, DecoderConfig, Oracle, widen
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm


class Qwen3Oracle(Oracle):
    """Qwen3's forward pass in float32, on the host."""

    def head(self, x):
        norm = widen(self.weights.model.norm.weight)
        return self.rms_norm(x, norm) @ self.embedding.T


class Qwen3(CausalLM):
    """Qwen3 on ``config``'s shape and a checkpoint's ``weights``, by its
    names. The embedding is the output head too. Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Qwen3Oracle

    def head(self, x):
        return GEMV.step(
            self.weights.model.embed_tokens.weight,
            RMSNorm.step(
                x, weight=self.weights.model.norm.weight, epsilon=self.config.eps
            ),
        )


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

    config = DecoderConfig
    model = Qwen3
    open_tokenizer = staticmethod(tokenizer)
    bos = 151643


if __name__ == "__main__":
    lm.main(Runner, "Qwen3 1.7B on the NPU")
