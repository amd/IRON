# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's vision tower on the NPU: the image processor's resize into
patches, the tower and its projection into the text model's space, as one
graph: Hugging Face's ``Gemma4VisionModel`` and ``embed_vision``, its shape
``VisionConfig``.
"""

import dataclasses
import math
from types import SimpleNamespace

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, Scratchpad, lm
from iron.lm import Attention, ImagePatches, NoCache, SandwichLayer, Tower, rope_angles
from iron.operators.axpy import AXPY
from iron.operators.gemm import GEMM


@dataclasses.dataclass(frozen=True)
class VisionConfig(lm.Config):
    # Every projection at HIGHEST (``Attention``, ``GatedMLP``).
    precision = Precision.HIGHEST
    json_prefix = "vision_config."

    hidden_size: int = 768
    num_hidden_layers: int = 16
    num_attention_heads: int = 12
    head_dim: int = 64
    intermediate_size: int = 3072
    # A patch's side in pixels, and a soft token's side in patches.
    patch_size: int = 16
    pooling_kernel_size: int = 3
    # The rows of each axis's position-embedding table.
    position_embedding_size: int = 10240
    rope_theta: float = dataclasses.field(
        default=100.0, metadata={"json": "rope_parameters.rope_theta"}
    )
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh", metadata={"json": "hidden_activation"}
    )
    text_dim: int = dataclasses.field(
        default=512, metadata={"json": "/text_config.hidden_size"}
    )
    # The processor's soft-token budget.
    image_tokens: int = dataclasses.field(
        default=280, metadata={"json": "/vision_soft_tokens_per_image"}
    )
    # The patch rows of a call, an image's budget, and the largest image it
    # takes either way up, 12.6 MP.
    patches: int = lm.not_json(2560)
    largest: tuple[int, int] = lm.not_json((3072, 4096))
    # A GEMM's row block at its default tile: the pooled rows are whole blocks.
    rows: int = lm.not_json(256)
    # The bytes of an image row Resample receives at a time, and a core's
    # patch columns, as many as its memory holds: 127 across on 16 cores.
    chunk: int = lm.not_json(4096)
    patch_columns: int = lm.not_json(8)

    @property
    def num_key_value_heads(self) -> int:
        return self.num_attention_heads

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
        side = self.pooling_kernel_size * self.patch_size
        max_patches = max_tokens * self.pooling_kernel_size**2
        target_px = max_patches * self.patch_size**2
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
        return (
            out_height * out_width // (self.pooling_kernel_size * self.patch_size) ** 2
        )


class VisionLayer(SandwichLayer):
    """Layer ``i``: unscaled attention over RMS-normed q, k and v, each
    head's channels of q and k reordered as they load, so that the axial
    RoPE turns halves rather than each half of a head.
    """

    def __init__(self, c: VisionConfig, i: int):
        super().__init__(c, i, Attention(c, i, norms="qkv"), cache=NoCache())
        self.self_attn.scaling = 1.0
        self.rope = c.head_dim

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        a = self.self_attn
        half, E = a.head_dim // 2, a.q_proj.in_features
        quarter = np.arange(half // 2)
        # The x half's first and second quarters, then the y half's.
        order = np.concatenate(
            [quarter, quarter + half, quarter + half // 2, quarter + 3 * half // 2]
        )
        for p in (a.q_proj, a.k_proj):
            w = p.weight.reshape(a.heads, a.head_dim, E)[:, order]
            p.weight = iron.param(w.reshape(E, E))
        for norm in (a.q_norm, a.k_norm):
            norm.weight = iron.param(norm.weight[order])


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

    The rows a call looks up by patch position, x's and y's position
    embeddings and RoPE angles, are copied from tables of whole windows in
    the same order: a window's x blocks by window column, its y blocks by
    window row, repeated across the widest image that reaches the row. A
    descriptor walks 64 window rows at most, so each copy walks `groups` in
    turn, each its rows of the image or, past them, one more into rows no
    later step reads.

    Args:
        config: The tower's shape.
        weights: The checkpoint's; the vision tower's tree is read.
    """

    layer_class = VisionLayer

    def __init__(self, config: VisionConfig, weights: SimpleNamespace):
        c = config
        tree = self.vision_tower = weights.vision_tower
        self.embed_vision = weights.embed_vision
        window = c.pooling_kernel_size**2
        tokens = -(-(c.patches // window) // c.rows) * c.rows
        super().__init__(config, c.patches, tokens)
        self.load_layers(weights, "vision_tower.encoder.layers.")
        self.processor = ImagePatches(
            c.patches,
            c.largest,
            pool=c.pooling_kernel_size,
            positions=c.position_embedding_size,
            patch_columns=c.patch_columns,
            chunk=c.chunk,
        )
        half = c.head_dim // 2
        k, windows, across = (
            c.pooling_kernel_size,
            c.patches // window,
            self.processor.across,
        )
        # Window rows in groups a descriptor walks, at most 64, doubling from
        # 8 so each group's y blocks are about as wide as the widest image
        # that reaches it: `pitch` blocks a window row from block `base`.
        self.groups, blocks, first = [], [], 0
        while first < windows:
            rows = min(64, max(8, first), windows - first)
            pitch = min(across, windows // (first + 1))
            self.groups.append((first, rows, pitch, len(blocks)))
            blocks += [first + r for r in range(rows) for _ in range(pitch)]
            first += rows
        # A walk past the image reads `across` blocks from its group's first row.
        last = max(
            base + (rows - 1) * pitch + across for _, rows, pitch, base in self.groups
        )
        blocks += [0] * (last - len(blocks))
        x_ids = [
            k * tx + wx for tx in range(across) for _ in range(k) for wx in range(k)
        ]
        y_ids = [k * ty + wy for ty in blocks for wy in range(k) for _ in range(k)]
        table = tree.patch_embedder.position_embedding_table
        self.x_windows, self.y_windows = table[0][x_ids], table[1][y_ids]
        rope = rope_angles(half, c.position_embedding_size, c.rope_theta).astype(
            bfloat16
        )
        self.x_angles, self.y_angles = iron.param(rope[x_ids]), iron.param(rope[y_ids])
        self.capacity = max(
            self.walked(hk, wk)
            for hk in range(1, windows + 1)
            for wk in range(1, min(across, windows // hk) + 1)
        )
        # What the walks write, past `patches` rows of the image's windows.
        self.window_rows = iron.state((self.capacity, c.hidden_size))
        self.angle_rows = iron.state((self.capacity, c.head_dim))
        self.minus_one = iron.weight(np.full((c.patches, c.hidden_size), -1, bfloat16))
        # Soft token j sums rows j * pool ** 2 onwards; a token past the
        # image's sums none of its rows.
        pool = np.zeros((tokens, c.patches), bfloat16)
        for j in range(c.patches // window):
            pool[j, j * window : (j + 1) * window] = 1
        self.pooling = iron.weight(pool)

    def window_positions(self, h, *, n, hk, wk, walked):
        """``h`` plus each patch's x and y position embeddings, and its
        angles by head size (``Call.ropes``), for an image of ``hk`` by
        ``wk`` windows, ``n`` patches.
        """
        c = self.config
        T = c.patches
        repeat = tuple(
            iron.clamp(hk - first, lo=1, hi=rows) for first, rows, *_ in self.groups
        )
        sides = self.x_windows, self.y_windows
        for table, x_side in zip(sides, (True, False)):
            walk = self.walk(table, x_side, repeat=repeat, wk=wk, walked=walked)
            self.window_rows[:walked] = walk
            side = TensorAccessPattern.full(self.window_rows.shape)[:T]
            side = self.window_rows.at(side, (T, c.hidden_size), bounds={0: n})
            h = h + side
        half = c.head_dim // 2
        for table, x_side, cut in (
            (self.x_angles, True, slice(None, half)),
            (self.y_angles, False, slice(half, None)),
        ):
            walk = self.walk(table, x_side, repeat=repeat, wk=wk, walked=walked)
            self.angle_rows[:walked, cut] = walk
        angles = TensorAccessPattern.full(self.angle_rows.shape)[:T]
        angles = self.angle_rows.at(angles, (T, c.head_dim), bounds={0: n})
        return h, {c.head_dim: (angles, angles)}

    def walk(self, table, x_side: bool, *, repeat, wk, walked):
        """The window blocks of ``table``, x's by window column or y's by
        window row, each group's ``repeat`` window rows of ``wk`` in turn.
        """
        k, across = self.config.pooling_kernel_size, self.processor.across
        width = table.shape[1]
        block = k * k * width
        return iron.weight(table).at(
            tuple(
                TensorAccessPattern(
                    table.shape,
                    0 if x_side else base * block,
                    [rows, across, k * k, width],
                    [0 if x_side else pitch * block, block, width, 1],
                )
                for _, rows, pitch, base in self.groups
            ),
            (self.capacity, width),
            bounds={0: walked},
            repeat=repeat,
            length=wk,
        )

    renames = {
        f"{module}.{p}_proj.linear": f"{module}.{p}_proj"
        for module, ps in (("self_attn", "qkvo"), ("mlp", ("gate", "up", "down")))
        for p in ps
    }

    def pool(self, x, n):
        return GEMM.step(self.pooling[:, :n], x, precision=self.config.precision)

    def head(self, x):
        c = self.config
        # The mean's 1 / pool ** 2 and the sqrt(hidden_size) scale folded into
        # the norm's epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        s2 = c.hidden_size / c.pooling_kernel_size**4
        x = F.rms_norm(x, x.shape[-1:], eps=c.eps / s2)
        projection = self.embed_vision.embedding_projection.weight
        return F.linear(x, projection, precision=c.precision)

    def body(
        self,
        rgb,
        *,
        n: Scratchpad[np.int32],
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
        hk: Scratchpad[np.int32],
        wk: Scratchpad[np.int32],
        walked: Scratchpad[np.int32],
    ):
        """The `(tokens, text_dim)` soft tokens of the image `rgb`, `height`
        by `width` pixels resized to `out_height` by `out_width`, its `n`
        patches in `hk` by `wk` windows, `tokens` `patches // pool ** 2`
        rounded up to whole `rows`; the first `n // pool ** 2` are the
        image's, the rest zero. `walked` is the rows its windows' walks move.
        """
        pixels, _, _ = self.processor(
            rgb,
            height=height,
            width=width,
            out_height=out_height,
            out_width=out_width,
        )
        x = AXPY.step(pixels[:n], self.minus_one[:n], scalar_factor=2.0)
        patch = self.vision_tower.patch_embedder.input_proj.weight
        h = F.linear(x, patch, precision=self.config.precision)
        h, angles = self.window_positions(h, n=n, hk=hk, wk=wk, walked=walked)
        return self.forward(h, n, angles)

    def soft(self, values: dict) -> int:
        return values["n"] // self.config.pooling_kernel_size**2

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, the largest image's."""
        chunks = self.processor.resample.image_chunks
        return [dict(rgb=((chunks, self.config.chunk), np.uint8))]

    def longest(self) -> dict:
        """The per-call values of the largest image, its patches filled."""
        c = self.config
        _, values = self.inputs(
            np.zeros((*c.largest, 3), np.uint8), c.patches // c.pooling_kernel_size**2
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
        side = c.pooling_kernel_size * c.patch_size
        hk, wk = out_height // side, out_width // side
        return rgb, dict(
            n=out_height // c.patch_size * (out_width // c.patch_size),
            hk=hk,
            wk=wk,
            walked=self.walked(hk, wk),
            **values,
        )

    def walked(self, hk: int, wk: int) -> int:
        """The rows the window walks move for an image of `hk` by `wk`
        windows: each group's window rows of it, or past it one.
        """
        rows = sum(max(1, min(hk - first, r)) for first, r, *_ in self.groups)
        return self.config.pooling_kernel_size**2 * wk * rows
