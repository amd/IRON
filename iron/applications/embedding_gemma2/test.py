#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 on the NPU, from the real checkpoint, against its
float32 oracles: the text encoder's embeddings (their cosine to the
oracle's, their norm, a query ranking two documents, every call
bit-identical to the first), each tower's soft tokens and, over text with
a clip and an image, the whole model's. The audio tower's features and the
image processor's patches are checked against the host's, which the
oracles take. The oracles are checked once against Hugging Face's
processors and model, their outputs saved by hugging_face.py. On NPU1 each
step is its own dispatch of an xclbin; on NPU2 that form is checked too.

Each tower's graph is built for the class that tests it and dropped after
it, before the text encoder's graphs are built for the module's last tests.
"""

import hashlib
import time
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import CostTable, JointNarrowing
from iron.applications.embedding_gemma2.audio import AudioTower
from iron.applications.embedding_gemma2.config import (
    PROFILES,
    AudioConfig,
    Config,
    VisionConfig,
)
from iron.applications.embedding_gemma2.model import (
    EmbeddingGemma,
    Multimodal,
    Tokenizer,
)
from iron.applications.embedding_gemma2.oracle import (
    AudioOracle,
    EmbeddingGemmaOracle,
    VisionOracle,
)
from iron.applications.embedding_gemma2.vision import VisionTower
from iron.applications.embedding_gemma2.weights import Weights
from iron.lm.testing import require, weights_dir
from iron.operators.copy import Copy

DIRECTORY = weights_dir("embeddinggemma-2")
# Hugging Face's outputs on these tests' inputs, by part, as hugging_face.py
# saved them.
REFERENCES = {
    part: Path(__file__).with_name(f"hugging_face{suffix}.npz")
    for part, suffix in (("text", ""), ("audio", "_audio"), ("vision", "_vision"))
}

QUERY = "What causes the northern lights?"
DOCUMENTS = [
    "The northern lights are caused by charged particles from the sun.",
    "Photosynthesis converts light energy into chemical energy in plants.",
]
PARAGRAPHS = [
    f"Paragraph {i}: the aurora borealis appears when solar wind particles collide "
    "with oxygen and nitrogen atoms in the upper atmosphere, emitting green and red light."
    for i in range(60)
]
# About 370 tokens.
LONG = " ".join(PARAGRAPHS[:12])
# About 920 tokens, past the sliding window.
LONGER = " ".join(PARAGRAPHS[:30])
# About 1840 tokens, near the encoder's 2048.
LONGEST = " ".join(PARAGRAPHS)

# Measured: 0.99986 at the least, where HF's own bf16 model is 0.99997.
MIN_COSINE = 0.9995
# Against the oracle fed its own towers' soft tokens, so the towers' error is in
# it. Measured: 0.99986 with an image, as the text alone.
MIN_COSINE_MIXED = 0.9995
# A unit vector rounded to bf16 is up to 2**-9 off in norm, and the device's
# reaches it.
NORM_RTOL = 2**-8

# Measured: 0.99925, 0.99953, 0.99931 and 0.99941 of the features are the
# host extractor's rounded to bf16.
AUDIO_MIN_EXACT = 0.999
# The rest are within one bf16 ulp, bar a log near 0, where the energy's
# relative error is the feature's absolute one: measured 1.9e-6 at most.
AUDIO_ATOL = 4e-6
# Measured: 0.983, 0.779, 0.565 and 0.622 at the worst token (mean 0.996 or
# more), where HF's own bf16 tower reaches 0.861, 0.795, 0.902 and 0.689.
AUDIO_MIN_COSINE = 0.55
# Measured: 0.042, 0.084, 0.072 and 0.074; the tower without its clamps is 0.88.
AUDIO_MAX_ERROR = 0.09

# Measured at the worst of IMAGES: min cosine 0.9705, relative error 4.0e-2.
# bf16 error grows over 16 layers: HF's own bf16 tower is 0.9973 and 2.3e-2
# off the oracle, the graph's bf16 reference 0.9864 and 2.9e-2.
VISION_MIN_COSINE = 0.96
VISION_MAX_ERROR = 0.05

# Seconds of audio, by the soft tokens they give.
CLIPS = {
    # 50 tokens.
    "short": 2.0,
    # 183 tokens.
    "medium": 7.3,
    # 450 tokens.
    "extended": 18.0,
    # 750 tokens: the extractor's 30 s cap.
    "long": 30.0,
}

I, V = VisionConfig().image_tokens, VisionConfig().video_tokens

# (height, width) of a decoded image, and its soft-token budget.
IMAGES = {
    # 14 x 20 tokens at its own size: the whole image budget, 2520 patches.
    "image": ((672, 960), I),
    # Resized to 21 x 12 tokens, 2268 patches: the processor pads 252 of them.
    "portrait": ((960, 576), I),
    # 10 x 14 tokens at its own size: a video frame's budget, 1260 patches.
    "video_frame": ((480, 672), V),
}

# The resizes the image processor is checked on, against Hugging Face's and
# on the NPU, each a (height, width) and budget and what the NPU's refuses
# it for: a phone photo either way up, up- and downscales, extreme aspect
# ratios, one side unchanged, and an image already at its size.
RESIZES = [
    ((3024, 4032), I, None),
    ((4032, 3024), I, None),
    ((480, 640), I, None),
    ((333, 517), V, None),
    ((1080, 1920), V, None),
    # 3648 pixels wide: more patch columns than 16 cores hold.
    ((97, 2003), I, "patch columns"),
    ((2003, 97), V, None),
    ((1, 5000), I, "patch columns"),
    ((17, 23), V, None),
    ((672, 517), I, None),
    ((672, 960), I, None),
]


def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def chirp(seconds: float, sweep: float = 900.0, over: float = 1.0) -> np.ndarray:
    """A chirp from 200 Hz under noise, its phase `sweep * t ** 2 / over`
    cycles past a steady tone's, mono at the extractor's sample rate.
    """
    rng = np.random.default_rng(0)
    rate = AudioConfig().sample_rate
    t = np.arange(int(seconds * rate)) / rate
    wave = 0.5 * np.sin(2 * np.pi * (200 * t + sweep * t**2 / over))
    return (wave + 0.05 * rng.standard_normal(t.size)).astype(np.float32)


def clip(name: str) -> np.ndarray:
    """The tower's clip `name`, rising 3600 Hz over its length."""
    seconds = CLIPS[name]
    return chirp(seconds, 1800, max(seconds, 1))


