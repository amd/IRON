# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3 end to end on the NPU; see ``iron/applications/qwen3/README.md``."""

from iron.lm.cli import exports

__all__ = ["Qwen3"]
__getattr__ = exports(__name__, __all__)
