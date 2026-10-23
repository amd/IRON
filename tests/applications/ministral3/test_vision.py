# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3 3B Base on the NPU with its vision tower, from the real
checkpoint: its text decoder and Pixtral as one ``iron.lm.Multimodal``,
against transformers' own Mistral 3 and image processor
(``Ministral3VLM.cpu_reference``) on COCO photos, one decoded image a
prompt, each of its own size through one compile: the prompt's logits and a
decode step's after it.
"""

import numpy as np
import pytest
from PIL import Image

from iron.applications.ministral3 import Ministral3VLM
from iron.lm.generation import divergence
from iron.lm.testing import Download, load_from_flags, weights_dir

WEIGHTS = weights_dir("ministral-3-3b-base-2512") / "model.safetensors.index.json"

pytestmark = pytest.mark.supported_devices("npu2")

VAL2017 = "https://s3.amazonaws.com/images.cocodataset.org/val2017"

# COCO val2017 photos, fetched into IRON's cache, each with what is asked
# of it.
PHOTOS = {
    # 640x480: 504x644 pixels, 18 x 23 soft tokens.
    "cats": (
        Download(
            f"{VAL2017}/000000039769.jpg",
            "dea9e7ef97386345f7cff32f9055da4982da5471c48d575146c796ab4563b04e",
        ),
        "The image shows",
    ),
    # 375x500, portrait: 392x504 pixels, 14 x 18 soft tokens.
    "stop_sign": (
        Download(
            f"{VAL2017}/000000000724.jpg",
            "5c0e559c75d3969c8e3e297b61f61063f78045c9d4802b526ba616361f3823fd",
        ),
        "This photo was taken",
    ),
}

# TODO: unmeasured; derive from the first device run against the golden.
MAX_KL = 0.05


@pytest.fixture(scope="module")
def model(request):
    yield load_from_flags(request, Ministral3VLM, WEIGHTS)()


def photo(name: str) -> np.ndarray:
    """``PHOTOS[name]``'s image, decoded: ``(height, width, 3)`` uint8."""
    with Image.open(PHOTOS[name][0].fetch()) as image:
        return np.array(image.convert("RGB"))


def prompt(model, image: np.ndarray, text: str) -> list[int]:
    """The ids of ``image``'s placeholders, as the processor lays them out,
    then ``text``, as the tokenizer begins a text.
    """
    tokenizer = model.tokenizer
    placed = model.config.vision.tokens(*image.shape[:2])
    return tokenizer("".join(map(tokenizer.encoding.token, placed)) + text)


@pytest.mark.bench
@pytest.mark.parametrize("name", list(PHOTOS))
def test_ministral_3_3b_image(model, name, record_property):
    """The device's next-token distribution after the prompt of a photo and
    its words, and after one greedy decode step, against transformers',
    which processes the photo itself, teacher-forced.
    """
    image = photo(name)
    tokens = prompt(model, image, PHOTOS[name][1])
    reference = model.cpu_reference()
    raw = {model.config.vision.image_token: (image,)}
    results = []
    for _ in range(2):
        want = reference.logits(tokens, image)
        results.append(divergence(want, model.logits(tokens, raw)))
        tokens.append(int(want.argmax()))
    worst = max(kl for kl, _ in results)
    record_property("MaxKL", worst)
    record_property("Top1Mismatches", sum(not top1 for _, top1 in results))
    assert worst <= MAX_KL, f"KL {worst} > {MAX_KL}"
