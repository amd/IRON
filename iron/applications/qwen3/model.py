# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 1.7B on the shared decoder (``iron.lm``), its shape read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen3.model``.

Qwen3 is Llama's layer plus a per-head RMSNorm on q and k before RoPE,
``self_attn.q_norm`` and ``k_norm`` (``Qwen3Layer``). Its output
head is the input embedding, tied; its checkpoint also ships
``lm_head.weight``, byte-identical to ``model.embed_tokens.weight``, which
is never read.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Qwen3 1.7B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone.
"""

from pathlib import Path

from iron import lm
from iron.lm import Attention, CausalLM, DecoderConfig, DecoderLayer


class Qwen3Layer(DecoderLayer):
    """Llama's layer, its attention norming q and k per head."""

    def __init__(self, c: DecoderConfig, i: int):
        super().__init__(c, i, Attention(c, i, norms="qk", o_bias=c.attention_bias))


class Qwen3(CausalLM):
    """The Qwen3 decoder, with the shape ``config`` and the checkpoint's
    ``weights``. ``Qwen3.load`` builds one from a checkpoint and its
    ``tokenizer.json``.
    """

    config = DecoderConfig
    profile = Path(__file__).with_name("profiles")
    layer_class = Qwen3Layer


if __name__ == "__main__":
    lm.main(Qwen3)
