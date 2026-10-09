#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's audio tower on the NPU, from the real checkpoint:
its features against the host extractor's, its soft tokens against its
float32 oracle, and the oracle and the host features once against Hugging
Face's.
"""

import time

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import CostTable, JointNarrowing
from iron.lm import Checkpoint, load_weights
from iron.lm.embeddinggemma2.audio.model import (
    AUDIO,
    COSTS,
    Audio,
    AudioTower,
    LogMel,
    audio_tensors,
    layout,
)
from iron.lm.embeddinggemma2.audio.oracle import AudioOracle
from iron.lm.testing import require, weights_dir
from iron.operators.copy import Copy

DIRECTORY = weights_dir("embeddinggemma-2")

# Seconds of audio: soft tokens, and the version that holds them.
CLIPS = {
    # 50 tokens in the 64-token version.
    "short": 2.0,
    # 183 tokens in the 256-token version.
    "medium": 7.3,
    # 450 tokens in the 512-token version.
    "extended": 18.0,
    # 750 tokens in the 768-token version: the extractor's 30 s cap.
    "long": 30.0,
}

# Measured: 0.99925, 0.99953, 0.99931 and 0.99941 of the features are the
# host extractor's rounded to bf16.
MIN_EXACT = 0.999
# The rest are within one bf16 ulp, bar a log near 0, where the energy's
# relative error is the feature's absolute one: measured 1.9e-6 at most.
ATOL = 4e-6

# Measured: 0.983, 0.779, 0.565 and 0.622 at the worst token (mean 0.996 or
# more), where HF's own bf16 tower reaches 0.861, 0.795, 0.902 and 0.689.
MIN_COSINE = 0.55
# Measured: 0.042, 0.084, 0.072 and 0.074; the tower without its clamps is 0.88.
MAX_ERROR = 0.09


def chirp(seconds: float) -> np.ndarray:
    """A rising chirp under noise, mono at the extractor's sample rate."""
    rng = np.random.default_rng(0)
    n = int(seconds * AUDIO.sample_rate)
    t = np.arange(n) / AUDIO.sample_rate
    wave = 0.5 * np.sin(2 * np.pi * (200 * t + 1800 * t**2 / max(seconds, 1)))
    return (wave + 0.05 * rng.standard_normal(n)).astype(np.float32)


class Features(iron.Graph):
    """The tower's features of a waveform, and the frame after them."""

    def __init__(self, tower: AudioTower):
        self.audio = tower

    def body(self, x, *, frames: Scratchpad[np.int32]):
        self.audio.logmel(x, frames)
        return Copy(self.audio.features[1 : x.shape[0] // AUDIO.hop + 1])


@pytest.fixture(scope="module")
def weights():
    require(DIRECTORY / "model.safetensors")
    tensors = audio_tensors(Checkpoint(DIRECTORY / "model.safetensors").tensors)
    return load_weights(tensors, layout(AUDIO), AUDIO.n_layers)


@pytest.fixture(scope="module")
def oracle(weights):
    return AudioOracle(AUDIO, weights)


@pytest.fixture(scope="module")
def audio(weights):
    table = COSTS / f"costs_{aie_utils.ensure_current_device().name}.json"
    tuner = JointNarrowing(CostTable(table)) if table.exists() else None
    yield Audio(AUDIO, weights).load(tuner)
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
def test_audio_features(audio, name, record_property):
    wave = chirp(CLIPS[name])
    x, _, frames = audio.audio.inputs(wave)
    features = Features(audio.audio)
    got = features(x, frames=frames).numpy().astype(np.float32)
    got = got.reshape(-1, AUDIO.mels)
    host, valid = LogMel(AUDIO)(wave)
    assert frames == valid
    want = host[:frames].astype(bfloat16).astype(np.float32)
    exact = float(np.mean(got[:frames] == want))
    ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(1e-30))) - 7)
    record_property("Exact", exact)
    assert exact >= MIN_EXACT, exact
    assert (np.abs(got[:frames] - want) <= np.maximum(ulp, ATOL)).all()
    assert not got[frames].any()


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("name", list(CLIPS))
def test_audio_accuracy(audio, oracle, name, record_property):
    wave = chirp(CLIPS[name])
    x, frames = LogMel(AUDIO)(wave)
    got, want = audio.embed(wave), oracle(x, frames)
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
    wave = chirp(CLIPS[name])
    audio.embed(wave)
    times = []
    for _ in range(10):
        t = time.perf_counter()
        audio.embed(wave)
        times.append(time.perf_counter() - t)
    record_property("Latency", float(np.median(times)) * 1e6)
