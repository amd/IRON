# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ports of FastFlowLM overlays to IRON.

Operators are re-exported lazily (PEP 562):

    from iron.operators.flm import GEMM  # imports iron.operators.flm.gemm.op

The one catalog is ``iron.operators._OPERATOR_MODULES``, dotted
(``"flm.GEMM"``); this package's own names, below, are that catalog's
``flm.`` entries with the prefix dropped.
"""

import importlib

from .. import _FLM_OPERATOR_MODULES as _OPERATOR_MODULES

__all__ = sorted(_OPERATOR_MODULES)


def __getattr__(name):
    """Import the operator that defines `name`, on first access."""
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f".{module}", __name__), name)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES))
