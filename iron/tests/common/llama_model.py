# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's shape at a size a host test runs in seconds, its weights
drawn or unread from a checkpoint of that shape written here."""

import dataclasses
import hashlib
import json
import math
import struct
import tempfile
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron.common import Profile
from iron.lm import Checkpoint, DecoderConfig
from iron.applications.llama.model import Llama, Llama3RopeScaling, LlamaConfig

# The tunables the graph runs with at ``SMALL``'s shape on NPU2: decode
# and the prompt at 256 rows. The application's own profiles are for Llama
# 1B's shape, which ``llama_1b`` runs under.
PROFILE = Profile.load(Path(__file__).with_name("llama_small_profile.json"))

#: Llama 3.2 1B's own rope_base and eps (meta-llama/Llama-3.2-1B's published
#: config.json): not the checkpoint, which these tests never read, but the
#: two numbers ``SMALL`` and ``llama_1b`` keep to be Llama 3.2's own shape.
_ROPE_BASE, _EPS = 500000.0, 1e-5

#: Llama 3.2 1B's real shape, for builds the real checkpoint's config.json
#: would otherwise give (``llama_1b``, and ``SMALL``'s inherited fields).
REAL_1B = LlamaConfig(
    vocab_size=128256,
    emb_dim=2048,
    n_layers=16,
    n_heads=32,
    n_kv_groups=8,
    head_dim=64,
    hidden_dim=8192,
    rope_base=_ROPE_BASE,
    eps=_EPS,
    rope_scaling=Llama3RopeScaling(
        factor=32.0,
        low_freq_factor=1.0,
        high_freq_factor=4.0,
        original_max_position_embeddings=8192,
    ),
)

#: Llama's shape, small, and its RoPE table unscaled.
SMALL = dataclasses.replace(
    REAL_1B,
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

# A run's checkpoints, one a shape, removed when the process exits.
CHECKPOINTS = tempfile.TemporaryDirectory(prefix="iron-llama-")


def shapes(config: DecoderConfig) -> dict[str, tuple[int, ...]]:
    """Each tensor of a Hugging Face Llama checkpoint of ``config``'s shape,
    by name: the model's own, then each layer's.
    """
    c = config
    E, F, V = c.emb_dim, c.hidden_dim, c.vocab_size
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    out = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(c.n_layers):
        layer = f"model.layers.{i}"
        out |= {
            f"{layer}.input_layernorm.weight": (E,),
            f"{layer}.self_attn.q_proj.weight": (Q, E),
            f"{layer}.self_attn.k_proj.weight": (KV, E),
            f"{layer}.self_attn.v_proj.weight": (KV, E),
            f"{layer}.self_attn.o_proj.weight": (E, Q),
            f"{layer}.post_attention_layernorm.weight": (E,),
            f"{layer}.mlp.gate_proj.weight": (F, E),
            f"{layer}.mlp.up_proj.weight": (F, E),
            f"{layer}.mlp.down_proj.weight": (E, F),
        }
    return out


def checkpoint(config: DecoderConfig) -> Checkpoint:
    """A ``.safetensors`` checkpoint of ``config``'s shape, every tensor bf16
    zeros, written once a shape. The file is sparse: its header and a hole,
    which neither a random nor an unread tree reads.
    """
    named = shapes(config)
    digest = hashlib.sha256(json.dumps(named).encode()).hexdigest()[:16]
    path = Path(CHECKPOINTS.name) / f"{digest}.safetensors"
    if not path.exists():
        header, end = {}, 0
        for name, shape in named.items():
            size = math.prod(shape) * np.dtype(bfloat16).itemsize
            header[name] = {
                "dtype": "BF16",
                "shape": shape,
                "data_offsets": [end, end + size],
            }
            end += size
        blob = json.dumps(header).encode()
        blob += b" " * (-len(blob) % 8)
        with open(path, "wb") as f:
            f.write(struct.pack("<Q", len(blob)) + blob)
            f.truncate(8 + len(blob) + end)
    return Checkpoint(path)


def small(seed=0, **config) -> Llama:
    """The model at ``SMALL``'s shape, as changed by ``config``, under
    ``PROFILE``, its weights drawn at ``seed``.
    """
    config = dataclasses.replace(SMALL, **config)
    model = Llama(config, checkpoint(config).tree("random", seed))
    model.profile = PROFILE
    return model


def llama_1b(n_layers=16) -> Llama:
    """Llama 3.2 1B's real shape with unset weights: for builds, not numbers.

    ``n_layers`` below 16 builds a shallower model of the same layer: the
    designs are the same at any depth.
    """
    config = dataclasses.replace(REAL_1B, n_layers=n_layers)
    return Llama(config, checkpoint(config).tree("unread"))
