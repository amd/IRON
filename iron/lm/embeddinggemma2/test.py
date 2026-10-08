#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's text encoder on the NPU, from the real checkpoint,
against its float32 oracle: each embedding's cosine to the oracle's, its
norm, the cosine similarities a query gives two documents, and every call
bit-identical to the first. The oracle, over text, a clip and an image,
once against Hugging Face's processor and model.
"""

import time

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.lm import Checkpoint, load_weights
from iron.lm.embeddinggemma2.audio import model as audio_model
from iron.lm.embeddinggemma2.audio.model import AUDIO, LogMel
from iron.lm.embeddinggemma2.audio.oracle import AudioOracle
from iron.lm.embeddinggemma2.encoder import Encoder
from iron.lm.embeddinggemma2.model import (
    COSTS,
    EMBEDDINGGEMMA_2,
    layout,
    text_tensors,
)
from iron.lm.embeddinggemma2.oracle import (
    PROMPTS,
    EmbeddingGemmaOracle,
    tokenizer,
    tokens,
)
from iron.lm.embeddinggemma2.vision import model as vision_model
from iron.lm.embeddinggemma2.vision.model import VISION
from iron.lm.embeddinggemma2.vision.oracle import VisionOracle, patches
from iron.lm.testing import requires, weights_dir

DIRECTORY = weights_dir("embeddinggemma-2")

pytestmark = requires(DIRECTORY / "model.safetensors", DIRECTORY / "tokenizer.json")

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
    yield Encoder(DIRECTORY, max_tokens=1024)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.fixture(scope="module")
def oracle(encoder):
    return encoder.oracle()


@pytest.mark.supported_devices("npu2")
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


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("dims", [512, 256, 128])
def test_embeddinggemma_2_truncation(encoder, oracle, dims, record_property):
    tokens = encoder.tokens(QUERY, "query")
    got = encoder.graph.encode(tokens, dims)
    record_property("Norm", float(np.linalg.norm(got)))
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)
    similarity = cosine(got, oracle(tokens, dims))
    record_property("Cosine", similarity)
    assert similarity >= MIN_COSINE, similarity


@pytest.mark.supported_devices("npu2")
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


# 50 soft tokens, and an image the processor upscales to 13 x 20 of its 280.
CLIP = chirp(2.0)
IMAGE = picture(288, 432)


@pytest.fixture(scope="module")
def multimodal():
    yield Encoder(DIRECTORY, max_tokens=512, towers=True, costs=COSTS)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


MIXED = {
    "audio": ("<|audio|> a bird singing", CLIP, None),
    "image": ("<|image|> waves at dusk", None, IMAGE),
    "both": ("<|image|> the picture, then the sound: <|audio|>", CLIP, IMAGE),
}


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("text,audio,image", MIXED.values(), ids=MIXED.keys())
def test_embeddinggemma_2_multimodal(multimodal, text, audio, image, record_property):
    c = multimodal.config
    got = multimodal(text, "query", audio=audio, image=image)
    audio_oracle, vision_oracle = multimodal.tower_oracles()
    soft = {}
    if audio is not None:
        soft[c.audio_token] = audio_oracle(*LogMel(AUDIO)(audio))
    if image is not None:
        soft[c.image_token] = vision_oracle(
            *patches(image, VISION.image_tokens, VISION)
        )
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


@pytest.mark.supported_devices("npu2")
def test_embeddinggemma_2_determinism(multimodal):
    # Interleaved, so that a version reading what another left in the shared
    # arena or state differs from its first call.
    calls = [(LONG, None, None), *MIXED.values()]
    first = [multimodal(t, "query", audio=a, image=i) for t, a, i in calls]
    for _ in range(4):
        for (t, a, i), want in zip(calls, first):
            np.testing.assert_array_equal(
                multimodal(t, "query", audio=a, image=i), want
            )


@pytest.fixture(scope="module")
def hugging_face():
    """Hugging Face's processor and float32 model of the checkpoint."""
    # Optional dependencies: the reference implementation, where installed.
    torch = pytest.importorskip("torch")
    # The processor's image resize needs both.
    pytest.importorskip("torchvision")
    pytest.importorskip("PIL")
    transformers = pytest.importorskip("transformers")
    pytest.importorskip(
        "transformers.models.embedding_gemma2.modeling_embedding_gemma2"
    )
    processor = transformers.AutoProcessor.from_pretrained(DIRECTORY)
    # Not eager: there Gemma4AudioAttention inverts the additive float mask
    # create_bidirectional_mask gives it.
    model = transformers.AutoModel.from_pretrained(
        DIRECTORY, dtype=torch.float32, attn_implementation="sdpa"
    ).eval()
    return processor, model


@pytest.fixture(scope="module")
def oracles():
    """The float32 text encoder and towers on the host, and the tokenizer."""
    tensors = Checkpoint(DIRECTORY / "model.safetensors").tensors
    c, A, V = EMBEDDINGGEMMA_2, AUDIO, VISION
    return (
        EmbeddingGemmaOracle(
            c, load_weights(text_tensors(tensors), layout(c), c.n_layers)
        ),
        AudioOracle(
            A,
            load_weights(
                audio_model.audio_tensors(tensors), audio_model.layout(A), A.n_layers
            ),
        ),
        VisionOracle(
            V,
            load_weights(
                vision_model.vision_tensors(tensors),
                vision_model.layout(V),
                V.n_layers,
            ),
        ),
        tokenizer(DIRECTORY / "tokenizer.json"),
    )


# At the size the processor's resize picks, so that its pixels are ours: 14 x 20
# tokens, the whole budget.
PROCESSED = picture(672, 960)


@pytest.mark.parametrize(
    "text,task,wave,image",
    [
        (QUERY, "query", None, None),
        (LONGER, "document", None, None),
        ("<|audio|> a bird singing", "query", chirp(2.0), None),
        ("<|image|> waves at dusk", "query", None, PROCESSED),
        (
            "<|image|> the picture, then the sound: <|audio|>",
            "query",
            chirp(2.0),
            PROCESSED,
        ),
    ],
    ids=["query", "past_the_window", "audio", "image", "both"],
)
def test_embeddinggemma_2_oracle_matches_hugging_face(
    hugging_face, oracles, text, task, wave, image
):
    torch = pytest.importorskip("torch")
    processor, model = hugging_face
    text_oracle, audio_oracle, vision_oracle, tok = oracles
    c = EMBEDDINGGEMMA_2
    media, soft = {}, {}
    if wave is not None:
        media["audio"] = [wave]
        soft[c.audio_token] = audio_oracle(*LogMel(AUDIO)(wave))
    if image is not None:
        media["images"] = [image]
        soft[c.image_token] = vision_oracle(
            *patches(image, VISION.image_tokens, VISION)
        )
    ids = tokens(
        tok,
        c,
        text,
        task,
        len(soft.get(c.audio_token, ())),
        len(soft.get(c.image_token, ())),
    )
    inputs = processor(text=PROMPTS[task] + text, return_tensors="pt", **media)
    assert ids == inputs["input_ids"][0].tolist()
    with torch.no_grad():
        want = model(**inputs).last_hidden_state[0].numpy().mean(axis=0)
    want /= np.linalg.norm(want)
    got = text_oracle(ids, soft=soft)
    # Measured: 1.4e-6 at the most, float32's own reordering.
    np.testing.assert_allclose(np.linalg.norm(got - want), 0, atol=1e-5)


@pytest.mark.supported_devices("npu2")
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
