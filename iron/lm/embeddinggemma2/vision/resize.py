# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The size the image processor resizes an image to."""

import math

from .model import VisionConfig


def size(height: int, width: int, max_tokens: int, config: VisionConfig):
    """The `(height, width)` the processor resizes an image to: the largest
    whole `pool * patch` blocks within `max_tokens` soft tokens at the
    image's aspect ratio.

    Args:
        height: The image's height in pixels.
        width: The image's width in pixels.
        max_tokens: The processor's `max_soft_tokens`.
        config: The tower's shape.

    Returns:
        The resized `(height, width)`.

    Raises:
        ValueError: Both sides round to no block, or the size exceeds the budget.
    """
    side = config.pool * config.patch
    max_patches = max_tokens * config.pool**2
    target_px = max_patches * config.patch**2
    factor = math.sqrt(target_px / (height * width))
    out_height = int(math.floor(factor * height / side)) * side
    out_width = int(math.floor(factor * width / side)) * side
    if out_height == 0 and out_width == 0:
        raise ValueError(f"a {height}x{width} image rounds to no {side}-pixel block")
    max_side = max_tokens * side
    if out_height == 0:
        out_height = side
        out_width = min(int(math.floor(width / height)) * side, max_side)
    elif out_width == 0:
        out_width = side
        out_height = min(int(math.floor(height / width)) * side, max_side)
    if out_height * out_width > target_px:
        raise ValueError(
            f"resizing {height}x{width} to {out_height}x{out_width} exceeds "
            f"{max_patches} patches"
        )
    return out_height, out_width
