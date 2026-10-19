# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Encoders and a tower of self-attention, and numpy's attention to judge them."""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.lm import Encoder, NoCache, Tower
from iron.operators.copy import Copy

ROWS, VOCAB, HEADS, HEAD_DIM = 128, 32, 2, 64


@dataclasses.dataclass(frozen=True)
class Shape:
    vocab_size: int = VOCAB
    hidden_size: int = HEADS * HEAD_DIM
    text_dim: int = HEADS * HEAD_DIM
    num_hidden_layers: int = 1
    num_attention_heads: int = HEADS
    window: int | None = None
    scale: float | None = None


class SelfAttend(iron.Graph):
    """A layer of the rows attending to themselves per head, within the
    config's ``window``, the logits scaled by its ``scale``."""

    def __init__(self, c, i: int):
        self.heads, self.scale = c.num_attention_heads, c.scale
        self.cache = NoCache(c.window)

    def body(self, x, step):
        n, E = x.shape
        q = x.reshape(n, self.heads, E // self.heads)
        return self.cache.attend(step, q, q, q, scale=self.scale)


class SelfAttention(Encoder):
    """Each layer the rows attending to themselves, unscaled, within
    ``window`` positions."""

    layer_class = SelfAttend

    def __init__(self, table, layers: int, window: int | None = None):
        self.table = table
        self.window = window
        super().__init__(
            Shape(num_hidden_layers=layers, window=window, scale=1.0), ROWS
        )

    def lookup(self, ids):
        return Copy.step(iron.weight(self.table)[ids])

    def head(self, x):
        return x


class Rows(Tower):
    """A tower whose front end is the rows it is given, one soft token each."""

    layer_class = SelfAttend

    def __init__(self):
        super().__init__(Shape(), ROWS, ROWS)

    def front(self, x, *, rows):
        return Copy.step(x)[:rows], None

    def head(self, x):
        return x

    def inputs(self, rows) -> tuple[np.ndarray, dict]:
        buffer = np.zeros((ROWS, HEADS * HEAD_DIM), bfloat16)
        buffer[: len(rows)] = rows
        return buffer, dict(rows=len(rows))

    def shapes(self) -> list[dict]:
        return [dict(x=((ROWS, HEADS * HEAD_DIM), bfloat16))]

    def body(self, x, *, rows: Scratchpad[np.int32]):
        x, angles = self.front(x, rows=rows)
        return self.forward(x, rows, angles)


def attention(x, scale: float, window: int | None = None) -> np.ndarray:
    """Every row of ``x`` over the rows within ``window`` of it, per head."""
    n = x.shape[0]
    h = x.astype(np.float32).reshape(n, HEADS, HEAD_DIM).transpose(1, 0, 2)
    logits = h @ h.transpose(0, 2, 1) * np.float32(scale)
    if window is not None:
        at = np.arange(n)
        logits[:, np.abs(at[:, None] - at[None, :]) > window] = -np.inf
    p = np.exp(logits - logits.max(axis=-1, keepdims=True))
    p /= p.sum(axis=-1, keepdims=True)
    return (p @ h).transpose(1, 0, 2).reshape(n, HEADS * HEAD_DIM)
