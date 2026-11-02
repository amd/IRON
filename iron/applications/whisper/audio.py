# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper audio loading and log-Mel spectrogram extraction in NumPy."""

import json
import wave
from pathlib import Path

import numpy as np

SAMPLE_RATE = 16000
N_FFT = 400
HOP_LENGTH = 160
N_MELS = 80
N_SAMPLES = 30 * SAMPLE_RATE
FRAMES = N_SAMPLES // HOP_LENGTH


def _hz_to_mel(freq: np.ndarray | float) -> np.ndarray | float:
    """Convert frequencies in Hz to the Slaney mel scale."""
    min_log_hz = 1000.0
    min_log_mel = 15.0
    logstep = 27.0 / np.log(6.4)
    freq_arr = np.asarray(freq, dtype=np.float64)
    mels = 3.0 * freq_arr / 200.0
    above = freq_arr >= min_log_hz
    if np.any(above):
        mels = np.where(
            above,
            min_log_mel
            + np.log(np.maximum(freq_arr, min_log_hz) / min_log_hz) * logstep,
            mels,
        )
    return mels


def _mel_to_hz(mels: np.ndarray) -> np.ndarray:
    """Convert Slaney mel values to frequencies in Hz."""
    min_log_hz = 1000.0
    min_log_mel = 15.0
    logstep = np.log(6.4) / 27.0
    mels = np.asarray(mels, dtype=np.float64)
    freqs = 200.0 * mels / 3.0
    above = mels >= min_log_mel
    return np.where(above, min_log_hz * np.exp((mels - min_log_mel) * logstep), freqs)


