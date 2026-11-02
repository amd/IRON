# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper's encoder and decoder graphs on the host against Hugging Face's Whisper in float32.

At a toy shape, its encoder hidden states and decoder logits recorded in
``goldens/toy.npz`` beside this test, device-free: every step of every
version resolves on ``npu1`` and ``npu2``, the encoder matches Hugging
Face's, and both step-by-step decoding from an empty cache and prompt
prefill + decoding match Hugging Face's forward logits.
"""

from types import SimpleNamespace

import numpy as np
import pytest
from aie.iron.kernels.sample import apply_ranges_ref

from iron.applications.whisper.audio import (
    log_mel_spectrogram,
    log_mel_spectrogram_long,
    slaney_filterbank,
)
from iron.applications.whisper.model import (
    EOS,
    FIRST_NON_TEXT_SPECIAL,
    MAX_INITIAL_TIMESTAMP,
    TIMESTAMP_BEGIN,
    TokenPolicy,
    Whisper,
    WhisperConfig,
    WhisperDecoder,
    windows_match,
    word_error_rate,
)
from iron.lm import OnHost
from iron.lm.generation import greedy
from iron.lm.testing import assert_close
from iron.tests.support.llama_model import checkpoint

pytestmark = pytest.mark.usefixtures("npu2")

#: Whisper's shape at toy size: 2 encoder layers and 2 decoder layers,
#: 4 heads of 64 (hidden_size=256), 64 source positions (128 Mel frames).
TOY = WhisperConfig(
    vocab_size=1024,
    hidden_size=256,
    num_hidden_layers=2,
    num_attention_heads=4,
    num_key_value_heads=4,
    intermediate_size=512,
    encoder_layers=2,
    encoder_attention_heads=4,
    encoder_ffn_dim=512,
    num_mel_bins=80,
    max_source_positions=64,
    max_seq_len=64,
    max_target_positions=64,
    prefill_chunk=64,
    bos_token_id=1000,
    eos_token_id=1000,
    pad_token_id=1000,
    decoder_start_token_id=1001,
    suppress_tokens=(1, 2),
    begin_suppress_tokens=(220, 1000),
)


def shapes(c: WhisperConfig) -> dict[str, tuple[int, ...]]:
    """Return every tensor of a Hugging Face Whisper checkpoint of ``c``'s shape."""
    E, M, S, T, V = (
        c.hidden_size,
        c.num_mel_bins,
        c.max_source_positions,
        c.max_target_positions,
        c.vocab_size,
    )
    FE, FD = c.encoder_ffn_dim, c.intermediate_size
    out: dict[str, tuple[int, ...]] = {
        "model.encoder.conv1.weight": (E, M, 3),
        "model.encoder.conv1.bias": (E,),
        "model.encoder.conv2.weight": (E, E, 3),
        "model.encoder.conv2.bias": (E,),
        "model.encoder.embed_positions.weight": (S, E),
        "model.encoder.layer_norm.weight": (E,),
        "model.encoder.layer_norm.bias": (E,),
        "model.decoder.embed_tokens.weight": (V, E),
        "model.decoder.embed_positions.weight": (T, E),
        "model.decoder.layer_norm.weight": (E,),
        "model.decoder.layer_norm.bias": (E,),
    }
    for i in range(c.encoder_layers):
        layer = f"model.encoder.layers.{i}"
        out |= {
            f"{layer}.self_attn_layer_norm.weight": (E,),
            f"{layer}.self_attn_layer_norm.bias": (E,),
            f"{layer}.self_attn.q_proj.weight": (E, E),
            f"{layer}.self_attn.q_proj.bias": (E,),
            f"{layer}.self_attn.k_proj.weight": (E, E),
            f"{layer}.self_attn.v_proj.weight": (E, E),
            f"{layer}.self_attn.v_proj.bias": (E,),
            f"{layer}.self_attn.out_proj.weight": (E, E),
            f"{layer}.self_attn.out_proj.bias": (E,),
            f"{layer}.final_layer_norm.weight": (E,),
            f"{layer}.final_layer_norm.bias": (E,),
            f"{layer}.fc1.weight": (FE, E),
            f"{layer}.fc1.bias": (FE,),
            f"{layer}.fc2.weight": (E, FE),
            f"{layer}.fc2.bias": (E,),
        }
    for i in range(c.num_hidden_layers):
        layer = f"model.decoder.layers.{i}"
        out |= {
            f"{layer}.self_attn_layer_norm.weight": (E,),
            f"{layer}.self_attn_layer_norm.bias": (E,),
            f"{layer}.self_attn.q_proj.weight": (E, E),
            f"{layer}.self_attn.q_proj.bias": (E,),
            f"{layer}.self_attn.k_proj.weight": (E, E),
            f"{layer}.self_attn.v_proj.weight": (E, E),
            f"{layer}.self_attn.v_proj.bias": (E,),
            f"{layer}.self_attn.out_proj.weight": (E, E),
            f"{layer}.self_attn.out_proj.bias": (E,),
            f"{layer}.encoder_attn_layer_norm.weight": (E,),
            f"{layer}.encoder_attn_layer_norm.bias": (E,),
            f"{layer}.encoder_attn.q_proj.weight": (E, E),
            f"{layer}.encoder_attn.q_proj.bias": (E,),
            f"{layer}.encoder_attn.k_proj.weight": (E, E),
            f"{layer}.encoder_attn.v_proj.weight": (E, E),
            f"{layer}.encoder_attn.v_proj.bias": (E,),
            f"{layer}.encoder_attn.out_proj.weight": (E, E),
            f"{layer}.encoder_attn.out_proj.bias": (E,),
            f"{layer}.final_layer_norm.weight": (E,),
            f"{layer}.final_layer_norm.bias": (E,),
            f"{layer}.fc1.weight": (FD, E),
            f"{layer}.fc1.bias": (FD,),
            f"{layer}.fc2.weight": (E, FD),
            f"{layer}.fc2.bias": (E,),
        }
    return out


