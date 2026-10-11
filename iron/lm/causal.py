# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

A call with no tensor is a decode step; ``prefill_chunk`` token ``ids`` are
a prompt chunk, of which a call runs the first ``rows``, their rows of the
embedding table gathered on the device, in a full ELF or an xclbin. Both
draw the next token on the device and carry it and ``position + 1`` into
the next call.
Both attend with ``MHA``. Where the decode step is not a full ELF (NPU1, or
``boundaries=each_step``) there is no device loop: the host starts each step
on the token the last one drew.
"""

import dataclasses
import logging
import time
from collections.abc import Iterator
from typing import Any

import aie.utils as aie_utils
import numpy as np
from aie.iron.kernels.sample import ROW_WORDS
from ml_dtypes import bfloat16

import iron
from iron.common import Carried, Scratchpad
from iron.common.graph import CarriedLoop, CompiledGraph, Handle
from iron.common.graph.handle import Weight
from iron.common.graph.narrowing import JointNarrowing, Tuning
from iron.operators.copy import Copy
from iron.operators.mha import MHA
from iron.operators.sample import Sample

from .base import Config, Oracle
from .generation import Sampler

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Step:
    prompt: bool
    angles: Handle
    # A per-call value in a trace, its number in the reference.
    chunk: Any
    rows: Any
    position: Any


class CausalLM(iron.Graph):
    """A decoder on ``config``'s shape; a subclass gives ``layer``, ``head`` and ``oracle``.

    The caches are ``(max_seq_len, n_kv_groups, head_dim)`` so no descriptor
    steps by ``max_seq_len``. A decode step attends with ``MHA`` of one
    query, which costs the context, not the cache.
    """

    embedding: Weight
    layers: list
    oracle: "type[Oracle]"

    def __init__(self, config: Config, weights):
        self.config = config
        vars(self).update(vars(weights))
        self.embedding = iron.weight(weights.embedding)
        G, L, D = config.n_kv_groups, config.max_seq_len, config.head_dim
        self.keys = [iron.state((L, G, D)) for _ in self.layers]
        self.values = [iron.state((L, G, D)) for _ in self.layers]
        self.rope = iron.weight(config.angles().astype(bfloat16))
        # Zero until the host writes draws: a row of zeros is greedy.
        self.draws = iron.state((L, ROW_WORDS), np.int32)
        self.drawn = iron.state((L,), np.int32)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches
        self._prompt: CompiledGraph | None = None
        self._decode: CompiledGraph | None = None
        self._loop: CarriedLoop | None = None

    def layer(self, step: Step, i: int, weights, x):
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def embed(self, x, pixel_values=None):
        return x

    def body(
        self,
        ids=None,
        pixel_values=None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        chunk: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
    ):
        c = self.config
        L, C, D = c.max_seq_len, c.prefill_chunk, c.head_dim
        prompt = ids is not None
        if prompt:
            x = Copy(self.embedding[ids[:rows]])
            angles = Copy(self.rope.reshape(L // C, C, D)[chunk, :rows])
        else:
            x = Copy(self.embedding[token]).reshape(1, c.emb_dim)
            angles = Copy(self.rope[position]).reshape(1, D)
        x = self.embed(x, pixel_values)
        step = Step(prompt, angles, chunk, rows, position)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        if prompt:
            x = Copy(x[rows - 1]).reshape(1, c.emb_dim)  # the last row's logits alone
        logits = self.head(x)
        _, drawn = Sample(
            logits.reshape(c.vocab_size),
            self.draws,
            self.drawn,
            row=position * ROW_WORDS,
            at=position,
        )
        return logits, iron.carry(token=drawn, position=position + 1)

    def attend(self, step: Step, i: int, q, k, v):
        """Write ``k`` and ``v`` into layer ``i``'s caches and attend over them causally."""
        c = self.config
        H, G, D, L, C = (
            c.n_heads,
            c.n_kv_groups,
            c.head_dim,
            c.max_seq_len,
            c.prefill_chunk,
        )
        keys, values = self.keys[i], self.values[i]
        n = q.shape[0] // H
        for x, cache in ((k, keys), (v, values)):
            if step.prompt:
                rows = cache.reshape(L // C, C, G, D)[step.chunk, : step.rows]
                Copy(x.reshape(n, G, D), rows)
            else:
                Copy(x.reshape(G, D), cache[step.position])
        span = np.s_[: step.position + 1]
        o = MHA(
            q.reshape(n, H, D),
            keys[span],
            values[span],
            heads_interleaved=True,
            kv_interleaved=True,
        )
        return o.reshape(n, H * D)

    # -- on the host -----------------------------------------------------------

    def shapes(self, rows: int) -> dict:
        """The input shapes of the version of ``rows`` rows: a prompt chunk's
        token ids, a decode step's none.
        """
        return dict(ids=((rows,), np.int32)) if rows > 1 else {}

    def load(
        self,
        release=None,
        tuner: JointNarrowing | None = None,
        boundaries: str | None = None,
        dev=None,
    ) -> "CausalLM":
        """Compile and load both versions before the first call, so the arena is made once.

        Args:
            release: Given each piece of each weight once it is on the device.
            tuner: Folds, narrows and packs each version's designs by cost.
            boundaries: Both versions' packaging.
            dev: The device both versions are compiled for, else the current
                one.
        """
        if dev is None:
            dev = aie_utils.ensure_current_device()
        decode = self.compile(
            dev=dev, coresident=tuner, boundaries=boundaries, **self.shapes(1)
        )
        if decode.plan.image != iron.ELF:
            logger.info("%s", decode.plan.report("decode"))
        feeds = decode if decode.emit is not None else None
        prompt = self.compile(
            dev=dev,
            feeds=feeds,
            coresident=tuner,
            boundaries=boundaries,
            **self.shapes(self.config.prefill_chunk),
        )
        for version in (decode, prompt):
            version.load(release=release)
        self._prompt, self._decode = prompt, decode
        return self

    def __call__(self, ids=None, pixel_values=None, **values) -> Any:
        """One call of the loaded prompt version on ``ids``
        (``prompt_ids``) and, where the model takes one, ``pixel_values``,
        else of the decode step.

        Raises:
            RuntimeError: Neither version is loaded: ``load()`` first, which
                compiles them with the tuner and packaging asked for.
        """
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        if ids is None:
            return self._decode(**values)
        assert self._prompt is not None
        if pixel_values is None:
            return self._prompt(ids, **values)
        return self._prompt(ids, pixel_values, **values)

    @property
    def device_loop(self) -> bool:
        """Whether ``generate`` can draw on the device: a full-ELF decode step."""
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        return self._decode.emit is not None

    @property
    def tunings(self) -> dict[str, Tuning]:
        """Each tuned version's ``Tuning``, by ``"decode"`` and ``"prompt"``."""
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        versions = dict(decode=self._decode, prompt=self._prompt)
        return {
            name: v.tuning
            for name, v in versions.items()
            if v is not None and v.tuning is not None
        }

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, the whole history.

        One more token than the last call's is a decode step; anything else
        runs from the first token the caches do not hold.

        Raises:
            ValueError: ``tokens`` is empty or longer than ``max_seq_len``.
            IndexError: A token is outside ``[0, vocab_size)``; refused
                before any dispatch, so the caches are as they were.
        """
        tokens = self._tokens(tokens)
        n, L, C = tokens.size, self.config.max_seq_len, self.config.prefill_chunk
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        held = self._held(tokens)
        if held == n - 1 == self._seen.size:
            out, _ = self(token=int(tokens[-1]), position=n - 1, chunk=0, rows=1)
        else:
            self._seen = tokens[: held // C * C]
            for ids, values in self._chunks(tokens, held):
                out, _ = self(ids, **values)
        self._seen = tokens
        # A copy: the next call rewrites the output buffer.
        logits = out.numpy()
        return np.array(logits).reshape(-1)

    def generate(
        self, tokens, num_tokens: int, sample: Sampler
    ) -> tuple[list[int], float, float]:
        """Draw ``num_tokens`` after ``tokens`` on the device.

        Where the decode step is a full ELF each step starts the next
        (``device_loop``); elsewhere the host starts each step on the token
        the last one drew, which it reads alone. The draws match
        ``generation.generate`` on the host with the same seed.

        Returns:
            The tokens drawn, the seconds to the first, and the mean seconds
            per token after it (NaN for one token).

        Raises:
            IndexError: A token is outside ``[0, vocab_size)``.
        """
        tokens = self._tokens(tokens)
        n, L, C = tokens.size, self.config.max_seq_len, self.config.prefill_chunk
        if not (0 < n and 0 < num_tokens and n + num_tokens - 1 <= L):
            raise ValueError(
                f"{n} tokens and {num_tokens} more to draw do not fit {L} rows"
            )
        loop = self.device_loop
        assert self._prompt is not None and self._decode is not None
        if loop and self._loop is None:
            self._loop = CarriedLoop(self._prompt, self._decode, depth=2)
        start = time.perf_counter()
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        draws = np.zeros((L, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + num_tokens] = sample.rows(num_tokens, self._k_max())
        self._decode.write(self.draws, draws)
        held = self._held(tokens)
        self._seen = tokens[: held // C * C]
        for ids, values in self._chunks(tokens, held):
            if not loop or values["position"] < n - 1:
                _, carry = self(ids, **values)
            else:
                self._loop.start(ids, **values)
        first = time.perf_counter()
        if loop:
            for _ in self._loop.steps(num_tokens - 1):
                pass
        else:
            drawn = [carry["token"]]
            for _ in range(num_tokens - 1):
                _, carry = self(chunk=0, rows=1, **carry)
                drawn.append(carry["token"])
        later = (
            (time.perf_counter() - first) / (num_tokens - 1)
            if num_tokens > 1
            else float("nan")
        )
        if loop:
            drawn = self._decode.read(self.drawn)[n - 1 : n - 1 + num_tokens]
        # The caches hold every token but the last drawn, which no step read.
        self._seen = np.concatenate([tokens, drawn[:-1]]).astype(np.int64)
        return [int(t) for t in drawn], first - start, later

    def _tokens(self, tokens) -> np.ndarray:
        """``tokens`` as one row of ids, each checked against the vocabulary.

        Raises:
            IndexError: A token is outside ``[0, vocab_size)``.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        V = self.config.vocab_size
        if ((tokens < 0) | (tokens >= V)).any():
            raise IndexError(
                f"tokens {tokens[(tokens < 0) | (tokens >= V)]} are outside [0, {V})"
            )
        return tokens

    def _held(self, tokens: np.ndarray) -> int:
        """How many of ``tokens`` the caches hold; never the last."""
        held = min(tokens.size - 1, self._seen.size)
        same = np.append(tokens[:held] == self._seen[:held], False)
        return int(np.argmin(same))

    def prompt_ids(self, tokens) -> np.ndarray:
        """A prompt call's ``ids`` for a chunk of ``tokens``, padded to
        ``prefill_chunk`` with row 0, which the bound by ``rows`` leaves
        unread.
        """
        tokens = np.asarray(tokens)
        ids = np.zeros(self.config.prefill_chunk, dtype=np.int32)
        ids[: tokens.size] = tokens
        return ids

    def _chunks(self, tokens: np.ndarray, held: int) -> Iterator[tuple]:
        n, C = tokens.size, self.config.prefill_chunk
        for begin in range(held // C * C, n, C):
            end = min(begin + C, n)
            ids = self.prompt_ids(tokens[begin:end])
            values = dict(
                token=int(tokens[end - 1]),
                position=end - 1,
                chunk=begin // C,
                rows=end - begin,
            )
            yield ids, values

    def _k_max(self) -> int:
        assert self._decode is not None
        return next(
            s.op.k_max for s in self._decode.traced.steps if isinstance(s.op, Sample)
        )
