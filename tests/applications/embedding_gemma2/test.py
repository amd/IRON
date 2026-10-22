# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 on the NPU, from the real checkpoint, against Hugging
Face's own processors and model in float32 (hugging_face.py), their outputs
recorded in ``golden.npz`` beside the checkpoint: the text encoder's
embeddings (their cosine to Hugging Face's, their norm, a query ranking two
documents, every call bit-identical to the first), each tower's soft tokens
and, over text with a clip and an image, the whole model's, and the audio
tower's features and the image processor's patches. On NPU1 each step is
its own dispatch of an xclbin; on NPU2 that form is checked too.

Each tower's graph is built for the class that tests it and dropped after
it, before the text encoder's graphs are built for the module's last tests.
"""

import functools
import time
from types import SimpleNamespace

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.benchmark import run_iters
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.applications.embedding_gemma2.model import (
    PROFILES,
    Config,
    EmbeddingGemma,
    Multimodal,
    TextProcessor,
)
from iron.applications.gemma4.audio import AudioConfig, AudioTower
from iron.applications.gemma4.vision import VisionConfig, VisionTower
from iron.lm import Checkpoint, rope_angles
from iron.lm.model import prompt_text
from iron.lm.golden import Golden
from iron.lm.testing import Download, check_embedding, require, weights_dir
from iron.operators.copy import Copy
from iron.tests.support.librispeech import utterance

DIRECTORY = weights_dir("embeddinggemma-2")

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
# Against Hugging Face's whole model, so the towers' error is in it. Measured:
# 0.99986 with an image, as the text alone.
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
# on npu2 over CLIPS before S21a's float32 scores and band (pr222/s21a-mask.md):
# 0.9991, 0.9929, 0.9994, 0.9984 and 0.9982, relative error 0.021, 0.038,
# 0.018, 0.047 and 0.037; HF's own bf16 tower against its float32 one: 0.9992,
# 0.9933, 0.9958, 0.9996 and 0.9990, and 0.015, 0.027, 0.043, 0.013 and 0.016.
# vtanh's Tanh, in the soft cap, reached 0.082.
# After S21a (simplify/p2-s21a, ae20edc09): 0.9994, 0.9950, 0.9985, 0.9990 and
# 0.9994 -- medium improves the most (0.9929 -> 0.9950) and is still the
# worst of the five; passage alone moves the wrong way (0.9994 -> 0.9985), by
# less than the others gain, within the same ill-conditioning this comment
# already describes (a specific token's content, not the path). The bound
# tightens to the new worst (medium), the same margin the old one carried.
# Relative error not remeasured this round, so AUDIO_MAX_ERROR stays as is.
AUDIO_MIN_COSINE = 0.992
AUDIO_MAX_ERROR = 0.06

# Measured on npu2 at the worst token of IMAGES: min cosine 0.9745, 0.9633
# and 0.9801, relative error 4.4e-2, 4.8e-2 and 5.3e-2. bf16 error grows
# over 16 layers: HF's own bf16 tower is 0.9684, 0.9673 and 0.9924, and
# 3.4e-2, 4.0e-2 and 4.1e-2, off its float32 one on the same photos.
VISION_MIN_COSINE = 0.95
VISION_MAX_ERROR = 0.06

# Utterances of LibriSpeech's test-clean (``librispeech``), 16 kHz mono, by the soft tokens they give.
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

# The processor's soft-token budgets for an image and for video.
I, V = VisionConfig().image_tokens, 140

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

# The resizes the image processor is checked on, the cats photo tiled to
# each (height, width), with its budget and what the NPU's refuses it for: a
# phone photo either way up, up- and downscales, extreme aspect ratios, one
# side unchanged, and an image already at its size.
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
    """The utterance `CLIPS[name]`, at the extractor's sample rate."""
    return utterance(CLIPS[name])


