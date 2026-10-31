# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.0-H; see ``iron/applications/granite_hybrid/README.md``."""

from iron.lm.cli import exports

__all__ = ["GraniteHybrid"]
__getattr__ = exports(__name__, __all__)
