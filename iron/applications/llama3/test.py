#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, and determinism. The model is compiled and
loaded once for the module and every test calls it in-process.
"""

import pytest

from iron.applications.common.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    requires,
    weights_dir,
)
from iron.applications.llama3.model import Runner

WEIGHTS = weights_dir("llama3.2-1b") / "model.safetensors"
TOKENIZER = weights_dir("llama3.2-1b") / "tokenizer.model"

pytestmark = [requires(WEIGHTS, TOKENIZER), pytest.mark.supported_devices("npu2")]


@pytest.fixture(scope="module")
def runner():
    return Runner(WEIGHTS, TOKENIZER)


@pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [(p, n) for p in (1024, 13) for n in (40, 1)],
    ids=[f"llama_3.2_1b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)
def test_llama_3_2_1b(runner, model, prompt_len, num_tokens):
    check_generation(runner, model, prompt_len, num_tokens)


# KL(fp32 CPU || NPU), teacher-forced over 40 steps. The graphs measure a
# mean of 0.0083 and a p90 of 0.018; over 140 positions of prompt.txt the
# p90 is 0.017. The largest step is prefill at 0.091, one of two positions
# of the 140 above 0.05. Decode attention over unmasked KV-cache slots
# measured 9.2.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.2}


def test_llama_3_2_1b_accuracy(runner, model):
    check_accuracy(runner, model, MAX_KL)


def test_llama_3_2_1b_determinism(runner, model):
    check_determinism(runner, model)
