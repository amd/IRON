#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct on the NPU, from the real checkpoint: its text
model and vision tower as one ``iron.lm.Multimodal``, against
transformers' own SmolVLM (``SmolVLM.cpu_reference``), over a few (image,
question) pairs, one unsplit image each: the prompt's logits and a decode
step's after it.

``--random-weights SEED`` runs it on drawn weights and random questions,
on a host without the checkpoint.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.idefics3.model import SmolVLM, build_prompt
from iron.lm.generation import divergence
from iron.lm.testing import load_from_flags, weights_dir

WEIGHTS = weights_dir("smolvlm-256m-instruct") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")

# The bound on each question's mean KL(float32 forward || device).
MAX_KL = 0.05

QUESTIONS = [
    "What is in this image?",
    "Describe this photo in detail, please.",
    "What colors do you see?",
]


@pytest.fixture(scope="module")
def model(request):
    yield load_from_flags(request, SmolVLM, WEIGHTS)()


@pytest.fixture(scope="module")
def reference(model):
    return model.cpu_reference()


@pytest.mark.bench
@pytest.mark.parametrize("seed,question", list(enumerate(QUESTIONS)))
def test_smolvlm_accuracy(model, reference, seed, question, record_property):
    """One image (a distinct synthetic one a seed) and one question: the
    device's next-token distribution after the prompt and after one decode
    step against transformers', teacher-forced. KL is held to its bound and
    a top-1 mismatch recorded, as ``check_accuracy`` does: on a synthetic
    image the reference's top two can be near tied.
    """
    vision = model.config.vision
    rng = np.random.default_rng(seed + 10)
    pixels = rng.integers(0, 256, (vision.image_size, vision.image_size, 3))
    # The processor's rescale and normalization, then the device's bf16.
    image = (pixels.astype(np.float32) / 255 - 0.5) / 0.5
    image = image.astype(bfloat16).astype(np.float32)
    if model.tokenizer is None:
        ids = [int(t) for t in rng.integers(0, vision.image_token, len(question) // 4)]
    else:
        ids = model.tokenizer.encoding.encode(question)
    tokens = build_prompt(ids, vision)
    raw = {vision.image_token: (image,)}
    results = []
    for _ in range(2):
        want = reference.logits(tokens, image)
        results.append(divergence(want, model.logits(tokens, raw)))
        tokens.append(int(want.argmax()))
    worst = max(kl for kl, _ in results)
    record_property("MaxKL", worst)
    record_property("Top1Mismatches", sum(not top1 for _, top1 in results))
    assert worst <= MAX_KL, f"KL {worst} > {MAX_KL}"