def slaney_filterbank(
    fft: int = N_FFT, mels: int = N_MELS, sample_rate: int = SAMPLE_RATE
) -> np.ndarray:
    """Compute the ``(fft // 2 + 1, mels)`` Slaney-normalized mel filterbank in float32."""
    mel_points = np.linspace(_hz_to_mel(0.0), _hz_to_mel(sample_rate / 2.0), mels + 2)
    filter_freqs = _mel_to_hz(mel_points)
    fft_freqs = np.linspace(0.0, sample_rate / 2.0, fft // 2 + 1, dtype=np.float64)
    fdiff = np.diff(filter_freqs)
    ramps = filter_freqs[None, :] - fft_freqs[:, None]
    lower = -ramps[:, :-2] / fdiff[:-1]
    upper = ramps[:, 2:] / fdiff[1:]
    weights = np.maximum(0.0, np.minimum(lower, upper))
    enorm = 2.0 / (filter_freqs[2 : mels + 2] - filter_freqs[:mels])
    return (weights * enorm[None, :]).astype(np.float32)


def mel_filters(
    directory: str | Path | None = None,
    fft: int = N_FFT,
    mels: int = N_MELS,
    sample_rate: int = SAMPLE_RATE,
) -> np.ndarray:
    """Return the ``(fft // 2 + 1, mels)`` float32 mel filterbank.

    Loads the exact ``mel_filters`` matrix from ``preprocessor_config.json``
    in ``directory`` when present, otherwise computes the Slaney filterbank.
    """
    bins = fft // 2 + 1
    if directory is not None:
        path = Path(directory)
        if path.is_file():
            path = path.parent
        config_path = path / "preprocessor_config.json"
        if config_path.exists():
            data = json.loads(config_path.read_text(encoding="utf-8"))
            if "mel_filters" in data:
                filters = np.asarray(data["mel_filters"], dtype=np.float32)
                if filters.shape == (mels, bins):
                    filters = np.ascontiguousarray(filters.T)
                if filters.shape != (bins, mels):
                    raise ValueError(
                        f"Unexpected Whisper mel_filters shape {filters.shape}, "
                        f"expected {(bins, mels)}"
                    )
                return filters
    return slaney_filterbank(fft, mels, sample_rate)


def load_wav(path: str | Path) -> np.ndarray:
    """Load a mono 16 kHz audio file as a 1-D float32 array in ``[-1, 1)``."""
    path = Path(path)
    if path.suffix.lower() == ".wav":
        with wave.open(str(path), "rb") as wav_file:
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            sample_rate = wav_file.getframerate()
            raw = wav_file.readframes(wav_file.getnframes())
        if channels != 1:
            raise ValueError(f"Expected mono WAV, got {channels} channels")
        if sample_rate != SAMPLE_RATE:
            raise ValueError(f"Expected {SAMPLE_RATE} Hz WAV, got {sample_rate} Hz")
        if sample_width == 2:
            return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    import soundfile  # pyright: ignore[reportMissingImports] -- requirements_examples.txt's: optional

    samples, rate = soundfile.read(path, dtype="float32")
    if samples.ndim != 1 or rate != SAMPLE_RATE:
        raise ValueError(
            f"{path}: expected 16 kHz mono, got shape {samples.shape} at {rate} Hz"
        )
    return np.asarray(samples, dtype=np.float32)


def _stft_log_mel(waveform: np.ndarray, filters: np.ndarray) -> np.ndarray:
    """Compute Whisper log-Mel features ``(num_frames, mels)`` float32 from padded samples."""
    pad = N_FFT // 2
    padded = np.pad(waveform, (pad, pad), mode="reflect")
    windows = np.lib.stride_tricks.sliding_window_view(padded, N_FFT)[::HOP_LENGTH][:-1]
    hann = (
        0.5 - 0.5 * np.cos(2.0 * np.pi * np.arange(N_FFT, dtype=np.float64) / N_FFT)
    ).astype(np.float32)
    spectrum = np.fft.rfft(windows * hann, n=N_FFT, axis=-1)
    magnitudes = (spectrum.real.astype(np.float32) ** 2) + (
        spectrum.imag.astype(np.float32) ** 2
    )
    mel = magnitudes @ filters
    log_spec = np.log10(np.maximum(mel, 1e-10))
    log_spec = np.maximum(log_spec, log_spec.max() - 8.0)
    return ((log_spec + 4.0) / 4.0).astype(np.float32)


def log_mel_spectrogram(
    waveform: np.ndarray,
    filters: np.ndarray | None = None,
    *,
    frames: int = FRAMES,
    n_samples: int = N_SAMPLES,
) -> np.ndarray:
    """Compute Whisper log-Mel features ``(frames, mels)`` float32 for one 30 s window.

    Pads or crops ``waveform`` to ``n_samples`` before the centered STFT so
    boundary frames see the canonical 30 s analysis window.
    """
    samples = np.asarray(waveform, dtype=np.float32).reshape(-1)
    padded = np.zeros(n_samples, dtype=np.float32)
    held = min(samples.size, n_samples)
    padded[:held] = samples[:held]
    if filters is None:
        filters = slaney_filterbank()
    features = _stft_log_mel(padded, filters)
    if features.shape[0] < frames:
        raise ValueError(
            f"STFT produced {features.shape[0]} frames, fewer than {frames}"
        )
    return np.ascontiguousarray(features[:frames])


def log_mel_spectrogram_long(
    waveform: np.ndarray,
    filters: np.ndarray | None = None,
    *,
    n_samples: int = N_SAMPLES,
) -> tuple[np.ndarray, int]:
    """Compute Whisper log-Mel features of a full recording for long-form decoding.

    Appends ``n_samples`` (30 s) of silence and normalizes over the whole
    recording, matching OpenAI Whisper's ``transcribe``. Returns
    ``(features, content_frames)`` where ``features`` is ``(total_frames, mels)``
    float32 and ``content_frames`` is the frame count before the trailing silence.
    """
    samples = np.asarray(waveform, dtype=np.float32).reshape(-1)
    padded = np.pad(samples, (0, n_samples))
    if filters is None:
        filters = slaney_filterbank()
    features = _stft_log_mel(padded, filters)
    return np.ascontiguousarray(features), samples.size // HOP_LENGTH
