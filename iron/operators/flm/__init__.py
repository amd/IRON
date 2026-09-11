# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ports of FastFlowLM overlays to IRON.

Operators are re-exported lazily (PEP 562):

    from iron.operators.flm import GEMM  # imports iron.operators.flm.gemm.op
"""

import importlib

_OPERATOR_MODULES = {
    # The port, built from source for the current device.
    "GEMM": "gemm",
    # The shipped overlay itself, downloaded as a pinned binary. NPU2 only;
    # exists so the port can be measured against what it was ported from.
    "MMPrebuilt": "mm_prebuilt",
}

__all__ = sorted(_OPERATOR_MODULES)


def __getattr__(name):
    """Import the operator that defines `name`, on first access."""
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f".{module}.op", __name__), name)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES))
