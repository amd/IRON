# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's vision tower in float32 on the host, the oracle the
NPU tower is judged by, and the image processor's.
"""

from types import SimpleNamespace

import numpy as np

from iron.lm import Oracle, rope_angles
from iron.operators.resample.reference import resize

from ..oracle import EmbeddingGemmaOracle, gelu_tanh, rms_norm
from .model import VisionConfig, size


def patches(image: np.ndarray, max_tokens: int, config: VisionConfig):
    """What the image processor hands the model for `image`: resized as
    torchvision resizes it to the size `size` picks, rescaled and cut into
    patches.

    Args:
        image: `(height, width, 3)` uint8.
        max_tokens: The processor's `max_soft_tokens`: 280 for an image,
            140 for a video frame.
        config: The tower's shape.

    Returns:
        `pixel_values` `(max_tokens * pool ** 2, 3 * patch ** 2)` float32 in
        [0, 1], each patch's pixels row-major, channels last, padded with
        zero rows; and `positions` `(max_tokens * pool ** 2, 2)` int, each
        patch's (x, y), padded with -1.
    """
    image = resize(image, *size(*image.shape[:2], max_tokens, config))
    p = config.patch
    height, width, _ = image.shape
    max_patches = max_tokens * config.pool**2
    rows, cols = height // p, width // p
    pixels = image.astype(np.float32) * np.float32(1 / 255)
    pixels = pixels.reshape(rows, p, cols, p, 3).transpose(0, 2, 1, 3, 4)
    values = np.zeros((max_patches, 3 * p * p), np.float32)
    values[: rows * cols] = pixels.reshape(rows * cols, -1)
    positions = np.full((max_patches, 2), -1, np.int64)
    y, x = np.divmod(np.arange(rows * cols), cols)
    positions[: rows * cols] = np.stack([x, y], axis=-1)
    return values, positions


class VisionOracle:
    """EmbeddingGemma 2's vision tower and its projection into the text
    model's space, in float32 on the host.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
    """

    def __init__(self, config: VisionConfig, weights: SimpleNamespace):
        self.config = config
        self.patch, self.position, self.projection = (
            vars(weights)[k].astype(np.float32)
            for k in ("patch", "position", "projection")
        )
        self.layers = [
            SimpleNamespace(**{k: v.astype(np.float32) for k, v in vars(w).items()})
            for w in weights.layers
        ]
        self.angles = rope_angles(
            config.head_dim // 2, config.positions, config.rope_base
        )

    def layer(self, w: SimpleNamespace, x, x_angles, y_angles):
        """A layer on `x` `(n, hidden)`; each query and key head's first half
        is rotated by the patch's x position (`x_angles`), its second by its y.
        """
        c, n = self.config, x.shape[0]
        H, D = c.n_heads, c.head_dim
        h = rms_norm(x, w.norm1, c.eps)
        q = rms_norm((h @ w.q.T).reshape(n, H, D), w.q_norm, c.eps)
        k = rms_norm((h @ w.k.T).reshape(n, H, D), w.k_norm, c.eps)
        v = rms_norm((h @ w.v.T).reshape(n, H, D), np.float32(1), c.eps)
        q, k = (
            np.concatenate(
                [
                    Oracle.rotate(t[..., : D // 2], x_angles),
                    Oracle.rotate(t[..., D // 2 :], y_angles),
                ],
                axis=-1,
            )
            for t in (q, k)
        )
        a = EmbeddingGemmaOracle.attend(q, k, v, None) @ w.o.T
        x = x + rms_norm(a, w.norm2, c.eps)
        h = rms_norm(x, w.norm3, c.eps)
        f = (gelu_tanh(h @ w.gate.T) * (h @ w.up.T)) @ w.down.T
        return x + rms_norm(f, w.norm4, c.eps)

    def __call__(self, pixel_values, positions) -> np.ndarray:
        """The soft tokens of one image or video frame, `(tokens, text_dim)`,
        from the processor's `pixel_values` and `positions` (see `patches`).
        Padding patches reach nothing but themselves, so they are dropped.
        """
        c = self.config
        real = (positions >= 0).all(axis=-1)
        pixels = np.asarray(pixel_values, np.float32)[real]
        x, y = np.asarray(positions)[real].T
        h = (2 * (pixels - np.float32(0.5))) @ self.patch.T
        h = h + self.position[0][x] + self.position[1][y]
        for w in self.layers:
            h = self.layer(w, h, self.angles[x], self.angles[y])
        # Each soft token is the mean of a pool x pool block of patches,
        # numbered row-major over the blocks.
        k = c.pool
        block = x // k + (x.max() + 1) // k * (y // k)
        pooled = np.zeros((block.max() + 1, c.hidden), np.float32)
        np.add.at(pooled, block, h)
        pooled *= np.float32(np.sqrt(c.hidden) / k**2)
        return rms_norm(pooled, np.float32(1), c.eps) @ self.projection.T
