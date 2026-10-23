# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct on the NPU, from the real checkpoint: speed,
accuracy against the float32 reference, determinism, and past its original
4096-position context, where LongRoPE turns to its long table: a prompt of
three chunks and a chat turn. The model is compiled and loaded once for the
module and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.

The ``model`` fixture packages it ``--each-step``: at 32 layers the full
ELF links far slower.
"""

import pytest

from iron.applications.phi3 import Phi4
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_generation,
    check_device_sampling,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("phi-4-mini-instruct") / "model.safetensors.index.json"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, Phi4, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    """The model, compiled and loaded once, packaged ``--each-step``."""
    yield load(full_elf=False)


# KL(fp32 CPU || NPU) over 13 steps measured 0.00039 to 0.0224, every top-1 matching.
MAX_KL = {"Mean": 0.015, "P90": 0.025, "Max": 0.1}


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
    ids=[
        f"phi_4_mini_instruct_prompt_{p}_tokens_{n}"
        for p in (1024, 13)
        for n in (40, 1)
    ],
)


@GENERATION
def test_phi_4_mini_instruct(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.extensive
def test_phi_4_mini_instruct_sampling(model, record_property):
    check_device_sampling(model, 256, 20, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_phi_4_mini_instruct_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, 10, 1024, record=record_property)


@pytest.mark.extensive
def test_phi_4_mini_instruct_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 22000 characters of prompt.txt, the text repeated past its end, are 5877
# tokens: past 4096 with the last 1000 left off too, so a chat turn's
# history and the run from scratch both rotate by the long table.
PAST = 22000


@pytest.mark.extensive
def test_phi_4_mini_instruct_accuracy_past_4096(model, record_property):
    """The prompt's three chunks, past the original context, and two decode
    steps after them, against the float32 reference over the whole prompt,
    which rotates every position by the long table as the device does.
    """
    assert (
        len(model.prompt(PAST)) - 1000 > model.config.original_max_position_embeddings
    )
    check_accuracy(model, MAX_KL, 3, PAST, record=record_property)


@pytest.mark.extensive
def test_phi_4_mini_instruct_chat_turn(model, record_property):
    """A turn of 1000 tokens past 4096 reruns the third chunk alone."""
    check_chat_turn(model, PAST, 1000, record=record_property)
