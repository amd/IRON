# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The blocks a model builds from operators, for a graph's body.

``project`` is a weight's projection at either row count. ``swiglu``
is the SwiGLU feed-forward, ``W_down @ (SiLU(W_gate @ x) * (W_up @ x))``,
for one token or a sequence, and ``SwiGLU`` is it as a graph of its
own, holding the weights, so they are uploaded once. ``geglu`` is the
GELU-gated feed-forward over GEMMs, ``sandwich`` a block between two RMS
norms with its residual (Gemma's sandwich norms), and ``attention`` an
encoder's bidirectional attention over one sequence, its queries and keys
RMS-normed and rotated. ``Block`` and ``BlockOracle`` are the attention +
SwiGLU layer Llama 3 and Granite 4.2 3B share, on the NPU and in numpy. ``LogMel`` is an audio front end's log-mel
spectrogram, ``Conv2d`` a convolution over rows of channels-last pixels,
``Conv1d`` one over rows of full-channel-depth input (an audio encoder's
front end), ``MaxPool2d`` a max pooling of channels-last pixels,
``ConcatChannels`` their concatenation along the channels and
``ImagePatches`` a vision front end's resize into patches. A graph
here is called in a model's body as it is on its own (``Graph``): its
steps trace into the model's.

The weights are a checkpoint's ``(out, in)``: SwiGLU's ``w_gate`` and
``w_up`` are ``(hidden_dim, embedding_dim)`` and ``w_down`` is
``(embedding_dim, hidden_dim)``. One row projects with GEMV, more with
flm.GEMM reading the weight as stored. The gate and up projections share
one array and one build. Nothing is padded: a row count the GEMM cannot tile
is an error at trace time.
"""

import dataclasses
import math
from collections.abc import Callable

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd
from iron.operators.elementwise_max import ElementwiseMax
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.limbs import Limbs, stacked
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.mha import MHA
from iron.operators.resample.op import SIDE, PatchPositions, Resample, ResampleTaps
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.silu import SiLU

from .causal import Step


def project(
    x,
    weight,
    bias=None,
    k_tile=None,
    tile_n=None,
    emulate_bf16_mmul_with_bfp16=None,
    **gemv,
):
    """``x @ weight.T`` for a checkpoint's ``(out, in)`` weight, plus
    ``bias`` if given, broadcast over every row (a linear layer's bias,
    Qwen 2's q/k/v projections): a GEMV for one row (a GEMV's output is a
    vector, batched into a row or not depending on its shape against the
    weight's), else flm.GEMM reading it column-major, ``k_tile`` if K is not
    a multiple of its default 512 (flm.GEMM's own ``k_tile``; Qwen 2.5's
    hidden_dim is not). ``tile_n`` with ``k_tile``, where the default
    ``tile_n``'s ``ct_max_k`` (128) does not divide a ``k_tile`` that does
    divide K (SmolVLM's emb_dim, 576, is 2**6 * 3**2, under 128's own 2**7:
    no multiple of 128 divides it, but ``tile_n=32``'s ``ct_max_k`` (32)
    does, at ``k_tile=192``). ``emulate_bf16_mmul_with_bfp16=False`` asks
    flm.GEMM for bf16 macs where its device's default is bfp16's (aie2p),
    the more accurate of the two. ``gemv`` are the GEMV's tunables, where
    the profile cannot tell it from another of its shape.
    """
    if len(x.shape) == 2 and x.shape[0] > 1:
        tiled = {}
        if k_tile is not None:
            tiled["k_tile"] = k_tile
        if tile_n is not None:
            tiled["tile_n"] = tile_n
        if emulate_bf16_mmul_with_bfp16 is not None:
            tiled["emulate_bf16_mmul_with_bfp16"] = emulate_bf16_mmul_with_bfp16
        y = FLMGEMM(x, weight, b_col_maj=True, epilogue_modes=(Epilogue.NONE,), **tiled)
    else:
        y = GEMV(weight, x, **gemv)
    if bias is None:
        return y
    if bias.shape[0] > RowwiseAdd.tile_cap:
        raise ValueError(
            f"project(): bias ({bias.shape[0]} elements) exceeds RowwiseAdd's "
            f"{RowwiseAdd.tile_cap}-element tile_cap; split the projection's "
            "weight and bias once at load time instead of folding them here"
        )
    rows = math.prod(y.shape) // bias.shape[0]
    return RowwiseAdd(y.reshape(rows, bias.shape[0]), bias).reshape(y.shape)


def swiglu(x, w_gate, w_up, w_down, k_tile=None, tile_n=None):
    """The feed-forward of ``x``, ``(rows, embedding_dim)``."""
    tiled = dict(k_tile=k_tile, tile_n=tile_n)
    gate, up = project(x, w_gate, **tiled), project(x, w_up, **tiled)
    return project(ElementwiseMul(SiLU(gate), up), w_down, **tiled)


class SwiGLU(iron.Graph):
    """The feed-forward as a graph, over the ``(out, in)`` weights it holds."""

    def __init__(self, w_gate, w_up, w_down):
        hidden_dim, embedding_dim = w_gate.shape
        if tuple(w_up.shape) != (hidden_dim, embedding_dim) or tuple(w_down.shape) != (
            embedding_dim,
            hidden_dim,
        ):
            raise ValueError(
                f"SwiGLU: w_gate {tuple(w_gate.shape)}, w_up {tuple(w_up.shape)} "
                f"and w_down {tuple(w_down.shape)} do not agree on (hidden, "
                "embedding)"
            )
        self.w_gate, self.w_up, self.w_down = w_gate, w_up, w_down

    def body(self, x):
        return swiglu(x, self.w_gate, self.w_up, self.w_down)


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
        a = Copy(wave, src=windows, dtype=np.float32).reshape(F, self.frame)[:frames]
        exact = dict(
            tile_m=32, dtype_out=np.float32, emulate_bf16_mmul_with_bfp16=False
        )
        spectrum = GEMM(Limbs(a), self.dft, **exact)
        energy = GEMM(Limbs(Magnitude(spectrum)), self.filterbank, **exact)
        if features is None:
            return Log(energy, offset=self.mel_floor)
        return Log(energy, features, offset=self.mel_floor)

    def exact(self, wave: np.ndarray, frames: int) -> np.ndarray:
        """The first ``frames`` features of ``wave`` in float64, rounded once
        to float32: the extractor's own computation, which the graph's
        reference, its operators', is held to.
        """
        starts = np.arange(frames)[:, None] * self.hop
        rows = np.asarray(wave, np.float32)[starts + np.arange(self.frame)]
        magnitude = np.abs(np.fft.rfft(rows * self.window, n=self.fft, axis=-1))
        return np.log(magnitude @ self.filters + self.mel_floor).astype(np.float32)


# Each product's float32 sum rounded once.
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)
# What every device's GEMM row block divides (aie2's 16 rows, aie2p's 8).
GEMM_ROWS = 16


class Conv2d(iron.Graph):
    """A 2-D convolution without bias of rows of ``width`` channels-last
    pixels by a ``(out_channels, channels_per_group, kernel, kernel)``
    ``weight`` at ``stride``. The width is padded with ``padding`` zero
    columns either side; padding in rows is rows the input holds, so a
    producer writes past them in place. Each output row is its pixels with
    ``border`` zero pixels either side, the padding of a convolution that
    reads it.

    A call takes the input ``(rows, width * channels)`` and the per-call
    ``rows`` of output it computes, and writes the output ``(out_rows,
    (out_width + 2 * border) * out_channels)`` where a caller gives it, else
    returns it. One channel (or ``groups == out_channels``, depthwise: each
    output channel its own input channel, ``channels_per_group == 1``) is a
    GEMM of ``kernel`` consecutive input rows, gathered whole, by the weight
    laid out as a band over the width (and, depthwise, block-diagonal over
    the channels too, so the GEMM mixes none of them). Where ``out_rows`` is
    not a whole number of ``GEMM_ROWS``-row blocks, the gather repeats its
    first row up to the next block and the GEMM computes every row: the
    output is those rows, bounded by ``rows`` (``rows`` rows where it is a
    number), and a caller cannot give it. More channels, not
    depthwise, are a GEMM of the gathered ``kernel * kernel * channels``
    patches by the weight, the output channels as its rows, so that few of
    them leave the patches to span every column (every row is then computed,
    as a GEMM bounds no column, and the output bounded after). Each GEMM
    sums its products in float32 and rounds once.

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
                a = Copy(x, src=gathered).reshape(out_rows, k * line)[:rows]
                return GEMM(a, self.matrix, *([] if y is None else [y]), **ACCURATE)
            if y is not None:
                raise ValueError(
                    f"Conv2d: {out_rows} output rows are not whole {GEMM_ROWS}-row "
                    f"blocks, so the GEMM computes {spare} more than a caller's "
                    f"output holds; take the returned output instead"
                )
            first = TensorAccessPattern((R, line), 0, [1, k * line], [s * line, 1])
            a = Copy(x, src=(gathered, *[first] * spare))
            out = GEMM(a.reshape(out_rows + spare, k * line), self.matrix, **ACCURATE)
            return out[:rows]
        n = out_rows * self.out_width
        patches = TensorAccessPattern(
            (R, line),
            0,
            [out_rows, self.out_width, k, k * C],
            [s * line, s * C, line, 1],
        )
        a = Copy(x, src=patches).reshape(n, k * k * C)
        # The few output channels as M, so that the patches span every
        # column; every row, as a GEMM bounds no N, and the output after.
        out = [] if y is None else [y.reshape(n, self.out_channels)]
        h = GEMM(self.matrix, a, *out, b_col_maj=True, c_col_maj=True, **ACCURATE)
        h = h if y is not None else h[: rows * self.out_width]
        return None if y is not None else h.reshape(out_rows, self.out_line)

    def exact(self, x: np.ndarray, weight: np.ndarray) -> np.ndarray:
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
    """A 1-D convolution over rows (time) of a full-channel-depth input: at
    each of ``kernel`` consecutive rows every input channel is contracted,
    by ``weight``, ``(out_channels, channels, kernel)``, at ``stride``, its
    ``bias``, ``(out_channels,)``, added once. Unlike ``Conv2d``, which
    slides one square kernel over both rows and a spatial ``width`` of
    channels-last pixels, there is no ``width`` axis here at all: a row
    already holds the whole channel vector a time step contracts.

    A call takes the input ``(rows, channels)`` and the per-call ``rows`` of
    output it computes, and writes the output ``(out_rows, out_channels)``
    where a caller gives it, else returns it. The ``kernel`` consecutive
    input rows are gathered whole (``Conv2d``'s single-channel row gather,
    which already does not touch ``width``) and projected by the weight
    reshaped to ``(kernel * channels, out_channels)`` in one GEMM, its bias
    folded on with ``RowwiseAdd``. Padding in rows is rows the input holds,
    so a producer writes past them in place.

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
        a = Copy(x, src=pattern).reshape(out_rows, k * line)[:rows]
        h = RowwiseAdd(GEMM(a, self.matrix, **ACCURATE), self.bias)
        return Copy(h, y) if y is not None else h

    def exact(self, x: np.ndarray, weight: np.ndarray, bias: np.ndarray) -> np.ndarray:
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

    A call takes the input ``(rows, width * channels)`` and returns the
    pooled output of the same shape. The input is written into a held
    border of ``kernel // 2`` pixels of ``-inf`` either side, in rows and
    columns, and the ``kernel * kernel`` shifted views of it, each whole
    rows of the input's shape, are combined by a running ``ElementwiseMax``:
    a selection, so the output is the max pooling exactly.

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
        Copy(self.border, self.padded)
        interior = TensorAccessPattern(
            shape, pad * line + pad * C, [self.rows, self.width * C], [line, 1]
        )
        Copy(x, self.padded, dst=interior)
        pooled = None
        for a in range(k):
            for b in range(k):
                view = TensorAccessPattern(
                    shape, a * line + b * C, [self.rows, self.width * C], [line, 1]
                )
                window = Copy(self.padded, src=view)
                # A pixel's channels are a line any plane divides into.
                pooled = (
                    window
                    if pooled is None
                    else ElementwiseMax(pooled, window, tile_size=C)
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

    A call takes each input ``(rows, width * channels[i])`` and returns
    ``(rows, width * sum(channels))``: each input copied into its channels
    of every pixel of a held buffer, which a last copy returns.

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
            Copy(x, self.out, dst=dst)
            offset += c
        return Copy(self.out[:])


class ImagePatches(iron.Graph):
    """A decoded image resized as torchvision's antialiased bicubic resize
    does it, rescaled to ``[0, 1]`` and cut into a vision tower's
    ``patches`` rows of 16x16-pixel patches, each soft token's ``pool ** 2``
    patches consecutive, row-major within its window, the tokens row-major
    over the image.

    A call takes the image, ``(height, width, 3)`` uint8 with each row
    padded to whole ``chunk``-byte chunks (``pack`` lays it out), and, per
    call, its ``height`` and ``width`` and the ``out_height`` by
    ``out_width`` it is resized to, whole ``pool * 16``-pixel windows. It
    returns the pixels, ``(patches, 768)`` bf16, each patch's ``xy``, its x
    and y side by side, and its ``position_ids``, every patch's x, then
    every patch's y plus ``positions``, ``(2 * patches,)`` int32 each; rows
    past the image are the zero patch at ``positions`` (and ``2 *
    positions``), the padding row of a table of that many. ``ResampleTaps``
    computes each axis's filter table, ``Resample`` resizes the image into a
    raster of patches over two cores a column, and ``PatchPositions``
    orders them, which a gathering ``Copy`` follows.

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
        taps_w = self.taps_w(in_samples=width, out_samples=out_width)
        taps_h = self.taps_h(in_samples=height, out_samples=out_height)
        self.resample(
            rgb,
            taps_w,
            taps_h,
            self.raster,
            rows=height,
            columns=width,
            out_rows=out_height,
            out_columns=out_width,
        )
        xy, position_ids, order = self.patch_positions(
            out_rows=out_height, out_columns=out_width
        )
        return Copy(self.raster[order]), xy.reshape(2 * T), position_ids.reshape(2 * T)

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


def geglu(x, w_gate, w_up, w_down, **gemm):
    """The GELU-gated feed-forward of ``x``, ``(rows, embedding_dim)``,
    ``W_down @ (GELU(W_gate @ x) * (W_up @ x))``, each projection a GEMM
    with ``gemm``'s keywords reading the weight as stored.
    """
    gate = GELU(GEMM(x, w_gate, b_col_maj=True, **gemm))
    f = ElementwiseMul(gate, GEMM(x, w_up, b_col_maj=True, **gemm))
    return GEMM(f, w_down, b_col_maj=True, **gemm)


def sandwich(x, block: Callable, pre, post, epsilon: float):
    """``x`` plus ``block`` of it between two RMS norms, weighted ``pre``
    before the block and ``post`` after it.
    """
    h = RMSNorm(x, weight=pre, epsilon=epsilon)
    return ElementwiseAdd(x, RMSNorm(block(h), weight=post, epsilon=epsilon))


def attention(
    h,
    angles,
    *,
    q_proj,
    k_proj,
    v_proj,
    o_proj,
    q_norm,
    k_norm,
    heads: int,
    groups: int,
    head_dim: int,
    epsilon: float,
    window: int | None = None,
    **gemm,
):
    """Bidirectional attention over the rows of ``h``, unscaled: ``q_proj``,
    ``k_proj`` and ``v_proj`` project them (GEMMs with ``gemm``'s keywords),
    the queries and keys are RMS-normed by ``q_norm`` and ``k_norm`` and
    rotated by ``angles``, a row each, and the values RMS-normed; ``MHA``
    attends within ``window`` positions if given, over the pipelines the
    profile gives it, and ``o_proj`` projects the heads back. Each weight
    is a checkpoint's ``(out, in)``.
    """
    T, H, G, D = h.shape[0], heads, groups, head_dim
    q = GEMM(h, q_proj, b_col_maj=True, **gemm).reshape(T * H, D)
    k = GEMM(h, k_proj, b_col_maj=True, **gemm).reshape(T * G, D)
    v = GEMM(h, v_proj, b_col_maj=True, **gemm).reshape(T * G, D)
    q = RoPE(RMSNorm(q, weight=q_norm, epsilon=epsilon), angles)
    k = RoPE(RMSNorm(k, weight=k_norm, epsilon=epsilon), angles)
    v = RMSNorm(v, epsilon=epsilon)
    o = MHA(
        q.reshape(T, H, D),
        k.reshape(T, G, D),
        v.reshape(T, G, D),
        heads_interleaved=True,
        kv_interleaved=True,
        causal=False,
        emulate_bf16_mmul_with_bfp16=False,
        window=window,
        scale=1.0,
    )
    return GEMM(o.reshape(T, H * D), o_proj, b_col_maj=True, **gemm)


#: RMSNorm's epsilon, shared by every model on ``Block``.
EPS = np.float32(1e-5)


def rms_norm(x, w):
    return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + EPS) * w


class Block:
    """The attention + SwiGLU layer Llama 3 and Granite 4.2 3B share, on the
    NPU: pre-norm attention, then pre-norm SwiGLU, both residual. A model
    mixes it in alongside ``CausalLM``, which gives ``attend`` and
    ``config``, and adds its own ``head``.
    """

    def layer(self, step: Step, i: int, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        a, mlp = w.self_attn, w.mlp
        h = RMSNorm(x, weight=w.input_layernorm.weight)
        # Half a head per tile for one row; q's shape is o's when H * D is
        # the width, so it is given here rather than by the profile.
        q, k, v = (
            project(h, p.weight, tile_size_output=D // 2)
            for p in (a.q_proj, a.k_proj, a.v_proj)
        )
        # One angle row per position, applied to that position's heads.
        q = RoPE(q.reshape(n * H, D), step.angles)
        k = RoPE(k.reshape(n * G, D), step.angles)
        x = ElementwiseAdd(x, project(self.attend(step, i, q, k, v), a.o_proj.weight))
        h = RMSNorm(x, weight=w.post_attention_layernorm.weight)
        ff = swiglu(h, mlp.gate_proj.weight, mlp.up_proj.weight, mlp.down_proj.weight)
        return ElementwiseAdd(x, ff)


class BlockOracle:
    """``Block``'s layer in float32, on the host, mixed in alongside
    ``Oracle``, which gives ``attend``, ``rotate``, ``buffer`` and ``config``.
    """

    def layer(self, angles, w, x):
        c, n = self.config, x.shape[0]
        H, G, D = c.n_heads, c.n_kv_groups, c.head_dim
        a, mlp = w.self_attn, w.mlp
        h = rms_norm(x, w.input_layernorm.weight)
        q = self.rotate((h @ a.q_proj.weight.T).reshape(n, H, D), angles)
        k = self.rotate((h @ a.k_proj.weight.T).reshape(n, G, D), angles)
        v = (h @ a.v_proj.weight.T).reshape(n, G, D)
        x = x + self.attend(q, k, v) @ a.o_proj.weight.T
        h = rms_norm(x, w.post_attention_layernorm.weight)
        F = mlp.gate_proj.weight.shape[0]
        half = np.matmul(h, mlp.gate_proj.weight.T, out=self.buffer("gate", (n, F)))
        half *= np.float32(0.5)
        # SiLU, with the sigmoid as a tanh, which does not overflow.
        silu = np.tanh(half, out=self.buffer("silu", (n, F)))
        silu += 1
        silu *= half
        silu *= np.matmul(h, mlp.up_proj.weight.T, out=self.buffer("up", (n, F)))
        return x + silu @ mlp.down_proj.weight.T
