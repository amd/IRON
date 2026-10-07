#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's vision tower on the NPU, from the real checkpoint,
against its float32 oracle, and the oracle once against Hugging Face's.
"""

import time

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.common.graph.narrowing import CostTable, JointNarrowing
from iron.lm import Checkpoint, load_weights
from iron.lm.embeddinggemma2.vision.model import (
    COSTS,
    VISION,
    Vision,
    layout,
    vision_tensors,
)
from iron.lm.embeddinggemma2.vision.oracle import VisionOracle, patches
from iron.lm.testing import requires, weights_dir

DIRECTORY = weights_dir("embeddinggemma-2")

pytestmark = requires(DIRECTORY / "model.safetensors")

# Measured at the worst of IMAGES: min cosine 0.9705, relative error 4.0e-2.
# bf16 error grows over 16 layers: HF's own bf16 tower is 0.9973 and 2.3e-2
# off the oracle, the graph's bf16 reference 0.9864 and 2.9e-2.
MIN_COSINE = 0.96
MAX_ERROR = 0.05

# (height, width) in pixels, at the size the processor's resize picks, and
# its soft-token budget.
IMAGES = {
    # 14 x 20 tokens: the whole image budget, 2520 patches.
    "image": ((672, 960), VISION.image_tokens),
    # 20 x 12 tokens, 2160 patches: the processor pads 360 of them.
    "portrait": ((960, 576), VISION.image_tokens),
    # 10 x 14 tokens: a video frame's budget, 1260 patches.
    "video_frame": ((480, 672), VISION.video_tokens),
}


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


@pytest.fixture(scope="module")
def weights():
    tensors = vision_tensors(Checkpoint(DIRECTORY / "model.safetensors").tensors)
    return load_weights(tensors, layout(VISION), VISION.n_layers)


@pytest.fixture(scope="module")
def oracle(weights):
    return VisionOracle(VISION, weights)


@pytest.fixture(scope="module")
def vision(weights):
    yield Vision(VISION, weights).load(JointNarrowing(CostTable(COSTS)))
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def test_vision_oracle_matches_hugging_face(weights, oracle):
    # Optional dependencies: the reference implementation, where installed.
    torch = pytest.importorskip("torch")
    gemma4 = pytest.importorskip("transformers.models.gemma4.modeling_gemma4")
    embedding_gemma2 = pytest.importorskip(
        "transformers.models.embedding_gemma2.modeling_embedding_gemma2"
    )
    transformers = pytest.importorskip("transformers")
    config = transformers.AutoConfig.from_pretrained(DIRECTORY)
    config.vision_config._attn_implementation = "eager"
    tower = gemma4.Gemma4VisionModel(config.vision_config).eval()
    embedder = embedding_gemma2.EmbeddingGemma2MultimodalEmbedder(
        config.vision_config, config.text_config
    ).eval()
    tensors = vision_tensors(Checkpoint(DIRECTORY / "model.safetensors").tensors)
    for module, prefix in ((tower, "vision_tower."), (embedder, "embed_vision.")):
        module.load_state_dict(
            {
                k.removeprefix(prefix): torch.from_numpy(v.astype(np.float32))
                for k, v in tensors.items()
                if k.startswith(prefix)
            }
        )
    values, positions = processed("portrait")
    with torch.no_grad():
        hidden = tower(
            pixel_values=torch.from_numpy(values)[None],
            pixel_position_ids=torch.from_numpy(positions)[None],
        ).last_hidden_state
        want = embedder(hidden).numpy().reshape(-1, VISION.text_dim)
    got = oracle(values, positions)
    # Measured: 2.4e-6, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-5
    )


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("name", list(IMAGES))
def test_vision_accuracy(vision, oracle, name, record_property):
    values, positions = processed(name)
    got, want = vision.embed(values, positions), oracle(values, positions)
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
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("name", ["image", "video_frame"])
def test_vision_latency(vision, name, record_property):
    values, positions = processed(name)
    vision.embed(values, positions)
    times = []
    for _ in range(10):
        t = time.perf_counter()
        vision.embed(values, positions)
        times.append(time.perf_counter() - t)
    record_property("Latency", float(np.median(times)) * 1e6)
