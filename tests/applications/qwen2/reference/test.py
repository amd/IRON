#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2.5's graph against Hugging Face's Qwen2 in float32 over the same
random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``) with a bias on each
of q, k and v.
"""

from iron.applications.qwen2.model import Qwen2, Qwen2Config
from iron.tests.support.llama_model import shapes
from iron.tests.support.llama_reference import Decoder

#: Qwen 2.5's proportions at toy size: GQA, a tied head.
TOY = Qwen2Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
)


class TestQwen2(Decoder):
    model, config, model_type, name = Qwen2, TOY, "qwen2", "toy"

    @classmethod
    def names(cls):
        c = cls.config
        Q, KV = c.num_attention_heads * c.head_dim, c.num_key_value_heads * c.head_dim
        out = shapes(c)
        for i in range(c.num_hidden_layers):
            attention = f"model.layers.{i}.self_attn"
            out |= {
                f"{attention}.q_proj.bias": (Q,),
                f"{attention}.k_proj.bias": (KV,),
                f"{attention}.v_proj.bias": (KV,),
            }
        return out
