# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's shape: the text encoder's (``Config``), the audio
tower's (``AudioConfig``) and the vision tower's (``VisionConfig``), as the
checkpoint's ``config.json`` and ``processor_config.json`` give them, named
as ``iron.lm.Config`` names a decoder's, and the largest call each graph is
compiled for. ``PROFILES`` holds every graph's tunables, one profile per
device, as ``iron.lm.tune`` writes them.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np

from iron import lm

from .blocks import SandwichLayer, TextLayer

PROFILES = Path(__file__).with_name("profiles")


def _global_layers(layer_types: list[str]) -> tuple[int, ...]:
    return tuple(i for i, kind in enumerate(layer_types) if kind == "full_attention")


@dataclasses.dataclass(frozen=True)
class Config(lm.Config):
    vocab_size: int = dataclasses.field(
        default=262144, metadata={"json": "text_config.vocab_size"}
    )
    hidden_size: int = dataclasses.field(
        default=512, metadata={"json": "text_config.hidden_size"}
    )
    num_hidden_layers: int = dataclasses.field(
        default=24, metadata={"json": "text_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        default=4, metadata={"json": "text_config.num_attention_heads"}
    )
    intermediate_size: int = dataclasses.field(
        default=2048, metadata={"json": "text_config.intermediate_size"}
    )
    # A sliding layer's KV groups, head size and RoPE base; a global layer's
    # are its own.
    num_key_value_heads: int = dataclasses.field(
        default=2, metadata={"json": "text_config.num_key_value_heads"}
    )
    head_dim: int = dataclasses.field(
        default=256, metadata={"json": "text_config.head_dim"}
    )
    rope_theta: float = dataclasses.field(
        default=10000.0,
        metadata={"json": "text_config.rope_parameters.sliding_attention.rope_theta"},
    )
    global_layers: tuple[int, ...] = dataclasses.field(
        default=(5, 11, 17, 23),
        metadata={"json": "text_config.layer_types", "convert": _global_layers},
    )
    global_kv_groups: int = dataclasses.field(
        default=1,
        metadata={"json": "text_config.per_layer_config.05.num_key_value_heads"},
    )
    global_head_dim: int = dataclasses.field(
        default=512, metadata={"json": "text_config.per_layer_config.05.head_dim"}
    )
    global_rope_base: float = dataclasses.field(
        default=1000000.0,
        metadata={"json": "text_config.rope_parameters.full_attention.rope_theta"},
    )
    sliding_window: int = dataclasses.field(
        default=512, metadata={"json": "text_config.sliding_window"}
    )
    ple_dim: int = dataclasses.field(
        default=512, metadata={"json": "text_config.hidden_size_per_layer_input"}
    )
    out_dim: int = dataclasses.field(
        default=768, metadata={"json": "text_config.embedding_dim"}
    )
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh",
        metadata={"json": "text_config.hidden_activation"},
    )
    # The Matryoshka truncations, each renormalized.
    mrl_dims: tuple[int, ...] = (768, 512, 256, 128)
    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "text_config.rms_norm_eps"}
    )
    bos: int = dataclasses.field(
        default=2, metadata={"json": "text_config.bos_token_id"}
    )
    eos: int = dataclasses.field(
        default=1, metadata={"json": "text_config.eos_token_id"}
    )
    pad: int = dataclasses.field(
        default=0, metadata={"json": "text_config.pad_token_id"}
    )
    # The placeholders an image's or a clip's soft tokens take the place of,
    # and the markers either side of a run of them.
    image_token: int = dataclasses.field(
        default=258880, metadata={"json": "image_token_id"}
    )
    audio_token: int = dataclasses.field(
        default=258881, metadata={"json": "audio_token_id"}
    )
    video_token: int = dataclasses.field(
        default=258884, metadata={"json": "video_token_id"}
    )
    boi: int = dataclasses.field(default=255999, metadata={"json": "boi_token_id"})
    eoi: int = dataclasses.field(default=258882, metadata={"json": "eoi_token_id"})
    boa: int = dataclasses.field(default=256000, metadata={"json": "boa_token_id"})
    # Hugging Face's own config.json spells this one an "index", unlike every
    # other marker's "id".
    eoa: int = dataclasses.field(default=258883, metadata={"json": "eoa_token_index"})
    # The longest sequence a call takes, soft tokens included.
    max_tokens: int = 2048
    # An MHA query block: the mean over the sequence is one query, a block.
    block: int = 64

    def heads(self, i: int) -> tuple[int, int, float]:
        """Layer ``i``'s KV groups, head size and RoPE base."""
        if i in self.global_layers:
            return self.global_kv_groups, self.global_head_dim, self.global_rope_base
        return self.num_key_value_heads, self.head_dim, self.rope_theta

    def layer(self, i: int) -> TextLayer:
        """Layer ``i``: unscaled attention over RMS-normed values, a sliding
        layer's within ``sliding_window`` positions.
        """
        G, D, _ = self.heads(i)
        window = None if i in self.global_layers else self.sliding_window
        return TextLayer(
            lm.Attention(
                self.num_attention_heads,
                G,
                D,
                self.eps,
                qk_norm=True,
                v_norm=True,
                scale=1.0,
                window=window,
                accurate=True,
            ),
            lm.MLP(self.hidden_act, accurate=True),
            lm.Norm(self.eps),
        )


