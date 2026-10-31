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
    """Compute the ``(fft // 2 + 1, mels)`` unnormalized mel triangles, HTK scale.

    Over the rfft's bins, from 0 Hz to ``max_hz``, float64, as transformers'
    ``mel_filter_bank``.
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
    """The log-mel spectrogram of float32 samples, as Hugging Face computes it.

    Gemma 4's feature extractor, via bf16-limb GEMMs (``Limbs``) for exact
    float32 rfft and filterbank products.
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
        if fft < frame:
            raise ValueError(
                f"LogMel: an rfft of {fft} points is shorter than a frame of {frame}"
            )
        self.frame, self.hop, self.fft, self.mels = frame, hop, fft, mels
        self.mel_floor = mel_floor
        # The samples a frame is read as: six limb planes of them are the
        # rfft GEMM's K, whole 64s; the rfft's rows past the frame are zero.
        self.span = -(-frame // 32) * 32
        filters = filterbank(fft, mels, sample_rate, max_hz)
        bins = fft // 2 + 1
        width = -(-bins // 64) * 64
        angle = 2 * np.pi * np.arange(frame)[:, None] * np.arange(bins) / fft
        window = np.hanning(frame + 1)[:-1, None].astype(np.float32)
        # The rfft as a matrix, the window folded in: the real parts, then
        # the imaginary, each padded to the width.
        dft = np.zeros((self.span, 2 * width))
        dft[:frame, :bins] = window * np.cos(angle)
        dft[:frame, width : width + bins] = -window * np.sin(angle)
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
        F = (wave.shape[0] - self.span) // self.hop + 1
        if F % 4:
            raise ValueError(f"LogMel: {F} frames are not whole rows of four")
        # Frame f from hop f; in three dimensions, as d1 wraps at 1023 and
        # d2 does not, so that one descriptor holds it.
        windows = TensorAccessPattern(
            wave.shape, 0, [F // 4, 4, self.span], [4 * self.hop, self.hop, 1]
        )
        a = Copy.step(wave, src=windows, dtype=np.float32).reshape(F, self.span)
        a = a[:frames]
        exact = dict(tile_m=32, output_dtype=np.float32, precision=Precision.HIGHEST)
        spectrum = GEMM.step(Limbs.step(a), self.dft, **exact)
        energy = GEMM.step(
            Limbs.step(Magnitude.step(spectrum)),
            self.filterbank,
            **exact,
        )
        if features is None:
            return Log.step(energy, offset=self.mel_floor)
        return Log.step(energy, features, offset=self.mel_floor)


class ImagePatches(iron.Graph):
    """A decoded image resized as torchvision's antialiased bicubic resize does it.

    Rescaled to ``[0, 1]`` and cut row-major into a vision tower's
    ``patches`` rows of 16x16-pixel patches.
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

    def pack(
        self, image: np.ndarray, out_height: int, out_width: int
    ) -> tuple[np.ndarray, dict]:
        """Build a call's image buffer and per-call sizes for a decoded ``image``.

        Resized to ``out_height`` by ``out_width``.

        Args:
            image: ``(height, width, 3)`` uint8.
            out_height: The height to resize to.
            out_width: The width to resize to.

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
    """Weights of these shapes, by name.

    Read where the checkpoint holds them and computed with elsewhere.
    """

    def __init__(self, **shapes: tuple[int, ...]):
        for name, shape in shapes.items():
            setattr(self, name, iron.param(*shape))


class Linear(iron.Graph):
    """``torch.nn.Linear``: ``x @ weight.T``, plus ``bias`` where it holds one.

    At ``precision`` (``F.linear``'s, the caller's choice).
    """

    def __init__(
        self,
        in_features: int,
        out_features: int,
        bias: bool = True,
        *,
        precision: Precision,
    ):
        self.in_features, self.out_features = in_features, out_features
        self.weight = iron.param(out_features, in_features)
        self.bias = iron.param(out_features) if bias else None
        self.precision = precision

    def body(self, x: Handle) -> Handle:
        return F.linear(x, self.weight, self.bias, precision=self.precision)

    def split(self, x, *rows: int, **gemv) -> list:
        """Project ``x`` through each run of ``rows`` of the weight in turn.

        Each a fused projection's output; splitting the output columns
        instead would need a strided view no bounded-row descriptor fits.
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
    """``torch.nn.RMSNorm`` over the last axis, times ``weight``.

    ``eps`` None is the input dtype's machine epsilon.
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
        """Make every ``RMSNorm`` of ``module``, loaded, scale by ``1 + weight``.

        As Gemma's and Qwen3.5's do, the sum in float32 rounded to bf16
        (Hugging Face keeps it float32).
        """
        for _, weight, norm, _ in list(walk(module)):
            if isinstance(norm, RMSNorm):
                norm.weight = iron.param(
                    (weight.astype(np.float32) + 1).astype(bfloat16)
                )


class LayerNorm(iron.Graph):
    """``torch.nn.LayerNorm`` over the last axis, times ``weight`` plus ``bias``.

    Computed by ``F.layer_norm``.
    """

    def __init__(self, normalized_shape: int | tuple[int], eps: float = 1e-5):
        n = normalized_shape
        self.normalized_shape = (n,) if isinstance(n, int) else tuple(n)
        self.eps = eps
        self.weight = iron.param(*self.normalized_shape)
        self.bias = iron.param(*self.normalized_shape)

    def body(self, x: Handle) -> Handle:
        return F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)


def activation(name: str):
    """Return the function ``hidden_act`` ``name`` is.

    Raises:
        ValueError: No operator computes it: only ``"silu"``, ``"gelu"``
            and ``"gelu_pytorch_tanh"`` have one.
    """
    if name == "silu":
        return F.silu
    if name == "gelu":
        return F.gelu
    if name == "gelu_pytorch_tanh":
        return partial(F.gelu, approximate="tanh")
    raise ValueError(
        f"no operator for hidden_act {name!r}; silu, gelu and gelu_pytorch_tanh "
        "have one"
    )


def residual_add(x, y, residual: float):
    """``x`` plus ``y`` times ``residual``, in ``x``'s shape."""
    y = y if y.shape == x.shape else y.reshape(x.shape)
    if residual == 1:
        return x + y
    return AXPY.step(y, x, scalar_factor=residual)


class Rope(iron.Graph):
    """A decoder's RoPE table, one row per position (``DecoderConfig.angles``).

    q and k share it unless ``q_scale`` gives q a scaled table of its own. A
    model copies each call's rows once (``rows``) for every layer to read.
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
        """Return ``call``'s rows of q's table and of k's.

        The same rows where they share one: a prompt chunk's from its
        ``start``, else the decode step's at its ``position``.
        """

        def read(table):
            if call.prompt:
                start = call.start
                return Copy.step(table[start : start + self.chunk][: call.rows])
            return Copy.step(table[call.position]).reshape(1, self.width)

        k = read(self.table)
        return (k if self.q_table is None else read(self.q_table)), k

    def table_start(self, n: int) -> int:
        """Return the row of the table a prompt of ``n`` tokens starts reading from.

        0, the table's first.
        """
        return 0


class KVCache(iron.Graph):
    """A layer's keys and values and causal attention over them (``attend``).

    A prompt chunk writes a run of rows; a decode step attends with ``MHA``
    over one query, which costs the context, not the cache.

    Args:
        window: The positions before a query it attends to besides its own
            (None: all). Hugging Face's ``sliding_window`` counts the
            query's own, so pass ``sliding_window - 1``.

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
        """Return where a call may start to change the positions from ``held`` on.

        After ``ran`` ran: the chunk boundary before it while the ring
        still holds the window before that, else the first.
        """
        assert self.ring is not None and self.window is not None, "restart needs a ring"
        start = held // self.chunk * self.chunk
        return start if ran - (start - self.window) <= self.ring else 0

    def attend(self, call, q, k, v, scale: float | None = None):
        """Write ``k`` and ``v`` ``(rows, groups, head_dim)`` at the call's positions.

        None for a layer reading another's cache. Attends ``q`` ``(rows,
        heads, head_dim)`` over them; ``(rows, heads * head_dim)``.
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
        """Return ``attend``'s keys, values and queries within the window ``W``.

        Staged from the ``R``-position ring for the call's chunk or decode
        step.
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
    """No memory: attention over the call's own rows, both ways, or back if ``causal``.

    Within ``window`` positions either side (None: all), what an encoder's
    layer holds in a ``KVCache``'s place.
    """

    def __init__(self, window: int | None = None, causal: bool = False):
        self.window, self.causal = window, causal

    def attend(self, call, q, k, v, scale: float | None = None):
        """Attend ``q`` ``(rows, heads, head_dim)`` over ``k`` and ``v``.

        ``k`` and ``v`` are ``(rows, groups, head_dim)``, the logits scaled
        by ``scale`` (MHA's ``1 / sqrt(head_dim)`` if None); ``(rows, heads
        * head_dim)``.
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


class Attention(iron.Graph):
    """Self-attention for layer ``i`` of a decoder with config ``c``.

    q, k and v project, RoPE rotates the first ``rotary`` columns when set,
    and attention runs over the layer's ``KVCache``.

    Args:
        norms: Which of q, k and v each head of is RMS-normed before RoPE
            (``q_norm``, ``k_norm``; v unweighted).

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
        self.scaling: float | None = None
        self.rotary = c.rotary_dim

    def projections(self, c) -> None:
        """``q_proj``, ``k_proj`` and ``v_proj``."""
        E, D = c.hidden_size, self.head_dim
        linear = partial(Linear, bias=c.attention_bias, precision=c.precision)
        self.q_proj = linear(E, self.heads * D)
        self.k_proj = linear(E, self.groups * D)
        self.v_proj = linear(E, self.groups * D)

    def project(self, x, **gemv) -> list:
        """Project q, k and v of ``x``, each given the GEMV's ``gemv``.

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
        """Turn ``x`` ``(rows, head_dim)`` by RoPE.

        Only its first ``rotary`` columns where given.
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
        # Given q's tiles where its shape is o's, the two share one array.
        shared = isinstance(self.o_proj, Linear) and self.o_proj.out_features == H * D
        return self.output(o, x, **(tiles if shared else {}))

    def output(self, o: Handle, x: Handle, **gemv) -> Handle:
        """Return the block's output from the heads ``o`` of the input ``x``.

        ``o`` is ``(rows, heads * head_dim)``; ``gemv``, where given, is its one-row
        GEMV's tunables.
        """
        if not gemv:
            return self.o_proj(o)
        p = self.o_proj
        return F.linear(o, p.weight, p.bias, precision=p.precision, **gemv)


class MLP(iron.Graph):
    """A feed-forward on ``c``'s shape: ``fc2(act(fc1(x)))``, ``act`` is ``hidden_act``.

    Each projection has a bias where the config's ``mlp_bias`` says, at
    ``precision``.
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
    """A gated feed-forward, ``down_proj(act(gate_proj(x)) * up_proj(x))``.

    ``act`` the config's ``hidden_act``; each projection has a bias when
    ``mlp_bias`` is set.
    """

    def __init__(self, c):
        self.projections(c)
        self.down_proj = Linear(
            c.intermediate_size, c.hidden_size, c.mlp_bias, precision=c.precision
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

    ``input_layernorm`` then ``self_attn`` over the layer's ``cache``,
    ``post_attention_layernorm`` then ``mlp``, each scaled by
    ``residual_multiplier`` before its residual.
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
        """Attend the normed rows ``h`` over the layer's ``cache``."""
        angles = None if self.rope is None else call.ropes[self.rope]
        return self.self_attn(h, self.cache, call, angles)


class EncoderLayer(DecoderLayer):
    """Layer ``i`` of a pre-norm encoder, as in SigLIP and Whisper.

    ``DecoderLayer``'s two blocks after a ``LayerNorm``, bidirectional
    attention with no cache (``NoCache``) and a plain (ungated) ``MLP``.
    """

    norm = LayerNorm

    def __init__(self, c, i: int, self_attn=None):
        super().__init__(c, i, self_attn, MLP(c), NoCache())


class SandwichLayer(DecoderLayer):
    """``DecoderLayer`` with each block's output normed again before its residual.

    (``post_attention_layernorm``, ``post_feedforward_layernorm``) and
    ``mlp``'s input normed by ``pre_feedforward_layernorm`` (Gemma's).
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
    """``SandwichLayer``, then its per-layer input ``ple`` ``(rows, ple_dim)`` gated in.

    (``per_layer_input_gate``, ``per_layer_projection``,
    ``post_per_layer_input_norm``) and scaled by ``layer_scalar`` (Gemma 4's).
    """

    def __init__(self, c, i: int, self_attn=None, mlp=None, cache=None):
        super().__init__(c, i, self_attn, mlp, cache)
        E, P = c.hidden_size, c.ple_dim
        self.per_layer_input_gate = Linear(E, P, False, precision=c.precision)
        self.per_layer_projection = Linear(P, E, False, precision=c.precision)
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
