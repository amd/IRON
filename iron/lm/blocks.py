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


class Linear(iron.Graph):
    """``torch.nn.Linear``: ``x @ weight.T``, plus ``bias`` where it holds one."""

    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        self.in_features, self.out_features = in_features, out_features
        self.weight = iron.param(out_features, in_features)
        self.bias = iron.param(out_features) if bias else None

    def body(self, x):
        return F.linear(x, self.weight, self.bias)


class Embedding(iron.Graph):
    """``torch.nn.Embedding``: the rows of ``weight`` that ``ids`` name."""

    def __init__(self, num_embeddings: int, embedding_dim: int):
        self.num_embeddings, self.embedding_dim = num_embeddings, embedding_dim
        self.weight = iron.param(num_embeddings, embedding_dim)

    def body(self, ids):
        return Copy.step(iron.weight(self.weight)[ids])


class RMSNorm(iron.Graph):
    """``torch.nn.RMSNorm`` over the last axis, times ``weight``; ``eps``
    None is the input dtype's machine epsilon.
    """

    def __init__(self, normalized_shape: int, eps: float | None = None):
        self.normalized_shape, self.eps = (normalized_shape,), eps
        self.weight = iron.param(normalized_shape)

    def body(self, x):
        return F.rms_norm(x, self.normalized_shape, self.weight, self.eps)


class LayerNorm(iron.Graph):
    """``torch.nn.LayerNorm`` over the last axis, times ``weight`` plus
    ``bias``; the kernel takes only its own ``eps`` (``F.layer_norm``).
    """

    def __init__(self, normalized_shape: int, eps: float = 1e-5):
        self.normalized_shape, self.eps = (normalized_shape,), eps
        self.weight = iron.param(normalized_shape)
        self.bias = iron.param(normalized_shape)

    def body(self, x):
        return F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)


def _activation(name: str):
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


def _add(x, y, residual: float):
    """``x`` plus ``y`` times ``residual``, in ``x``'s shape."""
    y = y if y.shape == x.shape else y.reshape(x.shape)
    if residual == 1:
        return x + y
    return AXPY.step(y, x, scalar_factor=residual)


class Rope(iron.Graph):
    """A decoder's RoPE table, a row a position (``DecoderConfig.angles``),
    with LongRoPE's long table stacked after it where the config gives one
    (``long_angles``), which a prompt passing ``long_past`` reads. A model
    copies a call's rows once (``rows``); each layer holding the table reads
    them.
    """

    def __init__(self, c):
        angles, long = c.angles(), c.long_angles()
        self.long_past = None if long is None else long[0]
        if long is not None:
            angles = np.concatenate([angles, long[1]])
        self.table = iron.weight(angles.astype(bfloat16))
        self.chunk, self.width = c.prefill_chunk, c.rope_width

    def rows(self, *, prompt: bool, position, start, rows, rope_start):
        """A call's rows: a prompt call's from ``start``, or from
        ``rope_start`` where a long table is stacked, else the decode step's
        at ``position``.
        """
        if prompt:
            begin = start if self.long_past is None else rope_start
            return Copy.step(self.table[begin : begin + self.chunk][:rows])
        return Copy.step(self.table[position]).reshape(1, self.width)


class KVCache(iron.Graph):
    """A layer's keys and values, each ``(max_seq_len, num_key_value_heads,
    head_dim)`` so no descriptor steps by the context, and causal attention
    over them (``attend``). A prompt chunk writes a run of rows
    (``cache[s : s + C][:rows]``), the last one short where the chunk does
    not divide ``max_seq_len``; a decode step attends with ``MHA`` of one
    query, which costs the context, not the cache.
    """

    def __init__(self, c):
        shape = (c.max_seq_len, c.num_key_value_heads, c.head_dim)
        self.keys, self.values = iron.state(shape), iron.state(shape)
        self.chunk = c.prefill_chunk

    def attend(self, step, q, k, v, scale: float | None = None):
        """Write ``k`` and ``v`` ``(rows, groups, head_dim)`` at ``step``'s
        positions and attend ``q`` ``(rows, heads, head_dim)`` over every
        position up to its last, causally, the logits scaled by ``scale``
        (MHA's ``1 / sqrt(head_dim)`` if None); ``(rows, heads * head_dim)``.
        """
        C, (_, G, D), (n, H, _) = self.chunk, self.keys.shape, q.shape
        for x, cache in ((k, self.keys), (v, self.values)):
            if step.prompt:
                cache[step.start : step.start + C][: step.rows] = x
            else:
                cache[step.position] = x.reshape(G, D)
        span = np.s_[: step.position + 1]
        o = MHA.step(
            q,
            self.keys[span],
            self.values[span],
            heads_interleaved=True,
            kv_interleaved=True,
            scale=scale,
        )
        return o.reshape(n, H * D)


