# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3's graph against Hugging Face's Ministral3 in float32 over the
same random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``). The toy was trained
at 64 positions, so YaRN stretches it and a query past 64 is scaled.
"""

import dataclasses
import json
import math

import numpy as np
import pytest

from iron.applications.ministral3.model import (
    Ministral3,
    Ministral3Config,
    YarnRopeScaling,
)
from iron.lm.checkpoint import leaves
from iron.lm.testing import assert_close
from iron.tests.support.llama_model import checkpoint
from iron.tests.support.llama_reference import Decoder

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


def test_yarn_scales_cos_and_sin_by_its_attention_factor_else_by_its_factor():
    assert TOY.rope_attention_scaling == pytest.approx(0.1 * math.log(4) + 1)
    yarn = dataclasses.replace(TOY.rope_scaling, attention_factor=1.5)
    assert dataclasses.replace(TOY, rope_scaling=yarn).rope_attention_scaling == 1.5


def test_a_query_temperature_without_yarn_is_refused():
    with pytest.raises(ValueError, match="there is no YaRN"):
        dataclasses.replace(TOY, rope_scaling=None)


#: Mistral 3's text decoder, as transformers 4 and 5 nest it.
NESTED = {
    "transformers 4": ("language_model.model.", "language_model.lm_head."),
    "transformers 5": ("model.language_model.", "lm_head."),
}


@pytest.mark.parametrize("saved", NESTED)
def test_a_mistral_3_checkpoint_reads_its_text_decoder(saved, npu2):
    model, head = NESTED[saved]
    named = {
        (head + n[8:] if n.startswith("lm_head.") else model + n[6:]): s
        for n, s in TestMinistral3.names().items()
    }
    named["model.vision_tower.patch_conv.weight"] = (8, 3, 4, 4)
    tree = checkpoint(TOY, named).tree("random", 0)
    want = dict(leaves(tree))
    got = Ministral3(TOY, tree)
    assert got.lm_head.weight is want[head + "weight"]
    assert got.model.norm.weight is want[model + "norm.weight"]


def test_an_fp8_checkpoint_is_refused(npu2):
    named = TestMinistral3.names() | {"model.norm.weight_scale_inv": (1,)}
    with pytest.raises(ValueError, match="FP8 checkpoint"):
        Ministral3(TOY, checkpoint(TOY, named).tree("random", 0))


def test_the_config_reads_from_a_mistral_3_text_config(tmp_path):
    text = TOY.to_json()
    (tmp_path / "config.json").write_text(json.dumps(text))
    flat = Ministral3Config.from_checkpoint(tmp_path)
    nested = {"model_type": "mistral3", "text_config": text, "vision_config": {}}
    (tmp_path / "config.json").write_text(json.dumps(nested))
    assert Ministral3Config.from_checkpoint(tmp_path) == flat
