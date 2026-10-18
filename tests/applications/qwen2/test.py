#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2.5 1.5B Instruct on the NPU, from the real checkpoint: speed,
accuracy against the float32 reference, and determinism. The model is
compiled and loaded once for the module and every test calls it in-process.

``--random-weights SEED`` runs it on weights drawn in the checkpoint's
shapes (only its header is read) and random prompts, on a host without the
tokenizer, and ``--max-seq-len`` at another context.

Not yet included: a chat-turn check, as Llama 3.2 1B's test has; the end
of the caches is ``long_context``'s.

The ``model`` fixture packages it ``--each-step``: the full-ELF link does
not finish within an hour.
"""

import pytest

from iron.applications.qwen2 import Qwen2
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    check_device_sampling,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("qwen2.5-1.5b-instruct") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Qwen2, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    """The model, compiled and loaded once, packaged ``--each-step``."""
    yield load(full_elf=False)


# KL(fp32 CPU || NPU) over 40 steps measured mean 0.0058, p90 0.0095, max 0.047.
MAX_KL = {"Mean": 0.015, "P90": 0.025, "Max": 0.1}


GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[
        f"qwen2.5_1.5b_instruct_prompt_{p}_tokens_{n}"
        for p in (1024, 13)
        for n in (40, 1)
    ],
)


@GENERATION
def test_qwen2_5_1_5b_instruct(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


def test_qwen2_5_1_5b_instruct_sampling(model, record_property):
    check_device_sampling(model, 256, 20, record=record_property)


@pytest.mark.bench
def test_qwen2_5_1_5b_instruct_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, 40, 1024, record=record_property)


def test_qwen2_5_1_5b_instruct_determinism(model, record_property):
    check_determinism(model, record=record_property)
