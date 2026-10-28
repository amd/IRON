# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B over the shared decoder and layer (``iron.lm``): its
embedding and head on the NPU (``Granite``) and its shape, read from its
checkpoint's ``config.json``. Run with ``python -m
iron.applications.granite.model``.

Granite is Llama's layer with four scalars from its config: attention
scaled by ``attention_multiplier``, each block's residual by
``residual_multiplier`` (``GraniteLayer``), the embedding rows by
``embedding_multiplier`` and the logits by ``logits_scaling``. Its head is
untied (``lm_head``); its checkpoint is sharded.

Tunables are keyed by operator shape in ``profiles/<device>.json``, at
Granite 4.2 3B's: a decode step's and a 2048-row prompt chunk's.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron import Precision, lm, param
from iron.lm import CausalLM, DecoderConfig, DecoderLayer


@dataclasses.dataclass(frozen=True)
class GraniteConfig(DecoderConfig):
    """``DecoderConfig``, Granite's own four scalars, and every
    projection's ``precision``.
    """

    attention_multiplier: float = dataclasses.field(kw_only=True)
    residual_multiplier: float = dataclasses.field(default=1.0, kw_only=True)
    embedding_multiplier: float = dataclasses.field(default=1.0, kw_only=True)
    logits_scaling: float = dataclasses.field(default=1.0, kw_only=True)
    # 4.2-3B's prompt over two chunks needs bf16 macs on its projections, as
    # Llama 3B's does (decision 40).
    precision: Precision = lm.not_json(Precision.HIGH, kw_only=True)


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
    """Granite on ``config``'s shape and a checkpoint's ``weights``: the
    untied output head is ``lm_head``, every matrix read ``(out, in)`` as
    the checkpoint ships it. From its sharded checkpoint and
    ``tokenizer.json``.
    """

    config = GraniteConfig
    profile = Path(__file__).with_name("profiles")
    layer_class = GraniteLayer

    def __init__(self, config: GraniteConfig, weights):
        super().__init__(config, weights)
        # The embedding's multiplier as a row every row is multiplied by.
        m = config.embedding_multiplier
        self.embed_scale = param(np.full(config.hidden_size, m, bfloat16))
        if config.logits_scaling != 1:
            # The logits' divisor folded into the final norm's loaded weight.
            norm = self.model.norm
            norm.weight = param(norm.weight / bfloat16(config.logits_scaling))

    def lookup(self, ids):
        x = super().lookup(ids)
        if self.config.embedding_multiplier == 1:
            return x
        E = self.config.hidden_size
        x = x.reshape(math.prod(x.shape) // E, E)
        return x * self.embed_scale


if __name__ == "__main__":
    lm.main(Granite)
