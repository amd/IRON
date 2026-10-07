# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library.

Operators are re-exported lazily (PEP 562):

    from iron.operators import GEMM  # imports iron.operators.gemm, nothing else

The FastFlowLM ports, and the binary they are measured against, are
``flm``'s, a catalog of their own: its GEMM is not this one.
"""

import importlib

# Operator name -> the module that defines it, relative to this package: one
# file (``relu``), or ``<directory>.op`` for one that keeps a design, a
# reference or a test of its own beside it.
_OPERATOR_MODULES = {
    "AXPY": "axpy",
    "Clamp": "clamp",
    "DepthwiseConv1d": "depthwise_conv1d",
    "Dequant": "dequant",
    "ElementwiseAdd": "elementwise_add",
    "ElementwiseMul": "elementwise_mul",
    "Emit": "emit",
    "GELU": "gelu",
    "GEMM": "gemm",
    "GEMV": "gemv",
    "GQAContext": "gqa_context",
    "LayerNorm": "layer_norm",
    "LeakyReLU": "leaky_relu",
    "Limbs": "limbs",
    "Log": "log",
    "Magnitude": "magnitude",
    "MHA": "mha",
    "ReLU": "relu",
    "RMSNorm": "rms_norm",
    "Repeat": "repeat",
    "RoPE": "rope",
    "Sample": "sample",
    "Sigmoid": "sigmoid",
    "SiLU": "silu",
    "Softmax": "softmax",
    "Copy": "copy",
    "Tanh": "tanh",
    "Transpose": "transpose",
}

__all__ = sorted(_OPERATOR_MODULES)


def __getattr__(name):
    """Import the operator that defines `name`, on first access."""
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f".{module}", __name__), name)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES))
