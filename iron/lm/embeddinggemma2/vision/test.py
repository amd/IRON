#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's vision tower on the NPU, from the real checkpoint,
against its float32 oracle, and the oracle once against Hugging Face's;
the image processor on the host against Hugging Face's, and on the NPU bit
for bit against the host's.
"""

import hashlib
import time
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import CostTable, JointNarrowing
from iron.lm import Checkpoint, load_weights
from iron.lm.embeddinggemma2.vision.model import (
    COSTS,
    VISION,
    ImageProcessor,
    Vision,
    layout,
    vision_tensors,
)
from iron.lm.embeddinggemma2.vision.oracle import VisionOracle, patches
from iron.lm.testing import require, weights_dir

DIRECTORY = weights_dir("embeddinggemma-2")
REFERENCES = Path(__file__).with_name("hugging_face.npz")

# Measured at the worst of IMAGES: min cosine 0.9705, relative error 4.0e-2.
# bf16 error grows over 16 layers: HF's own bf16 tower is 0.9973 and 2.3e-2
# off the oracle, the graph's bf16 reference 0.9864 and 2.9e-2.
MIN_COSINE = 0.96
MAX_ERROR = 0.05

# (height, width) of a decoded image, and its soft-token budget.
IMAGES = {
    # 14 x 20 tokens at its own size: the whole image budget, 2520 patches.
    "image": ((672, 960), VISION.image_tokens),
    # Resized to 21 x 12 tokens, 2268 patches: the processor pads 252 of them.
    "portrait": ((960, 576), VISION.image_tokens),
    # 10 x 14 tokens at its own size: a video frame's budget, 1260 patches.
    "video_frame": ((480, 672), VISION.video_tokens),
}

# (height, width) of a decoded image and its soft-token budget: a phone
# photo either way up, up- and downscales, extreme aspect ratios, one side
# unchanged, and an image already at its size.
RESIZES = [
    ((3024, 4032), VISION.image_tokens),
    ((4032, 3024), VISION.image_tokens),
    ((480, 640), VISION.image_tokens),
    ((333, 517), VISION.video_tokens),
    ((1080, 1920), VISION.video_tokens),
    ((97, 2003), VISION.image_tokens),
    ((2003, 97), VISION.video_tokens),
    ((1, 5000), VISION.image_tokens),
    ((17, 23), VISION.video_tokens),
    ((672, 517), VISION.image_tokens),
    ((672, 960), VISION.image_tokens),
]


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


def processed(name: str):
    (height, width), tokens = IMAGES[name]
    return patches(synthetic_image(height, width), tokens, VISION)


class Processor(iron.Graph):
    """The image processor alone, its outputs the tower's inputs."""

    def __init__(self):
        self.processor = ImageProcessor(VISION)

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        return self.processor(rgb, height, width, out_height, out_width)


def processor_reference(image, tokens: int, T: int):
    """The `(pixels, xy, position_ids)` `ImageProcessor` gives in `T` rows:
    the host's patches in pooling-window order, then the padding, which
    looks up each table's last row.
    """
    c, P = VISION, VISION.positions
    values, positions = patches(image, tokens, c)
    real = np.flatnonzero((positions >= 0).all(axis=-1))
    x, y = positions[real].T
    token = x // c.pool + (x.max() + 1) // c.pool * (y // c.pool)
    order = real[np.lexsort((x % c.pool, y % c.pool, token))]
    n = order.size
    x, y = positions[order].T
    pixels = np.zeros((T, 3 * c.patch**2), bfloat16)
    pixels[:n] = values[order]
    xy = np.full(2 * T, P, np.int32)
    xy.reshape(T, 2)[:n] = np.stack([x, y], axis=-1)
    position_ids = np.full(2 * T, 2 * P, np.int32)
    position_ids[:n], position_ids[T : T + n] = x, P + y
    return pixels, xy, position_ids


@pytest.fixture(scope="module")
def processor(module_npu_runtime):
    graph = Processor()
    graph.compile(**graph.processor.shapes())
    yield graph


@pytest.fixture(scope="module")
def weights():
    require(DIRECTORY / "model.safetensors")
    tensors = vision_tensors(Checkpoint(DIRECTORY / "model.safetensors").tensors)
    return load_weights(tensors, layout(VISION), VISION.n_layers)


@pytest.fixture(scope="module")
def oracle(weights):
    return VisionOracle(VISION, weights)


@pytest.fixture(scope="module")
def vision(weights, module_npu_runtime):
    table = COSTS / f"costs_{aie_utils.ensure_current_device().name}.json"
    tuner = JointNarrowing(CostTable(table)) if table.exists() else None
    yield Vision(VISION, weights).load(tuner)


@pytest.fixture(scope="module")
def hugging_face():
    """Hugging Face's image processor over `RESIZES` (the sha256 of its
    float32 pixels and int64 positions) and its tower over `processed("portrait")`,
    as iron/applications/embeddinggemma_2/hugging_face.py saved them.
    """
    with np.load(REFERENCES) as saved:
        return dict(saved)