class HostDecoder(OnHost, WhisperDecoder):
    """Run the decoder's recorded steps on the host."""

    profile = None


class HostWhisper(OnHost, Whisper):
    """``Whisper`` with both its outer graph and its decoder run via ``OnHost``."""

    profile = None
    decoder_class = HostDecoder

    def __init__(self, config: WhisperConfig, weights: SimpleNamespace):
        super().__init__(config, weights)
        self.encoder.profile = None

    def logits(self, tokens, mel=None):
        return Whisper.logits(self, tokens, mel)


@pytest.fixture(scope="module")
def cpu(golden):
    """Build the toy weights, Mel input, prompt and recorded Hugging Face goldens."""
    weights = checkpoint(TOY, shapes(TOY)).tree("random", seed=3)
    rng = np.random.default_rng(7)
    mel = rng.normal(0.0, 0.5, (TOY.frames, TOY.num_mel_bins)).astype(np.float32)
    prompt = rng.integers(0, TOY.vocab_size, 4, dtype=np.int64)

    def build_hf():
        from iron.applications.whisper.hugging_face import HuggingFaceWhisper

        return HuggingFaceWhisper.build("whisper", TOY, weights)

    ref = golden("toy", build_hf, TOY, weights)
    tokens = prompt.copy()
    first = logits = ref.logits(tokens, mel)
    expected = []
    for _ in range(4):
        tokens = np.append(tokens, logits.argmax())
        logits = ref.logits(tokens, mel)
        expected.append(logits)
    return SimpleNamespace(
        config=TOY,
        weights=weights,
        mel=mel,
        prompt=prompt,
        first=first,
        expected=expected,
    )


def test_every_step_of_every_version_resolves(npu1, npu2):
    """Check that every step of decode, prompt and encode resolves on npu1 and npu2."""
    import dataclasses

    one_layer = dataclasses.replace(TOY, num_hidden_layers=1, encoder_layers=1)
    weights = checkpoint(one_layer, shapes(one_layer)).tree("unread")
    for dev in (npu1, npu2):
        model = Whisper(one_layer, weights)
        for call in model.shapes():
            for step in model.record(**call).steps:
                step.op.resolved(dev)


def test_decode_from_an_empty_cache_matches_the_prompt_and_hugging_face(cpu):
    """Check that token-by-token decode and chunked prefill + decode match Hugging Face."""
    model = HostWhisper(cpu.config, cpu.weights)
    last = model.logits(cpu.prompt[:1], cpu.mel)
    for n in range(2, len(cpu.prompt) + 1):
        last = model.logits(cpu.prompt[:n])
    assert_close(last, cpu.first)

    model.decoder.forget(0)
    prefilled = model.logits(cpu.prompt)
    assert_close(prefilled, cpu.first)
    history = list(cpu.prompt)
    logits = prefilled
    for step, want in enumerate(cpu.expected):
        history.append(greedy(logits))
        logits = model.logits(history)
        assert_close(logits, want, f"step {step}")


def test_audio_spectrogram_and_token_policy():
    """Check pure-NumPy log-Mel extraction, timestamp rules and WER helpers."""
    t = np.linspace(0.0, 1.0, 16000, endpoint=False, dtype=np.float32)
    wave = 0.2 * np.sin(2.0 * np.pi * 440.0 * t)
    filters = slaney_filterbank()
    mel = log_mel_spectrogram(wave, filters, frames=128, n_samples=128 * 160)
    assert mel.shape == (128, 80) and np.isfinite(mel).all()
    mel_long, content = log_mel_spectrogram_long(wave, filters, n_samples=128 * 160)
    assert content == 100 and mel_long.shape == (228, 80)

    cfg = WhisperConfig()
    no_ts = TokenPolicy(cfg, timestamps=False)
    logits = np.zeros(cfg.vocab_size, dtype=np.float32)
    filtered = apply_ranges_ref(logits, no_ts.ranges([]))
    assert np.all(np.isneginf(filtered[FIRST_NON_TEXT_SPECIAL:]))
    assert np.isneginf(filtered[EOS])

    with_ts = TokenPolicy(cfg, timestamps=True)
    first_step = apply_ranges_ref(logits, with_ts.ranges([]))
    assert np.all(np.isneginf(first_step[:TIMESTAMP_BEGIN]))
    assert np.all(
        np.isneginf(first_step[TIMESTAMP_BEGIN + MAX_INITIAL_TIMESTAMP + 1 :])
    )
    second_step = apply_ranges_ref(logits, with_ts.ranges([TIMESTAMP_BEGIN]))
    assert np.all(np.isneginf(second_step[TIMESTAMP_BEGIN:]))

    assert word_error_rate("Mr. Quilter is here.", "mister quilter is here") == 0.0
    ok, diff = windows_match(
        [TIMESTAMP_BEGIN, 10, 20, TIMESTAMP_BEGIN + 50, EOS],
        [TIMESTAMP_BEGIN, 10, 20, TIMESTAMP_BEGIN + 52, EOS],
    )
    assert ok and diff == 2
