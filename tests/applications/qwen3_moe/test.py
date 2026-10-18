#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-30B-A3B on the NPU, from the real checkpoint: speed, accuracy against the
float32 reference and determinism. The model is compiled and loaded once
for the module and every test calls it in-process.

``--random-weights SEED`` runs it on weights drawn in the checkpoint's
shapes and random prompts, on a host without the tokenizer, and
``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.qwen3_moe import Qwen3Moe
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("qwen3-30b-a3b") / "model.safetensors.index.json"

pytestmark = [
    pytest.mark.supported_devices("npu2"),
    pytest.mark.skip(reason="Experts has no kernel yet"),
]


@pytest.fixture(scope="module")
def model(request):
    """The model, compiled and loaded once."""
    return load_from_flags(request, Qwen3Moe, WEIGHTS, staged=False)()


# Unmeasured on the NPU: Qwen3's bounds until its first run.
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}


@pytest.mark.bench
@pytest.mark.parametrize("prompt_len,num_tokens", [(1024, 40), (13, 1)])
def test_generation(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.bench
def test_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


def test_determinism(model, record_property):
    check_determinism(model, record=record_property)
