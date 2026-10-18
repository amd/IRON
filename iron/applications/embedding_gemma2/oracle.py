# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 in float32 on the host, as Hugging Face computes it:
the oracles its graphs are judged by, the text encoder's
(``EmbeddingGemmaOracle``), the audio tower's (``AudioOracle``, with the
feature extractor) and the vision tower's (``VisionOracle``, with the image
processor), each an ``Oracle``; the text encoder's and the vision tower's
layers are ``iron.lm.Layer.oracle``.
"""

import math
from collections.abc import Mapping
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16

from iron.lm import LogMel, Oracle, rope_angles, widen
from iron.operators.resample.reference import resize

from .config import AudioConfig, Config, VisionConfig


class EmbeddingGemmaOracle(Oracle):
    """The text encoder.

    Args:
        config: The encoder's shape.
        weights: The checkpoint's; the text encoder's tree is read.
    """

    def __init__(self, config: Config, weights: SimpleNamespace):
        super().__init__(config)
        w = weights.language_model
        # Widened by the rows a call looks up: the whole table in float32 is 512 MB.
        self.embedding = w.embed_tokens.weight
        self.norm, self.projection, self.ple, self.ple_norm, self.layers = widen(
            [
                w.norm.weight,
                w.embedding_projection.weight,
                w.ple.per_layer_model_projection.weight,
                w.ple.per_layer_projection_norm.weight,
                w.layers,
            ]
        )

    def layer(self, i: int, angles: np.ndarray, w, x, ple):
        """Layer `i` on `x` `(n, hidden_size)`, with its per-layer input `ple`
        `(n, ple_dim)` and the RoPE table `angles` of its head size.
        """
        return self.config.layer(i).oracle(self, w, x, self.attend, angles, ple=ple)

    def token_states(self, tokens, soft: Mapping[int, np.ndarray] = {}) -> np.ndarray:
        """Each token's `(n, out_dim)` output, before pooling.

        Args:
            tokens: The token ids.
            soft: Each placeholder id's soft tokens `(k, hidden_size)`, the
                `k` placeholders' embeddings in order.

        Raises:
            ValueError: A placeholder's count is not its soft tokens'.
        """
        c = self.config
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n = tokens.size
        # Hugging Face rounds the scale to the weights' dtype: 22.625 in bfloat16 only.
        x = self.embedding[tokens].astype(np.float32) * np.float32(
            np.sqrt(c.hidden_size)
        )
        for token, rows in soft.items():
            at = tokens == token
            if at.sum() != len(rows):
                raise ValueError(
                    f"{at.sum()} placeholders {token} for {len(rows)} soft tokens"
                )
            x[at] = rows
        ple = (x @ self.ple.T) * np.float32(c.hidden_size**-0.5)
        ple = self.rms_norm(
            ple.reshape(n, c.num_hidden_layers, c.ple_dim), self.ple_norm
        )
        angles = {
            D: rope_angles(D, n, base)
            for _, D, base in map(c.heads, range(c.num_hidden_layers))
        }
        for i, w in enumerate(self.layers):
            x = self.layer(i, angles[c.heads(i)[1]], w, x, ple[:, i])
        return self.rms_norm(x, self.norm) @ self.projection.T

    def encode(
        self, tokens, dims: int | None = None, soft: Mapping[int, np.ndarray] = {}
    ) -> np.ndarray:
        """The embedding of `tokens`, with `soft` as `token_states` takes it:
        the mean of their states, its first `dims` L2-normalized.
        """
        e = self.token_states(tokens, soft).mean(axis=0)[:dims]
        return e / np.linalg.norm(e)


class AudioOracle(Oracle):
    """The audio tower and its projection into the text model's space, and
    Hugging Face's feature extractor before it.

    Its gradient clipping (`1e10`) is left out: it is the identity on
    activations below it.

    Args:
        config: The tower's shape.
        weights: The checkpoint's; the audio tower's tree is read.
    """

    def __init__(self, config: AudioConfig, weights: SimpleNamespace):
        super().__init__(config)
        c = config
        self.weights = widen(weights.audio_tower)
        self.projection = widen(weights.embed_audio.embedding_projection.weight)
        self.timing = c.timing()
        self.log_mel = LogMel(
            frame=c.frame,
            hop=c.hop,
            fft=c.fft,
            mels=c.mels,
            sample_rate=c.sample_rate,
            max_hz=c.max_hz,
            mel_floor=c.mel_floor,
        )

    def features(self, waveform) -> tuple[np.ndarray, int]:
        """The feature extractor's `(frames, mels)` float32 log-mel features
        of a mono `waveform` at `sample_rate`, truncated to `max_samples`,
        and how many are valid. A frame is the `frame` samples from its hop
        (`iron.lm.LogMel.exact`), after `frame // 2` zeros in front; it is
        valid when its last sample is audio rather than the padding to a
        multiple of `pad_to` samples. Invalid frames are zero.
        """
        c = self.config
        audio = np.asarray(waveform, np.float32).reshape(-1)[: c.max_samples]
        n = audio.size
        wave = np.pad(audio, (c.frame // 2, -(-n // c.pad_to) * c.pad_to - n))
        features = self.log_mel.oracle(wave, (wave.size - c.frame - 1) // c.hop + 1)
        valid = c.frames(n)
        features[valid:] = 0
        return features, valid

    @staticmethod
    def clipped(w, x):
        """`x` through the clipped linear `w`: clamped to its input bounds,
        projected, and clamped to its output bounds.
        """
        y = np.clip(x, w.input_min, w.input_max) @ w.linear.weight.T
        return np.clip(y, w.output_min, w.output_max)

    @staticmethod
    def conv(x, w):
        """The 3x3 convolution of stride 2 and zero padding 1 of `x`
        `(time, freq, in)` by `w` `(out, in, 3, 3)`, channels last.
        """
        T, F = (x.shape[0] + 1) // 2, (x.shape[1] + 1) // 2
        x = np.pad(x, ((1, 1), (1, 1), (0, 0)))
        patches = np.stack(
            [
                x[a : a + 2 * T : 2, b : b + 2 * F : 2]
                for a in range(3)
                for b in range(3)
            ],
            axis=2,
        )
        return patches.reshape(T, F, -1) @ w.transpose(2, 3, 1, 0).reshape(
            -1, w.shape[0]
        )

    def subsample(self, features, frames: int):
        """The two convolutions over `features` `(F, mels)` with `frames`
        valid, each masking the rows its input's mask says are padding, and
        the input projection: `(ceil(F / 4), hidden_size)`.
        """
        sub = self.weights.subsample_conv_projection
        mask = np.arange(features.shape[0]) < frames
        x = features[:, :, None]
        for layer in (sub.layer0, sub.layer1):
            x = self.conv(x * mask[:, None, None], layer.conv.weight)
            x = x - x.mean(axis=-1, keepdims=True)
            x = np.maximum(self.rms_norm(x, layer.norm.weight), 0)
            mask = mask[::2]
        return x.reshape(x.shape[0], -1) @ sub.input_proj_linear.weight.T

    def feed_forward(self, w, x):
        h = self.clipped(w.ffw_layer_1, self.rms_norm(x, w.pre_layer_norm.weight))
        h = self.clipped(w.ffw_layer_2, h * (0.5 * (1 + np.tanh(0.5 * h))))
        post = self.rms_norm(h, w.post_layer_norm.weight)
        return x + post * np.float32(self.config.residual_weight)

    def attention(self, w, x):
        """The attention of each position over itself and the `window - 1`
        before it, with a learned relative-position term per distance, the
        logits soft-capped.
        """
        c = self.config
        T, H, D = x.shape[0], c.num_attention_heads, c.head_dim
        q_scale = np.float32(D**-0.5 / math.log(2))
        k_scale = np.float32(math.log(1 + math.e) / math.log(2))
        q = self.clipped(w.q_proj, x).reshape(T, H, D) * q_scale
        q = q * np.logaddexp(np.float32(0), w.per_dim_scale)
        k = self.clipped(w.k_proj, x).reshape(T, H, D) * k_scale
        v = self.clipped(w.v_proj, x).reshape(T, H, D)
        relative = self.timing @ w.relative_k_proj.weight.T
        relative = relative.reshape(c.window, H, D)
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
        return self.clipped(w.post, o)

    def light_conv(self, w, x):
        """The gated linear unit, then a causal depthwise convolution in time."""
        c = self.config
        E, K, T = c.hidden_size, c.conv_kernel, x.shape[0]
        h = self.clipped(w.linear_start, self.rms_norm(x, w.pre_layer_norm.weight))
        h = h[:, :E] * (0.5 * (1 + np.tanh(0.5 * h[:, E:])))
        h = np.pad(h, ((K - 1, 0), (0, 0)))
        h = sum(h[j : j + T] * w.depthwise_conv1d.weight[:, 0, j] for j in range(K))
        h = self.rms_norm(h, w.conv_norm.weight)
        return x + self.clipped(w.linear_end, h * (0.5 * (1 + np.tanh(0.5 * h))))

    def layer(self, w, x):
        x = self.feed_forward(w.feed_forward1, x)
        a = self.attention(w.self_attn, self.rms_norm(x, w.norm_pre_attn.weight))
        x = x + self.rms_norm(a, w.norm_post_attn.weight)
        x = self.feed_forward(w.feed_forward2, self.light_conv(w.lconv1d, x))
        return self.rms_norm(x, w.norm_out.weight)

    def tower(self, features, frames: int) -> np.ndarray:
        """The soft tokens of `features` `(F, mels)`, `frames` of them valid,
        in the text model's space: `(config.tokens(frames), text_dim)`.
        """
        c, w = self.config, self.weights
        x = self.subsample(np.asarray(features, np.float32), frames)
        for layer in w.layers:
            x = self.layer(layer, x)
        x = x[: c.tokens(frames)] @ w.output_proj.weight.T + w.output_proj.bias
        return self.rms_norm(x) @ self.projection.T

    def soft_tokens(self, waveform) -> np.ndarray:
        """The soft tokens of one mono clip at `sample_rate`."""
        return self.tower(*self.features(waveform))


class VisionOracle(Oracle):
    """The vision tower and its projection into the text model's space, and
    Hugging Face's image processor before it.

    Args:
        config: The tower's shape.
        weights: The checkpoint's; the vision tower's tree is read.
    """

    def __init__(self, config: VisionConfig, weights: SimpleNamespace):
        super().__init__(config)
        w = weights.vision_tower
        self.patch, self.position, self.projection, self.layers = widen(
            [
                w.patch_embedder.input_proj.weight,
                w.patch_embedder.position_embedding_table,
                weights.embed_vision.embedding_projection.weight,
                w.encoder.layers,
            ]
        )
        self.angles = rope_angles(
            config.head_dim // 2, config.positions, config.rope_theta
        )

    def patches(self, image: np.ndarray, max_tokens: int):
        """What the image processor hands the tower for `image`: resized as
        torchvision resizes it to the size `config.size` picks, rescaled
        and cut into patches, the `patch` by `patch` pixel squares the tower
        embeds a row each, as a ViT does.

        Args:
            image: `(height, width, 3)` uint8.
            max_tokens: The processor's `max_soft_tokens`: `image_tokens`
                for an image, `video_tokens` for a video frame.

        Returns:
            `pixel_values` `(max_tokens * pool ** 2, 3 * patch ** 2)` float32 in
            [0, 1], each patch's pixels row-major, channels last, padded with
            zero rows; and `positions` `(max_tokens * pool ** 2, 2)` int, each
            patch's (x, y), padded with -1.
        """
        c = self.config
        image = resize(image, *c.size(*image.shape[:2], max_tokens))
        p = c.patch
        height, width, _ = image.shape
        max_patches = max_tokens * c.pool**2
        rows, cols = height // p, width // p
        pixels = image.astype(np.float32) * np.float32(1 / 255)
        pixels = pixels.reshape(rows, p, cols, p, 3).transpose(0, 2, 1, 3, 4)
        values = np.zeros((max_patches, 3 * p * p), np.float32)
        values[: rows * cols] = pixels.reshape(rows * cols, -1)
        positions = np.full((max_patches, 2), -1, np.int64)
        y, x = np.divmod(np.arange(rows * cols), cols)
        positions[: rows * cols] = np.stack([x, y], axis=-1)
        return values, positions

    def windows(self, pixel_values, positions, rows: int):
        """The processor's patches (`patches`) as the NPU's
        `iron.lm.ImagePatches` gives them in `rows` rows: each soft token's
        `pool ** 2` patches together, row-major within their window, the
        tokens row-major over the image, then padding, ids past each
        table.

        Returns:
            `pixels` `(rows, 3 * patch ** 2)` bf16; `xy` `(2 * rows,)` int32,
            each patch's x and y side by side; and `position_ids`
            `(2 * rows,)` int32, every patch's x, then every patch's y plus
            `positions`.
        """
        c, P = self.config, self.config.positions
        real = np.flatnonzero((positions >= 0).all(axis=-1))
        x, y = positions[real].T
        token = x // c.pool + (x.max() + 1) // c.pool * (y // c.pool)
        order = real[np.lexsort((x % c.pool, y % c.pool, token))]
        n = order.size
        x, y = positions[order].T
        pixels = np.zeros((rows, 3 * c.patch**2), bfloat16)
        pixels[:n] = pixel_values[order]
        xy = np.full(2 * rows, P, np.int32)
        xy.reshape(rows, 2)[:n] = np.stack([x, y], axis=-1)
        position_ids = np.full(2 * rows, 2 * P, np.int32)
        position_ids[:n], position_ids[rows : rows + n] = x, P + y
        return pixels, xy, position_ids

    def tower(self, pixel_values, positions) -> np.ndarray:
        """The soft tokens of one image or video frame, `(tokens, text_dim)`,
        from the processor's `pixel_values` and `positions` (`patches`).
        Padding patches reach nothing but themselves, so they are dropped.
        """
        c = self.config
        real = (positions >= 0).all(axis=-1)
        pixels = np.asarray(pixel_values, np.float32)[real]
        x, y = np.asarray(positions)[real].T
        h = (2 * (pixels - np.float32(0.5))) @ self.patch.T
        h = h + self.position[0][x] + self.position[1][y]
        # Each head's first half turned by the patch's x, its second by its y.
        tables = [self.angles[x], self.angles[y]]
        for i, w in enumerate(self.layers):
            h = c.layer(i).oracle(self, w, h, self.attend, tables)
        # Each soft token is the mean of a pool x pool block of patches,
        # numbered row-major over the blocks.
        k = c.pool
        block = x // k + (x.max() + 1) // k * (y // k)
        pooled = np.zeros((block.max() + 1, c.hidden_size), np.float32)
        np.add.at(pooled, block, h)
        pooled *= np.float32(np.sqrt(c.hidden_size) / k**2)
        return self.rms_norm(pooled) @ self.projection.T

    def soft_tokens(self, image, max_tokens: int) -> np.ndarray:
        """The soft tokens of one decoded image or video frame at the
        processor's `max_tokens`.
        """
        return self.tower(*self.patches(image, max_tokens))