def photo(name: str) -> np.ndarray:
    """`COCO[name]`, fetched into IRON's cache and decoded:
    `(height, width, 3)` uint8.
    """
    from PIL import Image

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


@pytest.fixture(scope="module")
def weights():
    require(DIRECTORY / "model.safetensors")
    return Checkpoint(DIRECTORY / "model.safetensors").tree()


@pytest.fixture(scope="module")
def tokenizer():
    require(DIRECTORY / "tokenizer.json")
    return TextProcessor(DIRECTORY / "tokenizer.json")


@pytest.fixture(scope="module")
def reference():
    """``reference(key, compute)``: ``compute(model)`` on Hugging Face's own
    EmbeddingGemma 2 (hugging_face.py), an array kept under ``key`` in
    ``golden.npz`` beside the checkpoint, recorded under ``pytest
    --record-goldens`` (torch, torchvision and transformers installed) and
    refused once the checkpoint's ``config.json`` or tensors change.
    """

    @functools.cache
    def model():
        from iron.applications.embedding_gemma2.hugging_face import HuggingFace

        return HuggingFace(DIRECTORY)

    @functools.cache
    def inputs():
        checkpoint = Checkpoint(DIRECTORY / "model.safetensors")
        return (DIRECTORY / "config.json").read_text(), checkpoint.fingerprint()

    def recorded(key, compute):
        record = lambda: SimpleNamespace(
            logits=lambda _: compute(model())
        )  # noqa: E731
        golden = Golden(DIRECTORY / "golden.npz", record, inputs())
        return golden.logits(np.frombuffer(key.encode(), np.uint8))

    return recorded


def embedding(reference, text, task, speech=None, name=None, dims=None):
    """Hugging Face's embedding of ``text`` for ``task`` with the clip
    ``speech`` and the photo ``name`` at its placeholders, its first
    ``dims`` renormalized.
    """
    e = reference(
        f"embedding {task} {speech} {name} {text}",
        lambda model: model.encode(
            TextProcessor.TASKS[task] + text,
            None if speech is None else clip(speech),
            None if name is None else photo(name),
        ),
    )[:dims]
    return e / np.linalg.norm(e)


def windows(config, pixel_values, positions):
    """The processor's patches as the NPU's ``iron.lm.ImagePatches`` gives
    them in ``config.patches`` rows: each soft token's ``pool ** 2``
    patches together, row-major within their window, the tokens row-major
    over the image, then padding, ids past each table.

    Returns:
        ``pixels`` ``(rows, 3 * patch ** 2)`` bf16; ``xy`` ``(2 * rows,)``
        int32, each patch's x and y side by side; and ``position_ids``
        ``(2 * rows,)`` int32, every patch's x, then every patch's y plus
        ``positions``.
    """
    c, P, rows = config, config.position_embedding_size, config.patches
    real = np.flatnonzero((positions >= 0).all(axis=-1))
    x, y = positions[real].T
    token = x // c.pooling_kernel_size + (x.max() + 1) // c.pooling_kernel_size * (
        y // c.pooling_kernel_size
    )
    order = real[
        np.lexsort((x % c.pooling_kernel_size, y % c.pooling_kernel_size, token))
    ]
    n = order.size
    x, y = positions[order].T
    pixels = np.zeros((rows, 3 * c.patch_size**2), bfloat16)
    pixels[:n] = pixel_values[order]
    xy = np.full(2 * rows, P, np.int32)
    xy.reshape(rows, 2)[:n] = np.stack([x, y], axis=-1)
    position_ids = np.full(2 * rows, 2 * P, np.int32)
    position_ids[:n], position_ids[rows : rows + n] = x, P + y
    return pixels, xy, position_ids


