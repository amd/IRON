# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE Reduction Operator

Reduction operations (sum, mean, max, min) for AIE2 and AIE2P architectures.

Usage:
    from iron.operators.reduction import AIEReduction

    operator = AIEReduction(
        input_size=4096,
        reduction_size=64,
        reduction_op="sum",
        num_aie_columns=4,
        tile_size=1024,
    )
    result = operator(input_tensor)
"""

from .op import AIEReduction, ReductionOp

__all__ = ["AIEReduction", "ReductionOp"]
