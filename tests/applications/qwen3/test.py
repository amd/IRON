#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 1.7B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, and past one chunk: a prompt of
two and a chat turn (the end of the caches is ``long_context``'s). The model is compiled and loaded once for the module and every test calls
it in-process.

``--random-weights SEED`` runs it on weights drawn in the checkpoint's
shapes (only its header is read) and random prompts, on a host without the
tokenizer, and ``--max-seq-len`` at another context.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.qwen3.model import Runner
from iron.lm import Checkpoint
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_device_sampling,
    check_generation,
    require,
    weights_dir,
)

WEIGHTS = weights_dir("qwen3-1.7b") / "model.safetensors.index.json"
TOKENIZER = weights_dir("qwen3-1.7b") / "tokenizer.json"
CONFIG = weights_dir("qwen3-1.7b") / "config.json"

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
    """The model, compiled and loaded once, its versions tuned by
    ``--cost-table`` if given.
    """
    yield runner.npu(request.config.getoption("--cost-table"))


# KL(fp32 CPU || NPU), teacher-forced. TestEachStep's 20-step, 256-char run
# on npu1/Phoenix measured Mean 0.0110, P90 0.0331, Max 0.0553, 2/20 top-1
# mismatches; these bounds give it about 2.5-3x headroom. Not yet measured
# at the module-scoped tests' own 40-step/1024-char shape (full-ELF, npu2
# only).
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}


GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"qwen3_1_7b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin, the
    host drawing each token. Its model is built and dropped with the class,
    first: after any other test it would be held beside the module's
    full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, runner):
        model = runner.npu(full_elf=False)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    def test_qwen3_1_7b_each_step_accuracy(self, runner, model, record_property):
        check_accuracy(runner, model, MAX_KL, 20, 256, record=record_property)

    def test_qwen3_1_7b_each_step_determinism(self, runner, model, record_property):
        check_determinism(runner, model, 4, 3, 128, record=record_property)


@GENERATION
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


def test_qwen3_1_7b_lm_head_is_the_tied_embedding():
    """The real checkpoint's unread ``lm_head.weight`` is byte-identical to
    ``model.embed_tokens.weight``, read from both shards by their index.
    """
    require(WEIGHTS)
    tree = Checkpoint(WEIGHTS).tree()
    assert tree.lm_head.weight.dtype == bfloat16
    assert np.array_equal(
        tree.lm_head.weight.view(np.uint16),
        tree.model.embed_tokens.weight.view(np.uint16),
    )
