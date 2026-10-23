# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-MoE at a toy shape, and its checkpoint's tensors, for its reference
and device tests.
"""

from iron.applications.qwen3_moe.model import Qwen3MoeConfig

from .llama_model import shapes

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
    norm_topk_prob=True,
)


def names(c: Qwen3MoeConfig) -> dict[str, tuple[int, ...]]:
    """Qwen3-MoE's tensors: Llama's, q and k normed, each layer's MLP its
    router and experts, and an untied head.
    """
    out = shapes(c)
    out["lm_head.weight"] = (c.vocab_size, c.hidden_size)
    E, M, D = c.hidden_size, c.moe_intermediate_size, c.head_dim
    assert D is not None, "DecoderConfig derives head_dim"
    for i in range(c.num_hidden_layers):
        layer = f"model.layers.{i}"
        out |= {
            f"{layer}.self_attn.q_norm.weight": (D,),
            f"{layer}.self_attn.k_norm.weight": (D,),
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
