#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B on the NPU, from the real checkpoint: speed, accuracy against
the float32 reference, determinism, and past one chunk: a prompt of two, a
chat turn, and a prompt chunk and a step at the end of the caches. The
model is compiled and loaded once for the module and every test calls it
in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.lfm2.model import Runner
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

WEIGHTS = weights_dir("lfm2-1.2b") / "model.safetensors"
TOKENIZER = weights_dir("lfm2-1.2b") / "tokenizer.json"
CONFIG = weights_dir("lfm2-1.2b") / "config.json"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def runner(request):
    """``Runner.from_options``, the same way the CLI builds one: the
    options pytest's own ``--random-weights``/``--max-seq-len`` flags
    (``conftest.py``'s, ``Runner.FLAGS``) were given, as option strings.
    """
    seed = request.config.getoption("--random-weights")
    max_seq_len = request.config.getoption("--max-seq-len")
    options = [str(WEIGHTS)]
    if seed is not None:
        require(WEIGHTS, CONFIG)
        options += ["--random-weights", str(seed)]
    else:
        require(WEIGHTS, TOKENIZER, CONFIG)
        options.append(str(TOKENIZER))
    if max_seq_len is not None:
        options += ["--max-seq-len", str(max_seq_len)]
    return Runner.from_options(options)


@pytest.fixture(scope="module")
def model(runner, request):
    yield runner.npu(request.config.getoption("--cost-table"))


# KL(fp32 CPU || NPU), teacher-forced: test_lfm2_1_2b_accuracy measures a
# mean of 0.0013, a P90 of 0.0026 and a max of 0.0032 (40 steps); across two
# chunks (prompt + decode spanning the conv layers' window-cache carry, the
# part of this port least sure of itself) a mean of 0.0057, a P90 of 0.0068
# and a max of 0.0071 -- lower than Llama 3.2 1B's own (a dense model,
# every layer attending, accrues more bf16 error than LFM2's six attention
# layers of sixteen). One run each, so real headroom over the measured max,
# not a tight bound.
MAX_KL = {"Mean": 0.02, "P90": 0.03, "Max": 0.05}

# KL(graph reference || NPU) of one decode step, deep in the context
# (max_seq_len - 1): measured 0.0214 (decode) and 1.4e-6 (a whole prompt
# chunk at the deepest the caches hold), one run each; Llama 3.2 1B's own
# bound (0.1) has comfortable headroom over both and is kept as is rather
# than tightened from a single sample.
DEEP_KL = 0.1


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"lfm2_1_2b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_lfm2_1_2b(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


def test_lfm2_1_2b_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, record=record_property)


def test_lfm2_1_2b_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)


# 12000 characters of prompt.txt are a full chunk and most of a second,
# which attends (or convolves) over the first's caches.
LONG = 12000


def test_lfm2_1_2b_accuracy_across_chunks(runner, model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k
    tokens on the host, so only a few).
    """
    assert len(runner.prompt(LONG)) > runner.config.prefill_chunk
    check_accuracy(runner, model, MAX_KL, 3, LONG, record=record_property)


def test_lfm2_1_2b_chat_turn(runner, model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(runner, model, LONG, 1000, record=record_property)


def test_lfm2_1_2b_decode_deep_in_the_cache(runner, model, record_property):
    """The deepest step the caches hold, at ``max_seq_len - 1``: the conv
    layers' window cache and the attention layers' key/value caches both
    read their oldest-written rows here.
    """
    position = runner.config.max_seq_len - 1
    check_deep_decode(runner, model, position, DEEP_KL, record=record_property)


def test_lfm2_1_2b_prompt_deep_in_the_cache(runner, model, record_property):
    """The last chunk the caches hold, whole: the longest dispatch a prompt
    makes, over the whole context.
    """
    rows = runner.config.prefill_chunk
    check_deep_prompt(runner, model, rows, DEEP_KL, record=record_property)