@dataclasses.dataclass(frozen=True)
class AudioConfig(lm.Config):
    hidden_size: int = dataclasses.field(
        default=1024, metadata={"json": "audio_config.hidden_size"}
    )
    num_hidden_layers: int = dataclasses.field(
        default=12, metadata={"json": "audio_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        default=8, metadata={"json": "audio_config.num_attention_heads"}
    )
    intermediate_size: int = 4096
    mels: int = 128
    # The two subsampling convolutions' output channels.
    channels: tuple[int, int] = dataclasses.field(
        default=(128, 32),
        metadata={
            "json": "audio_config.subsampling_conv_channels",
            "convert": tuple,
        },
    )
    # A query attends to itself and the `window - 1` positions before it.
    window: int = 12
    # The key columns a query's band spans: its window, then the zeros that
    # make the row a whole Softmax line.
    band: int = 32
    logit_cap: float = dataclasses.field(
        default=50.0, metadata={"json": "audio_config.attention_logit_cap"}
    )
    conv_kernel: int = dataclasses.field(
        default=5, metadata={"json": "audio_config.conv_kernel_size"}
    )
    residual_weight: float = dataclasses.field(
        default=0.5, metadata={"json": "audio_config.residual_weight"}
    )
    output_dim: int = dataclasses.field(
        default=1536, metadata={"json": "audio_config.output_proj_dims"}
    )
    text_dim: int = 512
    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "audio_config.rms_norm_eps"}
    )
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
        return self.hidden_size // self.num_attention_heads

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
        """The `(window, hidden_size)` float32 timing signal of each distance a
        query reaches back: sines, then cosines.
        """
        n = self.hidden_size // 2
        rates = np.exp(np.arange(n) * -(math.log(1e4) / (n - 1))).astype(np.float32)
        angles = np.arange(self.window, dtype=np.float32)[:, None] * rates
        return np.concatenate([np.sin(angles), np.cos(angles)], axis=-1)


@dataclasses.dataclass(frozen=True)
class VisionConfig(lm.Config):
    hidden_size: int = dataclasses.field(
        default=768, metadata={"json": "vision_config.hidden_size"}
    )
    num_hidden_layers: int = dataclasses.field(
        default=16, metadata={"json": "vision_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        default=12, metadata={"json": "vision_config.num_attention_heads"}
    )
    head_dim: int = dataclasses.field(
        default=64, metadata={"json": "vision_config.head_dim"}
    )
    intermediate_size: int = dataclasses.field(
        default=3072, metadata={"json": "vision_config.intermediate_size"}
    )
    # A patch's side in pixels, and a soft token's side in patches.
    patch: int = dataclasses.field(
        default=16, metadata={"json": "vision_config.patch_size"}
    )
    pool: int = dataclasses.field(
        default=3, metadata={"json": "vision_config.pooling_kernel_size"}
    )
    # The rows of each axis's position-embedding table.
    positions: int = dataclasses.field(
        default=10240, metadata={"json": "vision_config.position_embedding_size"}
    )
    rope_theta: float = dataclasses.field(
        default=100.0, metadata={"json": "vision_config.rope_parameters.rope_theta"}
    )
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh",
        metadata={"json": "vision_config.hidden_activation"},
    )
    text_dim: int = 512
    # The processor's soft-token budgets.
    image_tokens: int = dataclasses.field(
        default=280, metadata={"json": "vision_soft_tokens_per_image"}
    )
    video_tokens: int = 140
    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "vision_config.rms_norm_eps"}
    )
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

    def layer(self, i: int) -> SandwichLayer:
        """Layer ``i``: unscaled attention over RMS-normed values."""
        H = self.num_attention_heads
        return SandwichLayer(
            lm.Attention(
                H,
                H,
                self.head_dim,
                self.eps,
                qk_norm=True,
                v_norm=True,
                scale=1.0,
                accurate=True,
            ),
            lm.MLP(self.hidden_act, accurate=True),
            lm.Norm(self.eps),
        )

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
