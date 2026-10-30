# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ports of FastFlowLM's Gemma 4 NPU overlays to IRON
(https://github.com/ROCm/FastFlowLM, MIT).
"""

from .dequant.op import DequantBFP
from .gemm.op import ProjectionGEMM
from .layer.op import DecodeLayer
from .lm_head.op import LMHead
from .prefill_attn.op import PrefillAttention, PrefillSlidingAttention

__all__ = [
    "DecodeLayer",
    "DequantBFP",
    "LMHead",
    "PrefillAttention",
    "PrefillSlidingAttention",
    "ProjectionGEMM",
]
