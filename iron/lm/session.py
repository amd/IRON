# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One conversation over a ``CausalLM``'s loaded versions: the tokens its
caches hold, and the calls that run a history's new tokens and draw after
it. Several sessions share one compiled model; its caches hold one
session's tokens at a time, so a session whose tokens another's calls
replaced runs its history again from the first token.
"""

from collections.abc import Iterator
from functools import partial

import numpy as np
from aie.iron.kernels.sample import ROW_WORDS

from iron.operators.sample import Sample

from .generation import Sampler

NOTHING = np.empty(0, dtype=np.int64)


class Session:
    """A conversation over the versions of ``lm``, a ``CausalLM``
    (``CausalLM.use``).
    """

    def __init__(self, lm):
        self.lm = lm
        self._seen = NOTHING  # the tokens in the caches

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, the whole history.

        One more token than the last call's is a decode step; anything else
        runs from the first token the caches do not hold (``resume``).

        Raises:
            ValueError: ``tokens`` is empty or longer than ``max_seq_len``.
            IndexError: A token is outside ``[0, vocab_size)``; refused
                before any dispatch, so the caches are as they were.
        """
        tokens = self._tokens(tokens)
        n, L = tokens.size, self.lm.config.max_seq_len
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        self._take()
        held = self._held(tokens)
        if held == n - 1 == self._seen.size:
            out, _ = self.lm(token=int(tokens[-1]), position=n - 1)
        else:
            start = self.resume(held)
            self._seen = tokens[:start]
            for inputs, values in self._chunks(tokens, start):
                out, _ = self.lm(*inputs, **values)
        self._seen = tokens
        # A copy: the next call rewrites the output buffer. An odd vocabulary
        # is padded by a logit no token has.
        return np.array(out.numpy()).reshape(-1)[: self.lm.config.vocab_size]

    def draw(
        self, tokens, max_tokens: int, sampler: Sampler, each: bool = True
    ) -> Iterator[int]:
        """Draw ``max_tokens`` after ``tokens`` on the device, each yielded
        as it is drawn (``Model.stream``): looped there where the decode
        step is a full ELF (``device_loop``), else each step started from
        the host. The draws match ``generate_on_host`` with the same seed.

        Raises:
            ValueError: The tokens and those to draw do not fit the caches.
            IndexError: A token is outside ``[0, vocab_size)``.
            RuntimeError: Neither version is loaded: ``load_versions()``
                first.
        """
        model, tokens = self.lm, self._tokens(tokens)
        n, L = tokens.size, model.config.max_seq_len
        if not (0 < n and 0 < max_tokens and n + max_tokens - 1 <= L):
            raise ValueError(
                f"{n} tokens and {max_tokens} more to draw do not fit {L} rows"
            )
        if model.prompt_chunk is None or model.decode_step is None:
            raise RuntimeError(f"{type(model).__name__}: load_versions() first")
        self._take()
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        rows = np.zeros((L, ROW_WORDS), dtype=np.int32)
        k_max = next(
            s.op.k_max
            for s in model.decode_step.recording.steps
            if isinstance(s.op, Sample)
        )
        rows[n - 1 : n - 1 + max_tokens] = sampler.rows(max_tokens, k_max)
        model.decode_step.write(model.draws, rows)
        start = self.resume(self._held(tokens))
        # A caller may stop early, leaving steps in the caches nothing records:
        # until the last token, they hold nothing.
        self._seen = NOTHING
        drawn = []
        chunks = self._chunks(tokens, start)
        if model.device_loop:
            draws = device_draws(model, chunks, n, max_tokens, each)
        else:
            draws = host_draws(model, chunks, max_tokens)
        for token in draws:
            drawn.append(token)
            yield token
        # The caches hold every token but the last drawn, which no step read.
        self._seen = np.concatenate([tokens, drawn[:-1]]).astype(np.int64)

    def forget(self, position: int) -> None:
        """Hold nothing the caches have from ``position`` on: the next call
        runs from there, as a change before it (a placeholder's soft tokens)
        would leave them stale.
        """
        self._seen = self._seen[:position]

    def resume(self, held: int) -> int:
        """The position calls start from to run the tokens from ``held`` on:
        ``held`` itself, or for a state that cannot restart there
        (``KVCache.restart``), the earliest one of them can.
        """
        ran = self._seen.size
        return min([held, *(c.restart(held, ran) for c in self.lm.recurrent)])

    def prompt_ids(self, tokens) -> np.ndarray:
        """A prompt call's ``ids`` for a chunk of ``tokens``, padded to
        ``prefill_chunk`` with row 0, which the bound by ``rows`` leaves
        unread.
        """
        tokens = np.asarray(tokens)
        ids = np.zeros(self.lm.config.prefill_chunk, dtype=np.int32)
        ids[: tokens.size] = tokens
        return ids

    def _take(self) -> None:
        """Hold the caches: what another session left there is none of this
        one's tokens.
        """
        if self.lm.holder is not self:
            self.lm.holder, self._seen = self, NOTHING

    def _tokens(self, tokens) -> np.ndarray:
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        V = self.lm.config.vocab_size
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

    def _chunks(self, tokens: np.ndarray, start: int) -> Iterator[tuple]:
        """Each prompt call from ``start``: its inputs, ``ids`` and for a call
        holding a placeholder ``before``, and its per-call values. With
        recurrent state a call ends at the next chunk boundary.
        """
        model = self.lm
        n, C = tokens.size, model.config.prefill_chunk
        placeholders = model.placeholders
        end = start
        while end < n:
            begin, end = end, min(end + C, n)
            if model.recurrent:
                end = min(end, (begin // C + 1) * C)
            ids = self.prompt_ids(tokens[begin:end])
            values = dict(
                model.call_values(),
                token=int(tokens[end - 1]),
                position=end - 1,
                start=begin,
                rows=end - begin,
                rope_start=model.rope_row(n, begin),
            )
            placed = np.isin(tokens[begin:end], placeholders).any()
            if model.placed_chunk is None or not placed:
                yield (ids,), values
                continue
            before = np.array(
                [np.count_nonzero(tokens[:begin] == t) for t in placeholders],
                np.int32,
            )
            yield (ids, before), values


def host_draws(model, chunks, max_tokens: int) -> Iterator[int]:
    """``max_tokens`` drawn after the prompt ``chunks``, the
    host starting each decode step on the token the last one drew, which it
    reads alone.
    """
    for inputs, values in chunks:
        _, carry = model(*inputs, **values)
    yield int(carry["token"])
    for _ in range(max_tokens - 1):
        _, carry = model(**carry)
        yield int(carry["token"])


def device_draws(model, chunks, n: int, max_tokens: int, each: bool) -> Iterator[int]:
    """``max_tokens`` drawn after the prompt ``chunks`` of ``n`` tokens, the
    last chunk starting a device loop of decode steps (``CausalLM.loop``):
    with ``each``, each token read once its step completes, else the first
    alone and the rest once the last has.
    """
    for inputs, values in chunks:
        if values["position"] < n - 1:
            model(*inputs, **values)
            continue
        loop = model.loop(
            model.prompt_chunk if len(inputs) == 1 else model.placed_chunk
        )
        loop.start(*inputs, **values)
    read = partial(model.decode_step.read, model.drawn)
    yield int(read()[n - 1])
    for k, _ in enumerate(loop.steps(max_tokens - 1), start=1):
        if each:
            yield int(read()[n - 1 + k])
    if not each:
        yield from (int(t) for t in read()[n : n - 1 + max_tokens])
