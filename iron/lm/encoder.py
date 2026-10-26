# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An encoder on the NPU as one graph: a sequence of at most ``max_tokens``
rows in, attended bidirectionally, compiled once for every length.

``Encoder`` looks up token ids and runs ``forward`` over them; a ``Tower``
is an encoder whose rows come from a front end and whose output is soft
tokens in a text model's space.
"""

from typing import Any, ClassVar

import numpy as np

from iron import Scratchpad
from iron.common.graph import Handle

from .blocks import EncoderLayer
from .causal import Call
from .checkpoint import renamed
from .model import Model


class Encoder(Model):
    """An encoder over ``max_tokens`` rows at most, one compile for every
    length: ``layers``, a ``layer_class(config, i)`` each, which a subclass
    loads from its checkpoint; it gives ``lookup`` and ``head``.

    Args:
        config: The model's shape: ``num_hidden_layers`` layers, and
            ``inputs`` reads its ``vocab_size``.
    """

    # A graph class taking (config, i).
    layer_class: ClassVar[type[Any]] = EncoderLayer

    def __init__(self, config, max_tokens: int):
        self.config = config
        self.layers = [
            self.layer_class(config, i) for i in range(config.num_hidden_layers)
        ]
        self.max_tokens = max_tokens
        # The rows a call gives, the first ``soft(values)`` of them valid.
        self.soft_rows = max_tokens
        # The norm module after the last layer.
        self.final_norm = None

    def load_layers(self, tree, layers: str, norm: str = "") -> None:
        """Layer ``i`` from ``tree``, renamed by ``renames``, at
        ``{layers}{i}.``, then ``final_norm``, where there is one, at ``norm``.
        """
        tree = renamed(tree, self.renames)
        for i, layer in enumerate(self.layers):
            layer.load_state_dict(tree, path=f"{layers}{i}.")
        if self.final_norm is not None:
            self.final_norm.load_state_dict(tree, path=norm)

    def lookup(self, ids):
        """The embedding rows of ``ids``, bounded as ``ids`` is."""
        raise NotImplementedError(f"{type(self).__name__} defines no lookup()")

    def angles(self, rows):
        """The RoPE angles of the first ``rows`` positions, by the ``rope``
        each layer names (``Call.ropes``); None: no RoPE.
        """
        return None

    def positions(self, x, call: Call):
        """``x``, the rows ``call`` runs, with the model's absolute positions
        placed; unchanged by default.
        """
        return x

    def layer(self, call: Call, i: int, weights, x):
        """Layer ``i``, the module ``weights``, on ``x``."""
        return weights(x, call)

    def pool(self, x, rows):
        """The rows ``head`` reads from the ``rows`` valid rows of ``x``; all
        of them by default.
        """
        return x

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def forward(self, x: Handle, rows, ropes, ids=None):
        """The layers, the final norm, ``pool`` and ``head`` over the rows
        ``x`` of ``ids`` (None for a tower's), bounded to their first
        ``rows``, rotated by ``ropes`` (``Call.ropes``).
        """
        call = Call(
            prompt=True,
            start=0,
            rows=rows,
            position=None,
            ropes=ropes,
            ids=ids,
            embeddings=x,
        )
        x = self.positions(x, call)
        for i, weights in enumerate(self.layers):
            x = self.layer(call, i, weights, x)
        if self.final_norm is not None:
            x = self.final_norm(x)
        return self.head(self.pool(x, rows))

    def from_rows(self, x, ids, *, rows):
        """A call on its embedding rows ``x``, bounded to ``rows``, in place
        of the lookup of its ``ids``.
        """
        return self.forward(x, rows, self.angles(rows), ids)

    def body(self, ids: Handle, *, rows: Scratchpad[np.int32]):
        ids = ids[:rows]
        return self.from_rows(self.lookup(ids), ids, rows=rows)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: one, ``max_tokens`` rows."""
        return [dict(ids=((self.max_tokens,), np.int32))]

    def longest(self) -> dict:
        """The per-call values of the longest call: every row real."""
        return dict(rows=self.max_tokens)

    def soft(self, values: dict) -> int:
        """The valid rows a call with per-call ``values`` gives: its
        ``rows`` by default.
        """
        return values["rows"]

    def inputs(self, tokens) -> tuple[np.ndarray, dict]:
        """A call's ``ids``, ``tokens`` padded to ``max_tokens``, and its
        per-call values.

        Raises:
            ValueError: ``tokens`` is empty or longer than ``max_tokens``.
            IndexError: A token is outside ``[0, vocab_size)``.
        """
        tokens = np.asarray(tokens)
        n, V = len(tokens), self.config.vocab_size
        if not 0 < n <= self.max_tokens:
            raise ValueError(f"{n} tokens do not fit {self.max_tokens} rows")
        outside = tokens[(tokens < 0) | (tokens >= V)]
        if outside.size:
            raise IndexError(f"tokens {outside} are outside [0, {V})")
        ids = np.zeros(self.max_tokens, np.int32)
        ids[:n] = tokens
        return ids, dict(rows=n)


class Tower(Encoder):
    """An encoder whose rows come from a front end rather than token ids,
    and whose output is soft tokens in a text model's space, ``text_dim``
    wide, which take a placeholder's places.

    Args:
        soft_rows: The rows of soft tokens a call returns, the first
            ``soft`` of them valid.
    """

    def __init__(self, config, max_tokens: int, soft_rows: int):
        super().__init__(config, max_tokens)
        self.soft_rows = soft_rows

    def inputs(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, *raw
    ) -> tuple[np.ndarray, dict]:
        """A call's input buffer and per-call values for ``raw``."""
        raise NotImplementedError(f"{type(self).__name__} defines no inputs()")

    def calls(self, *raw) -> list[tuple[np.ndarray, dict]]:
        """Each call ``raw`` takes, in turn, its input buffer and per-call
        values, each call's soft tokens after the last's: one, ``inputs``'s,
        by default.
        """
        return [self.inputs(*raw)]

    def soft_tokens(self, *raw) -> np.ndarray:
        """The soft tokens of ``raw``, as ``calls`` takes it,
        ``(soft, text_dim)`` float32.
        """
        calls = self.calls(*raw)
        for buffer, values in calls:
            out = self(buffer, **values)
        out = out.numpy().reshape(-1, self.config.text_dim)
        return np.asarray(out[: sum(self.soft(v) for _, v in calls)], np.float32)
