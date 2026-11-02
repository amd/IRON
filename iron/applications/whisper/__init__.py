# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper speech-to-text on the NPU; see ``iron/applications/whisper/README.md``."""

from iron.lm.cli import exports

__all__ = ["Whisper", "WhisperConfig", "WhisperEncoder"]
__getattr__ = exports(__name__, __all__)
