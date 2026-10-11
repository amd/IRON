#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B, an application built on ``iron.lm``: its layer is the
library's shared ``Block``/``BlockOracle`` (``iron.lm.blocks``, also
Llama 3's), so ``Granite`` and ``GraniteOracle`` mix those in alongside
``CausalLM``/``Oracle`` and add only Granite's own Config, q-scale fold,
untied head, tokenizer and sharded checkpoint.
Run it with ``python -m iron.applications.granite.model``.

Granite's checkpoint ships as two shards (``Checkpoint`` maps the index
beside them) and its attention does not scale by ``1/sqrt(head_dim)``, the
library's hardcoded ``MHA``/``attend`` scale, but by its own
``attention_multiplier``; ``Runner`` folds the difference into every
layer's ``q`` once after loading (``Q_FOLD``), so the model and the oracle
share it without a library change.
"""

from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16
from tokenizers import Tokenizer

import iron
from iron import lm
from iron.common.graph.handle import Weight
from iron.lm import Block, BlockOracle, CausalLM, Config, Layout, Oracle, rms_norm
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm

GRANITE_4_2_3B = Config(
    vocab_size=100352,
    emb_dim=2560,
    n_layers=40,
    n_heads=40,
    n_kv_groups=8,
    head_dim=64,
    hidden_dim=8192,
    max_seq_len=32768,
    rope_base=1e7,
)

# Granite's attention_multiplier (1/64) over the library's hardcoded
# MHA/attend scale (1/sqrt(64) = 0.125): folded into every layer's q once,
# in Runner.__init__. Exact: a power of two only shifts bf16 exponents.
Q_FOLD = bfloat16(0.125)


class GraniteOracle(BlockOracle, Oracle):
    """Granite's float32 forward pass: the shared block's layer, its own head."""

    lm_head: np.ndarray

    def head(self, x):
        return rms_norm(x, self.norm) @ self.lm_head.T


class Granite(Block, CausalLM):
    """Granite 4.2 3B on the NPU: the shared block's layer, its own
    (untied) head."""

    profile = Path(__file__).with_name("profiles")
    oracle = GraniteOracle
    lm_head: Weight

    def __init__(self, config: Config, weights):
        super().__init__(config, weights)
        self.lm_head = iron.weight(weights.lm_head)

    def head(self, x):
        return GEMV(self.lm_head, RMSNorm(x, weight=self.norm))


def layout(config: Config) -> Layout:
    """Each weight's place in ``Granite``, its name in a Hugging Face
    checkpoint and its shape: Llama's layout, plus its own output head.
    The tree path is ``lm_head``, not ``head``: ``CausalLM``/``Oracle``
    already define a ``head()`` method, which the weight would overwrite.
    """
    c = config
    E, F, V = c.emb_dim, c.hidden_dim, c.vocab_size
    Q, KV = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    layer = "model.layers.{i}"
    return {
        "embedding": ("model.embed_tokens.weight", (V, E)),
        "norm": ("model.norm.weight", (E,)),
        "lm_head": ("lm_head.weight", (V, E)),
        "layers.{i}.norm1": (f"{layer}.input_layernorm.weight", (E,)),
        "layers.{i}.q": (f"{layer}.self_attn.q_proj.weight", (Q, E)),
        "layers.{i}.k": (f"{layer}.self_attn.k_proj.weight", (KV, E)),
        "layers.{i}.v": (f"{layer}.self_attn.v_proj.weight", (KV, E)),
        "layers.{i}.o": (f"{layer}.self_attn.o_proj.weight", (E, Q)),
        "layers.{i}.norm2": (f"{layer}.post_attention_layernorm.weight", (E,)),
        "layers.{i}.gate": (f"{layer}.mlp.gate_proj.weight", (F, E)),
        "layers.{i}.up": (f"{layer}.mlp.up_proj.weight", (F, E)),
        "layers.{i}.down": (f"{layer}.mlp.down_proj.weight", (E, F)),
    }


def tokenizer(path) -> Tokenizer:
    """Granite's tokenizer, from its ``tokenizer.json``; its own ``encode``
    adds no special tokens (``Runner.encode`` prepends BOS itself)."""
    return Tokenizer.from_file(str(path))


class Runner(lm.Runner):
    """Granite 4.2 3B, from its sharded checkpoint and ``tokenizer.json``."""

    config = GRANITE_4_2_3B
    layout = staticmethod(layout)
    model = Granite
    open_tokenizer = staticmethod(tokenizer)
    bos = 100283  # "<s>"; eos/pad is "<|im_end|>" = 100257

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for layer in self.weights.layers:
            layer.q = layer.q * Q_FOLD

    def encode(self, text: str) -> list[int]:
        return [self.bos, *self.tokenizer.encode(text, add_special_tokens=False).ids]


if __name__ == "__main__":
    lm.main(Runner, "Granite 4.2 3B on the NPU")
