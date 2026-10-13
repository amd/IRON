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
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.applications.qwen3.model import QWEN3_1_7B, Runner, layout
from iron.lm import Checkpoint, load_weights
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


# KL(fp32 CPU || NPU), teacher-forced. TestEachStep's 20-step, 256-char run
# on npu1/Phoenix measured Mean 0.0110, P90 0.0331, Max 0.0553, 2/20 top-1
# mismatches (2026-10-10, commit 7c26849e, tests_latest.csv); these bounds
# give it about 2.5-3x headroom. Not yet measured at the module-scoped
# tests' own 40-step/1024-char shape (full-ELF, npu2 only).
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}


# KL(graph reference || NPU) of one decode step, deep in the cache. Measured
# 0.0039 at position 32767 (max_seq_len - 1, the default config's full
# depth) from a 256-char prompt, one sample (2026-10-10, commit 7c26849e).
# Llama's own bound spans several depths and prompts (0.002 to 0.038); this
# one point doesn't yet characterize Qwen3's spread the way Llama's does,
# so the bound keeps more headroom than the single measurement would need.
DEEP_KL = 0.1


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


def test_qwen3_1_7b_checkpoint_is_its_layout():
    """The real checkpoint's key spelling and shapes are the default
    config's (``lm_head.weight``, tied to the embedding, included), read
    from both shards by their index.
    """
    require(WEIGHTS)
    weights = load_weights(
        Checkpoint(WEIGHTS).tensors, layout(QWEN3_1_7B), QWEN3_1_7B.n_layers
    )
    assert weights.embedding.dtype == bfloat16
    assert len(weights.layers) == QWEN3_1_7B.n_layers
    assert np.array_equal(
        weights.lm_head.view(np.uint16), weights.embedding.view(np.uint16)
    )
