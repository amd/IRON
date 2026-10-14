# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's shape: the text encoder's (``Config``), the audio
tower's (``AudioConfig``) and the vision tower's (``VisionConfig``), as the
checkpoint's ``config.json`` and ``processor_config.json`` give them, named
as ``iron.lm.Config`` names a decoder's, and the largest call each graph is
compiled for. ``PROFILES`` holds every graph's tunables, one profile per
device, and the cost tables ``tune`` measures.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np

PROFILES = Path(__file__).with_name("profiles")


@dataclasses.dataclass(frozen=True)
class Config:
    vocab_size: int = 262144
    emb_dim: int = 512
    n_layers: int = 24
    n_heads: int = 4
    hidden_dim: int = 2048
    # A sliding layer's KV groups, head size and RoPE base; a global layer's
    # are its own.
    n_kv_groups: int = 2
    head_dim: int = 256
    rope_base: float = 10000.0
    global_layers: tuple[int, ...] = (5, 11, 17, 23)
    global_kv_groups: int = 1
    global_head_dim: int = 512
    global_rope_base: float = 1000000.0
    sliding_window: int = 512
    ple_dim: int = 512
    out_dim: int = 768
    # The Matryoshka truncations, each renormalized.
    mrl_dims: tuple[int, ...] = (768, 512, 256, 128)
    eps: float = 1e-6
    bos: int = 2
    eos: int = 1
    pad: int = 0
    # The placeholders an image's or a clip's soft tokens take the place of,
    # and the markers either side of a run of them.
    image_token: int = 258880
    audio_token: int = 258881
    video_token: int = 258884
    boi: int = 255999
    eoi: int = 258882
    boa: int = 256000
    eoa: int = 258883
    # The longest sequence a call takes, soft tokens included.
    max_tokens: int = 2048
    # An MHA query block: the mean over the sequence is one query, a block.
    block: int = 64

    def heads(self, i: int) -> tuple[int, int, float]:
        """Layer ``i``'s KV groups, head size and RoPE base."""
        if i in self.global_layers:
            return self.global_kv_groups, self.global_head_dim, self.global_rope_base
        return self.n_kv_groups, self.head_dim, self.rope_base


@dataclasses.dataclass(frozen=True)
class AudioConfig:
    emb_dim: int = 1024
    n_layers: int = 12
    n_heads: int = 8
    hidden_dim: int = 4096
    mels: int = 128
    # The two subsampling convolutions' output channels.
    channels: tuple[int, int] = (128, 32)
    # A query attends to itself and the `window - 1` positions before it.
    window: int = 12
    # The key columns a query's band spans: its window, then the zeros that
    # make the row a whole Softmax line.
    band: int = 32
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
    # The soft tokens a call takes at most: 30 s of audio gives 750.
    max_tokens: int = 768

    @property
    def head_dim(self) -> int:
        return self.emb_dim // self.n_heads

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

    def timing(self) -> np.ndarray:
        """The `(window, emb_dim)` float32 timing signal of each distance a
        query reaches back: sines, then cosines.
        """
        n = self.emb_dim // 2
        rates = np.exp(np.arange(n) * -(math.log(1e4) / (n - 1))).astype(np.float32)
        angles = np.arange(self.window, dtype=np.float32)[:, None] * rates
        return np.concatenate([np.sin(angles), np.cos(angles)], axis=-1)


@dataclasses.dataclass(frozen=True)
class VisionConfig:
    emb_dim: int = 768
    n_layers: int = 16
    n_heads: int = 12
    head_dim: int = 64
    hidden_dim: int = 3072
    # A patch's side in pixels, and a soft token's side in patches.
    patch: int = 16
    pool: int = 3
    # The rows of each axis's position-embedding table.
    positions: int = 10240
    rope_base: float = 100.0
    text_dim: int = 512
    # The processor's soft-token budgets.
    image_tokens: int = 280
    video_tokens: int = 140
    eps: float = 1e-6
    # The patch rows of a call, an image's budget, and the largest image it
    # takes either way up, 12.6 MP.
    patches: int = 2560
    largest: tuple[int, int] = (3072, 4096)
    # A GEMM's row block at its default tile: the pooled rows are whole blocks.
    rows: int = 256
    # The bytes of an image row Resample receives at a time, and a core's
    # patch columns, as many as its memory holds: 127 across on 16 cores.
    chunk: int = 4096
    patch_columns: int = 8

    def size(self, height: int, width: int, max_tokens: int) -> tuple[int, int]:
        """The `(height, width)` the processor resizes an image to: the
        largest whole `pool * patch` blocks within `max_tokens` soft tokens
        at the image's aspect ratio.

        Args:
            height: The image's height in pixels.
            width: The image's width in pixels.
            max_tokens: The processor's `max_soft_tokens`.

        Returns:
            The resized `(height, width)`.

        Raises:
            ValueError: Both sides round to no block, or the size exceeds
                the budget.
        """
        side = self.pool * self.patch
        max_patches = max_tokens * self.pool**2
        target_px = max_patches * self.patch**2
        factor = math.sqrt(target_px / (height * width))
        out_height = int(math.floor(factor * height / side)) * side
        out_width = int(math.floor(factor * width / side)) * side
        if out_height == 0 and out_width == 0:
            raise ValueError(
                f"a {height}x{width} image rounds to no {side}-pixel block"
            )
        max_side = max_tokens * side
        if out_height == 0:
            out_height = side
            out_width = min(int(math.floor(width / height)) * side, max_side)
        elif out_width == 0:
            out_width = side
            out_height = min(int(math.floor(height / width)) * side, max_side)
        if out_height * out_width > target_px:
            raise ValueError(
                f"resizing {height}x{width} to {out_height}x{out_width} exceeds "
                f"{max_patches} patches"
            )
        return out_height, out_width

    def tokens(self, height: int, width: int, max_tokens: int) -> int:
        """The soft tokens an image of `height` by `width` pixels gives at
        the processor's `max_tokens`.
        """
        out_height, out_width = self.size(height, width, max_tokens)
        return out_height * out_width // (self.pool * self.patch) ** 2
