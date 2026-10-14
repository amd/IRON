#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 on the NPU, from the real checkpoint, against its
float32 oracles: the text encoder's embeddings (their cosine to the
oracle's, their norm, a query ranking two documents, every call
bit-identical to the first), each tower's soft tokens and, over text with
a clip and an image, the whole model's. The audio tower's features and the
image processor's patches are checked against the host's, which the
oracles take. The oracles are checked against Hugging Face's processors
and model (hugging_face.py), where torch is installed. On NPU1 each step is
its own dispatch of an xclbin; on NPU2 that form is checked too.

Each tower's graph is built for the class that tests it and dropped after
it, before the text encoder's graphs are built for the module's last tests.
"""

import tarfile
import time

import aie.utils as aie_utils
import numpy as np
import pytest
import soundfile
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16
from PIL import Image

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
from iron.lm import prompt_text
from iron.lm.testing import Download, cache_dir, require, weights_dir
from iron.operators.copy import Copy

DIRECTORY = weights_dir("embeddinggemma-2")
CACHE = cache_dir()

QUERY = "What causes the northern lights?"
DOCUMENTS = [
    "The northern lights are caused by charged particles from the sun.",
    "Photosynthesis converts light energy into chemical energy in plants.",
]
# The library's shared text: 357 tokens as a document.
LONG = prompt_text(1200)
# 984 tokens, past the sliding window.
LONGER = prompt_text(3500)
# 1960 tokens, near the encoder's 2048.
LONGEST = prompt_text(7000)

# Measured: 0.99986 at the least, where HF's own bf16 model is 0.99997.
MIN_COSINE = 0.9995
# Against the oracle fed its own towers' soft tokens, so the towers' error is in
# it. Measured: 0.99986 with an image, as the text alone.
MIN_COSINE_MIXED = 0.9995
# A unit vector rounded to bf16 is up to 2**-9 off in norm, and the device's
# reaches it.
NORM_RTOL = 2**-8

# Measured on chirps: 0.99925, 0.99953, 0.99931 and 0.99941 of the features
# are the host extractor's rounded to bf16.
AUDIO_MIN_EXACT = 0.999
# The rest are within one bf16 ulp, bar a log near 0, where the energy's
# relative error is the feature's absolute one: measured 1.9e-6 at most.
AUDIO_ATOL = 4e-6
# The 1st percentile of the token cosines, not the worst token: the last layer
# is ill-conditioned at a few tokens, where HF's own float32 model turns the
# NPU's 11-layer state, within 0.9995 of its own there, into 0.74. Measured
# on npu2 over CLIPS: 0.9991, 0.9929, 0.9994, 0.9984 and 0.9982, relative
# error 0.021, 0.038, 0.018, 0.047 and 0.037; HF's own bf16 tower against its
# float32 one: 0.9992, 0.9933, 0.9958, 0.9996 and 0.9990, and 0.015, 0.027,
# 0.043, 0.013 and 0.016. vtanh's Tanh, in the soft cap, reached 0.082.
AUDIO_MIN_COSINE = 0.99
AUDIO_MAX_ERROR = 0.06

# Measured on npu2 at the worst token of IMAGES: min cosine 0.9745, 0.9633
# and 0.9801, relative error 4.4e-2, 4.8e-2 and 5.3e-2. bf16 error grows
# over 16 layers: HF's own bf16 tower is 0.9684, 0.9673 and 0.9924, and
# 3.4e-2, 4.0e-2 and 4.1e-2, off its float32 one on the same photos.
VISION_MIN_COSINE = 0.95
VISION_MAX_ERROR = 0.06

# LibriSpeech's test-clean (CC BY 4.0, V. Panayotov et al., 2015), as openslr
# publishes it, fetched once into IRON's cache.
LIBRISPEECH = Download(
    "https://www.openslr.org/resources/12/test-clean.tar.gz",
    "39fde525e59672dc6d1551919b1478f724438a95aa55f874b576be21967e6c23",
)

# Utterances of it, 16 kHz mono, by the soft tokens they give.
CLIPS = {
    # 2.0 s, 50 tokens: "Won't you tell Douglas".
    "short": "121-127105-0021",
    # 7.3 s, 183 tokens.
    "medium": "4446-2275-0016",
    # 13.0 s, 325 tokens.
    "passage": "2094-142345-0014",
    # 18.0 s, 450 tokens.
    "extended": "3729-6852-0017",
    # 35.0 s, 750 tokens: past the extractor's 30 s cap, which truncates it.
    "long": "4507-16021-0047",
}

I, V = VisionConfig().image_tokens, VisionConfig().video_tokens

VAL2017 = "https://s3.amazonaws.com/images.cocodataset.org/val2017"

# COCO val2017 photos, fetched into IRON's cache.
COCO = {
    # 640x480.
    "cats": Download(
        f"{VAL2017}/000000039769.jpg",
        "dea9e7ef97386345f7cff32f9055da4982da5471c48d575146c796ab4563b04e",
    ),
    # 375x500, portrait.
    "stop_sign": Download(
        f"{VAL2017}/000000000724.jpg",
        "5c0e559c75d3969c8e3e297b61f61063f78045c9d4802b526ba616361f3823fd",
    ),
    # 640x426.
    "living_room": Download(
        f"{VAL2017}/000000000139.jpg",
        "ffe0f0cec3b2e27aab1967229cdf0a0d7751dcdd5800322f0b8ac0dffb3b8a8d",
    ),
    # 621x640: the image of the text encoder's cases.
    "baseball": Download(
        f"{VAL2017}/000000000872.jpg",
        "c2aa138ee3a59b057a7ba6fc5a6a18e62af531aa7dab78a7bfd33c1cd7e55eb6",
    ),
}

# The vision tower's photos and the soft-token budget each is resized to.
IMAGES = {
    # 14 x 19 tokens, 2394 patches: an upscale to nearly the whole budget.
    "cats": I,
    # 19 x 14 tokens, the other way up.
    "stop_sign": I,
    # 9 x 14 tokens, 1134 patches: a video frame's budget.
    "living_room": V,
}

# The resizes the image processor is checked on, against Hugging Face's and
# on the NPU, the cats photo tiled to each (height, width), with its budget
# and what the NPU's refuses it for: a phone photo either way up, up- and
# downscales, extreme aspect ratios, one side unchanged, and an image
# already at its size.
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


def clip(name: str) -> np.ndarray:
    """The utterance `CLIPS[name]`, its FLAC member taken from the archive
    in IRON's cache the first time, decoded: float32 samples in
    [-1, 1) at the extractor's sample rate.
    """
    speaker, chapter, _ = CLIPS[name].split("-")
    member = f"LibriSpeech/test-clean/{speaker}/{chapter}/{CLIPS[name]}.flac"
    path = CACHE / member
    if not path.exists():
        with tarfile.open(LIBRISPEECH.fetch()) as archive:
            data = archive.extractfile(member).read()
        path.parent.mkdir(parents=True, exist_ok=True)
        # Renamed into place, so an interrupted extraction leaves no clip.
        partial = path.with_suffix(".part")
        partial.write_bytes(data)
        partial.replace(path)
    samples, rate = soundfile.read(path, dtype="float32")
    if samples.ndim != 1 or rate != AudioConfig().sample_rate:
        raise ValueError(f"{name}: not mono at the extractor's rate")
    return samples


def photo(name: str) -> np.ndarray:
    """`COCO[name]`, fetched into IRON's cache and decoded:
    `(height, width, 3)` uint8.
    """
    with Image.open(COCO[name].fetch()) as image:
        return np.array(image.convert("RGB"))


def tiled(image: np.ndarray, height: int, width: int) -> np.ndarray:
    """`image` repeated to `(height, width, 3)`: a photo's content at any shape."""
    reps = (-(-height // image.shape[0]), -(-width // image.shape[1]), 1)
    return np.tile(image, reps)[:height, :width]


# Text with a clip and the baseball photo (16 x 16 tokens) at its
# placeholders, each a mixed call's text, clip and photo.
MIXED = {
    "audio": ("<|audio|> someone reading aloud", "short", None),
    "image": ("<|image|> a baseball game", None, "baseball"),
    "both": ("<|image|> the picture, then the speech: <|audio|>", "short", "baseball"),
    # 325 soft tokens of audio and an image's.
    "long_clip_and_image": (
        "<|image|> the picture, then the speech: <|audio|>",
        "passage",
        "baseball",
    ),
}

# The cases the oracle's ids and embedding are checked against Hugging
# Face's processor and model on: text, and text with a clip and a photo.
HUGGING_FACE = {
    "query": (QUERY, "query", None, None),
    "past_the_window": (LONGER, "document", None, None),
    "audio": ("<|audio|> someone reading aloud", "query", "short", None),
    "image": ("<|image|> a baseball game", "query", None, "baseball"),
    "both": (
        "<|image|> the picture, then the speech: <|audio|>",
        "query",
        "short",
        "baseball",
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
    """The designs narrowed and packed by the cost table `iron.lm.tune`
    measured on this device, or as they resolve where it has measured none.
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


@pytest.fixture(scope="session")
def hugging_face():
    """Hugging Face's own EmbeddingGemma 2, which the oracles are checked
    against: optional dependencies, so its tests skip without them.
    """
    for module in ("torch", "torchvision", "transformers"):
        pytest.importorskip(module)
    require(DIRECTORY / "model.safetensors", DIRECTORY / "processor_config.json")
    # Imported here, once the optional dependencies are known to be present.
    from iron.applications.embedding_gemma2.hugging_face import HuggingFace

    return HuggingFace(DIRECTORY)


def loaded(graph, tuner, boundaries=None):
    """`graph` compiled and loaded for a fixture's tests, then released."""
    yield graph.load(tuner, boundaries)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def check_mixed(graph, oracle, audio_oracle, vision_oracle, case, record_property):
    """The embedding of `MIXED[case]` against the oracle fed its own towers'
    soft tokens.
    """
    text, speech, name = MIXED[case]
    audio = None if speech is None else clip(speech)
    image = None if name is None else photo(name)
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
        percentile = float(np.percentile(cosines, 1))
        record_property("Cosine", percentile)
        record_property("Worst cosine", float(cosines.min()))
        record_property("Relative error", error)
        assert percentile >= AUDIO_MIN_COSINE, percentile
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

    def check_processor(self, vision, processor, oracle, image, tokens, record):
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
        "name, shape, tokens",
        [
            *((name, None, tokens) for name, tokens in IMAGES.items()),
            *(("cats", s, tokens) for s, tokens, refusal in RESIZES if not refusal),
            # The largest image a call takes, the other way up.
            ("cats", VisionConfig().largest[::-1], I),
        ],
    )
    def test_image_processor(
        self, vision, processor, vision_oracle, name, shape, tokens, record_property
    ):
        image = photo(name) if shape is None else tiled(photo(name), *shape)
        self.check_processor(
            vision, processor, vision_oracle, image, tokens, record_property
        )

    @pytest.mark.supported_devices("npu2")
    def test_image_processor_npu2_only(
        self, vision, processor, vision_oracle, record_property
    ):
        # 2016 pixels wide at image_tokens: 126 patch columns, 16 a core on
        # npu1's eight cores (test_image_processor_refuses_on_npu1 below) but
        # only 8 a core on npu2's sixteen, which Resample's default holds.
        image = tiled(photo("cats"), 97, 640)
        self.check_processor(
            vision, processor, vision_oracle, image, I, record_property
        )

    @pytest.mark.parametrize("name", list(IMAGES))
    def test_vision_accuracy(self, vision, vision_oracle, name, record_property):
        image, tokens = photo(name), IMAGES[name]
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
    @pytest.mark.parametrize("name", ["cats", "living_room"])
    def test_vision_latency(self, vision, name, record_property):
        image, tokens = photo(name), IMAGES[name]
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
    calls = [
        (
            t,
            None if speech is None else clip(speech),
            None if name is None else photo(name),
        )
        for t, speech, name in [(LONG, None, None), *MIXED.values()]
    ]
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
    image = tiled(photo("cats"), *shape)
    got_values, got_positions = vision_oracle.patches(image, tokens)
    want_values, want_positions = hugging_face.patches(image, tokens)
    np.testing.assert_array_equal(got_values, want_values)
    np.testing.assert_array_equal(got_positions, want_positions)


def test_audio_oracle_matches_hugging_face(hugging_face, audio_oracle):
    wave = clip("medium")
    got_features, frames = audio_oracle.features(wave)
    want_features, mask = hugging_face.features(wave)
    assert frames == int(mask.sum()) and mask[:frames].all()
    # Measured: identical.
    np.testing.assert_allclose(got_features, want_features, atol=1e-5)
    want = hugging_face.audio_tower(want_features, mask)
    got = audio_oracle.tower(got_features, frames)
    assert got.shape == want.shape
    # Measured: 2.1e-5, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-4
    )


def test_vision_oracle_matches_hugging_face(hugging_face, vision_oracle):
    pixel_values, positions = vision_oracle.patches(
        photo("stop_sign"), IMAGES["stop_sign"]
    )
    want = hugging_face.vision_tower(pixel_values, positions)
    got = vision_oracle.tower(pixel_values, positions)
    # Measured: 2.4e-6, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-5
    )


@pytest.mark.parametrize("case", HUGGING_FACE)
def test_embeddinggemma_2_oracle_matches_hugging_face(
    hugging_face, tokenizer, oracle, audio_oracle, vision_oracle, case
):
    text, task, speech, name = HUGGING_FACE[case]
    wave = None if speech is None else clip(speech)
    image = None if name is None else photo(name)
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
    want_ids, want = hugging_face.encode(Tokenizer.TASKS[task] + text, wave, image)
    assert ids == want_ids
    got = oracle.encode(ids, soft=soft)
    # Measured: 1.4e-6 at the most, float32's own reordering.
    np.testing.assert_allclose(np.linalg.norm(got - want), 0, atol=1e-5)
