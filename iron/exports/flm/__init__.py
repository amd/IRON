# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ports of FastFlowLM overlays to IRON.

Operators are re-exported lazily (PEP 562):

    from iron.exports.flm import GEMM, Shipped  # imports iron.exports.flm.gemm.*
"""

import importlib

_OPERATOR_MODULES = {
    # The port, built from source for the current device.
    "GEMM": "gemm.op",
    # q4nx weights to the bfp16 B that GEMM reads, without a host-side pack.
    "DequantBFP": "dequant.op",
    # The shipped binary itself, downloaded and pinned, as a second form of
    # GEMM: Shipped(...). NPU2 only; exists so the port can be measured
    # against what it was ported from.
    "Shipped": "gemm.shipped",
}

__all__ = sorted(_OPERATOR_MODULES)  # pyright: ignore[reportUnsupportedDunderAll]


def __getattr__(name):
    """Import the operator that defines `name`, on first access."""
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f".{module}", __name__), name)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES))
