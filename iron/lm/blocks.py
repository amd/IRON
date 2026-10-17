# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The blocks a model builds from operators, for a graph's body.

A graph here is called in a model's body as it is on its own (``Graph``):
its steps trace into the model's. Weights are a checkpoint's ``(out, in)``:
one row projects with GEMV, more with flm.GEMM reading the weight as
stored, and nothing is padded, so a row count the GEMM cannot tile is an
error at trace time.
"""

import dataclasses
import math

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators.axpy import AXPY
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd
from iron.operators.elementwise_max import ElementwiseMax
from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.layer_norm import LayerNorm
from iron.operators.limbs import Limbs, stacked
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.resample.op import SIDE, PatchPositions, Resample, ResampleTaps
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.silu import SiLU

# Each product's float32 sum rounded once.
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)


def project(
    x,
    weight,
    bias=None,
    k_tile=None,
    tile_n=None,
    emulate_bf16_mmul_with_bfp16=None,
    accurate: bool = False,
    **gemv,
):
    """``x @ weight.T`` for a checkpoint's ``(out, in)`` weight, plus
    ``bias`` broadcast over every row if given: a GEMV for one row, else
    flm.GEMM reading it column-major, or with ``accurate`` the GEMM whose
    float32 sums round once (``ACCURATE``). ``k_tile`` and ``tile_n`` are
    flm.GEMM's tunables, where the profile cannot tell it from another of
    its shape (``tile_n``'s ``ct_max_k`` must divide ``k_tile``);
    ``emulate_bf16_mmul_with_bfp16=False`` asks for bf16 macs where the
    device defaults to bfp16's; ``gemv`` are the GEMV's tunables, where the
    profile cannot tell it from another of its shape.

    Raises:
        ValueError: ``accurate`` with one of flm.GEMM's keywords.
    """
    if len(x.shape) == 2 and x.shape[0] > 1:
        tiled = {}
        if k_tile is not None:
            tiled["k_tile"] = k_tile
        if tile_n is not None:
            tiled["tile_n"] = tile_n
        if emulate_bf16_mmul_with_bfp16 is not None:
            tiled["emulate_bf16_mmul_with_bfp16"] = emulate_bf16_mmul_with_bfp16
        if accurate and tiled:
            raise ValueError(f"project(): accurate takes no flm.GEMM {sorted(tiled)}")
        if accurate:
            y = GEMM.step(x, weight, b_col_maj=True, **ACCURATE)
        else:
            y = FLMGEMM.step(
                x, weight, b_col_maj=True, epilogue_modes=(Epilogue.NONE,), **tiled
            )
    else:
        y = GEMV.step(weight, x, **gemv)
    if bias is None:
        return y
    if bias.shape[0] > RowwiseAdd.tile_cap:
        raise ValueError(
            f"project(): bias ({bias.shape[0]} elements) exceeds RowwiseAdd's "
            f"{RowwiseAdd.tile_cap}-element tile_cap; split the projection's "
            "weight and bias once at load time instead of folding them here"
        )
    rows = math.prod(y.shape) // bias.shape[0]
    return RowwiseAdd.step(y.reshape(rows, bias.shape[0]), bias).reshape(y.shape)


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
        exact = dict(
            tile_m=32, dtype_out=np.float32, emulate_bf16_mmul_with_bfp16=False
        )
        spectrum = GEMM.step(Limbs.step(a), self.dft, **exact)
        energy = GEMM.step(
            Limbs.step(Magnitude.step(spectrum)), self.filterbank, **exact
        )
        if features is None:
            return Log.step(energy, offset=self.mel_floor)
        return Log.step(energy, features, offset=self.mel_floor)

    def oracle(self, wave: np.ndarray, frames: int) -> np.ndarray:
        """The first ``frames`` features of ``wave`` in float64, rounded once
        to float32: the extractor's own computation, which the graph's
        reference, its operators', is held to.
        """
        starts = np.arange(frames)[:, None] * self.hop
        rows = np.asarray(wave, np.float32)[starts + np.arange(self.frame)]
        magnitude = np.abs(np.fft.rfft(rows * self.window, n=self.fft, axis=-1))
        return np.log(magnitude @ self.filters + self.mel_floor).astype(np.float32)


# A pre-norm layer's two norms, before attention and before the
# feed-forward, by each family of Hugging Face names.
PRE_NORMS = (
    ("input_layernorm", "post_attention_layernorm"),
    ("layer_norm1", "layer_norm2"),
    ("self_attn_layer_norm", "final_layer_norm"),
)
# The epsilon mlir-aie's layer_norm kernel fixes.
LAYER_NORM_EPS = 1e-5
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
                    a, self.matrix, *([] if y is None else [y]), **ACCURATE
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
                a.reshape(out_rows + spare, k * line), self.matrix, **ACCURATE
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
        h = GEMM.step(self.matrix, a, *out, b_col_maj=True, c_col_maj=True, **ACCURATE)
        h = h if y is not None else h[: rows * self.out_width]
        return None if y is not None else h.reshape(out_rows, self.out_line)

    def oracle(self, x: np.ndarray, weight: np.ndarray) -> np.ndarray:
        """The convolution of ``x`` ``(rows, width * channels)`` by
        ``weight`` in float32, bordered: what the graph's GEMMs compute
        before their one rounding.
        """
        k, s, p = self.kernel, self.stride, self.padding
        w = np.asarray(weight, np.float32)
        image = np.asarray(x, np.float32).reshape(x.shape[0], self.width, self.channels)
        image = np.pad(image, ((0, 0), (p, p), (0, 0)))
        rows = (image.shape[0] - k) // s + 1
        patches = np.stack(
            [
                image[a : a + s * rows : s, b : b + s * self.out_width : s]
                for a in range(k)
                for b in range(k)
            ],
            axis=2,
        )
        if self.depthwise:
            taps = w[:, 0].reshape(self.out_channels, k * k)
            out = np.einsum("rwtc,ct->rwc", patches, taps)
        else:
            taps = w.transpose(2, 3, 1, 0).reshape(-1, self.out_channels)
            out = patches.reshape(rows, self.out_width, -1) @ taps
        out = np.pad(out, ((0, 0), (self.border, self.border), (0, 0)))
        return out.reshape(rows, self.out_line)


class Conv1d(iron.Graph):
    """A 1-D convolution over rows (time) of ``(rows, channels)``, at
    ``stride``, plus ``bias``: the ``kernel`` consecutive rows gathered whole
    and projected in one GEMM, the bias folded on with ``RowwiseAdd``. A
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
        k, s, C = self.kernel, self.stride, self.channels
        R, line = x.shape
        out_rows = (R - k) // s + 1
        pattern = TensorAccessPattern((R, line), 0, [out_rows, k * line], [s * line, 1])
        a = Copy.step(x, src=pattern).reshape(out_rows, k * line)[:rows]
        h = RowwiseAdd.step(GEMM.step(a, self.matrix, **ACCURATE), self.bias)
        return Copy.step(h, y) if y is not None else h

    def oracle(self, x: np.ndarray, weight: np.ndarray, bias: np.ndarray) -> np.ndarray:
        """The convolution of ``x`` ``(rows, channels)`` by ``weight`` and
        ``bias`` in float32: what the graph's GEMM and bias add compute
        before their one rounding each.
        """
        k, s = self.kernel, self.stride
        rows = (x.shape[0] - k) // s + 1
        x = np.asarray(x, np.float32)
        patches = np.stack([x[b : b + s * rows : s] for b in range(k)], axis=1)
        w = (
            np.asarray(weight, np.float32)
            .transpose(2, 1, 0)
            .reshape(-1, self.out_channels)
        )
        return patches.reshape(rows, -1) @ w + np.asarray(bias, np.float32)


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
    patch at ``positions``, the padding row of a table of that many.

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
        cores = 2 * aie_utils.ensure_current_device().cols
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


@dataclasses.dataclass(frozen=True)
class Layer:
    """A transformer layer over a checkpoint's layer module, read by its
    Hugging Face names: attention, then the feed-forward, each after its
    pre-norm and with its residual. Its norms are any family of
    ``PRE_NORMS``, its output projection ``o_proj`` or ``out_proj``.

    The module decides the rest: sandwich norms where it holds
    ``pre_feedforward_layernorm``; a norm's affine LayerNorm where it holds
    a bias, else its RMS norm; per-head q and k RMS norms where
    ``self_attn`` holds ``q_norm`` and ``k_norm``; a projection's bias where
    it holds one, its weight read through a ``linear`` wrapper; one fused
    ``qkv_proj`` or ``gate_up_proj`` cut by rows; a plain ``fc1``, ``fc2``
    feed-forward where ``mlp``, or the layer itself, holds them, else the
    gated one; a per-layer
    input through ``ple_block``; and a ``layer_scalar``. A model kind gives
    the attention and the rotation: ``attend(q, k, v, scale=, window=)`` on
    ``(rows, heads, head_dim)`` returns ``(rows, heads * head_dim)``, and
    ``angles`` turns q and k.

    Args:
        heads: The query heads.
        groups: The key and value heads.
        head_dim: A head's width.
        eps: Every norm's epsilon.
        activation: The feed-forward's ``hidden_act``, ``"silu"`` or
            ``"gelu_pytorch_tanh"``.
        scale: The attention logits' scale; None is ``head_dim ** -0.5``.
        window: The positions a query reaches either side; None is all.
        rotary: The leading columns of a head RoPE turns, the rest passed
            through; None is all.
        v_norm: Whether the values are RMS-normed, unweighted.
        residual: What each block's output is scaled by on its residual
            (``residual_multiplier``).
        accurate: Whether every projection sums in float32 and rounds once
            (``project(accurate=True)``).
    """

    heads: int
    groups: int
    head_dim: int
    eps: float
    activation: str = "silu"
    scale: float | None = None
    window: int | None = None
    rotary: int | None = None
    v_norm: bool = False
    residual: float = 1.0
    accurate: bool = False

    def __post_init__(self):
        if self.activation not in ("silu", "gelu_pytorch_tanh"):
            raise ValueError(
                f"Layer: no operator for hidden_act {self.activation!r}; "
                "silu and gelu_pytorch_tanh have one"
            )

    @staticmethod
    def linear(p) -> tuple:
        """The linear module ``p``'s ``weight`` and ``bias`` (None if it has
        none), through a ``linear`` wrapper.
        """
        p = vars(p).get("linear", p)
        return p.weight, vars(p).get("bias")

    @staticmethod
    def norms(w) -> tuple:
        """``w``'s norm modules: before attention, after it, before the
        feed-forward and after it, the second and fourth None but in a
        sandwich.

        Raises:
            ValueError: ``w`` holds no family of norms ``PRE_NORMS`` names.
        """
        held = vars(w)
        if "pre_feedforward_layernorm" in held:
            return (
                w.input_layernorm,
                w.post_attention_layernorm,
                w.pre_feedforward_layernorm,
                w.post_feedforward_layernorm,
            )
        for before, after in PRE_NORMS:
            if before in held:
                return held[before], None, held[after], None
        raise ValueError(f"Layer: the module holds none of the norms {PRE_NORMS}")

    def projections(self, w) -> tuple[tuple, ...]:
        """``w``'s q, k, v and o projections, then the feed-forward's (gate,
        up and down, or fc1 and fc2), each ``(weight, bias)``; a fused
        ``qkv_proj`` or ``gate_up_proj`` cut by rows, so each piece is a view
        of the checkpoint's own array.
        """
        a = w.self_attn
        mlp = w.mlp if "mlp" in vars(w) else w
        fused = []
        if "qkv_proj" in vars(a):
            Q, KV = self.heads * self.head_dim, self.groups * self.head_dim
            fused.append((a.qkv_proj, (0, Q, Q + KV, Q + 2 * KV)))
        else:
            fused += [(p, None) for p in (a.q_proj, a.k_proj, a.v_proj)]
        fused.append((a.o_proj if "o_proj" in vars(a) else a.out_proj, None))
        if "fc1" in vars(mlp):
            fused += [(mlp.fc1, None), (mlp.fc2, None)]
        elif "gate_up_proj" in vars(mlp):
            F = mlp.gate_up_proj.weight.shape[0] // 2
            fused += [(mlp.gate_up_proj, (0, F, 2 * F)), (mlp.down_proj, None)]
        else:
            fused += [(mlp.gate_proj, None), (mlp.up_proj, None), (mlp.down_proj, None)]
        out = []
        for p, cuts in fused:
            weight, bias = self.linear(p)
            if cuts is None:
                out.append((weight, bias))
                continue
            for lo, hi in zip(cuts, cuts[1:]):
                out.append((weight[lo:hi], None if bias is None else bias[lo:hi]))
        return tuple(out)

    def norm(self, x, n):
        """``x`` normed by the norm module ``n``: an affine LayerNorm where it
        holds a bias, else its RMS norm.

        Raises:
            ValueError: A LayerNorm at an epsilon but its kernel's.
        """
        if "bias" not in vars(n):
            return RMSNorm.step(x, weight=n.weight, epsilon=self.eps)
        if self.eps != LAYER_NORM_EPS:
            raise ValueError(
                f"Layer: LayerNorm's kernel takes no epsilon but {LAYER_NORM_EPS}, "
                f"not {self.eps}"
            )
        return RowwiseAdd.step(RowwiseMul.step(LayerNorm.step(x), n.weight), n.bias)

    def rotate(self, x, angles):
        """``x`` ``(rows, head_dim)`` turned by RoPE, a row of ``angles`` per
        position, only its first ``rotary`` columns where given.
        """
        if self.rotary is None:
            return RoPE.step(x, angles)
        prefix = x[:, : self.rotary]
        Copy.step(RoPE.step(Copy.step(prefix), angles), prefix)
        return x

    def derive(self, derived, w) -> None:
        """Put on ``derived`` (``iron.lm.Derived``) what ``step`` reads of
        ``w`` beyond the checkpoint: a ``layer_scalar`` as the row
        ``RowwiseMul`` takes, ``scale``.
        """
        if "layer_scalar" in vars(w):
            width = self.norms(w)[0].weight.shape[0]
            scalar = w.layer_scalar
            derived.put(w, scale=np.full(width, scalar[0], scalar.dtype))

    def step(self, w, x, attend, angles, *, ple=None, derived=None):
        """The layer on ``x`` ``(rows, width)``, in a graph's body.

        Args:
            w: The checkpoint's layer module.
            x: The layer's input.
            attend: The model kind's attention.
            angles: The RoPE angles, a row per position.
            ple: The per-layer input ``ple_block`` gates, ``(rows, ple_dim)``.
            derived: ``w``'s module of the model's derived tree (``derive``).

        Raises:
            TypeError: The module holds a ``ple_block`` and no ``ple`` is
                given, or a ``layer_scalar`` and no ``derived``.
        """
        n, H, G, D = x.shape[0], self.heads, self.groups, self.head_dim
        a, eps = w.self_attn, self.eps
        q_w, k_w, v_w, o_w, *mlp = self.projections(w)
        before, after, before_mlp, after_mlp = self.norms(w)
        act = SiLU if self.activation == "silu" else GELU
        h = self.norm(x, before)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (
            project(h, *p, accurate=self.accurate, tile_size_output=D // 2)
            for p in (q_w, k_w, v_w)
        )
        q, k, v = q.reshape(n * H, D), k.reshape(n * G, D), v.reshape(n * G, D)
        if "q_norm" in vars(a):
            q = self.norm(q, a.q_norm)
        # One angle row per position, applied to that position's heads.
        q = self.rotate(q, angles)
        if "k_norm" in vars(a):
            k = self.norm(k, a.k_norm)
        k = self.rotate(k, angles)
        if self.v_norm:
            v = RMSNorm.step(v, epsilon=eps)
        o = attend(
            q.reshape(n, H, D),
            k.reshape(n, G, D),
            v.reshape(n, G, D),
            scale=self.scale,
            window=self.window,
        )
        y = project(o, *o_w, accurate=self.accurate)
        if after is not None:
            y = self.norm(y, after)
        r = self.residual
        x = ElementwiseAdd.step(x, y) if r == 1 else AXPY.step(y, x, scalar_factor=r)
        h = self.norm(x, before_mlp)
        if len(mlp) == 2:
            fc1, fc2 = mlp
            f = act.step(project(h, *fc1, accurate=self.accurate))
        else:
            gate_w, up_w, fc2 = mlp
            gate = project(h, *gate_w, accurate=self.accurate)
            up = project(h, *up_w, accurate=self.accurate)
            f = ElementwiseMul.step(act.step(gate), up)
        f = project(f, *fc2, accurate=self.accurate)
        if after_mlp is not None:
            f = self.norm(f, after_mlp)
        x = ElementwiseAdd.step(x, f) if r == 1 else AXPY.step(f, x, scalar_factor=r)
        if "ple_block" in vars(w):
            if ple is None:
                raise TypeError("Layer.step: the module's ple_block needs ple=")
            b = w.ple_block
            g = project(x, *self.linear(b.per_layer_input_gate), accurate=self.accurate)
            g = ElementwiseMul.step(act.step(g), ple)
            g = project(g, *self.linear(b.per_layer_projection), accurate=self.accurate)
            x = ElementwiseAdd.step(x, self.norm(g, b.post_per_layer_input_norm))
        if "layer_scalar" in vars(w):
            if derived is None:
                raise TypeError("Layer.step: the module's layer_scalar needs derived=")
            x = RowwiseMul.step(x, derived.scale)
        return x

    def oracle(self, o, w, x, attend, angles, *, ple=None) -> np.ndarray:
        """``step``'s twin in float32 on the host, from the ``Oracle`` ``o``'s
        primitives.

        Args:
            o: The model's oracle.
            w: The checkpoint's layer module, widened to float32.
            x: The layer's input, ``(rows, width)``.
            attend: The oracle's attention (``Oracle.attend``).
            angles: The RoPE table, or tables (``Oracle.rotate``).
            ple: The per-layer input ``ple_block`` gates.
        """
        n, H, G, D = x.shape[0], self.heads, self.groups, self.head_dim
        a = w.self_attn
        q_w, k_w, v_w, o_w, *mlp = self.projections(w)
        before, after, before_mlp, after_mlp = self.norms(w)
        silu = self.activation == "silu"
        A = self.rotary or D
        h = o.normed(x, before)
        q = o.linear(h, *q_w).reshape(n, H, D)
        k = o.linear(h, *k_w).reshape(n, G, D)
        v = o.linear(h, *v_w).reshape(n, G, D)
        if "q_norm" in vars(a):
            q = o.normed(q, a.q_norm)
        if "k_norm" in vars(a):
            k = o.normed(k, a.k_norm)
        if self.v_norm:
            v = o.rms_norm(v)
        q, k = (
            np.concatenate([o.rotate(t[..., :A], angles), t[..., A:]], axis=-1)
            for t in (q, k)
        )
        y = o.linear(attend(q, k, v, scale=self.scale, window=self.window), *o_w)
        if after is not None:
            y = o.normed(y, after)
        r = np.float32(self.residual)
        x = x + y * r
        h = o.normed(x, before_mlp)
        if len(mlp) == 2:
            fc1, fc2 = mlp
            g = o.linear(h, *fc1)
            f = o.silu(g) if silu else o.gelu_tanh(g)
        else:
            (gate, gate_b), (up, up_b), fc2 = mlp
            F = gate.shape[0]
            g = np.matmul(h, gate.T, out=o.buffer("gate", (n, F)))
            if gate_b is not None:
                g += gate_b
            if silu:
                g *= np.float32(0.5)
                # SiLU, with the sigmoid as a tanh, which does not overflow.
                f = np.tanh(g, out=o.buffer("silu", (n, F)))
                f += 1
                f *= g
            else:
                f = o.gelu_tanh(g)
            u = np.matmul(h, up.T, out=o.buffer("up", (n, F)))
            if up_b is not None:
                u += up_b
            f *= u
        f = o.linear(f, *fc2)
        if after_mlp is not None:
            f = o.normed(f, after_mlp)
        x = x + f * r
        if "ple_block" in vars(w):
            b = w.ple_block
            g = o.linear(x, *self.linear(b.per_layer_input_gate))
            g = o.silu(g) if silu else o.gelu_tanh(g)
            p = o.linear(g * ple, *self.linear(b.per_layer_projection))
            x = x + o.normed(p, b.post_per_layer_input_norm)
        if "layer_scalar" in vars(w):
            x = x * w.layer_scalar
        return x
