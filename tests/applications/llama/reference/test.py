# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama's graph with ``attention_bias`` against Hugging Face's Llama in
float32 over the same random weights at a toy shape, its logits recorded in
``goldens/``, device-free: the shared decoder's tests (``Decoder``) with a
bias on each of q, k, v and o, as transformers' Llama biases them.
"""

import dataclasses

import numpy as np
import pytest

from iron.applications.llama.model import Llama
from iron.lm.golden import RECORD, Golden, HuggingFace
from iron.tests.support.llama_model import SMALL, shapes
from iron.tests.support.llama_reference import Decoder


class TestBiasedLlama(Decoder):
    model, model_type, name = Llama, "llama", "biased"
    config = dataclasses.replace(SMALL, attention_bias=True)
    seed = 1

    @classmethod
    def names(cls):
        c = cls.config
        Q, KV = c.num_attention_heads * c.head_dim, c.num_key_value_heads * c.head_dim
        out = shapes(c)
        for i in range(c.num_hidden_layers):
            attention = f"model.layers.{i}.self_attn"
            out |= {
                f"{attention}.q_proj.bias": (Q,),
                f"{attention}.k_proj.bias": (KV,),
                f"{attention}.v_proj.bias": (KV,),
                f"{attention}.o_proj.bias": (c.hidden_size,),
            }
        return out


def test_a_recorded_row_holds_its_own_logits_alone(tmp_path, monkeypatch):
    """A recorded row owns its bytes: no view keeps its forward's every
    position's logits alive, so recording many rows holds one row each.
    """
    pytest.importorskip("transformers")  # optional: only recording needs it
    monkeypatch.setenv(RECORD, "1")
    config, weights = TestBiasedLlama.config, TestBiasedLlama.weights()
    golden = Golden(
        tmp_path / "golden.npz",
        lambda: HuggingFace.build("llama", config, weights),
        (config, weights),
    )
    row = golden.logits(np.arange(8))
    assert row.shape == (config.vocab_size,) and row.base is None
