# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct on the NPU, from the real checkpoint: speed,
accuracy against the float32 reference, and determinism. The model is
compiled and loaded once for the module and every test calls it in-process.

``--random-weights SEED`` runs it on drawn weights and random prompts, on
a host without the checkpoint, and ``--max-seq-len`` at another context.

The ``model`` fixture packages it ``--each-step``: at 32 layers the full
ELF links far slower.
"""

import pytest

from iron.applications.phi3 import Phi4
from iron.lm.testing import (
    check_accuracy,
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
    [pytest.param(p, n, marks=pytest.mark.bench) for p in (1024, 13) for n in (40, 1)],
    ids=[
        f"phi_4_mini_instruct_prompt_{p}_tokens_{n}"
        for p in (1024, 13)
        for n in (40, 1)
    ],
)


@GENERATION
def test_phi_4_mini_instruct(model, prompt_len, num_tokens, record_property):
    check_generation(model, prompt_len, num_tokens, record=record_property)


def test_phi_4_mini_instruct_sampling(model, record_property):
    check_device_sampling(model, 256, 20, record=record_property)


@pytest.mark.bench
def test_phi_4_mini_instruct_accuracy(model, record_property):
    check_accuracy(model, MAX_KL, 10, 1024, record=record_property)


def test_phi_4_mini_instruct_determinism(model, record_property):
    check_determinism(model, record=record_property)
