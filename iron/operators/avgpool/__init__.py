# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE AveragePool Operator

2D average pooling operations for AIE2 and AIE2P architectures.

Usage:
    from iron.operators.avgpool import AIEAveragePool2d

    operator = AIEAveragePool2d(
        kernel_size=2,
        stride=2,
        padding=0,
    )
    result = operator(input_tensor)
"""

from .op import AIEAveragePool2d

__all__ = ["AIEAveragePool2d"]