def synthetic_image(height: int, width: int) -> np.ndarray:
    """A `(height, width, 3)` uint8 image: smooth waves and a ramp under noise."""
    rng = np.random.default_rng(0)
    y, x = np.mgrid[:height, :width]
    image = np.stack(
        [
            128 + 100 * np.sin(x / 37) * np.cos(y / 23),
            128 + 90 * np.cos((x + y) / 51),
            255 * x / width,
        ],
        axis=-1,
    )
    return np.clip(image + rng.normal(0, 12, image.shape), 0, 255).astype(np.uint8)


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

MIXED = {
    "audio": ("<|audio|> a bird singing", CLIP, None),
    "image": ("<|image|> waves at dusk", None, IMAGE),
    "both": ("<|image|> the picture, then the sound: <|audio|>", CLIP, IMAGE),
    # 325 soft tokens of audio and an image's.
    "long_clip_and_image": (
        "<|image|> the picture, then the sound: <|audio|>",
        chirp(13.0),
        IMAGE,
    ),
}

# The cases hugging_face.py saved the processor's ids and the model's
# embedding for: text, and text with a clip and an image at the size the
# processor's resize picks, so that its pixels are ours (14 x 20 tokens, the
# whole budget).
HUGGING_FACE = {
    "query": (QUERY, "query", None, None),
    "past_the_window": (LONGER, "document", None, None),
    "audio": ("<|audio|> a bird singing", "query", CLIP, None),
    "image": ("<|image|> waves at dusk", "query", None, picture(672, 960)),
    "both": (
        "<|image|> the picture, then the sound: <|audio|>",
        "query",
        CLIP,
        picture(672, 960),
    ),
}


@pytest.fixture(scope="module")
def weights():
    require(DIRECTORY / "model.safetensors")
    return Weights.read(DIRECTORY)


