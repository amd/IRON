#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, and determinism. The model is compiled and
loaded once for the module and every test calls it in-process.
"""

import os
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.llama_3_2_1b.runner import (
    SEED,
    Runner,
    Sampler,
    accuracy,
    determinism,
    generate,
)
from iron.common.harness import record_metric

weights_dir = Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / "llama3.2-1b"

requires_weights = pytest.mark.skipif(
    not os.environ.get("CI")
    and not (
        (weights_dir / "model.safetensors").exists()
        and (weights_dir / "tokenizer.model").exists()
    ),
    reason="llama3.2-1b weights not found outside CI",
)

pytestmark = [requires_weights, pytest.mark.supported_devices("npu2")]


@pytest.fixture(scope="module")
def runner():
    return Runner(weights_dir / "model.safetensors", weights_dir / "tokenizer.model")


@pytest.fixture(scope="module")
def model(runner):
    """The model, loaded once; the runtime is released after the module's
    last test, as ``npu_runtime`` does after each of the others.
    """
    yield runner.npu()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def prompt(runner, chars, num_tokens, skip=0):
    tokens = runner.prompt(chars, skip=skip)
    assert len(tokens) + num_tokens <= runner.config.max_seq_len
    return tokens


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [(p, n) for p in (1024, 13) for n in (40, 1)],
    ids=[f"llama_3.2_1b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_llama_3_2_1b(runner, model, prompt_len, num_tokens):
    tokens = prompt(runner, prompt_len, num_tokens)
    sample = Sampler(0.7, 50, np.random.default_rng(SEED))
    drawn, first, later = generate(model, tokens, num_tokens, sample)
    print(runner.tokenizer.decode(drawn))
    record_metric("TTFT", first)
    if num_tokens > 1:
        record_metric("TPS", 1 / later)


# KL(fp32 CPU || NPU) of the next-token distribution, teacher-forced over 40
# steps, bounded over all of them: any one step's KL is as much the
# position's as the NPU's. The graphs measure a mean of 0.0083 and a p90 of
# 0.018; over 140 positions of prompt.txt the p90 is 0.017. The mean and p90
# bound a drift across many steps, the max a single broken step. The largest
# step is prefill at 0.091, one of two positions of the 140 above 0.05.
# Decode attention over unmasked KV-cache slots measured 9.2.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.2}


def test_llama_3_2_1b_accuracy(runner, model):
    tokens = prompt(runner, 1024, 40)
    # Built here alone: the float32 weights are 5 GB.
    results = accuracy(model, runner.cpu(), tokens, 40)
    kl = np.array([k for k, _ in results])
    stats = {"Mean": kl.mean(), "P90": np.percentile(kl, 90), "Max": kl.max()}
    for stat, value in stats.items():
        record_metric(f"{stat}KL", float(value))
    record_metric("Top1Mismatches", sum(not t for _, t in results))
    for stat, bound in MAX_KL.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"


# Repeated runs must produce bit-identical logits. A prefill KV hand-off that
# was never flushed to the device made 12% of runs diverge. Alternating
# two prompts makes such a missing flush fail every run: 38/38 in each of three
# trials.
def test_llama_3_2_1b_determinism(runner, model):
    prompts = [prompt(runner, 1024, 4), prompt(runner, 1024, 4, skip=1024)]
    differing = determinism(model, prompts, 4, rounds=5)
    record_metric("DifferingRuns", differing)
    assert differing == 0, f"{differing}/8 runs' logits differ bitwise"
