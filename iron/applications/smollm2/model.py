#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM2 1.7B Instruct over the shared decoder and layer (``iron.lm``):
Llama 3's architecture (``iron.applications.llama``'s model and oracle) at
its own shape, read from its checkpoint's ``config.json``: full multi-head
attention (a KV group of one head), 24 layers, an unscaled RoPE base of
130000 and a tied head. What is its own is its tokenizer and its tunables.
Run it with ``python -m iron.applications.smollm2.model``.
"""

from pathlib import Path

from tokenizers import Tokenizer as HFTokenizer

from iron import lm
from iron.applications.llama.model import Llama, LlamaConfig


class SmolLM2(Llama):
    """Llama 3 at SmolLM2's shape, with SmolLM2's tunables."""

    profile = Path(__file__).with_name("profiles")


class Tokenizer:
    """SmolLM2's BPE tokenizer (its ``tokenizer.json``), whose
    post-processor adds no special tokens.
    """

    def __init__(self, hf: HFTokenizer):
        self.hf = hf

    def encode(self, text: str) -> list[int]:
        return self.hf.encode(text).ids

    def decode(self, tokens: list[int]) -> str:
        return self.hf.decode(tokens)


def tokenizer(path) -> Tokenizer:
    """SmolLM2's tokenizer, from its ``tokenizer.json``."""
    return Tokenizer(HFTokenizer.from_file(str(path)))


class Runner(lm.Runner):
    """SmolLM2 1.7B Instruct, from its checkpoint and ``tokenizer.json``."""

    config = LlamaConfig
    model = SmolLM2
    open_tokenizer = staticmethod(tokenizer)
    # "<|im_start|>", the ChatML turn marker every prompt starts with.
    bos = 1


if __name__ == "__main__":
    lm.main(Runner, "SmolLM2 1.7B Instruct on the NPU")
