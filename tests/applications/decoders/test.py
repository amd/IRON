#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each decoder below on the NPU, from its real checkpoint: speed, accuracy
against the float32 reference and determinism. Each model is compiled and
loaded once, and every test of it calls it in-process.

``--random-weights SEED`` runs them on weights drawn in each checkpoint's
shapes and random prompts, on a host without the tokenizer, and
``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.gemma3 import Gemma3
from iron.applications.gemma4 import Gemma4
from iron.applications.qwen3_moe import Qwen3Moe
from iron.applications.smollm3 import SmolLM3
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

INDEX = "model.safetensors.index.json"

# Each decoder's class, checkpoint file and long prompt's length.
DECODERS = [
    pytest.param((Gemma3, "gemma-3-1b-it/model.safetensors", 256), id="gemma3"),
    pytest.param((Gemma4, "gemma-4-e2b-it/model.safetensors", 256), id="gemma4"),
    pytest.param((SmolLM3, f"smollm3-3b/{INDEX}", 1024), id="smollm3"),
    pytest.param(
        (Qwen3Moe, f"qwen3-30b-a3b/{INDEX}", 1024),
        id="qwen3_moe",
        marks=pytest.mark.skip(
            reason="Experts streams every expert a row: too slow to generate"
        ),
    ),
]

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module", params=DECODERS)
def decoder(request):
    """A decoder, compiled and loaded once, and its long prompt's length."""
    cls, weights, long = request.param
    return load_from_flags(request, cls, weights_dir(weights), staged=False)(), long


# Unmeasured on the NPU: Qwen3's bounds until their first run.
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}


@pytest.mark.bench
@pytest.mark.parametrize(
    "prompt_len,num_tokens", [(None, 40), (13, 1)], ids=["long-40", "13-1"]
)
def test_generation(decoder, prompt_len, num_tokens, record_property):
    model, long = decoder
    check_generation(model, prompt_len or long, num_tokens, record=record_property)


@pytest.mark.bench
def test_accuracy(decoder, record_property):
    check_accuracy(decoder[0], MAX_KL, record=record_property)


def test_determinism(decoder, record_property):
    check_determinism(decoder[0], record=record_property)
