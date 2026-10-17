# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An encoder on the NPU as one graph: a sequence of at most ``max_tokens``
rows in, attended bidirectionally, compiled once for every length.

``Encoder`` is the graph's host side, its one version and a call's inputs;
a model subclasses it with its ``body``.
"""

import numpy as np

from .base import Model


class Encoder(Model):
    """An encoder over ``max_tokens`` rows at most, one compile for every
    length.

    A call takes the token ids, padded to ``max_tokens`` with 0, and ``n``,
    the real rows, which bound the embedding gather and every operator
    after it.

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
        ids = np.zeros(self.max_tokens, np.int32)
        ids[:n] = tokens % V
        return ids, n
