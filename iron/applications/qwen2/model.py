#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2.5 over the shared decoder and layer (``iron.lm``): its head on
the NPU (``Qwen2``) and on the CPU in float32 (``Qwen2Oracle``, the
reference it is judged by), its tokenizer, and Qwen 2.5 1.5B Instruct's
shape, read from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen2.model``.

Qwen 2 is Llama's layer with a bias on each of its q, k and v projections,
which ``Layer`` reads from the checkpoint and adds across every row
(``project(..., bias=)``). It ties its embedding and output head, as Llama
does, and takes no RoPE frequency scaling.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen 2.5 1.5B Instruct's shape: a decode step's
and a 2048-row prompt chunk's, at any ``max_seq_len``, which sizes the
caches and the RoPE table alone.
"""

from pathlib import Path

from tokenizers import Tokenizer

from iron import lm
from iron.lm import CausalLM, DecoderConfig, Oracle, widen
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm


class Qwen2Oracle(Oracle):
    """Qwen 2.5's forward pass in float32, on the host."""

    def head(self, x):
        norm = widen(self.weights.model.norm.weight)
        return self.rms_norm(x, norm) @ self.embedding.T


class Qwen2(CausalLM):
    """Qwen 2.5 on ``config``'s shape and a checkpoint's ``weights``, by its
    names. The embedding is the output head too. Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Qwen2Oracle

    def head(self, x):
        return GEMV.step(
            self.weights.model.embed_tokens.weight,
            RMSNorm.step(
                x, weight=self.weights.model.norm.weight, epsilon=self.config.eps
            ),
        )


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

    config = DecoderConfig
    model = Qwen2
    open_tokenizer = staticmethod(tokenizer)
    # "<|endoftext|>": every prompt's lead token, as Qwen 2.5's own generation
    # config gives it; it carries no chat template of its own.
    bos = 151643


if __name__ == "__main__":
    lm.main(Runner, "Qwen 2.5 1.5B Instruct on the NPU")
