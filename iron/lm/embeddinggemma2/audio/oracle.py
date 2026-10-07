# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's audio tower in float32 on the host, the oracle the
NPU tower is judged by.
"""

import math
from types import SimpleNamespace

import numpy as np

from ..oracle import rms_norm
from .model import AudioConfig, sinusoid


def widen(tree):
    """`tree`, a weight tree of namespaces and lists, in float32."""
    if isinstance(tree, list):
        return [widen(t) for t in tree]
    if isinstance(tree, SimpleNamespace):
        return SimpleNamespace(**{k: widen(v) for k, v in vars(tree).items()})
    return np.asarray(tree, np.float32)


def clipped(w, x):
    """`x` through the clipped linear `w`: clamped to its input bounds,
    projected, and clamped to its output bounds.
    """
    y = np.clip(x, w.input_min, w.input_max) @ w.weight.T
    return np.clip(y, w.output_min, w.output_max)


def conv(x, w):
    """The 3x3 convolution of stride 2 and zero padding 1 of `x`
    `(time, freq, in)` by `w` `(out, in, 3, 3)`, channels last.
    """
    T, F = (x.shape[0] + 1) // 2, (x.shape[1] + 1) // 2
    x = np.pad(x, ((1, 1), (1, 1), (0, 0)))
    patches = np.stack(
        [x[a : a + 2 * T : 2, b : b + 2 * F : 2] for a in range(3) for b in range(3)],
        axis=2,
    )
    return patches.reshape(T, F, -1) @ w.transpose(2, 3, 1, 0).reshape(-1, w.shape[0])


class AudioOracle:
    """EmbeddingGemma 2's audio tower and its projection into the text
    model's space in float32, on the host, as Hugging Face computes them.

    Its gradient clipping (`1e10`) is left out: it is the identity on
    activations below it.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
    """

    def __init__(self, config: AudioConfig, weights: SimpleNamespace):
        self.config = config
        self.weights = widen(weights)
        self.distances = sinusoid(config)

    def subsample(self, features, frames: int):
        """The two convolutions over `features` `(F, mels)` with `frames`
        valid, each masking the rows its input's mask says are padding, and
        the input projection: `(ceil(F / 4), hidden)`.
        """
        c, w = self.config, self.weights
        mask = np.arange(features.shape[0]) < frames
        x = features[:, :, None]
        for kernel, norm in ((w.conv0, w.norm0), (w.conv1, w.norm1)):
            x = conv(x * mask[:, None, None], kernel)
            x = x - x.mean(axis=-1, keepdims=True)
            x = x * np.power(
                np.mean(x * x, axis=-1, keepdims=True) + np.float32(c.eps),
                np.float32(-0.5),
            )
            x = np.maximum(x * norm, 0)
            mask = mask[::2]
        return x.reshape(x.shape[0], -1) @ w.input_proj.T

    def feed_forward(self, w, x):
        c = self.config
        h = clipped(w.up, rms_norm(x, w.pre, c.eps))
        h = clipped(w.down, h * (0.5 * (1 + np.tanh(0.5 * h))))
        return x + rms_norm(h, w.post, c.eps) * np.float32(c.residual_weight)

    def attention(self, w, x):
        """The attention of each position over itself and the `window - 1`
        before it, with a learned relative-position term per distance, the
        logits soft-capped.
        """
        c = self.config
        T, H, D = x.shape[0], c.n_heads, c.head_dim
        q_scale = np.float32(D**-0.5 / math.log(2))
        k_scale = np.float32(math.log(1 + math.e) / math.log(2))
        q = clipped(w.q, x).reshape(T, H, D) * q_scale
        q = q * np.logaddexp(np.float32(0), w.per_dim_scale)
        k = clipped(w.k, x).reshape(T, H, D) * k_scale
        v = clipped(w.v, x).reshape(T, H, D)
        relative = (self.distances @ w.relative.T).reshape(c.window, H, D)
        logits = q.transpose(1, 0, 2) @ k.transpose(1, 2, 0)
        d = np.arange(T)[:, None] - np.arange(T)[None, :]
        band = (d >= 0) & (d < c.window)
        rows, cols = np.nonzero(band)
        position = np.einsum("qhd,lhd->hql", q, relative)
        logits[:, rows, cols] += position[:, rows, d[rows, cols]]
        cap = np.float32(c.logit_cap)
        logits = np.where(band, np.tanh(logits / cap) * cap, np.float32(-1e9))
        logits -= logits.max(axis=-1, keepdims=True)
        p = np.exp(logits)
        p /= p.sum(axis=-1, keepdims=True)
        o = (p @ v.transpose(1, 0, 2)).transpose(1, 0, 2).reshape(T, H * D)
        return clipped(w.post, o)

    def light_conv(self, w, x):
        """The gated linear unit, then a causal depthwise convolution in time."""
        c = self.config
        E, K, T = c.hidden, c.conv_kernel, x.shape[0]
        h = clipped(w.start, rms_norm(x, w.pre, c.eps))
        h = h[:, :E] * (0.5 * (1 + np.tanh(0.5 * h[:, E:])))
        h = np.pad(h, ((K - 1, 0), (0, 0)))
        h = sum(h[j : j + T] * w.depthwise[:, 0, j] for j in range(K))
        h = rms_norm(h, w.norm, c.eps)
        return x + clipped(w.end, h * (0.5 * (1 + np.tanh(0.5 * h))))

    def layer(self, w, x):
        c = self.config
        x = self.feed_forward(w.ff1, x)
        a = self.attention(w.attn, rms_norm(x, w.norm_pre_attn, c.eps))
        x = x + rms_norm(a, w.norm_post_attn, c.eps)
        x = self.feed_forward(w.ff2, self.light_conv(w.conv, x))
        return rms_norm(x, w.norm_out, c.eps)

    def __call__(self, features, frames: int) -> np.ndarray:
        """The soft tokens of `features` `(F, mels)`, `frames` of them valid,
        in the text model's space: `(config.tokens(frames), text_dim)`.
        """
        c, w = self.config, self.weights
        x = self.subsample(np.asarray(features, np.float32), frames)
        for layer in w.layers:
            x = self.layer(layer, x)
        x = x[: c.tokens(frames)] @ w.output_proj.T + w.output_bias
        return rms_norm(x, np.float32(1), c.eps) @ w.projection.T
