#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 1.7B on the shared decoder (``iron.lm``), its shape read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen3.model``.

Qwen3 is Llama's layer plus a per-head RMSNorm on q and k before RoPE,
``self_attn.q_norm`` and ``k_norm`` (``Qwen3Config.attention``). Its output
head is the input embedding, tied; its checkpoint also ships
``lm_head.weight``, byte-identical to ``model.embed_tokens.weight``, which
is never read.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen3 1.7B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone.
"""

import dataclasses
from pathlib import Path

from iron import lm
from iron.lm import AttentionSpec, CausalLM, DecoderConfig


@dataclasses.dataclass(frozen=True)
class Qwen3Config(DecoderConfig):
    """``DecoderConfig``, its attention norming q and k per head."""

    def attention(self, i: int) -> AttentionSpec:
        return dataclasses.replace(super().attention(i), qk_norm=True)


class Qwen3(CausalLM):
    """Qwen3 on ``config``'s shape and a checkpoint's ``weights``, from its
    checkpoint and ``tokenizer.json``.

    Qwen3's ``tokenizer_config.json`` names no ``bos_token``; its
    ``generation_config.json`` names ``<|endoftext|>`` (151643) as both
    ``bos_token_id`` and ``pad_token_id``, which is used here as every
    prompt's leading token, as ``lm.Model`` requires one.
    """

    config = Qwen3Config
    profile = Path(__file__).with_name("profiles")
    bos = 151643


if __name__ == "__main__":
    lm.main(Qwen3)
