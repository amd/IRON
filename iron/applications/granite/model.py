#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B over the shared decoder and layer (``iron.lm``): its
embedding and head on the NPU (``Granite``) and its shape, read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.granite.model``.

Granite is Llama's layer with four scalars of its own config's: the
attention logits scale by ``attention_multiplier`` rather than ``1 /
sqrt(head_dim)``, each block's output joins its residual times
``residual_multiplier`` (``GraniteLayer``), the embedding rows are scaled
by ``embedding_multiplier`` and the logits divided by ``logits_scaling``,
folded into the final norm's weight once it loads.
Its output head is untied (``lm_head``). Its checkpoint is sharded;
``Checkpoint`` reads the index.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Granite 4.2 3B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron import lm
from iron.lm import CausalLM, DecoderConfig, DecoderLayer


@dataclasses.dataclass(frozen=True)
class GraniteConfig(DecoderConfig):
    """``DecoderConfig`` and Granite's own four scalars."""

    attention_multiplier: float = dataclasses.field(kw_only=True)
    residual_multiplier: float = dataclasses.field(default=1.0, kw_only=True)
    embedding_multiplier: float = dataclasses.field(default=1.0, kw_only=True)
    logits_scaling: float = dataclasses.field(default=1.0, kw_only=True)


class GraniteLayer(DecoderLayer):
    """Llama's layer, its attention logits scaled by
    ``attention_multiplier`` and each block's output by
    ``residual_multiplier``.
    """

    def __init__(self, c: GraniteConfig, i: int):
        super().__init__(c, i)
        self.self_attn.scaling = c.attention_multiplier
        self.residual_multiplier = c.residual_multiplier


class Granite(CausalLM):
    """Granite on ``config``'s shape and a checkpoint's ``weights``, by its
    names: the (untied) output head is ``lm_head``. Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B. From its sharded checkpoint and ``tokenizer.json``.
    """

    config = GraniteConfig
    profile = Path(__file__).with_name("profiles")
    layer_class = GraniteLayer
    bos = 100283  # "<s>"; eos/pad is "<|im_end|>" = 100257

    def __init__(self, config: GraniteConfig, weights):
        super().__init__(config, weights)
        # The embedding's multiplier as a row every row is multiplied by.
        m = config.embedding_multiplier
        self.embed_scale = np.full(config.hidden_size, m, bfloat16)
        if config.logits_scaling != 1:
            # The logits' divisor folded into the final norm's loaded weight.
            norm = self.model.norm
            norm.weight = norm.weight / bfloat16(config.logits_scaling)

    def lookup(self, ids):
        x = super().lookup(ids)
        if self.config.embedding_multiplier == 1:
            return x
        E = self.config.hidden_size
        x = x.reshape(math.prod(x.shape) // E, E)
        return x * self.embed_scale


if __name__ == "__main__":
    lm.main(Granite)
