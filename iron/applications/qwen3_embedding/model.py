# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-Embedding on the NPU: Qwen3's decoder without its head, one graph
compiled once for every length up to a prompt chunk. A text's embedding is
its last token's final hidden state, unit length; the tokenizer's end of
text closes it, and a query goes behind its task's instruction.
"""

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.applications.qwen3.model import Qwen3
from iron.lm import Attention, DecoderConfig, DecoderLayer, Encoder, NoCache
from iron.lm import RMSNorm, rope_angles
from iron.operators.copy import Copy


class Qwen3EmbeddingLayer(DecoderLayer):
    """Qwen3's layer over a call's own rows, causally."""

    def __init__(self, c: DecoderConfig, i: int):
        attention = Attention(c, i, norms="qk", o_bias=c.attention_bias)
        super().__init__(c, i, attention, cache=NoCache(causal=True))
        self.rope = c.head_dim


class Qwen3Embedding(Encoder):
    """Qwen3-Embedding on ``config``'s shape over ``config.prefill_chunk``
    rows at most, from a checkpoint's ``weights`` (Qwen3's ``model``
    modules at its root). A call returns the last row's final hidden state.
    """

    config = DecoderConfig
    profile = Qwen3.profile
    layer_class = Qwen3EmbeddingLayer
    bos = Qwen3.bos

    def __init__(self, config: DecoderConfig, weights):
        c = config
        super().__init__(config, c.prefill_chunk)
        self.final_norm = RMSNorm(c.hidden_size, c.eps)
        self.load_layers(weights, "layers.", "norm.")
        self.table = weights.embed_tokens.weight
        angles = rope_angles(c.head_dim, c.prefill_chunk, c.rope_theta)
        self.rope = iron.weight(angles.astype(bfloat16))

    def lookup(self, ids):
        return Copy.step(iron.weight(self.table)[ids])

    def angles(self, n):
        return {self.config.head_dim: (self.rope[:n],) * 2}

    def pool(self, x, n):
        return Copy.step(x[n - 1]).reshape(1, self.config.hidden_size)

    def head(self, x):
        return x

    def embed(self, text: str, task: str | None = None) -> np.ndarray:
        """The unit-length embedding of ``text``, a query behind ``task``'s
        instruction where given, else a document, float32.
        """
        if task is not None:
            text = f"Instruct: {task}\nQuery:{text}"
        tokens = [*self.tokenizer.encoding.encode(text), self.bos]
        ids, values = self.inputs(tokens)
        y = np.asarray(self(ids, **values).numpy(), np.float32).reshape(-1)
        return y / np.linalg.norm(y)
