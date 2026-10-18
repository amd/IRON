#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3's graph against Hugging Face's Ministral3 in float32 over the
same random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``). The toy was trained
at 64 positions, so YaRN stretches it and a query past 64 is scaled.
"""

import numpy as np

from iron.applications.ministral3.model import (
    Ministral3,
    Ministral3Config,
    YarnRopeScaling,
)
from iron.lm.testing import assert_close
from iron.tests.common.llama_reference import Decoder

#: Ministral 3's proportions at toy size: GQA, a head_dim of its own, YaRN
#: from 64 positions, the query temperature, an untied head.
TOY = Ministral3Config(
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
    eps=1e-5,
    rope_scaling=YarnRopeScaling(factor=4.0, original_max_position_embeddings=64),
    llama_4_scaling_beta=0.1,
)


class TestMinistral3(Decoder):
    model, config, model_type, name = Ministral3, TOY, "ministral3", "toy"
    json = {"pad_token_id": None}
    seed = 0

    @classmethod
    def names(cls):
        c = cls.config
        return super().names() | {"lm_head.weight": (c.vocab_size, c.hidden_size)}

    def test_the_query_scale_steps_up_past_the_trained_context(self, cpu):
        """The last of the toy's 64 trained positions, its query unscaled,
        then a decode step at 64, the first scaled.
        """
        model = self.host(cpu.config, cpu.weights)
        tokens = np.random.default_rng(5).integers(0, cpu.config.vocab_size, 65)
        for n in (64, 65):
            assert_close(model.logits(tokens[:n]), cpu.golden.logits(tokens[:n]))