@pytest.mark.parametrize("shape, tokens", RESIZES)
def test_resize_matches_hugging_face(hugging_face, shape, tokens):
    image = np.random.default_rng(0).integers(0, 256, (*shape, 3), dtype=np.uint8)
    values, positions = patches(image, tokens, VISION)
    key = f"resize/{shape[0]}x{shape[1]}_{tokens}"
    got = [
        hashlib.sha256(np.ascontiguousarray(values, np.float32)).hexdigest(),
        hashlib.sha256(np.ascontiguousarray(positions, np.int64)).hexdigest(),
    ]
    want = [str(hugging_face[f"{key}/{name}"]) for name in ("pixels", "positions")]
    assert got == want


# Up- and downscales, both ways up, the widest and tallest, a 4K photo and
# the largest image a call takes.
PROCESSED = [
    *IMAGES.values(),
    ((3024, 4032), VISION.image_tokens),
    ((333, 517), VISION.video_tokens),
    ((1080, 1920), VISION.video_tokens),
    ((2003, 97), VISION.video_tokens),
    ((17, 23), VISION.video_tokens),
    ((4096, 3072), VISION.image_tokens),
]


def _check_image_processor(shape, tokens, processor, record_property):
    image = synthetic_image(*shape)
    rgb, values = processor.processor.inputs(image, tokens)
    values.pop("n")
    want = processor_reference(image, tokens, processor.processor.patches)
    got = processor(rgb, **values)
    for name, g, w in zip(("pixels", "xy", "position_ids"), got, want):
        g = np.asarray(g.numpy()).reshape(w.shape)
        np.testing.assert_array_equal(g.view(np.uint8), w.view(np.uint8), err_msg=name)
    times = []
    for _ in range(5):
        t = time.perf_counter()
        processor(rgb, **values)
        times.append(time.perf_counter() - t)
    record_property("Latency", min(times) * 1e6)


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("shape, tokens", PROCESSED)
def test_image_processor(processor, shape, tokens, record_property):
    _check_image_processor(shape, tokens, processor, record_property)


@pytest.mark.supported_devices("npu2")
def test_image_processor_npu2_only(processor, record_property):
    # 2016 pixels wide at image_tokens: 126 patch columns, 16 a core on
    # npu1's eight cores (test_image_processor_refuses_on_npu1 below) but
    # only 8 a core on npu2's sixteen, which Resample's default holds.
    _check_image_processor((97, 640), VISION.image_tokens, processor, record_property)


@pytest.mark.parametrize(
    "shape, tokens, refusal",
    [
        # 3648 pixels wide: more patch columns than 16 cores hold.
        ((97, 2003), VISION.image_tokens, "patch columns"),
        ((1, 5000), VISION.image_tokens, "patch columns"),
        # 20 MP: more than the largest image a call takes.
        ((5000, 4000), VISION.image_tokens, "does not fit"),
    ],
)
def test_image_processor_refuses(npu2, shape, tokens, refusal):
    with pytest.raises(ValueError, match=refusal):
        ImageProcessor(VISION).inputs(np.zeros((*shape, 3), np.uint8), tokens)


def test_image_processor_refuses_on_npu1(npu1):
    # 2016 pixels wide at image_tokens: 16 patch columns a core on npu1's
    # eight cores, over the eight Resample's default holds there.
    with pytest.raises(ValueError, match="patch columns"):
        ImageProcessor(VISION).inputs(
            np.zeros((97, 640, 3), np.uint8), VISION.image_tokens
        )


def test_vision_oracle_matches_hugging_face(hugging_face, oracle):
    want = hugging_face["portrait/soft_tokens"]
    got = oracle(*processed("portrait"))
    # Measured: 2.4e-6, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-5
    )


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("name", list(IMAGES))
def test_vision_accuracy(vision, oracle, name, record_property):
    (height, width), tokens = IMAGES[name]
    got = vision.embed(synthetic_image(height, width), tokens)
    want = oracle(*processed(name))
    assert got.shape == want.shape
    cosine = (got * want).sum(-1) / (
        np.linalg.norm(got, axis=-1) * np.linalg.norm(want, axis=-1)
    )
    error = float(np.linalg.norm(got - want) / np.linalg.norm(want))
    record_property("Cosine", float(cosine.min()))
    record_property("Relative error", error)
    assert cosine.min() >= MIN_COSINE, cosine.min()
    assert error <= MAX_ERROR, error


@pytest.mark.bench
@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("name", ["image", "video_frame"])
def test_vision_latency(vision, name, record_property):
    (height, width), tokens = IMAGES[name]
    image = synthetic_image(height, width)
    vision.embed(image, tokens)
    times = []
    for _ in range(10):
        t = time.perf_counter()
        vision.embed(image, tokens)
        times.append(time.perf_counter() - t)
    record_property("Latency", float(np.median(times)) * 1e6)
