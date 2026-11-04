# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper audio loading."""

import wave
from pathlib import Path

import numpy as np

SAMPLE_RATE = 16000
N_FFT = 400
HOP_LENGTH = 160
N_MELS = 80
N_SAMPLES = 30 * SAMPLE_RATE
FRAMES = N_SAMPLES // HOP_LENGTH


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
