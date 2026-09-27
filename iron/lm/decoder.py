# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

:class:`CausalLM` is the part every such model shares: the body over
``x``, the embedded tokens, ``(rows, emb_dim)``, which branches on that
static shape; the key and value caches; attention over them
(:meth:`CausalLM.attend`); and ``logits(tokens)``. A model subclasses it
with its ``layer`` and its ``head``.

One row is a decode step: attention against the caches, the row written
into them at ``cache_offset``, the softmax masked to ``vector_size`` keys.
``max_seq_len`` rows are a prompt, of which a call runs the first ``rows``
(:func:`prompt_rows`): causal MHA masked to the ``vector_size`` tokens of
the prompt, the caches written from row zero, and the head for row
``last`` alone.

Each shape compiles its own version, and every version runs in the graph's
one scratch arena (:mod:`iron.common.graph.compiled`): the weights and the
caches are uploaded once, and the caches a prompt writes are the ones the
next decode step reads.

:class:`Oracle` is the same model's float32 forward pass on the host, the
reference it is judged by; a model subclasses it too, with a numpy
``layer`` and ``head``, and names it as its ``oracle``.
"""

import dataclasses
import math
from types import SimpleNamespace

import numpy as np
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.graph import Handle
from iron.operators.copy import Copy
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.repeat import Repeat
from iron.operators.rope import RopeScaling, rope_angles
from iron.operators.softmax import Softmax
from iron.operators.transpose import Transpose


@dataclasses.dataclass(frozen=True)
class Config:
    """A decoder's shape. ``max_seq_len`` is the rows the caches hold,
    prompt and generated tokens together; ``rope_scaling`` rescales the RoPE
    frequencies (Llama 3.2's is ``LLAMA_3_2``).
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

    def angles(self) -> np.ndarray:
        """The RoPE table, ``(max_seq_len, head_dim)`` float32."""
        return rope_angles(
            self.head_dim, self.max_seq_len, self.rope_base, self.rope_scaling
        )


def prompt_rows(n: int, max_seq_len: int) -> int:
    """The rows a prompt of ``n`` tokens runs: ``n`` rounded up to what MHA's
    pipelines take at once (64 rows each, eight of them at full length),
    which the GEMMs' row block divides, at most ``max_seq_len``.
    """
    unit = 64 * min(8, max_seq_len // 64)
    return min(-(-n // unit) * unit, max_seq_len)


@dataclasses.dataclass
class Step:
    """What one call runs: a ``prompt`` or a decode step, the RoPE rows of
    its positions (``angles``), and its per-call values.
    """

    prompt: bool
    angles: Handle
    rows: Scratchpad
    cache_offset: Scratchpad
    vector_size: Scratchpad


class CausalLM(iron.Graph):
    """A decoder on ``config``'s shape and ``weights``, whose top-level
    fields become the model's (named as they are: ``layers.3.q``). It needs
    ``embedding``, the rows the host looks tokens up in, and ``layers``;
    ``keys[i]`` and ``values[i]`` are each layer's cache, ``(n_kv_groups,
    max_seq_len, head_dim)``.

    A subclass gives :meth:`layer` and :meth:`head`, its ``profile``, and
    its ``oracle``, the :class:`Oracle` it is checked against.
    """

    embedding: np.ndarray
    layers: list
    oracle: "type[Oracle]"

    def __init__(self, config: Config, weights):
        self.config = config
        vars(self).update(vars(weights))
        G, L, D = config.n_kv_groups, config.max_seq_len, config.head_dim
        self.keys = [iron.state((G, L, D)) for _ in self.layers]
        self.values = [iron.state((G, L, D)) for _ in self.layers]
        # 1/sqrt(head_dim) over every score, as the elementwise multiply takes it.
        self.scale = np.full((config.n_heads, L), 1 / math.sqrt(D), dtype=bfloat16)
        # A float32 table would be another input signature, another compile.
        self.angles = config.angles().astype(bfloat16)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches

    def layer(self, step: Step, i: int, weights, x):
        """Layer ``i`` over ``x``, ``(rows, emb_dim)``, with its ``weights``."""
        raise NotImplementedError(f"{type(self).__name__} defines no layer()")

    def head(self, x):
        """The logits of ``x``, one row."""
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def body(
        self,
        x,
        angles,
        *,
        rows: Scratchpad[np.int32],
        cache_offset: Scratchpad[np.int32],
        vector_size: Scratchpad[np.int32],
        last: Scratchpad[np.int32],
    ):
        prompt = x.shape[0] > 1
        if prompt:
            # Every operator below runs the rows of this call alone.
            x, angles = x[:rows], angles[:rows]
        step = Step(prompt, angles, rows, cache_offset, vector_size)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        if prompt:
            x = Copy(x[last]).reshape(1, self.config.emb_dim)  # all the host reads
        return self.head(x)

    def attend(self, step: Step, i: int, q, k, v):
        """Causal attention of the call's rows over layer ``i``'s caches,
        once ``k`` and ``v`` are written into them: ``q`` and ``k``, rotated,
        ``(rows * n_heads, head_dim)`` and ``(rows * n_kv_groups,
        head_dim)``, ``v`` as projected. Returns ``(rows, n_heads *
        head_dim)``.
        """
        H, G, D = self.config.n_heads, self.config.n_kv_groups, self.config.head_dim
        keys, values = self.keys[i], self.values[i]
        n = q.shape[0] // H
        if step.prompt:
            # The heads interleaved per token as the projection wrote them,
            # into the first rows of the cache's (G, L, D).
            for x, cache in ((k, keys), (v, values)):
                Copy(
                    x.reshape(n, G, D).transpose(1, 0, 2),
                    cache[:, : step.rows],
                    tile_size=1024,
                )
            o = MHA(
                q.reshape(n, H, D),
                k.reshape(n, G, D),
                v.reshape(n, G, D),
                heads_interleaved=True,
                s_q=step.vector_size,
                s_kv=step.vector_size,
            )
            return o.reshape(n, H * D)
        Copy(k, keys[:, step.cache_offset])
        Copy(v.reshape(G, D), values[:, step.cache_offset])
        # Every head sees its group's keys and values.
        k_all = Repeat(keys, repeat=H // G)
        v_all = Repeat(values, repeat=H // G)
        scores = ElementwiseMul(GEMV(k_all, q), self.scale)
        # Masked from the context length on: the cache's unwritten tail
        # contributes nothing.
        weights = Softmax(scores, vector_size=step.vector_size)
        return GEMV(Transpose(v_all), weights).reshape(1, H * D)

    # -- on the host -----------------------------------------------------------

    def shapes(self, rows: int) -> dict:
        """The input shapes of the version that runs ``rows`` tokens."""
        return dict(x=(rows, self.config.emb_dim), angles=(rows, self.config.head_dim))

    def load(self, release=None) -> "CausalLM":
        """Compile and load the decode and prompt versions, weights uploaded.

        Both before the first call, so the arena is made once at its final
        size. ``release`` is given each piece of each weight once it is on
        the device, to drop the host's pages of it.
        """
        for rows in (1, self.config.max_seq_len):
            self.compile(**self.shapes(rows))
        for version in self.versions.values():
            version.load(release=release)
        return self

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, ``(vocab_size,)``.

        ``tokens`` is the whole history. One more token than the last call's
        is a decode step on the caches; anything else is a prompt.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n, seen, L = tokens.size, self._seen.size, self.config.max_seq_len
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        # Every call passes every per-call value; a version reads the ones
        # its operators bind.
        if n == seen + 1 and np.array_equal(tokens[:seen], self._seen):
            out = self(
                self.embedding[tokens[seen:]],
                self.angles[seen:n],
                rows=1,
                cache_offset=seen,
                vector_size=n,
                last=0,
            )
        else:
            x = np.zeros((L, self.config.emb_dim), dtype=bfloat16)
            x[:n] = self.embedding[tokens]
            out = self(
                x,
                self.angles,
                rows=prompt_rows(n, L),
                cache_offset=0,
                vector_size=n,
                last=n - 1,
            )
        self._seen = tokens
        # A copy: the image's output buffer is rewritten by the next call.
        return np.array(out.numpy()).reshape(-1)


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
        p = np.einsum("qhd,khd->hqk", q, k)
        p *= np.float32(1 / np.sqrt(D))
        p += np.triu(np.full((n, n), -np.inf, dtype=np.float32), k=1)
        p -= p.max(axis=-1, keepdims=True)
        np.exp(p, out=p)
        p /= p.sum(axis=-1, keepdims=True)
        return np.einsum("hqk,khd->qhd", p, v).reshape(n, H * D)


def _widen(value):
    """``value``'s arrays in float32, through its namespaces and lists."""
    if isinstance(value, np.ndarray):
        return value.astype(np.float32)
    if isinstance(value, list):
        return [_widen(v) for v in value]
    if isinstance(value, SimpleNamespace):
        return SimpleNamespace(**{k: _widen(v) for k, v in vars(value).items()})
    return value
