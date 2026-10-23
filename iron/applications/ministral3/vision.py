# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3's vision tower on the NPU: Pixtral's ViT and Mistral 3's
projector over one decoded image of any size, as one graph (Hugging
Face's ``PixtralVisionModel`` and ``Mistral3MultiModalProjector``), its
shape ``VisionConfig``.

The image processor's resize runs on the NPU (``ImageResize``): bicubic and
antialiased as torchvision resizes uint8, its longest edge at most
``longest_edge`` and each side up to whole soft tokens of ``patch_size *
merge`` pixels, then rescaled and normalized. The 14-pixel patches are cut
from that image in window order, the ``merge ** 2`` patches a soft token
merges consecutive: attention over one image is the same in any order of
its patches, each rotated by its own (row, column) angles, and the merger
is then a reshape. A call's grid, ``th`` by ``tw`` soft tokens, bounds
every copy by a per-call repeat and length, and ``nt``, their product,
every operator after.
"""

import dataclasses
import json
import math
from pathlib import Path

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, Scratchpad, lm
from iron.lm import DecoderLayer, ImageResize, Linear, NoCache, RMSNorm, Tower
from iron.lm.blocks import activation
from iron.lm.checkpoint import renamed, subtree
from iron.lm.config import rope_angles
from iron.operators.resample.reference import Interpolation

#: GEMM's K tile, which a patch row's width is padded to, and the soft
#: tokens' row block, which their rows are.
TILE_K, ROWS = 64, 64


@dataclasses.dataclass(frozen=True)
class VisionConfig(lm.Config):
    """Pixtral's and the projector's shape, from the checkpoint's
    ``vision_config`` and top level, and the image processor's from its
    ``processor_config.json`` (``from_checkpoint``).
    """

    json_prefix = "vision_config."

    precision: Precision = lm.not_json(Precision.HIGHEST, kw_only=True)
    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    head_dim: int
    intermediate_size: int
    patch_size: int
    rope_theta: float = dataclasses.field(
        metadata={"json": "rope_parameters.rope_theta"}
    )
    hidden_act: str = "silu"
    text_dim: int = dataclasses.field(
        default=3072, metadata={"json": "/text_config.hidden_size"}
    )
    # A soft token's side in patches.
    merge: int = dataclasses.field(default=2, metadata={"json": "/spatial_merge_size"})
    image_token: int = dataclasses.field(
        default=10, metadata={"json": "/image_token_index"}
    )
    projector_eps: float = dataclasses.field(
        default=1e-5, metadata={"json": "/text_config.rms_norm_eps"}
    )
    projector_act: str = dataclasses.field(
        default="gelu", metadata={"json": "/projector_hidden_act"}
    )
    # Pixtral's norms fix theirs.
    eps: float = lm.not_json(1e-5, kw_only=True)
    # The tokenizer's [IMG_BREAK] after each row of soft tokens, [IMG_END]
    # in place of the last.
    break_token: int = lm.not_json(12, kw_only=True)
    end_token: int = lm.not_json(13, kw_only=True)
    # The image processor's: the longest side a resize keeps, and its
    # normalization after the rescale by 1 / 255.
    longest_edge: int = lm.not_json(1540, kw_only=True)
    image_mean: tuple[float, ...] = lm.not_json(
        (0.48145466, 0.4578275, 0.40821073), kw_only=True
    )
    image_std: tuple[float, ...] = lm.not_json(
        (0.26862954, 0.26130258, 0.27577711), kw_only=True
    )
    # The largest image a call takes either way up, 12.6 MP.
    largest: tuple[int, int] = lm.not_json((3072, 4096), kw_only=True)

    @property
    def num_key_value_heads(self) -> int:
        return self.num_attention_heads

    @property
    def block(self) -> int:
        """A soft token's side in pixels."""
        return self.patch_size * self.merge

    @property
    def side(self) -> int:
        """The most soft tokens along a side."""
        return self.longest_edge // self.block

    @classmethod
    def from_checkpoint(cls, path) -> "VisionConfig":
        """``Config.from_checkpoint``, its processor's fields from the
        ``processor_config.json`` beside ``config.json``.
        """
        config = super().from_checkpoint(path)
        path = Path(path)
        directory = path if path.is_dir() else path.parent
        image = json.loads((directory / "processor_config.json").read_text())
        image = image["image_processor"]
        return dataclasses.replace(
            config,
            longest_edge=image["size"]["longest_edge"],
            image_mean=tuple(image["image_mean"]),
            image_std=tuple(image["image_std"]),
        )

    def size(self, height: int, width: int) -> tuple[int, int]:
        """The ``(height, width)`` the processor resizes an image to: within
        ``longest_edge`` on both sides at its aspect ratio, each side
        truncated, then each up to whole soft tokens.
        """
        ratio = max(height / self.longest_edge, width / self.longest_edge)
        if ratio > 1:
            height = int(math.floor(height / ratio))
            width = int(math.floor(width / ratio))
        b = self.block
        return (height - 1) // b * b + b, (width - 1) // b * b + b

    def tokens(self, height: int, width: int) -> list[int]:
        """The ids an image of ``height`` by ``width`` pixels takes in a
        prompt: a row of placeholders for each row of its soft tokens, each
        row ended by ``break_token``, the last by ``end_token``.
        """
        out_height, out_width = self.size(height, width)
        tw = out_width // self.block
        rows = [*[self.image_token] * tw, self.break_token] * (out_height // self.block)
        return rows[:-1] + [self.end_token]


class VisionLayer(DecoderLayer):
    """Pixtral's layer ``i``: RMS-normed attention over every patch of the
    image both ways, each rotated by its own 2-D angles, then RMS-normed
    gated SiLU, each joining its residual.
    """

    def __init__(self, c: VisionConfig, i: int):
        super().__init__(c, i, cache=NoCache())
        self.rope = c.head_dim


class PatchMerger(iron.Graph):
    """Mistral 3's merger: each soft token's ``merge ** 2`` patches side by
    side, projected by ``merging_layer``.
    """

    def __init__(self, c: VisionConfig):
        E = c.hidden_size
        self.merging_layer = Linear(
            E * c.merge**2, E, bias=False, precision=c.precision
        )

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # torch's unfold orders a token's inputs (channel, y, x); its
        # patches arrive (y, x, channel), each row whole.
        m = self.merging_layer
        E = m.out_features
        w = np.asarray(m.weight).reshape(E, E, -1).transpose(0, 2, 1)
        m.weight = iron.param(np.ascontiguousarray(w).reshape(E, -1))


class Projector(iron.Graph):
    """Mistral 3's ``multi_modal_projector``: ``norm``, the ``patch_merger``,
    ``linear_1``, its activation and ``linear_2``, into the text model's
    space.
    """

    def __init__(self, c: VisionConfig):
        E, T = c.hidden_size, c.text_dim
        self.norm = RMSNorm(E, c.projector_eps)
        self.patch_merger = PatchMerger(c)
        self.linear_1 = Linear(E, T, bias=False, precision=c.precision)
        self.linear_2 = Linear(T, T, bias=False, precision=c.precision)
        self.act = activation(c.projector_act)


class VisionTower(Tower):
    """Pixtral and the projector over one decoded image of at most
    ``side ** 2`` soft tokens, ``soft_rows`` rows, one compile for every
    size.

    Args:
        config: The tower's shape.
        weights: The checkpoint's tree; ``vision_tower`` and
            ``multi_modal_projector`` are read, at the top as transformers 4
            saved them or under ``model`` as transformers 5 does.
    """

    layer_class = VisionLayer
    profile = Path(__file__).with_name("profiles")
    renames = {
        "attention": "self_attn",
        "attention_norm": "input_layernorm",
        "ffn_norm": "post_attention_layernorm",
        "feed_forward": "mlp",
    }

    def __init__(self, config: VisionConfig, weights):
        c = config
        E, D, P, k = c.hidden_size, c.head_dim, c.patch_size, c.merge
        # Whole GEMM row blocks of soft tokens; past a call's, none is read.
        tokens = -(-(c.side**2) // ROWS) * ROWS
        super().__init__(c, tokens * k * k, tokens)
        found = vars(weights)
        nested = found["model"] if "vision_tower" not in found else weights
        tree = renamed(
            subtree(
                weights,
                vision_tower=nested.vision_tower,
                multi_modal_projector=nested.multi_modal_projector,
            ),
            self.renames,
        )
        self.load_layers(tree, "vision_tower.transformer.layers.")
        self.ln_pre = RMSNorm(E, c.eps)
        self.ln_pre.load_state_dict(tree, path="vision_tower.ln_pre.")
        self.multi_modal_projector = Projector(c)
        self.multi_modal_projector.load_state_dict(tree, path="multi_modal_projector.")
        # A patch moves in whole 16-byte units, so each of its P image rows
        # reads a few values past it, which zero weights drop.
        unit = 8 // math.gcd(P, 8)
        self.line = -(-3 * P // unit) * unit
        # The conv's (out, channel, y, x) as a patch row's (y, x, channel),
        # zeros past each line and to whole K tiles.
        conv = np.asarray(tree.vision_tower.patch_conv.weight).transpose(0, 2, 3, 1)
        self.width = -(-P * self.line // TILE_K) * TILE_K
        patch = np.zeros((E, P, self.line), conv.dtype)
        patch[:, :, : 3 * P] = conv.reshape(E, P, 3 * P)
        flat = np.zeros((E, self.width), conv.dtype)
        flat[:, : P * self.line] = patch.reshape(E, -1)
        self.patch = iron.param(flat)
        self.resize = ImageResize(
            c.largest,
            (c.longest_edge, c.longest_edge),
            Interpolation.BICUBIC,
            mean=c.image_mean,
            std=c.image_std,
        )
        # Each row's and column's angles, the even frequencies turning by
        # row and the odd by column, as Pixtral's axial RoPE splits them;
        # a table a window position, by soft token: a row's repeated across,
        # since a walk's length steps through its table.
        angles = rope_angles(D, c.side * k, c.rope_theta).reshape(-1, D // 4, 2, 2)
        rows, columns = (angles[:, :, axis].reshape(-1, D // 2) for axis in (0, 1))
        self.row_angles = [
            iron.weight(np.repeat(rows[y::k, None], c.side, 1).astype(bfloat16))
            for y in range(k)
        ]
        self.column_angles = [
            iron.weight(columns[x::k].astype(bfloat16)) for x in range(k)
        ]
        self.patches = iron.state((tokens, k * k, self.width))
        self.angle_rows = iron.state((tokens, k * k, D))

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
        th: Scratchpad[np.int32],
        tw: Scratchpad[np.int32],
        nt: Scratchpad[np.int32],
    ):
        """The ``(soft_rows, text_dim)`` soft tokens of the image ``rgb``,
        ``height`` by ``width`` pixels resized to ``out_height`` by
        ``out_width``, ``th`` by ``tw`` soft tokens, ``nt`` of them; the
        first ``nt`` rows are the image's, row by row.
        """
        c = self.config
        S, P, k, D = c.side, c.patch_size, c.merge, c.head_dim
        image = self.resize(
            rgb, height=height, width=width, out_height=out_height, out_width=out_width
        )
        pitch, half = image.shape[1], D // 2
        tokens = self.soft_rows
        by_row = TensorAccessPattern(
            (S, S, half), 0, [S, S, 1, half], [S * half, half, half, 1]
        )
        by_column = TensorAccessPattern(
            (S, half), 0, [S, S, 1, half], [0, half, half, 1]
        )
        for y in range(k):
            for x in range(k):
                w = y * k + x
                # Soft token (ty, tx)'s patch (y, x): P rows of P pixels.
                patch = TensorAccessPattern(
                    image.shape,
                    y * P * pitch + x * 3 * P,
                    [S, S, P, self.line],
                    [k * P * pitch, 3 * k * P, pitch, 1],
                )
                self.patches[:nt, w, : P * self.line] = image.at(
                    patch, (tokens, P * self.line), bounds={0: nt}, repeat=th, length=tw
                )
                for table, walk, cut in (
                    (self.row_angles[y], by_row, slice(None, half)),
                    (self.column_angles[x], by_column, slice(half, None)),
                ):
                    self.angle_rows[:nt, w, cut] = table.at(
                        walk, (tokens, half), bounds={0: nt}, repeat=th, length=tw
                    )
        n = nt * (k * k)
        pixels = self.patches.reshape(tokens * k * k, self.width)[:n]
        h = self.ln_pre(F.linear(pixels, self.patch, precision=c.precision))
        angles = self.angle_rows.reshape(tokens * k * k, D)[:n]
        return self.forward(h, n, {D: (angles, angles)})

    def pool(self, x, rows):
        c = self.config
        k2 = c.merge**2
        merger = self.multi_modal_projector
        x = merger.norm(x)
        # Bounded as x is, to a quarter of its rows.
        merged = x.reshape(self.soft_rows, k2 * c.hidden_size)
        return merger.patch_merger.merging_layer(merged)

    def head(self, x):
        p = self.multi_modal_projector
        return p.linear_2(p.act(p.linear_1(x)))

    def soft(self, values: dict) -> int:
        return values["nt"]

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, the largest image's."""
        rgb = (self.resize.resample.image_chunks, self.resize.chunk)
        return [dict(rgb=(rgb, np.uint8))]

    def longest(self) -> dict:
        """The per-call values of the largest image."""
        _, values = self.inputs(np.zeros((*self.config.largest, 3), np.uint8))
        return values

    def inputs(self, image) -> tuple[np.ndarray, dict]:
        """A call's image buffer and per-call sizes for a decoded ``image``,
        ``(height, width, 3)`` uint8.

        Raises:
            ValueError: The image does not fit a call, or the resize cannot
                resize it.
        """
        c = self.config
        out_height, out_width = c.size(*np.shape(image)[:2])
        rgb, values = self.resize.pack(image, out_height, out_width)
        th, tw = out_height // c.block, out_width // c.block
        return rgb, dict(**values, th=th, tw=tw, nt=th * tw)
