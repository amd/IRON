#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

test_dir = Path(__file__).resolve().parent

# Validated on the 128-frame real-audio path.
MAX_ENCODER_NRMSE_PERCENT = 5.0
# Full-window pipeline, with the encoder's LayerNorm, softmax and GELU on NPU
# kernels; 4.14% was measured on the 5.9 s test clip (see README.md).
MAX_PIPELINE_ENCODER_NRMSE_PERCENT = 6.0

checkpoint_value = os.environ.get("WHISPER_SAFE")
wav_value = os.environ.get("WHISPER_TEST_WAV")
long_wav_value = os.environ.get("WHISPER_LONG_TEST_WAV")

checkpoint = Path(checkpoint_value).expanduser() if checkpoint_value else None

wav = Path(wav_value).expanduser() if wav_value else None
long_wav = Path(long_wav_value).expanduser() if long_wav_value else None


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1")
@pytest.mark.metrics(
    encoder_rmse=(
        r"Final encoder vs FP32 reference[\s\S]*?" r"RMSE\s*:\s*(?P<value>[\d\.e\+\-]+)"
    ),
    encoder_cosine=(
        r"Final encoder vs FP32 reference[\s\S]*?"
        r"cosine\s*:\s*(?P<value>[\d\.e\+\-]+)"
    ),
    encoder_nrmse_percent=(
        r"Final encoder vs FP32 reference[\s\S]*?"
        r"NRMSE %\s*:\s*(?P<value>[\d\.e\+\-]+)"
    ),
)
@pytest.mark.skipif(
    checkpoint is None or not checkpoint.is_file(),
    reason="WHISPER_SAFE Whisper-small checkpoint not found",
)
@pytest.mark.skipif(
    wav is None or not wav.is_file(),
    reason="WHISPER_TEST_WAV validation audio not found",
)
def test_whisper_small_encoder():
    result = subprocess.run(
        [
            sys.executable,
            str(test_dir / "whisper_encoder.py"),
            "--all",
        ],
        cwd=test_dir,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)

    assert result.returncode == 0, (
        "Whisper-small encoder validation failed "
        f"with return code {result.returncode}\n"
        f"stderr:\n{result.stderr}"
    )

    match = re.search(
        r"Final encoder vs FP32 reference[\s\S]*?"
        r"NRMSE %\s*:\s*(?P<value>[\d\.e\+\-]+)",
        result.stdout,
    )

    assert match is not None, (
        "Final encoder NRMSE was not found in output.\n" f"stdout:\n{result.stdout}"
    )

    nrmse_percent = float(match.group("value"))

    assert nrmse_percent <= MAX_ENCODER_NRMSE_PERCENT, (
        f"Encoder NRMSE {nrmse_percent:.6f}% exceeds "
        f"{MAX_ENCODER_NRMSE_PERCENT:.6f}%"
    )


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1")
@pytest.mark.metrics(
    pipeline_encoder_nrmse_percent=(
        r"Encoder NRMSE vs FP32:\s*(?P<value>[\d\.e\+\-]+)%"
    ),
    pipeline_decode_tokens_per_second=(r"decode rate\s+(?P<value>[\d\.]+)"),
)
@pytest.mark.skipif(
    checkpoint is None or not checkpoint.is_file(),
    reason="WHISPER_SAFE Whisper-small checkpoint not found",
)
@pytest.mark.skipif(
    wav is None or not wav.is_file(),
    reason="WHISPER_TEST_WAV validation audio not found",
)
def test_whisper_small_transcription():
    result = subprocess.run(
        [sys.executable, str(test_dir / "whisper_pipeline.py"), "--wav", str(wav)],
        cwd=test_dir,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)

    assert result.returncode == 0, (
        "Whisper-small transcription failed "
        f"with return code {result.returncode}\n"
        f"stderr:\n{result.stderr}"
    )
    assert "Exact CPU FP32 token match: True" in result.stdout

    match = re.search(
        r"Encoder NRMSE vs FP32:\s*(?P<value>[\d\.e\+\-]+)%", result.stdout
    )
    assert match is not None, f"Encoder NRMSE not found.\nstdout:\n{result.stdout}"
    nrmse_percent = float(match.group("value"))
    assert nrmse_percent <= MAX_PIPELINE_ENCODER_NRMSE_PERCENT, (
        f"Full-window encoder NRMSE {nrmse_percent:.6f}% exceeds "
        f"{MAX_PIPELINE_ENCODER_NRMSE_PERCENT:.6f}%"
    )


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1")
@pytest.mark.metrics(
    long_form_decode_tokens_per_second=(r"decode rate\s+(?P<value>[\d\.]+)"),
)
@pytest.mark.skipif(
    checkpoint is None or not checkpoint.is_file(),
    reason="WHISPER_SAFE Whisper-small checkpoint not found",
)
@pytest.mark.skipif(
    long_wav is None or not long_wav.is_file(),
    reason="WHISPER_LONG_TEST_WAV audio longer than 30 s not found",
)
def test_whisper_small_long_form():
    # Validated with 422-122949-0013 (32.6 s) and the 97 s clip in README.md.
    result = subprocess.run(
        [
            sys.executable,
            str(test_dir / "whisper_pipeline.py"),
            "--wav",
            str(long_wav),
        ],
        cwd=test_dir,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)

    assert result.returncode == 0, (
        "Whisper-small long-form transcription failed "
        f"with return code {result.returncode}\n"
        f"stderr:\n{result.stderr}"
    )
    assert "long-form" in result.stdout
    assert "CPU FP32 match (text exact, timestamps +-2): True" in result.stdout
