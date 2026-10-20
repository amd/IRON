#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct on the NPU, from the real checkpoint: its text
model and vision tower as one ``iron.lm.Multimodal``, against
transformers' own SmolVLM and image processor (``SmolVLM.cpu_reference``),
over a few (image, question) pairs, one unsplit decoded image each, of any
size: the prompt's logits and a decode step's after it.

``--random-weights SEED`` runs it on drawn weights and random questions,
on a host without the checkpoint.
"""

import numpy as np
import pytest

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
# (height, width) of images the processor resizes through its longest edge
# to the tower's 512x512, either way up.
SIZES = [(480, 640), (1000, 667)]


@pytest.fixture(scope="module")
def model(request):
    yield load_from_flags(request, SmolVLM, WEIGHTS)()


@pytest.fixture(scope="module")
def reference(model):
    return model.cpu_reference()


def check(model, reference, image, question, rng, record_property):
    """The device's next-token distribution after the prompt of ``image``
    and ``question`` and after one decode step against transformers', which
    processes the image itself, teacher-forced. KL is held to its bound and
    a top-1 mismatch recorded, as ``check_accuracy`` does: on a synthetic
    image the reference's top two can be near tied.
    """
    vision = model.config.vision
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


@pytest.mark.bench
@pytest.mark.parametrize("seed,question", list(enumerate(QUESTIONS)))
def test_smolvlm_accuracy(model, reference, seed, question, record_property):
    """One decoded 512x512 image (a distinct synthetic one a seed) and one
    question.
    """
    rng = np.random.default_rng(seed + 10)
    image = rng.integers(0, 256, (512, 512, 3), dtype=np.uint8)
    check(model, reference, image, question, rng, record_property)


@pytest.mark.parametrize("size", SIZES, ids=[f"{h}x{w}" for h, w in SIZES])
def test_smolvlm_accuracy_at_another_size(model, reference, size, record_property):
    """One decoded image of ``size``, not the tower's, with the first
    question: the same compile resizes it on the NPU.
    """
    rng = np.random.default_rng(size[0])
    image = rng.integers(0, 256, (*size, 3), dtype=np.uint8)
    check(model, reference, image, QUESTIONS[0], rng, record_property)