@pytest.fixture(scope="module")
def tokenizer():
    require(DIRECTORY / "tokenizer.json")
    return Tokenizer(DIRECTORY / "tokenizer.json")


@pytest.fixture(scope="module")
def tuner(module_npu_runtime):
    """The designs narrowed and packed by the cost table `tune` measured on
    this device, or as they resolve where it has measured none.
    """
    table = PROFILES / f"costs_{aie_utils.ensure_current_device().name}.json"
    return JointNarrowing(CostTable(table)) if table.exists() else None


@pytest.fixture(scope="module")
def oracle(weights):
    return EmbeddingGemmaOracle(Config(), weights)


@pytest.fixture(scope="module")
def audio_oracle(weights):
    return AudioOracle(AudioConfig(), weights)


@pytest.fixture(scope="module")
def vision_oracle(weights):
    return VisionOracle(VisionConfig(), weights)


@pytest.fixture(scope="module")
def hugging_face():
    """Hugging Face's outputs on the tests' inputs, each part's under its name."""
    out = {}
    for part, path in REFERENCES.items():
        with np.load(path) as saved:
            out |= {f"{part}/{k}": v for k, v in saved.items() if k != "metadata"}
    return out


def loaded(graph, tuner, boundaries=None):
    """`graph` compiled and loaded for a fixture's tests, then released."""
    yield graph.load(tuner, boundaries)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def check_mixed(graph, oracle, audio_oracle, vision_oracle, case, record_property):
    """The embedding of `MIXED[case]` against the oracle fed its own towers'
    soft tokens.
    """
    text, audio, image = MIXED[case]
    c = graph.config
    got = graph.embed(text, "query", audio=audio, image=image)
    soft = {}
    if audio is not None:
        soft[c.audio_token] = audio_oracle.embed(audio)
    if image is not None:
        soft[c.image_token] = vision_oracle.embed(image, I)
    tokens = graph.tokenizer.encode(
        text,
        "query",
        len(soft.get(c.audio_token, ())),
        len(soft.get(c.image_token, ())),
    )
    similarity = cosine(got, oracle.encode(tokens, soft=soft))
    record_property("Cosine", similarity)
    record_property("Norm", float(np.linalg.norm(got)))
    assert similarity >= MIN_COSINE_MIXED, similarity
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)


