# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's audio tower and its projection into the text model's space on the NPU.

As one graph: Hugging Face's ``Gemma4AudioModel`` and ``embed_audio``, its
shape ``AudioConfig``.
"""

import dataclasses
import math
from functools import partial
from types import SimpleNamespace

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, Scratchpad, lm
from iron.common.graph.handle import State
from iron.lm import Conv2d, Linear, RMSNorm, Tower, blocks
from iron.operators.clamp import Clamp
from iron.operators.copy import Copy
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.gemm import GEMM
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.softmax import Softmax


@dataclasses.dataclass(frozen=True)
class AudioConfig(lm.Config):
    # Every projection and attention matmul at HIGHEST.
    precision: Precision = lm.not_json(Precision.HIGHEST, kw_only=True)
    json_prefix = "audio_config."

    hidden_size: int = 1024
    num_hidden_layers: int = 12
    num_attention_heads: int = 8
    intermediate_size: int = lm.not_json(4096)
    mels: int = lm.not_json(128)
    # The two subsampling convolutions' output channels.
    subsampling_conv_channels: tuple[int, int] = dataclasses.field(
        default=(128, 32), metadata={"convert": tuple}
    )
    # A query attends to itself and the `window - 1` positions before it.
    window: int = lm.not_json(12)
    # The key columns a query's band spans: its window, then the zeros that
    # make the row a whole Softmax line.
    band: int = lm.not_json(32)
    attention_logit_cap: float = 50.0
    use_clipped_linears: bool = True
    conv_kernel_size: int = 5
    residual_weight: float = 0.5
    text_dim: int = dataclasses.field(
        default=512, metadata={"json": "/text_config.hidden_size"}
    )
    # The tower's own output width, before embed_audio's projection into
    # text_dim: fixed by the tower's own pretraining, not by whichever text
    # model it is wired into.
    output_proj_dims: int = 1536
    # The feature extractor's: samples per second, per frame and per hop.
    sample_rate: int = lm.not_json(16000)
    frame: int = lm.not_json(320)
    hop: int = lm.not_json(160)
    max_samples: int = lm.not_json(480000)
    # The soft tokens a call takes at most: 30 s of audio gives 750.
    max_tokens: int = lm.not_json(768)

    @property
    def head_dim(self) -> int:
        return self.hidden_size // self.num_attention_heads

    def tokens(self, frames: int) -> int:
        """Return the soft tokens `frames` valid feature frames give.

        Each subsampling convolution keeps every other row.
        """
        rows = -(-frames // 2)
        return -(-rows // 2)

    def frames(self, samples: int) -> int:
        """Return the valid feature frames of a clip of `samples`.

        Those whose last sample is audio, after `frame // 2` zeros in front.
        """
        audio = min(samples, self.max_samples) - (self.frame - self.frame // 2)
        return max(0, -(-audio // self.hop))

    def timing(self) -> np.ndarray:
        """Return the `(window, hidden_size)` float32 timing signal of each distance.

        Each distance a query reaches back: sines, then cosines.
        """
        n = self.hidden_size // 2
        rates = np.exp(np.arange(n) * -(math.log(1e4) / (n - 1))).astype(np.float32)
        angles = np.arange(self.window, dtype=np.float32)[:, None] * rates
        return np.concatenate([np.sin(angles), np.cos(angles)], axis=-1)


class Clipped(iron.Graph):
    """A checkpoint's clippable linear: clamp, project by ``linear``, clamp.

    Projects at ``c.precision``; each clamp only where
    ``c.use_clipped_linears``.
    """

    def __init__(self, c, in_features: int, out_features: int):
        self.linear = Linear(in_features, out_features, False, precision=c.precision)
        bound = partial(iron.param, dtype=np.float32)
        self.input_min = self.input_max = self.output_min = self.output_max = None
        if c.use_clipped_linears:
            self.input_min, self.input_max = bound(), bound()
            self.output_min, self.output_max = bound(), bound()

    def clamp(self, x):
        lo, hi = self.input_min, self.input_max
        if lo is None:
            return x
        assert hi is not None, "input_min and input_max are bound together"
        return Clamp.step(x, low=float(lo), high=float(hi))

    def output(self, y):
        lo, hi = self.output_min, self.output_max
        if lo is None:
            return y
        assert hi is not None, "output_min and output_max are bound together"
        return Clamp.step(y, low=float(lo), high=float(hi))

    @staticmethod
    def same_input(*linears: "Clipped") -> None:
        """Check that ``linears``, which share an input, clamp it alike.

        So the first's ``clamp`` serves them all.

        Raises:
            ValueError: They clamp it to different bounds.
        """
        if linears[0].input_min is None:
            return
        bounds = set()
        for p in linears:
            assert (
                p.input_min is not None and p.input_max is not None
            ), "input_min and input_max are bound together"
            bounds.add((float(p.input_min), float(p.input_max)))
        if len(bounds) > 1:
            raise ValueError(f"linears sharing an input clamp it to {sorted(bounds)}")

    def project(self, x):
        """``x``, already clamped, projected and clamped."""
        return self.output(self.linear(x))

    def body(self, x):
        return self.project(self.clamp(x))


class FeedForward(iron.Graph):
    """A conformer's half step: ``x`` plus its clipped SiLU feed-forward between RMS norms.

    The post norm's weight times ``residual_weight``.
    """

    def __init__(self, c: AudioConfig):
        E, M = c.hidden_size, c.intermediate_size
        self.pre_layer_norm = RMSNorm(E, c.eps)
        self.ffw_layer_1 = Clipped(c, E, M)
        self.ffw_layer_2 = Clipped(c, M, E)
        self.post_layer_norm = RMSNorm(E, c.eps)
        self.residual = c.residual_weight

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        norm = self.post_layer_norm
        norm.weight = iron.param(norm.weight * bfloat16(self.residual))

    def body(self, x):
        h = self.ffw_layer_2(F.silu(self.ffw_layer_1(self.pre_layer_norm(x))))
        return x + self.post_layer_norm(h)


class ConformerAttention(iron.Graph):
    """A conformer's attention, and what it computes from its weights as they load.

    The query scale and the relative-position keys.
    """

    def __init__(self, c: AudioConfig):
        E, H, D = c.hidden_size, c.num_attention_heads, c.head_dim
        self.q_proj, self.k_proj, self.v_proj, self.post = (
            Clipped(c, E, E) for _ in range(4)
        )
        # Read on the host only, in float32.
        self.relative_k_proj = SimpleNamespace(
            weight=iron.param(E, E, dtype=np.float32)
        )
        self.per_dim_scale = iron.param(D, dtype=np.float32)
        self._timing, self.dims = c.timing(), (H, D, c.window, c.band)
        self.logit_cap = c.attention_logit_cap
        self.precision = c.precision
        # The tower's keys, values, scores and probabilities, every layer's.
        self._buffers: tuple[State, State, State, State] | None = None

    def load_state_dict(self, tree, *, path: str = "") -> None:
        """``Graph.load_state_dict``, then the derived tensors.

        Raises:
            ValueError: q, k and v are clamped to different input bounds.
        """
        super().load_state_dict(tree, path=path)
        H, D, W, B = self.dims
        Clipped.same_input(self.q_proj, self.k_proj, self.v_proj)
        # The key scale moved to the queries; the soft cap and the band
        # (window, period) are Softmax's own.
        q_scale = D**-0.5 / math.log(2)
        k_scale = math.log(1 + math.e) / math.log(2)
        softplus = np.logaddexp(0, self.per_dim_scale)
        relative = self._timing @ self.relative_k_proj.weight.T
        relative = relative.reshape(W, H, D)
        # Distance W - 1 - j at band column j, then at j + 1.
        band = np.zeros((H, 2 * B, D), np.float32)
        band[:, :W] = relative[::-1].transpose(1, 0, 2) / k_scale
        band[:, B + 1 : B + 1 + W] = band[:, :W]
        self.q_scale = iron.param(
            np.tile(softplus * (q_scale * k_scale), H).astype(bfloat16)
        )
        self.relative = iron.param(band.astype(bfloat16))

    def body(self, h, tokens):
        """Attention over ``h``, its first ``tokens`` rows valid.

        One GEMM a head over every key, of which each query's band is
        gathered, its relative-position terms keys of the same GEMM.
        """
        T, (H, D, W, B) = h.shape[0], self.dims
        assert self._buffers is not None, "AudioTower sets every layer's buffers"
        keys, values, scores, probs = self._buffers
        K = keys.shape[1]
        h = self.q_proj.clamp(h)
        q = self.q_proj.project(h) * self.q_scale
        k, val = self.k_proj.project(h), self.v_proj.project(h)
        keys[:, W - 1 : W - 1 + T] = k.reshape(T, H, D).transpose(1, 0, 2)
        R = T + W - 1 + (T + W - 1) % 2
        keys[:, R : R + 2 * B] = self.relative
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
                output_dtype=np.float32,
                precision=self.precision,
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
            soft_cap=self.logit_cap,
            input_dtype=np.float32,
            window=W,
            period=T,
        )
        Copy.step(probabilities, probs, dst=band)
        for i in range(H):
            GEMM.step(probs[i, :tokens], values[i], q[i], precision=self.precision)
        o = Copy.step(q.transpose(1, 0, 2)).reshape(T, H * D)
        return self.post(o)


class LightConv(iron.Graph):
    """A conformer's light convolution: ``x`` plus a GLU of its clipped projection.

    A depthwise convolution, an RMS norm, SiLU and a clipped projection.
    """

    def __init__(self, c: AudioConfig):
        E = c.hidden_size
        self.pre_layer_norm = RMSNorm(E, c.eps)
        self.linear_start = Clipped(c, E, 2 * E)
        self.depthwise_conv1d = SimpleNamespace(
            weight=iron.param(E, 1, c.conv_kernel_size)
        )
        self.conv_norm = RMSNorm(E, c.eps)
        self.linear_end = Clipped(c, E, E)

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # A row per tap, each the row RowwiseMul takes.
        weight = self.depthwise_conv1d.weight
        self.planes = iron.param(np.ascontiguousarray(weight[:, 0].T))

    def body(self, x):
        start = self.linear_start
        h = start.clamp(self.pre_layer_norm(x))
        E = self.linear_end.linear.out_features
        a, b = (start.output(y) for y in start.linear.split(h, E, E))
        h = DepthwiseConv1d.step(a * Sigmoid.step(b), self.planes)
        return x + self.linear_end(F.silu(self.conv_norm(h)))


class AudioLayer(iron.Graph):
    """Conformer layer ``i``: a feed-forward half step, attention, the light convolution.

    And a second half step.
    """

    def __init__(self, c: AudioConfig, i: int):
        E = c.hidden_size
        self.feed_forward1 = FeedForward(c)
        self.norm_pre_attn = RMSNorm(E, c.eps)
        self.self_attn = ConformerAttention(c)
        self.norm_post_attn = RMSNorm(E, c.eps)
        self.lconv1d = LightConv(c)
        self.feed_forward2 = FeedForward(c)
        self.norm_out = RMSNorm(E, c.eps)

    def body(self, x, call):
        x = self.feed_forward1(x)
        a = self.self_attn(self.norm_pre_attn(x), call.rows)
        x = self.lconv1d(x + self.norm_post_attn(a))
        return self.norm_out(self.feed_forward2(x))


class SubsampleConvProjection(iron.Graph):
    """The two subsampling convolutions, and the projection after them.

    Each convolution is an `iron.lm.Conv2d` built from its own kernel
    centred over its output channels (so its layer norm is an RMS norm),
    derived once this loads.
    """

    def __init__(self, c: AudioConfig):
        C0, C1 = c.subsampling_conv_channels
        self.layer0 = SimpleNamespace(
            conv=SimpleNamespace(weight=iron.param(C0, 1, 3, 3, dtype=np.float32)),
            norm=SimpleNamespace(weight=iron.param(C0)),
        )
        self.layer1 = SimpleNamespace(
            conv=SimpleNamespace(weight=iron.param(C1, C0, 3, 3, dtype=np.float32)),
            norm=SimpleNamespace(weight=iron.param(C1)),
        )
        self.input_proj_linear = SimpleNamespace(
            weight=iron.param(c.hidden_size, (c.mels // 4) * C1)
        )
        self.mels = c.mels

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        w0 = np.asarray(self.layer0.conv.weight, np.float32)
        w1 = np.asarray(self.layer1.conv.weight, np.float32)
        self.conv0 = Conv2d(
            w0 - w0.mean(axis=0), self.mels, stride=2, padding=1, border=1
        )
        self.conv1 = Conv2d(w1 - w1.mean(axis=0), self.mels // 2 + 2, stride=2)


class OutputProj(iron.Graph):
    """The tower's own output projection, before `embed_audio`'s."""

    def __init__(self, c: AudioConfig):
        self.weight = iron.param(c.output_proj_dims, c.hidden_size)
        self.bias = iron.param(c.output_proj_dims)


class EmbedAudio(iron.Graph):
    """The tower's output projected into the text model's space."""

    def __init__(self, c: AudioConfig):
        self.embedding_projection = SimpleNamespace(
            weight=iron.param(c.text_dim, c.output_proj_dims)
        )


class AudioTower(Tower):
    """The audio tower and `embed_audio` over at most `max_tokens` soft tokens.

    One compile for every clip; called in another graph's body, its steps
    are that graph's.

    Args:
        weights: The checkpoint's; the audio tower's tree is read.
    """

    layer_class = AudioLayer

    def __init__(self, config: AudioConfig, weights: SimpleNamespace):
        c = config
        self.audio_tower = SimpleNamespace()
        super().__init__(config, c.max_tokens, c.max_tokens)
        sub = SubsampleConvProjection(c)
        sub.load_state_dict(weights, path="audio_tower.subsample_conv_projection.")
        output_proj = OutputProj(c)
        output_proj.load_state_dict(weights, path="audio_tower.output_proj.")
        self.audio_tower.subsample_conv_projection = sub
        self.audio_tower.output_proj = output_proj
        self.audio_tower.layers = self.layers
        self.embed_audio = EmbedAudio(c)
        self.embed_audio.load_state_dict(weights, path="embed_audio.")
        self.load_layers(weights, "audio_tower.layers.")
        T = c.max_tokens
        H, D, W, B = c.num_attention_heads, c.head_dim, c.window, c.band
        C0, _ = c.subsampling_conv_channels
        F0 = c.mels // 2
        # The first convolution's output row: each frequency's channels in a
        # slot of their own, with a zero slot either side, the second's padding.
        self.slots = (F0 + 2) * C0
        self.conv0, self.conv1 = sub.conv0, sub.conv1
        self.log_mel = blocks.LogMel(
            c.frame, c.hop, mels=c.mels, sample_rate=c.sample_rate
        )
        self.features = iron.state((4 * T + 2, c.mels))
        self.zero_mel = iron.param(np.zeros((1, c.mels), bfloat16))
        self.subsampled = iron.state((2 * T + 2, self.slots))
        self.zero = iron.param(np.zeros((1, self.slots), bfloat16))
        # The keys' rows: the `W - 1` before the first, the T keys, then from
        # an even row the relative-position rows twice, the second a row on.
        K = -(-(T + W + 2 * B) // 128) * 128
        self.keys = iron.state((H, K, D))
        self.values = iron.state((H, K, D))
        # f32: the scores' chain into Softmax keeps them off bf16's 0.25 ulp
        # at |logit| >= 32 (eg2-audio-bug.md).
        self.scores = iron.state((H, T, K), dtype=np.float32)
        self.probs = iron.state((H, T, K))
        for layer in self.layers:
            layer.self_attn._buffers = self.keys, self.values, self.scores, self.probs

    def logmel(self, wave, frames):
        """Write the log-mel features of `wave`'s valid frames to `features[1 : frames + 1]`.

        Zeros the row after them.

        Args:
            wave: `((F + 1) * hop,)` float32 samples: the `frame // 2` zeros
                in front of the clip, then the clip, zero past it.
            frames: The per-call count of valid feature frames.
        """
        F = wave.shape[0] // self.config.hop - 1
        self.log_mel(wave, self.features[1 : F + 1], frames=frames)
        self.features[frames + 1] = self.zero_mel

    def head(self, x):
        c = self.config
        out = self.audio_tower.output_proj
        x = F.linear(x, out.weight, out.bias, precision=c.precision)
        x = F.rms_norm(x, x.shape[-1:], eps=c.eps)
        projection = self.embed_audio.embedding_projection.weight
        return F.linear(x, projection, precision=c.precision)

    def body(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        wave,
        *,
        n: Scratchpad[np.int32],
        frames: Scratchpad[np.int32],
        tokens: Scratchpad[np.int32],
    ):
        """Return the soft tokens of `wave`, `(max_tokens, text_dim)` bfloat16.

        The first `tokens` of them valid.

        Args:
            wave: `((4 * max_tokens + 1) * hop,)` float32 samples, as
                `logmel` takes them.
            n: The per-call `ceil(frames / 2)`.
            frames: The per-call count of valid feature frames.
            tokens: The per-call `config.tokens(frames)`.
        """
        c = self.config
        C0, C1 = c.subsampling_conv_channels
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
        x = F.linear(
            h.reshape(T, F1 * C1),
            sub.input_proj_linear.weight,
            precision=c.precision,
        )
        return self.forward(x, tokens, None)

    def soft(self, values: dict) -> int:
        return values["tokens"]

    def shapes(self) -> list[dict]:
        """Return the input shapes of each version: one, `max_tokens` soft tokens."""
        c = self.config
        return [dict(wave=(((4 * c.max_tokens + 1) * c.hop,), np.float32))]

    def longest(self) -> dict:
        """Return the per-call values of the longest clip: every frame valid."""
        T = self.config.max_tokens
        return dict(n=2 * T, frames=4 * T, tokens=T)

    def inputs(self, waveform) -> tuple[np.ndarray, dict]:
        """Return a call's `wave` and per-call sizes, `n`, `frames` and `tokens`.

        For a mono `waveform` at `sample_rate`, truncated to `max_samples`
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
