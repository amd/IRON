#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B on the NPU, from the real checkpoint: speed, accuracy against
the float32 reference, determinism, and past one chunk: a prompt of two and a
chat turn (the end of the caches is ``long_context``'s). The
model is compiled and loaded once for the module and every test calls it
in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.lfm2 import Lfm2
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("lfm2-1.2b") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Lfm2, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    yield load()


# KL(fp32 CPU || NPU) measured at most mean 0.0057, p90 0.0068, max 0.0071.
MAX_KL = {"Mean": 0.02, "P90": 0.03, "Max": 0.05}


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"lfm2_1_2b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_lfm2_1_2b(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.bench
def test_lfm2_1_2b_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


def test_lfm2_1_2b_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are a full chunk and most of a second,
# which attends (or convolves) over the first's caches.
LONG = 12000


def test_lfm2_1_2b_accuracy_across_chunks(model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k
    tokens on the host, so only a few).
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


def test_lfm2_1_2b_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
