#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's text model, E2B and E4B: its shape from the checkpoint's
config.json, and E2B's float32 oracle against Hugging Face's own model
where torch and transformers are installed (hugging_face.py).
"""

import numpy as np
import pytest

from iron.applications.gemma4.model import Gemma4Config, Gemma4Oracle
from iron.lm import Tokenizer
from iron.lm import Checkpoint, rope_angles
from iron.lm.base import prompt_text
from iron.lm.testing import require, weights_dir

DIRECTORY = weights_dir("gemma-4-e2b")
WEIGHTS = DIRECTORY / "model.safetensors"
CONFIG = DIRECTORY / "config.json"
TOKENIZER = DIRECTORY / "tokenizer.json"
E4B = weights_dir("gemma-4-e4b") / "config.json"

# The oracle's logits against Hugging Face's, both float32, summing in other
# orders: 2.8e-5 apart at 7 tokens and 1.4e-4 at 700, of logits up to 29.
MATCH = 1e-3
# The prompt's lengths the oracle is checked at: a few tokens, and past the
# 512-key window.
LENGTHS = (7, 700)


@pytest.fixture(scope="module")
def config():
    require(CONFIG)
    return Gemma4Config.from_checkpoint(CONFIG)


def test_the_config_reads_the_checkpoint_s_layers(config):
    """Every fifth layer global, at its own head size; the last 20 attend
    over the last earlier layer of their kind, 13's or 14's; a sliding
    query reaches 511 keys back, 512 in all.
    """
    assert config.global_layers == tuple(range(4, 35, 5))
    assert config.heads(4) == (1, 512) and config.heads(5) == (1, 256)
    sources = [config.kv_source(i) for i in range(config.num_hidden_layers)]
    assert sources[:15] == list(range(15))
    assert sources[15:] == [14 if i % 5 == 4 else 13 for i in range(15, 35)]
    assert [config.layer(i).shares_kv for i in (14, 15)] == [False, True]
    assert [config.layer(i).window for i in (3, 4)] == [511, None]


def test_e4b_s_config_reads_its_own_layers():
    """Every sixth layer global, two key and value heads at either head
    size; the last 18 attend over layer 22's or 23's.
    """
    require(E4B)
    config = Gemma4Config.from_checkpoint(E4B)
    assert (config.num_hidden_layers, config.hidden_size) == (42, 2560)
    assert config.global_layers == tuple(range(5, 42, 6))
    assert config.heads(5) == (2, 512) and config.heads(4) == (2, 256)
    sources = [config.kv_source(i) for i in range(config.num_hidden_layers)]
    assert sources[:24] == list(range(24))
    assert sources[24:] == [23 if i % 6 == 5 else 22 for i in range(24, 42)]


def test_a_global_layer_turns_a_quarter_of_each_head(config):
    """Proportional RoPE: a global head's first 64 pairs turn at the
    frequencies of a 512-wide head; the rest do not turn.
    """
    angles = config.global_angles()[:100]
    whole = rope_angles(512, 100, config.global_rope_base)
    np.testing.assert_array_equal(angles[:, :128], whole[:, :128])
    np.testing.assert_array_equal(angles[:, 128::2], 1)
    np.testing.assert_array_equal(angles[:, 129::2], 0)


@pytest.fixture(scope="module")
def tokens():
    require(TOKENIZER)
    return [2, *Tokenizer(TOKENIZER).encode(prompt_text(3000))][: max(LENGTHS)]


@pytest.fixture(scope="module")
def hugging_face(tokens):
    """Hugging Face's own Gemma 4 text model's logits after each of
    ``LENGTHS`` of ``tokens``, which the oracle is checked against: optional
    dependencies, so its tests skip without them. The model is dropped
    before the oracle is built.
    """
    for module in ("torch", "transformers"):
        pytest.importorskip(module)
    require(WEIGHTS, CONFIG)
    # Imported here, once the optional dependencies are known to be present.
    from iron.applications.gemma4.hugging_face import HuggingFace

    logits = HuggingFace(DIRECTORY).logits(tokens)
    return {n: logits[n - 1] for n in LENGTHS}


def test_the_oracle_matches_hugging_face(config, tokens, hugging_face):
    """The float32 oracle against Hugging Face's float32 model at a few
    tokens and past the sliding window, where the shared layers and both
    kinds of attention reach.
    """
    oracle = Gemma4Oracle(config, Checkpoint(WEIGHTS).tree())
    for n, expected in hugging_face.items():
        got = oracle.logits(tokens[:n])
        assert got.argmax() == expected.argmax()
        np.testing.assert_allclose(got, expected, rtol=0, atol=MATCH)
