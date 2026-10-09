# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

A call with no ``x`` is a decode step; ``prefill_chunk`` rows of ``x`` are a
prompt chunk, of which a call runs the first ``rows``. Both draw the next
token on the device and carry it and ``position + 1`` into the next call.
A prompt chunk attends with ``MHA``, so where MHA does not fit the device
there is no prompt version and a prompt runs a token at a time. Where the
decode step is not a full ELF (NPU1, or ``boundaries=each_step``) there is
no device loop.
"""

import dataclasses
import enum
import math
import time
from collections.abc import Callable, Iterator
from types import SimpleNamespace
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
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gqa import GQAContext, GQAScores
from iron.operators.mha import MHA
from iron.operators.sample import Sample
from iron.operators.softmax import Softmax

from .generation import Sampler

RopeScaling = Callable[[np.ndarray], np.ndarray]


def rope_angles(
    head_dim: int,
    context_length: int,
    rope_base: float = 500000.0,
    scaling: RopeScaling | None = None,
) -> np.ndarray:
    """The RoPE table, ``(context_length, head_dim)`` float32, cos and sin interleaved.

    Each transcendental is evaluated in float64 and rounded once.
    """
    exponents = np.arange(0, head_dim, 2, dtype=np.float32) / np.float32(head_dim)
    inv_freq = 1.0 / np.power(rope_base, exponents.astype(np.float64))
    if scaling is not None:
        inv_freq = scaling(inv_freq)
    inv_freq = inv_freq.astype(np.float32)
    freqs = np.outer(np.arange(context_length, dtype=np.float32), inv_freq)
    angles = np.empty((context_length, head_dim), dtype=np.float32)
    angles[:, ::2] = np.cos(freqs.astype(np.float64))
    angles[:, 1::2] = np.sin(freqs.astype(np.float64))
    return angles


@dataclasses.dataclass(frozen=True)
class Config:
    vocab_size: int
    emb_dim: int
    n_layers: int
    n_heads: int
    n_kv_groups: int
    head_dim: int
    hidden_dim: int
    max_seq_len: int
    rope_base: float
    rope_scaling: RopeScaling | None = None
    prefill_chunk: int = 2048

    def __post_init__(self):
        if self.max_seq_len % self.prefill_chunk:
            raise ValueError(
                f"prefill_chunk ({self.prefill_chunk}) must divide max_seq_len "
                f"({self.max_seq_len})"
            )

    def angles(self) -> np.ndarray:
        return rope_angles(
            self.head_dim, self.max_seq_len, self.rope_base, self.rope_scaling
        )


class DecodeAttention(enum.Enum):
    """How a decode step attends over the caches."""

    MHA = "mha"
    GQA = "gqa"


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
    query, or with ``DecodeAttention.GQA`` with ``GQAScores``, ``Softmax``
    and ``GQAContext`` reading each group's rows in place; either costs the
    context, not the cache. Left ``None`` it is ``MHA`` where MHA fits the
    device a trace is against, else ``GQA``.
    """

    embedding: Weight
    layers: list
    oracle: "type[Oracle]"
    decode_attention: DecodeAttention | None = None

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
        # On the query rather than the scores: the same bits where
        # 1/sqrt(head_dim) is a power of two (64), and no row per position.
        scale = np.full((1, config.n_heads * D), 1 / math.sqrt(D), dtype=bfloat16)
        self.scale = iron.weight(scale)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches
        self._prompt: CompiledGraph | None = None
        self._decode: CompiledGraph | None = None
        self._loop: CarriedLoop | None = None

    def layer(self, step: Step, i: int, weights, x):
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def body(
        self,
        x=None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        chunk: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
    ):
        c = self.config
        L, C, D = c.max_seq_len, c.prefill_chunk, c.head_dim
        prompt = x is not None
        if prompt:
            x = x[:rows]
            angles = Copy(self.rope.reshape(L // C, C, D)[chunk], tile_size=1024)
            angles = angles.reshape(C, D)[:rows]
        else:
            x = Copy(self.embedding[token]).reshape(1, c.emb_dim)
            angles = Copy(self.rope[position]).reshape(1, D)
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
        attention = self.attention(aie_utils.ensure_current_device())
        if not step.prompt and attention is DecodeAttention.GQA:
            scores = GQAScores(keys[span], ElementwiseMul(q, self.scale).reshape(H, D))
            ctx = GQAContext(values[span], Softmax(scores))
            return ctx.reshape(1, H * D)
        o = MHA(
            q.reshape(n, H, D),
            keys[span],
            values[span],
            heads_interleaved=True,
            kv_interleaved=True,
        )
        return o.reshape(n, H * D)

    # -- on the host -----------------------------------------------------------

    def attention(self, dev) -> DecodeAttention:
        """The decode step's attention on ``dev``.

        Args:
            dev: The device the decode step is traced against; None takes MHA.

        Returns:
            ``decode_attention`` where given, else ``MHA`` where MHA fits
            ``dev``, else ``GQA``.
        """
        if self.decode_attention is not None:
            return self.decode_attention
        if dev is None or MHA.fits(dev):
            return DecodeAttention.MHA
        return DecodeAttention.GQA

    def shapes(self, rows: int) -> dict:
        return dict(x=(rows, self.config.emb_dim)) if rows > 1 else {}

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
                one. ``reference`` traces against the current device, so
                where they differ it may attend as the other does.
        """
        if dev is None:
            dev = aie_utils.ensure_current_device()
        decode = self.compile(
            dev=dev, coresident=tuner, boundaries=boundaries, **self.shapes(1)
        )
        if decode.plan.image != iron.ELF:
            print(decode.plan.report("decode"), flush=True)
        if not MHA.fits(dev):
            decode.load(release=release)
            self._prompt, self._decode = None, decode
            return self
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

    def __call__(self, x=None, **values) -> Any:
        """One call of the loaded prompt version on ``x``, else of the decode step.

        Raises:
            RuntimeError: Neither version is loaded: ``load()`` first, which
                compiles them with the tuner and packaging asked for.
        """
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        if x is None:
            return self._decode(**values)
        if self._prompt is None:
            raise RuntimeError(
                f"{type(self).__name__}: no prompt version on this device; "
                f"a prompt runs a decode step per token (logits)"
            )
        return self._prompt(x, **values)

    @property
    def device_loop(self) -> bool:
        """Whether ``generate`` can draw on the device: a full-ELF decode step
        beside a prompt version."""
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        return self._prompt is not None and self._decode.emit is not None

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
        elif self._prompt is None:
            self._seen = tokens[:held]
            for position in range(held, n):
                token = int(tokens[position])
                out, _ = self(token=token, position=position, chunk=0, rows=1)
        else:
            self._seen = tokens[: held // C * C]
            for x, values in self._chunks(tokens, held):
                out, _ = self(x, **values)
        self._seen = tokens
        # A copy: the next call rewrites the output buffer.
        logits = out.numpy()
        return np.array(logits).reshape(-1)

    def generate(
        self, tokens, num_tokens: int, sample: Sampler
    ) -> tuple[list[int], float, float]:
        """Draw ``num_tokens`` after ``tokens`` with the host out of the loop.

        The draws match ``generation.generate`` on the host with the same seed.

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
        if not self.device_loop:
            assert self._decode is not None
            raise RuntimeError(
                f"{type(self).__name__}: the device loop needs a full-ELF "
                f"decode step beside a prompt version, and this decode step "
                f"is an {self._decode.plan.image}; draw on the host "
                f"(generation.generate)"
            )
        assert self._prompt is not None and self._decode is not None
        if self._loop is None:
            self._loop = CarriedLoop(self._prompt, self._decode, depth=2)
        start = time.perf_counter()
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        draws = np.zeros((L, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + num_tokens] = sample.rows(num_tokens, self._k_max())
        self._decode.write(self.draws, draws)
        held = self._held(tokens)
        self._seen = tokens[: held // C * C]
        for x, values in self._chunks(tokens, held):
            if values["position"] < n - 1:
                self(x, **values)
            else:
                self._loop.start(x, **values)
        first = time.perf_counter()
        for _ in self._loop.steps(num_tokens - 1):
            pass
        later = (
            (time.perf_counter() - first) / (num_tokens - 1)
            if num_tokens > 1
            else float("nan")
        )
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

    def _chunks(self, tokens: np.ndarray, held: int) -> Iterator[tuple]:
        n, C = tokens.size, self.config.prefill_chunk
        x = np.zeros((C, self.config.emb_dim), dtype=bfloat16)
        for begin in range(held // C * C, n, C):
            end = min(begin + C, n)
            x[: end - begin] = self.embedding.array[tokens[begin:end]]
            values = dict(
                token=int(tokens[end - 1]),
                position=end - 1,
                chunk=begin // C,
                rows=end - begin,
            )
            yield x, values

    def _k_max(self) -> int:
        assert self._decode is not None
        return next(
            s.op.k_max for s in self._decode.traced.steps if isinstance(s.op, Sample)
        )


class Oracle:
    """A decoder's float32 forward pass on the host, the oracle the model is judged by.

    It is numpy, not composed from the operators' references, so it catches
    a wiring mistake the graph's own reference would repeat. Its weights are
    twice the checkpoint, so it is built to check with and dropped.
    """

    embedding: np.ndarray
    layers: list

    def __init__(self, config: Config, weights):
        self.config = config
        vars(self).update(vars(_widen(weights)))
        self.angles = config.angles()
        self.buffers: dict[str, np.ndarray] = {}

    def layer(self, angles, w, x):
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def logits(self, tokens) -> np.ndarray:
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        angles = self.angles[: tokens.size]
        x = self.embedding[tokens]
        for w in self.layers:
            x = self.layer(angles, w, x)
        return self.head(x[-1])

    @staticmethod
    def rotate(x, angles):
        cos, sin = angles[:, None, ::2], angles[:, None, 1::2]
        x1, x2 = np.split(x, 2, axis=-1)
        return np.concatenate([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1)

    def buffer(self, name: str, shape: tuple[int, ...]) -> np.ndarray:
        """A float32 array of `shape` that `name` reuses from call to call.

        A temporary past glibc's mmap threshold is mapped afresh and faulted
        in page by page, which under memory pressure costs more than the
        arithmetic.

        Args:
            name: What the array holds; one array per name.
            shape: Its shape this time.

        Returns:
            A view of the array, its contents undefined.
        """
        size = math.prod(shape)
        held = self.buffers.get(name)
        if held is None or held.size < size:
            # Headroom, so a history growing a token a step seldom reallocates.
            held = np.empty(
                size if held is None else max(size, held.size * 5 // 4), np.float32
            )
            self.buffers[name] = held
        return held[:size].reshape(shape)

    def attend(self, q, k, v):
        n, H, D = q.shape
        k, v = (np.repeat(a, H // self.config.n_kv_groups, axis=1) for a in (k, v))
        # Batched matmuls, not einsum: BLAS is 10x faster at 3k.
        p = np.matmul(
            q.transpose(1, 0, 2),
            k.transpose(1, 2, 0),
            out=self.buffer("scores", (H, n, n)),
        )
        p *= np.float32(1 / np.sqrt(D))
        p += np.triu(np.full((n, n), -np.inf, dtype=np.float32), k=1)
        p -= p.max(axis=-1, keepdims=True)
        np.exp(p, out=p)
        p /= p.sum(axis=-1, keepdims=True)
        return (p @ v.transpose(1, 0, 2)).transpose(1, 0, 2).reshape(n, H * D)


def _widen(value):
    if isinstance(value, np.ndarray):
        return value.astype(np.float32)
    if isinstance(value, list):
        return [_widen(v) for v in value]
    if isinstance(value, SimpleNamespace):
        return SimpleNamespace(**{k: _widen(v) for k, v in vars(value).items()})
    return value
