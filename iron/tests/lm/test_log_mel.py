# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.LogMel on a device: one compile at 3072 frames, called at two
frame counts, every 8th frame against Hugging Face's Gemma 4 feature
extractor's float64 features, recorded in ``goldens/``. Then Whisper's,
on the host and on a device, a 30 s clip's every 8th frame against its
``WhisperFeatureExtractor``'s.
"""

import time

import numpy as np
import pytest

import iron
from iron.lm import LogMel
from iron.tests.support.log_mel import EVERY, Extractor, WhisperExtractor, whisper_wave

FRAMES = 3072
# Measured on the host, the operators' references against the extractor:
# 0.99969 of the kept features are its bf16 rounding. Held at FRAMES alone:
# 200 frames keep 3200 features, too few for a rate.
MIN_EXACT = 0.999
# The rest within one bf16 ulp, bar a log near 0, where the energy's
# relative error is the feature's absolute one.
ATOL = 4e-6

# Whisper's clip: 30 s, 3000 frames, which LogMel's GEMMs take as 3072 rows.
CLIP, CLIP_FRAMES, ROWS = 480000, 3000, 3072
# Measured on the host, the operators' references against the extractor's
# float32: 0.99991 of the kept features are its bf16 rounding, the rest a
# float32 tie's ulp from it.
WHISPER_MIN_EXACT = 0.9995


@pytest.fixture(scope="module")
def log_mel():
    graph = LogMel()
    graph.compile(wave=(((FRAMES + 1) * graph.hop,), np.float32))
    yield graph


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("frames", [200, FRAMES])
def test_log_mel(log_mel, frames, golden, record_property):
    n = (FRAMES + 1) * log_mel.hop
    t = np.arange(n) / 16000
    rng = np.random.default_rng(0)
    wave = (0.5 * np.sin(2 * np.pi * (200 * t + 300 * t**2))).astype(np.float32)
    wave += 0.05 * rng.standard_normal(n).astype(np.float32)
    out = log_mel(wave, frames=frames).numpy().reshape(FRAMES, log_mel.mels)
    got = out[:frames:EVERY].astype(np.float32)
    want = golden("log_mel", Extractor).logits((), wave)[: len(got)]
    ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(1e-30))) - 7)
    exact = float(np.mean(got == want))
    record_property("Exact", exact)
    if frames == FRAMES:
        assert exact >= MIN_EXACT, exact
    else:
        first = out[:frames].view(np.uint16).tolist()
        full = log_mel(wave, frames=FRAMES).numpy().reshape(FRAMES, log_mel.mels)
        assert first == full[:frames].view(np.uint16).tolist()
    assert (np.abs(got - want) <= np.maximum(ulp, ATOL)).all()
    times = []
    for _ in range(5):
        start = time.perf_counter()
        log_mel(wave, frames=frames)
        times.append(time.perf_counter() - start)
    record_property("Latency", min(times) * 1e6)


class WhisperFeatures(iron.Graph):
    """Whisper's log-mel features of a clip's wave (``whisper_wave``)."""

    def __init__(self):
        self.log_mel = LogMel(
            400,
            160,
            400,
            128,
            mel_floor=1e-10,
            mel_scale="slaney",
            norm="slaney",
            power=2,
            decades=8.0,
        )

    def body(self, wave):
        return self.log_mel(wave, frames=CLIP_FRAMES)


@pytest.fixture(scope="module")
def speech():
    """20 s of a rising tone in noise, silent to the end of the clip, its
    wave and the extractor's features of it.
    """
    t = np.arange(20 * 16000) / 16000
    rng = np.random.default_rng(0)
    audio = (0.5 * np.sin(2 * np.pi * (200 * t + 30 * t**2))).astype(np.float32)
    audio += 0.05 * rng.standard_normal(t.size).astype(np.float32)
    graph = WhisperFeatures()
    wave = whisper_wave(audio, CLIP, 400, (ROWS - 1) * 160 + graph.log_mel.span)
    return audio, wave


def check_whisper(got, want, record_property):
    """``got``'s kept frames against the extractor's ``want``."""
    got = np.asarray(got, np.float32).reshape(CLIP_FRAMES, 128)[::EVERY]
    ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(2.0**-126))) - 7)
    exact = float(np.mean(got == want))
    record_property("Exact", exact)
    assert exact >= WHISPER_MIN_EXACT, exact
    assert (np.abs(got - want) <= ulp).all(), np.abs(got - want).max()


@pytest.mark.usefixtures("npu2")
def test_whisper_log_mel_s_reference(speech, golden, record_property):
    audio, wave = speech
    want = golden("whisper_log_mel", WhisperExtractor).logits((), audio)
    check_whisper(WhisperFeatures().reference(wave), want, record_property)


@pytest.mark.supported_devices("npu1", "npu2")
def test_whisper_log_mel(speech, golden, record_property):
    audio, wave = speech
    graph = WhisperFeatures()
    graph.compile(wave=(wave.shape, np.float32))
    want = golden("whisper_log_mel", WhisperExtractor).logits((), audio)
    check_whisper(graph(wave).numpy(), want, record_property)
    times = []
    for _ in range(5):
        start = time.perf_counter()
        graph(wave)
        times.append(time.perf_counter() - start)
    record_property("Latency", min(times) * 1e6)
