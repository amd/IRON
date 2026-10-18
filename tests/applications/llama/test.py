#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 on the NPU, 1B and 3B, from the real checkpoints: speed,
accuracy against the float32 reference, determinism, and past one chunk: a
prompt of two and a chat turn (the end of the caches is ``long_context``'s).
Every test runs on each checkpoint, which its id names; each one's model is
compiled and loaded once and every test calls it in-process.

``--random-weights SEED`` runs it on weights drawn in the checkpoint's
shapes (only its header is read) and random prompts, on a host without the
tokenizer, and ``--max-seq-len`` at another context.
"""

import functools

import aie.utils as aie_utils
import pytest

from iron.applications.llama import Llama
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_device_sampling,
    check_generation,
    require,
    weights_dir,
)

# Each checkpoint's directory under $IRON_EXAMPLE_WEIGHTS_DIR and its file:
# 3B's is two shards and their index. CI holds both, so one missing there
# fails (``require``).
CHECKPOINTS = {
    "llama_3.2_1b": ("llama3.2-1b", "model.safetensors"),
    "llama_3.2_3b": ("llama3.2-3b", "model.safetensors.index.json"),
}

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module", params=list(CHECKPOINTS), ids=str)
def load(request):
    """``Llama.load`` of the checkpoint, as the CLI loads it: at the
    options pytest's own ``--random-weights``/``--max-seq-len`` flags
    (``conftest.py``'s, ``iron.lm.cli.FLAGS``) were given.
    """
    directory, name = CHECKPOINTS[request.param]
    weights = weights_dir(directory) / name
    tokenizer = weights.with_name("tokenizer.model")
    config = weights.with_name("config.json")
    seed = request.config.getoption("--random-weights")
    max_seq_len = request.config.getoption("--max-seq-len")
    require(*((weights, config) if seed is not None else (weights, tokenizer, config)))
    return functools.partial(
        Llama.load, weights.parent, seed=seed, max_seq_len=max_seq_len
    )


@pytest.fixture(scope="module")
def model(load):
    """The model, compiled and loaded once; the runtime is released after its
    checkpoint's last test.
    """
    yield load()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


# KL(fp32 CPU || NPU), teacher-forced over 40 steps. The graphs measure a
# mean of 0.0083 and a p90 of 0.018; over 140 positions of prompt.txt the
# p90 is 0.017. The largest step is prefill at 0.091, one of two positions
# of the 140 above 0.05. Decode attention over unmasked KV-cache slots
# measured 9.2. Measured on 1B; 3B's projections take bf16 macs (its
# profile), and its bounds are 1B's until measured.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.2}


GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin, the host
    starting each on the token the last one drew. Its model is built and dropped with the class,
    first: after any other test it would be held beside the module's
    full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, load):
        model = load(full_elf=False)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    @GENERATION
    def test_llama_3_2_each_step(self, model, prompt_len, num_tokens, record_property):
        check_generation(model, prompt_len, num_tokens, record=record_property)

    def test_llama_3_2_each_step_accuracy(self, model, record_property):
        check_accuracy(model, MAX_KL, 20, 256, record=record_property)

    def test_llama_3_2_each_step_sampling(self, model, record_property):
        check_device_sampling(model, 256, 20, record=record_property)

    def test_llama_3_2_each_step_determinism(self, model, record_property):
        check_determinism(model, 4, 3, 128, record=record_property)


@GENERATION
def test_llama_3_2(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


# The device draws every token and starts every decode step itself; from the
# same seed its text is the host loop's. The figures are the device loop's.
@pytest.mark.bench
def test_llama_3_2_device_loop(model, record_property):
    check_device_sampling(model, 1024, 100, record=record_property)


def test_llama_3_2_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


def test_llama_3_2_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are 3262 tokens: a full chunk and most of a
# second, which attends over the first's caches.
LONG = 12000


def test_llama_3_2_accuracy_across_chunks(model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k
    tokens on the host, so only a few).
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


def test_llama_3_2_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
