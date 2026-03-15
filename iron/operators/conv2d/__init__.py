# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE 2D Convolution Operator

2D convolution operations for AIE2 and AIE2P architectures.
Supports standard conv2d, depthwise conv2d, and pointwise (1x1) conv2d.

Usage:
    from iron.operators.conv2d import AIEConv2d

    operator = AIEConv2d(
        in_channels=3,
        out_channels=16,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
        use_bias=True,
    )
    result = operator(input_tensor, weight, bias)
"""

from .op import AIEConv2d

__all__ = ["AIEConv2d"]
