#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.LogMel on a device: one compile at 3072 frames, called at two
frame counts, every 8th frame against Hugging Face's Gemma 4 feature
extractor's float64 features, recorded in ``goldens/``.
"""

import time

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import LogMel

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

FRAMES = 3072
# Measured on the host, the operators' references against the extractor:
# 0.99969 of the kept features are its bf16 rounding.
MIN_EXACT = 0.999
# The rest within one bf16 ulp, bar a log near 0, where the energy's
# relative error is the feature's absolute one.
ATOL = 4e-6
# The frames the goldens keep.
EVERY = 8


class Extractor:
    """transformers' ``Gemma4AudioFeatureExtractor``, what records a
    golden: every ``EVERY``th frame's features of a float32 wave, rounded
    once to bf16.
    """

    def logits(self, tokens, wave):
        import transformers

        # The extractor's first frame is centred on the wave's start, a half
        # frame of zeros before it, so its frame f + 1 is LogMel's f; the
        # zero after completes the last.
        wave = np.append(wave, np.float32(0))
        extractor = transformers.Gemma4AudioFeatureExtractor()
        features, _ = extractor._extract_spectrogram(wave, np.ones(wave.size, bool))
        return features[1::EVERY].astype(bfloat16).astype(np.float32)


@pytest.fixture(scope="module")
def log_mel():
    graph = LogMel()
    graph.compile(wave=(((FRAMES + 1) * graph.hop,), np.float32))
    yield graph


@pytest.mark.parametrize("frames", [200, FRAMES])
def test_log_mel(log_mel, frames, golden, record_property):
    n = (FRAMES + 1) * log_mel.hop
    t = np.arange(n) / 16000
    rng = np.random.default_rng(0)
    wave = (0.5 * np.sin(2 * np.pi * (200 * t + 300 * t**2))).astype(np.float32)
    wave += 0.05 * rng.standard_normal(n).astype(np.float32)
    got = log_mel(wave, frames=frames).numpy().reshape(FRAMES, log_mel.mels)
    got = got[:frames:EVERY].astype(np.float32)
    want = golden("log_mel", Extractor).logits((), wave)[: len(got)]
    ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(1e-30))) - 7)
    exact = float(np.mean(got == want))
    record_property("Exact", exact)
    assert exact >= MIN_EXACT, exact
    assert (np.abs(got - want) <= np.maximum(ulp, ATOL)).all()
    times = []
    for _ in range(5):
        start = time.perf_counter()
        log_mel(wave, frames=frames)
        times.append(time.perf_counter() - start)
    record_property("Latency", min(times) * 1e6)
