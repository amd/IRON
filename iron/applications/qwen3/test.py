#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 1.7B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, and past one chunk: a prompt of
two, a chat turn, and a prompt chunk and a step at the end of the caches.
The model is compiled and loaded once for the module and every test calls
it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import dataclasses

import aie.utils as aie_utils
import pytest

import iron
from iron.applications.qwen3.model import Runner
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_deep_decode,
    check_deep_prompt,
    check_determinism,
    check_device_sampling,
    check_generation,
    require,
    weights_dir,
)

WEIGHTS = weights_dir("qwen3-1.7b") / "model.safetensors.index.json"
TOKENIZER = weights_dir("qwen3-1.7b") / "tokenizer.json"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def runner(request):
    config = Runner.config
    max_seq_len = request.config.getoption("--max-seq-len")
    if max_seq_len is not None:
        config = dataclasses.replace(config, max_seq_len=max_seq_len)
    seed = request.config.getoption("--random-weights")
    if seed is not None:
        return Runner(config=config, seed=seed)
    require(WEIGHTS, TOKENIZER)
    return Runner(WEIGHTS, TOKENIZER, config)


@pytest.fixture(scope="module")
def model(runner, request, module_npu_runtime):
    """The model, compiled and loaded once, its versions tuned by
    ``--cost-table`` if given; the runtime is released after the module's
    last test, as ``npu_runtime`` does after each of the others.
    """
    yield runner.npu(request.config.getoption("--cost-table"))


# KL(fp32 CPU || NPU), teacher-forced over 40 steps. Qwen3 is 28 layers
# against Llama 3.2 1B's 16, so bf16 error has more steps to accumulate;
# these bounds are provisional (Llama's own, at Llama's depth, with
# headroom) until measured on real hardware -- see qwen/stats.md.
MAX_KL = {"Mean": 0.04, "P90": 0.08, "Max": 0.4}


# KL(graph reference || NPU) of one decode step, provisional like MAX_KL.
DEEP_KL = 0.2


@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin, and the
    host drawing each token. Its model is built and dropped with the class,
    first: after any other test it would be held beside the module's
    full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, runner):
        model = runner.npu(boundaries=iron.each_step)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    def test_qwen3_1_7b_each_step_accuracy(self, runner, model, record_property):
        check_accuracy(runner, model, MAX_KL, 20, 256, record=record_property)

    def test_qwen3_1_7b_each_step_determinism(self, runner, model, record_property):
        check_determinism(runner, model, 4, 3, 128, record=record_property)

    def test_qwen3_1_7b_each_step_decode_deep_in_the_cache(
        self, runner, model, record_property
    ):
        position = runner.config.max_seq_len - 1
        check_deep_decode(runner, model, position, DEEP_KL, 256, record=record_property)

    def test_qwen3_1_7b_each_step_prompt_deep_in_the_cache(
        self, runner, model, record_property
    ):
        rows = runner.config.prefill_chunk
        check_deep_prompt(runner, model, rows, DEEP_KL, 256, record=record_property)


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"qwen3_1_7b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_qwen3_1_7b(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


# The device draws every token and starts every decode step itself; from the
# same seed its text is the host loop's. The figures are the device loop's.
@pytest.mark.bench
def test_qwen3_1_7b_device_loop(runner, model, record_property):
    check_device_sampling(runner, model, 1024, 100, record=record_property)


def test_qwen3_1_7b_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, record=record_property)


def test_qwen3_1_7b_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)


# 12000 characters of prompt.txt are 3262 tokens (confirmed against Qwen3's
# own tokenizer): a full chunk and most of a second, which attends over the
# first's caches.
LONG = 12000


def test_qwen3_1_7b_accuracy_across_chunks(runner, model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k+
    tokens on the host, so only a few).
    """
    assert len(runner.prompt(LONG)) > runner.config.prefill_chunk
    check_accuracy(runner, model, MAX_KL, 3, LONG, record=record_property)


def test_qwen3_1_7b_chat_turn(runner, model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(runner, model, LONG, 1000, record=record_property)


def test_qwen3_1_7b_decode_deep_in_the_cache(runner, model, record_property):
    """The deepest step the caches hold, at ``max_seq_len - 1``."""
    position = runner.config.max_seq_len - 1
    check_deep_decode(runner, model, position, DEEP_KL, record=record_property)


def test_qwen3_1_7b_prompt_deep_in_the_cache(runner, model, record_property):
    """The last chunk the caches hold, whole: the longest dispatch a prompt
    makes, over the whole context.
    """
    rows = runner.config.prefill_chunk
    check_deep_prompt(runner, model, rows, DEEP_KL, record=record_property)
