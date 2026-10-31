# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Conv2d``, a convolution over the rows of a channels-last feature map.

The map is ``(rows, width * channels)``.
"""

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron import Precision, Scratchpad
from iron.operators.copy import Copy
from iron.operators.gemm import GEMM

# What every device's GEMM row block divides (aie2's 16 rows, aie2p's 8).
GEMM_ROWS = 16
# GEMM's default tile_n, which a patches GEMM's pixels are padded to.
GEMM_COLUMNS = GEMM.declaration.params["tile_n"].default


class Conv2d(iron.Graph):
    """A bias-free 2-D convolution of channels-last rows ``(rows, width * channels)``.

    Any row padding is held in the input. It computes the per-call ``rows``
    of ``(out_rows, (out_width + 2 * border) * out_channels)`` summed in
    float32. Its output is written to a given ``y`` only when it fills whole
    GEMM blocks.

    Args:
        weight: ``(out_channels, in_channels // groups, kernel, kernel)``.
        width: The input's pixels a row, its held padding among them.
        stride: The step between output pixels, and rows.
        padding: The zero columns either side of the width; one channel or
            depthwise only.
        border: The zero pixels either side of each output row; one channel or
            depthwise only.
        groups: ``1``, or ``out_channels`` (depthwise); no other grouping is built.
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
