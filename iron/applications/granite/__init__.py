# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B end to end on the NPU; see ``iron/applications/granite/README.md``."""

from iron.lm.cli import exports

__all__ = ["Granite"]
__getattr__ = exports(__name__, __all__)