class Attention(iron.Graph):
    """Layer ``i``'s self-attention on ``c``'s shape: ``q_proj``, ``k_proj``
    and ``v_proj`` of the layer's input, q and k turned by the call's RoPE
    angles where given, attended over the layer's ``KVCache``, then
    ``o_proj``. ``scale`` is the logits' scale; None is ``head_dim **
    -0.5``.

    Args:
        c: The decoder's shape.
        i: The layer.
        norms: Which of q and k each head of is RMS-normed by ``q_norm``
            and ``k_norm``, before RoPE.
        bias: Whether q, k and v each add a bias.
    """

    def __init__(self, c, i: int, norms: str = "", bias: bool = False):
        H, G, D, E = (
            c.num_attention_heads,
            c.num_key_value_heads,
            c.head_dim,
            c.hidden_size,
        )
        self.heads, self.groups, self.head_dim = H, G, D
        self.q_proj = Linear(E, H * D, bias=bias)
        self.k_proj = Linear(E, G * D, bias=bias)
        self.v_proj = Linear(E, G * D, bias=bias)
        self.o_proj = Linear(H * D, E, bias=False)
        self.q_norm = RMSNorm(D, c.eps) if "q" in norms else None
        self.k_norm = RMSNorm(D, c.eps) if "k" in norms else None
        self.scale = None

    def body(self, x, cache, step, angles=None):
        n, H, G, D = x.shape[0], self.heads, self.groups, self.head_dim
        # One row's GEMV tiles half a head. Given here, not by the profile:
        # q's shape is o's when heads * head_dim is the width.
        tiles = dict(tile_size_output=D // 2) if n == 1 else {}
        q, k, v = (
            F.linear(x, p.weight, p.bias, **tiles)
            for p in (self.q_proj, self.k_proj, self.v_proj)
        )
        q, k, v = q.reshape(n * H, D), k.reshape(n * G, D), v.reshape(n * G, D)
        if self.q_norm is not None:
            q = self.q_norm(q)
        if self.k_norm is not None:
            k = self.k_norm(k)
        if angles is not None:
            q, k = F.rope(q, angles), F.rope(k, angles)
        o = cache.attend(
            step,
            q.reshape(n, H, D),
            k.reshape(n, G, D),
            v.reshape(n, G, D),
            scale=self.scale,
        )
        return self.o_proj(o)


class GatedMLP(iron.Graph):
    """A gated feed-forward on ``c``'s shape:
    ``down_proj(act(gate_proj(x)) * up_proj(x))``, ``act`` its
    ``hidden_act``.
    """

    def __init__(self, c):
        E, M = c.hidden_size, c.intermediate_size
        self.gate_proj = Linear(E, M, bias=False)
        self.up_proj = Linear(E, M, bias=False)
        self.down_proj = Linear(M, E, bias=False)
        self.act = _activation(c.hidden_act)

    def body(self, x):
        gate, up = self.gate_proj(x), self.up_proj(x)
        return self.down_proj(self.act(gate) * up)


class DecoderLayer(iron.Graph):
    """Layer ``i`` of a pre-norm decoder on ``c``'s shape: ``self_attn``
    after ``input_layernorm``, attending over the layer's own ``cache``,
    then ``mlp`` after ``post_attention_layernorm``, each block's output
    added to its residual times ``residual``. ``rope`` is the model's
    ``Rope``, whose rows of the call (``DecodeStep.angles``) turn q and k;
    None turns nothing.
    """

    def __init__(self, c, i: int):
        self.input_layernorm = RMSNorm(c.hidden_size, c.eps)
        self.self_attn = Attention(c, i)
        self.post_attention_layernorm = RMSNorm(c.hidden_size, c.eps)
        self.mlp = GatedMLP(c)
        self.cache = KVCache(c)
        self.rope: Rope | None = None
        self.residual = 1.0

    def body(self, x, step):
        angles = None if self.rope is None else step.angles
        h = self.self_attn(self.input_layernorm(x), self.cache, step, angles)
        x = _add(x, h, self.residual)
        return _add(x, self.mlp(self.post_attention_layernorm(x)), self.residual)


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
class AttentionSpec:
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
            raise ValueError("AttentionSpec: a q, k or v norm needs its eps")

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
        _activation(self.activation)

    def act(self, x):
        return _activation(self.activation)(x)

    def __call__(self, w, x):
        act = self.act
        if not self.gated:
            h = act(_linear(x, w.fc1, precision=self.precision))
            return _linear(h, w.fc2, precision=self.precision)
        gate = _linear(x, w.gate_proj, precision=self.precision)
        up = _linear(x, w.up_proj, precision=self.precision)
        return _linear(act(gate) * up, w.down_proj, precision=self.precision)


@dataclasses.dataclass(frozen=True)
class DecoderLayerSpec:
    """A pre-norm transformer layer module's: ``self_attn`` after
    ``input_layernorm``, then ``mlp`` after ``post_attention_layernorm``,
    each block's output added to its residual times ``residual``.
    """

    attention: AttentionSpec
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
        return _add(x, y, self.residual)


@dataclasses.dataclass(frozen=True)
class CrossDecoderLayer(DecoderLayerSpec):
    """``DecoderLayerSpec`` with a third block between its two: ``encoder_attn``
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
