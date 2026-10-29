# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 3 1B on the NPU, from the real checkpoint: speed, accuracy against
the float32 reference, determinism, and past one chunk: a prompt of two and
a chat turn, which crosses a sliding layer's ring (the end of the caches is
``long_context``'s). The model is compiled and loaded once for the module
and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.gemma3 import Gemma3
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("gemma-3-1b-it") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Gemma3, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    loaded = load()
    yield loaded
    loaded.release()


# KL(fp32 CPU || NPU) measured on npu2 (Strix Halo) mean 0.0025, p90 0.0049,
# max 0.0388 over 40 steps after a 1024-character prompt, 2 top-1 mismatches.
MAX_KL = {"Mean": 0.01, "P90": 0.02, "Max": 0.1}


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
    ids=[f"gemma_3_1b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@GENERATION
def test_gemma_3_1b(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_gemma_3_1b_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


@pytest.mark.extensive
def test_gemma_3_1b_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are several chunks and several slides of
# the sliding layers' ring.
LONG = 12000


@pytest.mark.extensive
def test_gemma_3_1b_accuracy_across_chunks(model, record_property):
    """The prompt's chunks and two decode steps after them, against the
    float32 reference over the whole prompt.
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


@pytest.mark.extensive
def test_gemma_3_1b_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the chunks it reaches alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
