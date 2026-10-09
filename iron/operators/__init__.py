# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library.

Operators are re-exported lazily (PEP 562):

    from iron.operators import GEMM  # imports iron.operators.gemm, nothing else

The FastFlowLM ports, and the binary they are measured against, are
``flm``'s, a catalog of their own: its GEMM is not this one.
"""

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # the same names, for a checker; the runtime loads them lazily
    from .axpy import AXPY
    from .clamp import Clamp
    from .copy import Copy
    from .depthwise_conv1d import DepthwiseConv1d
    from .dequant import Dequant
    from .elementwise_add import ElementwiseAdd
    from .elementwise_mul import ElementwiseMul, RowwiseMul
    from .emit import Emit
    from .gelu import GELU
    from .gemm import GEMM
    from .gemv import GEMV
    from .gqa import GQAContext, GQAScores
    from .layer_norm import LayerNorm
    from .leaky_relu import LeakyReLU
    from .limbs import Limbs
    from .log import Log
    from .magnitude import Magnitude
    from .merge import Merge
    from .mha import MHA
    from .relu import ReLU
    from .repeat import Repeat
    from .resample.op import PatchPositions, Resample, ResampleTaps
    from .rms_norm import RMSNorm
    from .rope import RoPE
    from .sample import Sample
    from .sigmoid import Sigmoid
    from .silu import SiLU
    from .softmax import Softmax
    from .tanh import Tanh
    from .transpose import Transpose


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
    "GQAContext": "gqa",
    "GQAScores": "gqa",
    "LayerNorm": "layer_norm",
    "LeakyReLU": "leaky_relu",
    "Limbs": "limbs",
    "Log": "log",
    "Magnitude": "magnitude",
    "Merge": "merge",
    "MHA": "mha",
    "PatchPositions": "resample.op",
    "ReLU": "relu",
    "RMSNorm": "rms_norm",
    "Repeat": "repeat",
    "Resample": "resample.op",
    "ResampleTaps": "resample.op",
    "RoPE": "rope",
    "RowwiseMul": "elementwise_mul",
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
