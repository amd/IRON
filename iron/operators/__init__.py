# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library."""

from . import flm
from .axpy import AXPY
from .clamp import Clamp
from .copy import Copy, Gather, GatherWords
from .depthwise_conv1d import DepthwiseConv1d
from .elementwise_add import ElementwiseAdd, RowwiseAdd
from .elementwise_max import ElementwiseMax
from .elementwise_mul import ElementwiseMul, RowwiseMul
from .emit import Emit
from .experts import Experts
from .gated_delta_rule import GatedDeltaRule
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
from .selective_scan import SelectiveScan
from .sigmoid import Sigmoid
from .silu import SiLU
from .softmax import Softmax
from .tanh import Tanh

__all__ = sorted(name for name in dir() if name[0].isupper())

#: Every operator by the name a profile gives it, flm's as ``"flm.<name>"``.
CATALOG = {name: globals()[name] for name in __all__} | {
    f"flm.{name}": getattr(flm, name) for name in flm.__all__
}
