#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, the device loop, and past one
chunk: a prompt of two and a chat turn (the end of the caches is
``long_context``'s). The model is compiled and loaded once for the module
and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.granite import Granite
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_device_sampling,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("granite-4.2-3b") / "model.safetensors.index.json"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Granite, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    """The model, compiled and loaded once as a full ELF: the arena's banks
    keep its ~10 GB of weights and caches within aiebu's 32-bit relocation
    addend.
    """
    loaded = load()
    assert loaded.device_loop
    yield loaded


# KL(fp32 CPU || NPU) over 40 steps measured mean 0.0031, p90 0.0062, max 0.0152.
MAX_KL = {"Mean": 0.01, "P90": 0.02, "Max": 0.05}


@pytest.mark.supported_devices("npu2")
class TestEachStep:
    """Every step its own xclbin dispatch, the host starting each on the
    token the last one drew. Its model is built and dropped with the class,
    first: after any other test it would be held beside the module's
    full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, load):
        model = load(full_elf=False)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    def test_granite_4_2_3b_each_step_accuracy(self, model, record_property):
        check_accuracy(model, MAX_KL, 20, 512, record=record_property)

    def test_granite_4_2_3b_each_step_determinism(self, model, record_property):
        check_determinism(model, 4, 3, 128, record=record_property)


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"granite_4_2_3b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_granite_4_2_3b(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


# The device draws every token and starts every decode step itself; from the
# same seed its text is the host loop's. The figures are the device loop's.
@pytest.mark.bench
def test_granite_4_2_3b_device_loop(model, record_property):
    check_device_sampling(model, 1024, 100, record=record_property)


@pytest.mark.bench
def test_granite_4_2_3b_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


def test_granite_4_2_3b_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are a full chunk and most of a second for
# Granite's tokenizer too: it attends over the first's caches.
LONG = 12000


def test_granite_4_2_3b_accuracy_across_chunks(model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over the
    chunks on the host, so only a few).
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


def test_granite_4_2_3b_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
