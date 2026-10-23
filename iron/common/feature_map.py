# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The graphs ``iron.functional``'s CNN functions are built on, each over
the rows of a channels-last feature map, ``(rows, width * channels)``.
"""

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron import Precision, Scratchpad
from iron.operators.copy import Copy
from iron.operators.elementwise_max import ElementwiseMax
from iron.operators.gemm import GEMM

# What every device's GEMM row block divides (aie2's 16 rows, aie2p's 8).
GEMM_ROWS = 16
# GEMM's default tile_n, which a patches GEMM's pixels are padded to.
GEMM_COLUMNS = GEMM.declaration.params["tile_n"].default


class Conv2d(iron.Graph):
    """A 2-D convolution without bias of rows of ``width`` channels-last
    pixels, at ``stride``, the width padded with ``padding`` zero columns
    and each output row with ``border`` zero pixels either side; padding in
    rows is rows the input holds, so a producer writes past them in place.

    A call takes ``(rows, width * channels)`` and the per-call ``rows`` it
    computes, and writes ``(out_rows, (out_width + 2 * border) *
    out_channels)`` where a caller gives it, else returns it. One channel
    (or depthwise) is a GEMM of ``kernel`` gathered rows by the weight laid
    out as a band over the width; a ragged last block of ``GEMM_ROWS`` rows
    repeats the first row, so its output cannot be given. More channels
    are a GEMM of the output channels, as its rows, by the gathered
    ``kernel * kernel * channels`` patches; pixels short of a whole
    ``GEMM_COLUMNS`` repeat the first patch, so their output cannot be
    given either. Each GEMM sums in float32 and rounds once.

    Args:
        weight: ``(out_channels, channels_per_group, kernel, kernel)``,
            ``channels_per_group`` the checkpoint's own (``in_channels //
            groups``, as a depthwise checkpoint already stores it).
        width: The input's pixels a row, its held padding among them.
        stride: The step between output pixels, and rows.
        padding: The zero columns either side of the width, one channel only.
        border: The zero pixels either side of each output row, one channel
            only.
        groups: ``1`` (every output channel reads every input channel) or
            ``out_channels`` (depthwise: each its own). No other grouping is
            built.
    """

    def __init__(
        self,
        weight: np.ndarray,
        width: int,
        stride: int = 1,
        padding: int = 0,
        border: int = 0,
        groups: int = 1,
    ):
        w = np.asarray(weight, np.float32)
        C_out, channels_per_group, k, _ = w.shape
        depthwise = groups > 1
        if depthwise and (groups != C_out or channels_per_group != 1):
            raise ValueError(
                "Conv2d: groups > 1 is depthwise only: groups must equal "
                "out_channels, and the weight's own channel axis must be 1"
            )
        C = groups if depthwise else channels_per_group
        banded = C == 1 or depthwise
        if not banded and (padding or border):
            raise ValueError(
                "Conv2d: gathered patches hold no zero padding or border; with "
                "more than one channel (not depthwise) the input holds its "
                "padding columns"
            )
        self.width, self.stride, self.padding, self.border = (
            width,
            stride,
            padding,
            border,
        )
        self.channels, self.out_channels, self.kernel = C, C_out, k
        self.banded, self.depthwise = banded, depthwise
        self.out_width = (width + 2 * padding - k) // stride + 1
        if self.out_width < 1:
            raise ValueError(
                f"Conv2d: a {k}-wide kernel does not fit {width} pixels padded "
                f"by {padding}"
            )
        self.out_line = (self.out_width + 2 * border) * C_out
        if C == 1:
            band = np.zeros((k, width, self.out_width + 2 * border, C_out), np.float32)
            for f in range(self.out_width):
                for b in range(k):
                    i = stride * f - padding + b
                    if 0 <= i < width:
                        band[:, i, f + border] = w[:, 0, :, b].T
            matrix = band.reshape(k * width, self.out_line)
        elif depthwise:
            band = np.zeros(
                (k, width, C, self.out_width + 2 * border, C_out), np.float32
            )
            channel = np.arange(C)
            for f in range(self.out_width):
                for b in range(k):
                    i = stride * f - padding + b
                    if 0 <= i < width:
                        band[:, i, channel, f + border, channel] = w[:, 0, :, b].T
            matrix = band.reshape(k * width * C, self.out_line)
        else:
            matrix = w.transpose(0, 2, 3, 1).reshape(C_out, k * k * C)
        self.matrix = iron.param(matrix.astype(bfloat16))

    def body(self, x, y=None, *, rows: Scratchpad[np.int32]):
        k, s, C = self.kernel, self.stride, self.channels
        R, line = x.shape
        out_rows = (R - k) // s + 1
        if self.banded:
            gathered = TensorAccessPattern(
                (R, line), 0, [out_rows, k * line], [s * line, 1]
            )
            spare = -out_rows % GEMM_ROWS
            if not spare:
                a = Copy.step(x, src=gathered).reshape(out_rows, k * line)[:rows]
                return GEMM.step(
                    a,
                    self.matrix,
                    *([] if y is None else [y]),
                    precision=Precision.HIGHEST,
                )
            if y is not None:
                raise ValueError(
                    f"Conv2d: {out_rows} output rows are not whole {GEMM_ROWS}-row "
                    f"blocks, so the GEMM computes {spare} more than a caller's "
                    f"output holds; take the returned output instead"
                )
            first = TensorAccessPattern((R, line), 0, [1, k * line], [s * line, 1])
            a = Copy.step(x, src=(gathered, *[first] * spare))
            out = GEMM.step(
                a.reshape(out_rows + spare, k * line),
                self.matrix,
                precision=Precision.HIGHEST,
            )
            return out[:rows]
        n = out_rows * self.out_width
        patches = TensorAccessPattern(
            (R, line),
            0,
            [out_rows, self.out_width, k, k * C],
            [s * line, s * C, line, 1],
        )
        spare = -n % GEMM_COLUMNS
        if spare and y is not None:
            raise ValueError(
                f"Conv2d: {n} output pixels are not whole {GEMM_COLUMNS}-pixel "
                f"tiles, so the GEMM computes {spare} more than a caller's "
                f"output holds; take the returned output instead"
            )
        src = patches
        if spare:
            first = TensorAccessPattern((R, line), 0, [spare, k, k * C], [0, line, 1])
            src = (patches, first)
        a = Copy.step(x, src=src).reshape(n + spare, k * k * C)
        # The few output channels as M, so that the patches span every
        # column; every row, as a GEMM bounds no N, and the output after.
        out = [] if y is None else [y.reshape(n, self.out_channels)]
        h = GEMM.step(
            self.matrix,
            a,
            *out,
            b_col_maj=True,
            c_col_maj=True,
            precision=Precision.HIGHEST,
        )
        if spare:
            h = h[:n]
        h = h if y is not None else h[: rows * self.out_width]
        return None if y is not None else h.reshape(out_rows, self.out_line)


class MaxPool2d(iron.Graph):
    """Max pooling of ``rows`` rows of ``width`` channels-last pixels, each
    channel on its own, by a ``kernel``-wide square window at stride 1,
    padded with ``-inf`` so the output is the input's shape.

    The input is written into a held ``-inf`` border, and the ``kernel *
    kernel`` shifted views of it are combined by a running
    ``ElementwiseMax``, a selection, so exact.

    Args:
        rows: The input's rows.
        width: The input's pixels a row.
        channels: The channels a pixel.
        kernel: The window's side, odd.
    """

    def __init__(self, rows: int, width: int, channels: int, kernel: int):
        if kernel % 2 == 0:
            raise ValueError(
                f"MaxPool2d: kernel ({kernel}) must be odd, for same padding"
            )
        self.rows, self.width, self.channels, self.kernel = (
            rows,
            width,
            channels,
            kernel,
        )
        pad = kernel // 2
        shape = (rows + 2 * pad, (width + 2 * pad) * channels)
        self.border = iron.param(np.full(shape, -np.inf, bfloat16))
        self.padded = iron.state(shape)

    def body(self, x):
        k, C, pad = self.kernel, self.channels, self.kernel // 2
        shape = self.padded.shape
        line = shape[1]
        Copy.step(self.border, self.padded)
        interior = TensorAccessPattern(
            shape, pad * line + pad * C, [self.rows, self.width * C], [line, 1]
        )
        Copy.step(x, self.padded, dst=interior)
        pooled = None
        for a in range(k):
            for b in range(k):
                view = TensorAccessPattern(
                    shape, a * line + b * C, [self.rows, self.width * C], [line, 1]
                )
                window = Copy.step(self.padded, src=view)
                # A pixel's channels are a line any plane divides into.
                pooled = (
                    window
                    if pooled is None
                    else ElementwiseMax.step(pooled, window, tile_size=C)
                )
        return pooled.reshape(self.rows, self.width * C)

    def exact(self, x: np.ndarray) -> np.ndarray:
        """The max pooling of ``x`` ``(rows, width * channels)`` in float32."""
        k, pad = self.kernel, self.kernel // 2
        image = np.asarray(x, np.float32).reshape(self.rows, self.width, self.channels)
        image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), constant_values=-np.inf)
        windows = np.stack(
            [
                image[a : a + self.rows, b : b + self.width]
                for a in range(k)
                for b in range(k)
            ]
        )
        return windows.max(axis=0).reshape(self.rows, self.width * self.channels)


class ConcatChannels(iron.Graph):
    """Two to four inputs of ``rows`` rows of ``width`` channels-last pixels
    concatenated along their channels, ``channels`` each input's a pixel.

    Each input is copied into its channels of a held buffer, which a last
    copy returns.

    Args:
        rows: The inputs' rows.
        width: The inputs' pixels a row.
        channels: Each input's channels a pixel, two to four of them.
    """

    def __init__(self, rows: int, width: int, channels: tuple[int, ...]):
        if not 2 <= len(channels) <= 4:
            raise ValueError(
                f"ConcatChannels: {len(channels)} inputs; it joins two to four"
            )
        if any(c % 2 for c in channels):
            raise ValueError(
                f"ConcatChannels: channels {tuple(channels)} are not all even; "
                f"each input's run of a pixel is one transfer of whole 4-byte units"
            )
        self.rows, self.width, self.channels = rows, width, tuple(channels)
        self.out = iron.state((rows, width * sum(channels)))

    def body(self, x0, x1, x2=None, x3=None):
        xs = [x for x in (x0, x1, x2, x3) if x is not None]
        if len(xs) != len(self.channels):
            raise TypeError(
                f"ConcatChannels: {len(xs)} inputs given, {len(self.channels)} "
                f"declared"
            )
        total = sum(self.channels)
        offset = 0
        for x, c in zip(xs, self.channels):
            dst = TensorAccessPattern(
                self.out.shape,
                offset,
                [self.rows, self.width, c],
                [self.width * total, total, 1],
            )
            Copy.step(x, self.out, dst=dst)
            offset += c
        return Copy.step(self.out[:])
