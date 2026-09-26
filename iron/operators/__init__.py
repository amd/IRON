# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library.

Operators are re-exported lazily (PEP 562):

    from iron.operators import GEMM  # imports iron.operators.gemm.op, nothing else
"""

import importlib

# Operator name -> the module that defines it, relative to this package. A
# small operator is one file (``relu``); one with a design, a reference or a
# test of its own keeps a directory (``gemm.op``).
_OPERATOR_MODULES = {
    "AXPY": "axpy",
    "Dequant": "dequant",
    "ElementwiseAdd": "elementwise_add",
    "Emit": "emit",
    "ElementwiseMul": "elementwise_mul",
    "GELU": "gelu",
    "GEMM": "gemm.op",
    "GEMV": "gemv.op",
    "LayerNorm": "layer_norm",
    "LeakyReLU": "leaky_relu",
    "MHA": "mha.op",
    "MemCopy": "mem_copy",
    "ReLU": "relu",
    "RMSNorm": "rms_norm",
    "WeightedRMSNorm": "rms_norm",
    "Repeat": "repeat",
    "Sample": "sample",
    "RoPE": "rope.op",
    "Sigmoid": "sigmoid",
    "SiLU": "silu",
    "Softmax": "softmax",
    "DynamicSoftmax": "softmax",
    "StridedCopy": "strided_copy",
    "SwiGLUDecode": "swiglu_decode.op",
    "SwiGLUPrefill": "swiglu_prefill.op",
    "Tanh": "tanh",
    "Transpose": "transpose",
}

# Sub-packages whose operator names would collide with the table above.
_SUBPACKAGES = ("flm",)

__all__ = sorted(set(_OPERATOR_MODULES) | set(_SUBPACKAGES))


def __getattr__(name):
    """Import the operator that defines `name`, on first access."""
    if name in _SUBPACKAGES:
        return importlib.import_module(f".{name}", __name__)
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(f".{module}", __name__), name)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES) | set(_SUBPACKAGES))
