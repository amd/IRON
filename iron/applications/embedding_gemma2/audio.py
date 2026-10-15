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
from iron import Scratchpad
from iron.lm import Model, blocks
from iron.lm.blocks import ACCURATE
from iron.operators.clamp import Clamp
from iron.operators.copy import Copy
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemm import GEMM
from iron.operators.relu import ReLU
from iron.operators.rms_norm import RMSNorm
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax

from .config import PROFILES, AudioConfig


class AudioTower(Model):
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
        tree = weights.audio_tower
        sub = tree.subsample_conv_projection
        if c.frame != 2 * c.hop:
            raise ValueError(f"a frame of {c.frame} samples is not two hops")
        self.config = config
        T = c.max_tokens
        E, H, D, W, B = c.emb_dim, c.n_heads, c.head_dim, c.window, c.band
        C0, C1 = c.channels
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
        self.norm0, self.norm1 = sub.layer0.norm.weight, sub.layer1.norm.weight
        self.input_proj = sub.input_proj_linear.weight
        self.output_proj = tree.output_proj.weight
        self.output_bias = iron.weight(np.tile(tree.output_proj.bias, (T, 1)))
        self.projection = weights.embed_audio.embedding_projection.weight
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
        # The key scale moved to the queries; the soft cap and the band
        # (window, period) are Softmax's own.
        q_scale = D**-0.5 / math.log(2)
        k_scale = math.log(1 + math.e) / math.log(2)
        scale = q_scale * k_scale
        timing = c.timing()
        # A feed-forward's residual weight in its post norm's, exact at 0.5.
        residual = bfloat16(c.residual_weight)
        self.layers = []
        for w in tree.layers:
            a, conv = w.self_attn, w.lconv1d
            ff1, ff2 = w.feed_forward1, w.feed_forward2
            clipped = {
                name: SimpleNamespace(
                    weight=linear.linear.weight,
                    input=dict(
                        low=float(linear.input_min), high=float(linear.input_max)
                    ),
                    output=dict(
                        low=float(linear.output_min), high=float(linear.output_max)
                    ),
                )
                for name, linear in dict(
                    q=a.q_proj,
                    k=a.k_proj,
                    v=a.v_proj,
                    post=a.post,
                    start=conv.linear_start,
                    end=conv.linear_end,
                    up1=ff1.ffw_layer_1,
                    down1=ff1.ffw_layer_2,
                    up2=ff2.ffw_layer_1,
                    down2=ff2.ffw_layer_2,
                ).items()
            }
            if not clipped["q"].input == clipped["k"].input == clipped["v"].input:
                raise ValueError("q, k and v are clamped to different input bounds")
            softplus = np.logaddexp(0, np.asarray(a.per_dim_scale, np.float32))
            relative = timing @ np.asarray(a.relative_k_proj.weight, np.float32).T
            relative = relative.reshape(W, H, D)
            # Distance W - 1 - j at band column j, then at j + 1.
            band = np.zeros((H, 2 * B, D), np.float32)
            band[:, :W] = relative[::-1].transpose(1, 0, 2) / k_scale
            band[:, B + 1 : B + 1 + W] = band[:, :W]
            self.layers.append(
                SimpleNamespace(
                    ff=[
                        SimpleNamespace(
                            pre=f.pre_layer_norm.weight,
                            post=f.post_layer_norm.weight * residual,
                            up=clipped[f"up{j}"],
                            down=clipped[f"down{j}"],
                        )
                        for j, f in ((1, ff1), (2, ff2))
                    ],
                    norm_pre_attn=w.norm_pre_attn.weight,
                    norm_post_attn=w.norm_post_attn.weight,
                    norm_out=w.norm_out.weight,
                    attn=SimpleNamespace(
                        q=clipped["q"],
                        k=clipped["k"],
                        v=clipped["v"],
                        post=clipped["post"],
                        scale=iron.weight(
                            np.tile(np.tile(softplus * scale, H), (T, 1)).astype(
                                bfloat16
                            )
                        ),
                        relative=band.astype(bfloat16),
                    ),
                    conv=SimpleNamespace(
                        pre=conv.pre_layer_norm.weight,
                        start=clipped["start"],
                        glu=(clipped["start"].weight[:E], clipped["start"].weight[E:]),
                        planes=np.ascontiguousarray(
                            conv.depthwise_conv1d.weight[:, 0].T
                        ),
                        norm=conv.conv_norm.weight,
                        end=clipped["end"],
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
        F = wave.shape[0] // self.config.hop - 1
        self.log_mel(wave, self.features[1 : F + 1], frames=frames)
        Copy.step(self.zero_mel, self.features[frames + 1])

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
        c = self.config
        C0, C1 = c.channels
        F1 = c.mels // 4
        T = c.max_tokens
        # The first row of each convolution's input is its zero padding in time.
        self.logmel(wave, frames)
        h = self.conv0(self.features, rows=n)
        h = RMSNorm.step(
            h.reshape(2 * T * self.slots // C0, C0), weight=self.norm0, epsilon=c.eps
        )
        ReLU.step(h.reshape(2 * T, self.slots), self.subsampled[1 : 2 * T + 1])
        Copy.step(self.zero, self.subsampled[n + 1])
        h = self.conv1(self.subsampled, rows=tokens)
        h = ReLU.step(
            RMSNorm.step(h.reshape(T * F1, C1), weight=self.norm1, epsilon=c.eps)
        )
        x = GEMM.step(
            h.reshape(T, F1 * C1), self.input_proj, b_col_maj=True, **ACCURATE
        )
        for w in self.layers:
            x = self.layer(w, x, tokens)
        x = GEMM.step(x, self.output_proj, b_col_maj=True, **ACCURATE)
        x = RMSNorm.step(
            ElementwiseAdd.step(x, self.output_bias[:tokens]), epsilon=c.eps
        )
        return GEMM.step(x, self.projection, b_col_maj=True, **ACCURATE)

    def linear(self, w, x, weight=None):
        """`x`, already clamped to the input bounds of `w`, projected by
        `weight` (`w`'s own by default) and clamped to its output bounds.
        """
        weight = w.weight if weight is None else weight
        return Clamp.step(GEMM.step(x, weight, b_col_maj=True, **ACCURATE), **w.output)

    def layer(self, w, x, tokens):
        c = self.config
        x = self.feed_forward(w.ff[0], x)
        h = RMSNorm.step(x, weight=w.norm_pre_attn, epsilon=c.eps)
        a = RMSNorm.step(
            self.attention(w.attn, h, tokens), weight=w.norm_post_attn, epsilon=c.eps
        )
        x = self.feed_forward(
            w.ff[1], self.light_conv(w.conv, ElementwiseAdd.step(x, a))
        )
        return RMSNorm.step(x, weight=w.norm_out, epsilon=c.eps)

    def feed_forward(self, w, x):
        c = self.config
        h = Clamp.step(RMSNorm.step(x, weight=w.pre, epsilon=c.eps), **w.up.input)
        h = self.linear(w.up, h)
        h = self.linear(w.down, Clamp.step(SiLU.step(h), **w.down.input))
        return ElementwiseAdd.step(x, RMSNorm.step(h, weight=w.post, epsilon=c.eps))

    def attention(self, w, h, tokens):
        c = self.config
        T, H, D, W, B = h.shape[0], c.n_heads, c.head_dim, c.window, c.band
        K = self.width
        keys, values = self.keys, self.values
        scores, probs = self.scores, self.probs
        h = Clamp.step(h, **w.q.input)
        q = ElementwiseMul.step(self.linear(w.q, h), w.scale[:tokens])
        k, val = self.linear(w.k, h), self.linear(w.v, h)
        Copy.step(k.reshape(T, H, D).transpose(1, 0, 2), keys[:, W - 1 : W - 1 + T])
        R = T + W - 1 + (T + W - 1) % 2
        Copy.step(w.relative, keys[:, R : R + 2 * B])
        Copy.step(val.reshape(T, H, D).transpose(1, 0, 2), values[:, W - 1 : W - 1 + T])
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
                **ACCURATE,
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
            GEMM.step(probs[i, :tokens], values[i], q[i], **ACCURATE)
        o = Copy.step(q.transpose(1, 0, 2)).reshape(T, H * D)
        return self.linear(w.post, Clamp.step(o, **w.post.input))

    def light_conv(self, w, x):
        c = self.config
        h = Clamp.step(RMSNorm.step(x, weight=w.pre, epsilon=c.eps), **w.start.input)
        a, b = (self.linear(w.start, h, weight) for weight in w.glu)
        h = DepthwiseConv1d.step(ElementwiseMul.step(a, Sigmoid.step(b)), w.planes)
        h = SiLU.step(RMSNorm.step(h, weight=w.norm, epsilon=c.eps))
        return ElementwiseAdd.step(x, self.linear(w.end, Clamp.step(h, **w.end.input)))

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

    def soft_tokens(self, waveform) -> np.ndarray:
        """The soft tokens of one mono clip at `sample_rate`:
        `(config.tokens(frames), text_dim)` float32, in the text model's
        space.
        """
        wave, values = self.inputs(waveform)
        tokens = self(wave, **values).numpy().reshape(-1, self.config.text_dim)
        return np.asarray(tokens[: values["tokens"]], np.float32)
