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
host step is the lighter touch for this first pass, flagged, not hidden:
`skill-gaps.md`). The patch grid is then whole (32x32, 1024 patches), so
each patch's absolute position embedding is simply its raster index,
``row * 32 + col`` -- the real processor's bucketized, padding-aware
position ids reduce to this when every patch is real and the grid is
square, which it always is here.

Unlike EmbeddingGemma 2's tower (RMSNorm, RoPE, q/k-norm, pooled soft
tokens), this one is unpooled (each patch is its own token until the
connector's pixel-shuffle, after every layer) and its norm is affine
LayerNorm (weight *and* bias, not RMSNorm): composed from the library's
``LayerNorm`` (gamma 1, beta 0) with ``RowwiseMul``/``RowwiseAdd``, the
same composition whisper-port's encoder uses.
"""

from pathlib import Path
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.lm import Conv2d, Layout, project
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd, RowwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.layer_norm import LayerNorm
from iron.operators.mha import MHA

# Each product's float32 sum rounded once.
ACCURATE = dict(prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False)


class VisionConfig:
    hidden = 768
    n_layers = 12
    n_heads = 12
    head_dim = 64
    hidden_dim = 3072
    patch = 16
    image_size = 512
    # The kernel's own layer_norm is eps=1e-5, fixed; the checkpoint's own
    # is 1e-6 (negligible past bf16, verified against the oracle).
    scale_factor = 4
    text_dim = 576


VISION = VisionConfig()


def layout(config: VisionConfig) -> Layout:
    """Each weight's place in the tower and the connector, its name in a
    Hugging Face checkpoint and its shape.
    """
    c = config
    E, F = c.hidden, c.hidden_dim
    P = c.patch
    layer = "model.vision_model.encoder.layers.{i}"
    return {
        "patch_embed.weight": (
            "model.vision_model.embeddings.patch_embedding.weight",
            (E, 3, P, P),
        ),
        "patch_embed.bias": (
            "model.vision_model.embeddings.patch_embedding.bias",
            (E,),
        ),
        "position": (
            "model.vision_model.embeddings.position_embedding.weight",
            (1024, E),
        ),
        "post_norm.weight": ("model.vision_model.post_layernorm.weight", (E,)),
        "post_norm.bias": ("model.vision_model.post_layernorm.bias", (E,)),
        "layers.{i}.norm1.weight": (f"{layer}.layer_norm1.weight", (E,)),
        "layers.{i}.norm1.bias": (f"{layer}.layer_norm1.bias", (E,)),
        "layers.{i}.q": (f"{layer}.self_attn.q_proj.weight", (E, E)),
        "layers.{i}.q_bias": (f"{layer}.self_attn.q_proj.bias", (E,)),
        "layers.{i}.k": (f"{layer}.self_attn.k_proj.weight", (E, E)),
        "layers.{i}.k_bias": (f"{layer}.self_attn.k_proj.bias", (E,)),
        "layers.{i}.v": (f"{layer}.self_attn.v_proj.weight", (E, E)),
        "layers.{i}.v_bias": (f"{layer}.self_attn.v_proj.bias", (E,)),
        "layers.{i}.o": (f"{layer}.self_attn.out_proj.weight", (E, E)),
        "layers.{i}.o_bias": (f"{layer}.self_attn.out_proj.bias", (E,)),
        "layers.{i}.norm2.weight": (f"{layer}.layer_norm2.weight", (E,)),
        "layers.{i}.norm2.bias": (f"{layer}.layer_norm2.bias", (E,)),
        "layers.{i}.fc1": (f"{layer}.mlp.fc1.weight", (F, E)),
        "layers.{i}.fc1_bias": (f"{layer}.mlp.fc1.bias", (F,)),
        "layers.{i}.fc2": (f"{layer}.mlp.fc2.weight", (E, F)),
        "layers.{i}.fc2_bias": (f"{layer}.mlp.fc2.bias", (E,)),
        "connector": (
            "model.connector.modality_projection.proj.weight",
            (c.text_dim, E * c.scale_factor**2),
        ),
    }


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
        conv = Conv2d(w.patch_embed.weight, c.image_size, stride=c.patch)
        patches = conv.exact(
            image.reshape(c.image_size, c.image_size * 3), w.patch_embed.weight
        )
        patches = patches.reshape(side * side, c.hidden) + w.patch_embed.bias
        x = patches + w.position
        for lw in w.layers:
            x = self.layer(lw, x)
        x = layer_norm(x, w.post_norm.weight, w.post_norm.bias)
        x = pixel_shuffle(x, side, c.scale_factor)
        return x @ w.connector.T

    def layer(self, w, x):
        c = self.config
        h = layer_norm(x, w.norm1.weight, w.norm1.bias)
        x = x + self.attention(w, h)
        h = layer_norm(x, w.norm2.weight, w.norm2.bias)
        h = gelu_tanh(h @ w.fc1.T + w.fc1_bias) @ w.fc2.T + w.fc2_bias
        return x + h

    def attention(self, w, h):
        c = self.config
        T, H, D = h.shape[0], c.n_heads, c.head_dim
        q = (h @ w.q.T + w.q_bias).reshape(T, H, D).transpose(1, 0, 2)
        k = (h @ w.k.T + w.k_bias).reshape(T, H, D).transpose(1, 0, 2)
        v = (h @ w.v.T + w.v_bias).reshape(T, H, D).transpose(1, 0, 2)
        scores = (q @ k.transpose(0, 2, 1)) * (D**-0.5)
        weights = _softmax(scores)
        o = (weights @ v).transpose(1, 0, 2).reshape(T, H * D)
        return o @ w.o.T + w.o_bias


def layer_norm(
    x: np.ndarray, weight: np.ndarray, bias: np.ndarray, eps=1e-6
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
    """

    def __init__(self, config: VisionConfig, weights):
        self.config = config
        side = config.image_size // config.patch
        self.patch_embed = Conv2d(
            weights.patch_embed.weight, config.image_size, stride=config.patch
        )
        self.patch_bias = weights.patch_embed.bias
        self.position = iron.weight(weights.position)
        self.post_norm = weights.post_norm
        self.layers = weights.layers
        self.connector = weights.connector
        self.side = side

    def __call__(self, image):
        c = self.config
        side = self.side
        h = self.patch_embed(image, rows=side).reshape(side * side, c.hidden)
        h = RowwiseAdd(h, self.patch_bias)
        h = ElementwiseAdd(h, self.position)
        for w in self.layers:
            h = self.layer(w, h)
        h = affine_layer_norm(h, self.post_norm.weight, self.post_norm.bias)
        h = Copy(h, src=_pixel_shuffle_tap(side, c.scale_factor, c.hidden)).reshape(
            (side // c.scale_factor) ** 2, c.hidden * c.scale_factor**2
        )
        return GEMM(h, self.connector, b_col_maj=True, **ACCURATE)

    def layer(self, w, x):
        c = self.config
        h = affine_layer_norm(x, w.norm1.weight, w.norm1.bias)
        x = ElementwiseAdd(x, self.attention(w, h))
        h = affine_layer_norm(x, w.norm2.weight, w.norm2.bias)
        # hidden (768) is not a multiple of flm.GEMM's default k_tile (512);
        # hidden_dim (3072) is.
        h = GELU(project(h, w.fc1, bias=w.fc1_bias, k_tile=256))
        h = project(h, w.fc2, bias=w.fc2_bias)
        return ElementwiseAdd(x, h)

    def attention(self, w, h):
        c = self.config
        T, H, D = h.shape[0], c.n_heads, c.head_dim
        q = project(h, w.q, bias=w.q_bias, k_tile=256).reshape(T, H, D)
        k = project(h, w.k, bias=w.k_bias, k_tile=256).reshape(T, H, D)
        v = project(h, w.v, bias=w.v_bias, k_tile=256).reshape(T, H, D)
        o = MHA(
            q,
            k,
            v,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
        )
        return project(o.reshape(T, H * D), w.o, bias=w.o_bias, k_tile=256)


def affine_layer_norm(x, weight, bias):
    """``LayerNorm`` (gamma 1, beta 0) folded with the checkpoint's own
    weight and bias: ``RowwiseMul`` then ``RowwiseAdd``, the composition
    whisper-port's affine norms use (no library change: the plain
    ``LayerNorm`` and the elementwise rowwise ops already cover it).
    """
    return RowwiseAdd(RowwiseMul(LayerNorm(x), weight), bias)


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
