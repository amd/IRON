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

checkpoint_value = os.environ.get("WHISPER_SAFE")
wav_value = os.environ.get("WHISPER_TEST_WAV")

checkpoint = Path(checkpoint_value).expanduser() if checkpoint_value else None

wav = Path(wav_value).expanduser() if wav_value else None


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
