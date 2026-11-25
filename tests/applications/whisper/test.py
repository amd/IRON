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
import json
import os
import time
from types import SimpleNamespace

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.whisper.audio import (
    MEL_MAX_ABS_ERROR,
    N_SAMPLES,
    SAMPLE_RATE,
)
from iron.applications.whisper.model import (
    TokenPolicy,
    Whisper,
)
from iron.lm import Checkpoint
from iron.lm.generation import divergence, kl_stats
from iron.lm.golden import RECORD, Golden
from iron.lm.testing import check_embedding, require, weights_dir
from iron.tests.support.librispeech import utterance
from iron.tests.support.whisper import check_long_form

DIRECTORY = weights_dir("whisper-small")

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

# Measured on Phoenix (npu1): 1st-percentile token cosine >= 0.9519 (across all
# 1500 rows, including trailing silence; whole-array cosine >= 0.9991), and
# whole-array relative error (NRMSE) 0.022 to 0.044 across LibriSpeech clips.
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
def feature_extractor():
    """Load the checkpoint's independent Hugging Face Whisper feature extractor."""
    from transformers import WhisperFeatureExtractor

    return WhisperFeatureExtractor.from_pretrained(DIRECTORY)


def hf_mel(feature_extractor, waveform: np.ndarray, *, long_form: bool = False):
    """Extract Whisper features independently of the NPU frontend."""
    samples = np.asarray(waveform, dtype=np.float32)
    if long_form:
        samples = np.pad(samples, (0, N_SAMPLES))
        extracted = feature_extractor(
            samples,
            sampling_rate=16000,
            padding="do_not_pad",
            truncation=False,
            return_tensors="np",
        )
    else:
        extracted = feature_extractor(samples, sampling_rate=16000, return_tensors="np")
    return np.asarray(extracted.input_features[0].T, dtype=np.float32)


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
def reference(request):
    """Return ``reference(key, compute)`` backed by ``golden.npz`` beside the checkpoint."""
    if request.config.getoption("--random-weights") is not None:
        pytest.skip("pretrained goldens do not match random weights")
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

    def recorded(key: str, mel: np.ndarray, compute):
        golden = Golden(
            DIRECTORY / "golden.npz",
            lambda: SimpleNamespace(logits=lambda _, audio: compute(hf_model(), audio)),
            inputs(),
        )
        return golden.logits(np.frombuffer(key.encode(), np.uint8), mel)

    return recorded


@pytest.mark.bench
def test_whisper_short(model, reference, feature_extractor, record_property):
    """Encode and decode a short clip on the NPU (runs on every PR)."""
    wave = clip("short")
    want_mel = hf_mel(feature_extractor, wave)
    mel, _ = model.log_mel(wave)
    mel_error = float(np.max(np.abs(mel - want_mel)))
    record_property("MelMaxAbsError", mel_error)
    assert mel_error <= MEL_MAX_ABS_ERROR, mel_error
    policy = TokenPolicy(model.config, timestamps=False)
    t0 = time.perf_counter()
    tokens, got_enc = model.window(mel, policy=policy)
    elapsed = time.perf_counter() - t0
    record_property("Latency", elapsed * 1e6)
    want_enc = reference("encoder short", want_mel, lambda hf, audio: hf.encode(audio))
    check_embedding(
        got_enc,
        want_enc,
        ENCODER_MIN_COSINE,
        ENCODER_MAX_ERROR,
        record=record_property,
    )
    want_tokens = reference(
        "window single-call no-eos short",
        want_mel,
        lambda hf, audio: np.asarray(
            hf.window(audio, list(policy.prompt), policy)[0], np.int32
        ),
    )
    if tokens and tokens[-1] == policy.eos:
        tokens = tokens[:-1]
    assert tokens == want_tokens.astype(np.int32).tolist()


@pytest.mark.extensive
@pytest.mark.parametrize("name", ["short", "medium", "passage"])
def test_whisper_encoder_accuracy(
    model, reference, feature_extractor, name, record_property
):
    """Check the NPU encoder's hidden states against float32 Hugging Face."""
    mel = hf_mel(feature_extractor, clip(name))
    got = model.encode(mel)
    want = reference(f"encoder {name}", mel, lambda hf, audio: hf.encode(audio))
    check_embedding(
        got,
        want,
        ENCODER_MIN_COSINE,
        ENCODER_MAX_ERROR,
        record=record_property,
    )


@pytest.mark.extensive
@pytest.mark.parametrize("name", ["short", "medium"])
def test_whisper_decoder_accuracy(
    model, reference, feature_extractor, name, record_property
):
    """Check teacher-forced decoder logits against float32 Hugging Face."""
    mel = hf_mel(feature_extractor, clip(name))
    tokens: list[int] = list(TokenPolicy(model.config).prompt)
    results = []
    for step in range(STEPS):
        want = reference(
            f"logits {name} {step} {tokens}",
            mel,
            lambda hf, audio, t=list(tokens): hf.logits(t, audio),
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
def test_whisper_determinism(model, feature_extractor, record_property):
    """Alternating calls over two clips produce bit-identical encoder outputs and logits."""
    mels = [hf_mel(feature_extractor, clip(n)) for n in ("short", "medium")]
    prompt = list(TokenPolicy(model.config).prompt)
    first = [(model.encode(m).copy(), model.logits(prompt).copy()) for m in mels]
    differing = 0
    for _ in range(2):
        for (want_enc, want_logits), m in zip(first, mels):
            got_enc = model.encode(m)
            got_logits = model.logits(prompt)
            if not (
                np.array_equal(got_enc, want_enc)
                and np.array_equal(got_logits, want_logits)
            ):
                differing += 1
    record_property("DifferingRuns", differing)
    assert differing == 0


@pytest.mark.extensive
def test_whisper_long_form(model, reference, feature_extractor, record_property):
    """Check multi-window timestamped long-form transcription on a 35 s clip."""
    res = model.transcribe(clip("long"), long_form=True)
    assert res["long_form"] and len(res["windows"]) >= 2
    wave = clip("long")
    mel = hf_mel(feature_extractor, wave, long_form=True)
    mel_error = float(np.max(np.abs(res["mel"] - mel)))
    record_property("MelMaxAbsError", mel_error)
    assert mel_error <= MEL_MAX_ABS_ERROR, mel_error
    recorded = reference(
        f"whole long-form HF {CLIPS['long']}",
        wave,
        lambda hf, audio: hf.long_form(audio),
    )
    expected = json.loads(recorded.astype(np.uint8).tobytes().decode("utf-8"))
    wer, drift = check_long_form(res, expected, wave.size / SAMPLE_RATE)
    record_property("WER", wer)
    record_property("TimestampDrift", drift)


def test_whisper_frontend_cache_is_bounded(model, feature_extractor):
    """Reuse one capacity and release its arena on eviction and model teardown."""
    previous = None
    previous_samples = None
    for samples in (1600, 1600, 16000, 1600):
        wave = np.zeros(samples, np.float32)
        got, _ = model.log_mel(wave, long_form=True)
        want = hf_mel(feature_extractor, wave, long_form=True)
        assert np.max(np.abs(got - want)) <= MEL_MAX_ABS_ERROR
        assert len(model._frontends) == 1
        current = next(iter(model._frontends.values()))
        if previous is not None:
            if samples == 1600 and previous_samples == 1600:
                assert current is previous
            else:
                assert current is not previous
                assert not previous.is_loaded
                assert previous.arena is not None and not previous.arena.loaded
        previous, previous_samples = current, samples
    model.release()
    assert not model._frontends
    assert previous is not None and not previous.is_loaded
