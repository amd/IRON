# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Minimal Whisper audio feature extraction using PyTorch only."""

import json
import wave
from pathlib import Path

import torch

from whisper_common import whisper_checkpoint

SAMPLE_RATE = 16000
N_FFT = 400
HOP_LENGTH = 160
N_MELS = 80

# Our currently validated Phoenix geometry.
TARGET_FRAMES = 128


def _preprocessor_config():
    checkpoint = whisper_checkpoint()

    config_path = checkpoint.parent / "preprocessor_config.json"

    with config_path.open(
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)


def mel_filterbank():
    """Load the exact Mel matrix shipped with the Whisper checkpoint."""

    cfg = _preprocessor_config()

    filters = torch.tensor(
        cfg["mel_filters"],
        dtype=torch.float32,
    )

    expected = (
        N_MELS,
        N_FFT // 2 + 1,
    )

    if filters.shape != expected:
        raise RuntimeError(
            "Unexpected Whisper Mel matrix: "
            f"{tuple(filters.shape)}, "
            f"expected {expected}"
        )

    return filters


def load_wav(path):
    """Load a mono 16-kHz PCM WAV as normalized float32."""

    path = Path(path)

    with wave.open(
        str(path),
        "rb",
    ) as wav:
        channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        frames = wav.getnframes()

        raw = wav.readframes(frames)

    if channels != 1:
        raise ValueError(f"Expected mono WAV, got {channels} channels")

    if sample_rate != SAMPLE_RATE:
        raise ValueError(f"Expected {SAMPLE_RATE} Hz WAV, " f"got {sample_rate} Hz")

    if sample_width != 2:
        raise ValueError("Initial Whisper validation supports " "16-bit PCM WAV only")

    samples = torch.frombuffer(
        bytearray(raw),
        dtype=torch.int16,
    ).clone()

    waveform = samples.to(torch.float32) / 32768.0

    return waveform


def log_mel_spectrogram(
    waveform,
    target_frames=TARGET_FRAMES,
):
    """Compute Whisper-compatible log-Mel features.

    The current Phoenix integration deliberately uses only 128
    Mel frames so that it matches the already validated encoder
    geometry.
    """

    waveform = waveform.to(dtype=torch.float32).flatten()

    # Whisper's canonical feature extractor pads/crops the audio
    # to the configured 30-second analysis window BEFORE the STFT.
    #
    # target_frames controls only how many resulting Mel frames
    # are returned. It must not truncate the waveform before a
    # centered STFT, because doing so changes the right-hand
    # context of the final requested frame.
    cfg = _preprocessor_config()

    n_samples = int(cfg["n_samples"])

    if waveform.numel() < n_samples:
        waveform = torch.nn.functional.pad(
            waveform,
            (
                0,
                n_samples - waveform.numel(),
            ),
        )
    else:
        waveform = waveform[:n_samples]

    window = torch.hann_window(
        N_FFT,
        periodic=True,
        dtype=torch.float32,
    )

    stft = torch.stft(
        waveform,
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        window=window,
        center=True,
        return_complex=True,
    )

    magnitudes = stft[..., :-1].abs().pow(2.0)

    filters = mel_filterbank()

    mel = filters @ magnitudes

    log_spec = torch.clamp(
        mel,
        min=1e-10,
    ).log10()

    log_spec = torch.maximum(
        log_spec,
        log_spec.max() - 8.0,
    )

    log_spec = (log_spec + 4.0) / 4.0

    if log_spec.shape[1] < target_frames:
        raise RuntimeError("STFT produced too few frames: " f"{log_spec.shape[1]}")

    log_spec = log_spec[
        :,
        :target_frames,
    ].contiguous()

    expected = (
        N_MELS,
        target_frames,
    )

    if log_spec.shape != expected:
        raise RuntimeError(f"Unexpected log-Mel shape " f"{tuple(log_spec.shape)}")

    if not torch.isfinite(log_spec).all():
        raise RuntimeError("Non-finite Whisper features")

    return log_spec.unsqueeze(0)
