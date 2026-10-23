# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.0-H 1B on the NPU, from the real checkpoint: speed, accuracy
against the float32 reference, determinism, and past one chunk: a prompt of
two and a chat turn, which restarts the Mamba2 states from a chunk
boundary's checkpoint. The model is compiled and loaded once for the
module and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.
"""

import pytest

from iron.applications.granite_hybrid import GraniteHybrid
from iron.lm.testing import (
    check_accuracy,
    check_chat_turn,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("granite-4.0-h-1b") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, GraniteHybrid, WEIGHTS)


@pytest.fixture(scope="module")
def model(load):
    yield load()


# KL(fp32 CPU || NPU) measured mean 0.0029, p90 0.0051, max 0.0105 over 40
# steps; over two chunks and two decode steps mean 0.0098, max 0.025.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.05}


@pytest.mark.parametrize(
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
        f"granite_4_0_h_1b_prompt_{p}_tokens_{n}" for p in (1024, 13) for n in (40, 1)
    ],
)
def test_granite_4_0_h_1b(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


@pytest.mark.extensive
@pytest.mark.bench
def test_granite_4_0_h_1b_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, record=record_property)


@pytest.mark.extensive
def test_granite_4_0_h_1b_determinism(model, record_property):
    check_determinism(model, record=record_property)


# 12000 characters of prompt.txt are a full chunk and most of a second,
# which scans on from the first's states.
LONG = 12000


@pytest.mark.extensive
def test_granite_4_0_h_1b_accuracy_across_chunks(model, record_property):
    """The prompt's two chunks and two decode steps after them, against the
    float32 reference over the whole prompt.
    """
    assert len(model.prompt(LONG)) > model.config.prefill_chunk
    check_accuracy(model, MAX_KL, 3, LONG, record=record_property)


@pytest.mark.extensive
def test_granite_4_0_h_1b_chat_turn(model, record_property):
    """A turn of 1000 tokens reruns the second chunk alone, from the states
    the first left at its boundary.
    """
    check_chat_turn(model, LONG, 1000, record=record_property)
