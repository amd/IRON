# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The layers a model builds from operators, for a graph's body.

``project`` is a weight's projection at either row count. ``swiglu``
is the SwiGLU feed-forward, ``W_down @ (SiLU(W_gate @ x) * (W_up @ x))``,
for one token or a sequence, and ``SwiGLU`` is it as a graph of its
own, holding the weights, so they are uploaded once. ``LogMel`` is an
audio front end's log-mel spectrogram. A graph here is called in a
model's body as it is on its own (``Graph``): its steps trace into the
model's.

The weights are a checkpoint's ``(out, in)``: SwiGLU's ``w_gate`` and
``w_up`` are ``(hidden_dim, embedding_dim)`` and ``w_down`` is
``(embedding_dim, hidden_dim)``. One row projects with GEMV, more with
flm.GEMM reading the weight as stored. The gate and up projections share
one array and one build. Nothing is padded: a row count the GEMM cannot tile
is an error at trace time.
"""

import math

import numpy as np
from aie.helpers.taplib import TensorAccessPattern

import iron
from iron.common import Scratchpad
from iron.operators.copy import Copy
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.limbs import Limbs, stacked
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.silu import SiLU


def project(x, weight, **gemv):
    """``x @ weight.T`` for a checkpoint's ``(out, in)`` weight: a GEMV for
    one row (a GEMV's output is a vector), else flm.GEMM reading it
    column-major. ``gemv`` are the GEMV's tunables, where the profile cannot
    tell it from another of its shape.
    """
    if len(x.shape) == 2 and x.shape[0] > 1:
        return FLMGEMM(x, weight, b_col_maj=True, epilogue_modes=(Epilogue.NONE,))
    return GEMV(weight, x, **gemv)


def swiglu(x, w_gate, w_up, w_down):
    """The feed-forward of ``x``, ``(rows, embedding_dim)``."""
    gate, up = project(x, w_gate), project(x, w_up)
    return project(ElementwiseMul(SiLU(gate), up), w_down)


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
