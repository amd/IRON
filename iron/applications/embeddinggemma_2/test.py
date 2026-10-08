#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's text encoder on the NPU, from the real checkpoint,
against its float32 oracle: each embedding's cosine to the oracle's, its
norm, and the cosine similarities a query gives two documents.
"""

import time

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.lm.embeddinggemma2.audio.model import AUDIO, LogMel
from iron.lm.embeddinggemma2.encoder import Encoder
from iron.lm.embeddinggemma2.model import COSTS
from iron.lm.embeddinggemma2.vision.model import VISION
from iron.lm.embeddinggemma2.vision.oracle import patches
from iron.lm.testing import require, weights_dir

DIRECTORY = weights_dir("embeddinggemma-2")

pytestmark = pytest.mark.supported_devices("npu2")

QUERY = "What causes the northern lights?"
DOCUMENTS = [
    "The northern lights are caused by charged particles from the sun.",
    "Photosynthesis converts light energy into chemical energy in plants.",
]
PARAGRAPHS = [
    f"Paragraph {i}: the aurora borealis appears when solar wind particles collide "
    "with oxygen and nitrogen atoms in the upper atmosphere, emitting green and red light."
    for i in range(30)
]
# About 370 tokens: the 512-row version.
LONG = " ".join(PARAGRAPHS[:12])
# About 920 tokens: the 1024-row version, past the sliding window.
LONGER = " ".join(PARAGRAPHS)

# Measured: 0.99986 at the least, where HF's own bf16 model is 0.99997.
MIN_COSINE = 0.9995
# Against the oracle fed its own towers' soft tokens, so the towers' error is in
# it. Measured: 0.99986 with an image, as the text alone.
MIN_COSINE_MIXED = 0.9995
# A unit vector rounded to bf16 is up to 2**-9 off in norm, and the device's
# reaches it.
NORM_RTOL = 2**-8


def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


@pytest.fixture(scope="module")
def encoder():
    require(DIRECTORY / "model.safetensors", DIRECTORY / "tokenizer.json")
    yield Encoder(DIRECTORY, max_tokens=1024)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.fixture(scope="module")
def oracle(encoder):
    return encoder.oracle()


@pytest.mark.parametrize(
    "text,task",
    [
        (QUERY, "query"),
        (DOCUMENTS[0], "document"),
        (LONG, "document"),
        (LONGER, "document"),
    ],
    ids=["query", "document", "long_document", "past_the_window"],
)
def test_embeddinggemma_2_accuracy(encoder, oracle, text, task, record_property):
    tokens = encoder.tokens(text, task)
    got = encoder.graph.encode(tokens)
    similarity = cosine(got, oracle(tokens))
    record_property("Cosine", similarity)
    record_property("Norm", float(np.linalg.norm(got)))
    assert similarity >= MIN_COSINE, similarity
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)


@pytest.mark.parametrize("dims", [512, 256, 128])
def test_embeddinggemma_2_truncation(encoder, oracle, dims, record_property):
    tokens = encoder.tokens(QUERY, "query")
    got = encoder.graph.encode(tokens, dims)
    record_property("Norm", float(np.linalg.norm(got)))
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)
    similarity = cosine(got, oracle(tokens, dims))
    record_property("Cosine", similarity)
    assert similarity >= MIN_COSINE, similarity


def test_embeddinggemma_2_ranking(encoder, oracle):
    query = encoder(QUERY, "query")
    scores = [cosine(encoder(d, "document"), query) for d in DOCUMENTS]
    want_query = oracle(encoder.tokens(QUERY, "query"))
    want = [
        cosine(oracle(encoder.tokens(d, "document")), want_query) for d in DOCUMENTS
    ]
    assert scores[0] > scores[1]
    # Measured: 0.0013 and 0.0016 below the oracle's 0.871 and 0.604.
    np.testing.assert_allclose(scores, want, atol=3e-3)


def chirp(seconds: float) -> np.ndarray:
    """A rising chirp under noise, mono at the extractor's sample rate."""
    rng = np.random.default_rng(0)
    t = np.arange(int(seconds * AUDIO.sample_rate)) / AUDIO.sample_rate
    wave = 0.5 * np.sin(2 * np.pi * (200 * t + 900 * t**2))
    return (wave + 0.05 * rng.standard_normal(t.size)).astype(np.float32)


def picture(height: int, width: int) -> np.ndarray:
    """A `(height, width, 3)` uint8 image of smooth waves under noise."""
    rng = np.random.default_rng(1)
    y, x = np.mgrid[:height, :width]
    image = np.stack(
        [128 + 100 * np.sin(x / 37), 128 + 90 * np.cos((x + y) / 51), 255 * y / height],
        axis=-1,
    )
    return np.clip(image + rng.normal(0, 12, image.shape), 0, 255).astype(np.uint8)


# 50 soft tokens, and 6 x 9 of an image's 280.
CLIP = LogMel(AUDIO)(chirp(2.0))
IMAGE = patches(picture(288, 432), VISION.image_tokens, VISION)


@pytest.fixture(scope="module")
def multimodal():
    require(DIRECTORY / "model.safetensors", DIRECTORY / "tokenizer.json")
    yield Encoder(DIRECTORY, max_tokens=512, towers=True, costs=COSTS)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.mark.parametrize(
    "text,audio,image",
    [
        ("<|audio|> a bird singing", CLIP, None),
        ("<|image|> waves at dusk", None, IMAGE),
    ],
    ids=["audio", "image"],
)
def test_embeddinggemma_2_multimodal(multimodal, text, audio, image, record_property):
    c = multimodal.config
    got = multimodal(text, "query", audio=audio, image=image)
    audio_oracle, vision_oracle = multimodal.tower_oracles()
    soft = {}
    if audio is not None:
        soft[c.audio_token] = audio_oracle(*audio)
    if image is not None:
        soft[c.image_token] = vision_oracle(*image)
    tokens = multimodal.tokens(
        text,
        "query",
        len(soft.get(c.audio_token, ())),
        len(soft.get(c.image_token, ())),
    )
    similarity = cosine(got, multimodal.oracle()(tokens, soft=soft))
    record_property("Cosine", similarity)
    record_property("Norm", float(np.linalg.norm(got)))
    assert similarity >= MIN_COSINE_MIXED, similarity
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)


@pytest.mark.bench
@pytest.mark.parametrize(
    "text", [QUERY, LONG, LONGER], ids=["query", "long_document", "past_the_window"]
)
def test_embeddinggemma_2_latency(encoder, text, record_property):
    tokens = encoder.tokens(text, "document")
    encoder.graph.encode(tokens)
    times = []
    for _ in range(10):
        t = time.perf_counter()
        encoder.graph.encode(tokens)
        times.append(time.perf_counter() - t)
    record_property("Latency", float(np.median(times)) * 1e6)
