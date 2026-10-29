# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-MoE on the shared decoder; see ``model.py``."""

from iron.lm.cli import exports

__all__ = ["Qwen3Moe"]
__getattr__ = exports(__name__, __all__)
