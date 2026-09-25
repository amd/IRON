#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import subprocess
import sys
from pathlib import Path

import pytest

test_dir = Path(__file__).resolve().parent

checkpoint_value = os.environ.get("WHISPER_SAFE")

checkpoint = Path(checkpoint_value).expanduser().resolve() if checkpoint_value else None


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1")
@pytest.mark.metrics(
    encoder_rmse=(
        r"FINAL ENCODER RESULTS[\s\S]*?" r"RMSE\s*:\s*(?P<value>[\d\.e\+\-]+)"
    ),
    encoder_cosine=(
        r"FINAL ENCODER RESULTS[\s\S]*?" r"cosine\s*:\s*(?P<value>[\d\.e\+\-]+)"
    ),
    encoder_nrmse_percent=(
        r"FINAL ENCODER RESULTS[\s\S]*?" r"NRMSE %\s*:\s*(?P<value>[\d\.e\+\-]+)"
    ),
)
@pytest.mark.skipif(
    checkpoint is None or not checkpoint.is_file(),
    reason="WHISPER_SAFE Whisper-small checkpoint not found",
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
