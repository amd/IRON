# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON Operators - Machine Learning operators for AIE acceleration."""

from .common.aie_base import AIEOperatorBase, AIEOperatorConstraintError
from .elementwise_add.op import AIEElementwiseAdd
from .elementwise_mul.op import AIEElementwiseMul
from .gemm.op import AIEGEMM
from .gemv.op import AIEGEMV
from .mha.op import AIEMHA
from .rms_norm.op import AIERMSNorm
from .rope.op import AIERope
from .silu.op import AIESiLU
from .softmax.op import AIESoftmax
from .swiglu_decode.op import AIESwiGLUDecode
from .swiglu_prefill.op import AIESwiGLUPrefill

__all__ = [
    # Base classes
    "AIEOperatorBase",
    "AIEOperatorConstraintError",
    # Operators
    "AIEElementwiseAdd",
    "AIEElementwiseMul",
    "AIEGEMM",
    "AIEGEMV",
    "AIEMHA",
    "AIERMSNorm",
    "AIERope",
    "AIESiLU",
    "AIESoftmax",
    "AIESwiGLUDecode",
    "AIESwiGLUPrefill",
]
