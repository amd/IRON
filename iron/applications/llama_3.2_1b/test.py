#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, and past one chunk: a prompt of
two, a chat turn, and a step at the end of the caches. The model is
compiled and loaded once for the module and every test calls it
in-process.
"""

import aie.utils as aie_utils
import pytest

import iron
from iron.lm.llama3.model import Runner
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_deep_decode,
    check_determinism,
    check_device_loop,
    check_generation,
    requires,
    weights_dir,
)

WEIGHTS = weights_dir("llama3.2-1b") / "model.safetensors"
TOKENIZER = weights_dir("llama3.2-1b") / "tokenizer.model"

pytestmark = [requires(WEIGHTS, TOKENIZER), pytest.mark.supported_devices("npu2")]


@pytest.fixture(scope="module")
def runner():
    return Runner(WEIGHTS, TOKENIZER)


@pytest.fixture(scope="module")
def model(runner, request):
    """The model, compiled and loaded once, its decode step tuned by
    ``--cost-table`` if given; the runtime is released after the module's
    last test, as ``npu_runtime`` does after each of the others.
    """
    yield runner.npu(request.config.getoption("--cost-table"))
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


# KL(fp32 CPU || NPU), teacher-forced over 40 steps. The graphs measure a
# mean of 0.0083 and a p90 of 0.018; over 140 positions of prompt.txt the
# p90 is 0.017. The largest step is prefill at 0.091, one of two positions
# of the 140 above 0.05. Decode attention over unmasked KV-cache slots
# measured 9.2.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.2}


# KL(graph reference || NPU) of one decode step, three tokens at each depth:
# 0.002 to 0.015 just past the prompt, 0.009 to 0.033 at 16k and 0.030 to
# 0.038 at 32k: it grows with the keys the step sums over.
DEEP_KL = 0.1


@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin, and the
    host drawing each token. NPU2 feeds a prompt through its prompt version;
    NPU1, without MHA, through the decode step a token at a time, so the
    prompts are shorter than the full ELF's. Its model is built and dropped
    with the class, first: after any other test it would be held beside the
    module's full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, runner):
        model = runner.npu(boundaries=iron.each_step)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    def test_llama_3_2_1b_each_step_accuracy(self, runner, model, record_property):
        check_accuracy(runner, model, MAX_KL, 20, 256, record=record_property)

    def test_llama_3_2_1b_each_step_determinism(self, runner, model, record_property):
        check_determinism(runner, model, 4, 3, 128, record=record_property)

    def test_llama_3_2_1b_each_step_decode_deep_in_the_cache(
        self, runner, model, record_property
    ):
        position = runner.config.max_seq_len - 1
        check_deep_decode(runner, model, position, DEEP_KL, 256, record=record_property)


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"llama_3.2_1b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_llama_3_2_1b(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


# The device draws every token and starts every decode step itself; from the
# same seed its text is the host loop's. The figures are the device loop's.
@pytest.mark.bench
def test_llama_3_2_1b_device_loop(runner, model, record_property):
    check_device_loop(runner, model, 1024, 100, record=record_property)


def test_llama_3_2_1b_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, record=record_property)


def test_llama_3_2_1b_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)


# 12000 characters of prompt.txt are 3262 tokens: a full chunk and most of a
# second, which attends over the first's caches.
LONG = 12000


def test_llama_3_2_1b_accuracy_across_chunks(runner, model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k
    tokens on the host, so only a few).
    """
    assert len(runner.prompt(LONG)) > runner.config.prefill_chunk
    check_accuracy(runner, model, MAX_KL, 3, LONG, record=record_property)


def test_llama_3_2_1b_chat_turn(runner, model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(runner, model, LONG, 1000, record=record_property)


def test_llama_3_2_1b_decode_deep_in_the_cache(runner, model, record_property):
    """The deepest step the caches hold, at ``max_seq_len - 1``."""
    position = runner.config.max_seq_len - 1
    check_deep_decode(runner, model, position, DEEP_KL, record=record_property)
