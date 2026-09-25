# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from pathlib import Path

# Whisper-small geometry used by the controlled Phoenix validation.
FRAMES = 128
MELS = 80
SEQ = 64
STATE = 768
HEADS = 12
HEAD_DIM = 64
MLP = 3072
BLOCKS = 12

SCALE = HEAD_DIM**-0.5


# Application / repository paths.
APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[2]

# Keep generated validation artifacts out of the source directory.
ARTIFACT_ROOT = Path(
    os.environ.get(
        "IRON_WHISPER_ARTIFACT_DIR",
        REPO_ROOT / "phoenix-whisper-probes",
    )
).resolve()


def whisper_checkpoint() -> Path:
    """Return the configured Whisper-small safetensors checkpoint."""

    value = os.environ.get("WHISPER_SAFE")

    if not value:
        raise RuntimeError(
            "WHISPER_SAFE is not set. Point it to the "
            "Whisper-small model.safetensors checkpoint."
        )

    path = Path(value).expanduser().resolve()

    if not path.is_file():
        raise FileNotFoundError(f"Whisper checkpoint not found: {path}")

    return path
