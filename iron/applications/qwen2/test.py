#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen 2.5 1.5B Instruct on the NPU, from the real checkpoint: speed,
accuracy against the float32 reference, and determinism. The model is
compiled and loaded once for the module and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.

Not yet included: a deep-cache check (``check_deep_decode``/
``check_deep_prompt``) and a chat-turn check, as Llama 3.2 1B's test has.
Both need a measured KL bound at this model's shape, not borrowed from
Llama's; add them once measured, at a smaller ``--max-seq-len`` if the
real one (32768) is too slow to fill cheaply (the skill's own guidance).

The decode step and the prompt chunk here compile much faster packaged
``--each-step`` than as a full ELF: the full-ELF link did not finish in
about an hour (not a hang, confirmed progressing; see
skill-ports/qwen2.5-1.5b/skill-gaps.md), so this module's ``model`` fixture
requests ``--each-step`` packaging explicitly rather than the default.
"""

import dataclasses

import pytest

import iron
from iron.applications.qwen2.model import Runner
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    check_device_sampling,
    require,
    weights_dir,
)

WEIGHTS = weights_dir("qwen2.5-1.5b-instruct") / "model.safetensors"
TOKENIZER = weights_dir("qwen2.5-1.5b-instruct") / "tokenizer.json"

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
    """The model, compiled and loaded once, packaged ``--each-step``
    (the full-ELF link is impractically slow here, see the module
    docstring); the runtime is released after the module's last test.
    """
    yield runner.npu(
        request.config.getoption("--cost-table"), boundaries=iron.each_step
    )


# KL(fp32 CPU || NPU), teacher-forced over 40 steps, a 1024-character
# prompt: mean 0.00577, p90 0.00946, max 0.04660 (step 13), 3/40 top-1
# mismatches, each at a KL under 0.05 (a near-tie flip, not a broken
# step) -- comparable to or better than Llama 3.2 1B's own measured bound.
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
def test_qwen2_5_1_5b_instruct(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


def test_qwen2_5_1_5b_instruct_sampling(runner, model, record_property):
    check_device_sampling(runner, model, 256, 20, record=record_property)


def test_qwen2_5_1_5b_instruct_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, 40, 1024, record=record_property)


def test_qwen2_5_1_5b_instruct_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)
