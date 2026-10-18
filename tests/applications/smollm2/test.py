#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM2 1.7B Instruct on the NPU, from the real checkpoint: speed,
accuracy against the float32 reference, determinism, and past one chunk: a
prompt of two and a chat turn (the end of the caches is ``long_context``'s).
The model is compiled and loaded once for the module and every test calls
it in-process.

``--random-weights SEED`` runs it on weights drawn in the checkpoint's
shapes and random prompts, on a host without the tokenizer, and
``--max-seq-len`` at another context.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.smollm2.model import Runner
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_device_sampling,
    check_generation,
    require,
    weights_dir,
)

WEIGHTS = weights_dir("smollm2-1.7b-instruct") / "model.safetensors"
TOKENIZER = weights_dir("smollm2-1.7b-instruct") / "tokenizer.json"
CONFIG = weights_dir("smollm2-1.7b-instruct") / "config.json"

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
def model(runner):
    """The model, compiled and loaded once."""
    yield runner.npu()


# KL(fp32 CPU || NPU), teacher-forced over 40 steps from a 1024-character
# prompt: a mean of 0.034, a p90 of 0.074 and a largest step of 0.287 (3 of
# 40 steps rank another token first); a 10-step, 512-character run measured
# a mean of 0.0056, a p90 of 0.011 and a largest step of 0.032. SmolLM2's 24
# layers at Llama 3.2 1B's widths accumulate more bf16 error a step; these
# bounds are the longer run's with headroom.
MAX_KL = {"Mean": 0.05, "P90": 0.1, "Max": 0.35}

GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"smollm2_1_7b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin, the host
    starting each on the token the last one drew. Its model is built and
    dropped with the class, first: after any other test it would be held
    beside the module's full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, runner):
        model = runner.npu(full_elf=False)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    @GENERATION
    def test_smollm2_1_7b_each_step(
        self, runner, model, prompt_len, num_tokens, record_property
    ):
        check_generation(runner, model, prompt_len, num_tokens, record=record_property)

    def test_smollm2_1_7b_each_step_accuracy(self, runner, model, record_property):
        check_accuracy(runner, model, MAX_KL, 20, 256, record=record_property)

    def test_smollm2_1_7b_each_step_determinism(self, runner, model, record_property):
        check_determinism(runner, model, 4, 3, 128, record=record_property)


@GENERATION
def test_smollm2_1_7b(runner, model, prompt_len, num_tokens, record_property):
    check_generation(runner, model, prompt_len, num_tokens, record=record_property)


# The device draws every token and starts every decode step itself; from the
# same seed its text is the host loop's. The figures are the device loop's.
@pytest.mark.bench
def test_smollm2_1_7b_device_loop(runner, model, record_property):
    check_device_sampling(runner, model, 1024, 100, record=record_property)


def test_smollm2_1_7b_accuracy(runner, model, record_property):
    check_accuracy(runner, model, MAX_KL, record=record_property)


def test_smollm2_1_7b_determinism(runner, model, record_property):
    check_determinism(runner, model, record=record_property)


# 12000 characters of prompt.txt are a full chunk and most of a second,
# which attends over the first's caches.
LONG = 12000


def test_smollm2_1_7b_accuracy_across_chunks(runner, model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt.
    """
    assert len(runner.prompt(LONG)) > runner.config.prefill_chunk
    check_accuracy(runner, model, MAX_KL, 3, LONG, record=record_property)


def test_smollm2_1_7b_chat_turn(runner, model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(runner, model, LONG, 1000, record=record_property)
