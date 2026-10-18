#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-MoE's graph against Hugging Face's Qwen3MoE in float32 over the
same random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``). The checkpoint names
each expert's projections, which transformers stacks as it loads them
(``HuggingFace.converted``).
"""

import pytest

from iron.applications.qwen3_moe.model import Qwen3Moe, Qwen3MoeConfig
from iron.lm.golden import HuggingFace
from iron.tests.common.llama_model import shapes
from iron.tests.common.llama_reference import Decoder

#: Qwen3-MoE's proportions at toy size: GQA, q and k normed, eight experts
#: of which a token takes two, an untied head.
TOY = Qwen3MoeConfig(
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
    num_experts=8,
    num_experts_per_tok=2,
    moe_intermediate_size=256,
)


@pytest.fixture(scope="module")
def golden(golden):
    def recorded(name, reference, config, weights):
        def build():
            return HuggingFace.converted("qwen3_moe", config, weights)

        return golden(name, build, config, weights)

    return recorded


class TestQwen3Moe(Decoder):
    model, config, model_type, name = Qwen3Moe, TOY, "qwen3_moe", "toy"
    # One whose bf16 router picks the experts float32 does at every step.
    seed = 0

    @classmethod
    def names(cls):
        c = cls.config
        out = shapes(c)
        out["lm_head.weight"] = (c.vocab_size, c.hidden_size)
        E, M = c.hidden_size, c.moe_intermediate_size
        for i in range(c.num_hidden_layers):
            layer = f"model.layers.{i}"
            out |= {
                f"{layer}.self_attn.q_norm.weight": (c.head_dim,),
                f"{layer}.self_attn.k_norm.weight": (c.head_dim,),
                f"{layer}.mlp.gate.weight": (c.num_experts, E),
            }
            for p in ("gate_proj", "up_proj", "down_proj"):
                del out[f"{layer}.mlp.{p}.weight"]
            for j in range(c.num_experts):
                expert = f"{layer}.mlp.experts.{j}"
                out |= {
                    f"{expert}.gate_proj.weight": (M, E),
                    f"{expert}.up_proj.weight": (M, E),
                    f"{expert}.down_proj.weight": (E, M),
                }
        return out
