# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper-small on the NPU, from the real checkpoint, against Hugging Face.

Checked against Hugging Face's ``WhisperForConditionalGeneration`` in
float32 (``hugging_face.py``), its outputs recorded in ``golden.npz``
beside the checkpoint: the audio encoder's hidden states (cosine and
relative error), the decoder's next-token logits and greedy
transcription over LibriSpeech utterances, determinism, and multi-window
long-form timestamp decoding.
"""

import functools
import os
import time
from types import SimpleNamespace

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.whisper.audio import (
    log_mel_spectrogram,
    log_mel_spectrogram_long,
)
from iron.applications.whisper.model import (
    PROMPT,
    TIMESTAMP_TOLERANCE,
    TokenPolicy,
    Whisper,
    decode_window,
    windows_match,
)
from iron.lm import Checkpoint
from iron.lm.generation import divergence, kl_stats
from iron.lm.golden import RECORD, Golden
from iron.lm.testing import check_embedding, require, weights_dir
from iron.tests.support.librispeech import utterance

DIRECTORY = weights_dir("whisper-small")

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

# Measured on Phoenix (npu1): 1st-percentile token cosine >= 0.9519 (across all
# 1500 rows, including trailing silence; whole-array cosine >= 0.9991), and
# whole-array relative error (NRMSE) 0.022 to 0.041 across LibriSpeech clips.
ENCODER_MIN_COSINE = 0.95
ENCODER_MAX_ERROR = 0.05

# Teacher-forced decoder KL(float32 HF || NPU) over 8 steps.
MAX_KL = {"Mean": 0.05, "Max": 0.25}
STEPS = 8

CLIPS = {
    # 2.0 s: "Won't you tell Douglas".
    "short": "121-127105-0021",
    # 7.3 s.
    "medium": "4446-2275-0016",
    # 13.0 s.
    "passage": "2094-142345-0014",
    # 35.0 s: past the 30 s window, exercising 2-window long-form decoding.
    "long": "4507-16021-0047",
}


def clip(name: str) -> np.ndarray:
    """Return the LibriSpeech utterance ``CLIPS[name]`` at 16 kHz mono."""
    return utterance(CLIPS[name])


@pytest.fixture(scope="module")
def model(request):
    """Compile and load ``Whisper`` once for the module's tests."""
    seed = request.config.getoption("--random-weights")
    files = [DIRECTORY / "model.safetensors", DIRECTORY / "config.json"]
    if seed is None:
        files.append(DIRECTORY / "tokenizer.json")
    require(*files)
    loaded = Whisper.load(DIRECTORY, random_weights=seed)
    yield loaded
    loaded.release()
    if aie_utils.DefaultNPURuntime is not None:
        aie_utils.DefaultNPURuntime.cleanup()


@pytest.fixture(scope="module")
def reference():
    """Return ``reference(key, compute)`` backed by ``golden.npz`` beside the checkpoint."""
    if not os.environ.get(RECORD):
        require(DIRECTORY / "golden.npz")

    @functools.cache
    def hf_model():
        from iron.applications.whisper.hugging_face import HuggingFaceWhisper

        return HuggingFaceWhisper.load(DIRECTORY)

    @functools.cache
    def inputs():
        checkpoint = Checkpoint(DIRECTORY / "model.safetensors")
        return (DIRECTORY / "config.json").read_text(), checkpoint.fingerprint()

    def recorded(key: str, compute):
        golden = Golden(
            DIRECTORY / "golden.npz",
            lambda: SimpleNamespace(logits=lambda _: compute(hf_model())),
            inputs(),
        )
        return golden.logits(np.frombuffer(key.encode(), np.uint8))

    return recorded


