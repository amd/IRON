#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 on the NPU, 1.7B and 0.6B, from the real checkpoints: speed,
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
import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.qwen3 import Qwen3
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

# Each checkpoint's directory under $IRON_EXAMPLE_WEIGHTS_DIR and its file.
CHECKPOINTS = {
    "qwen3_1.7b": ("qwen3-1.7b", "model.safetensors.index.json"),
    "qwen3_0.6b": ("qwen3-0.6b", "model.safetensors"),
}
# The checkpoints CI holds, so one missing there fails, not skips.
STAGED = {"qwen3_1.7b"}

pytestmark = pytest.mark.supported_devices("npu2")


def files(name: str, seed) -> tuple:
    """The checkpoint ``name``'s files a run needs: with ``seed``, its
    weights' header and config.json, else its tokenizer too. One missing
    skips the checkpoint unless CI holds it (``STAGED``).
    """
    directory, checkpoint = CHECKPOINTS[name]
    weights = weights_dir(directory) / checkpoint
    tokenizer = weights.with_name("tokenizer.json")
    config = weights.with_name("config.json")
    needed = (weights, config) if seed is not None else (weights, tokenizer, config)
    if name not in STAGED and not all(f.exists() for f in needed):
        pytest.skip(f"{name}'s files are not in {weights.parent}")
    require(*needed)
    return weights, tokenizer


@pytest.fixture(scope="module", params=list(CHECKPOINTS), ids=str)
def load(request):
    """``Qwen3.load`` of the checkpoint, as the CLI loads it: at the
    options pytest's own ``--random-weights``/``--max-seq-len`` flags
    (``conftest.py``'s, ``iron.lm.cli.FLAGS``) were given.
    """
    seed = request.config.getoption("--random-weights")
    max_seq_len = request.config.getoption("--max-seq-len")
    weights, _ = files(request.param, seed)
    return functools.partial(
        Qwen3.load, weights.parent, seed=seed, max_seq_len=max_seq_len
    )


@pytest.fixture(scope="module")
def model(load):
    """The model, compiled and loaded once; the runtime is released after its
    checkpoint's last test.
    """
    yield load()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


# KL(fp32 CPU || NPU), teacher-forced. TestEachStep's 20-step, 256-char run
# on npu1/Phoenix measured Mean 0.0110, P90 0.0331, Max 0.0553, 2/20 top-1
# mismatches; these bounds give it about 2.5-3x headroom. Not yet measured
# at the module-scoped tests' own 40-step/1024-char shape (full-ELF, npu2
# only). Measured on 1.7B; 0.6B's are 1.7B's until measured.
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}


GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[f"prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin, the
    host drawing each token. Its model is built and dropped with the class,
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

    def test_qwen3_each_step_accuracy(self, model, record_property):
        check_accuracy(model, MAX_KL, 20, 256, record=record_property)

    def test_qwen3_each_step_determinism(self, model, record_property):
        check_determinism(model, 4, 3, 128, record=record_property)


@GENERATION
def test_qwen3(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


# The device draws every token and starts every decode step itself; from the
# same seed its text is the host loop's. The figures are the device loop's.
@pytest.mark.bench
def test_qwen3_device_loop(model, record_property):
    check_device_sampling(model, 1024, 100, record=record_property)


@pytest.mark.bench
def test_qwen3_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


def test_qwen3_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are 3262 tokens (confirmed against Qwen3's
# own tokenizer): a full chunk and most of a second, which attends over the
# first's caches.
LONG = 12000


def test_qwen3_accuracy_across_chunks(model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k+
    tokens on the host, so only a few).
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


def test_qwen3_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)


@pytest.mark.parametrize("name", list(CHECKPOINTS))
def test_qwen3_lm_head_is_the_tied_embedding(name):
    """The real checkpoint's unread ``lm_head.weight`` is byte-identical to
    ``model.embed_tokens.weight``.
    """
    weights, _ = files(name, seed=0)
    tree = Checkpoint(weights).tree()
    assert tree.lm_head.weight.dtype == bfloat16
    assert np.array_equal(
        tree.lm_head.weight.view(np.uint16),
        tree.model.embed_tokens.weight.view(np.uint16),
    )
