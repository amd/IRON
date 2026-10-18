# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's audio tower and its projection into the text model's
space on the NPU, as one graph.
"""

import math
from types import SimpleNamespace

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, Scratchpad
from iron.lm import Tower, blocks
from iron.operators.copy import Copy
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.gemm import GEMM
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.softmax import Softmax

from .blocks import Clipped
from .config import PROFILES, AudioConfig


class AudioTower(Tower):
    """The audio tower and `embed_audio` over at most `max_tokens` soft
    tokens, one compile for every clip; called in another graph's body, its
    steps are that graph's.

    A call takes the `4 * T + 1` hops of waveform its `4 * T` frames read
    (the first the zeros in front of the clip, zero past it), `T` being
    `max_tokens`, and per call the valid frames, `n`, the rows of the
    first convolution's output that are valid, and `tokens`, the soft
    tokens, which bound the operators over each. Its features are
    `iron.lm.LogMel`'s. The frame after the valid ones is zeroed, as are the
    first convolution's rows after its valid ones before the second reads
    them, as Hugging Face's mask does. Past that nothing masks padding: the
    attention and the light convolution look only back, so a valid token
    never reads a padded one.

    Each subsampling convolution is an `iron.lm.Conv2d`, its weight centered
    over the output channels so that its layer norm is an RMS norm.
    Attention is one GEMM a head over every key, of which each query's band
    of `band` columns (its window, the rest masked) is gathered, its
    relative-position terms keys of the same GEMM; the probabilities are
    scattered back to the band of zeros for the GEMM with the values. Every
    clipped linear's clamps run as `Clamp`s.

    Args:
        config: The tower's shape.
        weights: The checkpoint's; the audio tower's tree is read.
    """

    profile = PROFILES

    def __init__(self, config: AudioConfig, weights: SimpleNamespace):
        c = config
        tree = self.audio_tower = weights.audio_tower
        self.embed_audio = weights.embed_audio
        sub = tree.subsample_conv_projection
        if c.frame != 2 * c.hop:
            raise ValueError(f"a frame of {c.frame} samples is not two hops")
        super().__init__(config, tree.layers, c.max_tokens, c.max_tokens)
        T = c.max_tokens
        H, D, W, B = c.num_attention_heads, c.head_dim, c.window, c.band
        C0, _ = c.channels
        F0 = c.mels // 2
        # The first convolution's output row: each frequency's channels in a
        # slot of their own, with a zero slot either side, the second's padding.
        self.slots = (F0 + 2) * C0
        w0, w1 = (
            np.asarray(layer.conv.weight, np.float32)
            for layer in (sub.layer0, sub.layer1)
        )
        self.conv0 = blocks.Conv2d(
            w0 - w0.mean(axis=0), c.mels, stride=2, padding=1, border=1
        )
        self.conv1 = blocks.Conv2d(w1 - w1.mean(axis=0), F0 + 2, stride=2)
        self.log_mel = blocks.LogMel(
            frame=c.frame,
            hop=c.hop,
            fft=c.fft,
            mels=c.mels,
            sample_rate=c.sample_rate,
            max_hz=c.max_hz,
            mel_floor=c.mel_floor,
        )
        self.features = iron.state((4 * T + 2, c.mels))
        self.zero_mel = np.zeros((1, c.mels), bfloat16)
        self.subsampled = iron.state((2 * T + 2, self.slots))
        self.zero = np.zeros((1, self.slots), bfloat16)
        # The keys' rows: the `W - 1` before the first, the T keys, then from
        # an even row the relative-position rows twice, the second a row on.
        self.width = K = -(-(T + W + 2 * B) // 128) * 128
        self.keys = iron.state((H, K, D))
        self.values = iron.state((H, K, D))
        # f32: the scores' chain into Softmax keeps them off bf16's 0.25 ulp
        # at |logit| >= 32 (eg2-audio-bug.md).
        self.scores = iron.state((H, T, K), dtype=np.float32)
        self.probs = iron.state((H, T, K))

    def sanitize(self, w):
        """``w`` and what its layer computes from it once: attention's
        query scale and relative-position keys, each feed-forward's post norm
        times ``residual_weight``, the light convolution's tap planes.

        Raises:
            ValueError: q, k and v are clamped to different input bounds.
        """
        c = self.config
        H, D, W, B = c.num_attention_heads, c.head_dim, c.window, c.band
        a, conv = w.self_attn, w.lconv1d
        if not (
            (a.q_proj.input_min, a.q_proj.input_max)
            == (a.k_proj.input_min, a.k_proj.input_max)
            == (a.v_proj.input_min, a.v_proj.input_max)
        ):
            raise ValueError("q, k and v are clamped to different input bounds")
        # The key scale moved to the queries; the soft cap and the band
        # (window, period) are Softmax's own.
        q_scale = D**-0.5 / math.log(2)
        k_scale = math.log(1 + math.e) / math.log(2)
        softplus = np.logaddexp(0, np.asarray(a.per_dim_scale, np.float32))
        relative = c.timing() @ np.asarray(a.relative_k_proj.weight, np.float32).T
        relative = relative.reshape(W, H, D)
        # Distance W - 1 - j at band column j, then at j + 1.
        band = np.zeros((H, 2 * B, D), np.float32)
        band[:, :W] = relative[::-1].transpose(1, 0, 2) / k_scale
        band[:, B + 1 : B + 1 + W] = band[:, :W]
        residual = bfloat16(c.residual_weight)
        f1, f2 = (
            SimpleNamespace(**vars(f), post_norm=f.post_layer_norm.weight * residual)
            for f in (w.feed_forward1, w.feed_forward2)
        )
        a = SimpleNamespace(
            **vars(a),
            q_scale=np.tile(softplus * (q_scale * k_scale), H).astype(bfloat16),
            relative=band.astype(bfloat16),
        )
        planes = np.ascontiguousarray(conv.depthwise_conv1d.weight[:, 0].T)
        conv = SimpleNamespace(**vars(conv), planes=planes)
        return SimpleNamespace(
            **{
                **vars(w),
                "self_attn": a,
                "feed_forward1": f1,
                "feed_forward2": f2,
                "lconv1d": conv,
            }
        )

    def logmel(self, wave, frames):
        """Write the log-mel features of `wave`'s valid frames to
        `features[1 : frames + 1]`, and zero the row after them.

        Args:
            wave: `((F + 1) * hop,)` float32 samples: the `frame // 2` zeros
                in front of the clip, then the clip, zero past it.
            frames: The per-call valid frames, an int32 value.
        """
        F = wave.shape[0] // self.config.hop - 1
        self.log_mel(wave, self.features[1 : F + 1], frames=frames)
        self.features[frames + 1] = self.zero_mel

    def front(self, wave, *, n, frames, tokens):
        """The rows of `wave`'s `tokens` soft tokens before the first layer;
        nothing rotates them.
        """
        c = self.config
        C0, C1 = c.channels
        F1 = c.mels // 4
        T = c.max_tokens
        # The first row of each convolution's input is its zero padding in time.
        self.logmel(wave, frames)
        sub = self.audio_tower.subsample_conv_projection
        h = self.conv0(self.features, rows=n)
        h = F.rms_norm(
            h.reshape(2 * T * self.slots // C0, C0),
            (C0,),
            sub.layer0.norm.weight,
            c.eps,
        )
        ReLU.step(h.reshape(2 * T, self.slots), self.subsampled[1 : 2 * T + 1])
        self.subsampled[n + 1] = self.zero
        h = self.conv1(self.subsampled, rows=tokens)
        h = ReLU.step(
            F.rms_norm(h.reshape(T * F1, C1), (C1,), sub.layer1.norm.weight, c.eps)
        )
        x = GEMM.step(
            h.reshape(T, F1 * C1),
            sub.input_proj_linear.weight,
            b_col_maj=True,
            precision=Precision.HIGHEST,
        )
        return x, None

    def head(self, x):
        c = self.config
        out = self.audio_tower.output_proj
        x = GEMM.step(x, out.weight, b_col_maj=True, precision=Precision.HIGHEST)
        x = F.rms_norm(x + out.bias, out.bias.shape, eps=c.eps)
        projection = self.embed_audio.embedding_projection.weight
        return GEMM.step(x, projection, b_col_maj=True, precision=Precision.HIGHEST)

    def body(
        self,
        wave,
        *,
        n: Scratchpad[np.int32],
        frames: Scratchpad[np.int32],
        tokens: Scratchpad[np.int32],
    ):
        """The soft tokens of `wave`, `(max_tokens, text_dim)` bfloat16, the
        first `tokens` of them valid.

        Args:
            wave: `((4 * max_tokens + 1) * hop,)` float32 samples, as
                `logmel` takes them.
            n: The per-call `ceil(frames / 2)`.
            frames: The per-call valid frames.
            tokens: The per-call `config.tokens(frames)`.
        """
        x, angles = self.front(wave, n=n, frames=frames, tokens=tokens)
        return self.forward(x, tokens, angles)

    def layer(self, step, i, w, x):
        """The conformer layer `i`: a feed-forward half step, attention, the
        light convolution and a second half step.
        """
        c = self.config
        x = self.feed_forward(w.feed_forward1, x)
        h = F.rms_norm(x, x.shape[-1:], w.norm_pre_attn.weight, c.eps)
        a = F.rms_norm(
            self.attention(w.self_attn, h, step.rows),
            x.shape[-1:],
            w.norm_post_attn.weight,
            c.eps,
        )
        h = self.light_conv(w.lconv1d, x + a)
        x = self.feed_forward(w.feed_forward2, h)
        return F.rms_norm(x, x.shape[-1:], w.norm_out.weight, c.eps)

    def soft(self, values: dict) -> int:
        return values["tokens"]

    def feed_forward(self, f, x):
        c = self.config
        h = Clipped(f.ffw_layer_1)(
            F.rms_norm(x, x.shape[-1:], f.pre_layer_norm.weight, c.eps)
        )
        h = Clipped(f.ffw_layer_2)(F.silu(h))
        return x + F.rms_norm(h, h.shape[-1:], f.post_norm, c.eps)

    def attention(self, a, h, tokens):
        c = self.config
        T, H, D, W, B = h.shape[0], c.num_attention_heads, c.head_dim, c.window, c.band
        K = self.width
        keys, values = self.keys, self.values
        scores, probs = self.scores, self.probs
        q_proj = Clipped(a.q_proj)
        h = q_proj.clamp(h)
        q = q_proj.project(h) * a.q_scale
        k, val = Clipped(a.k_proj).project(h), Clipped(a.v_proj).project(h)
        keys[:, W - 1 : W - 1 + T] = k.reshape(T, H, D).transpose(1, 0, 2)
        R = T + W - 1 + (T + W - 1) % 2
        keys[:, R : R + 2 * B] = a.relative
        values[:, W - 1 : W - 1 + T] = val.reshape(T, H, D).transpose(1, 0, 2)
        q = Copy.step(q.reshape(T, H, D).transpose(1, 0, 2))
        # Over every key: those past the valid ones are stale but finite, as
        # only bounded copies write them.
        for i in range(H):
            GEMM.step(
                q[i],
                keys[i],
                scores[i],
                b_col_maj=True,
                dtype_out=np.float32,
                precision=Precision.HIGHEST,
            )
        # Query t's band starts at the even column of t and t - 1, its
        # relative terms at R or R + band.
        pairs = [H, T // 2, 2, B]
        band = TensorAccessPattern((H, T, K), 0, pairs, [T * K, 2 * K + 2, K, 1])
        relative = TensorAccessPattern((H, T, K), R, pairs, [T * K, 2 * K, K + B, 1])
        logits = Copy.step(scores, src=band, dtype=np.float32).reshape(H * T, B)
        position = Copy.step(scores, src=relative, dtype=np.float32).reshape(H * T, B)
        probabilities = Softmax.step(
            logits,
            addend=position,
            soft_cap=c.logit_cap,
            input_dtype=np.float32,
            window=W,
            period=T,
        )
        Copy.step(probabilities, probs, dst=band)
        for i in range(H):
            GEMM.step(probs[i, :tokens], values[i], q[i], precision=Precision.HIGHEST)
        o = Copy.step(q.transpose(1, 0, 2)).reshape(T, H * D)
        return Clipped(a.post)(o)

    def light_conv(self, conv, x):
        c = self.config
        start = Clipped(conv.linear_start)
        h = start.clamp(F.rms_norm(x, x.shape[-1:], conv.pre_layer_norm.weight, c.eps))
        glu, E = conv.linear_start.linear.weight, c.hidden_size
        a, b = start.project(h, glu[:E]), start.project(h, glu[E:])
        h = DepthwiseConv1d.step(a * Sigmoid.step(b), conv.planes)
        h = F.silu(F.rms_norm(h, h.shape[-1:], conv.conv_norm.weight, c.eps))
        return x + Clipped(conv.linear_end)(h)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, `max_tokens` soft tokens."""
        c = self.config
        return [dict(wave=(((4 * c.max_tokens + 1) * c.hop,), np.float32))]

    def longest(self) -> dict:
        """The per-call values of the longest clip: every frame valid."""
        T = self.config.max_tokens
        return dict(n=2 * T, frames=4 * T, tokens=T)

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
        if not 0 < tokens <= c.max_tokens:
            raise ValueError(
                f"{audio.size} samples give {tokens} soft tokens, not 1 to "
                f"{c.max_tokens}"
            )
        # Samples past the last frame are only ever read by invalid ones.
        wave = np.zeros((4 * c.max_tokens + 1) * c.hop, np.float32)
        held = min(audio.size, wave.size - c.hop)
        wave[c.hop : c.hop + held] = audio[:held]
        return wave, dict(n=-(-frames // 2), frames=frames, tokens=tokens)