@pytest.mark.bench
def test_whisper_short(model, reference, record_property):
    """Encode and decode a short clip on the NPU (runs on every PR)."""
    want_mel = log_mel_spectrogram(
        clip("short"), model.filters(), frames=model.config.frames
    )
    mel, _ = model.log_mel(clip("short"))
    assert np.max(np.abs(mel - want_mel)) <= 0.03
    policy = TokenPolicy(model.config, timestamps=False)
    t0 = time.perf_counter()
    tokens, got_enc = model.window(mel, list(PROMPT), policy)
    elapsed = time.perf_counter() - t0
    record_property("Latency", elapsed * 1e6)
    record_property("TPS", len(tokens) / max(elapsed, 1e-6))
    want_enc = reference("encoder short", lambda hf: hf.encode(want_mel))
    check_embedding(
        got_enc,
        want_enc,
        ENCODER_MIN_COSINE,
        ENCODER_MAX_ERROR,
        record=record_property,
    )
    want_tokens = reference(
        "window short",
        lambda hf: np.asarray(hf.window(want_mel, list(PROMPT), policy)[0], np.int32),
    )
    assert tokens == list(want_tokens)


@pytest.mark.extensive
@pytest.mark.parametrize("name", ["short", "medium", "passage"])
def test_whisper_encoder_accuracy(model, reference, name, record_property):
    """Check the NPU encoder's hidden states against float32 Hugging Face."""
    mel = log_mel_spectrogram(clip(name), model.filters(), frames=model.config.frames)
    got = model.encode(mel)
    want = reference(f"encoder {name}", lambda hf: hf.encode(mel))
    check_embedding(
        got,
        want,
        ENCODER_MIN_COSINE,
        ENCODER_MAX_ERROR,
        record=record_property,
    )


@pytest.mark.extensive
@pytest.mark.parametrize("name", ["short", "medium"])
def test_whisper_decoder_accuracy(model, reference, name, record_property):
    """Check teacher-forced decoder logits against float32 Hugging Face."""
    mel = log_mel_spectrogram(clip(name), model.filters(), frames=model.config.frames)
    tokens: list[int] = list(PROMPT)
    results = []
    for step in range(STEPS):
        want = reference(
            f"logits {name} {step} {tokens}",
            lambda hf, t=list(tokens): hf.logits(t, mel),
        )
        got = model.logits(tokens, mel if step == 0 else None)
        results.append(divergence(want, got))
        tokens.append(int(want.argmax()))
    stats = kl_stats(results)
    for stat, value in stats.items():
        record_property(f"{stat}KL", float(value))
    record_property("Top1Mismatches", sum(not top1 for _, top1 in results))
    for stat, bound in MAX_KL.items():
        assert stats[stat] <= bound, f"{stat.lower()} KL {stats[stat]} > {bound}"


@pytest.mark.extensive
def test_whisper_determinism(model, record_property):
    """Alternating calls over two clips produce bit-identical encoder outputs and logits."""
    mels = [
        log_mel_spectrogram(clip(n), model.filters(), frames=model.config.frames)
        for n in ("short", "medium")
    ]
    first = [(model.encode(m).copy(), model.logits(list(PROMPT)).copy()) for m in mels]
    differing = 0
    for _ in range(2):
        for (want_enc, want_logits), m in zip(first, mels):
            got_enc = model.encode(m)
            got_logits = model.logits(list(PROMPT))
            if not (
                np.array_equal(got_enc, want_enc)
                and np.array_equal(got_logits, want_logits)
            ):
                differing += 1
    record_property("DifferingRuns", differing)
    assert differing == 0


@pytest.mark.extensive
def test_whisper_long_form(model, reference, record_property):
    """Check multi-window timestamped long-form transcription on a 35 s clip."""
    res = model.transcribe(clip("long"), long_form=True)
    assert res["long_form"] and len(res["windows"]) >= 2
    mel, content_frames = log_mel_spectrogram_long(clip("long"), model.filters())
    policy = TokenPolicy(model.config, timestamps=True)
    worst = 0
    for i, w in enumerate(res["windows"]):
        seek = int(w["seek"])
        expected = reference(
            f"long_window {i} {seek}",
            lambda hf, s=seek: np.asarray(
                decode_window(
                    hf, mel, s, content_frames, policy, frames=model.config.frames
                )[1],
                np.int32,
            ),
        )
        ok, diff = windows_match(w["tokens"], list(expected), tokenizer=model.tokenizer)
        assert ok, f"window {i} (seek {seek}): {w['tokens']} != {list(expected)}"
        if diff is not None:
            worst = max(worst, diff)
    record_property("DifferingTokens", worst)
    assert worst <= TIMESTAMP_TOLERANCE
