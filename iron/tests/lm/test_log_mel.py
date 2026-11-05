# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.LogMel on a device: one compile at 3072 frames, called at two frame counts.

Every 8th frame against Hugging Face's Gemma 4 feature extractor's
float64 features, recorded in ``goldens/``.
"""

import time

import numpy as np
import pytest

from iron.applications.whisper.audio import MEL_MAX_ABS_ERROR
from iron.lm import LogMel
from iron.tests.support.log_mel import EVERY, Extractor

FRAMES = 3072
# Measured on the host, the operators' references against the extractor:
# 0.99969 of the kept features are its bf16 rounding. Held at FRAMES alone:
# 200 frames keep 3200 features, too few for a rate.
MIN_EXACT = 0.999
# The rest within one bf16 ulp, bar a log near 0, where the energy's
# relative error is the feature's absolute one.
ATOL = 4e-6


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


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("silent", [False, True])
def test_whisper_log_mel(silent, record_property):
    """Check the fused Whisper frontend against Hugging Face's feature extractor."""
    from transformers import WhisperFeatureExtractor

    frames = 64
    graph = LogMel(
        frame=400,
        fft=400,
        mels=80,
        mel_scale="slaney",
        mel_floor=1e-10,
        power=2,
        decades=8,
        shift=4,
        scale=0.25,
    )
    wave = np.zeros(frames * graph.hop, np.float32)
    if not silent:
        t = np.arange(wave.size) / 16000
        wave[:] = 0.2 * np.sin(2 * np.pi * 440 * t)
        wave[: wave.size // 3] *= 0.001
    padded = np.pad(wave, (graph.frame // 2, graph.frame // 2), mode="reflect")
    net = graph.compile(wave=((padded.size,), np.float32))
    try:
        got = net(padded, frames=frames).numpy().reshape(frames, 80).astype(np.float32)
    finally:
        net.release()
    extracted = WhisperFeatureExtractor()(
        wave,
        sampling_rate=16000,
        padding="do_not_pad",
        truncation=False,
        return_tensors="np",
    )
    want = extracted.input_features[0].T[:frames].astype(np.float32)
    error = float(np.max(np.abs(got - want)))
    record_property("MaxAbsError", error)
    assert error <= MEL_MAX_ABS_ERROR, error
