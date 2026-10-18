#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM's vision tower: a SigLIP ViT (``Idefics3VisionTransformer``) and
its ``Idefics3Connector`` (pixel-shuffle, then a bias-free projection into
the text model's space), an ``iron.lm.Tower`` of ``DecoderLayer``s over
SigLIP's modules (``layer_norm1``/``layer_norm2``, biased attention, a
GELU-tanh ``fc1``/``fc2``).

One 512x512 image, no splitting (``do_image_splitting=False``), resized and
normalized on the host. The patch grid is then whole (32x32), so a patch's
position embedding is its raster index, as the processor's position ids
are for a whole square grid. Nothing rotates (``angles`` None).
"""

import dataclasses
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron.functional as F
from iron.functional import ACCURATE, LAYER_NORM_EPS
from iron.lm import MLP, Attention, Config, Conv2d, DecoderLayer, Norm, Tower
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd
from iron.operators.gemm import GEMM


@dataclasses.dataclass(frozen=True)
class VisionConfig(Config):
    """SmolVLM's vision tower and connector's shape, from the checkpoint's
    ``vision_config``, ``text_config`` and top-level ``scale_factor``.
    """

    hidden: int = dataclasses.field(metadata={"json": "vision_config.hidden_size"})
    num_hidden_layers: int = dataclasses.field(
        metadata={"json": "vision_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        metadata={"json": "vision_config.num_attention_heads"}
    )
    intermediate_size: int = dataclasses.field(
        metadata={"json": "vision_config.intermediate_size"}
    )
    patch: int = dataclasses.field(metadata={"json": "vision_config.patch_size"})
    image_size: int = dataclasses.field(metadata={"json": "vision_config.image_size"})
    scale_factor: int = dataclasses.field(metadata={"json": "scale_factor"})
    text_dim: int = dataclasses.field(metadata={"json": "text_config.hidden_size"})
    image_token: int = dataclasses.field(metadata={"json": "image_token_id"})
    head_dim: int | None = dataclasses.field(default=None, kw_only=True)
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
                self, "head_dim", self.hidden // self.num_attention_heads
            )

    @property
    def side(self) -> int:
        """The patches along each side of the image."""
        return self.image_size // self.patch

    @property
    def tokens(self) -> int:
        """The soft tokens an image gives."""
        return (self.side // self.scale_factor) ** 2

    def layer(self, i: int) -> DecoderLayer:
        # TODO(pin group): LayerNorm at the checkpoint's eps (layer_norm_eps)
        # once the pin carries the kernel option; transformers' uses it now.
        H, D = self.num_attention_heads, self.head_dim
        return DecoderLayer(
            Attention(H, H, D),
            MLP(self.hidden_act, gated=False),
            Norm(LAYER_NORM_EPS, bias=True),
        )


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
        embeddings = self.vision_model.embeddings
        self.patch_embed = Conv2d(
            embeddings.patch_embedding.weight, c.image_size, stride=c.patch
        )

    def front(self, rgb):
        """The patches of the image ``rgb`` embedded, with their positions."""
        c, e = self.config, self.vision_model.embeddings
        h = self.patch_embed(rgb, rows=c.side).reshape(c.side**2, c.hidden)
        h = RowwiseAdd.step(h, e.patch_embedding.bias)
        return ElementwiseAdd.step(h, e.position_embedding.weight), None

    def sanitize(self, w):
        a = w.self_attn
        return SimpleNamespace(
            input_layernorm=w.layer_norm1,
            self_attn=SimpleNamespace(
                q_proj=a.q_proj, k_proj=a.k_proj, v_proj=a.v_proj, o_proj=a.out_proj
            ),
            post_attention_layernorm=w.layer_norm2,
            mlp=w.mlp,
        )

    def norm(self, x):
        n = self.vision_model.post_layernorm
        return F.layer_norm(x, n.weight, n.bias, LAYER_NORM_EPS)

    def pool(self, x, n):
        c = self.config
        side, scale, rows = c.side, c.scale_factor, c.side // c.scale_factor
        shuffle = TensorAccessPattern(
            (side, side * c.hidden),
            0,
            [rows, rows, scale, scale * c.hidden],
            [scale * side * c.hidden, scale * c.hidden, side * c.hidden, 1],
        )
        return Copy.step(x, src=shuffle).reshape(rows * rows, c.hidden * scale**2)

    def head(self, x):
        projection = self.connector.modality_projection.proj.weight
        return GEMM.step(x, projection, b_col_maj=True, **ACCURATE)

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
