#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B over the shared decoder and layer (``iron.lm``): its
embedding and head on the NPU (``Granite``) and on the CPU in float32
(``GraniteOracle``, the reference it is judged by), and its shape, read from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.granite.model``.

Granite is Llama's layer with four scalars of its own config's: the
attention logits scale by ``attention_multiplier`` rather than ``1 /
sqrt(head_dim)``, each block's output joins its residual times
``residual_multiplier`` (both ``Layer``'s), the embedding rows are scaled
by ``embedding_multiplier`` and the logits divided by ``logits_scaling``.
Its output head is untied (``lm_head``). Its checkpoint is sharded;
``Checkpoint`` reads the index.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Granite 4.2 3B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone.
"""

import dataclasses
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron import lm
from iron.lm import CausalLM, DecoderConfig, Derived, Layer, Oracle, widen
from iron.operators.elementwise_mul import RowwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm


@dataclasses.dataclass(frozen=True)
class GraniteConfig(DecoderConfig):
    """``DecoderConfig`` and Granite's own four scalars."""

    attention_multiplier: float = dataclasses.field(
        kw_only=True, metadata={"json": "attention_multiplier"}
    )
    residual_multiplier: float = dataclasses.field(
        default=1.0, kw_only=True, metadata={"json": "residual_multiplier"}
    )
    embedding_multiplier: float = dataclasses.field(
        default=1.0, kw_only=True, metadata={"json": "embedding_multiplier"}
    )
    logits_scaling: float = dataclasses.field(
        default=1.0, kw_only=True, metadata={"json": "logits_scaling"}
    )

    def layer(self, i: int) -> Layer:
        return dataclasses.replace(
            super().layer(i),
            scale=self.attention_multiplier,
            residual=self.residual_multiplier,
        )


class GraniteOracle(Oracle):
    """Granite's forward pass in float32, on the host."""

    def embed(self, x):
        return x * np.float32(self.config.embedding_multiplier)

    def head(self, x):
        norm = widen(self.weights.model.norm.weight)
        lm_head = widen(self.weights.lm_head.weight)
        logits = self.rms_norm(x, norm) @ lm_head.T
        return logits / np.float32(self.config.logits_scaling)


class Granite(CausalLM):
    """Granite on ``config``'s shape and a checkpoint's ``weights``, by its
    names: the (untied) output head is ``lm_head``. Every matrix is read
    ``(out, in)``, as the checkpoint ships it: GEMV's ``(M, K)`` and GEMM's
    column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = GraniteOracle

    def __init__(self, config: GraniteConfig, weights):
        super().__init__(config, weights)
        derived = Derived(weights)
        model = weights.model
        if config.embedding_multiplier != 1:
            m = config.embedding_multiplier
            derived.put(
                model.embed_tokens, scale=np.full(config.hidden_size, m, bfloat16)
            )
        if config.logits_scaling != 1:
            # The logits' divisor folded into the final norm's weight.
            divided = model.norm.weight / bfloat16(config.logits_scaling)
            derived.put(model.norm, divided=divided)
        self.derived = derived.tree()

    def embed(self, x):
        if self.config.embedding_multiplier == 1:
            return x
        return RowwiseMul.step(x, self.derived.model.embed_tokens.scale)

    def head(self, x):
        norm = self.weights.model.norm.weight
        if self.config.logits_scaling != 1:
            norm = self.derived.model.norm.divided
        return GEMV.step(
            self.weights.lm_head.weight,
            RMSNorm.step(x, weight=norm, epsilon=self.config.eps),
        )


class Runner(lm.Runner):
    """Granite 4.2 3B, from its sharded checkpoint and ``tokenizer.json``."""

    config = GraniteConfig
    model = Granite
    bos = 100283  # "<s>"; eos/pad is "<|im_end|>" = 100257


if __name__ == "__main__":
    lm.main(Runner, "Granite 4.2 3B on the NPU")
