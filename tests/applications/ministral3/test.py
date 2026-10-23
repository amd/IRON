# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3 3B Base's text decoder on the NPU, from the real checkpoint:
speed, accuracy against the float32 reference at three lengths (one chunk,
two, and past the 16384 positions it was trained at, where YaRN's query
temperature turns on), determinism and a chat turn. The model is compiled
and loaded once for the module and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import numpy as np
import pytest

from iron.applications.ministral3 import Ministral3
from iron.lm.generation import divergence
from iron.lm.testing import (
    assert_close,
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("ministral-3-3b-base-2512") / "model.safetensors.index.json"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Ministral3, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    yield load()


# KL(fp32 CPU || NPU) measured mean 0.0049, p90 0.0071, max 0.093 over 40
# steps; over two chunks and two decode steps mean 0.0040, max 0.0063.
MAX_KL = {"Mean": 0.01, "P90": 0.02, "Max": 0.2}

GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [
        pytest.param(
            p,
            n,
            # The shortest per PR; the rest nightly.
            marks=[
                pytest.mark.bench,
                *([] if (p, n) == (13, 1) else [pytest.mark.extensive]),
            ],
        )
        for p in (1024, 13)
        for n in (40, 1)
    ],
    ids=[f"ministral_3_3b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@GENERATION
def test_ministral_3_3b(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_ministral_3_3b_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


@pytest.mark.extensive
def test_ministral_3_3b_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are 3349 tokens: a full chunk and most of
# a second, which attends over the first's caches.
LONG = 12000


@pytest.mark.extensive
def test_ministral_3_3b_accuracy_across_chunks(model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt.
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


# BOS, then the ids of prompt.txt's text repeated to 17000 tokens: its last
# chunk and the decode step after it run past the 16384 positions YaRN was
# trained at.
DEEP = 17000


@pytest.mark.extensive
def test_ministral_3_3b_accuracy_past_the_trained_context(model, record_property):
    """The prompt's ninth chunk and a decode step after it, each query
    scaled by Llama 4's temperature, against the float32 reference: the
    logits themselves, since repeated text leaves the distributions too
    peaked for KL to tell.
    """
    trained = model.config.rope_scaling.original_max_position_embeddings
    bos, *text = model.prompt(LONG)
    tokens = [bos, *(text * (DEEP // len(text) + 1))[: DEEP - 1]]
    assert len(tokens) > trained
    reference = model.cpu_reference()
    for step in range(2):
        want = reference.logits(tokens)
        got = np.asarray(model.logits(tokens), np.float32).reshape(want.shape)
        kl, _ = divergence(want, got)
        record_property(f"KL{step}", kl)
        record_property(
            f"MaxDiff{step}", float(np.abs(got - want).max() / np.abs(want).max())
        )
        assert_close(got, want)
        tokens.append(int(want.argmax()))


@pytest.mark.extensive
def test_ministral_3_3b_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
