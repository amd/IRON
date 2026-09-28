# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's shape at a size a host test runs in seconds, as numpy weights."""

import dataclasses
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron.common import Profile
from iron.lm import checkpoint_shapes, load_weights
from iron.lm.llama3.model import LLAMA_3_2_1B, Llama, layout

# The tunables the graph runs with at :data:`SMALL`'s shape on NPU2: decode
# at 256 and 64 rows of context, the prompt at 64. The application's own
# profiles are for Llama 1B's shape, which :func:`llama_1b` runs under.
PROFILE = Profile.load(Path(__file__).with_name("llama_small_profile.json"))

#: Llama's shape, small, and its RoPE table unscaled.
SMALL = dataclasses.replace(
    LLAMA_3_2_1B,
    vocab_size=1024,
    emb_dim=256,
    n_layers=2,
    n_heads=16,
    n_kv_groups=4,
    head_dim=64,
    hidden_dim=512,
    max_seq_len=64,
    prefill_chunk=64,
    rope_scaling=None,
)


def random_weights(config, seed=0):
    """``config``'s weights through the checkpoint's names, drawn at ``seed``:
    each matrix uniform in ``+-1/sqrt(in)``, each norm weight one.
    """
    rng = np.random.default_rng(seed)

    def draw(shape):
        if len(shape) == 1:
            return np.ones(shape, dtype=bfloat16)
        bound = 1.0 / np.sqrt(shape[1])
        return rng.uniform(-bound, bound, shape).astype(bfloat16)

    shapes = checkpoint_shapes(layout(config), config.n_layers)
    tensors = {k: draw(s) for k, s in shapes.items()}
    return load_weights(tensors, layout(config), config.n_layers)


def small(seed=0, **config) -> Llama:
    """The model at :data:`SMALL`'s shape, as changed by ``config``, under
    :data:`PROFILE`.
    """
    config = dataclasses.replace(SMALL, **config)
    model = Llama(config, random_weights(config, seed))
    model.profile = PROFILE
    return model


def llama_1b(n_layers=16) -> Llama:
    """Llama 3.2 1B's real shape with unset weights: for builds, not numbers.

    Each array is ``np.empty``, so the 2.5 GB is reserved and never
    touched. ``n_layers`` below 16 builds a shallower model of the same
    layer: the designs are the same at any depth.
    """
    config = dataclasses.replace(LLAMA_3_2_1B, n_layers=n_layers)
    shapes = checkpoint_shapes(layout(config), n_layers)
    tensors = {k: np.empty(s, dtype=bfloat16) for k, s in shapes.items()}
    return Llama(config, load_weights(tensors, layout(config), n_layers))
