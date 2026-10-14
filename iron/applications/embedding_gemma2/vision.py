# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's vision tower on the NPU: the image processor's resize
into patches, the tower and its projection into the text model's space, as
one graph.
"""

from functools import partial
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.lm import ImagePatches, Model, attention, rope_angles, sandwich_layer
from iron.lm.blocks import ACCURATE
from iron.operators.axpy import AXPY
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.operators.rms_norm import RMSNorm

from .config import PROFILES, VisionConfig


class VisionTower(Model):
    """The vision tower and `embed_vision` over at most `patches` patches,
    one compile for every image; called in another graph's body, its steps
    are that graph's.

    A call takes a decoded image, which `processor` (`iron.lm.ImagePatches`)
    resizes as Hugging Face's image processor does and cuts into patches,
    the 16x16-pixel squares the tower embeds a row each, in pooling-window
    order on the NPU, so pooling is a fixed sum of row blocks, a GEMM by a
    0/1 matrix. `n`, the real patches, bounds every operator after the
    processor, the pooling's sum among them. Each head's channels are
    reordered so that the axial RoPE, x on its first half and y on its
    second, is one rotation of halves: a permutation within a head changes
    neither its norm nor a query's product with a key.

    The rows a call looks up by patch position are gathered on the NPU: the
    RoPE angles by `xy`, each patch's x and y side by side, so a patch's row
    is x's angles then y's; the position embeddings by `position_ids` from
    x's table and y's as one, every patch's x, then every patch's y plus
    `positions`. Padding looks up each table's last row, zero.

    Args:
        config: The tower's shape.
        weights: The checkpoint's; the vision tower's tree is read.
    """

    profile = PROFILES

    def __init__(self, config: VisionConfig, weights: SimpleNamespace):
        c = config
        tree = weights.vision_tower
        self.config = config
        self.processor = ImagePatches(
            c.patches,
            c.largest,
            pool=c.pool,
            positions=c.positions,
            patch_columns=c.patch_columns,
            chunk=c.chunk,
        )
        self.patch = tree.patch_embedder.input_proj.weight
        position = np.zeros((2 * c.positions + 1, c.emb_dim), bfloat16)
        table = tree.patch_embedder.position_embedding_table
        position[:-1] = table.reshape(-1, c.emb_dim)
        self.position = iron.weight(position)
        self.projection = weights.embed_vision.embedding_projection.weight
        half = c.head_dim // 2
        quarter = np.arange(half // 2)
        # The x half's first and second quarters, then the y half's.
        order = np.concatenate(
            [quarter, quarter + half, quarter + half // 2, quarter + 3 * half // 2]
        )
        self.layers = tree.encoder.layers
        # Each layer's query and key weights, each head's channels in `order`.
        self.reordered = [
            SimpleNamespace(
                q_proj=w.self_attn.q_proj.linear.weight.reshape(
                    c.n_heads, c.head_dim, c.emb_dim
                )[:, order].reshape(c.emb_dim, c.emb_dim),
                k_proj=w.self_attn.k_proj.linear.weight.reshape(
                    c.n_heads, c.head_dim, c.emb_dim
                )[:, order].reshape(c.emb_dim, c.emb_dim),
                q_norm=w.self_attn.q_norm.weight[order],
                k_norm=w.self_attn.k_norm.weight[order],
            )
            for w in self.layers
        ]
        angles = np.zeros((c.positions + 1, half), bfloat16)
        angles[:-1] = rope_angles(half, c.positions, c.rope_base)
        self.angles = iron.weight(angles)
        self.minus_one = iron.weight(np.full((c.patches, c.emb_dim), -1, bfloat16))
        # Soft token j sums rows j * pool ** 2 onwards; a token past the
        # image's sums none of its rows.
        window = c.pool**2
        tokens = -(-(c.patches // window) // c.rows) * c.rows
        pool = np.zeros((tokens, c.patches), bfloat16)
        for j in range(c.patches // window):
            pool[j, j * window : (j + 1) * window] = 1
        self.pool = iron.weight(pool)

    def body(
        self,
        rgb,
        *,
        n: Scratchpad[np.int32],
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        """The `(tokens, text_dim)` soft tokens of the image `rgb`, `height`
        by `width` pixels resized to `out_height` by `out_width`, its `n`
        patches, `tokens` `patches // pool ** 2` rounded up to whole `rows`;
        the first `n // pool ** 2` are the image's, the rest zero.
        """
        c = self.config
        pixels, xy, position_ids = self.processor(
            rgb,
            height=height,
            width=width,
            out_height=out_height,
            out_width=out_width,
        )
        T = pixels.shape[0]
        x = AXPY(pixels[:n], self.minus_one[:n], scalar_factor=2.0)
        h = GEMM(x, self.patch, b_col_maj=True, **ACCURATE)
        position = Copy(self.position[position_ids]).reshape(2, T, c.emb_dim)
        h = ElementwiseAdd(ElementwiseAdd(h, position[0, :n]), position[1, :n])
        angles = Copy(self.angles[xy]).reshape(T, c.head_dim)[:n]
        for w, r in zip(self.layers, self.reordered):
            attend = partial(
                attention,
                angles=angles,
                q_proj=r.q_proj,
                k_proj=r.k_proj,
                v_proj=w.self_attn.v_proj.linear.weight,
                o_proj=w.self_attn.o_proj.linear.weight,
                q_norm=r.q_norm,
                k_norm=r.k_norm,
                heads=c.n_heads,
                groups=c.n_heads,
                head_dim=c.head_dim,
                epsilon=c.eps,
                **ACCURATE,
            )
            h = sandwich_layer(
                h,
                attend,
                norms=(
                    w.input_layernorm.weight,
                    w.post_attention_layernorm.weight,
                    w.pre_feedforward_layernorm.weight,
                    w.post_feedforward_layernorm.weight,
                ),
                gate=w.mlp.gate_proj.linear.weight,
                up=w.mlp.up_proj.linear.weight,
                down=w.mlp.down_proj.linear.weight,
                epsilon=c.eps,
                **ACCURATE,
            )
        pooled = GEMM(self.pool[:, :n], h, **ACCURATE)
        # The mean's 1 / pool ** 2 and the sqrt(emb_dim) scale folded into
        # the norm's epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        s2 = c.emb_dim / c.pool**4
        pooled = RMSNorm(pooled, epsilon=c.eps / s2)
        return GEMM(pooled, self.projection, b_col_maj=True, **ACCURATE)

    # -- on the host -----------------------------------------------------------

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, the largest image's."""
        chunks = self.processor.resample.image_chunks
        return [dict(rgb=((chunks, self.config.chunk), np.uint8))]

    def longest(self) -> dict:
        """The per-call values of the largest image, its patches filled."""
        c = self.config
        _, values = self.inputs(
            np.zeros((*c.largest, 3), np.uint8), c.patches // c.pool**2
        )
        return values

    def inputs(self, image, max_tokens: int) -> tuple[np.ndarray, dict]:
        """A call's image buffer and per-call sizes, `n` (its patches) among
        them, for a decoded `image` at the processor's `max_tokens`.

        Args:
            image: `(height, width, 3)` uint8.
            max_tokens: The processor's `max_soft_tokens`.

        Raises:
            ValueError: The image or its patches do not fit a call, or
                `Resample` cannot resize it.
        """
        c = self.config
        out_height, out_width = c.size(*np.shape(image)[:2], max_tokens)
        rgb, values = self.processor.pack(image, out_height, out_width)
        return rgb, dict(n=out_height // c.patch * (out_width // c.patch), **values)

    def embed(self, image, max_tokens: int) -> np.ndarray:
        """The soft tokens of one decoded image or video frame,
        `(tokens, text_dim)` float32, in the text model's space.

        Args:
            image: `(height, width, 3)` uint8.
            max_tokens: The processor's `max_soft_tokens`: `image_tokens`
                for an image, `video_tokens` for a frame.
        """
        c = self.config
        rgb, values = self.inputs(image, max_tokens)
        tokens = self(rgb, **values).numpy().reshape(-1, c.text_dim)
        return np.asarray(tokens[: values["n"] // c.pool**2], np.float32)
