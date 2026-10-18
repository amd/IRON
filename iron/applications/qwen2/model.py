#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2.5 1.5B Instruct on the shared decoder (``iron.lm``), its shape read
from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen2.model``.

Qwen 2 is Llama's layer with a bias on each of its q, k and v projections,
which ``Attention`` adds wherever the checkpoint holds one. It ties its embedding and output
head, as Llama does, and takes no RoPE frequency scaling.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen 2.5 1.5B Instruct's shape: a decode step's
and a 2048-row prompt chunk's, at any ``max_seq_len``, which sizes the
caches and the RoPE table alone.
"""

from pathlib import Path

from iron import lm
from iron.lm import CausalLM, DecoderConfig


class Qwen2(CausalLM):
    """Qwen 2.5 on ``config``'s shape and a checkpoint's ``weights``."""

    profile = Path(__file__).with_name("profiles")


class Runner(lm.Runner):
    """Qwen 2.5 1.5B Instruct, from its checkpoint and ``tokenizer.json``."""

    config = DecoderConfig
    model = Qwen2
    # "<|endoftext|>": every prompt's lead token, as Qwen 2.5's own generation
    # config gives it; it carries no chat template of its own.
    bos = 151643


if __name__ == "__main__":
    lm.main(Runner, "Qwen 2.5 1.5B Instruct on the NPU")
