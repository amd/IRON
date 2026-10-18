# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# A checker's view of the names __getattr__ loads lazily at runtime (PEP
# 562); flm's own names are iron/operators/flm/__init__.pyi's.

from .axpy import AXPY
from .clamp import Clamp
from .copy import Copy, Gather, GatherWords
from .depthwise_conv1d import DepthwiseConv1d
from .elementwise_add import ElementwiseAdd, RowwiseAdd
from .elementwise_max import ElementwiseMax
from .elementwise_mul import ElementwiseMul, RowwiseMul
from .emit import Emit
from .experts import Experts
from .gelu import GELU
from .gemm import GEMM
from .gemv import GEMV
from .layer_norm import LayerNorm
from .limbs import Limbs
from .log import Log
from .magnitude import Magnitude
from .merge import Merge
from .mha import MHA
from .relu import ReLU
from .resample.op import PatchPositions, Resample, ResampleTaps
from .rms_norm import RMSNorm
from .rope import RoPE
from .router import TopKRouter
from .sample import Sample
from .sigmoid import Sigmoid
from .silu import SiLU
from .softmax import Softmax
from .tanh import Tanh
from .transpose import Transpose
