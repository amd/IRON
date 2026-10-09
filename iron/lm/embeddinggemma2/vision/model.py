#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's vision tower: its shape, where its checkpoint keeps
each weight, the size the image processor resizes an image to, and the
resize, the tower and its projection into the text model's space on the
NPU as one graph.
"""

import dataclasses
import math
from pathlib import Path
from types import SimpleNamespace

import aie.utils as aie_utils
import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import JointNarrowing
from iron.lm import Layout, rope_angles
from iron.operators.axpy import AXPY
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.mha import MHA
from iron.operators.resample.op import PatchPositions, Resample, ResampleTaps
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE

from ..model import ACCURATE, PIPELINES
from ..model import ROWS as BLOCK

# A GEMM's row block at its default tile: the patch rows and the pooled rows
# are whole blocks.
ROWS = 256
# The bytes of an image row Resample receives at a time.
CHUNK = 4096
# A core's patch columns, as many as its memory holds: 127 across on 16 cores.
PATCH_COLUMNS = 8
# The patch rows of a call, an image's budget, and the largest image it
# takes either way up, 12.6 MP.
PATCHES = 2560
LARGEST = (3072, 4096)

# Where the vision tune writes its tables, one per device.
COSTS = Path(__file__).parent


@dataclasses.dataclass(frozen=True)
class VisionConfig:
    hidden: int = 768
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


VISION = VisionConfig()


def layout(config: VisionConfig) -> Layout:
    """Each weight's place in the tower, its name in the checkpoint and its shape."""
    c = config
    E, F, D = c.hidden, c.hidden_dim, c.head_dim
    tower = "vision_tower"
    layer = f"{tower}.encoder.layers.{{i}}"
    out = {
        "patch": (f"{tower}.patch_embedder.input_proj.weight", (E, 3 * c.patch**2)),
        "position": (
            f"{tower}.patch_embedder.position_embedding_table",
            (2, c.positions, E),
        ),
        "projection": ("embed_vision.embedding_projection.weight", (c.text_dim, E)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.norm3": (f"{layer}.pre_feedforward_layernorm.weight", (E,)),
        "layers.{i}.norm4": (f"{layer}.post_feedforward_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.linear.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.linear.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.linear.weight", (E, F)),
    }
    for name in "qkvo":
        out[f"layers.{{i}}.{name}"] = (
            f"{layer}.self_attn.{name}_proj.linear.weight",
            (E, E),
        )
    for name in "qk":
        out[f"layers.{{i}}.{name}_norm"] = (
            f"{layer}.self_attn.{name}_norm.weight",
            (D,),
        )
    return out


def vision_tensors(tensors: dict) -> dict:
    """The vision tower's tensors of the full checkpoint, with the projection
    that takes its output into the text model's space.
    """
    return {
        k: v
        for k, v in tensors.items()
        if k.startswith(("vision_tower.", "embed_vision."))
    }


def size(height: int, width: int, max_tokens: int, config: VisionConfig):
    """The `(height, width)` the processor resizes an image to: the largest
    whole `pool * patch` blocks within `max_tokens` soft tokens at the
    image's aspect ratio.

    Args:
        height: The image's height in pixels.
        width: The image's width in pixels.
        max_tokens: The processor's `max_soft_tokens`.
        config: The tower's shape.

    Returns:
        The resized `(height, width)`.

    Raises:
        ValueError: Both sides round to no block, or the size exceeds the budget.
    """
    side = config.pool * config.patch
    max_patches = max_tokens * config.pool**2
    target_px = max_patches * config.patch**2
    factor = math.sqrt(target_px / (height * width))
    out_height = int(math.floor(factor * height / side)) * side
    out_width = int(math.floor(factor * width / side)) * side
    if out_height == 0 and out_width == 0:
        raise ValueError(f"a {height}x{width} image rounds to no {side}-pixel block")
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


class ImageProcessor(SimpleNamespace):
    """The image processor on the NPU, called in a graph's body: a decoded
    image resized as torchvision resizes it, rescaled to `[0, 1]` and cut
    into the tower's patches, each soft token's `pool ** 2` patches
    consecutive rows, row-major within the window, the tokens row-major
    over the image.

    A call takes the image, `(height, width, 3)` uint8 with each row padded
    to whole `CHUNK`-byte chunks (`inputs` lays it out), and the size the
    processor resizes it to, all four sizes per call. `Resample` resizes it
    by the `ResampleTaps` tables into the state `raster`, and
    `PatchPositions` gives each tower row's patch in it, `xy` and
    `position_ids`; rows past the image gather the raster's zero patch.

    Args:
        config: The tower's shape.
        patches: The patch rows of a call.
        image: The `(height, width)` of the largest image a call takes
            either way up.
    """

    def __init__(self, config: VisionConfig, patches=PATCHES, image=LARGEST):
        c = config
        self.config = config
        self.patches = patches
        self.image = image
        k, side = c.pool, c.pool * c.patch
        cores = 2 * aie_utils.ensure_current_device().cols
        # Every grid of whole pooling windows the rows hold; the fewest patch
        # columns give the most bands and padded raster rows.
        grids = [(patches // s // k * k, s) for s in range(k, patches // k + 1, k)]
        shared = dict(
            height=side,
            width=side,
            out_height=side,
            out_width=side,
            chunk=CHUNK,
            patch_columns=PATCH_COLUMNS,
            width_chunks=PATCH_COLUMNS * cores,
            height_chunks=16 * -(-grids[0][0] // 16),
            patch_rows=max(b * (s // cores + 1) * cores for b, s in grids),
            num_aie_columns=cores // 2,
            num_channels=2,
        )
        a, b = image
        self.resample = Resample(
            image_chunks=max(a * -(-3 * b // CHUNK), b * -(-3 * a // CHUNK)),
            **shared,
        )
        self.raster = iron.state((shared["patch_rows"], 3 * c.patch**2))
        taps = dict(
            in_size=side,
            out_size=side,
            words=self.resample.words,
            slots=c.patch,
            num_aie_columns=cores // 2,
            num_channels=2,
        )
        self.taps_w = ResampleTaps(chunks=shared["width_chunks"], **taps)
        self.taps_h = ResampleTaps(chunks=shared["height_chunks"], **taps)
        self.patch_positions = PatchPositions(
            rows=patches,
            out_height=side,
            out_width=side,
            pool=k,
            positions=c.positions,
            cores=cores,
        )

    def __call__(self, rgb, height, width, out_height, out_width):
        """The `(pixels, xy, position_ids)` of the image `rgb`, `height` by
        `width` pixels resized to `out_height` by `out_width`, in `patches`
        rows: `(patches, 3 * patch ** 2)` bf16 and `(2 * patches,)` int32
        twice.
        """
        T = self.patches
        taps_w = self.taps_w(in_samples=width, out_samples=out_width)
        taps_h = self.taps_h(in_samples=height, out_samples=out_height)
        self.resample(
            rgb,
            taps_w,
            taps_h,
            self.raster,
            rows=height,
            columns=width,
            out_rows=out_height,
            out_columns=out_width,
        )
        xy, position_ids, order = self.patch_positions(
            out_rows=out_height, out_columns=out_width
        )
        return Copy(self.raster[order]), xy.reshape(2 * T), position_ids.reshape(2 * T)

    # -- on the host -----------------------------------------------------------

    def shapes(self) -> dict:
        """The input shape of a call."""
        return dict(rgb=((self.resample.image_chunks, CHUNK), np.uint8))

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
        image = np.asarray(image)
        if image.dtype != np.uint8 or image.ndim != 3 or image.shape[2] != 3:
            raise ValueError(
                f"an image is (height, width, 3) uint8, not {image.shape} {image.dtype}"
            )
        c = self.config
        H, W, _ = image.shape
        ho, wo = size(H, W, max_tokens, c)
        n = ho // c.patch * (wo // c.patch)
        line = -(-3 * W // CHUNK) * CHUNK
        op = self.resample
        if n > self.patches or op.image_chunks * CHUNK < H * line:
            a, b = self.image
            raise ValueError(
                f"a {H}x{W} image of {n} patches does not fit a call's "
                f"{self.patches} patches or {a}x{b} image"
            )
        # Resample's own checks refuse a size it cannot resize.
        dataclasses.replace(op, height=H, width=W, out_height=ho, out_width=wo)
        buffer = np.zeros((op.image_chunks, CHUNK), np.uint8)
        rows = buffer.reshape(-1)[: H * line].reshape(H, line)
        rows[:, : 3 * W] = image.reshape(H, 3 * W)
        return buffer, dict(n=n, height=H, width=W, out_height=ho, out_width=wo)


class VisionTower(SimpleNamespace):
    """The vision tower and `embed_vision` over at most `patches` patches,
    one compile for every image, called in a graph's body. It is a
    namespace, so the graph that holds it names its weights by their path.

    A call takes a decoded image, which `processor` resizes and cuts into
    patches in pooling-window order on the NPU, so pooling is a fixed sum
    of row blocks, a GEMM by a 0/1 matrix. `n`, the real patches, bounds
    every operator after the processor, the pooling's sum among them. Each
    head's channels are reordered so that the axial RoPE, x on its first
    half and y on its second, is one rotation of halves: a permutation
    within a head changes neither its norm nor a query's product with a key.

    The rows a call looks up by patch position are gathered on the NPU: the
    RoPE angles by `xy`, each patch's x and y side by side, so a patch's row
    is x's angles then y's; the position embeddings by `position_ids` from
    x's table and y's as one, every patch's x, then every patch's y plus
    `positions`. Padding looks up each table's last row, zero.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
        patches: The patch rows of a call, whole `ROWS`-row blocks and
            attention's blocks for each of its pipelines.
        image: The largest image a call takes, as `ImageProcessor` takes it.
    """

    def __init__(
        self,
        config: VisionConfig,
        weights: SimpleNamespace,
        patches=PATCHES,
        image=LARGEST,
    ):
        c = config
        if patches % ROWS or patches % (BLOCK * PIPELINES):
            raise ValueError(
                f"{patches} patches are not whole {ROWS}-row blocks and "
                f"{BLOCK}-row blocks for each of attention's {PIPELINES} pipelines"
            )
        self.config = config
        self.processor = ImageProcessor(config, patches, image)
        self.patch = weights.patch
        position = np.zeros((2 * c.positions + 1, c.hidden), bfloat16)
        position[:-1] = weights.position.reshape(-1, c.hidden)
        self.position = iron.weight(position)
        self.projection = weights.projection
        half = c.head_dim // 2
        quarter = np.arange(half // 2)
        # The x half's first and second quarters, then the y half's.
        order = np.concatenate(
            [quarter, quarter + half, quarter + half // 2, quarter + 3 * half // 2]
        )
        self.layers = [
            SimpleNamespace(
                **vars(w)
                | {
                    name: vars(w)[name]
                    .reshape(c.n_heads, c.head_dim, c.hidden)[:, order]
                    .reshape(c.hidden, c.hidden)
                    for name in ("q", "k")
                }
                | {name: vars(w)[name][order] for name in ("q_norm", "k_norm")}
            )
            for w in weights.layers
        ]
        angles = np.zeros((c.positions + 1, half), bfloat16)
        angles[:-1] = rope_angles(half, c.positions, c.rope_base)
        self.angles = iron.weight(angles)
        self.minus_one = iron.weight(np.full((patches, c.hidden), -1, bfloat16))
        # Soft token j sums rows j * pool ** 2 onwards; a token past the
        # image's sums none of its rows.
        window = c.pool**2
        tokens = -(-(patches // window) // ROWS) * ROWS
        pool = np.zeros((tokens, patches), bfloat16)
        for j in range(patches // window):
            pool[j, j * window : (j + 1) * window] = 1
        self.pool = iron.weight(pool)

    def __call__(self, rgb, n, height, width, out_height, out_width):
        """The `(tokens, text_dim)` soft tokens of the image `rgb`, `height`
        by `width` pixels resized to `out_height` by `out_width`, its `n`
        patches, `tokens` `patches // pool ** 2` rounded up to whole `ROWS`;
        the first `n // pool ** 2` are the image's, the rest zero.
        """
        c = self.config
        pixels, xy, position_ids = self.processor(
            rgb, height, width, out_height, out_width
        )
        T = pixels.shape[0]
        x = AXPY(pixels[:n], self.minus_one[:n], scalar_factor=2.0)
        h = GEMM(x, self.patch, b_col_maj=True, **ACCURATE)
        position = Copy(self.position[position_ids]).reshape(2, T, c.hidden)
        h = ElementwiseAdd(ElementwiseAdd(h, position[0, :n]), position[1, :n])
        angles = Copy(self.angles[xy]).reshape(T, c.head_dim)[:n]
        for w in self.layers:
            h = self.layer(w, h, angles)
        pooled = GEMM(self.pool[:, :n], h, **ACCURATE)
        # The mean's 1 / pool ** 2 and the sqrt(hidden) scale folded into
        # the norm's epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        s2 = c.hidden / c.pool**4
        pooled = RMSNorm(pooled, epsilon=c.eps / s2)
        return GEMM(pooled, self.projection, b_col_maj=True, **ACCURATE)

    def layer(self, w, x, angles):
        c = self.config
        h = RMSNorm(x, weight=w.norm1, epsilon=c.eps)
        a = RMSNorm(self.attention(w, h, angles), weight=w.norm2, epsilon=c.eps)
        x = ElementwiseAdd(x, a)
        h = RMSNorm(x, weight=w.norm3, epsilon=c.eps)
        gate = GELU(GEMM(h, w.gate, b_col_maj=True, **ACCURATE))
        f = ElementwiseMul(gate, GEMM(h, w.up, b_col_maj=True, **ACCURATE))
        f = GEMM(f, w.down, b_col_maj=True, **ACCURATE)
        return ElementwiseAdd(x, RMSNorm(f, weight=w.norm4, epsilon=c.eps))

    def attention(self, w, h, angles):
        c = self.config
        T, H, D = h.shape[0], c.n_heads, c.head_dim
        q = GEMM(h, w.q, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        k = GEMM(h, w.k, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        v = GEMM(h, w.v, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        q = RoPE(RMSNorm(q, weight=w.q_norm, epsilon=c.eps), angles)
        k = RoPE(RMSNorm(k, weight=w.k_norm, epsilon=c.eps), angles)
        v = RMSNorm(v, epsilon=c.eps)
        o = MHA(
            q.reshape(T, H, D),
            k.reshape(T, H, D),
            v.reshape(T, H, D),
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            emulate_bf16_mmul_with_bfp16=False,
            scale=1.0,
            num_pipelines=PIPELINES,
        )
        return GEMM(o.reshape(T, H * D), w.o, b_col_maj=True, **ACCURATE)


class Vision(iron.Graph):
    """The vision tower as a graph of its own, one compile for every image.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
        patches: The patch rows of a call, as `VisionTower` takes them.
        image: The largest image a call takes, as `ImageProcessor` takes it.
    """

    # GEMM tiles narrow enough for N = 768 to span every column.
    profile = Path(__file__).with_name("profiles")

    def __init__(
        self,
        config: VisionConfig,
        weights: SimpleNamespace,
        patches=PATCHES,
        image=LARGEST,
    ):
        self.config = config
        self.vision = VisionTower(config, weights, patches, image)

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
        return self.vision(rgb, n, height, width, out_height, out_width)

    # -- on the host -----------------------------------------------------------

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, `patches` rows."""
        return [self.vision.processor.shapes()]

    def load(self, tuner: JointNarrowing | None = None) -> "Vision":
        """Compile before the first call, so the arena is made once.

        Args:
            tuner: Narrows and packs each version's designs by cost.
        """
        for shapes in self.shapes():
            self.compile(coresident=tuner, **shapes)
        return self

    def embed(self, image, max_tokens: int = VISION.image_tokens) -> np.ndarray:
        """The soft tokens of one decoded image or video frame,
        `(tokens, text_dim)` float32, in the text model's space.

        Args:
            image: `(height, width, 3)` uint8.
            max_tokens: The processor's `max_soft_tokens`: `image_tokens`
                for an image, `video_tokens` for a frame.
        """
        rgb, values = self.vision.processor.inputs(image, max_tokens)
        tokens = self(rgb, **values).numpy().reshape(-1, self.config.text_dim)
        return np.asarray(tokens[: values["n"] // self.config.pool**2], np.float32)
