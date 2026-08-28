# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library.

Operators are re-exported lazily (PEP 562):

    from iron.operators import GEMM  # imports iron.operators.gemm.op, nothing else
"""

import importlib

_OPERATOR_MODULES = {
    "ElementwiseAdd": "elementwise_add",
    "ElementwiseMul": "elementwise_mul",
    "GEMM": "gemm",
    "GEMV": "gemv",
    "MHA": "mha",
    "RMSNorm": "rms_norm",
    "RoPE": "rope",
    "SiLU": "silu",
    "Softmax": "softmax",
    "SwiGLUDecode": "swiglu_decode",
    "SwiGLUPrefill": "swiglu_prefill",
    "Transpose": "transpose",
    "StridedCopy": "strided_copy",
    "Repeat": "repeat",
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
