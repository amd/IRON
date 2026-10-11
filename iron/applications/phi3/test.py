#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct on the NPU, from the real checkpoint: speed,
accuracy against the float32 reference, and determinism. The model is
compiled and loaded once for the module and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.

Like Qwen2.5-1.5B-Instruct, the decode step and the prompt chunk compile
much faster packaged ``--each-step`` than as a full ELF at this model's
depth (32 layers); this module's ``model`` fixture requests it explicitly.
"""

import dataclasses

import pytest

import iron
from iron.applications.phi3.model import Runner
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    check_device_sampling,
    require,
    weights_dir,
)

WEIGHTS = weights_dir("phi-4-mini-instruct") / "model.safetensors.index.json"
TOKENIZER = weights_dir("phi-4-mini-instruct") / "tokenizer.json"

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
    (the full-ELF link is impractically slow at this model's depth, the
    same finding Qwen2.5-1.5B-Instruct's own port made); the runtime is
    released after the module's last test.
    """
    yield runner.npu(
        request.config.getoption("--cost-table"), boundaries=iron.each_step
    )


# KL(fp32 CPU || NPU), teacher-forced over 10 steps (not Llama/Qwen2.5's
# own 40: the float32 CPU oracle recomputes the whole forward pass from
# scratch every step, and at this model's scale -- emb_dim 3072, vocab
# 200064, both well past Qwen2.5-1.5B-Instruct's own -- that cost alone
# measured ~30s/step on this host, 40 steps would run well past the NPU
# lock's ~10-minute budget even before any dispatch cost; see stats.md).
# Measured over the first 13 steps before this window was found:
# KL 0.00039-0.02240, 13/13 top-1 -- comparable to or better than every
# other model's own bound tonight.
MAX_KL = {"Mean": 0.015, "P90": 0.025, "Max": 0.1}


GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[
        f"phi_4_mini_instruct_prompt_{p}_tokens_{n}"
        for p in (1024, 13)
        for n in (40, 1)
    ],
)


@GENERATION
def test_phi_4_mini_instruct(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


@pytest.mark.xfail(
    strict=False,
    reason="model.generate()'s on-device loop needs a full-ELF decode step; "
    "this model's decode step is each-step/xclbin (the full-ELF link is "
    "impractically slow at this depth, see the module docstring) -- a "
    "pre-existing CausalLM.generate() constraint, not specific to this model.",
)
def test_phi_4_mini_instruct_sampling(runner, model, record_property):
    check_device_sampling(runner, model, 256, 20, record=record_property)


def test_phi_4_mini_instruct_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, 10, 1024, record=record_property)


def test_phi_4_mini_instruct_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)
