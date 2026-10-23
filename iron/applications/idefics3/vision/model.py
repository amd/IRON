# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM's vision tower: a SigLIP ViT (``Idefics3VisionTransformer``) and
its ``Idefics3Connector`` (pixel-shuffle, then a bias-free projection into
the text model's space), an ``iron.lm.Tower`` of ``EncoderLayer``s loaded
from SigLIP's modules (``layer_norm1``/``layer_norm2``, biased attention, a
GELU-tanh ``fc1``/``fc2``).

One image of any size up to ``largest``, processed on the NPU as
Idefics3's image processor does it, each resize Lanczos as torchvision
computes it on uint8: resized to ``longest_edge`` on its longest side
(``ImageResize``), then to whole ``image_size`` squares (another
``ImageResize``) and split (``do_image_splitting``) into those squares, a
frame each, and the whole resized to ``image_size`` square, a last frame;
each frame rescaled and normalized (``ImagePatches``). Each frame's patch
grid is whole, so a patch's position embedding is its raster index, as the
processor's position ids are for a whole square grid. Nothing rotates
(``angles`` None).
"""

import dataclasses
from pathlib import Path

import numpy as np
from aie.helpers.taplib import TensorAccessPattern

import iron
import iron.functional as F
from iron import Precision, Scratchpad
from iron.lm import Config, ImagePatches, ImageResize, LayerNorm, Tower, not_json
from iron.operators.copy import Copy
from iron.operators.resample.reference import Interpolation


@dataclasses.dataclass(frozen=True)
class VisionConfig(Config):
    """SmolVLM's vision tower and connector's shape, from the checkpoint's
    ``vision_config``, ``text_config`` and top-level ``scale_factor``;
    ``eps`` is its LayerNorms', the checkpoint's ``layer_norm_eps``.
    """

    precision: Precision = not_json(Precision.MEDIUM, kw_only=True)
    # Every projection biased (``Attention``, ``MLP``).
    attention_bias = mlp_bias = True

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
    # The image processor's (preprocessor_config.json): the first resize's
    # longest side, whether it splits the image into squares of
    # ``image_size``, and its normalization after the rescale by 1 / 255.
    longest_edge: int = not_json(2048, kw_only=True)
    do_image_splitting: bool = not_json(True, kw_only=True)
    image_mean: tuple[float, ...] = not_json((0.5, 0.5, 0.5), kw_only=True)
    image_std: tuple[float, ...] = not_json((0.5, 0.5, 0.5), kw_only=True)
    # The largest image a call takes either way up, 12.6 MP.
    largest: tuple[int, int] = not_json((3072, 4096), kw_only=True)

    def __post_init__(self):
        if self.head_dim is None:
            object.__setattr__(
                self, "head_dim", self.hidden_size // self.num_attention_heads
            )

    @property
    def num_key_value_heads(self) -> int:
        return self.num_attention_heads

    @property
    def side(self) -> int:
        """The patches along each side of the image."""
        return self.image_size // self.patch_size

    @property
    def tokens(self) -> int:
        """The soft tokens an image gives."""
        return (self.side // self.scale_factor) ** 2

    @property
    def frames(self) -> int:
        """The most frames an image gives: its squares and the whole."""
        if not self.do_image_splitting:
            return 1
        return (-(-self.longest_edge // self.image_size)) ** 2 + 1

    def split(self, height: int, width: int) -> tuple[int, int]:
        """The `(height, width)` the processor resizes the first resize's
        `height` by `width` to before splitting it: whole `image_size`
        squares at its aspect ratio; unchanged without splitting.
        """
        if not self.do_image_splitting:
            return height, width
        M, aspect = self.image_size, width / height
        if width >= height:
            width = -(-width // M) * M
            height = -(-int(width / aspect) // M) * M
        else:
            height = -(-height // M) * M
            width = -(-int(height * aspect) // M) * M
        return height, width

    def grid(self, height: int, width: int) -> tuple[int, int]:
        """The rows and columns of squares an image of `height` by `width`
        pixels is split into: none (0, 0) where the split size is one square
        or less.
        """
        split = self.split(*self.size(height, width))
        if not self.do_image_splitting or max(split) <= self.image_size:
            return 0, 0
        return split[0] // self.image_size, split[1] // self.image_size

    def size(self, height: int, width: int) -> tuple[int, int]:
        """The `(height, width)` the processor first resizes an image to:
        `longest_edge` on its longest side, the other at its aspect ratio,
        truncated, then made even.
        """
        aspect = width / height
        if width >= height:
            width = self.longest_edge
            height = int(width / aspect)
            height += height % 2
        else:
            height = self.longest_edge
            width = int(height * aspect)
            width += width % 2
        return max(height, 1), max(width, 1)


class VisionTower(Tower):
    """The vision tower and connector over one decoded image, a frame a
    call: resized (``VisionConfig.size``, then ``VisionConfig.split``) and
    a frame of it, a square or the whole resized to ``image_size`` square,
    normalized on the NPU, its patches embedded, its soft tokens in the text
    model's space written after the frames before it. A call returns every
    frame's rows, those of the image's frames so far valid.

    Every call of an image resizes it anew: a call is one version, whose
    steps all run.

    Args:
        config: The tower's shape.
        weights: The checkpoint's tree; ``model.vision_model`` and
            ``model.connector`` are read.
    """

    profile = Path(__file__).with_name("profiles")
    renames = {
        "layer_norm1": "input_layernorm",
        "self_attn.out_proj": "self_attn.o_proj",
        "layer_norm2": "post_attention_layernorm",
    }

    def __init__(self, config: VisionConfig, weights):
        c = config
        self.vision_model = weights.model.vision_model
        self.connector = weights.model.connector
        super().__init__(c, c.side**2, c.frames * c.tokens)
        self.final_norm = LayerNorm(c.hidden_size, c.eps)
        v = "model.vision_model."
        self.load_layers(weights, f"{v}encoder.layers.", f"{v}post_layernorm.")
        through = (c.longest_edge, c.longest_edge)
        self.resize = ImageResize(c.largest, through, Interpolation.LANCZOS)
        # A band past the split image: the last square's rows from its corner
        # run past the image's last row by the squares before it in its row.
        self.squares = ImageResize(
            through,
            (c.longest_edge + 16, c.longest_edge),
            Interpolation.LANCZOS,
            chunk=self.resize.pitch,
        )
        self.processor = ImagePatches(
            c.side**2,
            through,
            pool=1,
            chunk=self.squares.pitch,
            interpolation=Interpolation.LANCZOS,
            mean=c.image_mean,
            std=c.image_std,
            out=(c.image_size, c.image_size),
        )
        # The conv's (out, channel, y, x) as a patch row's (y, x, channel).
        weight = self.vision_model.embeddings.patch_embedding.weight
        weight = np.ascontiguousarray(weight.transpose(0, 2, 3, 1))
        self.patch = iron.param(weight.reshape(c.hidden_size, -1))
        # A frame's rows, as the processor reads them.
        self.frame = iron.state(
            (self.processor.resample.image_chunks, self.squares.pitch), np.uint8
        )
        self.soft_frames = iron.state((self.soft_rows, c.text_dim))

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

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        mid_height: Scratchpad[np.int32],
        mid_width: Scratchpad[np.int32],
        split_height: Scratchpad[np.int32],
        split_width: Scratchpad[np.int32],
        offset: Scratchpad[np.int32],
        frame_height: Scratchpad[np.int32],
        frame_width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
        first: Scratchpad[np.int32],
    ):
        """Every frame's soft tokens, this one's of the image ``rgb`` from
        row ``first``: ``height`` by ``width`` pixels resized to
        ``mid_height`` by ``mid_width``, then to ``split_height`` by
        ``split_width``; the frame ``frame_height`` by ``frame_width``
        pixels of that from byte ``offset``, resized to ``out_height`` by
        ``out_width``, the tower's square.
        """
        mid = self.resize(
            rgb,
            height=height,
            width=width,
            out_height=mid_height,
            out_width=mid_width,
        )
        split = self.squares(
            mid,
            height=mid_height,
            width=mid_width,
            out_height=split_height,
            out_width=split_width,
        )
        # The frame's rows from its corner, in segments of a square's row.
        pitch, chunks = self.squares.pitch, self.processor.resample.image_chunks
        k = pitch // (3 * self.config.image_size)
        segments = split.reshape(split.shape[0] * k, pitch // k)
        n = frame_height * k
        frame = self.frame.reshape(chunks * k, pitch // k)
        Copy.step(segments[offset : offset + chunks * k][:n], frame[:n], dtype=np.uint8)
        pixels, _, _ = self.processor(
            self.frame,
            height=frame_height,
            width=frame_width,
            out_height=out_height,
            out_width=out_width,
        )
        e = self.vision_model.embeddings
        h = F.linear(pixels, self.patch, precision=Precision.HIGHEST)
        h = h + e.patch_embedding.bias + e.position_embedding.weight
        soft = self.forward(h, self.max_tokens, None)
        self.soft_frames[first : first + soft.shape[0]] = soft
        return Copy.step(self.soft_frames)

    def soft(self, values: dict) -> int:
        return self.config.tokens

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, the largest image's."""
        rgb = (self.resize.resample.image_chunks, self.resize.chunk)
        return [dict(rgb=(rgb, np.uint8))]

    def longest(self) -> dict:
        """The per-call values of the largest image's first frame."""
        (_, values), *_ = self.calls(np.zeros((*self.config.largest, 3), np.uint8))
        return values

    def calls(self, image) -> list[tuple[np.ndarray, dict]]:
        """Each frame's call of a decoded ``image``, ``(height, width, 3)``
        uint8, in the processor's order: the squares row by row, then the
        whole; its image buffer and per-call sizes.

        Raises:
            ValueError: The image does not fit a call, or a resize cannot
                resize it.
        """
        c, M = self.config, self.config.image_size
        mid = c.size(*np.shape(image)[:2])
        split = c.split(*mid)
        rgb, values = self.resize.pack(image, *mid)
        # Resample's own checks refuse a size it cannot resize.
        self.squares.resample.replace(
            height=mid[0], width=mid[1], out_height=split[0], out_width=split[1]
        )
        sizes = dict(
            height=values["height"],
            width=values["width"],
            mid_height=mid[0],
            mid_width=mid[1],
            split_height=split[0],
            split_width=split[1],
            out_height=M,
            out_width=M,
        )
        rows, columns = c.grid(*np.shape(image)[:2])
        pitch = self.squares.pitch
        k = pitch // (3 * M)
        frames = [(r * M * k + j, M, M) for r in range(rows) for j in range(columns)]
        frames.append((0, *split))
        return [
            (
                rgb,
                sizes
                | dict(
                    offset=offset,
                    frame_height=h,
                    frame_width=w,
                    first=i * c.tokens,
                ),
            )
            for i, (offset, h, w) in enumerate(frames)
        ]
