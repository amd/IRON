#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM's vision tower: a SigLIP-style ViT (``Idefics3VisionTransformer``,
traced from the real ``transformers`` source), its patch embedding, its
``Idefics3Connector`` (pixel-shuffle then a bias-free projection into the
text model's space), on the NPU as one graph, and ``VisionTowerOracle``,
its float32 forward pass on the host.

Scoped to one 512x512 image, no splitting (``do_image_splitting=False``):
the real processor's NaViT-style variable-resolution tiling (several crops
plus a thumbnail, each with its own valid patch grid) is not attempted
here. The image is decoded, resized to 512x512 and normalized on the
host (the library's on-device ``Resample`` targets antialiased resize at
whatever aspect ratio a call gives; for one fixed square size the simpler
host step is the lighter touch for this first pass). The patch grid is
then whole (32x32, 1024 patches), so each patch's absolute position
embedding is simply its raster index, ``row * 32 + col`` -- the real
processor's bucketized, padding-aware position ids reduce to this when
every patch is real and the grid is square, which it always is here.

Unlike EmbeddingGemma 2's tower (RMSNorm, RoPE, q/k-norm, pooled soft
tokens), this one is unpooled (each patch is its own token until the
connector's pixel-shuffle, after every layer) and its norm is affine
LayerNorm (weight *and* bias, not RMSNorm): composed from the library's
``LayerNorm`` (gamma 1, beta 0) with ``RowwiseMul``/``RowwiseAdd``, the
same composition whisper-port's encoder uses -- the device kernel's own
``eps`` is fixed (1e-5); the checkpoint's own (1e-6) is negligible past
bf16, verified against the oracle, which uses the checkpoint's value.
"""

import dataclasses
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.lm import Config, Conv2d, project
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.layer_norm import LayerNorm
from iron.operators.mha import MHA

# Each product's float32 sum rounded once.
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)

# The checkpoint's own LayerNorm eps (vision_config.layer_norm_eps):
# negligible past bf16 against the device kernel's fixed 1e-5, so only the
# float32 oracle uses it.
EPS = 1e-6


@dataclasses.dataclass(frozen=True)
class VisionConfig(Config):
    """SmolVLM's vision tower and connector's shape, from the checkpoint's
    ``vision_config``/``text_config``/top-level ``scale_factor``.
    """

    hidden: int = dataclasses.field(metadata={"json": "vision_config.hidden_size"})
    n_layers: int = dataclasses.field(
        metadata={"json": "vision_config.num_hidden_layers"}
    )
    n_heads: int = dataclasses.field(
        metadata={"json": "vision_config.num_attention_heads"}
    )
    hidden_dim: int = dataclasses.field(
        metadata={"json": "vision_config.intermediate_size"}
    )
    patch: int = dataclasses.field(metadata={"json": "vision_config.patch_size"})
    image_size: int = dataclasses.field(metadata={"json": "vision_config.image_size"})
    scale_factor: int = dataclasses.field(metadata={"json": "scale_factor"})
    text_dim: int = dataclasses.field(metadata={"json": "text_config.hidden_size"})
    head_dim: int | None = dataclasses.field(default=None, kw_only=True)

    def __post_init__(self):
        if self.head_dim is None:
            object.__setattr__(self, "head_dim", self.hidden // self.n_heads)


def vision_tensors(tensors: dict) -> dict:
    """The vision tower's and connector's tensors of the full checkpoint."""
    return {
        k: v
        for k, v in tensors.items()
        if k.startswith(("model.vision_model.", "model.connector."))
    }


def pixel_shuffle(x: np.ndarray, side: int, scale: int) -> np.ndarray:
    """``x`` ``(side * side, hidden)`` patches, row-major, merged
    ``scale x scale`` neighboring patches' channels together:
    ``(side // scale) ** 2, hidden * scale ** 2)``, row-major over the
    smaller grid. The exact reshape/permute the real connector's
    ``pixel_shuffle`` does, as one array op (no batch dimension here).
    """
    h = x.reshape(side, side, -1)
    h = h.reshape(side, side // scale, -1)
    h = h.transpose(1, 0, 2)
    h = h.reshape(side // scale, side // scale, -1)
    h = h.transpose(1, 0, 2)
    return h.reshape((side // scale) ** 2, -1)


class VisionTowerOracle:
    """SmolVLM's vision tower and connector's forward pass in float32, on
    the host: the reference ``VisionTower`` (the device graph) is judged
    by, as a decoder's oracle is the decoder's.
    """

    def __init__(self, config: VisionConfig, weights):
        self.config = config
        self.weights = _widen(weights)

    def __call__(self, image: np.ndarray) -> np.ndarray:
        """``image``, ``(512, 512, 3)`` float32 in ``[-1, 1]`` (the real
        processor's mean/std of 0.5 both ways), to ``(64, text_dim)``
        image features, the connector's own output.
        """
        c, w = self.config, self.weights
        side = c.image_size // c.patch
        embed = w.vision_model.embeddings
        conv = Conv2d(embed.patch_embedding.weight, c.image_size, stride=c.patch)
        patches = conv.oracle(
            image.reshape(c.image_size, c.image_size * 3), embed.patch_embedding.weight
        )
        patches = patches.reshape(side * side, c.hidden) + embed.patch_embedding.bias
        x = patches + embed.position_embedding.weight
        for lw in w.vision_model.encoder.layers:
            x = self.layer(lw, x)
        x = layer_norm(
            x, w.vision_model.post_layernorm.weight, w.vision_model.post_layernorm.bias
        )
        x = pixel_shuffle(x, side, c.scale_factor)
        return x @ w.connector.modality_projection.proj.weight.T

    def layer(self, w, x):
        c = self.config
        h = layer_norm(x, w.layer_norm1.weight, w.layer_norm1.bias)
        x = x + self.attention(w, h)
        h = layer_norm(x, w.layer_norm2.weight, w.layer_norm2.bias)
        h = gelu_tanh(h @ w.mlp.fc1.weight.T + w.mlp.fc1.bias) @ w.mlp.fc2.weight.T
        h = h + w.mlp.fc2.bias
        return x + h

    def attention(self, w, h):
        c = self.config
        T, H, D = h.shape[0], c.n_heads, c.head_dim
        a = w.self_attn
        q = (h @ a.q_proj.weight.T + a.q_proj.bias).reshape(T, H, D).transpose(1, 0, 2)
        k = (h @ a.k_proj.weight.T + a.k_proj.bias).reshape(T, H, D).transpose(1, 0, 2)
        v = (h @ a.v_proj.weight.T + a.v_proj.bias).reshape(T, H, D).transpose(1, 0, 2)
        scores = (q @ k.transpose(0, 2, 1)) * (D**-0.5)
        weights = _softmax(scores)
        o = (weights @ v).transpose(1, 0, 2).reshape(T, H * D)
        return o @ a.out_proj.weight.T + a.out_proj.bias


def layer_norm(
    x: np.ndarray, weight: np.ndarray, bias: np.ndarray, eps: float = EPS
) -> np.ndarray:
    mean = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(var + eps) * weight + bias


def gelu_tanh(x: np.ndarray) -> np.ndarray:
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))


def _softmax(x: np.ndarray) -> np.ndarray:
    x = x - x.max(axis=-1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=-1, keepdims=True)


def _widen(weights):
    """``weights``, every array upcast to float32 (twice the checkpoint)."""
    if isinstance(weights, SimpleNamespace):
        return SimpleNamespace(**{k: _widen(v) for k, v in vars(weights).items()})
    if isinstance(weights, list):
        return [_widen(v) for v in weights]
    return np.asarray(weights, np.float32)


class VisionTower(SimpleNamespace):
    """The vision tower and connector, one compile for a 512x512 image,
    called in a graph's body (``SmolVLM``'s ``embed()``). A namespace, so
    the graph that holds it names its weights by their path.

    Args:
        config: The tower's shape.
        weights: The checkpoint's ``model`` subtree (``weights.model``):
            ``vision_model`` and ``connector`` are read here.
    """

    def __init__(self, config: VisionConfig, weights):
        self.config = config
        side = config.image_size // config.patch
        embed = weights.vision_model.embeddings
        self.patch_embed = Conv2d(
            embed.patch_embedding.weight, config.image_size, stride=config.patch
        )
        self.patch_bias = embed.patch_embedding.bias
        self.position = iron.weight(embed.position_embedding.weight)
        self.post_norm = weights.vision_model.post_layernorm
        self.layers = weights.vision_model.encoder.layers
        self.connector = weights.connector.modality_projection.proj.weight
        self.side = side

    def __call__(self, image):
        c = self.config
        side = self.side
        h = self.patch_embed(image, rows=side).reshape(side * side, c.hidden)
        h = RowwiseAdd.step(h, self.patch_bias)
        h = ElementwiseAdd.step(h, self.position)
        for w in self.layers:
            h = self.layer(w, h)
        h = affine_layer_norm(h, self.post_norm.weight, self.post_norm.bias)
        h = Copy.step(
            h, src=_pixel_shuffle_tap(side, c.scale_factor, c.hidden)
        ).reshape((side // c.scale_factor) ** 2, c.hidden * c.scale_factor**2)
        return GEMM.step(h, self.connector, b_col_maj=True, **ACCURATE)

    def layer(self, w, x):
        c = self.config
        h = affine_layer_norm(x, w.layer_norm1.weight, w.layer_norm1.bias)
        x = ElementwiseAdd.step(x, self.attention(w, h))
        h = affine_layer_norm(x, w.layer_norm2.weight, w.layer_norm2.bias)
        # hidden (768) is not a multiple of flm.GEMM's default k_tile (512);
        # hidden_dim (3072) is.
        a = w.self_attn
        h = GELU.step(project(h, w.mlp.fc1.weight, bias=w.mlp.fc1.bias, k_tile=256))
        h = project(h, w.mlp.fc2.weight, bias=w.mlp.fc2.bias)
        return ElementwiseAdd.step(x, h)

    def attention(self, w, h):
        c = self.config
        T, H, D = h.shape[0], c.n_heads, c.head_dim
        a = w.self_attn
        q = project(h, a.q_proj.weight, bias=a.q_proj.bias, k_tile=256).reshape(T, H, D)
        k = project(h, a.k_proj.weight, bias=a.k_proj.bias, k_tile=256).reshape(T, H, D)
        v = project(h, a.v_proj.weight, bias=a.v_proj.bias, k_tile=256).reshape(T, H, D)
        o = MHA.step(
            q,
            k,
            v,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
        )
        return project(
            o.reshape(T, H * D), a.out_proj.weight, bias=a.out_proj.bias, k_tile=256
        )


def affine_layer_norm(x, weight, bias):
    """``LayerNorm`` (gamma 1, beta 0) folded with the checkpoint's own
    weight and bias: ``RowwiseMul`` then ``RowwiseAdd``, the composition
    whisper-port's affine norms use (no library change: the plain
    ``LayerNorm`` and the elementwise rowwise ops already cover it).
    """
    return RowwiseAdd.step(RowwiseMul.step(LayerNorm.step(x), weight), bias)


def _pixel_shuffle_tap(side: int, scale: int, hidden: int):
    """The real connector's ``pixel_shuffle`` as one gather: patch
    ``(r, c)``'s channels end up at merged patch
    ``(r // scale, c // scale)``, ordered by ``(r % scale, c % scale)``
    within the merged channel block -- a ``Copy`` these strides reach,
    no data computed, only moved.
    """
    from aie.helpers.taplib import TensorAccessPattern

    rows = side // scale
    return TensorAccessPattern(
        (side, side * hidden),
        0,
        [rows, rows, scale, scale * hidden],
        [scale * side * hidden, scale * hidden, side * hidden, 1],
    )


class Vision(iron.Graph):
    """The vision tower and connector as a graph of its own, one compile
    for a 512x512 image: standalone (its own device test) and called
    inside ``SmolVLM``'s ``embed()`` once that is built.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: VisionConfig, weights):
        self.config = config
        self.tower = VisionTower(config, weights)

    def body(self, rgb):
        return self.tower(rgb)
