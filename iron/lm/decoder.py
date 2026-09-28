# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

:class:`CausalLM` is the part every such model shares: the body over
``x``, the embedded tokens, ``(rows, emb_dim)``, which branches on that
static shape; the key and value caches and the RoPE table, on the device;
attention over the caches (:meth:`CausalLM.attend`); and
``logits(tokens)``. A model subclasses it with its ``layer`` and its
``head``.

No ``x`` is a decode step at ``position``: the token's embedding row and
the position's RoPE row gathered on the device, the row written into the
caches there, and MHA of its one query over the ``position + 1`` keys up to
it. ``prefill_chunk`` rows of ``x`` are a chunk of a prompt, of which a
call runs the first ``rows``: the chunk's rows written into the caches at
chunk ``chunk``, causal MHA of them over the caches up to ``position``, its
last token, and the head for that token alone. A prompt is its chunks in
turn, so what a call costs follows the tokens it runs, and a step the
context it attends over, not ``max_seq_len``, which sizes the caches and the
RoPE table alone.

Both end in the head, and draw the next token from its logits on the device
(:class:`~iron.operators.sample.Sample`, from a draw the host wrote ahead
for the position). They return the logits and carry the token and
``position + 1`` into the next call, so a prompt's last chunk can start a
decode step and each step the next with nothing from the host
(:meth:`CausalLM.generate`). ``logits(tokens)`` returns the logits instead,
for the host to draw from.

Each shape compiles its own version, and every version runs in the graph's
one scratch arena (:mod:`iron.common.graph.compiled`): the weights and the
caches are uploaded once, and the caches a prompt writes are the ones the
next decode step reads.

:class:`Oracle` is the same model's float32 forward pass on the host, the
reference it is judged by; a model subclasses it too, with a numpy
``layer`` and ``head``, and names it as its ``oracle``.
"""

import dataclasses
import time
from collections.abc import Callable, Iterator
from types import SimpleNamespace
from typing import Any

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

from .generation import Sampler

#: A RoPE frequency scaling: the frequencies (radians per position, float64)
#: in, scaled out (Llama 3's is :class:`~iron.lm.llama3.model.Llama3RopeScaling`).
RopeScaling = Callable[[np.ndarray], np.ndarray]


def rope_angles(
    head_dim: int,
    context_length: int,
    rope_base: float = 500000.0,
    scaling: RopeScaling | None = None,
) -> np.ndarray:
    """The RoPE table, ``(context_length, head_dim)`` float32: cos and sin
    interleaved per frequency, as the RoPE kernel reads it.

    ``inv_freq`` and each ``position * inv_freq`` are rounded to float32;
    ``scaling``, if given, is applied to the frequencies in float64 before
    that rounding, and each transcendental is evaluated in float64 and
    rounded once, so every entry is the correctly rounded float32 of the
    formula.
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
    """A decoder's shape. ``max_seq_len`` is the rows the caches hold,
    prompt and generated tokens together, and ``prefill_chunk``, which
    divides it, the rows a prompt runs at once; ``rope_scaling`` rescales
    the RoPE frequencies (:data:`RopeScaling`).
    """

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
        """The RoPE table, ``(max_seq_len, head_dim)`` float32."""
        return rope_angles(
            self.head_dim, self.max_seq_len, self.rope_base, self.rope_scaling
        )


@dataclasses.dataclass
class Step:
    """What one call runs: a chunk of a ``prompt`` or a decode step, the
    RoPE rows of its positions (``angles``), and its per-call values.
    """

    prompt: bool
    angles: Handle
    # Each the graph's per-call value in a trace, its number in the reference.
    chunk: Any
    rows: Any
    position: Any


