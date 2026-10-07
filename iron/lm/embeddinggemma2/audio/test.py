#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's audio tower on the NPU, from the real checkpoint,
against its float32 oracle, and the oracle and the features once against
Hugging Face's.
"""

import time

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.lm import Checkpoint, load_weights
from iron.lm.embeddinggemma2.audio.model import (
    AUDIO,
    Audio,
    LogMel,
    audio_tensors,
    layout,
)
from iron.lm.embeddinggemma2.audio.oracle import AudioOracle
from iron.lm.testing import requires, weights_dir

DIRECTORY = weights_dir("embeddinggemma-2")

pytestmark = requires(DIRECTORY / "model.safetensors")

# Seconds of audio: soft tokens, and the version that holds them.
CLIPS = {
    # 50 tokens in the 64-token version.
    "short": 2.0,
    # 183 tokens in the 256-token version.
    "medium": 7.3,
    # 750 tokens in the 768-token version: the extractor's 30 s cap.
    "long": 30.0,
}

# Measured: 0.987, 0.831 and 0.594 at the worst token (mean 0.997 or more),
# where HF's own bf16 tower reaches 0.861, 0.834 and 0.655.
MIN_COSINE = 0.55
# Measured: 0.044, 0.070 and 0.076; the tower without its clamps is 0.88.
MAX_ERROR = 0.09


def chirp(seconds: float) -> np.ndarray:
    """A rising chirp under noise, mono at the extractor's sample rate."""
    rng = np.random.default_rng(0)
    n = int(seconds * AUDIO.sample_rate)
    t = np.arange(n) / AUDIO.sample_rate
    wave = 0.5 * np.sin(2 * np.pi * (200 * t + 1800 * t**2 / max(seconds, 1)))
    return (wave + 0.05 * rng.standard_normal(n)).astype(np.float32)


def features(name: str):
    return LogMel(AUDIO)(chirp(CLIPS[name]))


@pytest.fixture(scope="module")
def weights():
    tensors = audio_tensors(Checkpoint(DIRECTORY / "model.safetensors").tensors)
    return load_weights(tensors, layout(AUDIO), AUDIO.n_layers)


@pytest.fixture(scope="module")
def oracle(weights):
    return AudioOracle(AUDIO, weights)


@pytest.fixture(scope="module")
def audio(weights):
    yield Audio(AUDIO, weights).load()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


def test_audio_oracle_matches_hugging_face(oracle):
    # Optional dependencies: the reference implementation, where installed.
    torch = pytest.importorskip("torch")
    transformers = pytest.importorskip("transformers")
    gemma4 = pytest.importorskip("transformers.models.gemma4.modeling_gemma4")
    embedding_gemma2 = pytest.importorskip(
        "transformers.models.embedding_gemma2.modeling_embedding_gemma2"
    )
    config = transformers.AutoConfig.from_pretrained(DIRECTORY)
    # Not eager: there Gemma4AudioAttention inverts the additive float mask
    # create_bidirectional_mask gives it.
    config.audio_config._attn_implementation = "sdpa"
    tower = gemma4.Gemma4AudioModel(config.audio_config).eval()
    embedder = embedding_gemma2.EmbeddingGemma2MultimodalEmbedder(
        config.audio_config, config.text_config
    ).eval()
    tensors = audio_tensors(Checkpoint(DIRECTORY / "model.safetensors").tensors)
    for module, prefix in ((tower, "audio_tower."), (embedder, "embed_audio.")):
        module.load_state_dict(
            {
                k.removeprefix(prefix): torch.from_numpy(v.astype(np.float32))
                for k, v in tensors.items()
                if k.startswith(prefix)
            }
        )
    extractor = transformers.AutoFeatureExtractor.from_pretrained(DIRECTORY)
    wave = chirp(CLIPS["medium"])
    processed = extractor([wave], return_tensors="np")
    want_features = processed["input_features"][0]
    mask = processed["input_features_mask"][0]
    got_features, frames = LogMel(AUDIO)(wave)
    assert frames == int(mask.sum()) and mask[:frames].all()
    # Measured: identical.
    np.testing.assert_allclose(got_features, want_features, atol=1e-5)
    with torch.no_grad():
        out = tower(torch.from_numpy(want_features)[None], torch.from_numpy(mask)[None])
        valid = torch.from_numpy(out.attention_mask[0].numpy())
        want = embedder(out.last_hidden_state)[0][valid].numpy()
    got = oracle(got_features, frames)
    assert got.shape == want.shape
    # Measured: 2.1e-5, float32's own reordering.
    np.testing.assert_allclose(
        np.linalg.norm(got - want) / np.linalg.norm(want), 0, atol=1e-4
    )


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("name", list(CLIPS))
def test_audio_accuracy(audio, oracle, name, record_property):
    x, frames = features(name)
    got, want = audio.embed(x, frames), oracle(x, frames)
    assert got.shape == want.shape == (AUDIO.tokens(frames), AUDIO.text_dim)
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
@pytest.mark.parametrize("name", list(CLIPS))
def test_audio_latency(audio, name, record_property):
    x, frames = features(name)
    audio.embed(x, frames)
    times = []
    for _ in range(10):
        t = time.perf_counter()
        audio.embed(x, frames)
        times.append(time.perf_counter() - t)
    record_property("Latency", float(np.median(times)) * 1e6)
