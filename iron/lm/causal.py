# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

A call with no tensor is a decode step; ``prefill_chunk`` token ``ids`` are
a prompt chunk, of which a call runs the first ``rows``, their rows of the
embedding table gathered on the device, in a full ELF or an xclbin. Both
draw the next token on the device and carry it and ``position + 1`` into
the next call.
Both attend with ``MHA``. Where the decode step is not a full ELF (NPU1, or
``full_elf=False``) there is no device loop: the host starts each step
on the token the last one drew.
"""

import dataclasses
import logging
import time
from collections.abc import Iterator
from functools import partial
from typing import Any, ClassVar

import aie.utils as aie_utils
import numpy as np
from aie.iron.kernels.sample import ROW_WORDS
from ml_dtypes import bfloat16

import iron
from iron import Carried, Scratchpad
from iron.common.graph import CarriedLoop, CompiledGraph, Handle
from iron.common.graph.handle import State
from iron.common.graph.tuner import Tuning
from iron.tune.probe import Call, Point
from iron.operators.copy import Copy
from iron.operators.mha import MHA
from iron.operators.sample import Sample

from .base import DecoderConfig, Model, Oracle
from .generation import Sampler

logger = logging.getLogger(__name__)


def contexts(top: int, count: int, unit: int) -> list[tuple[float, int]]:
    """At most ``count`` contexts halving down from ``top``, multiples of
    ``unit``, ascending, each weighted by the share of a uniform context in
    ``(0, top]`` nearest it (the trapezoid rule): the weights sum to 1.

    Raises:
        ValueError: ``top`` is not a positive multiple of ``unit``.
    """
    if top < unit or top % unit:
        raise ValueError(f"the context {top} is not a multiple of {unit}")
    found = [top]
    while len(found) < count and found[-1] // 2 >= unit and found[-1] // 2 % unit == 0:
        found.append(found[-1] // 2)
    found.reverse()
    edges = [0] + [(a + b) / 2 for a, b in zip(found, found[1:])] + [top]
    return [((hi - lo) / top, c) for lo, hi, c in zip(edges, edges[1:], found)]


@dataclasses.dataclass
class DecodeStep:
    prompt: bool
    # None turns nothing.
    angles: Handle | None
    # A per-call value in a trace, its number in the reference.
    chunk: Any
    rows: Any
    position: Any
    # The encoder's rows a cross attention reads (``EncoderDecoder``).
    source: Any = None


@dataclasses.dataclass(frozen=True)
class Checkpoints:
    """A state a decoder carries from position to position, a slot per
    prompt-chunk boundary: slot ``k`` holds it after the positions of chunk
    ``k - 1`` run so far, slot 0 (never written) before the sequence.
    """

    slots: State
    chunk: int

    @classmethod
    def of(
        cls, shape: tuple[int, ...], max_seq_len: int, chunk: int, dtype=bfloat16
    ) -> "Checkpoints":
        """A state of ``shape``, a slot for every boundary of ``chunk``-position
        prompt chunks up to ``max_seq_len`` positions.

        Raises:
            ValueError: ``chunk`` is not a power of two, which a decode step's
                slot (``position // chunk``) needs.
        """
        if chunk < 1 or chunk & (chunk - 1):
            raise ValueError(
                f"Checkpoints: a {chunk}-position chunk is no power of two"
            )
        slots = (max_seq_len - 1) // chunk + 2
        return cls(iron.state((slots, *shape), dtype), chunk)

    def at(self, step: DecodeStep) -> tuple[Handle, Handle]:
        """The slot ``step`` reads and the slot it writes, in a graph's body: a
        prompt chunk's boundary and the next; a decode step's chunk's own, but
        at the chunk's first position the boundary before it.
        """
        if step.prompt:
            return self.slots[step.chunk], self.slots[step.chunk + 1]
        p = step.position
        return self.slots[(p - 1) // self.chunk + 1], self.slots[p // self.chunk + 1]

    def slot(self, position: int) -> int:
        """The slot holding the state after the first ``position`` positions."""
        return 0 if position == 0 else (position - 1) // self.chunk + 1


class CausalLM(Model):
    """A decoder on ``config``'s shape; a subclass gives ``head`` and ``oracle``.

    The caches are ``(max_seq_len, n_kv_groups, head_dim)`` so no descriptor
    steps by the context; a prompt chunk is a run of them
    (``cache[s : s + C][:rows]``), the last one short where the chunk does
    not divide ``max_seq_len``. A decode step attends with ``MHA`` of one
    query, which costs the context, not the cache.

    Args:
        config: The decoder's shape.
        weights: The checkpoint's tree (``Checkpoint.tree``).
        decoder: The decoder's module of ``weights``, whose ``embed_tokens``
            and ``layers`` are read here, the rest by the subclass; None is
            ``weights.model``.
    """

    layers: list
    oracle: "type[Oracle]"
    # The per-call value bounding a prompt chunk's rows.
    bound: ClassVar[str] = "rows"

    def __init__(self, config: DecoderConfig, weights, decoder=None):
        self.config = config
        self.weights = weights
        self.decoder = weights.model if decoder is None else decoder
        self.layers = self.decoder.layers
        if len(self.layers) != config.n_layers:
            raise ValueError(
                f"the checkpoint has {len(self.layers)} layers, the config "
                f"{config.n_layers}"
            )
        G, L, D = config.n_kv_groups, config.max_seq_len, config.head_dim
        # By layer: the key and value caches of a module that attends, and the
        # states a recurrent mixer carries position to position, by name.
        self.keys: dict[int, State] = {}
        self.values: dict[int, State] = {}
        self.recurrent: dict[int, dict[str, Checkpoints]] = {}
        for i, w in enumerate(self.layers):
            if "self_attn" in vars(w):
                self.keys[i] = iron.state((L, G, D))
                self.values[i] = iron.state((L, G, D))
            if "mamba" in vars(w):
                ssm = config.layer(i).ssm
                if ssm is None:
                    raise ValueError(f"layer {i} holds mamba and the config no ssm")
                self.recurrent[i] = {
                    name: Checkpoints.of(shape, L, config.prefill_chunk, dtype)
                    for name, (shape, dtype) in ssm.states().items()
                }
        angles = config.angles()
        self.rope = None if angles is None else iron.weight(angles.astype(bfloat16))
        # Zero until the host writes draws: a row of zeros is greedy.
        self.draws = iron.state((L, ROW_WORDS), np.int32)
        self.drawn = iron.state((L,), np.int32)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches
        self._prompt: CompiledGraph | None = None
        self._decode: CompiledGraph | None = None
        self._placed: CompiledGraph | None = None
        self._placeholders: tuple[int, ...] = ()
        # By the version a device loop starts from, its loop.
        self._loops: dict[int, CarriedLoop] = {}

    def layer(self, step: DecodeStep, i: int, weights, x):
        """Layer ``i`` on ``x``: ``config.layer(i)``, attending over the caches."""
        attend = partial(self.attend, step, i)
        return self.config.layer(i).step(weights, x, attend, step.angles)

    def head(self, x):
        raise NotImplementedError(f"{type(self).__name__} defines no head()")

    def embed(self, x):
        return x

    def positions(self, x, step: DecodeStep):
        """``x``, the rows ``step`` runs, with the model's absolute positions
        placed; unchanged by default.
        """
        return x

    def lookup(self, ids):
        """The embedding rows of ``ids``, bounded as ``ids`` is."""
        return Copy.step(iron.weight(self.decoder.embed_tokens.weight)[ids])

    def body(
        self,
        ids=None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        chunk: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
    ):
        if ids is not None:
            return self.from_rows(
                self.lookup(ids[:rows]),
                token=token,
                position=position,
                chunk=chunk,
                rows=rows,
            )
        embedding = iron.weight(self.decoder.embed_tokens.weight)
        x = Copy.step(embedding[token]).reshape(1, self.config.emb_dim)
        return self.forward(x, prompt=False, position=position, chunk=chunk, rows=rows)

    def from_rows(self, x, *, token, position, chunk, rows):
        """A prompt chunk's call on its embedding rows ``x``, bounded to
        ``rows``, in place of its ids' lookup; ``token`` is the decode
        step's, unread here.
        """
        return self.forward(x, prompt=True, position=position, chunk=chunk, rows=rows)

    def forward(self, x, *, prompt: bool, position, chunk, rows, source=None):
        """The layers, the head and the draw over ``x``: a prompt chunk's
        rows, else the decode step's one at ``position``; ``source`` is the
        step's (``DecodeStep``).
        """
        c = self.config
        C, A = c.prefill_chunk, c.rope_width
        if self.rope is None:
            angles = None
        elif prompt:
            angles = Copy.step(self.rope[chunk * C : chunk * C + C][:rows])
        else:
            angles = Copy.step(self.rope[position]).reshape(1, A)
        step = DecodeStep(prompt, angles, chunk, rows, position, source)
        x = self.positions(self.embed(x), step)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        if prompt:
            x = Copy.step(x[rows - 1]).reshape(
                1, c.emb_dim
            )  # the last row's logits alone
        logits = self.head(x)
        _, drawn = Sample.step(
            logits.reshape(c.vocab_size),
            self.draws,
            self.drawn,
            row=position * ROW_WORDS,
            at=position,
        )
        return logits, iron.carry(token=drawn, position=position + 1)

    def attend(
        self,
        step: DecodeStep,
        i: int,
        q,
        k,
        v,
        *,
        scale: float | None = None,
        window: int | None = None,
    ):
        """Write ``k`` and ``v`` ``(rows, groups, head_dim)`` into layer
        ``i``'s caches and attend ``q`` ``(rows, heads, head_dim)`` over them
        causally, the logits scaled by ``scale`` (MHA's ``1 / sqrt(head_dim)``
        if None).

        Raises:
            ValueError: A ``window`` is given: none is built over the caches.
        """
        if window is not None:
            raise ValueError(f"CausalLM.attend: no {window}-position window")
        c = self.config
        G, D, C = c.n_kv_groups, c.head_dim, c.prefill_chunk
        keys, values = self.keys[i], self.values[i]
        n, H, _ = q.shape
        for x, cache in ((k, keys), (v, values)):
            if step.prompt:
                start = step.chunk * C
                Copy.step(x, cache[start : start + C][: step.rows])
            else:
                Copy.step(x.reshape(G, D), cache[step.position])
        span = np.s_[: step.position + 1]
        o = MHA.step(
            q,
            keys[span],
            values[span],
            heads_interleaved=True,
            kv_interleaved=True,
            scale=scale,
        )
        return o.reshape(n, H * D)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: the decode step's (none), then
        the prompt chunk's token ids.
        """
        return [{}, dict(ids=((self.config.prefill_chunk,), np.int32))]

    def load(
        self,
        *,
        release=None,
        tuner=None,
        full_elf: bool | None = None,
        dev=None,
    ) -> "CausalLM":
        """Compile and load both versions before the first call, so the arena is made once.

        Args:
            release: Given each piece of each weight once it is on the device.
            tuner: Folds, narrows and packs each version's designs by cost.
            full_elf: Both versions' packaging (``Graph.compile``).
            dev: The device both versions are compiled for, else the current
                one.
        """
        super().load(release=release, tuner=tuner, full_elf=full_elf, dev=dev)
        self.use(*self.versions.values())
        return self

    def use(
        self,
        decode: CompiledGraph,
        prompt: CompiledGraph,
        placed: CompiledGraph | None = None,
        placeholders: tuple[int, ...] = (),
    ) -> None:
        """Run ``logits`` and ``generate`` on these versions: this model's
        own, or those of a graph tracing it in their bodies (a multimodal
        model's), in one arena, each prompt version feeding ``decode``.

        Args:
            decode: The decode step.
            prompt: A prompt chunk, on ``ids``.
            placed: A prompt chunk holding any of ``placeholders``, on its
                ``ids`` and ``before``, the count of each placeholder before
                the chunk.
            placeholders: The placeholder tokens, in ``before``'s order.
        """
        self._decode, self._prompt = decode, prompt
        self._placed, self._placeholders = placed, tuple(placeholders)
        self._loops = {}
        self._seen = np.empty(0, dtype=np.int64)
        if not decode.plan.full_elf:
            logger.info("%s", decode.plan.report("decode"))

    def call_values(self) -> dict:
        """The per-call values every call gives beyond the token, position,
        chunk and rows: none by default.
        """
        return {}

    def __call__(self, ids=None, before=None, **values) -> Any:
        """One call of the prompt version on ``ids`` (``prompt_ids``), of the
        placed one on ``ids`` and ``before`` (``use``), else of the decode
        step, with ``call_values`` where ``values`` give none of their own.

        Raises:
            RuntimeError: Neither version is loaded: ``load()`` first, which
                compiles them with the tuner and packaging asked for.
        """
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        values = {**self.call_values(), **values}
        if ids is None:
            return self._decode(**values)
        if before is not None:
            assert self._placed is not None
            return self._placed(ids, before, **values)
        assert self._prompt is not None
        return self._prompt(ids, **values)

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

    def tune_calls(
        self,
        sample: Sampler,
        position: int,
        token: int,
        context: int,
        count: int,
    ) -> list[Call]:
        """The calls the model's designs are measured in on the current device:
        the decode step at ``position`` and ``token``, and the prompt chunk at
        a whole first chunk, each as traced and with each fold it admits, Sample
        on the draw rows ``sample`` gives. Each is priced over ``contexts`` up to
        ``context``, ``count`` of them: the decode step at their last position,
        the prompt chunk as the whole chunk ending there.
        """
        dev = aie_utils.ensure_current_device()
        C = self.config.prefill_chunk
        decode_shapes, prompt_shapes = self.shapes()
        versions = [
            (
                decode_shapes,
                dict(position=position, token=token),
                [
                    Point(w, dict(position=c - 1, token=token))
                    for w, c in contexts(context, count, 1)
                ],
            ),
            (
                prompt_shapes,
                dict(position=C - 1, token=token, chunk=0, rows=C),
                [
                    Point(
                        w, dict(position=c - 1, token=token, chunk=c // C - 1, rows=C)
                    )
                    for w, c in contexts(context, count, C)
                ],
            ),
        ]
        out = []
        for shapes, values, points in versions:
            traced = self.trace(**shapes)
            # Sample's work follows its draw row's temperature and top-k: measure
            # it at the rows generation writes, not at random words.
            [k_max] = {s.op.k_max for s in traced.steps if isinstance(s.op, Sample)}
            _, draws = traced.states[id(self.draws)]
            rows = sample.rows(self.config.max_seq_len, k_max)
            out += Call.admitted(traced, dev, values, {draws.name: rows}, points)
        return out

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
            for inputs, values in self._chunks(tokens, held):
                out, _ = self(*inputs, **values)
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
        start = time.perf_counter()
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        draws = np.zeros((L, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + num_tokens] = sample.rows(num_tokens, self._k_max())
        self._decode.write(self.draws, draws)
        held = self._held(tokens)
        self._seen = tokens[: held // C * C]
        for inputs, values in self._chunks(tokens, held):
            if not loop or values["position"] < n - 1:
                _, carry = self(*inputs, **values)
            else:
                version = self._prompt if len(inputs) == 1 else self._placed
                started = self._loops.setdefault(
                    id(version), CarriedLoop(version, self._decode, depth=2)
                )
                started.start(*inputs, **values)
        first = time.perf_counter()
        if loop:
            for _ in started.steps(num_tokens - 1):
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

    def forget(self, position: int) -> None:
        """Hold nothing the caches have from ``position`` on: the next call
        runs from there, as a change before it (a placeholder's soft tokens)
        would leave them stale.
        """
        self._seen = self._seen[:position]

    def _tokens(self, tokens) -> np.ndarray:
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
        """Each prompt chunk from the first the caches do not hold: its
        inputs, ``ids`` and for a chunk holding a placeholder ``before``, and
        its per-call values.
        """
        n, C = tokens.size, self.config.prefill_chunk
        for begin in range(held // C * C, n, C):
            end = min(begin + C, n)
            ids = self.prompt_ids(tokens[begin:end])
            values = dict(
                self.call_values(),
                token=int(tokens[end - 1]),
                position=end - 1,
                chunk=begin // C,
                rows=end - begin,
            )
            placed = np.isin(tokens[begin:end], self._placeholders).any()
            if self._placed is None or not placed:
                yield (ids,), values
                continue
            before = np.array(
                [np.count_nonzero(tokens[:begin] == t) for t in self._placeholders],
                np.int32,
            )
            yield (ids, before), values

    def _k_max(self) -> int:
        assert self._decode is not None
        return next(
            s.op.k_max for s in self._decode.traced.steps if isinstance(s.op, Sample)
        )
