# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM3's graph against Hugging Face's SmolLM3 in float32 over the same
random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``) with layer 3 NoPE.
"""

import dataclasses

import pytest

from iron.applications.smollm3.model import SmolLM3, SmolLM3Config
from iron.tests.support.llama_reference import Decoder

#: SmolLM3's proportions at toy size: GQA, its RoPE base, every fourth
#: layer NoPE, a tied head.
TOY = SmolLM3Config(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=1024,
    rope_theta=5000000.0,
    max_seq_len=256,
    prefill_chunk=256,
    no_rope_layers=(1, 1, 1, 0),
)


class TestSmolLM3(Decoder):
    model, config, model_type, name = SmolLM3, TOY, "smollm3", "toy"
    json = {"pad_token_id": None}
    seed = 0


def test_a_no_rope_list_short_of_the_layers_is_refused():
    with pytest.raises(ValueError, match="3 no_rope_layers for 4 layers"):
        dataclasses.replace(TOY, no_rope_layers=(1, 1, 0))
