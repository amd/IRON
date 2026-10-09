# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""torchvision's antialiased bicubic resample of a uint8 image, in fixed
point as torch runs it on the CPU: the reference the resample operators are
held to bit for bit.
"""

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Taps:
    """One axis's resampling filter: output `i` is the `count[i]` input
    samples from `start[i]` on, weighted by `weights[i]`, a fixed-point
    fraction of `precision` bits.
    """

    start: np.ndarray
    count: np.ndarray
    weights: np.ndarray
    precision: int


def window(in_size: int, out_size: int) -> int:
    """The most input samples one output of the axis reads.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.

    Returns:
        The filter's window, `2 * ceil(support) + 1`.
    """
    scale = in_size / out_size
    return math.ceil(2.0 * scale if scale >= 1.0 else 2.0) * 2 + 1


def taps(in_size: int, out_size: int) -> Taps:
    """The filter torch resamples `in_size` samples to `out_size` with: Keys'
    cubic (a = -0.5) stretched by the scale when shrinking, its weights
    normalized in float64 and rounded to int16 at the most bits that keep
    the largest below 2^14.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.

    Returns:
        The axis's `Taps`, `weights` `(out_size, window)` int16, zero past
        each output's `count`.
    """
    scale = in_size / out_size
    support = 2.0 * scale if scale >= 1.0 else 2.0
    invscale = 1.0 / scale if scale >= 1.0 else 1.0
    center = scale * (np.arange(out_size) + 0.5)
    start = np.maximum((center - support + 0.5).astype(np.int64), 0)
    end = np.minimum((center + support + 0.5).astype(np.int64), in_size)
    count = np.clip(end - start, 0, window(in_size, out_size))
    j = np.arange(window(in_size, out_size))
    x = np.abs((start[:, None] + j - center[:, None] + 0.5) * invscale)
    a = -0.5
    w = np.where(
        x < 1.0,
        ((a + 2) * x - (a + 3)) * x * x + 1,
        np.where(x < 2.0, ((a * x - 5 * a) * x + 8 * a) * x - 4 * a, 0.0),
    )
    w = np.where(j < count[:, None], w, 0.0)
    total = np.zeros(out_size)
    for k in range(len(j)):
        total = total + w[:, k]
    normalized = (total != 0.0)[:, None]
    w = np.where(normalized, w / np.where(normalized, total[:, None], 1.0), w)
    wt_max = max(0.0, float(np.where(normalized, w, 0.0).max()))
    precision = 0
    while precision < 22 and int(0.5 + wt_max * (1 << (precision + 1))) < 1 << 15:
        precision += 1
    v = w * (1 << precision)
    weights = np.trunc(np.where(v < 0, v - 0.5, v + 0.5)).astype(np.int16)
    return Taps(start, count, weights, precision)


def resize(image: np.ndarray, height: int, width: int) -> np.ndarray:
    """`image` resampled to `(height, width)` as torchvision's antialiased
    bicubic resize does on a uint8 image on the CPU: across first, then
    down, each pass rounded to uint8.

    Args:
        image: `(rows, columns, channels)` uint8.
        height: The output rows.
        width: The output columns.

    Returns:
        `(height, width, channels)` uint8.
    """
    out = image
    for axis, size_out in ((1, width), (0, height)):
        if out.shape[axis] == size_out:
            continue
        t = taps(out.shape[axis], size_out)
        acc = np.full(
            out.shape[:axis] + (size_out,) + out.shape[axis + 1 :],
            1 << (t.precision - 1),
            np.int32,
        )
        weight_shape = (size_out,) + (1,) * (out.ndim - axis - 1)
        for k in range(t.weights.shape[1]):
            index = np.minimum(t.start + k, out.shape[axis] - 1)
            pixels = np.take(out, index, axis=axis).astype(np.int32)
            acc += pixels * t.weights[:, k].astype(np.int32).reshape(weight_shape)
        out = np.clip(acc >> t.precision, 0, 255).astype(np.uint8)
    return out
