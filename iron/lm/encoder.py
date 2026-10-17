# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An encoder on the NPU as one graph: a sequence of at most ``max_tokens``
rows in, attended bidirectionally, compiled once for every length.

``Encoder`` looks up token ids' rows and runs ``forward`` over them: each
layer, the final norm, ``pool`` and ``head``. A ``Tower`` is an encoder
whose rows come from a front end, ``front``, and whose output is soft tokens
in a text model's space.
"""

import dataclasses
from functools import partial
from typing import Any, ClassVar

import numpy as np

from iron import Scratchpad
from iron.operators.mha import MHA

from .base import Model


@dataclasses.dataclass
class EncodeStep:
    """What each of an encoder's layers is called with."""

    # The rows valid this call, a per-call value in a trace.
    n: Any
    angles: Any
    # The rows ``forward`` took, before any positions.
    embeddings: Any


class Encoder(Model):
    """An encoder over ``max_tokens`` rows at most, one compile for every
    length; a subclass gives ``lookup`` and ``head``, and its config
    ``layer(i)``.

    A call takes the token ids, padded to ``max_tokens`` with 0, and ``n``,
    the real rows, which bound the embedding gather and every operator
    after it.

    Args:
        config: The model's shape: its ``layer(i)`` is each layer, and
            ``inputs`` reads its ``vocab_size``.
        layers: The checkpoint's layers, which the subclass holds by their
            checkpoint path before this is called.
        max_tokens: The longest sequence a call takes.
    """

    # The per-call value bounding a call's rows.
    bound: ClassVar[str] = "n"

    def __init__(self, config, layers: list, max_tokens: int):
        self.config = config
        self.layers = layers
        self.max_tokens = max_tokens

    def lookup(self, ids):
        """The embedding rows of ``ids``, bounded as ``ids`` is."""
        raise NotImplementedError(f"{type(self).__name__} defines no lookup()")

    def angles(self, n):
        """The RoPE angles of the first ``n`` positions, as ``layer`` reads
        them; None rotates nothing.
        """
        return None

    def positions(self, x, step: EncodeStep):
        """``x``, the rows ``step`` runs, with the model's absolute positions
        placed; unchanged by default.
        """
        return x

    def layer(self, step: EncodeStep, i: int, weights, x):
        """Layer ``i`` on ``x``: ``config.layer(i)``, attending bidirectionally."""
        attend = partial(self.attend, step, i)
        return self.config.layer(i).step(weights, x, attend, step.angles)

    def attend(
        self,
        step: EncodeStep,
        i: int,
        q,
        k,
        v,
        *,
        scale: float | None = None,
        window: int | None = None,
    ):
        """``q`` ``(rows, heads, head_dim)`` over every row of ``k`` and
        ``v`` ``(rows, groups, head_dim)``, or within ``window`` positions
        either side, the logits scaled by ``scale`` (MHA's
        ``1 / sqrt(head_dim)`` if None).
        """
        n, H, D = q.shape
        o = MHA.step(
            q,
            k,
            v,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            emulate_bf16_mmul_with_bfp16=False,
            window=window,
            scale=scale,
        )
        return o.reshape(n, H * D)

    def norm(self, x):
        """The final norm over the last layer's rows; none by default."""
        return x

    def pool(self, x, n):
        """The rows ``head`` reads from the ``n`` valid rows of ``x``; all
        of them by default.
        """
        return x

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def forward(self, x, n, angles):
        """The layers, the final norm, ``pool`` and ``head`` over the rows
        ``x``, bounded to their first ``n``, rotated by ``angles``.
        """
        step = EncodeStep(n, angles, x)
        x = self.positions(x, step)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        return self.head(self.pool(self.norm(x), n))

    def from_rows(self, x, *, n):
        """A call on its embedding rows ``x``, bounded to ``n``, in place of
        its ids' lookup.
        """
        return self.forward(x, n, self.angles(n))

    def body(self, ids, *, n: Scratchpad[np.int32]):
        return self.from_rows(self.lookup(ids[:n]), n=n)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, ``max_tokens`` rows."""
        return [dict(ids=((self.max_tokens,), np.int32))]

    def longest(self) -> dict:
        """The per-call values of the longest call: every row real."""
        return dict(n=self.max_tokens)

    def inputs(self, tokens) -> tuple[np.ndarray, dict]:
        """A call's ``ids``, ``tokens`` padded to ``max_tokens``, and its
        per-call values.

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
        return ids, dict(n=n)


class Tower(Encoder):
    """An encoder whose rows come from a front end rather than token ids,
    and whose output is soft tokens in a text model's space, ``text_dim``
    wide, which take a placeholder's places.

    A subclass gives ``front``, ``soft``, ``inputs`` and ``shapes``, and a
    ``body`` naming its input and per-call values that runs ``forward`` on
    what ``front`` gives.

    Args:
        config: The tower's shape; ``soft_tokens`` reads its ``text_dim``.
        layers: As ``Encoder`` takes them.
        max_tokens: The rows its layers take.
        soft_rows: The rows of soft tokens a call returns, the first
            ``soft`` of them valid.
    """

    def __init__(self, config, layers: list, max_tokens: int, soft_rows: int):
        super().__init__(config, layers, max_tokens)
        self.soft_rows = soft_rows

    def front(self, *inputs, **values):
        """The rows the layers take, bounded, and the angles they rotate by."""
        raise NotImplementedError(f"{type(self).__name__} defines no front()")

    def soft(self, values: dict) -> int:
        """The soft tokens a call with per-call ``values`` gives."""
        raise NotImplementedError(f"{type(self).__name__} defines no soft()")

    def inputs(self, *raw) -> tuple[np.ndarray, dict]:
        """A call's input buffer and per-call values for ``raw``."""
        raise NotImplementedError(f"{type(self).__name__} defines no inputs()")

    def soft_tokens(self, *raw) -> np.ndarray:
        """The soft tokens of ``raw``, as ``inputs`` takes it,
        ``(soft, text_dim)`` float32.
        """
        buffer, values = self.inputs(*raw)
        out = self(buffer, **values).numpy().reshape(-1, self.config.text_dim)
        return np.asarray(out[: self.soft(values)], np.float32)
