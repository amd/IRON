#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3's graph against Hugging Face's Qwen3 in float32 over the same
random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``) with q and k normed
per head.
"""

from iron.applications.qwen3.model import Qwen3, Qwen3Config
from iron.tests.common.llama_model import shapes
from iron.tests.common.llama_reference import Decoder

#: Qwen3's proportions at toy size: GQA, a head_dim of its own, a tied head.
TOY = Qwen3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
)


class TestQwen3(Decoder):
    model, config, model_type, name = Qwen3, TOY, "qwen3", "toy"
    seed = 3

    @classmethod
    def names(cls):
        c = cls.config
        out = shapes(c)
        for i in range(c.num_hidden_layers):
            attention = f"model.layers.{i}.self_attn"
            out |= {
                f"{attention}.q_norm.weight": (c.head_dim,),
                f"{attention}.k_norm.weight": (c.head_dim,),
            }
        return out
