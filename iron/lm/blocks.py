# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The blocks a model builds from operators, for a graph's body.

A graph here is called in a model's body as it is on its own (``Graph``):
its steps record into the model's. Weights are a checkpoint's ``(out, in)``,
projected by ``F.linear``.
"""

import dataclasses
import math
from collections.abc import Hashable
from functools import partial
from typing import Any

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, Scratchpad
from iron.common.graph import Handle
from iron.common.graph.compiled import walk
from iron.common.image.packaging import require_device
from iron.operators.axpy import AXPY
from iron.operators.copy import Copy
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs, stacked
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.mha import MHA
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
        filters = filterbank(fft, mels, sample_rate, max_hz)
        bins = fft // 2 + 1
        width = -(-bins // 64) * 64
        angle = 2 * np.pi * np.arange(frame)[:, None] * np.arange(bins) / fft
        window = np.hanning(frame + 1)[:-1, None].astype(np.float32)
        # The rfft as a matrix, the window folded in: the real parts, then
        # the imaginary, each padded to the width.
        dft = np.zeros((frame, 2 * width))
        dft[:, :bins] = window * np.cos(angle)
        dft[:, width : width + bins] = -window * np.sin(angle)
        self.dft = iron.param(stacked(dft))
        self.filterbank = iron.param(
            stacked(np.pad(filters, ((0, width - bins), (0, 0))))
        )

    def body(
        self,
        wave: Handle,
        features: Handle | None = None,
        *,
        frames: Scratchpad[np.int32],
    ) -> Handle:
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
        self.matrix = iron.param(
            w.transpose(2, 1, 0).reshape(k * C, C_out).astype(bfloat16)
        )
        self.bias = iron.weight(np.asarray(bias, np.float32).astype(bfloat16))

    def body(
        self, x: Handle, y: Handle | None = None, *, rows: Scratchpad[np.int32]
    ) -> Handle:
        k, s = self.kernel, self.stride
        R, line = x.shape
        out_rows = (R - k) // s + 1
        pattern = TensorAccessPattern((R, line), 0, [out_rows, k * line], [s * line, 1])
        a = Copy.step(x, src=pattern).reshape(out_rows, k * line)[:rows]
        h = GEMM.step(a, self.matrix, precision=Precision.HIGHEST) + self.bias
        return Copy.step(h, y) if y is not None else h


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
        shared: dict[str, Any] = dict(
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
        taps: dict[str, Any] = dict(
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
        rgb: Handle,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ) -> tuple[Handle, Handle, Handle]:
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
        op.replace(height=H, width=W, out_height=out_height, out_width=out_width)
        buffer = np.zeros((op.image_chunks, self.chunk), np.uint8)
        rows = buffer.reshape(-1)[: H * line].reshape(H, line)
        rows[:, : 3 * W] = image.reshape(H, 3 * W)
        return buffer, dict(
            height=H, width=W, out_height=out_height, out_width=out_width
        )


class Weights(iron.Graph):
    """Weights of these shapes, by name, read where the checkpoint holds
    them and computed with elsewhere.
    """

    def __init__(self, **shapes: tuple[int, ...]):
        for name, shape in shapes.items():
            setattr(self, name, iron.param(*shape))


class Linear(iron.Graph):
    """``torch.nn.Linear``: ``x @ weight.T``, plus ``bias`` where it holds one,
    at ``precision`` (None: ``F.linear``'s).
    """

    def __init__(
        self,
        in_features: int,
        out_features: int,
        bias: bool = True,
        precision: Precision | None = None,
    ):
        self.in_features, self.out_features = in_features, out_features
        self.weight = iron.param(out_features, in_features)
        self.bias = iron.param(out_features) if bias else None
        self.precision = precision

    def body(self, x: Handle) -> Handle:
        return F.linear(x, self.weight, self.bias, precision=self.precision)

    def split(self, x, *rows: int, **gemv) -> list:
        """``x`` through each run of ``rows`` of the weight in turn, one
        ``F.linear`` each: a fused projection's outputs. Each reads its rows
        in place, where one projection's columns would be a strided view no
        descriptor of a bounded row count fits.
        """
        ends = np.cumsum(rows)
        return [
            F.linear(
                x,
                self.weight[end - n : end],
                None if self.bias is None else self.bias[end - n : end],
                precision=self.precision,
                **gemv,
            )
            for n, end in zip(rows, ends)
        ]


class Embedding(iron.Graph):
    """``torch.nn.Embedding``: the rows of ``weight`` that ``ids`` name."""

    def __init__(self, num_embeddings: int, embedding_dim: int):
        self.num_embeddings, self.embedding_dim = num_embeddings, embedding_dim
        self.weight = iron.param(num_embeddings, embedding_dim)

    def body(self, ids: Handle) -> Handle:
        return Copy.step(iron.weight(self.weight)[ids])


class RMSNorm(iron.Graph):
    """``torch.nn.RMSNorm`` over the last axis, times ``weight``; ``eps``
    None is the input dtype's machine epsilon.
    """

    def __init__(self, normalized_shape: int | tuple[int], eps: float | None = None):
        n = normalized_shape
        self.normalized_shape = (n,) if isinstance(n, int) else tuple(n)
        self.eps = eps
        self.weight = iron.param(*self.normalized_shape)

    def body(self, x: Handle) -> Handle:
        return F.rms_norm(x, self.normalized_shape, self.weight, self.eps)

    @staticmethod
    def plus_one(module) -> None:
        """Every ``RMSNorm`` of ``module``, loaded, scaling by ``1 + weight``
        (Gemma's, Qwen3.5's), the sum in float32 rounded to bf16 (Hugging
        Face keeps it float32).
        """
        for _, weight, norm, _ in list(walk(module)):
            if isinstance(norm, RMSNorm):
                norm.weight = iron.param(
                    (weight.astype(np.float32) + 1).astype(bfloat16)
                )


class LayerNorm(iron.Graph):
    """``torch.nn.LayerNorm`` over the last axis, times ``weight`` plus
    ``bias``; the kernel takes only its own ``eps`` (``F.layer_norm``).
    """

    def __init__(self, normalized_shape: int | tuple[int], eps: float = 1e-5):
        n = normalized_shape
        self.normalized_shape = (n,) if isinstance(n, int) else tuple(n)
        self.eps = eps
        self.weight = iron.param(*self.normalized_shape)
        self.bias = iron.param(*self.normalized_shape)

    def body(self, x: Handle) -> Handle:
        return F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)


class BatchNorm2d(iron.Graph):
    """``torch.nn.BatchNorm2d``'s affine weights and running statistics,
    float32, which ``fold`` folds into the conv before it.
    """

    def __init__(self, num_features: int, eps: float = 1e-5):
        self.weight = iron.param(num_features, dtype=np.float32)
        self.bias = iron.param(num_features, dtype=np.float32)
        self.running_mean = iron.param(num_features, dtype=np.float32)
        self.running_var = iron.param(num_features, dtype=np.float32)
        self.num_batches_tracked = iron.param(dtype=np.int64)
        self.eps = eps

    def fold(self, weight) -> tuple[np.ndarray, np.ndarray]:
        """The bias-free conv ``weight`` with this norm folded in, and the
        bias it gives, float32 whatever the conv's dtype, so a bf16 weight
        rounds once, after the fold.
        """
        scale = self.weight / np.sqrt(self.running_var + np.float32(self.eps))
        weight = np.asarray(weight, np.float32) * scale[:, None, None, None]
        return weight, (self.bias - self.running_mean * scale).astype(np.float32)


def activation(name: str):
    """The function ``hidden_act`` ``name`` is.

    Raises:
        ValueError: No operator computes it: only ``"silu"`` and
            ``"gelu_pytorch_tanh"`` have one.
    """
    if name == "silu":
        return F.silu
    if name == "gelu_pytorch_tanh":
        return partial(F.gelu, approximate="tanh")
    raise ValueError(
        f"no operator for hidden_act {name!r}; silu and gelu_pytorch_tanh have one"
    )


def residual_add(x, y, residual: float):
    """``x`` plus ``y`` times ``residual``, in ``x``'s shape."""
    y = y if y.shape == x.shape else y.reshape(x.shape)
    if residual == 1:
        return x + y
    return AXPY.step(y, x, scalar_factor=residual)


class Rope(iron.Graph):
    """A decoder's RoPE table, a row a position (``DecoderConfig.angles``):
    k's, and q's too unless ``q_scale``, a factor for each row of the table,
    scales a table of q's own. A model copies a call's rows of each ``Rope``
    its layers hold once (``rows``), and every layer holding it reads them.
    """

    def __init__(self, c, q_scale: np.ndarray | None = None):
        angles = c.angles()
        self.table = iron.weight(angles.astype(bfloat16))
        self.q_table = None
        if q_scale is not None:
            q = angles * np.asarray(q_scale, np.float32)[:, None]
            self.q_table = iron.weight(q.astype(bfloat16))
        self.chunk, self.width = c.prefill_chunk, c.rope_width

    def rows(self, call) -> tuple:
        """``call``'s rows of q's table and of k's, the same rows where they
        share one: a prompt chunk's from its ``start``, else the decode
        step's at its ``position``.
        """

        def read(table):
            if call.prompt:
                start = call.start
                return Copy.step(table[start : start + self.chunk][: call.rows])
            return Copy.step(table[call.position]).reshape(1, self.width)

        k = read(self.table)
        return (k if self.q_table is None else read(self.q_table)), k

    def table_start(self, n: int) -> int:
        """The row of the table a prompt of ``n`` tokens reads its first
        position from: 0, the table's first.
        """
        return 0


class KVCache(iron.Graph):
    """A layer's keys and values and causal attention over them
    (``attend``). A prompt chunk writes a run of rows, the last one short
    where the chunk does not divide ``max_seq_len``; a decode step attends
    with ``MHA`` of one query, which costs the context, not the cache.

    Keys and values are each ``(max_seq_len, num_key_value_heads,
    head_dim)``, so no descriptor steps by the context. Within a window
    whose ring and staging, three rings' rows, are fewer than that, they
    keep only the last ``ring`` positions, ``ring`` the power of two holding
    a window and a chunk: position ``p`` at rows ``p % ring`` and ``ring +
    p % ring``, so any ``ring`` positions in a row are one run. A call
    copies the run it attends over to ``staged``: a chunk's ``ring``
    positions ending at its last row, a decode step's window. A call stays
    within a chunk and restarts where the ring still holds the window
    before it (``restart``).

    Args:
        c: The decoder's shape.
        window: The positions before a query it attends to besides its own,
            as ``MHA`` counts them; None is all. Hugging Face's
            ``sliding_window`` counts the query's own, so a model passes
            ``sliding_window - 1``.

    Raises:
        ValueError: A ring with a chunk of other than a power of two.
    """

    def __init__(self, c, window: int | None = None):
        G, D, C = c.num_key_value_heads, c.head_dim, c.prefill_chunk
        self.chunk, self.window, rows = C, window, c.max_seq_len
        self.ring = None if window is None else 1 << (window + C - 1).bit_length()
        if self.ring is not None and 3 * self.ring < rows:
            if C & (C - 1):
                raise ValueError(f"KVCache: a {C}-position chunk is no power of two")
            self.staged = iron.state((self.ring, G, D)), iron.state((self.ring, G, D))
            rows = 2 * self.ring
        else:
            self.ring = None
        self.keys, self.values = iron.state((rows, G, D)), iron.state((rows, G, D))

    def restart(self, held: int, ran: int) -> int:
        """Where a call may start to change the positions from ``held`` on,
        after ``ran`` positions ran: there where the last call ended, else at
        the boundary before it while the ring holds the window before that,
        else at the first.
        """
        if held == ran:
            return held
        assert self.ring is not None and self.window is not None, "restart needs a ring"
        start = held // self.chunk * self.chunk
        return start if ran - (start - self.window) <= self.ring else 0

    def attend(self, call, q, k, v, scale: float | None = None):
        """Write ``k`` and ``v`` ``(rows, groups, head_dim)`` at ``call``'s
        positions, unless None (a layer reading another's cache), and attend
        ``q`` ``(rows, heads, head_dim)`` over every position up to its
        last, causally and within ``window``, the logits scaled by ``scale``
        (MHA's ``1 / sqrt(head_dim)`` if None); ``(rows, heads * head_dim)``.
        """
        C, (_, G, D), (n, H, _) = self.chunk, self.keys.shape, q.shape
        if self.ring is None:
            for x, cache in ((k, self.keys), (v, self.values)):
                if x is None:
                    continue
                if call.prompt:
                    cache[call.start : call.start + C][: call.rows] = x
                else:
                    cache[call.position] = x.reshape(G, D)
            keys, values = (x[: call.position + 1] for x in (self.keys, self.values))
        else:
            assert self.window is not None, "a ring has a window"
            keys, values, q = self._ring(call, self.ring, self.window, q, k, v)
        o = MHA.step(
            q,
            keys,
            values,
            heads_interleaved=True,
            kv_interleaved=True,
            window=self.window,
            scale=scale,
        )
        if call.prompt and self.ring is not None:
            o = o[: call.rows]
        return o.reshape(n, H * D)

    def _ring(self, call, R: int, W: int, q, k, v):
        """``attend``'s keys, values and queries within the window ``W``:
        a chunk attends from all its rows (those past ``rows`` are later
        than every query's, so masked) over the ``R`` positions of the ring
        ending at its last; a decode step over its window. A layer reading
        another's cache (``k`` None) reads its ``staged``, which that layer,
        earlier in the call, copied.
        """
        C = self.chunk
        if call.prompt:
            at, width = call.start % R, C
            first, read = iron.clamp(call.start + C - R, lo=0) % R, R
            n = iron.clamp(call.start + C, hi=R)
            q = dataclasses.replace(q, valid={})
        else:
            at, width = call.position % R, None
            first, read = iron.clamp(call.position - W, lo=0) % R, W + 1
            n = iron.clamp(call.position + 1, hi=W + 1)
        for x, ring, staged in zip((k, v), (self.keys, self.values), self.staged):
            if x is None:
                continue
            for row in (at, at + R):
                if width is None:
                    ring[row] = x.reshape(ring.shape[1:])
                else:
                    ring[row : row + width][: call.rows] = x
            Copy.step(ring[first : first + read][:n], staged[:read])
        return (*(staged[:n] for staged in self.staged), q)


class NoCache(iron.Graph):
    """No memory: attention over the call's own rows, both ways or, if
    ``causal``, back only, within ``window`` positions either side (None:
    all), what an encoder's layer holds in a ``KVCache``'s place.
    """

    def __init__(self, window: int | None = None, causal: bool = False):
        self.window, self.causal = window, causal

    def attend(self, call, q, k, v, scale: float | None = None):
        """``q`` ``(rows, heads, head_dim)`` over ``k`` and ``v`` ``(rows,
        groups, head_dim)``, the logits scaled by ``scale`` (MHA's ``1 /
        sqrt(head_dim)`` if None); ``(rows, heads * head_dim)``.
        """
        n, H, D = q.shape
        o = MHA.step(
            q,
            k,
            v,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=self.causal,
            window=self.window,
            scale=scale,
        )
        return o.reshape(n, H * D)


class CrossCache(iron.Graph):
    """A layer's keys and values of an encoder's output, each ``(rows,
    num_key_value_heads, head_dim)``, written once an encoding (``write``)
    and attended over by every call after, their first ``call.source``
    rows.
    """

    def __init__(self, c, rows: int):
        shape = (rows, c.num_key_value_heads, c.head_dim)
        self.keys, self.values = iron.state(shape), iron.state(shape)

    def write(self, k, v):
        """``k`` and ``v`` ``(rows, groups, head_dim)`` from the first row."""
        self.keys[: k.shape[0]] = k
        self.values[: v.shape[0]] = v

    def attend(self, call, q, k, v, scale: float | None = None):
        """``q`` ``(rows, heads, head_dim)`` over the first ``call.source``
        rows, both ways; ``k`` and ``v`` are None (``CrossAttention``).
        """
        n, H, D = q.shape
        span = np.s_[: call.source]
        o = MHA.step(
            q,
            self.keys[span],
            self.values[span],
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            scale=scale,
        )
        return o.reshape(n, H * D)


class Attention(iron.Graph):
    """Self-attention for layer ``i`` of a decoder with config ``c``.

    The input is projected by ``q_proj``, ``k_proj`` and ``v_proj``. If the
    call carries RoPE angles (``Rope.rows``), q and k are rotated, only
    their first ``rotary`` columns when the config sets ``rotary_dim``.
    Attention then runs over the layer's ``KVCache``, and ``output`` turns
    the heads into the block's output: ``o_proj`` unless a model overrides it.

    q, k and v have a bias when ``config.attention_bias`` is set; o has one
    when ``o_bias`` is. Every projection runs at ``config.precision``.
    ``projections`` builds the projections that ``project`` applies.
    ``scaling`` scales the logits and defaults to ``head_dim ** -0.5``. A
    layer that shares another layer's ``KVCache`` sets ``k_proj`` and
    ``v_proj`` to None and writes no keys or values.

    Args:
        c: The decoder's shape.
        i: The layer.
        norms: Which of q, k and v each head of is RMS-normed before RoPE:
            q and k by ``q_norm`` and ``k_norm``, v unweighted.

    Raises:
        ValueError: ``norms`` names other than q, k and v.
    """

    def __init__(self, c, i: int, norms: str = "", o_bias: bool = False):
        if set(norms) - set("qkv"):
            raise ValueError(f"Attention: norms {norms!r} names other than q, k and v")
        H, G, D, E = (
            c.num_attention_heads,
            c.num_key_value_heads,
            c.head_dim,
            c.hidden_size,
        )
        self.heads, self.groups, self.head_dim = H, G, D
        self.projections(c)
        self.o_proj = Linear(H * D, E, bias=o_bias, precision=c.precision)
        self.q_norm = RMSNorm(D, c.eps) if "q" in norms else None
        self.k_norm = RMSNorm(D, c.eps) if "k" in norms else None
        self.v_norm, self.eps = "v" in norms, c.eps
        self.scaling = None
        self.rotary = c.rotary_dim

    def projections(self, c) -> None:
        """``q_proj``, ``k_proj`` and ``v_proj``."""
        E, D = c.hidden_size, self.head_dim
        linear = partial(Linear, bias=c.attention_bias, precision=c.precision)
        self.q_proj = linear(E, self.heads * D)
        self.k_proj = linear(E, self.groups * D)
        self.v_proj = linear(E, self.groups * D)

    def project(self, x, **gemv) -> list:
        """q, k and v of ``x``, each projection given the GEMV's ``gemv``;
        None for a projection the layer does not hold.
        """
        return [
            (
                None
                if p is None
                else F.linear(x, p.weight, p.bias, precision=p.precision, **gemv)
            )
            for p in (self.q_proj, self.k_proj, self.v_proj)
        ]

    def rotate(self, x, angles):
        """``x`` ``(rows, head_dim)`` turned by RoPE, only its first
        ``rotary`` columns where given.
        """
        if self.rotary is None:
            return F.rope(x, angles)
        x[:, : self.rotary] = F.rope(Copy.step(x[:, : self.rotary]), angles)
        return x

    def body(self, x: Handle, cache, call, angles: Handle | None = None) -> Handle:
        n, H, G, D = x.shape[0], self.heads, self.groups, self.head_dim
        # One row's GEMV tiles half a head. Given here, not by the profile:
        # q's shape is o's when heads * head_dim is the width.
        tiles = dict(tile_size_output=D // 2) if n == 1 else {}
        q, k, v = self.project(x, **tiles)
        q = q.reshape(n * H, D)
        if self.q_norm is not None:
            q = self.q_norm(q)
        if k is not None:
            k, v = k.reshape(n * G, D), v.reshape(n * G, D)
            if self.k_norm is not None:
                k = self.k_norm(k)
            if self.v_norm:
                v = F.rms_norm(v, (D,), eps=self.eps)
        if angles is not None:
            q = self.rotate(q, angles[0])
            k = None if k is None else self.rotate(k, angles[1])
        if k is not None:
            k, v = k.reshape(n, G, D), v.reshape(n, G, D)
        o = cache.attend(call, q.reshape(n, H, D), k, v, scale=self.scaling)
        return self.output(o, x)

    def output(self, o: Handle, x: Handle) -> Handle:
        """The block's output from the heads ``o`` ``(rows, heads *
        head_dim)`` of the input ``x``.
        """
        return self.o_proj(o)


class CrossAttention(Attention):
    """``Attention`` over a ``CrossCache``: a call projects q alone, the
    keys and values an encoder's output's, projected once (``keys_values``).
    """

    def project(self, x, **gemv) -> list:
        q = self.q_proj
        return [
            F.linear(x, q.weight, q.bias, precision=q.precision, **gemv),
            None,
            None,
        ]

    def keys_values(self, memory) -> list:
        """The keys and values of ``memory`` ``(rows, width)``, each
        ``(rows, groups, head_dim)``.
        """
        n, G, D = memory.shape[0], self.groups, self.head_dim
        return [p(memory).reshape(n, G, D) for p in (self.k_proj, self.v_proj)]


class MLP(iron.Graph):
    """A feed-forward on ``c``'s shape: ``fc2(act(fc1(x)))``, ``act`` its
    ``hidden_act``, each projection with a bias where the config's
    ``mlp_bias`` says, at its ``precision``.
    """

    def __init__(self, c):
        E, M = c.hidden_size, c.intermediate_size
        linear = partial(Linear, bias=c.mlp_bias, precision=c.precision)
        self.fc1 = linear(E, M)
        self.fc2 = linear(M, E)
        self.act = activation(c.hidden_act)

    def body(self, x: Handle) -> Handle:
        return self.fc2(self.act(self.fc1(x)))


class GatedMLP(iron.Graph):
    """A gated feed-forward on ``c``'s shape:
    ``down_proj(act(gate_proj(x)) * up_proj(x))``, ``act`` its
    ``hidden_act``, each projection with a bias where the config's
    ``mlp_bias`` says, at its ``precision``. ``projections`` builds what
    ``body`` reads besides ``down_proj``.
    """

    def __init__(self, c):
        self.projections(c)
        self.down_proj = Linear(
            c.intermediate_size, c.hidden_size, c.mlp_bias, c.precision
        )
        self.act = activation(c.hidden_act)

    def projections(self, c) -> None:
        """``gate_proj`` and ``up_proj``."""
        E, M = c.hidden_size, c.intermediate_size
        linear = partial(Linear, bias=c.mlp_bias, precision=c.precision)
        self.gate_proj = linear(E, M)
        self.up_proj = linear(E, M)

    def body(self, x: Handle) -> Handle:
        gate, up = self.gate_proj(x), self.up_proj(x)
        return self.down_proj(self.act(gate) * up)


class DecoderLayer(iron.Graph):
    """Layer ``i`` of a pre-norm decoder with config ``c``.

    The input goes through ``input_layernorm`` and ``self_attn``, which
    attends over the layer's own ``cache``, then through
    ``post_attention_layernorm`` and ``mlp``. Each block's output is
    multiplied by ``residual_multiplier`` and added to its residual. Both
    norms are ``norm``, which is ``RMSNorm`` unless a model sets another.

    ``rope`` selects which of the call's RoPE angles (``Call.ropes``)
    rotate q and k. It is the model's ``Rope`` unless a model sets another
    key, and None means the layer applies no RoPE.

    A model may pass its own ``self_attn``, ``mlp`` and ``cache``. The
    default ``self_attn`` gives o a bias when ``attention_bias`` is set, as
    it does q, k and v.

    A layer that mixes its rows otherwise (a convolution, Mamba)
    overrides ``mix``.
    """

    norm = RMSNorm

    def __init__(self, c, i: int, self_attn=None, mlp=None, cache=None):
        self.input_layernorm = self.norm(c.hidden_size, c.eps)
        self.self_attn = (
            Attention(c, i, o_bias=c.attention_bias) if self_attn is None else self_attn
        )
        self.post_attention_layernorm = self.norm(c.hidden_size, c.eps)
        self.mlp = GatedMLP(c) if mlp is None else mlp
        self.cache = KVCache(c, c.window) if cache is None else cache
        self.rope: Hashable | None = None
        self.residual_multiplier = 1.0

    def body(self, x: Handle, call) -> Handle:
        x = residual_add(
            x, self.mix(self.input_layernorm(x), call), self.residual_multiplier
        )
        h = self.mlp(self.post_attention_layernorm(x))
        return residual_add(x, h, self.residual_multiplier)

    def mix(self, h: Handle, call) -> Handle:
        """The normed rows ``h`` attending over the layer's ``cache``."""
        angles = None if self.rope is None else call.ropes[self.rope]
        return self.self_attn(h, self.cache, call, angles)


class EncoderLayer(DecoderLayer):
    """Layer ``i`` of a pre-norm encoder on ``c``'s shape (SigLIP's,
    Whisper's): ``DecoderLayer``'s two blocks, each after a ``LayerNorm``,
    a plain ``MLP``, attending both ways over the call's rows (``NoCache``),
    ``o_proj`` biased with q, k and v; ``self_attn`` a model's own where
    given.
    """

    def __init__(self, c, i: int, self_attn=None):
        self.input_layernorm = LayerNorm(c.hidden_size)
        self.self_attn = (
            Attention(c, i, o_bias=c.attention_bias) if self_attn is None else self_attn
        )
        self.post_attention_layernorm = LayerNorm(c.hidden_size)
        self.mlp = MLP(c)
        self.cache = NoCache()
        self.rope = None
        self.residual_multiplier = 1.0


class CrossDecoderLayer(DecoderLayer):
    """``DecoderLayer`` with a third block between its two:
    ``encoder_attn`` after ``encoder_attn_layer_norm``, attending over
    ``cross``, the ``CrossCache`` an ``EncoderDecoder`` gives it;
    ``encoder_attn`` a model's own where given, as ``DecoderLayer``'s
    modules.
    """

    def __init__(self, c, i: int, self_attn=None, mlp=None, encoder_attn=None):
        super().__init__(c, i, self_attn, mlp)
        self.encoder_attn_layer_norm = self.norm(c.hidden_size, c.eps)
        self.encoder_attn = (
            CrossAttention(c, i) if encoder_attn is None else encoder_attn
        )
        self.cross: CrossCache | None = None

    def body(self, x: Handle, call) -> Handle:
        x = residual_add(
            x, self.mix(self.input_layernorm(x), call), self.residual_multiplier
        )
        h = self.encoder_attn(self.encoder_attn_layer_norm(x), self.cross, call)
        x = residual_add(x, h, self.residual_multiplier)
        h = self.mlp(self.post_attention_layernorm(x))
        return residual_add(x, h, self.residual_multiplier)


class SandwichLayer(DecoderLayer):
    """``DecoderLayer`` with each block's output normed again before its
    residual, by ``post_attention_layernorm`` and
    ``post_feedforward_layernorm``, and ``mlp``'s input by
    ``pre_feedforward_layernorm`` (Gemma's).
    """

    def __init__(self, c, i: int, self_attn=None, mlp=None, cache=None):
        super().__init__(c, i, self_attn, mlp, cache)
        self.pre_feedforward_layernorm = RMSNorm(c.hidden_size, c.eps)
        self.post_feedforward_layernorm = RMSNorm(c.hidden_size, c.eps)

    def body(self, x: Handle, call) -> Handle:
        h = self.mix(self.input_layernorm(x), call)
        x = residual_add(x, self.post_attention_layernorm(h), self.residual_multiplier)
        h = self.mlp(self.pre_feedforward_layernorm(x))
        return residual_add(
            x, self.post_feedforward_layernorm(h), self.residual_multiplier
        )


class PleLayer(SandwichLayer):
    """``SandwichLayer``, then its per-layer input ``ple`` ``(rows,
    ple_dim)`` gated in (``per_layer_input_gate``, ``per_layer_projection``,
    ``post_per_layer_input_norm``) and the sum scaled by ``layer_scalar``
    (Gemma 4's).
    """

    def __init__(self, c, i: int, self_attn=None, mlp=None, cache=None):
        super().__init__(c, i, self_attn, mlp, cache)
        E, P = c.hidden_size, c.ple_dim
        self.per_layer_input_gate = Linear(E, P, False, c.precision)
        self.per_layer_projection = Linear(P, E, False, c.precision)
        self.post_per_layer_input_norm = RMSNorm(E, c.eps)
        self.layer_scalar = iron.param(1)

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # The row RowwiseMul takes.
        scalar, E = self.layer_scalar, self.per_layer_projection.out_features
        self.scale = iron.param(np.full(E, scalar[0], scalar.dtype))

    def body(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, x: Handle, call, ple: Handle
    ) -> Handle:
        x = super().body(x, call)
        g = self.mlp.act(self.per_layer_input_gate(x)) * ple
        g = self.post_per_layer_input_norm(self.per_layer_projection(g))
        return residual_add(x, g, self.residual_multiplier) * self.scale
