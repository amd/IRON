# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's shape at a size a host test runs in seconds, as numpy weights."""

import dataclasses
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron.common import Profile
from iron.lm import checkpoint_shapes, load_weights, random_weights
from iron.lm.llama3.model import LLAMA_3_2_1B, Llama, layout

# The tunables the graph runs with at ``SMALL``'s shape on NPU2: decode
# and the prompt at 256 rows. The application's own profiles are for Llama
# 1B's shape, which ``llama_1b`` runs under.
PROFILE = Profile.load(Path(__file__).with_name("llama_small_profile.json"))

#: Llama's shape, small, and its RoPE table unscaled.
SMALL = dataclasses.replace(
    LLAMA_3_2_1B,
    vocab_size=1024,
    emb_dim=512,
    n_layers=2,
    n_heads=16,
    n_kv_groups=4,
    head_dim=64,
    hidden_dim=2048,
    max_seq_len=256,
    prefill_chunk=256,
    rope_scaling=None,
)


def small(seed=0, **config) -> Llama:
    """The model at ``SMALL``'s shape, as changed by ``config``, under
    ``PROFILE``.
    """
    config = dataclasses.replace(SMALL, **config)
    model = Llama(config, random_weights(layout(config), config.n_layers, seed))
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
