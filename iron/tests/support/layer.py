# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A layer module's parts, by their Hugging Face names."""


def shapes(E, H, G, D, F) -> dict[str, tuple[int, ...]]:
    """Each part of a layer module of that shape, by its Hugging Face name."""
    return {
        "input_layernorm": (E,),
        "post_attention_layernorm": (E,),
        "pre_feedforward_layernorm": (E,),
        "post_feedforward_layernorm": (E,),
        "self_attn.q_proj": (H * D, E),
        "self_attn.k_proj": (G * D, E),
        "self_attn.v_proj": (G * D, E),
        "self_attn.o_proj": (E, H * D),
        "self_attn.q_norm": (D,),
        "self_attn.k_norm": (D,),
        "mlp.gate_proj": (F, E),
        "mlp.up_proj": (F, E),
        "mlp.down_proj": (E, F),
        "self_attn_layer_norm": (E,),
        "self_attn.out_proj": (E, H * D),
        "encoder_attn_layer_norm": (E,),
        "encoder_attn.q_proj": (H * D, E),
        "encoder_attn.k_proj": (G * D, E),
        "encoder_attn.v_proj": (G * D, E),
        "encoder_attn.out_proj": (E, H * D),
        "final_layer_norm": (E,),
        "fc1": (F, E),
        "fc2": (E, F),
    }
