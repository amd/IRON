#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's vision tower: its shape, where its checkpoint keeps
each weight, and the tower with its projection into the text model's space
on the NPU as one graph.
"""

import dataclasses
from pathlib import Path
from types import SimpleNamespace

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
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.softmax import Softmax
from iron.operators.transpose import Transpose

from ..model import ACCURATE

# A GEMM's row block at its default tile: a version's rows are a multiple of it.
ROWS = 256

# Where `python -m iron.lm.embeddinggemma2.vision.tune` writes its measurements.
COSTS = Path(__file__).with_name("costs_npu2.json")


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


class Vision(iron.Graph):
    """The vision tower and `embed_vision` over at most `rows[-1]` patches, a
    version per entry of `rows`.

    A call takes an image's patches in pooling-window order: each soft
    token's `pool ** 2` patches are consecutive rows, the tokens row-major
    over the image, so pooling is a fixed sum of row blocks, a GEMM by a 0/1
    matrix. `n`, the real patches, masks the padded keys; padded rows are
    zero, stay finite and are never read. Each head's channels are
    reordered so that the axial RoPE, x on its first half and y on its
    second, is one rotation of halves: a permutation within a head changes
    neither its norm nor a query's product with a key.

    The rows a call looks up by patch position (the position embeddings and
    the RoPE angles) are gathered on the host, in `gathered`.

    Args:
        config: The tower's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
        rows: Each version's patch rows, whole `ROWS`-row blocks.
    """

    # GEMM tiles narrow enough for N = 768 or 1280 to span every column.
    profile = Path(__file__).with_name("profiles")

    def __init__(
        self, config: VisionConfig, weights: SimpleNamespace, rows=(1280, 2560)
    ):
        c = config
        if any(T % ROWS for T in rows):
            raise ValueError(f"{rows} rows are not whole {ROWS}-row versions")
        self.config = config
        self.rows = sorted(rows)
        self.patch = weights.patch
        self.position = weights.position
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
        self.angles = rope_angles(half, c.positions, c.rope_base).astype(bfloat16)
        self.minus_one = np.full((self.rows[-1], c.hidden), -1, bfloat16)
        # Soft token j sums rows j * pool ** 2 onwards; rows of padded tokens
        # are padding's.
        window = c.pool**2
        self.pool = {}
        for T in self.rows:
            tokens = -(-(T // window) // ROWS) * ROWS
            pool = np.zeros((tokens, T), bfloat16)
            for j in range(T // window):
                pool[j, j * window : (j + 1) * window] = 1
            self.pool[T] = pool

    def body(self, pixels, px, py, angles, *, n: Scratchpad[np.int32]):
        c = self.config
        T = pixels.shape[0]
        x = AXPY(pixels, self.minus_one[:T], scalar_factor=2.0)
        h = GEMM(x, self.patch, b_col_maj=True, **ACCURATE)
        h = ElementwiseAdd(ElementwiseAdd(h, px), py)
        for w in self.layers:
            h = self.layer(w, h, angles, n)
        pooled = GEMM(self.pool[T], h, **ACCURATE)
        # The mean's 1 / pool ** 2 and the sqrt(hidden) scale folded into
        # the norm's epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        s2 = c.hidden / c.pool**4
        pooled = RMSNorm(pooled, epsilon=c.eps / s2)
        return GEMM(pooled, self.projection, b_col_maj=True, **ACCURATE)

    def layer(self, w, x, angles, n):
        c = self.config
        h = RMSNorm(x, weight=w.norm1, epsilon=c.eps)
        a = RMSNorm(self.attention(w, h, angles, n), weight=w.norm2, epsilon=c.eps)
        x = ElementwiseAdd(x, a)
        h = RMSNorm(x, weight=w.norm3, epsilon=c.eps)
        gate = GELU(GEMM(h, w.gate, b_col_maj=True, **ACCURATE))
        f = ElementwiseMul(gate, GEMM(h, w.up, b_col_maj=True, **ACCURATE))
        f = GEMM(f, w.down, b_col_maj=True, **ACCURATE)
        return ElementwiseAdd(x, RMSNorm(f, weight=w.norm4, epsilon=c.eps))

    def attention(self, w, h, angles, n):
        c = self.config
        T, H, D = h.shape[0], c.n_heads, c.head_dim
        q = GEMM(h, w.q, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        k = GEMM(h, w.k, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        v = GEMM(h, w.v, b_col_maj=True, **ACCURATE).reshape(T * H, D)
        q = RoPE(RMSNorm(q, weight=w.q_norm, epsilon=c.eps), angles)
        k = RoPE(RMSNorm(k, weight=w.k_norm, epsilon=c.eps), angles)
        v = RMSNorm(v, epsilon=c.eps)
        q, k = (
            Copy(t.reshape(T, H, D).transpose(1, 0, 2)).reshape(H, T, D) for t in (q, k)
        )
        v = Transpose(v.reshape(T, H * D)).reshape(H, D, T)
        for i in range(H):
            scores = GEMM(q[i], k[i], b_col_maj=True, **ACCURATE)
            weights = Softmax(scores, vector_size=n)
            # weights @ v as (v^T @ weights^T)^T: N = T rather than D spans
            # every column. Over the head's queries, which the scores were
            # their last use of.
            GEMM(
                v[i],
                weights,
                q[i],
                b_col_maj=True,
                c_col_maj=True,
                tile_k=128,
                **ACCURATE,
            )
        o = Copy(q.transpose(1, 0, 2)).reshape(T, H * D)
        return GEMM(o, w.o, b_col_maj=True, **ACCURATE)

    # -- on the host -----------------------------------------------------------

    def shapes(self) -> list[dict]:
        """Each version's input shapes, fewest rows first."""
        c = self.config
        return [
            dict(
                pixels=(T, 3 * c.patch**2),
                px=(T, c.hidden),
                py=(T, c.hidden),
                angles=(T, c.head_dim),
            )
            for T in self.rows
        ]

    def load(self, tuner: JointNarrowing | None = None) -> "Vision":
        """Compile every version before the first call, so the arena is made once.

        Args:
            tuner: Narrows and packs each version's designs by cost.
        """
        for shapes in self.shapes():
            self.compile(coresident=tuner, **shapes)
        return self

    def order(self, positions) -> np.ndarray:
        """The real patches of `positions` `(patches, 2)`, (x, y) with -1
        for padding, in pooling-window order: each soft token's patches
        consecutive, row-major within the window, the tokens row-major.

        Raises:
            ValueError: The real patches are not whole pooling windows.
        """
        k = self.config.pool
        real = np.flatnonzero((positions >= 0).all(axis=-1))
        x, y = positions[real].T
        width, height = x.max() + 1, y.max() + 1
        if width % k or height % k or real.size != width * height:
            raise ValueError(
                f"{real.size} patches are not a whole grid of {k}x{k} windows"
            )
        token = x // k + width // k * (y // k)
        return real[np.lexsort((x % k, y % k, token))]

    def gathered(self, positions):
        """The rows the patches at `positions` (in the order a call takes
        them) look up: their x and y position embeddings and their RoPE
        angles, x's then y's. The one place a call's lookups run on the
        host; an on-NPU gather by per-call indices replaces it.
        """
        x, y = positions.T
        angles = np.concatenate([self.angles[x], self.angles[y]], axis=-1)
        return self.position[0][x], self.position[1][y], angles

    def inputs(self, pixel_values, positions) -> tuple[dict, int]:
        """A call's inputs and `n` for the processor's `pixel_values`
        `(patches, 3 * patch ** 2)` and `positions` `(patches, 2)`, padded to
        the fewest rows a version has.

        Raises:
            ValueError: More real patches than the largest version holds.
        """
        c = self.config
        order = self.order(np.asarray(positions))
        n = order.size
        if n > self.rows[-1]:
            raise ValueError(f"{n} patches do not fit {self.rows[-1]} rows")
        T = min(T for T in self.rows if T >= n)
        shapes = next(s for s in self.shapes() if s["pixels"][0] == T)
        out = {name: np.zeros(shape, bfloat16) for name, shape in shapes.items()}
        out["pixels"][:n] = np.asarray(pixel_values)[order]
        for name, rows in zip(
            ("px", "py", "angles"), self.gathered(np.asarray(positions)[order])
        ):
            out[name][:n] = rows
        return out, n

    def embed(self, pixel_values, positions) -> np.ndarray:
        """The soft tokens of one image or video frame, `(tokens, text_dim)`
        float32, in the text model's space.
        """
        inputs, n = self.inputs(pixel_values, positions)
        tokens = self(*inputs.values(), n=n).numpy().reshape(-1, self.config.text_dim)
        return np.asarray(tokens[: n // self.config.pool**2], np.float32)
