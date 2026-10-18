#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM's vision tower: a SigLIP ViT (``Idefics3VisionTransformer``) and
its ``Idefics3Connector`` (pixel-shuffle, then a bias-free projection into
the text model's space), an ``iron.lm.Tower`` of ``DecoderLayerSpec``s over
SigLIP's modules (``layer_norm1``/``layer_norm2``, biased attention, a
GELU-tanh ``fc1``/``fc2``).

One 512x512 image, no splitting (``do_image_splitting=False``), resized and
normalized on the host. The patch grid is then whole (32x32), so a patch's
position embedding is its raster index, as the processor's position ids
are for a whole square grid. Nothing rotates (``angles`` None).
"""

import dataclasses
from pathlib import Path

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron.functional as F
from iron import Precision
from iron.functional import LAYER_NORM_EPS
from iron.lm import (
    MLP,
    AttentionSpec,
    Config,
    Conv2d,
    DecoderLayerSpec,
    Norm,
    Tower,
    not_json,
)
from iron.operators.copy import Copy


@dataclasses.dataclass(frozen=True)
class VisionConfig(Config):
    """SmolVLM's vision tower and connector's shape, from the checkpoint's
    ``vision_config``, ``text_config`` and top-level ``scale_factor``.
    """

    hidden_size: int = dataclasses.field(metadata={"json": "vision_config.hidden_size"})
    num_hidden_layers: int = dataclasses.field(
        metadata={"json": "vision_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        metadata={"json": "vision_config.num_attention_heads"}
    )
    intermediate_size: int = dataclasses.field(
        metadata={"json": "vision_config.intermediate_size"}
    )
    patch_size: int = dataclasses.field(metadata={"json": "vision_config.patch_size"})
    image_size: int = dataclasses.field(metadata={"json": "vision_config.image_size"})
    scale_factor: int = dataclasses.field(metadata={"json": "scale_factor"})
    text_dim: int = dataclasses.field(metadata={"json": "text_config.hidden_size"})
    image_token: int = dataclasses.field(metadata={"json": "image_token_id"})
    head_dim: int | None = not_json(None, kw_only=True)
    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "vision_config.layer_norm_eps"}
    )
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh",
        kw_only=True,
        metadata={"json": "vision_config.hidden_act"},
    )

    def __post_init__(self):
        if self.head_dim is None:
            object.__setattr__(
                self, "head_dim", self.hidden_size // self.num_attention_heads
            )

    @property
    def side(self) -> int:
        """The patches along each side of the image."""
        return self.image_size // self.patch_size

    @property
    def tokens(self) -> int:
        """The soft tokens an image gives."""
        return (self.side // self.scale_factor) ** 2

    def layer(self, i: int) -> DecoderLayerSpec:
        H, D = self.num_attention_heads, self.head_dim
        return DecoderLayerSpec(
            AttentionSpec(H, H, D), MLP(self.hidden_act, gated=False), self.norm()
        )

    def norm(self) -> Norm:
        # The kernel's LayerNorm eps, not the checkpoint's layer_norm_eps,
        # which transformers' uses.
        return Norm(LAYER_NORM_EPS, bias=True)


class VisionTower(Tower):
    """The vision tower and connector over one 512x512 image: its 1024
    patches in, its 64 soft tokens in the text model's space out.

    Args:
        config: The tower's shape.
        weights: The checkpoint's tree; ``model.vision_model`` and
            ``model.connector`` are read.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: VisionConfig, weights):
        c = config
        self.vision_model = weights.model.vision_model
        self.connector = weights.model.connector
        super().__init__(c, self.vision_model.encoder.layers, c.side**2, c.tokens)
        self.final_norm = self.vision_model.post_layernorm
        embeddings = self.vision_model.embeddings
        self.patch_embed = Conv2d(
            embeddings.patch_embedding.weight, c.image_size, stride=c.patch_size
        )

    def front(self, rgb):
        """The patches of the image ``rgb`` embedded, with their positions."""
        c, e = self.config, self.vision_model.embeddings
        h = self.patch_embed(rgb, rows=c.side).reshape(c.side**2, c.hidden_size)
        return h + e.patch_embedding.bias + e.position_embedding.weight, None

    renames = {
        "layer_norm1": "input_layernorm",
        "self_attn.out_proj": "self_attn.o_proj",
        "layer_norm2": "post_attention_layernorm",
    }

    def pool(self, x, n):
        c = self.config
        side, scale, rows = c.side, c.scale_factor, c.side // c.scale_factor
        shuffle = TensorAccessPattern(
            (side, side * c.hidden_size),
            0,
            [rows, rows, scale, scale * c.hidden_size],
            [
                scale * side * c.hidden_size,
                scale * c.hidden_size,
                side * c.hidden_size,
                1,
            ],
        )
        return Copy.step(x, src=shuffle).reshape(rows * rows, c.hidden_size * scale**2)

    def head(self, x):
        projection = self.connector.modality_projection.proj.weight
        return F.linear(x, projection, precision=Precision.HIGHEST)

    def body(self, rgb):
        """The soft tokens of the image ``rgb``, ``(512, 512 * 3)``."""
        x, angles = self.front(rgb)
        return self.forward(x, self.max_tokens, angles)

    def soft(self, values: dict) -> int:
        return self.soft_rows

    def shapes(self) -> list[dict]:
        c = self.config
        return [dict(rgb=((c.image_size, c.image_size * 3), bfloat16))]

    def longest(self) -> dict:
        return {}

    def inputs(self, image) -> tuple[np.ndarray, dict]:
        """A call's buffer for ``image``, ``(512, 512, 3)`` float32 in
        ``[-1, 1]`` (the processor's mean and std of 0.5 both ways).
        """
        c = self.config
        return np.asarray(image).astype(bfloat16).reshape(c.image_size, -1), {}
