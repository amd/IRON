# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct on the NPU, from the real checkpoint: its text
model and vision tower as one ``iron.lm.Multimodal``, against
transformers' own SmolVLM and image processor (``SmolVLM.cpu_reference``),
which splits an image into squares and its whole, as the checkpoint's
processor does: COCO photos of several sizes and aspects, one compile
serving them all, each a question's prompt and ``STEPS - 1``
teacher-forced decode steps after it.

``--random-weights SEED`` runs it on drawn weights and random questions,
on a host without the checkpoint.
"""

import numpy as np
import pytest

from iron.applications.idefics3.model import SmolVLM, build_prompt
from iron.lm.generation import divergence, kl_stats
from iron.lm.testing import load_from_flags, weights_dir
from iron.tests.support.coco import photo

WEIGHTS = weights_dir("smolvlm-256m-instruct") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")

# The prompt and the decode steps after it, each judged.
STEPS = 8

# The bounds on each case's KL(float32 transformers || device) over its steps,
# twice the worst measured on npu2 (10-23): mean 0.016 and max 0.080, both
# stop_sign's; the others' means 0.0031 to 0.0074, no top-1 mismatch.
MAX_KL = {"Mean": 0.035, "Max": 0.16}

# Each case's COCO photo and question.
CASES = {
    # 640x480: 3 rows of 4 squares and the whole, 832 soft tokens.
    "cats": ("cats", "What is in this image?"),
    # 375x500, portrait: 4 rows of 3.
    "stop_sign": ("stop_sign", "Describe this photo in detail, please."),
    # 640x426: 3 rows of 4, its first resize's 1364 rows split as 1536.
    "living_room": ("living_room", "What colors do you see?"),
    # 621x640: 4 by 4, the most an image gives, 1088 soft tokens.
    "baseball": ("baseball", "What sport is being played?"),
}


def inputs(model, rng, case: str):
    """The prompt of ``CASES[case]``, as the processor lays it out, and the
    photo; random question ids without a tokenizer.
    """
    name, question = CASES[case]
    image, vision = photo(name), model.config.vision
    if model.tokenizer is None:
        ids = [int(t) for t in rng.integers(0, vision.image_token, len(question) // 4)]
    else:
        ids = model.tokenizer.encoding.encode(question)
    return build_prompt(ids, vision, *vision.grid(*image.shape[:2])), image


@pytest.fixture(scope="module")
def model(request):
    yield load_from_flags(request, SmolVLM, WEIGHTS)()


@pytest.fixture(scope="module")
def reference(model):
    return model.cpu_reference()


@pytest.mark.bench
@pytest.mark.parametrize("case", list(CASES))
def test_smolvlm_accuracy(model, reference, case, record_property):
    rng = np.random.default_rng(list(CASES).index(case) + 10)
    tokens, image = inputs(model, rng, case)
    raw = {model.config.vision.image_token: (image,)}
    results = []
    for _ in range(STEPS):
        want = reference.logits(tokens, image)
        results.append(divergence(want, model.logits(tokens, raw)))
        tokens.append(int(want.argmax()))
    stats = kl_stats(results)
    for stat, value in stats.items():
        record_property(f"{stat}KL", float(value))
    record_property("Top1Mismatches", sum(not top1 for _, top1 in results))
    for stat, bound in MAX_KL.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"
