#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2.5 1.5B Instruct on the shared decoder (``iron.lm``), its shape read
from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen2.model``.

Qwen 2 is Llama's layer with a bias on each of its q, k and v projections
(``Qwen2Layer``). It ties its embedding and output head, as Llama does, and
takes no RoPE frequency scaling.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen 2.5 1.5B Instruct's shape: a decode step's
and a 2048-row prompt chunk's, at any ``max_seq_len``, which sizes the
caches and the RoPE table alone.
"""

from pathlib import Path

from iron import lm
from iron.lm import Attention, CausalLM, DecoderConfig, DecoderLayer


class Qwen2Layer(DecoderLayer):
    """Llama's layer, its q, k and v projections each with a bias."""

    def __init__(self, c: DecoderConfig, i: int):
        super().__init__(c, i)
        self.self_attn = Attention(c, i, bias=True)


class Qwen2(CausalLM):
    """Qwen 2.5 on ``config``'s shape and a checkpoint's ``weights``, from
    its checkpoint and ``tokenizer.json``.
    """

    config = DecoderConfig
    profile = Path(__file__).with_name("profiles")
    layer_class = Qwen2Layer


if __name__ == "__main__":
    lm.main(Qwen2)