def loaded(graph, full_elf=None):
    """`graph` compiled and loaded for a fixture's tests, then released."""
    yield graph.load_versions(full_elf=full_elf)
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def check_mixed(graph, reference, case, record_property):
    """The embedding of `MIXED[case]` against Hugging Face's."""
    text, speech, name = MIXED[case]
    audio = None if speech is None else clip(speech)
    image = None if name is None else photo(name)
    got = graph.embed(text, "query", audio=audio, image=image)
    similarity = cosine(got, embedding(reference, text, "query", speech, name))
    record_property("Cosine", similarity)
    record_property("Norm", float(np.linalg.norm(got)))
    assert similarity >= MIN_COSINE_MIXED, similarity
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
class TestEachStep:
    """The form NPU1 runs: each step its own dispatch of an xclbin, the
    towers' included.
    """

    @pytest.fixture(scope="class")
    def each_step(self, weights, tokenizer):
        yield from loaded(Multimodal(Config(), weights, tokenizer), False)

    @pytest.mark.parametrize(
        "text,task",
        [(QUERY, "query"), (LONGER, "document")],
        ids=["query", "past_the_window"],
    )
    def test_embeddinggemma_2_each_step_accuracy(
        self, each_step, reference, text, task, record_property
    ):
        tokens = each_step.tokenizer.encode(text, task)
        got = each_step.encode(tokens)
        similarity = cosine(got, embedding(reference, text, task))
        record_property("Cosine", similarity)
        assert similarity >= MIN_COSINE, similarity
        np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)
        np.testing.assert_array_equal(each_step.encode(tokens), got)

    def test_embeddinggemma_2_each_step_multimodal(
        self, each_step, reference, record_property
    ):
        check_mixed(each_step, reference, "both", record_property)


