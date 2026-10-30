# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Mono 16 kHz PCM16 WAV audio for Whisper, over the ``wave`` module: no
torch or transformers, so a WAV loads the same in every venv that runs a
Whisper reference (``iron.applications.whisper.hugging_face``'s torch one
included) or ``--wav`` on the device.
"""

import wave
from pathlib import Path

import numpy as np

SAMPLE_RATE = 16000


def load_wav(path) -> np.ndarray:
    """A mono 16 kHz PCM16 WAV's samples, float32 in ``[-1, 1)``.

    Raises:
        ValueError: ``path`` is not mono, 16-bit or 16 kHz.
    """
    path = Path(path)
    with wave.open(str(path), "rb") as wav:
        channels = wav.getnchannels()
        width = wav.getsampwidth()
        rate = wav.getframerate()
        raw = wav.readframes(wav.getnframes())
    if channels != 1 or width != 2 or rate != SAMPLE_RATE:
        raise ValueError(
            f"{path}: expected mono {SAMPLE_RATE} Hz 16-bit PCM, got "
            f"{channels} channel(s), {8 * width}-bit, {rate} Hz"
        )
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


def save_wav(path, samples: np.ndarray) -> None:
    """``samples``, float32 in ``[-1, 1)`` at ``SAMPLE_RATE``, as a mono
    16-bit PCM WAV.
    """
    pcm = np.clip(np.asarray(samples, np.float32), -1.0, 1.0)
    pcm = (pcm * 32767.0).astype(np.int16)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(pcm.tobytes())