@pytest.mark.supported_devices("npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of an xclbin, the
    towers' included.
    """

    @pytest.fixture(scope="class")
    def each_step(self, weights, tokenizer):
        yield from loaded(
            Multimodal(Config(), weights, tokenizer), None, iron.each_step
        )

    @pytest.mark.parametrize(
        "text,task",
        [(QUERY, "query"), (LONGER, "document")],
        ids=["query", "past_the_window"],
    )
    def test_embeddinggemma_2_each_step_accuracy(
        self, each_step, oracle, text, task, record_property
    ):
        tokens = each_step.tokenizer.encode(text, task)
        got = each_step.encode(tokens)
        similarity = cosine(got, oracle.encode(tokens))
        record_property("Cosine", similarity)
        assert similarity >= MIN_COSINE, similarity
        np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)
        np.testing.assert_array_equal(each_step.encode(tokens), got)

    def test_embeddinggemma_2_each_step_multimodal(
        self, each_step, oracle, audio_oracle, vision_oracle, record_property
    ):
        check_mixed(
            each_step, oracle, audio_oracle, vision_oracle, "both", record_property
        )


class Features(iron.Graph):
    """The audio tower's features of a waveform, and the frame after them."""

    def __init__(self, tower: AudioTower):
        self.audio = tower

    def body(self, wave, *, frames: Scratchpad[np.int32]):
        self.audio.logmel(wave, frames)
        hop = self.audio.config.hop
        return Copy(self.audio.features[1 : wave.shape[0] // hop + 1])


@pytest.mark.supported_devices("npu1", "npu2")
class TestAudio:
    """The audio tower alone."""

    @pytest.fixture(scope="class")
    def audio(self, weights, tuner):
        yield from loaded(AudioTower(AudioConfig(), weights), tuner)

    @pytest.mark.parametrize("name", list(CLIPS))
    def test_audio_features(self, audio, audio_oracle, name, record_property):
        wave = clip(name)
        x, values = audio.inputs(wave)
        frames = values["frames"]
        got = Features(audio)(x, frames=frames).numpy().astype(np.float32)
        got = got.reshape(-1, audio.config.mels)
        host, valid = audio_oracle.features(wave)
        assert frames == valid
        want = host[:frames].astype(bfloat16).astype(np.float32)
        exact = float(np.mean(got[:frames] == want))
        ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(1e-30))) - 7)
        record_property("Exact", exact)
        assert exact >= AUDIO_MIN_EXACT, exact
        assert (np.abs(got[:frames] - want) <= np.maximum(ulp, AUDIO_ATOL)).all()
        assert not got[frames].any()

    # Longest first: each clip runs over the rows a longer one left behind.
    @pytest.mark.parametrize("name", list(CLIPS)[::-1])
    def test_audio_accuracy(self, audio, audio_oracle, name, record_property):
        wave = clip(name)
        got, want = audio.embed(wave), audio_oracle.embed(wave)
        c = audio.config
        assert got.shape == want.shape
        assert got.shape == (c.tokens(c.frames(wave.size)), c.text_dim)
        cosines = (got * want).sum(-1) / (
            np.linalg.norm(got, axis=-1) * np.linalg.norm(want, axis=-1)
        )
        error = float(np.linalg.norm(got - want) / np.linalg.norm(want))
        record_property("Cosine", float(cosines.min()))
        record_property("Relative error", error)
        assert cosines.min() >= AUDIO_MIN_COSINE, cosines.min()
        assert error <= AUDIO_MAX_ERROR, error

    @pytest.mark.bench
    @pytest.mark.parametrize("name", list(CLIPS))
    def test_audio_latency(self, audio, name, record_property):
        latency = run_iters(audio.embed, clip(name), warmup=1, iters=10).e2e
        record_property("Latency", latency.median_us)


@pytest.mark.supported_devices("npu1", "npu2")
class TestVision:
    """The vision tower alone, and its image processor alone: a graph the
    tower calls in its body, compiled here on its own.
    """

    @pytest.fixture(scope="class")
    def vision(self, weights, tuner):
        yield from loaded(VisionTower(VisionConfig(), weights), tuner)

    @pytest.fixture(scope="class")
    def processor(self, vision):
        (shapes,) = vision.shapes()
        vision.processor.compile(**shapes)
        return vision.processor

    def check_processor(self, vision, processor, oracle, shape, tokens, record):
        image = synthetic_image(*shape)
        rgb, values = vision.inputs(image, tokens)
        values.pop("n")
        want = oracle.windows(*oracle.patches(image, tokens), vision.config.patches)
        got = processor(rgb, **values)
        for name, g, w in zip(("pixels", "xy", "position_ids"), got, want):
            g = np.asarray(g.numpy()).reshape(w.shape)
            np.testing.assert_array_equal(
                g.view(np.uint8), w.view(np.uint8), err_msg=name
            )
        times = []
        for _ in range(5):
            t = time.perf_counter()
            processor(rgb, **values)
            times.append(time.perf_counter() - t)
        record("Latency", min(times) * 1e6)

    @pytest.mark.parametrize(
        "shape, tokens",
        [
            *IMAGES.values(),
            *((shape, tokens) for shape, tokens, refusal in RESIZES if not refusal),
            # The largest image a call takes, the other way up.
            (VisionConfig().largest[::-1], I),
        ],
    )
    def test_image_processor(
        self, vision, processor, vision_oracle, shape, tokens, record_property
    ):
        self.check_processor(
            vision, processor, vision_oracle, shape, tokens, record_property
        )

    @pytest.mark.supported_devices("npu2")
    def test_image_processor_npu2_only(
        self, vision, processor, vision_oracle, record_property
    ):
        # 2016 pixels wide at image_tokens: 126 patch columns, 16 a core on
        # npu1's eight cores (test_image_processor_refuses_on_npu1 below) but
        # only 8 a core on npu2's sixteen, which Resample's default holds.
        self.check_processor(
            vision, processor, vision_oracle, (97, 640), I, record_property
        )

    @pytest.mark.parametrize("name", list(IMAGES))
    def test_vision_accuracy(self, vision, vision_oracle, name, record_property):
        (height, width), tokens = IMAGES[name]
        image = synthetic_image(height, width)
        got, want = vision.embed(image, tokens), vision_oracle.embed(image, tokens)
        assert got.shape == want.shape
        cosines = (got * want).sum(-1) / (
            np.linalg.norm(got, axis=-1) * np.linalg.norm(want, axis=-1)
        )
        error = float(np.linalg.norm(got - want) / np.linalg.norm(want))
        record_property("Cosine", float(cosines.min()))
        record_property("Relative error", error)
        assert cosines.min() >= VISION_MIN_COSINE, cosines.min()
        assert error <= VISION_MAX_ERROR, error

    @pytest.mark.bench
    @pytest.mark.parametrize("name", ["image", "video_frame"])
    def test_vision_latency(self, vision, name, record_property):
        (height, width), tokens = IMAGES[name]
        image = synthetic_image(height, width)
        latency = run_iters(vision.embed, image, tokens, warmup=1, iters=10).e2e
        record_property("Latency", latency.median_us)


