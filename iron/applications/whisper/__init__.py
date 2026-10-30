# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper, an encoder-decoder, on the NPU; see ``iron/applications/whisper/README.md``."""

from iron.lm.cli import exports

__all__ = ["Whisper"]
__getattr__ = exports(__name__, __all__)
