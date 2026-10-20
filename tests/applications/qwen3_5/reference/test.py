#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3.5's text decoder against Hugging Face's Qwen3.5 in float32 over
the same random weights at a toy shape, its logits recorded in
``goldens/``, device-free: the shared decoder's tests (``Decoder``), whose
prompts span several of the toy's 64-row chunks, so the Gated DeltaNet
layers' states carry across chunk boundaries and into decode steps.
"""

import dataclasses

import numpy as np
import pytest

from iron.applications.qwen3_5.model import Qwen35, Qwen35Config
from iron.lm import TokenizerJson
from iron.lm.checkpoint import leaves
from iron.lm.testing import require, weights_dir
from iron.tests.support.llama_reference import Decoder

#: Qwen3.5's proportions at toy size: Gated DeltaNet layers of twice as
#: many value heads as key heads, and gated attention layers of one KV head
#: turning a quarter of each head, alternating (Qwen3.5's three to one
#: puts the toy's bf16 error at 3.4% of its logits, transformers' own
#: bf16 at 2.8%); its head tied, as the small checkpoints' are.
TOY = Qwen35Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=10000000.0,
    max_seq_len=256,
    prefill_chunk=64,
    layer_types=("linear_attention", "full_attention") * 2,
    linear_conv_kernel_dim=4,
    linear_key_head_dim=64,
    linear_value_head_dim=64,
    linear_num_key_heads=2,
    linear_num_value_heads=4,
)


class TestQwen35(Decoder):
    model, config, model_type, name = Qwen35, TOY, "qwen3_5", "toy"
    # Seed 7's last greedy step's top two swap in bf16.
    seed = 1
    json = {"text_config": {"rope_parameters": {"rope_type": "default"}}}

    @classmethod
    def names(cls):
        c = cls.config
        E, V, I = c.hidden_size, c.vocab_size, c.intermediate_size
        H, G, D = c.num_attention_heads, c.num_key_value_heads, c.head_dim
        Hv, Dv, C = c.linear_num_value_heads, c.linear_value_head_dim, c.conv_channels
        model = "model.language_model"
        out = {
            f"{model}.embed_tokens.weight": (V, E),
            f"{model}.norm.weight": (E,),
        }
        for i, kind in enumerate(c.layer_types):
            p = f"{model}.layers.{i}"
            out |= {
                f"{p}.input_layernorm.weight": (E,),
                f"{p}.post_attention_layernorm.weight": (E,),
                f"{p}.mlp.gate_proj.weight": (I, E),
                f"{p}.mlp.up_proj.weight": (I, E),
                f"{p}.mlp.down_proj.weight": (E, I),
            }
            if kind == "full_attention":
                a = f"{p}.self_attn"
                out |= {
                    f"{a}.q_proj.weight": (2 * H * D, E),
                    f"{a}.k_proj.weight": (G * D, E),
                    f"{a}.v_proj.weight": (G * D, E),
                    f"{a}.o_proj.weight": (E, H * D),
                    f"{a}.q_norm.weight": (D,),
                    f"{a}.k_norm.weight": (D,),
                }
            else:
                a = f"{p}.linear_attn"
                out |= {
                    f"{a}.in_proj_qkv.weight": (C, E),
                    f"{a}.in_proj_z.weight": (Hv * Dv, E),
                    f"{a}.in_proj_b.weight": (Hv, E),
                    f"{a}.in_proj_a.weight": (Hv, E),
                    f"{a}.conv1d.weight": (C, 1, c.linear_conv_kernel_dim),
                    f"{a}.dt_bias": (Hv,),
                    f"{a}.A_log": (Hv,),
                    f"{a}.norm.weight": (Dv,),
                    f"{a}.out_proj.weight": (E, Hv * Dv),
                }
        return out

    @classmethod
    def weights(cls):
        """The drawn tree, each norm that scales by ``1 + weight`` drawn
        about zero, and the time steps and decays as the Gated DeltaNet
        initializes them, so a state lasts many positions.
        """
        tree = super().weights()
        rng = np.random.default_rng(0)
        for name, weight in leaves(tree):
            if name.endswith("norm.weight") and "linear_attn" not in name:
                weight[...] = weight.astype(np.float32) - 1
            elif name.endswith("A_log"):
                weight[...] = np.log(rng.uniform(1, 16, weight.size))
            elif name.endswith("dt_bias"):
                dt = np.exp(rng.uniform(np.log(1e-3), np.log(1e-1), weight.size))
                weight[...] = dt + np.log(-np.expm1(-dt))
        return tree


def test_a_quarter_of_each_head_turns():
    assert TOY.rotary_dim == 32


@pytest.mark.parametrize(
    "text",
    [{"attention_bias": True}, {"rope_parameters": {"rope_type": "yarn"}}],
)
def test_what_is_not_built_is_refused(text):
    data = TOY.to_json()
    data["text_config"] |= text
    with pytest.raises(ValueError, match="not built here"):
        Qwen35Config.from_json(data)


def test_a_tied_head_is_read_from_the_root_where_the_text_config_lacks_it():
    data = TOY.to_json()
    del data["text_config"]["tie_word_embeddings"]
    assert not Qwen35Config.from_json(
        data | {"tie_word_embeddings": False}
    ).tie_word_embeddings


def test_layer_types_other_than_its_two_are_refused():
    with pytest.raises(ValueError, match="layer_types"):
        dataclasses.replace(TOY, layer_types=("attention",) * 4)


def test_a_config_reads_back_from_its_json():
    assert Qwen35Config.from_json(TOY.to_json()).to_json() == TOY.to_json()


def test_the_bos_and_eos_named_are_the_checkpoint_s_end_tokens():
    """The checkpoint names neither; the ids are its tokenizer's."""
    path = weights_dir("qwen3.5-0.8b") / "tokenizer.json"
    require(path, staged=False)
    tokenizer = TokenizerJson(path)
    assert tokenizer.encode("<|endoftext|>") == [Qwen35.bos]
    ends = tokenizer.encode("<|endoftext|><|im_end|>")
    assert Qwen35.eos == set(ends)
