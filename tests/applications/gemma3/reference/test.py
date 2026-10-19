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
import pytest

from iron.applications.gemma3.model import Gemma3, Gemma3Config
from iron.lm.checkpoint import leaves
from iron.lm.testing import assert_close
from iron.tests.support.llama_model import shapes
from iron.tests.support.llama_reference import Decoder

#: Gemma 3's proportions at toy size: one KV head, an attention scale other
#: than head_dim's, sliding and global layers, a window that every prompt
#: and decode step but the first few slides, a tied head.
TOY = Gemma3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=4,
    num_key_value_heads=1,
    head_dim=128,
    intermediate_size=1024,
    rope_theta=1000000.0,
    # A context past three rings of 128, so the sliding layers keep a ring;
    # a chunk of 64 builds for the device only at HIGHEST, as
    # flm.ProjectionGEMM tiles 256 rows.
    max_seq_len=512,
    prefill_chunk=64,
    sliding_window=8,
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

    def test_an_edit_past_the_ring_reruns_from_the_first_position(self, cpu):
        """Tokens changed from position 70 after 200 ran: the sliding
        layers' ring (128 positions) no longer holds the window before the
        chunk at 64, so the call reruns from 0.
        """
        config = cpu.config
        model = self.host(config, cpu.weights)
        tokens = np.random.default_rng(5).integers(0, config.vocab_size, 200)
        model.logits(tokens)
        assert model.session.resume(70) == 0
        edit = np.random.default_rng(6).integers(0, config.vocab_size, 130)
        tokens = np.concatenate([tokens[:70], edit])
        assert_close(model.logits(tokens), cpu.golden.logits(tokens))


def test_a_transformers_5_config_gives_both_rope_bases():
    data = TOY.to_json()
    del data["rope_theta"]
    data["rope_parameters"] = {
        "sliding_attention": {"rope_type": "default", "rope_theta": 10000.0},
        "full_attention": {"rope_type": "default", "rope_theta": 1000000.0},
    }
    config = Gemma3Config.from_json(data)
    assert (config.rope_theta, config.rope_local_base_freq) == (1000000.0, 10000.0)


@pytest.mark.parametrize(
    "key, value",
    [
        ("final_logit_softcapping", 30.0),
        ("attn_logit_softcapping", 50.0),
        ("use_bidirectional_attention", True),
    ],
)
def test_what_is_not_built_is_refused(key, value):
    with pytest.raises(ValueError, match=key):
        Gemma3Config.from_json(TOY.to_json() | {key: value})


def test_without_layer_types_every_sixth_layer_is_global():
    config = dataclasses.replace(TOY, num_hidden_layers=24, layer_types=None)
    full = [i for i, kind in enumerate(config.layer_types) if kind == "full_attention"]
    assert full == [5, 11, 17, 23]
