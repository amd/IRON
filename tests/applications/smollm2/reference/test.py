# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM2's graph against Hugging Face's Llama in float32 over the same
random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``).
"""

from iron.applications.llama.model import LlamaConfig
from iron.applications.smollm2.model import SmolLM2
from iron.tests.support.llama_reference import Decoder

#: SmolLM2's proportions at toy size: full multi-head attention, its RoPE
#: base, a tied head.
TOY = LlamaConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=2,
    num_attention_heads=8,
    num_key_value_heads=8,
    intermediate_size=1024,
    rope_theta=130000.0,
    max_seq_len=256,
    prefill_chunk=256,
)


class TestSmolLM2(Decoder):
    model, config, model_type, name = SmolLM2, TOY, "llama", "toy"
