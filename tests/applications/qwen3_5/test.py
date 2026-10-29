# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3.5 0.8B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, and past one chunk: a prompt of
two and a chat turn, which carries the Gated DeltaNet layers' states across
a chunk boundary (the end of the caches is ``long_context``'s). The model
is compiled and loaded once for the module and every test calls it
in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.qwen3_5 import Qwen35
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("qwen3.5-0.8b") / "model.safetensors.index.json"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Qwen35, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    loaded = load()
    yield loaded
    loaded.release()


# KL(fp32 CPU || NPU) measured over 40 steps after a 1024-character prompt.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.1}


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
    ids=[f"qwen3_5_0_8b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@GENERATION
def test_qwen3_5_0_8b(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_qwen3_5_0_8b_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


@pytest.mark.extensive
def test_qwen3_5_0_8b_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are several chunks, each holding some of
# the Gated DeltaNet layers' carried state.
LONG = 12000


@pytest.mark.extensive
def test_qwen3_5_0_8b_accuracy_across_chunks(model, record_property):
    """The prompt's chunks and two decode steps after them, against the
    float32 reference over the whole prompt.
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


@pytest.mark.extensive
def test_qwen3_5_0_8b_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the chunks it reaches alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
