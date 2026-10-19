#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct's graph against Hugging Face's Phi-3 in float32 over
the same random weights, its logits recorded in ``goldens/``, device-free
(no checkpoint, no NPU): its partial rotary and fused qkv_proj and
gate_up_proj, through the shared decoder's caches, independent of whether
the real checkpoint or hardware is at hand.
"""

import dataclasses

import numpy as np

from iron.applications.phi3.model import LongRope, Phi4, Phi4Config
from iron.lm.golden import HuggingFace
from iron.lm.testing import LOGITS, assert_close
from iron.tests.support.llama_model import checkpoint
from iron.tests.common.llama_reference import Decoder

#: Phi-4-mini-instruct's proportions at toy size: GQA, a fused qkv/gate_up,
#: partial rotary (half of each head).
TOY = Phi4Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=64,
    intermediate_size=512,
    rope_theta=10000.0,
    max_seq_len=256,
    partial_rotary_factor=0.5,
    prefill_chunk=256,
)


def _shapes(c: Phi4Config) -> dict[str, tuple[int, ...]]:
    E, F, V = c.hidden_size, c.intermediate_size, c.vocab_size
    Q, KV = c.num_attention_heads * c.head_dim, c.num_key_value_heads * c.head_dim
    out = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(c.num_hidden_layers):
        layer = f"model.layers.{i}"
        out |= {
            f"{layer}.input_layernorm.weight": (E,),
            f"{layer}.self_attn.qkv_proj.weight": (Q + 2 * KV, E),
            f"{layer}.self_attn.o_proj.weight": (E, Q),
            f"{layer}.post_attention_layernorm.weight": (E,),
            f"{layer}.mlp.gate_up_proj.weight": (2 * F, E),
            f"{layer}.mlp.down_proj.weight": (E, F),
        }
    return out


#: LongRoPE at toy size: a 128-position original context, served to 512.
LONG = dataclasses.replace(
    TOY,
    max_seq_len=512,
    prefill_chunk=128,
    original_max_position_embeddings=128,
    longrope=LongRope(
        short_factor=(1.0,) * 16,
        long_factor=tuple(float(f) for f in np.geomspace(1, 32, 16)),
    ),
)


class TestPhi3(Decoder):
    model, config, model_type, name = Phi4, TOY, "phi3", "toy"
    # Hugging Face's default padding token lies past the toy vocabulary.
    json = dict(pad_token_id=None)

    @classmethod
    def names(cls):
        return _shapes(cls.config)

    def test_a_turn_past_the_original_context_rotates_only_its_own_rows(self, golden):
        """Decision 35 on decision 50: a prompt within 128 positions rotates
        short and a first turn passing 128 long throughout, both Hugging
        Face's; a second turn passing 128 runs from its first new token, its
        own rows rotated long, the cached ones as they were written, so it
        differs from a first turn over the same tokens, and a decode step past
        128 then reads the long rows as a turn over it does. Hugging Face's
        logits are a whole forward call's, so no golden judges the second turn.
        """
        weights = checkpoint(LONG, _shapes(LONG)).tree("random")
        reference = golden(
            "long",
            lambda: HuggingFace.build("phi3", LONG, weights, **self.json),
            LONG,
            weights,
        )
        model = self.host(LONG, weights)
        tokens = np.random.default_rng(5).integers(0, LONG.vocab_size, 301)
        assert_close(model.logits(tokens[:100]), reference.logits(tokens[:100]))
        got = np.asarray(model.logits(tokens[:300]), np.float32)
        whole = reference.logits(tokens[:300])
        # Measured 64%: past twice LOGITS, so no rounding passes for it.
        assert np.abs(got - whole).max() > 2 * LOGITS * np.abs(whole).max()
        turned = self.host(LONG, weights)
        turned.logits(tokens[:100])
        assert_close(model.logits(tokens), turned.logits(tokens))
        assert_close(self.host(LONG, weights).logits(tokens), reference.logits(tokens))
