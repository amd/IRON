#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM2 1.7B Instruct over the shared decoder and layer (``iron.lm``):
Llama 3's architecture (``iron.applications.llama``'s model) at
its own shape, read from its checkpoint's ``config.json``: full multi-head
attention (a KV group of one head), 24 layers, an unscaled RoPE base of
130000 and a tied head. What is its own is its tunables.
Run it with ``python -m iron.applications.smollm2.model``.
"""

from pathlib import Path

from iron import lm
from iron.applications.llama.model import Llama


class SmolLM2(Llama):
    """Llama 3 at SmolLM2's shape, with SmolLM2's tunables, from its
    checkpoint and ``tokenizer.json``.
    """

    profile = Path(__file__).with_name("profiles")


if __name__ == "__main__":
    lm.main(SmolLM2)
