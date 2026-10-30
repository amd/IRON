# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's text decoder against Hugging Face's Gemma 4 in float32 over the same random weights.

At a toy shape, its logits recorded in ``goldens/``, device-free: the
shared decoder's tests (``Decoder``) with global layers of their own head
size and proportional RoPE, two shared caches, double-wide MLPs, per-layer
inputs and capped logits.
"""

import dataclasses

import numpy as np
import pytest

from iron.applications.gemma4.model import Gemma4, Gemma4Config
from iron.lm.checkpoint import leaves
from iron.tests.support.llama_reference import Decoder

#: Gemma 4 E2B's proportions at toy size: one KV head, sliding and global
#: layers alternating, the last two sharing caches (a sliding and a
#: global), a window that every prompt and decode step but the first few
#: slides, a tied head and logits capped where the toy's reach.
TOY = Gemma4Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=6,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=512,
    rope_theta=10000.0,
    # A context past three rings of 128, so the sliding layers keep a ring;
    # a chunk of 64 builds for the device only at HIGHEST, as
    # flm.ProjectionGEMM tiles 256 rows.
    max_seq_len=512,
    prefill_chunk=64,
    sliding_window=8,
    layer_types=("sliding_attention", "full_attention") * 3,
    global_head_dim=256,
    num_kv_shared_layers=2,
    use_double_wide_mlp=True,
    ple_dim=128,
    final_logit_softcapping=5.0,
)


class TestGemma4(Decoder):
    model, config, model_type, name = Gemma4, TOY, "gemma4", "toy"
    recorded = dict(prefill_chunk=256)
    json = {
        "text_config": {
            "vocab_size_per_layer_input": TOY.vocab_size,
            "rope_parameters": {
                "sliding_attention": {"rope_type": "default"},
                "full_attention": {"rope_type": "proportional"},
            },
        }
    }

    @classmethod
    def names(cls):
        c = cls.config
        L, E, P, V = c.num_hidden_layers, c.hidden_size, c.ple_dim, c.vocab_size
        H, G = c.num_attention_heads, c.num_key_value_heads
        model = "model.language_model"
        out = {
            f"{model}.embed_tokens.weight": (V, E),
            f"{model}.norm.weight": (E,),
            f"{model}.embed_tokens_per_layer.weight": (V, L * P),
            f"{model}.per_layer_model_projection.weight": (L * P, E),
            f"{model}.per_layer_projection_norm.weight": (P,),
        }
        for i in range(L):
            D = c.global_head_dim if c.full(i) else c.head_dim
            F = c.intermediate_size * (2 if c.owner(i) != i else 1)
            layer = f"{model}.layers.{i}"
            out |= {
                f"{layer}.self_attn.q_proj.weight": (H * D, E),
                f"{layer}.self_attn.o_proj.weight": (E, H * D),
                f"{layer}.self_attn.q_norm.weight": (D,),
                f"{layer}.mlp.gate_proj.weight": (F, E),
                f"{layer}.mlp.up_proj.weight": (F, E),
                f"{layer}.mlp.down_proj.weight": (E, F),
                f"{layer}.per_layer_input_gate.weight": (P, E),
                f"{layer}.per_layer_projection.weight": (E, P),
                f"{layer}.layer_scalar": (1,),
                f"{layer}.self_attn.k_proj.weight": (G * D, E),
                f"{layer}.self_attn.v_proj.weight": (G * D, E),
                f"{layer}.self_attn.k_norm.weight": (D,),
            }
            out |= {
                f"{layer}.{norm}.weight": (E,)
                for norm in (
                    "input_layernorm",
                    "post_attention_layernorm",
                    "pre_feedforward_layernorm",
                    "post_feedforward_layernorm",
                    "post_per_layer_input_norm",
                )
            }
        return out

    @classmethod
    def weights(cls):
        """Return the drawn tree, q's and k's norms each scaled by ``head_dim ** -0.25``.

        Attention is unscaled, so a trained model's norms carry the
        ``head_dim ** -0.5`` that unit norms leave out, and without it
        bf16's rounding of q and k moves the peaked scores by 10 to 30%.
        """
        tree = super().weights()
        for name, weight in leaves(tree):
            if name.endswith(("q_norm.weight", "k_norm.weight")):
                weight[...] = weight.astype(np.float32) * weight.size**-0.25
        return tree


@pytest.mark.parametrize(
    "text",
    [
        {"attention_k_eq_v": True},
        {"enable_moe_block": True},
        {"use_bidirectional_attention": "all"},
        {"use_bidirectional_attention": True},
        {"attn_logit_softcapping": 50.0},
        {"vocab_size_per_layer_input": 512},
        {"rope_parameters": {"full_attention": {"rope_type": "default"}}},
    ],
)
def test_what_is_not_built_is_refused(text):
    data = TOY.to_json()
    data["text_config"] |= text
    with pytest.raises(ValueError, match="not built here"):
        Gemma4Config.from_json(data)


def test_bidirectional_attention_for_images_alone_is_text_s_causal():
    data = TOY.to_json()
    data["text_config"]["use_bidirectional_attention"] = "vision"
    assert Gemma4Config.from_json(data).layer_types == TOY.layer_types


def test_a_shared_layer_with_no_earlier_layer_of_its_kind_is_refused():
    with pytest.raises(ValueError, match="shared layer 0 has no earlier layer"):
        dataclasses.replace(TOY, num_kv_shared_layers=6).owner(0)


def test_a_placeholder_s_per_layer_inputs_are_the_padding_token_s(npu2):
    """Check that each layer's per-layer table holds the padding token's row at the placeholders.

    The image, audio and video placeholders, as transformers'
    ``Gemma4Model`` reads a placeholder as the padding token for the
    per-layer inputs.
    """
    placeholders = dict(image_token_id=1021, audio_token_id=1022, video_token_id=1023)
    config = dataclasses.replace(TOY, **placeholders)
    model = Gemma4(config, TestGemma4.weights())
    for layer in model.layers:
        table = np.asarray(layer.per_layer_embedding)
        for token in placeholders.values():
            np.testing.assert_array_equal(table[token], table[config.pad_token_id])
        assert not np.array_equal(table[1020], table[config.pad_token_id])
