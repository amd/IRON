# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each decoder below on the NPU, from its real checkpoint: speed, accuracy against the float32 reference, determinism, and past one chunk.

A prompt of two and a chat turn (the end of the caches is
``long_context``'s). Each model is compiled and loaded once, and every
test of it calls it in-process.

``--random-weights SEED`` runs them on weights drawn in each checkpoint's
shapes and random prompts, on a host without the tokenizer, and
``--max-seq-len`` at another context.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.gemma4 import Gemma4
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_device_sampling,
    check_generation,
    load_from_flags,
    weights_dir,
)

# Each decoder's class, checkpoint file, and the lengths of the long and the
# short prompt it generates from.
DECODERS = [
    pytest.param((Gemma4, "gemma-4-e2b-it/model.safetensors", (256, 13)), id="gemma4"),
]

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module", params=DECODERS)
def load(request):
    """Return a decoder's loader and its prompts' lengths."""
    cls, weights, prompts = request.param
    return load_from_flags(request, cls, weights_dir(weights)), prompts


@pytest.fixture(scope="module")
def decoder(load):
    """Return a decoder, compiled and loaded once, and its prompts' lengths.

    Its runtime is released before the next decoder loads.
    """
    load_fn, prompts = load
    model = load_fn()
    yield model, prompts
    model.release()
    aie_utils.cleanup_npu_runtime()


# Gemma 4 E2B on npu2 measured mean 0.0055, P90 0.0086, max 0.100 over 40 steps.
MAX_KL = {"Mean": 0.03, "P90": 0.08, "Max": 0.2}


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
# On npu2 this form checks npu1's path; npu2's own figures are its full ELF's.
@pytest.mark.tracked_on("npu1")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of one xclbin.

    The host starts each on the token the last one drew. Its model is
    built and dropped with the class, first: after any other test it
    would be held beside the module's full-ELF one.
    """

    @pytest.fixture(scope="class")
    def decoder(self, load):
        load_fn, prompts = load
        model = load_fn(full_elf=False)
        assert not model.device_loop
        yield model, prompts
        model.release()
        aie_utils.cleanup_npu_runtime()

    @pytest.mark.parametrize(
        "prompt_idx,num_tokens",
        [
            pytest.param(0, 40, id="long-40", marks=pytest.mark.bench),
            pytest.param(1, 1, id="short-1", marks=pytest.mark.bench),
        ],
    )
    def test_gemma4_each_step(self, decoder, prompt_idx, num_tokens, record_property):
        model, prompts = decoder
        check_generation(model, prompts[prompt_idx], num_tokens, record=record_property)

    @pytest.mark.bench
    def test_gemma4_each_step_accuracy(self, decoder, record_property):
        check_accuracy(decoder[0], MAX_KL, record=record_property)

    def test_gemma4_each_step_determinism(self, decoder, record_property):
        check_determinism(decoder[0], record=record_property)


@pytest.mark.bench
@pytest.mark.parametrize(
    "prompt,num_tokens",
    [
        pytest.param(0, 40, id="long-40", marks=pytest.mark.extensive),
        pytest.param(1, 1, id="short-1"),
    ],
)
def test_generation(decoder, prompt, num_tokens, record_property):
    model, prompts = decoder
    check_generation(model, prompts[prompt], num_tokens, record=record_property)


# Decode's speed per PR: the device loop's draws are the host's from the same
# logits, and those within MAX_KL of the golden's (the accuracy test's first
# rows).
@pytest.mark.bench
def test_decode(decoder, record_property):
    check_device_sampling(decoder[0], 1024, 20, record=record_property)
    check_accuracy(decoder[0], MAX_KL, 20, 1024, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_accuracy(decoder, record_property):
    check_accuracy(decoder[0], MAX_KL, record=record_property)


@pytest.mark.extensive
def test_determinism(decoder, record_property):
    check_determinism(decoder[0], record=record_property)


# 12000 characters of prompt.txt are 3261 to 3457 tokens by these
# decoders' tokenizers: two prompt chunks or more, each attending over the
# caches the ones before it wrote.
LONG = 12000


@pytest.mark.extensive
def test_accuracy_across_chunks(decoder, record_property):
    """The prompt's chunks and two decode steps after them, against the float32 reference over the whole prompt."""
    model = decoder[0]
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


@pytest.mark.extensive
def test_chat_turn(decoder, record_property):
    """A turn of 1000 tokens reruns the chunks it reaches alone."""
    check_chat_turn(decoder[0], LONG, 1000, record=record_property)
