# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An encoder on the NPU as one graph: a sequence of at most ``max_tokens``
rows in, attended bidirectionally, compiled once for every length.

``Encoder`` is the graph's host side, its one version and a call's inputs;
a model subclasses it with its ``body``. ``sandwich_layer`` is the layer
EmbeddingGemma 2's text encoder and its vision tower share: attention, then
the GELU-gated feed-forward, each between sandwich norms.
"""

from collections.abc import Callable
from functools import partial

import numpy as np

from .base import Model
from .blocks import geglu, sandwich


class Encoder(Model):
    """An encoder over ``max_tokens`` rows at most, one compile for every
    length.

    A call takes the token ids, padded to ``max_tokens`` with ``vocab_size``
    (the model's id of a zero row), and ``n``, the real rows, which bound
    every operator after the embedding gather.

    Args:
        config: The model's shape; its ``vocab_size`` is read here.
        max_tokens: The longest sequence a call takes.
    """

    def __init__(self, config, max_tokens: int):
        self.config = config
        self.max_tokens = max_tokens

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, ``max_tokens`` rows."""
        return [dict(ids=((self.max_tokens,), np.int32))]

    def inputs(self, tokens) -> tuple[np.ndarray, int]:
        """A call's ``ids`` and ``n`` for ``tokens``, padded to ``max_tokens``.

        Raises:
            ValueError: ``tokens`` is empty or longer than ``max_tokens``.
            IndexError: A token is outside ``[-vocab_size, vocab_size)``.
        """
        tokens = np.asarray(tokens)
        n, V = len(tokens), self.config.vocab_size
        if not 0 < n <= self.max_tokens:
            raise ValueError(f"{n} tokens do not fit {self.max_tokens} rows")
        outside = tokens[(tokens < -V) | (tokens >= V)]
        if outside.size:
            raise IndexError(f"tokens {outside} are outside [-{V}, {V})")
        ids = np.full(self.max_tokens, V, np.int32)
        ids[:n] = tokens % V
        return ids, n


def sandwich_layer(
    x,
    attend: Callable,
    norms: tuple,
    gate,
    up,
    down,
    epsilon: float,
    **gemm,
):
    """A layer on ``x``: ``attend`` between ``norms``' first two RMS norm
    weights, then the GELU-gated feed-forward (``gate``, ``up``, ``down``,
    GEMMs with ``gemm``'s keywords) between its last two, each with its
    residual.
    """
    x = sandwich(x, attend, norms[0], norms[1], epsilon)
    feed_forward = partial(geglu, w_gate=gate, w_up=up, w_down=down, **gemm)
    return sandwich(x, feed_forward, norms[2], norms[3], epsilon)
