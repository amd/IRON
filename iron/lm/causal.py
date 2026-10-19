# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder-only language model on the NPU, as one graph.

A call with no tensor is a decode step; ``prefill_chunk`` token ``ids`` are
a prompt chunk from position ``start``, of which a call runs the first
``rows``, their embedding rows gathered on the device. Both draw the next
token on the device and carry it and ``position + 1`` into the next call.
Where the decode step is not a full ELF (NPU1, or ``full_elf=False``) there
is no device loop: the host starts each step on the token the last one drew.
"""

import dataclasses
import logging
from collections.abc import Iterator
from functools import partial
from typing import Any, ClassVar

import numpy as np
from aie.iron.kernels.sample import ROW_WORDS
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Carried, Scratchpad
from iron.common.graph import CarriedLoop, CompiledGraph, Handle
from iron.common.graph.compiled import _leaves
from iron.common.graph.handle import State
from iron.operators.copy import Copy
from iron.operators.sample import Sample

from .blocks import DecoderLayer, Embedding, KVCache, Linear, RMSNorm, Rope
from .checkpoint import renamed
from .config import DecoderConfig
from .model import Model
from .generation import Sampler

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Call:
    """One call's values, built once in ``body`` and read by every module
    that keeps memory from call to call (``KVCache``, ``Checkpoints``,
    ``Rope``): a prompt chunk's ``rows`` from ``start``, or the decode
    step's one at ``position``. Each is a per-call value in a trace and its
    number in the reference.
    """

    prompt: bool
    # The first position the call runs; a decode step's is its ``position``.
    start: Any
    rows: Any
    # The last position the call runs.
    position: Any
    # The row a prompt chunk's first position reads of a stacked RoPE table.
    rope_start: Any = None
    # The encoder's rows a cross attention reads (``EncoderDecoder``).
    source: Any = None
    # The k rows of the model's rotary_emb, which a layer on config.layer(i)
    # reads; None: no RoPE.
    angles: Handle | None = None
    # By each Rope a layer holds, its rows of the call (Rope.rows).
    ropes: dict = dataclasses.field(default_factory=dict)


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

    def at(self, call: Call) -> tuple[Handle, Handle]:
        """The slot ``call`` reads, the state before its first position, and
        the slot it writes, the state after its last, in a graph's body. A
        call ends within the chunk it starts in (``CausalLM`` splits them).
        """
        C = self.chunk
        return self.slots[(call.start - 1) // C + 1], self.slots[call.position // C + 1]

    def restart(self, held: int, ran: int) -> int:
        """Where a call may start to change the positions from ``held`` on,
        after ``ran`` positions ran: there where the last call ended, else at
        the boundary before it.
        """
        return held if held == ran else held // self.chunk * self.chunk

    def slot(self, position: int) -> int:
        """The slot holding the state after the first ``position`` positions."""
        return 0 if position == 0 else (position - 1) // self.chunk + 1


class Decoder(iron.Graph):
    """A decoder's modules on ``c``'s shape, as a checkpoint's ``model``
    names them: ``embed_tokens``, ``layers``, layer ``i`` a ``layer(c, i)``,
    and the final ``norm``.
    """

    def __init__(self, c: DecoderConfig, layer: type[iron.Graph]):
        self.embed_tokens = Embedding(c.vocab_size, c.hidden_size)
        self.layers = [layer(c, i) for i in range(c.num_hidden_layers)]
        self.norm = RMSNorm(c.hidden_size, c.eps)


class CausalLM(Model):
    """A decoder on ``config``'s shape: ``model``, a ``Decoder`` of
    ``layer_class`` layers, each holding its own ``KVCache``; ``lm_head``,
    the embedding where tied, loaded from ``weights``; and ``rotary_emb``,
    the RoPE table (``Rope``), None with no ``rope_theta``.

    Args:
        config: The decoder's shape.
        weights: The checkpoint's tree (``Checkpoint.tree``).
        decoder: With no ``layer_class``, the decoder's module of
            ``weights``, whose ``embed_tokens``, ``layers`` and ``norm`` are
            read here; None is ``weights.model``.

    With no ``layer_class``, a model's layers are ``config.layer(i)`` on the
    checkpoint's own modules, ``caches`` holding each attention layer's
    ``KVCache``, and ``final_norm``, the norm module ``head`` reads, is
    ``decoder.norm``; a subclass sets it where the checkpoint names it
    otherwise.
    """

    layer_class: ClassVar[type[iron.Graph] | None] = DecoderLayer
    layers: list

    def __init__(self, config: DecoderConfig, weights, decoder=None):
        self.config = config
        self.weights = weights
        self.rotary_emb = None if config.rope_theta is None else Rope(config)
        # Zero until the host writes draws: a row of zeros is greedy.
        self.draws = iron.state((config.max_seq_len, ROW_WORDS), np.int32)
        self.drawn = iron.state((config.max_seq_len,), np.int32)
        self._seen = np.empty(0, dtype=np.int64)  # the tokens in the caches
        self._prompt: CompiledGraph | None = None
        self._decode: CompiledGraph | None = None
        self._placed: CompiledGraph | None = None
        self._placeholders: tuple[int, ...] = ()
        # By the version a device loop starts from, its loop.
        self._loops: dict[int, CarriedLoop] = {}
        if self.layer_class is not None:
            self.model = Decoder(config, self.layer_class)
            for layer in self.model.layers:
                layer.rope = self.rotary_emb
            self.lm_head = Linear(config.hidden_size, config.vocab_size, bias=False)
            if config.tie_word_embeddings:
                self.lm_head.weight = self.model.embed_tokens.weight
            self.load_state_dict(renamed(weights, self.renames))
            self.layers = self.model.layers
            return
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
        self.caches = {
            i: KVCache(config, config.layer(i).attention.window)
            for i, w in enumerate(self.layers)
            if "self_attn" in vars(w)
        }

    @property
    def recurrent(self) -> list[Checkpoints]:
        """Each state a layer carries from position to position."""
        return [p for _, _, p, _ in _leaves(self) if isinstance(p, Checkpoints)]

    def layer(self, call: Call, i: int, w, x):
        """Layer ``i`` on ``x``: the module ``w`` itself, or with no
        ``layer_class`` ``config.layer(i)`` on its weights ``w``, attending
        over ``caches``.
        """
        if self.layer_class is not None:
            return w(x, call)
        attend = partial(self.attend, call, i)
        return self.config.layer(i)(w, x, attend, call.angles)

    def head(self, x):
        """The final norm, then the output head (the embedding, if tied)."""
        if self.layer_class is not None:
            return self.lm_head(self.model.norm(x))
        c = self.config
        x = c.norm()(self.final_norm, x)
        if c.tie_word_embeddings:
            return F.linear(x, self.decoder.embed_tokens.weight)
        return F.linear(x, self.weights.lm_head.weight)

    def positions(self, x, call: Call):
        """``x``, the rows ``call`` runs, with the model's absolute positions
        placed; unchanged by default.
        """
        return x

    def lookup(self, ids):
        """The embedding rows of ``ids``, bounded as ``ids`` is, or of the
        decode step's token.
        """
        if self.layer_class is not None:
            return self.model.embed_tokens(ids)
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
            x = self.lookup(ids[:rows])
            return self.forward(x, Call(True, start, rows, position, rope_start))
        x = self.lookup(token).reshape(1, self.config.hidden_size)
        return self.forward(x, Call(False, position, rows, position, rope_start))

    def from_rows(self, x, *, token, position, start, rows, rope_start):
        """A prompt chunk's call on its embedding rows ``x``, bounded to
        ``rows``, in place of its ids' lookup; ``token`` is the decode
        step's, unread here.
        """
        return self.forward(x, Call(True, start, rows, position, rope_start))

    def forward(self, x, call: Call):
        """The layers, the head and the draw over ``x``, the rows ``call``
        runs, each memory module reading ``call``.
        """
        c = self.config
        held = [self.rotary_emb]
        if self.layer_class is not None:
            held = [layer.rope for layer in self.layers]
        for rope in held:
            if rope is not None and rope not in call.ropes:
                call.ropes[rope] = rope.rows(call)
        if self.rotary_emb in call.ropes:
            call.angles = call.ropes[self.rotary_emb][1]
        x = self.positions(x, call)
        for i, weights in enumerate(self.layers):
            x = self.layer(call, i, weights, x)
        if call.prompt:
            x = Copy.step(x[call.rows - 1]).reshape(
                1, c.hidden_size
            )  # the last row's logits alone
        logits = self.head(x)
        _, drawn = Sample.step(
            logits.reshape(c.vocab_size),
            self.draws,
            self.drawn,
            row=call.position * ROW_WORDS,
            at=call.position,
        )
        return logits, iron.carry(token=drawn, position=call.position + 1)

    def attend(
        self,
        call: Call,
        i: int,
        q,
        k,
        v,
        *,
        scale: float | None = None,
        window: int | None = None,
    ):
        """Layer ``i``'s ``KVCache.attend``, built with its layer's
        ``window``.
        """
        return self.caches[i].attend(call, q, k, v, scale)

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

    def _draw(
        self, tokens, max_tokens: int, sampler: Sampler, each: bool = True
    ) -> Iterator[int]:
        """Draw ``max_tokens`` after ``tokens`` on the device, each yielded
        as it is drawn (``Model.stream``).

        Where the decode step is a full ELF each step starts the next
        (``device_loop``): with ``each``, each token is read once its step
        completes, else the first alone and the rest once the last has;
        elsewhere the host starts each step on the token the last one drew,
        which it reads alone. The draws match ``generate_on_host`` with the
        same seed.

        Raises:
            ValueError: The tokens and those to draw do not fit the caches.
            IndexError: A token is outside ``[0, vocab_size)``.
            RuntimeError: Neither version is loaded: ``load_versions()``
                first.
        """
        tokens = self._tokens(tokens)
        n, L = tokens.size, self.config.max_seq_len
        if not (0 < n and 0 < max_tokens and n + max_tokens - 1 <= L):
            raise ValueError(
                f"{n} tokens and {max_tokens} more to draw do not fit {L} rows"
            )
        if self._prompt is None or self._decode is None:
            raise RuntimeError(f"{type(self).__name__}: load_versions() first")
        loop = self.device_loop
        # The prompt draws at its last position, n - 1; decode step k at n + k.
        draws = np.zeros((L, ROW_WORDS), dtype=np.int32)
        draws[n - 1 : n - 1 + max_tokens] = sampler.rows(max_tokens, self._k_max())
        self._decode.write(self.draws, draws)
        start = self.resume(self._held(tokens))
        # A caller may stop early, leaving steps in the caches nothing records:
        # until the last token, they hold nothing.
        self._seen = np.empty(0, dtype=np.int64)
        for inputs, values in self._chunks(tokens, start):
            if not loop or values["position"] < n - 1:
                _, carry = self(*inputs, **values)
            else:
                version = self._prompt if len(inputs) == 1 else self._placed
                started = self._loops.setdefault(
                    id(version), CarriedLoop(version, self._decode, depth=2)
                )
                started.start(*inputs, **values)
        drawn = []
        if loop:
            read = partial(self._decode.read, self.drawn)
            drawn.append(int(read()[n - 1]))
            yield drawn[-1]
            for k, _ in enumerate(started.steps(max_tokens - 1), start=1):
                if each:
                    drawn.append(int(read()[n - 1 + k]))
                    yield drawn[-1]
            if not each:
                drawn += [int(t) for t in read()[n : n - 1 + max_tokens]]
                yield from drawn[1:]
        else:
            drawn.append(int(carry["token"]))
            yield drawn[-1]
            for _ in range(max_tokens - 1):
                _, carry = self(start=0, rows=1, rope_start=0, **carry)
                drawn.append(int(carry["token"]))
                yield drawn[-1]
        # The caches hold every token but the last drawn, which no step read.
        self._seen = np.concatenate([tokens, drawn[:-1]]).astype(np.int64)

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
        return min([held, *(c.restart(held, ran) for c in self.recurrent)])

    def prompt_ids(self, tokens) -> np.ndarray:
        """A prompt call's ``ids`` for a chunk of ``tokens``, padded to
        ``prefill_chunk`` with row 0, which the bound by ``rows`` leaves
        unread.
        """
        tokens = np.asarray(tokens)
        ids = np.zeros(self.config.prefill_chunk, dtype=np.int32)
        ids[: tokens.size] = tokens
        return ids

    def _chunks(self, tokens: np.ndarray, start: int) -> Iterator[tuple]:
        """Each prompt call from ``start``: its inputs, ``ids`` and for a call
        holding a placeholder ``before``, and its per-call values. With
        recurrent state a call ends at the next chunk boundary, the slot it
        writes.
        """
        n, C, rope = tokens.size, self.config.prefill_chunk, self.rotary_emb
        table = 0 if rope is None else rope.table_start(n)
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
