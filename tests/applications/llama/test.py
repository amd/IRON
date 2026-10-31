# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 on the NPU, 1B and 3B, from the real checkpoints.

Speed, accuracy against the float32 reference, determinism, and past
one chunk: a prompt of two and a chat turn (the end of the caches is
``long_context``'s). Every test runs on each checkpoint, which its id
names; each one's model is compiled and loaded once and every test
calls it in-process.

``--random-weights SEED`` runs it on weights drawn in the checkpoint's
shapes (only its header is read) and random prompts, on a host without the
tokenizer, and ``--max-seq-len`` at another context.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.llama import Llama
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_device_sampling,
    check_generation,
    load_from_flags,
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
    directory, name = CHECKPOINTS[request.param]
    weights = weights_dir(directory) / name
    return load_from_flags(request, Llama, weights)


@pytest.fixture(scope="module")
def model(load):
    """Build the model, compiled and loaded once.

    The runtime is released after its checkpoint's last test.
    """
    model = load()
    yield model
    model.release()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


# KL(fp32 CPU || NPU) over 40 steps of 1B measured mean 0.0083, p90 0.018, max 0.091.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.2}


GENERATION = pytest.mark.parametrize(
    "prompt_len,num_tokens",
    [
        pytest.param(
            p,
            n,
            # The shortest per PR; the rest nightly.
            marks=[
                pytest.mark.bench,
                *([] if (p, n) == (13, 1) else [pytest.mark.extensive]),
            ],
        )
        for p in (1024, 13)
        for n in (40, 1)
    ],
    ids=[f"prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)],
)


@pytest.mark.extensive
def test_the_readme_quick_start(record_property):
    """Check the README's quick start, word for word but for the checkpoint's directory.

    In place of the repository's id: ``Llama.load`` compiling from
    scratch. First, so no other model is held beside it.
    """
    directory = weights_dir("llama3.2-1b")
    require(
        directory / "config.json",
        directory / "model.safetensors",
        directory / "tokenizer.json",
    )
    try:
        model = Llama.load(directory)
        out = model.generate("The capital of France is", 8)
        print(out)
    finally:
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()
    record_property("TTFT", model.stats.ttft)
    record_property("TPS", model.stats.tokens_per_s)
    assert out


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin.

    The host starts each on the token the last one drew. Its model is
    built and dropped with the class, first: after any other test it
    would be held beside the module's full-ELF one.
    """

    @pytest.fixture(scope="class")
    def model(self, load):
        model = load(full_elf=False)
        assert not model.device_loop
        yield model
        model.release()
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
@pytest.mark.extensive
@pytest.mark.bench
def test_llama_3_2_device_loop(model, record_property):
    check_device_sampling(model, 1024, 100, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_llama_3_2_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


@pytest.mark.extensive
def test_llama_3_2_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are 3262 tokens: a full chunk and most of a
# second, which attends over the first's caches.
LONG = 12000


@pytest.mark.extensive
def test_llama_3_2_accuracy_across_chunks(model, record_property):
    """Check Llama 3.2 accuracy across chunks.

    The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt (each step a forward over 3k
    tokens on the host, so only a few).
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


@pytest.mark.extensive
def test_llama_3_2_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone."""
    check_chat_turn(model, LONG, 1000, record=record_property)
