# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's shape at a size a host test runs in seconds, as numpy weights."""

from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron.applications.llama_3_2_1b.weights import LayerWeights, LlamaWeights
from iron.common import Profile
from iron.operators.rope.op import rope_angles

# The knobs the graphs run with at :class:`Config`'s shape on NPU2: decode
# at 256 and 64 rows of context, the prompt at 64. The application's own
# profiles are for Llama 1B's shape; :class:`Llama1B` runs under those.
PROFILE = Profile.load(Path(__file__).with_name("llama_small_profile.json"))


def _shapes(cfg):
    """Each LayerWeights field's shape, ``(out, in)`` for a matrix."""
    E, F = cfg.emb_dim, cfg.hidden_dim
    Q, KV = cfg.n_heads * cfg.head_dim, cfg.n_kv_groups * cfg.head_dim
    return {
        "norm1": (E,),
        "q": (Q, E),
        "k": (KV, E),
        "v": (KV, E),
        "o": (E, Q),
        "norm2": (E,),
        "gate": (F, E),
        "up": (F, E),
        "down": (E, F),
    }


class Config:
    """Llama's shape, small, with the weights drawn at a seed.

    ``weights`` is the :class:`LlamaWeights` the graphs close over and the
    float32 reference (``cpu.Reference``) reads; ``angles`` is the RoPE
    table for ``context_length``, in bf16. Each projection is drawn uniform
    in ``+-1/sqrt(in)``, each norm weight is one.
    """

    n_layers, n_heads, n_kv_groups, head_dim = 2, 16, 4, 64
    emb_dim, hidden_dim, vocab_size = 256, 512, 1024
    context_length = 64

    def __init__(self, seed=0):
        rng = np.random.default_rng(seed)

        def draw(shape):
            if len(shape) == 1:
                return np.ones(shape, dtype=bfloat16)
            bound = 1.0 / np.sqrt(shape[1])
            return rng.uniform(-bound, bound, shape).astype(bfloat16)

        shapes = _shapes(self)
        self.weights = LlamaWeights(
            embedding=draw((self.vocab_size, self.emb_dim)),
            norm=draw((self.emb_dim,)),
            layers=tuple(
                LayerWeights(**{f: draw(s) for f, s in shapes.items()})
                for _ in range(self.n_layers)
            ),
        )
        self.angles = rope_angles(self.head_dim, self.context_length).astype(bfloat16)


class Llama1B(Config):
    """Llama 3.2 1B's real shape with unset weights: for builds, not numbers.

    Each array is ``np.empty``, so the 2.5 GB is reserved and never
    touched. ``n_layers`` below 16 builds a shallower model of the same
    layer: the designs are the same at any depth.
    """

    n_layers, n_heads, n_kv_groups, head_dim = 16, 32, 8, 64
    emb_dim, hidden_dim, vocab_size = 2048, 8192, 128256
    context_length = 2048

    def __init__(self, n_layers=16):
        self.n_layers = n_layers
        shapes = _shapes(self)
        self.weights = LlamaWeights(
            embedding=np.empty((self.vocab_size, self.emb_dim), dtype=bfloat16),
            norm=np.empty((self.emb_dim,), dtype=bfloat16),
            layers=tuple(
                LayerWeights(
                    **{f: np.empty(s, dtype=bfloat16) for f, s in shapes.items()}
                )
                for _ in range(n_layers)
            ),
        )
        self.angles = rope_angles(self.head_dim, self.context_length).astype(bfloat16)
