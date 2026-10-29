# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Reranker on the NPU; see ``model.py``."""

from iron.lm.cli import exports

__all__ = ["Qwen3Reranker"]
__getattr__ = exports(__name__, __all__)