@pytest.fixture(scope="module")
def encoder(weights, tokenizer, tuner):
    yield from loaded(EmbeddingGemma(Config(), weights, tokenizer), tuner)


@pytest.fixture(scope="module")
def multimodal(weights, tokenizer, tuner):
    yield from loaded(Multimodal(Config(), weights, tokenizer), tuner)


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "text,task",
    [
        (QUERY, "query"),
        (DOCUMENTS[0], "document"),
        (LONG, "document"),
        (LONGER, "document"),
        (LONGEST, "document"),
    ],
    ids=["query", "document", "long_document", "past_the_window", "near_the_limit"],
)
def test_embeddinggemma_2_accuracy(encoder, oracle, text, task, record_property):
    tokens = encoder.tokenizer.encode(text, task)
    got = encoder.encode(tokens)
    similarity = cosine(got, oracle.encode(tokens))
    record_property("Cosine", similarity)
    record_property("Norm", float(np.linalg.norm(got)))
    assert similarity >= MIN_COSINE, similarity
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("dims", [512, 256, 128])
def test_embeddinggemma_2_truncation(encoder, oracle, dims, record_property):
    tokens = encoder.tokenizer.encode(QUERY, "query")
    got = encoder.encode(tokens, dims)
    record_property("Norm", float(np.linalg.norm(got)))
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)
    similarity = cosine(got, oracle.encode(tokens, dims))
    record_property("Cosine", similarity)
    assert similarity >= MIN_COSINE, similarity


@pytest.mark.supported_devices("npu1", "npu2")
def test_embeddinggemma_2_ranking(encoder, oracle):
    query = encoder.embed(QUERY, "query")
    scores = [cosine(encoder.embed(d, "document"), query) for d in DOCUMENTS]
    want_query = oracle.encode(encoder.tokenizer.encode(QUERY, "query"))
    want = [
        cosine(oracle.encode(encoder.tokenizer.encode(d, "document")), want_query)
        for d in DOCUMENTS
    ]
    assert scores[0] > scores[1]
    # Measured: 0.0013 and 0.0009 below the oracle's 0.871 and 0.604.
    np.testing.assert_allclose(scores, want, atol=3e-3)


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("case", MIXED)
def test_embeddinggemma_2_multimodal(
    multimodal, oracle, audio_oracle, vision_oracle, case, record_property
):
    check_mixed(multimodal, oracle, audio_oracle, vision_oracle, case, record_property)


