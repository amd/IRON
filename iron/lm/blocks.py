# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The blocks a model builds from operators, for a graph's body.

A graph here is called in a model's body as it is on its own (``Graph``):
its steps trace into the model's. Weights are a checkpoint's ``(out, in)``,
projected by ``F.linear``.
"""

import dataclasses
import math
from functools import partial

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, Scratchpad
from iron.common.image.packaging import require_device
from iron.operators.axpy import AXPY
from iron.operators.copy import Copy
from iron.operators.elementwise_max import ElementwiseMax
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs, stacked
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.resample.op import SIDE, PatchPositions, Resample, ResampleTaps


def filterbank(fft: int, mels: int, sample_rate: int, max_hz: float) -> np.ndarray:
    """The ``(fft // 2 + 1, mels)`` HTK mel triangles over the rfft's bins,
    from 0 Hz to ``max_hz``, unnormalized, float64.
    """
    mel = np.linspace(0, 2595 * math.log10(1 + max_hz / 700), mels + 2)
    edges = 700 * (10 ** (mel / 2595) - 1)
    bins = np.linspace(0, sample_rate // 2, fft // 2 + 1)
    slopes = edges[None, :] - bins[:, None]
    widths = np.diff(edges)
    return np.maximum(
        0, np.minimum(-slopes[:, :-2] / widths[:-1], slopes[:, 2:] / widths[1:])
    )


class LogMel(iron.Graph):
    """The log-mel spectrogram of float32 samples, as Hugging Face's Gemma 4
    feature extractor computes it: frame ``f`` is the ``frame`` samples from
    ``f * hop`` under a periodic Hann window, its rfft over ``fft`` points,
    the magnitude through ``mels`` HTK triangles to ``max_hz``, and the log
    of that plus ``mel_floor``, rounded once to bf16.

    A call takes ``(F + 1) * hop`` samples for ``F`` frames, a whole number
    of rows of four, and the per-call ``frames`` it computes; it writes
    ``features``, ``(F, mels)``, where a caller gives them (a state's rows),
    else returns them, past ``frames`` unwritten. The rfft and the filterbank
    are GEMMs of exact float32 products, each operand six planes of its bf16
    limbs (``Limbs``), the bins padded with zeros to whole 64-column tiles;
    ``Magnitude`` and ``Log`` are float32.

    Args:
        frame: The samples of a frame, one to two hops.
        hop: The samples between frames.
        fft: The rfft's points, at least a frame.
        mels: The mel bands.
        sample_rate: The samples per second.
        max_hz: The top of the highest band.
        mel_floor: What the log adds to each energy.
    """

    def __init__(
        self,
        frame: int = 320,
        hop: int = 160,
        fft: int = 512,
        mels: int = 128,
        sample_rate: int = 16000,
        max_hz: float = 8000.0,
        mel_floor: float = 1e-3,
    ):
        if not hop <= frame <= 2 * hop:
            raise ValueError(
                f"LogMel: a frame of {frame} is not one to two {hop}-sample hops"
            )
        if fft < frame:
            raise ValueError(
                f"LogMel: an rfft of {fft} points is shorter than a frame of {frame}"
            )
        self.frame, self.hop, self.fft, self.mels = frame, hop, fft, mels
        self.mel_floor = mel_floor
        self.window = np.hanning(frame + 1)[:-1].astype(np.float32)
        self.filters = filterbank(fft, mels, sample_rate, max_hz)
        bins = fft // 2 + 1
        width = -(-bins // 64) * 64
        angle = 2 * np.pi * np.arange(frame)[:, None] * np.arange(bins) / fft
        window = self.window.astype(np.float64)[:, None]
        # The rfft as a matrix, the window folded in: the real parts, then
        # the imaginary, each padded to the width.
        dft = np.zeros((frame, 2 * width))
        dft[:, :bins] = window * np.cos(angle)
        dft[:, width : width + bins] = -window * np.sin(angle)
        self.dft = stacked(dft)
        self.filterbank = stacked(np.pad(self.filters, ((0, width - bins), (0, 0))))

    def body(self, wave, features=None, *, frames: Scratchpad[np.int32]):
        F = wave.shape[0] // self.hop - 1
        if F % 4:
            raise ValueError(f"LogMel: {F} frames are not whole rows of four")
        # Frame f is hops f and f + 1; in three dimensions, as d1 wraps at
        # 1023 and d2 does not, so that one descriptor holds it.
        windows = TensorAccessPattern(
            wave.shape, 0, [F // 4, 4, self.frame], [4 * self.hop, self.hop, 1]
        )
        a = Copy.step(wave, src=windows, dtype=np.float32).reshape(F, self.frame)[
            :frames
        ]
        exact = dict(tile_m=32, output_dtype=np.float32, precision=Precision.HIGHEST)
        spectrum = GEMM.step(Limbs.step(a), self.dft, **exact)
        energy = GEMM.step(
            Limbs.step(Magnitude.step(spectrum)), self.filterbank, **exact
        )
        if features is None:
            return Log.step(energy, offset=self.mel_floor)
        return Log.step(energy, features, offset=self.mel_floor)


# What every device's GEMM row block divides (aie2's 16 rows, aie2p's 8).
GEMM_ROWS = 16


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
    ``kernel * kernel * channels`` patches. Each GEMM sums in float32 and
    rounds once.

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
            self.matrix = band.reshape(k * width, self.out_line).astype(bfloat16)
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
            self.matrix = band.reshape(k * width * C, self.out_line).astype(bfloat16)
        else:
            self.matrix = w.transpose(0, 2, 3, 1).reshape(C_out, k * k * C)
            self.matrix = self.matrix.astype(bfloat16)

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
        a = Copy.step(x, src=patches).reshape(n, k * k * C)
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
        h = h if y is not None else h[: rows * self.out_width]
        return None if y is not None else h.reshape(out_rows, self.out_line)


class Conv1d(iron.Graph):
    """A 1-D convolution over rows (time) of ``(rows, channels)``, at
    ``stride``, plus ``bias``: the ``kernel`` consecutive rows gathered whole
    and projected in one GEMM, plus the bias on every row. A
    call computes the per-call ``rows`` and writes ``(out_rows,
    out_channels)`` where a caller gives it, else returns it; padding in
    rows is rows the input holds.

    Args:
        weight: ``(out_channels, channels, kernel)``.
        bias: ``(out_channels,)``.
        channels: The input's channels a row.
        stride: The step between output rows.
    """

    def __init__(
        self,
        weight: np.ndarray,
        bias: np.ndarray,
        channels: int,
        stride: int = 1,
    ):
        w = np.asarray(weight, np.float32)
        C_out, C, k = w.shape
        if C != channels:
            raise ValueError(f"Conv1d: weight holds {C} channels, not {channels}")
        self.channels, self.out_channels, self.kernel, self.stride = C, C_out, k, stride
        # Kernel tap as the slower axis, channel the faster: the same order
        # a contiguous k * channels row gather reads them in.
        self.matrix = w.transpose(2, 1, 0).reshape(k * C, C_out).astype(bfloat16)
        self.bias = iron.weight(np.asarray(bias, np.float32).astype(bfloat16))

    def body(self, x, y=None, *, rows: Scratchpad[np.int32]):
        k, s = self.kernel, self.stride
        R, line = x.shape
        out_rows = (R - k) // s + 1
        pattern = TensorAccessPattern((R, line), 0, [out_rows, k * line], [s * line, 1])
        a = Copy.step(x, src=pattern).reshape(out_rows, k * line)[:rows]
        h = GEMM.step(a, self.matrix, precision=Precision.HIGHEST) + self.bias
        return Copy.step(h, y) if y is not None else h


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
        self.border = np.full(shape, -np.inf, bfloat16)
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


class ImagePatches(iron.Graph):
    """A decoded image resized as torchvision's antialiased bicubic resize
    does it, rescaled to ``[0, 1]`` and cut into a vision tower's
    ``patches`` rows of 16x16-pixel patches, each soft token's ``pool ** 2``
    patches consecutive, row-major within its window, the tokens row-major
    over the image.

    A call takes the image, ``(height, width, 3)`` uint8 laid out by
    ``pack``, and per call its size and the ``pool * 16``-pixel windows it
    is resized to. It returns the pixels, ``(patches, 768)`` bf16, each
    patch's ``xy`` (x and y side by side) and ``position_ids`` (every x,
    then every y plus ``positions``); rows past the image are the zero
    patch at ids ``positions`` and ``2 * positions``, past each table, which
    a gather bounded to the image's patches never reads.

    Args:
        patches: The patch rows of a call.
        image: The ``(height, width)`` of the largest image a call takes
            either way up.
        pool: A soft token's side in patches.
        positions: The rows of each axis's position table.
        patch_columns: The patch columns a core holds.
        chunk: The bytes of an image row ``Resample`` receives at a time.
    """

    def __init__(
        self,
        patches: int,
        image: tuple[int, int],
        pool: int = 3,
        positions: int = 10240,
        patch_columns: int = 8,
        chunk: int = 4096,
    ):
        self.patches, self.image, self.pool, self.chunk = patches, image, pool, chunk
        k, side = pool, pool * SIDE
        cores = 2 * require_device().cols
        # The most pooling windows across: Resample's cores hold
        # `patch_columns` patch columns each, one a zero column past the image.
        self.across = (patch_columns * cores - 1) // k
        # Every grid of whole pooling windows the rows hold; the fewest patch
        # columns give the most bands and padded raster rows.
        grids = [(patches // s // k * k, s) for s in range(k, patches // k + 1, k)]
        shared = dict(
            height=side,
            width=side,
            out_height=side,
            out_width=side,
            chunk=chunk,
            patch_columns=patch_columns,
            width_chunks=patch_columns * cores,
            height_chunks=16 * -(-grids[0][0] // 16),
            patch_rows=max(b * (s // cores + 1) * cores for b, s in grids),
            num_aie_columns=cores // 2,
            num_channels=2,
        )
        a, b = image
        self.resample = Resample(
            image_chunks=max(a * -(-3 * b // chunk), b * -(-3 * a // chunk)),
            **shared,
        )
        self.raster = iron.state((shared["patch_rows"], 3 * SIDE**2))
        taps = dict(
            in_size=side,
            out_size=side,
            words=self.resample.words,
            slots=SIDE,
            num_aie_columns=cores // 2,
            num_channels=2,
        )
        self.taps_w = ResampleTaps(chunks=shared["width_chunks"], **taps)
        self.taps_h = ResampleTaps(chunks=shared["height_chunks"], **taps)
        self.patch_positions = PatchPositions(
            rows=patches,
            out_height=side,
            out_width=side,
            pool=k,
            positions=positions,
            cores=cores,
        )

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        T = self.patches
        taps_w = self.taps_w.apply(in_samples=width, out_samples=out_width)
        taps_h = self.taps_h.apply(in_samples=height, out_samples=out_height)
        self.resample.apply(
            rgb,
            taps_w,
            taps_h,
            self.raster,
            rows=height,
            columns=width,
            out_rows=out_height,
            out_columns=out_width,
        )
        xy, position_ids, order = self.patch_positions.apply(
            out_rows=out_height, out_columns=out_width
        )
        return (
            Copy.step(self.raster[order]),
            xy.reshape(2 * T),
            position_ids.reshape(2 * T),
        )

    def pack(self, image, out_height: int, out_width: int) -> tuple[np.ndarray, dict]:
        """A call's image buffer and per-call sizes for a decoded ``image``
        resized to ``out_height`` by ``out_width``.

        Args:
            image: ``(height, width, 3)`` uint8.
            out_height: The rows it is resized to.
            out_width: The columns it is resized to.

        Raises:
            ValueError: The image or its patches do not fit a call, or
                ``Resample`` cannot resize it.
        """
        image = np.asarray(image)
        if image.dtype != np.uint8 or image.ndim != 3 or image.shape[2] != 3:
            raise ValueError(
                f"an image is (height, width, 3) uint8, not {image.shape} {image.dtype}"
            )
        H, W, _ = image.shape
        n = out_height // SIDE * (out_width // SIDE)
        line = -(-3 * W // self.chunk) * self.chunk
        op = self.resample
        if n > self.patches or op.image_chunks * self.chunk < H * line:
            a, b = self.image
            raise ValueError(
                f"a {H}x{W} image of {n} patches does not fit a call's "
                f"{self.patches} patches or {a}x{b} image"
            )
        # Resample's own checks refuse a size it cannot resize.
        dataclasses.replace(
            op, height=H, width=W, out_height=out_height, out_width=out_width
        )
        buffer = np.zeros((op.image_chunks, self.chunk), np.uint8)
        rows = buffer.reshape(-1)[: H * line].reshape(H, line)
        rows[:, : 3 * W] = image.reshape(H, 3 * W)
        return buffer, dict(
            height=H, width=W, out_height=out_height, out_width=out_width
        )


def _linear(x, p, **kw):
    """``x`` through the linear module ``p``: its ``weight``, and its
    ``bias`` where it holds one.
    """
    return F.linear(x, p.weight, vars(p).get("bias"), **kw)


@dataclasses.dataclass(frozen=True)
class Norm:
    """A norm module's: an RMS norm by its ``weight``, or with ``bias`` an
    affine LayerNorm.
    """

    eps: float
    bias: bool = False

    def __call__(self, w, x):
        if self.bias:
            return F.layer_norm(x, x.shape[-1:], w.weight, w.bias, self.eps)
        return F.rms_norm(x, x.shape[-1:], w.weight, self.eps)


@dataclasses.dataclass(frozen=True)
class Attention:
    """Self-attention over an attention module's ``q_proj``, ``k_proj``,
    ``v_proj`` and ``o_proj``, each with its bias where it holds one. A
    model kind gives the attention itself: ``attend(q, k, v, scale=,
    window=)`` on ``(rows, heads, head_dim)`` returns ``(rows, heads *
    head_dim)``.

    Args:
        heads: The query heads.
        groups: The key and value heads.
        head_dim: A head's width.
        eps: The q, k and v norms' epsilon, needed where one is set.
        qk_norm: Whether each head of q and k is RMS-normed by the module's
            ``q_norm`` and ``k_norm``.
        v_norm: Whether each head of v is RMS-normed, unweighted.
        scale: The logits' scale; None is ``head_dim ** -0.5``.
        window: The positions a query reaches either side; None is all.
        rotary: The leading columns of a head RoPE turns, the rest passed
            through; None is all.
        precision: Every projection's ``Precision``; None is ``F.linear``'s.
    """

    heads: int
    groups: int
    head_dim: int
    eps: float | None = None
    qk_norm: bool = False
    v_norm: bool = False
    scale: float | None = None
    window: int | None = None
    rotary: int | None = None
    precision: Precision | None = None

    def __post_init__(self):
        if (self.qk_norm or self.v_norm) and self.eps is None:
            raise ValueError("Attention: a q, k or v norm needs its eps")

    def __call__(self, w, x, attend, angles):
        """The block on ``x`` ``(rows, width)``; ``angles``, a row per
        position, turns q and k (None: no RoPE).
        """
        n, H, G, D = x.shape[0], self.heads, self.groups, self.head_dim
        q, k, v = (
            _linear(x, p, precision=self.precision, **self.head_tiles(n))
            for p in (w.q_proj, w.k_proj, w.v_proj)
        )
        q, k, v = q.reshape(n * H, D), k.reshape(n * G, D), v.reshape(n * G, D)
        if self.qk_norm:
            q = F.rms_norm(q, (D,), w.q_norm.weight, self.eps)
            k = F.rms_norm(k, (D,), w.k_norm.weight, self.eps)
        if self.v_norm:
            v = F.rms_norm(v, (D,), eps=self.eps)
        if angles is not None:
            q, k = self.rotate(q, angles), self.rotate(k, angles)
        o = attend(
            q.reshape(n, H, D),
            k.reshape(n, G, D),
            v.reshape(n, G, D),
            scale=self.scale,
            window=self.window,
        )
        return _linear(o, w.o_proj, precision=self.precision)

    def head_tiles(self, rows: int) -> dict:
        """For one row, GEMV tiles of half a head. Set here, not in the
        profile: q's shape is o's when ``heads * head_dim`` is the width, so
        the profile cannot tell them apart.
        """
        return dict(tile_size_output=self.head_dim // 2) if rows == 1 else {}

    def rotate(self, x, angles):
        """``x`` ``(rows, head_dim)`` turned by RoPE, only its first
        ``rotary`` columns where given.
        """
        if self.rotary is None:
            return F.rope(x, angles)
        x[:, : self.rotary] = F.rope(Copy.step(x[:, : self.rotary]), angles)
        return x

    def keys_values(self, w, memory) -> tuple:
        """The keys and values ``w`` projects from an encoder's output
        ``memory`` ``(rows, width)``, each ``(rows, groups, head_dim)``.
        """
        n, G, D = memory.shape[0], self.groups, self.head_dim
        return tuple(
            _linear(memory, p, precision=self.precision).reshape(n, G, D)
            for p in (w.k_proj, w.v_proj)
        )

    def cross(self, w, x, cross):
        """The block on ``x`` attending over an encoder's keys and values:
        ``cross(q, scale=)`` on ``(rows, heads, head_dim)``.
        """
        n, H, D = x.shape[0], self.heads, self.head_dim
        q = _linear(x, w.q_proj, precision=self.precision, **self.head_tiles(n))
        o = cross(q.reshape(n, H, D), scale=self.scale)
        return _linear(o, w.o_proj, precision=self.precision)


@dataclasses.dataclass(frozen=True)
class MLP:
    """A feed-forward module's: ``down_proj(act(gate_proj(x)) * up_proj(x))``,
    or plain, ``fc2(act(fc1(x)))``.

    Args:
        activation: ``hidden_act``, ``"silu"`` or ``"gelu_pytorch_tanh"``.
        gated: Whether it is gated.
        precision: Every projection's ``Precision``; None is ``F.linear``'s.
    """

    activation: str = "silu"
    gated: bool = True
    precision: Precision | None = None

    def __post_init__(self):
        if self.activation not in ("silu", "gelu_pytorch_tanh"):
            raise ValueError(
                f"MLP: no operator for hidden_act {self.activation!r}; "
                "silu and gelu_pytorch_tanh have one"
            )

    def act(self, x):
        if self.activation == "silu":
            return F.silu(x)
        return F.gelu(x, approximate="tanh")

    def __call__(self, w, x):
        act = self.act
        if not self.gated:
            h = act(_linear(x, w.fc1, precision=self.precision))
            return _linear(h, w.fc2, precision=self.precision)
        gate = _linear(x, w.gate_proj, precision=self.precision)
        up = _linear(x, w.up_proj, precision=self.precision)
        return _linear(act(gate) * up, w.down_proj, precision=self.precision)


@dataclasses.dataclass(frozen=True)
class DecoderLayer:
    """A pre-norm transformer layer module's: ``self_attn`` after
    ``input_layernorm``, then ``mlp`` after ``post_attention_layernorm``,
    each block's output added to its residual times ``residual``.
    """

    attention: Attention
    mlp: MLP
    norm: Norm
    residual: float = 1.0

    def __call__(self, w, x, attend, angles):
        x = self.block(
            x,
            w.input_layernorm,
            partial(self.attention, w.self_attn, attend=attend, angles=angles),
        )
        return self.block(x, w.post_attention_layernorm, partial(self.mlp, w.mlp))

    def block(self, x, pre, f, post=None):
        """``x`` plus ``f`` on ``x`` normed by the norm module ``pre``, its
        output normed again by ``post`` where given (``add``).
        """
        h = f(self.norm(pre, x))
        return self.add(x, h if post is None else self.norm(post, h))

    def add(self, x, y):
        """``x`` plus ``y`` times ``residual``, in ``x``'s shape."""
        y = y if y.shape == x.shape else y.reshape(x.shape)
        if self.residual == 1:
            return x + y
        return AXPY.step(y, x, scalar_factor=self.residual)


@dataclasses.dataclass(frozen=True)
class CrossDecoderLayer(DecoderLayer):
    """``DecoderLayer`` with a third block between its two: ``encoder_attn``
    after ``encoder_attn_layer_norm``, attending over an encoder's output.
    """

    def __call__(self, w, x, attend, angles, cross):
        x = self.block(
            x,
            w.input_layernorm,
            partial(self.attention, w.self_attn, attend=attend, angles=angles),
        )
        x = self.block(
            x,
            w.encoder_attn_layer_norm,
            partial(self.attention.cross, w.encoder_attn, cross=cross),
        )
        return self.block(x, w.post_attention_layernorm, partial(self.mlp, w.mlp))

    def keys_values(self, w, memory) -> tuple:
        """The keys and values ``encoder_attn`` projects from ``memory``."""
        return self.attention.keys_values(w.encoder_attn, memory)
