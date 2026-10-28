# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 end to end on the NPU; see ``iron/applications/llama/README.md``."""

from iron.lm.cli import exports

__all__ = ["Llama"]
__getattr__ = exports(__name__, __all__)
