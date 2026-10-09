#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's audio tower: its shape, where its checkpoint keeps
each weight, its log-mel features, and the tower with its projection into
the text model's space on the NPU as one graph.
"""

import dataclasses
import math
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16, finfo

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import JointNarrowing
from iron.lm import Layout, checkpoint_shapes, load_weights
from iron.operators.axpy import AXPY
from iron.operators.clamp import Clamp
from iron.operators.copy import Copy
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs, stacked
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.relu import ReLU
from iron.operators.rms_norm import RMSNorm
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.operators.tanh import Tanh

from ..model import ACCURATE, ROWS

# Each clipped linear's bounds, scalars in the checkpoint.
BOUNDS = ("input_min", "input_max", "output_min", "output_max")

# Where the audio tune writes its tables, one per device.
COSTS = Path(__file__).parent

# The key columns a query's band spans: its window, then the zeros that make
# the row a whole Softmax line.
BAND = 32


@dataclasses.dataclass(frozen=True)
class AudioConfig:
    hidden: int = 1024
    n_layers: int = 12
    n_heads: int = 8
    hidden_dim: int = 4096
    mels: int = 128
    # The two subsampling convolutions' output channels.
    channels: tuple[int, int] = (128, 32)
    # A query attends to itself and the `window - 1` positions before it.
    window: int = 12
    logit_cap: float = 50.0
    conv_kernel: int = 5
    residual_weight: float = 0.5
    output_dim: int = 1536
    text_dim: int = 512
    eps: float = 1e-6
    # The feature extractor's: samples per second, per frame and per hop.
    sample_rate: int = 16000
    frame: int = 320
    hop: int = 160
    fft: int = 512
    mel_floor: float = 1e-3
    max_hz: float = 8000.0
    max_samples: int = 480000
    pad_to: int = 128

    @property
    def head_dim(self) -> int:
        return self.hidden // self.n_heads

    def tokens(self, frames: int) -> int:
        """The soft tokens `frames` valid feature frames give: each
        subsampling convolution keeps every other row.
        """
        rows = -(-frames // 2)
        return -(-rows // 2)

    def frames(self, samples: int) -> int:
        """The valid feature frames of a clip of `samples`: those whose last
        sample is audio, after `frame // 2` zeros in front.
        """
        audio = min(samples, self.max_samples) - (self.frame - self.frame // 2)
        return max(0, -(-audio // self.hop))


AUDIO = AudioConfig()


def layout(config: AudioConfig) -> Layout:
    """Each weight's place in the tower, its name in the checkpoint and its
    shape. A clipped linear is a namespace of its `weight` and its four
    `BOUNDS`.
    """
    c = config
    E, F, (C0, C1) = c.hidden, c.hidden_dim, c.channels
    tower = "audio_tower"
    sub = f"{tower}.subsample_conv_projection"
    layer = f"{tower}.layers.{{i}}"
    out = {
        "conv0": (f"{sub}.layer0.conv.weight", (C0, 1, 3, 3)),
        "norm0": (f"{sub}.layer0.norm.weight", (C0,)),
        "conv1": (f"{sub}.layer1.conv.weight", (C1, C0, 3, 3)),
        "norm1": (f"{sub}.layer1.norm.weight", (C1,)),
        "input_proj": (f"{sub}.input_proj_linear.weight", (E, C1 * c.mels // 4)),
        "output_proj": (f"{tower}.output_proj.weight", (c.output_dim, E)),
        "output_bias": (f"{tower}.output_proj.bias", (c.output_dim,)),
        "projection": (
            "embed_audio.embedding_projection.weight",
            (c.text_dim, c.output_dim),
        ),
        "layers.{i}.norm_pre_attn": (f"{layer}.norm_pre_attn.weight", (E,)),
        "layers.{i}.norm_post_attn": (f"{layer}.norm_post_attn.weight", (E,)),
        "layers.{i}.norm_out": (f"{layer}.norm_out.weight", (E,)),
        "layers.{i}.attn.relative": (
            f"{layer}.self_attn.relative_k_proj.weight",
            (E, E),
        ),
        "layers.{i}.attn.per_dim_scale": (
            f"{layer}.self_attn.per_dim_scale",
            (c.head_dim,),
        ),
        "layers.{i}.conv.depthwise": (
            f"{layer}.lconv1d.depthwise_conv1d.weight",
            (E, 1, c.conv_kernel),
        ),
        "layers.{i}.conv.pre": (f"{layer}.lconv1d.pre_layer_norm.weight", (E,)),
        "layers.{i}.conv.norm": (f"{layer}.lconv1d.conv_norm.weight", (E,)),
    }
    clipped = {
        "conv.start": ("lconv1d.linear_start", (2 * E, E)),
        "conv.end": ("lconv1d.linear_end", (E, E)),
        "attn.q": ("self_attn.q_proj", (E, E)),
        "attn.k": ("self_attn.k_proj", (E, E)),
        "attn.v": ("self_attn.v_proj", (E, E)),
        "attn.post": ("self_attn.post", (E, E)),
    }
    for j in (1, 2):
        ff = f"feed_forward{j}"
        out[f"layers.{{i}}.ff{j}.pre"] = (f"{layer}.{ff}.pre_layer_norm.weight", (E,))
        out[f"layers.{{i}}.ff{j}.post"] = (
            f"{layer}.{ff}.post_layer_norm.weight",
            (E,),
        )
        clipped[f"ff{j}.up"] = (f"{ff}.ffw_layer_1", (F, E))
        clipped[f"ff{j}.down"] = (f"{ff}.ffw_layer_2", (E, F))
    for path, (name, shape) in clipped.items():
        out[f"layers.{{i}}.{path}.weight"] = (f"{layer}.{name}.linear.weight", shape)
        for bound in BOUNDS:
            out[f"layers.{{i}}.{path}.{bound}"] = (f"{layer}.{name}.{bound}", ())
    return out


def sinusoid(config: AudioConfig) -> np.ndarray:
    """The `(window, hidden)` float32 timing signal of each distance a query
    reaches back: sines, then cosines.
    """
    n = config.hidden // 2
    rates = np.exp(np.arange(n) * -(math.log(1e4) / (n - 1))).astype(np.float32)
    angles = np.arange(config.window, dtype=np.float32)[:, None] * rates
    return np.concatenate([np.sin(angles), np.cos(angles)], axis=-1)


def unread_audio_weights(config: AudioConfig) -> SimpleNamespace:
    """`iron.lm.unread_weights` for the tower: every array allocated and
    never written but each clipped linear's bounds, `[-inf, inf]`, which
    the tower checks as it is built.
    """
    tensors = {
        name: (
            np.full(shape, -np.inf if name.endswith("_min") else np.inf, bfloat16)
            if name.rpartition(".")[2] in BOUNDS
            else np.empty(shape, bfloat16)
        )
        for name, shape in checkpoint_shapes(layout(config), config.n_layers).items()
    }
    return load_weights(tensors, layout(config), config.n_layers)


def audio_tensors(tensors: dict) -> dict:
    """The audio tower's tensors of the full checkpoint, with its projection
    into the text model's space.
    """
    return {
        k: v
        for k, v in tensors.items()
        if k.startswith("audio_tower.") or k.startswith("embed_audio.")
    }


class LogMel:
    """The feature extractor of Hugging Face's Gemma 4 processor in numpy:
    a waveform's log-mel frames and how many of them are valid.

    A frame is the `frame` samples from its hop, after `frame // 2` zeros
    in front, under a periodic Hann window; it is valid when its last sample
    is audio rather than the padding to a multiple of `pad_to` samples.
    Invalid frames are zero.

    Args:
        config: The tower's shape and its feature extractor's.
    """

    def __init__(self, config: AudioConfig):
        c = config
        self.config = config
        self.window = np.hanning(c.frame + 1)[:-1].astype(np.float32)
        # HTK mel triangles over the FFT bins, unnormalized.
        mel = np.linspace(0, 2595 * math.log10(1 + c.max_hz / 700), c.mels + 2)
        edges = 700 * (10 ** (mel / 2595) - 1)
        bins = np.linspace(0, c.sample_rate // 2, c.fft // 2 + 1)
        slopes = edges[None, :] - bins[:, None]
        widths = np.diff(edges)
        self.filters = np.maximum(
            0, np.minimum(-slopes[:, :-2] / widths[:-1], slopes[:, 2:] / widths[1:])
        )
        # The rfft as a matrix: `(frame, 2 * bins)`, the real parts then the
        # imaginary, the window folded in.
        angle = 2 * np.pi * np.arange(c.frame)[:, None] * np.arange(bins.size) / c.fft
        window = self.window.astype(np.float64)[:, None]
        self.basis = np.concatenate(
            [window * np.cos(angle), -window * np.sin(angle)], axis=1
        )

    def __call__(self, waveform: np.ndarray) -> tuple[np.ndarray, int]:
        """The `(frames, mels)` float32 features of a mono `waveform` at
        `sample_rate`, truncated to `max_samples`, and the valid frames.
        """
        c = self.config
        audio = np.asarray(waveform, np.float32).reshape(-1)[: c.max_samples]
        n = audio.size
        padded = -(-n // c.pad_to) * c.pad_to
        audio = np.pad(audio, (c.frame // 2, padded - n))
        count = (audio.size - c.frame - 1) // c.hop + 1
        starts = np.arange(count) * c.hop
        frames = audio[starts[:, None] + np.arange(c.frame)] * self.window
        magnitude = np.abs(np.fft.rfft(frames, n=c.fft, axis=-1))
        features = np.log(magnitude @ self.filters + c.mel_floor).astype(np.float32)
        valid = c.frames(n)
        features[valid:] = 0
        return features, valid


class AudioTower(SimpleNamespace):
    """The audio tower and `embed_audio` over at most `max_tokens` soft
    tokens, one compile for every clip, called in a graph's body. It is a
    namespace, so the graph that holds it names its weights and states by
    their path.

    A call takes the `4 * T + 1` hops of waveform its `4 * T` frames read
    (the first the zeros in front of the clip, zero past it), `T` being
    `max_tokens`, and per call the valid frames, `n`, the rows of the
    first convolution's output that are valid, and `tokens`, the soft
    tokens, which bound the operators over each. Its features are
    `LogMel`'s, each GEMM over float32 operands as six products of their
    bf16 limbs. The frame after the valid ones is zeroed, as are the first
    convolution's rows after its valid ones before the second reads them,
    as Hugging Face's mask does. Past that nothing masks padding: the
    attention and the light convolution look only back, so a valid token
    never reads a padded one.

    Each subsampling convolution is a GEMM over the rows a call's patterns
    gather, its weight centered over the output channels so that its layer
    norm is an RMS norm. Attention is one GEMM a head over every key, of
    which each query's band of `BAND` columns (its window, the rest masked)
    is gathered, its relative-position terms keys of the same GEMM; the
    probabilities are scattered back to the band of zeros for the GEMM with
    the values. Every clipped linear's clamps run as `Clamp`s.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
        max_tokens: The soft tokens a call takes at most, whole `ROWS`-row
            blocks.
    """

    def __init__(
        self,
        config: AudioConfig,
        weights: SimpleNamespace,
        max_tokens: int = 768,
    ):
        c = config
        if max_tokens % ROWS:
            raise ValueError(f"{max_tokens} tokens are not whole {ROWS}-row blocks")
        if c.frame != 2 * c.hop:
            raise ValueError(f"a frame of {c.frame} samples is not two hops")
        self.config = config
        self.max_tokens = T = max_tokens
        E, H, D, W = c.hidden, c.n_heads, c.head_dim, c.window
        C0, C1 = c.channels
        F0 = c.mels // 2
        # The first convolution's output row: each frequency's channels in a
        # slot of their own, with a zero slot either side, the second's padding.
        self.slots = (F0 + 2) * C0
        w0 = np.asarray(weights.conv0, np.float32)[:, 0]
        w0 = w0 - w0.mean(axis=0)
        conv0 = np.zeros((3, c.mels, F0 + 2, C0), np.float32)
        for f in range(F0):
            for b in range(3):
                if 0 <= 2 * f - 1 + b < c.mels:
                    conv0[:, 2 * f - 1 + b, f + 1] = w0[:, :, b].T
        self.conv0 = conv0.reshape(3 * c.mels, self.slots).astype(bfloat16)
        w1 = np.asarray(weights.conv1, np.float32)
        w1 = w1 - w1.mean(axis=0)
        self.conv1 = w1.transpose(0, 2, 3, 1).reshape(C1, 9 * C0).astype(bfloat16)
        self.norm0, self.norm1 = weights.norm0, weights.norm1
        self.input_proj = weights.input_proj
        self.output_proj = weights.output_proj
        self.output_bias = iron.weight(np.tile(weights.output_bias, (T, 1)))
        self.projection = weights.projection
        logmel = LogMel(config)
        bins = logmel.filters.shape[0]
        # The bins padded to whole 64-column GEMM tiles, the padding zero.
        width = -(-bins // 64) * 64
        dft = np.zeros((c.frame, 2 * width))
        dft[:, :bins] = logmel.basis[:, :bins]
        dft[:, width : width + bins] = logmel.basis[:, bins:]
        self.dft = stacked(dft)
        self.filters = stacked(np.pad(logmel.filters, ((0, width - bins), (0, 0))))
        self.features = iron.state((4 * T + 2, c.mels))
        self.zero_mel = np.zeros((1, c.mels), bfloat16)
        self.subsampled = iron.state((2 * T + 2, self.slots))
        self.zero = np.zeros((1, self.slots), bfloat16)
        # The keys' rows: the `W - 1` before the first, the T keys, then from
        # an even row the relative-position rows twice, the second a row on.
        self.width = K = -(-(T + W + 2 * BAND) // 128) * 128
        self.keys = iron.state((H, K, D))
        self.values = iron.state((H, K, D))
        self.scores = iron.state((H, T, K))
        self.probs = iron.state((H, T, K))
        q, j = np.arange(T)[:, None], np.arange(BAND)
        # An odd query's band starts a column early, at an even column.
        d = j - q % 2
        mask = np.where(
            (d >= 0) & (d < W) & (q - (W - 1) + d >= 0), 0, finfo(bfloat16).min
        )
        self.mask = np.tile(mask.astype(bfloat16), (H, 1))
        # The logits scaled by 1 / logit_cap, the key scale moved to the queries.
        q_scale = D**-0.5 / math.log(2)
        k_scale = math.log(1 + math.e) / math.log(2)
        scale = q_scale * k_scale / c.logit_cap
        timing = sinusoid(config)
        # A feed-forward's residual weight in its post norm's, exact at 0.5.
        residual = bfloat16(c.residual_weight)
        self.layers = []
        for w in weights.layers:
            a = w.attn
            if not all(
                float(vars(a.q)[b]) == float(vars(p)[b])
                for p in (a.k, a.v)
                for b in BOUNDS[:2]
            ):
                raise ValueError("q, k and v are clamped to different input bounds")
            softplus = np.logaddexp(0, np.asarray(a.per_dim_scale, np.float32))
            relative = (timing @ np.asarray(a.relative, np.float32).T).reshape(W, H, D)
            # Distance W - 1 - j at band column j, then at j + 1.
            band = np.zeros((H, 2 * BAND, D), np.float32)
            band[:, :W] = relative[::-1].transpose(1, 0, 2) / k_scale
            band[:, BAND + 1 : BAND + 1 + W] = band[:, :W]
            self.layers.append(
                SimpleNamespace(
                    ff=[
                        SimpleNamespace(**vars(f) | {"post": f.post * residual})
                        for f in (w.ff1, w.ff2)
                    ],
                    norm_pre_attn=w.norm_pre_attn,
                    norm_post_attn=w.norm_post_attn,
                    norm_out=w.norm_out,
                    attn=SimpleNamespace(
                        q=a.q,
                        k=a.k,
                        v=a.v,
                        post=a.post,
                        scale=iron.weight(
                            np.tile(np.tile(softplus * scale, H), (T, 1)).astype(
                                bfloat16
                            )
                        ),
                        relative=band.astype(bfloat16),
                    ),
                    conv=SimpleNamespace(
                        pre=w.conv.pre,
                        start=w.conv.start,
                        glu=(w.conv.start.weight[:E], w.conv.start.weight[E:]),
                        planes=np.ascontiguousarray(w.conv.depthwise[:, 0].T),
                        norm=w.conv.norm,
                        end=w.conv.end,
                    ),
                )
            )

    def logmel(self, wave, frames):
        """Write the log-mel features of `wave`'s valid frames to
        `features[1 : frames + 1]`, and zero the row after them.

        Args:
            wave: `((F + 1) * hop,)` float32 samples: the `frame // 2` zeros
                in front of the clip, then the clip, zero past it.
            frames: The per-call valid frames, an int32 value.
        """
        c = self.config
        F = wave.shape[0] // c.hop - 1
        # Frame f is hops f and f + 1; in three dimensions, as d1 wraps at
        # 1023 and d2 does not, so that one descriptor holds it.
        windows = TensorAccessPattern(
            wave.shape, 0, [F // 4, 4, c.frame], [4 * c.hop, c.hop, 1]
        )
        a = Copy(wave, src=windows, dtype=np.float32).reshape(F, c.frame)[:frames]
        a = Limbs(a)
        exact = dict(dtype_out=np.float32, emulate_bf16_mmul_with_bfp16=False)
        spectrum = GEMM(a, self.dft, tile_m=32, **exact)
        energy = GEMM(Limbs(Magnitude(spectrum)), self.filters, tile_m=32, **exact)
        Log(energy, self.features[1 : F + 1], offset=c.mel_floor)
        Copy(self.zero_mel, self.features[frames + 1])

    def __call__(self, wave, n, frames, tokens):
        """The soft tokens of `wave`, `(max_tokens, text_dim)` bfloat16, the
        first `tokens` of them valid.

        Args:
            wave: `((4 * max_tokens + 1) * hop,)` float32 samples, as
                `logmel` takes them.
            n: The per-call `ceil(frames / 2)`, an int32 value.
            frames: The per-call valid frames, an int32 value.
            tokens: The per-call `config.tokens(frames)`, an int32 value.
        """
        c = self.config
        C0, C1 = c.channels
        F1 = c.mels // 4
        T = self.max_tokens
        # The first row of each convolution's input is its zero padding in time.
        self.logmel(wave, frames)
        patches = TensorAccessPattern(
            self.features.shape, 0, [2 * T, 3 * c.mels], [2 * c.mels, 1]
        )
        h = GEMM(
            Copy(self.features, src=patches).reshape(2 * T, 3 * c.mels)[:n],
            self.conv0,
            **ACCURATE,
        )
        h = RMSNorm(
            h.reshape(2 * T * self.slots // C0, C0), weight=self.norm0, epsilon=c.eps
        )
        ReLU(h.reshape(2 * T, self.slots), self.subsampled[1 : 2 * T + 1])
        Copy(self.zero, self.subsampled[n + 1])
        rows = TensorAccessPattern(
            self.subsampled.shape,
            0,
            [T, F1, 3, 3 * C0],
            [2 * self.slots, 2 * C0, self.slots, 1],
        )
        h = Copy(self.subsampled, src=rows).reshape(T * F1, 9 * C0)
        # The few output channels as M, so that the patches span every column;
        # every row, as a GEMM bounds no N.
        h = GEMM(self.conv1, h, b_col_maj=True, c_col_maj=True, **ACCURATE)
        h = ReLU(RMSNorm(h[: tokens * F1], weight=self.norm1, epsilon=c.eps))
        x = GEMM(h.reshape(T, F1 * C1), self.input_proj, b_col_maj=True, **ACCURATE)
        for w in self.layers:
            x = self.layer(w, x, tokens)
        x = GEMM(x, self.output_proj, b_col_maj=True, **ACCURATE)
        x = RMSNorm(ElementwiseAdd(x, self.output_bias[:tokens]), epsilon=c.eps)
        return GEMM(x, self.projection, b_col_maj=True, **ACCURATE)

    def clamped(self, w, x, side: str):
        """`x` clamped to the `side` (`input` or `output`) bounds of `w`."""
        low, high = (float(vars(w)[f"{side}_{b}"]) for b in ("min", "max"))
        return Clamp(x, low=low, high=high)

    def linear(self, w, x, weight=None):
        """`x`, already clamped to the input bounds of `w`, projected by
        `weight` (`w`'s own by default) and clamped to its output bounds.
        """
        weight = w.weight if weight is None else weight
        return self.clamped(w, GEMM(x, weight, b_col_maj=True, **ACCURATE), "output")

    def layer(self, w, x, tokens):
        c = self.config
        x = self.feed_forward(w.ff[0], x)
        h = RMSNorm(x, weight=w.norm_pre_attn, epsilon=c.eps)
        a = RMSNorm(
            self.attention(w.attn, h, tokens), weight=w.norm_post_attn, epsilon=c.eps
        )
        x = self.feed_forward(w.ff[1], self.light_conv(w.conv, ElementwiseAdd(x, a)))
        return RMSNorm(x, weight=w.norm_out, epsilon=c.eps)

    def feed_forward(self, w, x):
        c = self.config
        h = self.clamped(w.up, RMSNorm(x, weight=w.pre, epsilon=c.eps), "input")
        h = self.linear(w.up, h)
        h = self.linear(w.down, self.clamped(w.down, SiLU(h), "input"))
        return ElementwiseAdd(x, RMSNorm(h, weight=w.post, epsilon=c.eps))

    def attention(self, w, h, tokens):
        c = self.config
        T, H, D, W = h.shape[0], c.n_heads, c.head_dim, c.window
        K = self.width
        keys, values = self.keys, self.values
        scores, probs = self.scores, self.probs
        h = self.clamped(w.q, h, "input")
        q = ElementwiseMul(self.linear(w.q, h), w.scale[:tokens])
        k, val = self.linear(w.k, h), self.linear(w.v, h)
        Copy(k.reshape(T, H, D).transpose(1, 0, 2), keys[:, W - 1 : W - 1 + T])
        R = T + W - 1 + (T + W - 1) % 2
        Copy(w.relative, keys[:, R : R + 2 * BAND])
        Copy(val.reshape(T, H, D).transpose(1, 0, 2), values[:, W - 1 : W - 1 + T])
        q = Copy(q.reshape(T, H, D).transpose(1, 0, 2))
        # Over every key: those past the valid ones are stale but finite, as
        # only bounded copies write them.
        for i in range(H):
            GEMM(q[i], keys[i], scores[i], b_col_maj=True, **ACCURATE)
        # Query t's band starts at the even column of t and t - 1, its
        # relative terms at R or R + BAND: a DMA moves 4-byte words.
        pairs = [H, T // 2, 2, BAND]
        band = TensorAccessPattern((H, T, K), 0, pairs, [T * K, 2 * K + 2, K, 1])
        relative = TensorAccessPattern((H, T, K), R, pairs, [T * K, 2 * K, K + BAND, 1])
        logits = ElementwiseAdd(
            Copy(scores, src=band).reshape(H * T, BAND),
            Copy(scores, src=relative).reshape(H * T, BAND),
        )
        logits = AXPY(Tanh(logits), self.mask, scalar_factor=c.logit_cap)
        Copy(Softmax(logits), probs, dst=band)
        for i in range(H):
            GEMM(probs[i, :tokens], values[i], q[i], **ACCURATE)
        o = Copy(q.transpose(1, 0, 2)).reshape(T, H * D)
        return self.linear(w.post, self.clamped(w.post, o, "input"))

    def light_conv(self, w, x):
        c = self.config
        h = self.clamped(w.start, RMSNorm(x, weight=w.pre, epsilon=c.eps), "input")
        a, b = (self.linear(w.start, h, weight) for weight in w.glu)
        h = DepthwiseConv1d(ElementwiseMul(a, Sigmoid(b)), w.planes)
        h = SiLU(RMSNorm(h, weight=w.norm, epsilon=c.eps))
        return ElementwiseAdd(x, self.linear(w.end, self.clamped(w.end, h, "input")))

    def inputs(self, waveform) -> tuple[np.ndarray, dict]:
        """A call's `wave` and per-call sizes, `n`, `frames` and `tokens`,
        for a mono `waveform` at `sample_rate`, truncated to `max_samples`
        and padded with zeros.

        Raises:
            ValueError: The clip has no valid frame, or more soft tokens
                than `max_tokens`.
        """
        c = self.config
        audio = np.asarray(waveform, np.float32).reshape(-1)[: c.max_samples]
        frames = c.frames(audio.size)
        tokens = c.tokens(frames)
        if not 0 < tokens <= self.max_tokens:
            raise ValueError(
                f"{audio.size} samples give {tokens} soft tokens, not 1 to "
                f"{self.max_tokens}"
            )
        # Samples past the last frame are only ever read by invalid ones.
        wave = np.zeros((4 * self.max_tokens + 1) * c.hop, np.float32)
        held = min(audio.size, wave.size - c.hop)
        wave[c.hop : c.hop + held] = audio[:held]
        return wave, dict(n=-(-frames // 2), frames=frames, tokens=tokens)


class Audio(iron.Graph):
    """The audio tower as a graph of its own, one compile for every clip.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
        max_tokens: The soft tokens a call takes at most, whole `ROWS`-row
            blocks.
    """

    def __init__(
        self,
        config: AudioConfig,
        weights: SimpleNamespace,
        max_tokens: int = 768,
    ):
        self.config = config
        self.audio = AudioTower(config, weights, max_tokens)

    def body(
        self,
        x,
        *,
        n: Scratchpad[np.int32],
        frames: Scratchpad[np.int32],
        tokens: Scratchpad[np.int32],
    ):
        return self.audio(x, n, frames, tokens)

    # -- on the host -----------------------------------------------------------

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, `max_tokens` rows."""
        hop = self.config.hop
        return [dict(x=(((4 * self.audio.max_tokens + 1) * hop,), np.float32))]

    def load(self, tuner: JointNarrowing | None = None) -> "Audio":
        """Compile before the first call, so the arena is made once.

        Args:
            tuner: Narrows and packs each version's designs by cost.
        """
        for shapes in self.shapes():
            self.compile(coresident=tuner, **shapes)
        return self

    def embed(self, waveform) -> np.ndarray:
        """The soft tokens of one mono clip at `sample_rate`:
        `(config.tokens(frames), text_dim)` float32, in the text model's
        space.
        """
        c = self.config
        x, values = self.audio.inputs(waveform)
        tokens = self(x, **values).numpy().reshape(-1, c.text_dim)
        return np.asarray(tokens[: values["tokens"]], np.float32)
