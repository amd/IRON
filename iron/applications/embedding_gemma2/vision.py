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
from iron.lm import Derived, ImagePatches, Tower, rope_angles
from iron.lm.blocks import ACCURATE
from iron.operators.axpy import AXPY
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.operators.rms_norm import RMSNorm

from .config import PROFILES, VisionConfig


class VisionTower(Tower):
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
    `positions`. Each gather is bounded to the image's patches, so the
    processor's padding ids are never read.

    Args:
        config: The tower's shape.
        weights: The checkpoint's; the vision tower's tree is read.
    """

    profile = PROFILES

    def __init__(self, config: VisionConfig, weights: SimpleNamespace):
        c = config
        tree = self.vision_tower = weights.vision_tower
        self.embed_vision = weights.embed_vision
        window = c.pool**2
        tokens = -(-(c.patches // window) // c.rows) * c.rows
        super().__init__(config, tree.encoder.layers, c.patches, tokens)
        derived = Derived(weights)
        self.processor = ImagePatches(
            c.patches,
            c.largest,
            pool=c.pool,
            positions=c.positions,
            patch_columns=c.patch_columns,
            chunk=c.chunk,
        )
        half = c.head_dim // 2
        quarter = np.arange(half // 2)
        # The x half's first and second quarters, then the y half's.
        order = np.concatenate(
            [quarter, quarter + half, quarter + half // 2, quarter + 3 * half // 2]
        )
        heads = (c.n_heads, c.head_dim, c.emb_dim)
        for layer in tree.encoder.layers:
            a = layer.self_attn
            derived.put(
                a,
                q_reordered=a.q_proj.linear.weight.reshape(heads)[:, order].reshape(
                    c.emb_dim, c.emb_dim
                ),
                k_reordered=a.k_proj.linear.weight.reshape(heads)[:, order].reshape(
                    c.emb_dim, c.emb_dim
                ),
                q_norm_reordered=a.q_norm.weight[order],
                k_norm_reordered=a.k_norm.weight[order],
            )
        self.derived = derived.tree()
        self.rope = iron.weight(
            rope_angles(half, c.positions, c.rope_base).astype(bfloat16)
        )
        self.minus_one = iron.weight(np.full((c.patches, c.emb_dim), -1, bfloat16))
        # Soft token j sums rows j * pool ** 2 onwards; a token past the
        # image's sums none of its rows.
        pool = np.zeros((tokens, c.patches), bfloat16)
        for j in range(c.patches // window):
            pool[j, j * window : (j + 1) * window] = 1
        self.pooling = iron.weight(pool)

    def front(self, rgb, *, n, height, width, out_height, out_width):
        """The rows of the image ``rgb``'s ``n`` patches, ``height`` by
        ``width`` pixels resized to ``out_height`` by ``out_width``, with
        their position embeddings, and each patch's angles.
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
        v, d = self.vision_tower, self.derived.vision_tower
        x = AXPY.step(pixels[:n], self.minus_one[:n], scalar_factor=2.0)
        patch = v.patch_embedder.input_proj.weight
        h = GEMM.step(x, patch, b_col_maj=True, **ACCURATE)
        table = v.patch_embedder.position_embedding_table.reshape(-1, c.emb_dim)
        ids = position_ids.reshape(2, T)
        x_side = Copy.step(iron.weight(table)[ids[0, :n]])
        y_side = Copy.step(iron.weight(table)[ids[1, :n]])
        h = ElementwiseAdd.step(ElementwiseAdd.step(h, x_side), y_side)
        angles = Copy.step(self.rope[xy[: 2 * n]]).reshape(T, c.head_dim)
        return h, angles

    def layer(self, step, i, w, x):
        a = self.derived.vision_tower.encoder.layers[i].self_attn
        # q and k reordered, until RoPE turns each half of a head itself.
        reordered = {
            "q_proj": SimpleNamespace(weight=a.q_reordered),
            "k_proj": SimpleNamespace(weight=a.k_reordered),
            "q_norm": SimpleNamespace(weight=a.q_norm_reordered),
            "k_norm": SimpleNamespace(weight=a.k_norm_reordered),
        }
        self_attn = SimpleNamespace(**{**vars(w.self_attn), **reordered})
        w = SimpleNamespace(**{**vars(w), "self_attn": self_attn})
        attend = partial(self.attend, step, i)
        return self.config.layer(i).step(w, x, attend, step.angles)

    def pool(self, x, n):
        return GEMM.step(self.pooling[:, :n], x, **ACCURATE)

    def head(self, x):
        c = self.config
        # The mean's 1 / pool ** 2 and the sqrt(emb_dim) scale folded into
        # the norm's epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        s2 = c.emb_dim / c.pool**4
        x = RMSNorm.step(x, epsilon=c.eps / s2)
        projection = self.embed_vision.embedding_projection.weight
        return GEMM.step(x, projection, b_col_maj=True, **ACCURATE)

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
        x, angles = self.front(
            rgb,
            n=n,
            height=height,
            width=width,
            out_height=out_height,
            out_width=out_width,
        )
        return self.forward(x, n, angles)

    def soft(self, values: dict) -> int:
        return values["n"] // self.config.pool**2

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
