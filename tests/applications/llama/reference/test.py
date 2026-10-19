#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama's graph with ``attention_bias`` against Hugging Face's Llama in
float32 over the same random weights at a toy shape, its logits recorded in
``goldens/``, device-free: the shared decoder's tests (``Decoder``) with a
bias on each of q, k, v and o, as transformers' Llama biases them.
"""

import dataclasses

from iron.applications.llama.model import Llama
from iron.tests.common.llama_model import SMALL, shapes
from iron.tests.common.llama_reference import Decoder


class TestBiasedLlama(Decoder):
    model, model_type, name = Llama, "llama", "biased"
    config = dataclasses.replace(SMALL, attention_bias=True)
    seed = 1

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
                f"{attention}.o_proj.bias": (c.hidden_size,),
            }
        return out
