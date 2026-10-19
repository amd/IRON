#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 3's graph against Hugging Face's Gemma 3 in float32 over the same
random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``) with sandwich norms,
q and k normed per head and two RoPE bases.
"""

import dataclasses

import numpy as np

from iron.applications.gemma3.model import Gemma3, Gemma3Config
from iron.lm.checkpoint import leaves
from iron.tests.support.llama_model import shapes
from iron.tests.support.llama_reference import Decoder

#: Gemma 3's proportions at toy size: one KV head, an attention scale other
#: than head_dim's, sliding and global layers, a window past every test's
#: context, a tied head.
TOY = Gemma3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    max_seq_len=256,
    prefill_chunk=256,
    sliding_window=1024,
    layer_types=("sliding_attention", "full_attention") * 2,
)


class TestGemma3(Decoder):
    model, config, model_type, name = Gemma3, TOY, "gemma3_text", "toy"

    @classmethod
    def names(cls):
        c = cls.config
        out = shapes(c)
        for i in range(c.num_hidden_layers):
            layer = f"model.layers.{i}"
            out |= {
                f"{layer}.self_attn.q_norm.weight": (c.head_dim,),
                f"{layer}.self_attn.k_norm.weight": (c.head_dim,),
                f"{layer}.pre_feedforward_layernorm.weight": (c.hidden_size,),
                f"{layer}.post_feedforward_layernorm.weight": (c.hidden_size,),
            }
        return out

    @classmethod
    def weights(cls):
        """The drawn tree, each norm's weight about zero: Gemma's norms
        scale by ``1 + weight``.
        """
        tree = super().weights()
        for name, weight in leaves(tree):
            if name.endswith("norm.weight"):
                weight[...] = weight.astype(np.float32) - 1
        return tree


def test_the_context_is_capped_at_the_sliding_window():
    config = dataclasses.replace(TOY, max_seq_len=4096, prefill_chunk=2048)
    assert (config.max_seq_len, config.prefill_chunk, config.window) == (
        1024,
        1024,
        None,
    )
