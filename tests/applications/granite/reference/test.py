# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite's graph against Hugging Face's Granite in float32 over the same
random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``) with Granite's four
scalars, none at its default, and an untied head.
"""

from iron.applications.granite.model import Granite, GraniteConfig
from iron.tests.support.llama_model import shapes
from iron.tests.support.llama_reference import Decoder

#: Granite's proportions at toy size, its scalars Granite 3's own but the
#: attention's, which at 1/64 of a 64-wide head would leave the toy's
#: attention near uniform.
TOY = GraniteConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=1024,
    rope_theta=10000.0,
    max_seq_len=256,
    prefill_chunk=256,
    tie_word_embeddings=False,
    attention_multiplier=0.0625,
    residual_multiplier=0.22,
    embedding_multiplier=12.0,
    logits_scaling=8.0,
)


class TestGranite(Decoder):
    model, config, model_type, name = Granite, TOY, "granite", "toy"
    seed = 0

    @classmethod
    def names(cls):
        c = cls.config
        return shapes(c) | {"lm_head.weight": (c.vocab_size, c.hidden_size)}
