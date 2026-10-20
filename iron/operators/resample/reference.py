# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""torchvision's antialiased bicubic or Lanczos resample of a uint8 image,
in fixed point as torch runs it on the CPU: the reference the resample
operators are held to bit for bit.
"""

import math
from dataclasses import dataclass
from enum import StrEnum

import numpy as np


class Interpolation(StrEnum):
    """A resize's filter, by torch's name for it."""

    BICUBIC = "bicubic"
    LANCZOS = "lanczos"

    @property
    def radius(self) -> float:
        """The filter's support, in input samples at a scale of 1."""
        return 3.0 if self is Interpolation.LANCZOS else 2.0

    def weights(self, x: np.ndarray) -> np.ndarray:
        """The filter at `x`, float64: Keys' cubic (a = -0.5), or Lanczos-3,
        `sinc(x) * sinc(x / 3)` with the C library's `sin`, as torch's is.
        """
        x = np.abs(x)
        if self is Interpolation.LANCZOS:
            y = np.stack([x, x / 3.0]) * math.pi
            ratio = np.vectorize(math.sin, otypes=[np.float64])(y) / np.where(y, y, 1.0)
            sinc = np.where(y == 0.0, 1.0, ratio)
            return np.where(x < 3.0, sinc[0] * sinc[1], 0.0)
        a = -0.5
        return np.where(
            x < 1.0,
            ((a + 2) * x - (a + 3)) * x * x + 1,
            np.where(x < 2.0, ((a * x - 5 * a) * x + 8 * a) * x - 4 * a, 0.0),
        )


@dataclass(frozen=True)
class Taps:
    """One axis's resampling filter, `precision`-bit fixed-point weights."""

    start: np.ndarray
    count: np.ndarray
    weights: np.ndarray
    precision: int


def window(
    in_size: int, out_size: int, interpolation: Interpolation = Interpolation.BICUBIC
) -> int:
    """The most input samples one output of the axis reads.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.
        interpolation: The filter.

    Returns:
        The filter's window, `2 * ceil(support) + 1`.
    """
    scale = in_size / out_size
    radius = Interpolation(interpolation).radius
    return math.ceil(radius * scale if scale >= 1.0 else radius) * 2 + 1


def taps(
    in_size: int, out_size: int, interpolation: Interpolation = Interpolation.BICUBIC
) -> Taps:
    """The filter torch resamples `in_size` samples to `out_size` with:
    `interpolation`'s, stretched by the scale when shrinking, its weights
    normalized in float64 and rounded to int16 at the most bits that keep
    the largest below 2^14.

    Args:
        in_size: The input samples on the axis.
        out_size: The output samples on the axis.
        interpolation: The filter.

    Returns:
        The axis's `Taps`, `weights` `(out_size, window)` int16, zero past
        each output's `count`.
    """
    interpolation = Interpolation(interpolation)
    scale = in_size / out_size
    radius = interpolation.radius
    support = radius * scale if scale >= 1.0 else radius
    invscale = 1.0 / scale if scale >= 1.0 else 1.0
    taps_window = window(in_size, out_size, interpolation)
    center = scale * (np.arange(out_size) + 0.5)
    start = np.maximum((center - support + 0.5).astype(np.int64), 0)
    end = np.minimum((center + support + 0.5).astype(np.int64), in_size)
    count = np.clip(end - start, 0, taps_window)
    j = np.arange(taps_window)
    w = interpolation.weights((start[:, None] + j - center[:, None] + 0.5) * invscale)
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


def resize(
    image: np.ndarray,
    height: int,
    width: int,
    interpolation: Interpolation = Interpolation.BICUBIC,
) -> np.ndarray:
    """`image` resampled to `(height, width)` as torchvision's antialiased
    resize does on a uint8 image on the CPU: across first, then down, each
    pass rounded to uint8.

    Args:
        image: `(rows, columns, channels)` uint8.
        height: The output rows.
        width: The output columns.
        interpolation: The filter.

    Returns:
        `(height, width, channels)` uint8.
    """
    out = image
    for axis, size_out in ((1, width), (0, height)):
        if out.shape[axis] == size_out:
            continue
        t = taps(out.shape[axis], size_out, interpolation)
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