class Features(iron.Graph):
    """The audio tower's features of a waveform, and the frame after them."""

    def __init__(self, tower: AudioTower):
        self.audio = tower

    def body(self, wave, *, frames: Scratchpad[np.int32]):
        self.audio.logmel(wave, frames)
        hop = self.audio.config.hop
        return Copy.step(self.audio.features[1 : wave.shape[0] // hop + 1])


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
class TestAudio:
    """The audio tower alone."""

    @pytest.fixture(scope="class")
    def audio(self, weights):
        tower = AudioTower(AudioConfig(), weights)
        # EmbeddingGemma 2's tuning, which its towers take inlined.
        tower.profile = PROFILES
        yield from loaded(tower)

    @pytest.mark.parametrize("name", list(CLIPS))
    def test_audio_features(self, audio, reference, name, record_property):
        wave = clip(name)
        x, values = audio.inputs(wave)
        frames = values["frames"]
        got = Features(audio)(x, frames=frames).numpy().reshape(-1, audio.config.mels)
        want = reference(f"features {name}", lambda model: model.features(wave))
        assert frames == len(want)
        want = want.astype(bfloat16)
        exact = float(
            np.mean(got[:frames].astype(np.float32) == want.astype(np.float32))
        )
        record_property("Exact", exact)
        assert exact >= AUDIO_MIN_EXACT, exact
        verdict = compare(got[:frames], want, Tolerance(ulps=1, atol=AUDIO_ATOL))
        assert verdict, verdict.detail
        assert not got[frames].any()

    # Longest first: each clip runs over the rows a longer one left behind.
    @pytest.mark.parametrize("name", list(CLIPS)[::-1])
    def test_audio_accuracy(self, audio, reference, name, record_property):
        wave = clip(name)
        got = audio.soft_tokens(wave)
        want = reference(f"audio {name}", lambda model: model.audio_tower(wave))
        c = audio.config
        assert got.shape == want.shape
        assert got.shape == (c.tokens(c.frames(wave.size)), c.text_dim)
        check_embedding(
            got, want, AUDIO_MIN_COSINE, AUDIO_MAX_ERROR, record=record_property
        )

    @pytest.mark.bench
    @pytest.mark.parametrize("name", list(CLIPS))
    def test_audio_latency(self, audio, name, record_property):
        latency = run_iters(audio.soft_tokens, clip(name), warmup=1, iters=10).e2e
        record_property("Latency", latency.median_us)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
class TestVision:
    """The vision tower alone, and its image processor alone: a graph the
    tower calls in its body, compiled here on its own.
    """

    @pytest.fixture(scope="class")
    def vision(self, weights):
        tower = VisionTower(VisionConfig(), weights)
        # EmbeddingGemma 2's tuning, which its towers take inlined.
        tower.profile = PROFILES
        yield from loaded(tower)

    @pytest.fixture(scope="class")
    def processor(self, vision):
        (shapes,) = vision.shapes()
        vision.processor.compile(**shapes)
        return vision.processor

    def check_processor(self, vision, processor, reference, key, image, tokens, record):
        rgb, values = vision.inputs(image, tokens)
        # The tower's per-call values, not the processor's alone.
        for name in ("n", "hk", "wk", "walked"):
            values.pop(name)
        pixel_values = reference(
            f"pixel_values {key} {tokens}", lambda m: m.patches(image, tokens)[0]
        )
        positions = reference(
            f"positions {key} {tokens}", lambda m: m.patches(image, tokens)[1]
        )
        want = windows(vision.config, pixel_values, positions.astype(np.int64))
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
        self, vision, processor, reference, name, shape, tokens, record_property
    ):
        image = photo(name) if shape is None else tiled(photo(name), *shape)
        self.check_processor(
            vision,
            processor,
            reference,
            f"{name} {shape}",
            image,
            tokens,
            record_property,
        )

    @pytest.mark.supported_devices("npu2")
    def test_image_processor_npu2_only(
        self, vision, processor, reference, record_property
    ):
        # 2016 pixels wide at image_tokens: 126 patch columns, 16 a core on
        # npu1's eight cores (test_image_processor_refuses_on_npu1 below) but
        # only 8 a core on npu2's sixteen, which Resample's default holds.
        image = tiled(photo("cats"), 97, 640)
        self.check_processor(
            vision, processor, reference, "cats (97, 640)", image, I, record_property
        )

    @pytest.mark.parametrize("name", list(IMAGES))
    def test_vision_accuracy(self, vision, reference, name, record_property):
        image, tokens = photo(name), IMAGES[name]
        got = vision.soft_tokens(image, tokens)
        want = reference(
            f"vision {name} {tokens}",
            lambda model: model.vision_tower(*model.patches(image, tokens)),
        )
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
        latency = run_iters(vision.soft_tokens, image, tokens, warmup=1, iters=10).e2e
        record_property("Latency", latency.median_us)


@pytest.fixture(scope="module")
def encoder(weights, tokenizer):
    yield from loaded(EmbeddingGemma(Config(), weights, tokenizer))


@pytest.fixture(scope="module")
def multimodal(weights, tokenizer):
    yield from loaded(Multimodal(Config(), weights, tokenizer))


@pytest.mark.bench
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
def test_embeddinggemma_2_accuracy(encoder, reference, text, task, record_property):
    tokens = encoder.tokenizer.encode(text, task)
    got = encoder.encode(tokens)
    similarity = cosine(got, embedding(reference, text, task))
    record_property("Cosine", similarity)
    record_property("Norm", float(np.linalg.norm(got)))
    assert similarity >= MIN_COSINE, similarity
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("dims", [512, 256, 128])
def test_embeddinggemma_2_truncation(encoder, reference, dims, record_property):
    tokens = encoder.tokenizer.encode(QUERY, "query")
    got = encoder.encode(tokens, dims)
    record_property("Norm", float(np.linalg.norm(got)))
    np.testing.assert_allclose(np.linalg.norm(got), 1, rtol=NORM_RTOL)
    similarity = cosine(got, embedding(reference, QUERY, "query", dims=dims))
    record_property("Cosine", similarity)
    assert similarity >= MIN_COSINE, similarity


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
def test_embeddinggemma_2_ranking(encoder, reference):
    query = encoder.embed(QUERY, "query")
    scores = [cosine(encoder.embed(d, "document"), query) for d in DOCUMENTS]
    want_query = embedding(reference, QUERY, "query")
    want = [cosine(embedding(reference, d, "document"), want_query) for d in DOCUMENTS]
    assert scores[0] > scores[1]
    # Measured: 0.0013 and 0.0009 below Hugging Face's 0.871 and 0.604.
    np.testing.assert_allclose(scores, want, atol=3e-3)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("case", MIXED)
def test_embeddinggemma_2_multimodal(multimodal, reference, case, record_property):
    check_mixed(multimodal, reference, case, record_property)


@pytest.mark.extensive
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


@pytest.mark.extensive
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
    require(DIRECTORY / "model.safetensors")
    vision = VisionTower(
        VisionConfig(), Checkpoint(DIRECTORY / "model.safetensors").tree("unread")
    )
    with pytest.raises(ValueError, match=refusal):
        vision.inputs(np.zeros((*shape, 3), np.uint8), tokens)


class WindowPositions(iron.Graph):
    """`VisionTower.window_positions` alone, on given rows."""

    def __init__(self, tower: VisionTower):
        self.tower = tower

    def body(
        self,
        h,
        *,
        n: Scratchpad[np.int32],
        hk: Scratchpad[np.int32],
        wk: Scratchpad[np.int32],
        walked: Scratchpad[np.int32],
    ):
        tower = self.tower
        h, ropes = tower.inline(
            tower.window_positions, h[:n], n=n, hk=hk, wk=wk, walked=walked
        )
        angles, _ = ropes[tower.config.head_dim]
        return h, Copy.step(angles)


@pytest.mark.parametrize(
    "hk, wk", [(1, 1), (14, 19), (16, 16), (6, 42), (8, 35), (65, 4), (200, 1)]
)
def test_vision_window_positions_are_each_patch_rows(npu2, hk, wk):
    """Each patch in window order gets its x and y position embeddings, each
    add rounded as `ElementwiseAdd` rounds it, and its x and y angles.
    """
    require(DIRECTORY / "model.safetensors")
    weights = Checkpoint(DIRECTORY / "model.safetensors").tree()
    tower = VisionTower(VisionConfig(), weights)
    c = tower.config
    k, n = c.pooling_kernel_size, c.pooling_kernel_size**2 * hk * wk
    rng = np.random.default_rng(hk * 100 + wk)
    h = rng.standard_normal((c.patches, c.hidden_size)).astype(bfloat16)
    got, angles = WindowPositions(tower).reference(
        h, n=n, hk=hk, wk=wk, walked=tower.walked(hk, wk)
    )
    ty, tx, wy, wx = np.indices((hk, wk, k, k)).reshape(4, -1)
    x, y = k * tx + wx, k * ty + wy
    table = weights.vision_tower.patch_embedder.position_embedding_table
    want = h[:n]
    for side in (table[0][x], table[1][y]):
        want = (want.astype(np.float32) + side.astype(np.float32)).astype(bfloat16)
    np.testing.assert_array_equal(
        np.asarray(got)[:n].view(np.uint16), want.view(np.uint16)
    )
    rope = rope_angles(c.head_dim // 2, c.position_embedding_size, c.rope_theta).astype(
        bfloat16
    )
    np.testing.assert_array_equal(
        np.asarray(angles)[:n].view(np.uint16),
        np.concatenate([rope[x], rope[y]], axis=1).view(np.uint16),
    )


def test_image_processor_refuses_on_npu1(npu1):
    # 2016 pixels wide at image_tokens: 16 patch columns a core on npu1's
    # eight cores, over the eight Resample's default holds there.
    require(DIRECTORY / "model.safetensors")
    vision = VisionTower(
        VisionConfig(), Checkpoint(DIRECTORY / "model.safetensors").tree("unread")
    )
    with pytest.raises(ValueError, match="patch columns"):
        vision.inputs(np.zeros((97, 640, 3), np.uint8), I)
