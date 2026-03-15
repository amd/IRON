# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE Conv3D Operator

3D convolution operations for AIE2 and AIE2P architectures.

Supports:
- Standard 3D convolution (video, spatiotemporal)
- Pointwise convolution (1x1x1) - compute primitive for Linear layers
- Depthwise convolution (channel-wise)
- Grouped convolution (including GQA-style operations)

Usage:
    # Video convolution (semantic use)
    conv3d = AIEConv3d(
        in_channels=64,
        out_channels=128,
        kernel_size=(3, 3, 3),
        stride=(1, 2, 2),
        padding=(1, 1, 1)
    )

    # Compute primitive for text models (shape manipulation)
    # Reshape MHA tensors (B, G, H, S, D_h) for Conv3D processing
    conv3d = AIEConv3d(
        in_channels=G,
        out_channels=G,
        kernel_size=(1, 3, 3),  # Local attention windows
    )
"""

from .op import AIEConv3d

__all__ = ["AIEConv3d"]
