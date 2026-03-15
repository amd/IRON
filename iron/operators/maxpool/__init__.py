# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE MaxPool Operator

2D max pooling operations for AIE2 and AIE2P architectures.

Usage:
    from iron.operators.maxpool import AIEMaxPool2d

    operator = AIEMaxPool2d(
        kernel_size=2,
        stride=2,
        padding=0,
    )
    result = operator(input_tensor)
"""

from .op import AIEMaxPool2d

__all__ = ["AIEMaxPool2d"]