@pytest.mark.supported_devices("npu1", "npu2")
def test_embeddinggemma_2_determinism(multimodal):
    # Interleaved, so that a version reading what another left in the shared
    # arena or state differs from its first call.
    calls = [(LONG, None, None), *MIXED.values()]
    first = [multimodal.embed(t, "query", audio=a, image=i) for t, a, i in calls]
    for _ in range(4):
        for (t, a, i), want in zip(calls, first):
            np.testing.assert_array_equal(
                multimodal.embed(t, "query", audio=a, image=i), want
            )


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.bench
@pytest.mark.parametrize(
    "text", [QUERY, LONG, LONGER], ids=["query", "long_document", "past_the_window"]
)
def test_embeddinggemma_2_latency(encoder, text, record_property):
    tokens = encoder.tokenizer.encode(text, "document")
    latency = run_iters(encoder.encode, tokens, warmup=1, iters=10).e2e
    record_property("Latency", latency.median_us)


@pytest.mark.parametrize(
    "shape, tokens, refusal",
    [
        *((s, t, r) for s, t, r in RESIZES if r),
        # 20 MP: more than the largest image a call takes.
        ((5000, 4000), I, "does not fit"),
    ],
)
def test_image_processor_refuses(npu2, shape, tokens, refusal):
    vision = VisionTower(VisionConfig(), Weights.unread())
    with pytest.raises(ValueError, match=refusal):
        vision.inputs(np.zeros((*shape, 3), np.uint8), tokens)


def test_image_processor_refuses_on_npu1(npu1):
    # 2016 pixels wide at image_tokens: 16 patch columns a core on npu1's
    # eight cores, over the eight Resample's default holds there.
    vision = VisionTower(VisionConfig(), Weights.unread())
    with pytest.raises(ValueError, match="patch columns"):
        vision.inputs(np.zeros((97, 640, 3), np.uint8), I)


@pytest.mark.parametrize("shape, tokens, refusal", RESIZES)
def test_resize_matches_hugging_face(
    hugging_face, vision_oracle, shape, tokens, refusal
):
    image = np.random.default_rng(0).integers(0, 256, (*shape, 3), dtype=np.uint8)
    values, positions = vision_oracle.patches(image, tokens)
    key = f"vision/resize/{shape[0]}x{shape[1]}_{tokens}"
    got = [
        hashlib.sha256(np.ascontiguousarray(values, np.float32)).hexdigest(),
        hashlib.sha256(np.ascontiguousarray(positions, np.int64)).hexdigest(),
    ]
    want = [str(hugging_face[f"{key}/{name}"]) for name in ("pixels", "positions")]
    assert got == want


def test_audio_oracle_matches_hugging_face(hugging_face, audio_oracle):
    got_features, frames = audio_oracle.features(clip("medium"))
    mask = hugging_face["audio/medium/mask"]
    assert frames == int(mask.sum()) and mask[:frames].all()
    # Measured: identical.
    np.testing.assert_allclose(
        got_features, hugging_face["audio/medium/features"], atol=1e-5
    )
    want = hugging_face["audio/medium/soft_tokens"]
    got = audio_oracle.tower(got_features, frames)
    assert got.shape == want.shape
    # Measured: 2.1e-5, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-4
    )


def test_vision_oracle_matches_hugging_face(hugging_face, vision_oracle):
    want = hugging_face["vision/portrait/soft_tokens"]
    (height, width), tokens = IMAGES["portrait"]
    got = vision_oracle.embed(synthetic_image(height, width), tokens)
    # Measured: 2.4e-6, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-5
    )


@pytest.mark.parametrize("case", HUGGING_FACE)
def test_embeddinggemma_2_oracle_matches_hugging_face(
    hugging_face, tokenizer, oracle, audio_oracle, vision_oracle, case
):
    text, task, wave, image = HUGGING_FACE[case]
    c = oracle.config
    soft = {}
    if wave is not None:
        soft[c.audio_token] = audio_oracle.embed(wave)
    if image is not None:
        soft[c.image_token] = vision_oracle.embed(image, I)
    ids = tokenizer.encode(
        text,
        task,
        len(soft.get(c.audio_token, ())),
        len(soft.get(c.image_token, ())),
    )
    assert ids == hugging_face[f"text/{case}/input_ids"].tolist()
    want = hugging_face[f"text/{case}/embedding"]
    got = oracle.encode(ids, soft=soft)
    # Measured: 1.4e-6 at the most, float32's own reordering.
    np.testing.assert_allclose(np.linalg.norm(got - want), 0, atol=1e-5)
