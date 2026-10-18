# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

A call with no tensor is a decode step; ``prefill_chunk`` token ``ids`` are
a prompt chunk from position ``start``, of which a call runs the first
``rows``, their rows of the
embedding table gathered on the device, in a full ELF or an xclbin. Both
draw the next token on the device and carry it and ``position + 1`` into
the next call.
Both attend with ``MHA``. Where the decode step is not a full ELF (NPU1, or
``full_elf=False``) there is no device loop: the host starts each step
on the token the last one drew.
"""

import argparse
import dataclasses
import logging
import time
from collections.abc import Iterator
from functools import partial
from pathlib import Path
from typing import Any

import numpy as np
from aie.iron.kernels.sample import ROW_WORDS
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Carried, Scratchpad
from iron.common.graph import CarriedLoop, CompiledGraph, Handle
from iron.common.graph.handle import State
from iron.tune.autotune import Call, Point
from iron.operators.copy import Copy
from iron.operators.mha import MHA
from iron.operators.sample import Sample

from .checkpoint import Checkpoint, renamed
from .config import DecoderConfig
from .model import Model
from .cli import sampling_arguments
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
    # The first position the call runs: a per-call value in a trace, its
    # number in the reference.
    start: Any
    rows: Any
    position: Any
    # The encoder's rows a cross attention reads (``EncoderDecoder``).
    source: Any = None
    # The rows the embedding gave, and the ids (a prompt chunk's, bounded) or
    # the token (a decode step's) they are of; None for rows given.
    embeddings: Any = None
    ids: Any = None


@dataclasses.dataclass(frozen=True)
class Checkpoints:
    """A state a decoder carries from position to position, a slot per
    prompt-chunk boundary: slot ``k`` holds it after the positions up to
    ``k * chunk`` run so far, slot 0 (never written) before the sequence.
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
        """The slot ``step`` reads, the state before its first position, and
        the slot it writes, the state after its last, in a graph's body. A
        call ends within the chunk it starts in (``CausalLM`` splits them).
        """
        C = self.chunk
        return self.slots[(step.start - 1) // C + 1], self.slots[step.position // C + 1]

    def restart(self, held: int, ran: int) -> int:
        """Where a call may start to change the positions from ``held`` on,
        after ``ran`` positions ran: there where the last call ended, else at
        the boundary before it.
        """
        return held if held == ran else held // self.chunk * self.chunk

    def slot(self, position: int) -> int:
        """The slot holding the state after the first ``position`` positions."""
        return 0 if position == 0 else (position - 1) // self.chunk + 1


class CausalLM(Model):
    """A decoder on ``config``'s shape.

    The caches are ``(max_seq_len, num_key_value_heads, head_dim)`` so no descriptor
    steps by the context; a prompt chunk is a run of them
    (``cache[s : s + C][:rows]``), the last one short where the chunk does
    not divide ``max_seq_len``. A decode step attends with ``MHA`` of one
    query, which costs the context, not the cache.

    Args:
        config: The decoder's shape.
        weights: The checkpoint's tree (``Checkpoint.tree``).
        decoder: The decoder's module of ``weights``, whose ``embed_tokens``,
            ``layers`` and ``norm`` are read here; None is ``weights.model``.

    ``final_norm``, the norm module ``head`` reads, is ``decoder.norm``;
    a subclass sets it where the checkpoint names it otherwise.
    """

    layers: list

    def __init__(self, config: DecoderConfig, weights, decoder=None):
        self.config = config
        self.weights = weights
        self.decoder = weights.model if decoder is None else decoder
        self.layers = [
            self.sanitize(renamed(w, self.renames)) for w in self.decoder.layers
        ]
        self.final_norm = getattr(self.decoder, "norm", None)
        if len(self.layers) != config.num_hidden_layers:
            raise ValueError(
                f"the checkpoint has {len(self.layers)} layers, the config "
                f"{config.num_hidden_layers}"
            )
        L = config.max_seq_len
        # By layer: the key and value caches of a module that attends with its
        # own, and the states a recurrent mixer carries position to position,
        # by name.
        self.keys: dict[int, State] = {}
        self.values: dict[int, State] = {}
        self.recurrent: dict[int, dict[str, Checkpoints]] = {}
        for i, w in enumerate(self.layers):
            if "self_attn" in vars(w):
                a = config.layer(i).attention
                self.keys[i] = iron.state((L, a.groups, a.head_dim))
                self.values[i] = iron.state((L, a.groups, a.head_dim))
        angles = config.angles()
        long = config.long_angles()
        # LongRoPE's: a prompt passing it reads the second table, stacked after.
        self.long_past = None if long is None else long[0]
        if long is not None:
            angles = np.concatenate([angles, long[1]])
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
        return self.config.layer(i)(weights, x, attend, step.angles)

    def head(self, x):
        """The final norm, then the output head (the embedding, if tied)."""
        c = self.config
        x = c.norm()(self.final_norm, x)
        if c.tie_word_embeddings:
            return F.linear(x, self.decoder.embed_tokens.weight)
        return F.linear(x, self.weights.lm_head.weight)

    def positions(self, x, step: DecodeStep):
        """``x``, the rows ``step`` runs, with the model's absolute positions
        placed; unchanged by default.
        """
        return x

    def angles(self, *, prompt: bool, position, start, rows, rope_start):
        """The RoPE angles of a step's rows, a row a position, as ``layer``
        reads them: a prompt call's from ``start``, or from ``rope_start``
        where a second table is stacked (``long_angles``), else the decode
        step's at ``position``; None turns nothing.
        """
        c = self.config
        C, A = c.prefill_chunk, c.rope_width
        if self.rope is None:
            return None
        if prompt:
            begin = start if self.long_past is None else rope_start
            return Copy.step(self.rope[begin : begin + C][:rows])
        return Copy.step(self.rope[position]).reshape(1, A)

    def lookup(self, ids):
        """The embedding rows of ``ids``, bounded as ``ids`` is, or of the
        decode step's token.
        """
        return Copy.step(iron.weight(self.decoder.embed_tokens.weight)[ids])

    def body(
        self,
        ids=None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        start: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
        rope_start: Scratchpad[np.int32],
    ):
        if ids is not None:
            bounded = ids[:rows]
            return self.forward(
                self.lookup(bounded),
                prompt=True,
                position=position,
                start=start,
                rows=rows,
                rope_start=rope_start,
                ids=bounded,
            )
        x = self.lookup(token).reshape(1, self.config.hidden_size)
        return self.forward(
            x,
            prompt=False,
            position=position,
            start=start,
            rows=rows,
            rope_start=rope_start,
            ids=token,
        )

    def from_rows(self, x, *, token, position, start, rows, rope_start):
        """A prompt chunk's call on its embedding rows ``x``, bounded to
        ``rows``, in place of its ids' lookup; ``token`` is the decode
        step's, unread here.
        """
        return self.forward(
            x,
            prompt=True,
            position=position,
            start=start,
            rows=rows,
            rope_start=rope_start,
        )

    def forward(
        self,
        x,
        *,
        prompt: bool,
        position,
        start,
        rows,
        rope_start,
        source=None,
        ids=None,
    ):
        """The layers, the head and the draw over ``x``: a prompt call's rows
        from ``start``, else the decode step's one at ``position``; ``source``
        and ``ids`` are the step's (``DecodeStep``).
        """
        c = self.config
        angles = self.angles(
            prompt=prompt,
            position=position,
            start=start,
            rows=rows,
            rope_start=rope_start,
        )
        # A decode step's one position is its start.
        start = start if prompt else position
        step = DecodeStep(prompt, angles, start, rows, position, source, x, ids)
        x = self.positions(x, step)
        for i, weights in enumerate(self.layers):
            x = self.layer(step, i, weights, x)
        if prompt:
            x = Copy.step(x[rows - 1]).reshape(
                1, c.hidden_size
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
        C = c.prefill_chunk
        keys, values = self.keys[i], self.values[i]
        _, G, D = keys.shape
        n, H, _ = q.shape
        for x, cache in ((k, keys), (v, values)):
            if step.prompt:
                cache[step.start : step.start + C][: step.rows] = x
            else:
                cache[step.position] = x.reshape(G, D)
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

    def loaded(self, versions: list) -> None:
        """Run ``logits`` and ``generate`` on the decode step and the
        prompt chunk (``use``).
        """
        self.use(*versions)

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
        start, rows and rope_start: none by default.
        """
        return {}

    def __call__(self, ids=None, before=None, **values) -> Any:
        """One call of the prompt version on ``ids`` (``prompt_ids``), of the
        placed one on ``ids`` and ``before`` (``use``), else of the decode
        step, with ``call_values`` where ``values`` give none of their own.

        Raises:
            RuntimeError: Neither version is loaded: ``load_versions()``
                first, which compiles them with the packaging asked for.
        """
        if self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load_versions() first")
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
            raise RuntimeError(f"{type(self).__name__}: load_versions() first")
        return self._decode.emit is not None

    @classmethod
    def tune_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """The flags ``tune_calls`` follows from: the checkpoint whose header
        gives the weights' shapes, the decode step's position and token, the
        contexts attention over the cache is timed at, and the sampling
        Sample is timed at.
        """
        parser.add_argument(
            "--checkpoint",
            type=Path,
            required=True,
            help="the .safetensors checkpoint, or a sharded one's "
            "model.safetensors.index.json, of which only the header is read",
        )
        parser.add_argument(
            "--position",
            type=int,
            default=256,
            help="the decode position the decode step's designs are timed at: "
            "what their per-call values follow from (default: 256)",
        )
        parser.add_argument(
            "--token",
            type=int,
            default=0,
            help="the token the step embeds (default: 0)",
        )
        parser.add_argument(
            "--context",
            type=int,
            default=8192,
            help="the longest context a design whose work follows it is timed "
            "at, a multiple of the prompt chunk (default: 8192)",
        )
        parser.add_argument(
            "--points",
            type=int,
            default=6,
            help="how many contexts up to --context it is timed at, each "
            "timed per setting: their cost grows with it (default: 6)",
        )
        sampling_arguments(parser)

    @classmethod
    def tune_calls(
        cls, parser: argparse.ArgumentParser, args: argparse.Namespace
    ) -> list[Call]:
        """The calls the model's designs are timed in, on weights it never
        reads (``tune_arguments``'s flags): the decode step at ``--position``
        and ``--token``, and the prompt chunk at a whole first chunk, Sample
        on the draw rows the sampling gives. Each is timed over ``contexts``
        up to ``--context``, ``--points`` of them: the decode step at their
        last position, the prompt chunk as the whole chunk ending there.
        """
        config = cls.default_config(args.checkpoint)
        if args.context > config.max_seq_len:
            parser.error(
                f"--context {args.context} is past max_seq_len {config.max_seq_len}"
            )
        model = cls(config, Checkpoint(args.checkpoint).tree("unread"))
        sample = Sampler(args.temperature, args.top_k)
        position, token = args.position, args.token
        C = model.config.prefill_chunk
        decode_shapes, prompt_shapes = model.shapes()
        versions = [
            (
                decode_shapes,
                dict(position=position, token=token),
                [
                    Point(w, dict(position=c - 1, token=token))
                    for w, c in contexts(args.context, args.points, 1)
                ],
            ),
            (
                prompt_shapes,
                dict(position=C - 1, token=token, start=0, rows=C, rope_start=0),
                [
                    Point(
                        w,
                        dict(
                            position=c - 1,
                            token=token,
                            start=c - C,
                            rows=C,
                            rope_start=c - C,
                        ),
                    )
                    for w, c in contexts(args.context, args.points, C)
                ],
            ),
        ]
        out = []
        for shapes, values, points in versions:
            traced = model.trace(**shapes)
            # Sample's work follows its draw row's temperature and top-k: measure
            # it at the rows generation writes, not at random words.
            [k_max] = {s.op.k_max for s in traced.steps if isinstance(s.op, Sample)}
            _, draws = traced.states[id(model.draws)]
            rows = sample.rows(model.config.max_seq_len, k_max)
            out.append(Call(traced, values, {draws.name: rows}, points))
        return out

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
        n, L = tokens.size, self.config.max_seq_len
        if not 0 < n <= L:
            raise ValueError(f"{n} tokens do not fit {L} rows")
        held = self._held(tokens)
        if held == n - 1 == self._seen.size:
            out, _ = self(
                token=int(tokens[-1]), position=n - 1, start=0, rows=1, rope_start=0
            )
        else:
            start = self.resume(held)
            self._seen = tokens[:start]
            for inputs, values in self._chunks(tokens, start):
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
        n, L = tokens.size, self.config.max_seq_len
        if not (0 < n and 0 < num_tokens and n + num_tokens - 1 <= L):
            raise ValueError(
                f"{n} tokens and {num_tokens} more to draw do not fit {L} rows"
            )
        loop = self.device_loop
        assert self._prompt is not None and self._decode is not None
        began = time.perf_counter()
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        draws = np.zeros((L, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + num_tokens] = sample.rows(num_tokens, self._k_max())
        self._decode.write(self.draws, draws)
        start = self.resume(self._held(tokens))
        self._seen = tokens[:start]
        for inputs, values in self._chunks(tokens, start):
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
                _, carry = self(start=0, rows=1, rope_start=0, **carry)
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
        return [int(t) for t in drawn], first - began, later

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

    def resume(self, held: int) -> int:
        """The position calls start from to run the tokens from ``held`` on:
        ``held`` itself, or for a state that cannot restart there
        (``Checkpoints.restart``), the earliest one of them can.
        """
        ran = self._seen.size
        states = [c for layer in self.recurrent.values() for c in layer.values()]
        return min([held, *(c.restart(held, ran) for c in states)])

    def prompt_ids(self, tokens) -> np.ndarray:
        """A prompt call's ``ids`` for a chunk of ``tokens``, padded to
        ``prefill_chunk`` with row 0, which the bound by ``rows`` leaves
        unread.
        """
        tokens = np.asarray(tokens)
        ids = np.zeros(self.config.prefill_chunk, dtype=np.int32)
        ids[: tokens.size] = tokens
        return ids

    def table_start(self, n: int) -> int:
        """The row of the RoPE angles a sequence of ``n`` tokens reads from:
        past ``long_past``, the second table's, ``max_seq_len`` rows on.
        """
        past = self.long_past
        return self.config.max_seq_len if past is not None and n > past else 0

    def _chunks(self, tokens: np.ndarray, start: int) -> Iterator[tuple]:
        """Each prompt call from ``start``: its inputs, ``ids`` and for a call
        holding a placeholder ``before``, and its per-call values. With
        recurrent state a call ends at the next chunk boundary, the slot it
        writes.
        """
        n, C = tokens.size, self.config.prefill_chunk
        table = self.table_start(n)
        end = start
        while end < n:
            begin, end = end, min(end + C, n)
            if self.recurrent:
                end = min(end, (begin // C + 1) * C)
            ids = self.prompt_ids(tokens[begin:end])
            values = dict(
                self.call_values(),
                token=int(tokens[end - 1]),
                position=end - 1,
                start=begin,
                rows=end - begin,
                rope_start=table + begin,
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
