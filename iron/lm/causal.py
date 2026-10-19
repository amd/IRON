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
from typing import Any, ClassVar

import numpy as np
from aie.iron.kernels.sample import ROW_WORDS
from ml_dtypes import bfloat16

import iron
from iron import Carried, Scratchpad
from iron.common.graph import CarriedLoop, CompiledGraph, Handle
from iron.common.graph.compiled import walk
from iron.common.graph.handle import State
from iron.operators.copy import Copy
from iron.operators.sample import Sample

from .blocks import DecoderLayer, Embedding, Linear, RMSNorm, Rope
from .checkpoint import renamed
from .config import DecoderConfig
from .model import Model
from .generation import Sampler
from .session import Session

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
    """A decoder on ``config``'s shape: ``model``, a ``decoder_class`` of
    ``layer_class`` layers, each holding its own ``KVCache``; ``lm_head``,
    the embedding where tied, loaded from ``weights``; and ``rotary_emb``,
    the RoPE table (``Rope``), None with no ``rope_theta``.

    Args:
        config: The decoder's shape.
        weights: The checkpoint's tree (``Checkpoint.tree``).
    """

    decoder_class: ClassVar[type[Decoder]] = Decoder
    layer_class: ClassVar[type[iron.Graph]] = DecoderLayer
    layers: list

    def __init__(self, config: DecoderConfig, weights):
        self.config = config
        self.weights = weights
        self.rotary_emb = None if config.rope_theta is None else Rope(config)
        # Zero until the host writes draws: a row of zeros is greedy.
        self.draws = iron.state((config.max_seq_len, ROW_WORDS), np.int32)
        self.drawn = iron.state((config.max_seq_len,), np.int32)
        self._prompt: CompiledGraph | None = None
        self._decode: CompiledGraph | None = None
        self._placed: CompiledGraph | None = None
        self._placeholders: tuple[int, ...] = ()
        # By the version a device loop starts from, its loop (``loop``).
        self._loops: dict[int, CarriedLoop] = {}
        # The session whose tokens the caches hold, and the one ``logits``
        # and ``generate`` run in.
        self._holder: Session | None = None
        self.session = Session(self)
        self.model = self.decoder_class(config, self.layer_class)
        for layer in self.model.layers:
            layer.rope = self.rotary_emb
        self.lm_head = Linear(config.hidden_size, config.vocab_size, bias=False)
        if config.tie_word_embeddings:
            self.lm_head.weight = self.model.embed_tokens.weight
        self.load_state_dict(renamed(weights, self.renames))
        self.layers = self.model.layers

    @property
    def recurrent(self) -> list[Checkpoints]:
        """Each state a layer carries from position to position."""
        return [p for _, _, p, _ in walk(self) if isinstance(p, Checkpoints)]

    def layer(self, call: Call, i: int, w, x):
        """Layer ``i``, the module ``w``, on ``x``."""
        return w(x, call)

    def head(self, x):
        """The final norm, then the output head (the embedding, if tied)."""
        return self.lm_head(self.model.norm(x))

    def positions(self, x, call: Call):
        """``x``, the rows ``call`` runs, with the model's absolute positions
        placed; unchanged by default.
        """
        return x

    def lookup(self, ids):
        """The embedding rows of ``ids``, bounded as ``ids`` is, or of the
        decode step's token.
        """
        return self.model.embed_tokens(ids)

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
        for rope in (layer.rope for layer in self.layers):
            if rope is not None and rope not in call.ropes:
                call.ropes[rope] = rope.rows(call)
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
        self._loops, self._holder = {}, None
        if not decode.plan.full_elf:
            logger.info("%s", decode.plan.report("decode"))

    def call_values(self) -> dict:
        """The per-call values every call gives beyond the token, position,
        start, rows and rope_start: none by default.
        """
        return {}

    def __call__(self, ids=None, before=None, **values) -> Any:
        """One call of the prompt version on ``ids``
        (``Session.prompt_ids``), of the placed one on ``ids`` and
        ``before`` (``use``), else of the decode step, with ``call_values``
        where ``values`` give none of their own.

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

    def loop(self, version: CompiledGraph) -> CarriedLoop:
        """The device loop of decode steps ``version`` starts, made once: its
        runs are bound to the versions, which every session shares.
        """
        if id(version) not in self._loops:
            self._loops[id(version)] = CarriedLoop(version, self._decode, depth=2)
        return self._loops[id(version)]

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, the whole history, in
        ``session`` (``Session.logits``).
        """
        return self.session.logits(tokens)

    def _draw(
        self, tokens, max_tokens: int, sampler: Sampler, each: bool = True
    ) -> Iterator[int]:
        """``Model.stream``'s draws, in ``session`` (``Session.draw``)."""
        return self.session.draw(tokens, max_tokens, sampler, each)

    def forget(self, position: int) -> None:
        """Hold nothing the caches have from ``position`` on, whichever
        session's tokens they hold (``Session.forget``).
        """
        if self._holder is not None:
            self._holder.forget(position)
