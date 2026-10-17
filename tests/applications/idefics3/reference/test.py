#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM's graphs against their own float32 forward passes, device-free
(no checkpoint, no NPU), at a toy shape: the vision tower on ``Layer``'s
SigLIP names.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.idefics3.vision.model import (
    VisionConfig,
    VisionOracle,
    VisionTower,
)
from iron.tests.common.llama_model import checkpoint

pytestmark = pytest.mark.usefixtures("npu2")

#: SmolVLM's vision tower at toy size: an 8x8 patch grid, shuffled 2x2.
VISION = VisionConfig(
    hidden=256,
    n_layers=2,
    n_heads=4,
    hidden_dim=512,
    patch=16,
    image_size=128,
    scale_factor=2,
    text_dim=256,
)


def vision_names(c: VisionConfig) -> dict[str, tuple[int, ...]]:
    """The vision tower's and connector's tensors of a checkpoint of ``c``'s
    shape, by name.
    """
    E, F = c.hidden, c.hidden_dim
    v = "model.vision_model"
    out = {
        f"{v}.embeddings.patch_embedding.weight": (E, 3, c.patch, c.patch),
        f"{v}.embeddings.patch_embedding.bias": (E,),
        f"{v}.embeddings.position_embedding.weight": (c.side**2, E),
        f"{v}.post_layernorm.weight": (E,),
        f"{v}.post_layernorm.bias": (E,),
        "model.connector.modality_projection.proj.weight": (
            c.text_dim,
            E * c.scale_factor**2,
        ),
    }
    for i in range(c.n_layers):
        p = f"{v}.encoder.layers.{i}"
        for norm in ("layer_norm1", "layer_norm2"):
            out |= {f"{p}.{norm}.weight": (E,), f"{p}.{norm}.bias": (E,)}
        for proj in ("q_proj", "k_proj", "v_proj", "out_proj"):
            out |= {
                f"{p}.self_attn.{proj}.weight": (E, E),
                f"{p}.self_attn.{proj}.bias": (E,),
            }
        out |= {
            f"{p}.mlp.fc1.weight": (F, E),
            f"{p}.mlp.fc1.bias": (F,),
            f"{p}.mlp.fc2.weight": (E, F),
            f"{p}.mlp.fc2.bias": (E,),
        }
    return out


def drawn(c: VisionConfig, seed: int):
    """A random tree of ``c``'s shape whose biases are drawn too, not ones,
    which every LayerNorm after them would cancel.
    """
    names = vision_names(c)
    tree = checkpoint(c, names).tree("random", seed)
    rng = np.random.default_rng(seed)
    for name, shape in names.items():
        if name.endswith(".bias"):
            *path, leaf = name.split(".")
            node = tree
            for part in path:
                node = node[int(part)] if part.isdigit() else vars(node)[part]
            setattr(node, leaf, (rng.standard_normal(shape) / 4).astype(bfloat16))
    return tree


def test_the_vision_tower_s_soft_tokens_match_its_oracle():
    """The tower's reference against ``VisionOracle``: bf16 against float32,
    LayerNorm at the kernel's 1e-5 against the checkpoint's 1e-6, so within
    5% of the largest soft token's magnitude, as a decoder's logits are held
    (three seeds measure 0.6-0.7%).
    """
    weights = drawn(VISION, 0)
    tower = VisionTower(VISION, weights)
    rng = np.random.default_rng(1)
    image = rng.uniform(-1, 1, (VISION.image_size, VISION.image_size, 3))
    buffer, values = tower.inputs(image)
    got = np.asarray(tower.reference(buffer, **values), np.float32)
    want = VisionOracle(VISION, weights).soft_tokens(buffer.astype(np.float32))
    assert got.shape == (tower.soft_rows, VISION.text_dim)
    err, scale = np.abs(got - want).max(), np.abs(want).max()
    assert err <= 0.05 * scale, f"|diff| {err:.4f} against |soft tokens| {scale:.3f}"