class CausalLM(iron.Graph):
    """A decoder on ``config``'s shape and ``weights``, whose top-level
    fields become the model's (named as they are: ``layers.3.q``). It needs
    ``embedding``, the rows tokens are looked up in, and ``layers``;
    ``keys[i]`` and ``values[i]`` are each layer's cache, ``(max_seq_len,
    n_kv_groups, head_dim)``, a position's heads together as the projection
    writes them, so no descriptor steps by ``max_seq_len``; ``rope`` the RoPE
    table the device reads each call's rows of; ``draws`` holds the device's
    draw at each position (``Sampler.rows``) and ``drawn`` the token it drew
    there.

    A subclass gives :meth:`layer` and :meth:`head`, its ``profile``, and
    its ``oracle``, the :class:`Oracle` it is checked against.
    """

    embedding: Weight
    layers: list
    oracle: "type[Oracle]"

    def __init__(self, config: Config, weights):
        self.config = config
        vars(self).update(vars(weights))
        # A decode step gathers its token's row on the device.
        self.embedding = iron.weight(weights.embedding)
        G, L, D = config.n_kv_groups, config.max_seq_len, config.head_dim
        self.keys = [iron.state((L, G, D)) for _ in self.layers]
        self.values = [iron.state((L, G, D)) for _ in self.layers]
        self.rope = iron.weight(config.angles().astype(bfloat16))
        # Zero until the host writes draws: a row of zeros is greedy.
        self.draws = iron.state((L, ROW_WORDS), np.int32)
        self.drawn = iron.state((L,), np.int32)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches
        # The two versions and the loop over them, once loaded.
        self._prompt: CompiledGraph | None = None
        self._decode: CompiledGraph | None = None
        self._loop: CarriedLoop | None = None

    def layer(self, step: Step, i: int, weights, x):
        """Layer ``i`` over ``x``, ``(rows, emb_dim)``, with its ``weights``."""
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        """The logits of ``x``, one row."""
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
            # Every operator below runs the rows of this call alone.
            x = x[:rows]
            angles = Copy(self.rope.reshape(L // C, C, D)[chunk], tile_size=1024)
            angles = angles.reshape(C, D)[:rows]
        else:
            # The token's embedding row and the position's RoPE row, gathered
            # here: a decode step takes nothing from the host.
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
        """Causal attention of the call's rows over layer ``i``'s caches,
        once ``k`` and ``v`` are written into them: ``q`` and ``k``, rotated,
        ``(rows * n_heads, head_dim)`` and ``(rows * n_kv_groups,
        head_dim)``, ``v`` as projected. Returns ``(rows, n_heads *
        head_dim)``.
        """
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
        # The call's rows of the cache, a chunk's or a step's one, as the
        # projection wrote them.
        for x, cache in ((k, keys), (v, values)):
            if step.prompt:
                rows = cache.reshape(L // C, C, G, D)[step.chunk, : step.rows]
                Copy(x.reshape(n, G, D), rows)
            else:
                Copy(x.reshape(G, D), cache[step.position])
        # The queries are the last rows of the keys so far; one query, a
        # step's, MHA packs by its heads.
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
        """The input shapes of the version that runs ``rows`` tokens: none
        for a decode step, which gathers its row on the device.
        """
        return dict(x=(rows, self.config.emb_dim)) if rows > 1 else {}

    def load(self, release=None, tuner: JointNarrowing | None = None) -> "CausalLM":
        """Compile and load the decode and prompt versions, weights uploaded.

        Both before the first call, so the arena is made once at its final
        size. ``release`` is given each piece of each weight once it is on
        the device, to drop the host's pages of it. A ``tuner`` narrows the
        decode step's designs and packs them into shared device
        configurations by what each costs (:attr:`tuning`).
        """
        decode = self.compile(coresident=tuner, **self.shapes(1))
        # A prompt's carried values start a decode step (generate()), where
        # the image has an Emit to write them with.
        feeds = decode if decode.emit is not None else None
        prompt = self.compile(feeds=feeds, **self.shapes(self.config.prefill_chunk))
        for version in (decode, prompt):
            version.load(release=release)
        self._prompt, self._decode = prompt, decode
        return self

    @property
    def tuning(self) -> Tuning | None:
        """What the ``tuner`` given to :meth:`load` chose for the decode
        step; None without one."""
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        return self._decode.tuning

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, ``(vocab_size,)``.

        ``tokens`` is the whole history. One more token than the last call's
        is a decode step on the caches; anything else is a prompt, run in
        chunks from the one holding the first token the caches do not.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n, L = tokens.size, self.config.max_seq_len
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        held = self._held(tokens)
        # Every call passes every per-call value; a version reads the ones
        # its operators bind. The token the device draws is the host's to
        # draw again.
        if held == n - 1 == self._seen.size:
            out, _ = self(token=int(tokens[-1]), position=n - 1, chunk=0, rows=1)
        else:
            for x, values in self._chunks(tokens, held):
                out, _ = self(x, **values)
        self._seen = tokens
        # The range holds the last token, so it runs at least once; a copy,
        # since the image's output buffer is rewritten by the next call.
        logits = out.numpy()  # pyright: ignore[reportPossiblyUnboundVariable]
        return np.array(logits).reshape(-1)

    def generate(
        self, tokens, num_tokens: int, sample: Sampler
    ) -> tuple[list[int], float, float]:
        """Draw ``num_tokens`` after ``tokens`` with the host out of the loop.

        The prompt runs from the host, a chunk at a time; its last chunk
        draws the first token, and its carried values, that token and the
        position after it, start the first decode step, and each step the
        next (:class:`CarriedLoop`). Every draw is the device's, from a row
        ``sample`` gives it before the prompt
        (:meth:`~.generation.Sampler.rows`), so the tokens are the ones
        :func:`~.generation.generate` draws on the host from the same logits
        and the same seed.

        Returns what that does: the tokens drawn, the seconds to the first
        and the mean seconds per token after it (NaN for one token).
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n, L = tokens.size, self.config.max_seq_len
        if not (0 < n and 0 < num_tokens and n + num_tokens - 1 <= L):
            raise ValueError(
                f"{n} tokens and {num_tokens} more to draw do not fit {L} rows"
            )
        if self._prompt is None or self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() before generate()")
        if self._loop is None:
            self._loop = CarriedLoop(self._prompt, self._decode, depth=2)
        start = time.perf_counter()
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        draws = np.zeros((L, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + num_tokens] = sample.rows(num_tokens, self._k_max())
        self._decode.write(self.draws, draws)
        # A prompt the caches partly hold runs from the chunk holding its
        # first new token; the last chunk starts the loop.
        for x, values in self._chunks(tokens, self._held(tokens)):
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

    def _held(self, tokens: np.ndarray) -> int:
        """How many of ``tokens`` the caches hold; never the last, which is
        always run.
        """
        held = min(tokens.size - 1, self._seen.size)
        same = np.append(tokens[:held] == self._seen[:held], False)
        return int(np.argmin(same))

    def _chunks(self, tokens: np.ndarray, held: int) -> Iterator[tuple]:
        """A prompt's calls, ``(x, values)``, from the chunk holding token
        ``held`` to the last. ``x`` is one buffer refilled per chunk: the
        rows past a chunk's tokens are never read.
        """
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
        """The largest top-k the device draws with: its Sample's."""
        assert self._decode is not None
        return next(
            s.op.k_max for s in self._decode.traced.steps if isinstance(s.op, Sample)
        )


class Oracle:
    """A decoder's forward pass in float32 on the host, on ``config``'s
    shape and RoPE table and ``weights``, as its :class:`CausalLM` takes
    them: the oracle the model is judged by.

    A plain causal pass over one token sequence, with no cache: the logits
    at position ``t`` of a causal pass over ``t + 1`` tokens are what a
    cached decode produces at step ``t``. It is numpy, not composed from the
    operators' references, on purpose: the graph's reference
    (``Graph.reference``) defines what the graph computes, so only an
    independent forward can catch a wiring mistake, a transposed layout or
    a softmax over the wrong length.

    A model subclasses it beside its :class:`CausalLM` with :meth:`layer`
    and :meth:`head`; the pass, RoPE (:meth:`rotate`) and attention
    (:meth:`attend`) are shared, as the graph's are. The weights are widened
    to float32 once, here (exactly: every bf16 is a float32), which is
    twice the checkpoint (5 GB for a 1B model), so an oracle is built to
    check with and dropped. The NPU's bf16 RoPE table is rounded from the
    same float32 one.
    """

    embedding: np.ndarray
    layers: list

    def __init__(self, config: Config, weights):
        self.config = config
        vars(self).update(vars(_widen(weights)))
        self.angles = config.angles()

    def layer(self, angles, w, x):
        """Layer ``w`` over ``x``, ``(n, emb_dim)``, whose positions' RoPE
        rows are ``angles``.
        """
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        """The logits of ``x``, one row."""
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens`` (``(n,)``), ``(vocab_size,)``,
        each token attending to itself and those before it.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        angles = self.angles[: tokens.size]
        x = self.embedding[tokens]
        for w in self.layers:
            x = self.layer(angles, w, x)
        return self.head(x[-1])

    @staticmethod
    def rotate(x, angles):
        """The two halves of each ``(n, heads, head_dim)`` row rotated by its
        position's ``angles``, the table's cosines and sines interleaved.
        """
        cos, sin = angles[:, None, ::2], angles[:, None, 1::2]
        x1, x2 = np.split(x, 2, axis=-1)
        return np.concatenate([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1)

    def attend(self, q, k, v):
        """Causal attention of ``q``, ``(n, n_heads, head_dim)``, over ``k``
        and ``v``, ``(n, n_kv_groups, head_dim)``. Returns ``(n, n_heads *
        head_dim)``.
        """
        n, H, D = q.shape
        # Each key and value head serves H // G consecutive query heads.
        k, v = (np.repeat(a, H // self.config.n_kv_groups, axis=1) for a in (k, v))
        # The softmax in place: the scores are (H, n, n), and a temporary
        # freed per layer is paid for again in page faults by the next.
        # Batched matmuls, not einsum's own loops: BLAS is 10x faster at 3k.
        p = q.transpose(1, 0, 2) @ k.transpose(1, 2, 0)
        p *= np.float32(1 / np.sqrt(D))
        p += np.triu(np.full((n, n), -np.inf, dtype=np.float32), k=1)
        p -= p.max(axis=-1, keepdims=True)
        np.exp(p, out=p)
        p /= p.sum(axis=-1, keepdims=True)
        return (p @ v.transpose(1, 0, 2)).transpose(1, 0, 2).reshape(n, H * D)


def _widen(value):
    """``value``'s arrays in float32, through its namespaces and lists."""
    if isinstance(value, np.ndarray):
        return value.astype(np.float32)
    if isinstance(value, list):
        return [_widen(v) for v in value]
    if isinstance(value, SimpleNamespace):
        return SimpleNamespace(**{k: _widen(v) for k, v in vars(value).items()})
    return value
