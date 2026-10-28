# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4 E2B whole on the NPU, from the real checkpoint: its text decoder
and its vision and audio towers as one ``iron.lm.Multimodal``
(``Gemma4Multimodal``), against transformers' own Gemma 4 and processors in
float32 (``hugging_face.py``), its logits recorded in ``golden.npz`` beside
the checkpoint. Each case is a chat turn over COCO photos and LibriSpeech
clips of several sizes, one compile serving them all: the prompt's
next-token distribution and ``STEPS - 1`` teacher-forced decode steps'.
"""

import numpy as np
import pytest

from iron.applications.gemma4.model import Gemma4Multimodal
from iron.lm.generation import divergence, kl_stats
from iron.lm.testing import load_from_flags, weights_dir
from iron.tests.support.coco import photo
from iron.tests.support.librispeech import utterance

WEIGHTS = weights_dir("gemma-4-e2b-it") / "model.safetensors"

pytestmark = pytest.mark.supported_devices("npu2")

# The prompt and the decode steps after it, each judged.
STEPS = 8

# The bounds on each case's KL(float32 transformers || device) over its steps,
# twice the worst measured on npu2 (10-23): mean 0.0053 and max 0.042, both
# stop_sign's; the others' means 0.00005 to 0.0024.
MAX_KL = {"Mean": 0.01, "Max": 0.08}

# Each case's question, COCO photo and LibriSpeech utterance, a chat turn
# with the photo, then the clip, before the question.
CASES = {
    # 640x480: 14 by 19 soft tokens.
    "cats": ("What is in this image?", "cats", None),
    # 375x500, portrait: 19 by 14.
    "stop_sign": ("Describe this photo in detail.", "stop_sign", None),
    # 2.0 s: 50 soft tokens.
    "short_clip": ("Transcribe this audio.", None, "121-127105-0021"),
    # 7.3 s: 183.
    "medium_clip": ("Transcribe this audio.", None, "4446-2275-0016"),
    "both": (
        "Does the speech describe the picture?",
        "living_room",
        "121-127105-0021",
    ),
}


def inputs(config, tokenizer, case: str):
    """The prompt of ``CASES[case]``, as the chat template and
    ``Gemma4Processor`` lay it out, the model's ``raw`` by placeholder, and
    the photo and the clip as the reference takes them (empty: none).
    """
    question, name, speech = CASES[case]
    content, raw = [], {}
    image = np.zeros((0, 0, 3), np.uint8)
    audio = np.zeros(0, np.float32)
    if name is not None:
        image = photo(name)
        content.append({"type": "image"})
        raw[config.image_token_id] = (image, config.vision.image_tokens)
    if speech is not None:
        audio = utterance(speech)
        content.append({"type": "audio"})
        raw[config.audio_token_id] = (audio,)
    content.append({"type": "text", "text": question})
    tokens = tokenizer.chat([{"role": "user", "content": content}])
    return config.expand(tokens, raw), raw, (image, audio)


@pytest.fixture(scope="module")
def model(request):
    model = load_from_flags(request, Gemma4Multimodal, WEIGHTS)()
    yield model
    model.release()


@pytest.fixture(scope="module")
def reference(model):
    return model.cpu_reference()


@pytest.mark.extensive
@pytest.mark.parametrize("case", list(CASES))
def test_gemma4_multimodal_accuracy(model, reference, case, record_property):
    tokens, raw, media = inputs(model.config, model.tokenizer, case)
    results = []
    for _ in range(STEPS):
        want = reference.logits(tokens, *media)
        results.append(divergence(want, model.logits(tokens, raw)))
        tokens.append(int(want.argmax()))
    stats = kl_stats(results)
    for stat, value in stats.items():
        record_property(f"{stat}KL", float(value))
    record_property("Top1Mismatches", sum(not top1 for _, top1 in results))
    for stat, bound in MAX_KL.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"
