#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, and past one chunk: a prompt of
two, a chat turn, and a prompt chunk and a step at the end of the caches.
The model is compiled and loaded once for the module and every test calls
it in-process.

Granite's decode step does not fit a full ELF at its scale (see
``model.py``'s docstring), so it always runs ``--each-step``: there is no
full-ELF alternative to test, and no device loop.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import dataclasses

import pytest

import iron
from iron.applications.granite.model import Runner
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_deep_decode,
    check_deep_prompt,
    check_determinism,
    check_generation,
    require,
    weights_dir,
)

DIRECTORY = weights_dir("granite-4.2-3b")
WEIGHTS = DIRECTORY / "model.safetensors.index.json"
TOKENIZER = DIRECTORY / "tokenizer.json"

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
    """The model, compiled and loaded once with ``--each-step`` (the only
    packaging Granite's scale fits), its versions tuned by ``--cost-table``
    if given; the runtime is released after the module's last test, as
    ``npu_runtime`` does after each of the others.
    """
    loaded = runner.npu(
        request.config.getoption("--cost-table"), boundaries=iron.each_step
    )
    assert not loaded.device_loop
    yield loaded


# KL(fp32 CPU || NPU), teacher-forced over 40 steps from a 1024-character
# prompt. The graphs measure a mean of 0.0031 and a p90 of 0.0061; a
# separate 20-step, 512-character run measured a mean of 0.0039 and a p90
# of 0.0087. The largest step measured is 0.0152. 40 layers accumulate more
# bf16 error than Llama 3.2 1B's 16, so the bounds carry more headroom over
# the measured values than Llama's test does.
MAX_KL = {"Mean": 0.01, "P90": 0.02, "Max": 0.05}


# KL(graph reference || NPU) of one decode step and one prompt chunk, deep
# in the caches (max_seq_len - 1 and the last chunk). The graph's own
# reference is O(context^2); at the real max_seq_len (32768) it did not
# finish in 13 minutes on this host, so the measurement below is at
# --max-seq-len 4096 instead (position 4095, 1/8 the real depth): decode
# measured 0.0033, the prompt chunk 2.3e-6, both far under Llama's own
# bound. Llama's own DEEP_KL grows noticeably with depth (0.002 to 0.015
# near the prompt, 0.030 to 0.038 at its full 32768), so this bound keeps
# Llama's full headroom rather than tightening it to the shallower number
# actually measured here; the true value at 32768 is unmeasured.
DEEP_KL = 0.1


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"granite_4_2_3b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_granite_4_2_3b(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


def test_granite_4_2_3b_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, record=record_property)


def test_granite_4_2_3b_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)


# 12000 characters of prompt.txt are a full chunk and most of a second for
# Granite's tokenizer too: it attends over the first's caches.
LONG = 12000


def test_granite_4_2_3b_accuracy_across_chunks(runner, model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over the
    chunks on the host, so only a few).
    """
    assert len(runner.prompt(LONG)) > runner.config.prefill_chunk
    check_accuracy(runner, model, MAX_KL, 3, LONG, record=record_property)


def test_granite_4_2_3b_chat_turn(runner, model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(runner, model, LONG, 1000, record=record_property)


def test_granite_4_2_3b_decode_deep_in_the_cache(runner, model, record_property):
    """The deepest step the caches hold, at ``max_seq_len - 1``."""
    position = runner.config.max_seq_len - 1
    check_deep_decode(runner, model, position, DEEP_KL, record=record_property)


def test_granite_4_2_3b_prompt_deep_in_the_cache(runner, model, record_property):
    """The last chunk the caches hold."""
    rows = runner.config.prefill_chunk
    check_deep_prompt(runner, model, rows, DEEP_KL, record=record_property)
