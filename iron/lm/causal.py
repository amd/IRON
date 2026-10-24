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

from .blocks import DecoderLayer, Embedding, KVCache, Linear, RMSNorm, Rope
from .checkpoint import Checkpoint, renamed, weights_file
from .config import DecoderConfig
from .model import Model
from .generation import Sampler
from .session import Session

logger = logging.getLogger(__name__)


@dataclasses.dataclass(kw_only=True)
class Call:
    """One call's values, built once in ``body`` and read by every module
    that keeps memory from call to call (``KVCache``, ``Checkpoints``,
    ``Rope``): a prompt chunk's ``rows`` from ``start``, or the decode
    step's one at ``position``. Each is a per-call value in a recording and its
    number in the reference.
    """

    prompt: bool
    # The first position the call runs; a decode step's is its ``position``.
    start: Any
    rows: Any
    # The last position the call runs; None for an encoder's, which no cache
    # reads (``Encoder.forward``).
    position: Any
    # The row a prompt chunk's first position reads of a stacked RoPE table.
    rope_start: Any = None
    # By each Rope a layer holds, its rows of the call (Rope.rows).
    ropes: dict = dataclasses.field(default_factory=dict)
    # The token ids the call embeds, a prompt chunk's rows or the decode
    # step's token, placeholders included where a tower's rows replace
    # their embeddings (``from_rows``); None for a tower's call.
    ids: Any = None
    # The token value the call was given: the decode step's, or a prompt
    # chunk's last; None where no token is given (an encoder's call).
    token: Any = None
    # The embedding rows the layers start from (``forward``).
    embeddings: Any = None


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

    def __init__(self, c: DecoderConfig, layer: type[DecoderLayer]):
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
    layer_class: ClassVar[type[DecoderLayer]] = DecoderLayer
    layers: list

    def __init__(self, config: DecoderConfig, weights):
        self.config = config
        self.weights = weights
        self.rotary_emb = None if config.rope_theta is None else self.rotary(config)
        # Zero until the host writes draws: a row of zeros is greedy.
        self.draws = iron.state((config.max_seq_len, ROW_WORDS), np.int32)
        self.drawn = iron.state((config.max_seq_len,), np.int32)
        # The versions ``use`` runs, which every session calls.
        self.prompt_chunk: CompiledGraph | None = None
        self.decode_step: CompiledGraph | None = None
        self.placed_chunk: CompiledGraph | None = None
        self.placeholders: tuple[int, ...] = ()
        # By the version a device loop starts from, its loop (``loop``).
        self._loops: dict[int, CarriedLoop] = {}
        # The session whose tokens the caches hold, and the one ``logits``
        # and ``generate`` run in.
        self.holder: Session | None = None
        self.session = Session(self)
        self.model = self.decoder_class(config, self.layer_class)
        for layer in self.model.layers:
            layer.rope = self.rotary_emb
        self.lm_head = Linear(
            config.hidden_size, config.vocab_size, False, precision=config.precision
        )
        if config.tie_word_embeddings:
            self.lm_head.weight = self.model.embed_tokens.weight
        self.load_state_dict(renamed(weights, self.renames))
        if config.vocab_size % 2:
            # An odd vocabulary's logits end mid-word; a zero row makes them
            # whole words, and Sample draws none from it.
            head = np.asarray(self.lm_head.weight)
            self.lm_head.weight = iron.param(np.pad(head, ((0, 1), (0, 0))))
        self.layers = self.model.layers

    @property
    def recurrent(self) -> list[Checkpoints | KVCache]:
        """Each state a layer carries from position to position, which
        restarts only at some (``restart``): ``Checkpoints``, and a
        ``KVCache`` keeping a ring.
        """
        found = {}
        for _, _, p, _ in walk(self):
            if (
                isinstance(p, Checkpoints)
                or isinstance(p, KVCache)
                and p.ring is not None
            ):
                found.setdefault(id(p), p)
        return list(found.values())

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
        ids: Handle | None = None,
        *,
        token: Carried[np.int32],
        position: Carried[np.int32],
        start: Scratchpad[np.int32] = np.int32(0),
        rows: Scratchpad[np.int32] = np.int32(1),
        rope_start: Scratchpad[np.int32] = np.int32(0),
    ):
        prompt = ids is not None
        call = Call(
            prompt=prompt,
            start=start if prompt else position,
            rows=rows,
            position=position,
            rope_start=rope_start,
            ids=ids[:rows] if prompt else token,
            token=token,
        )
        if prompt:
            return self.forward(self.lookup(call.ids), call)
        return self.forward(
            self.lookup(token).reshape(1, self.config.hidden_size), call
        )

    def from_rows(self, x, ids, *, token, position, start, rows, rope_start):
        """A prompt chunk's call on its embedding rows ``x``, bounded to
        ``rows``, in place of the lookup of its ``ids``; ``token`` is the
        decode step's, unread here.
        """
        return self.forward(
            x,
            Call(
                prompt=True,
                start=start,
                rows=rows,
                position=position,
                rope_start=rope_start,
                ids=ids,
            ),
        )

    def forward(self, x: Handle, call: Call):
        """The layers, the head and the draw over ``x``, the rows ``call``
        runs, each memory module reading ``call``.
        """
        c = self.config
        call.embeddings = x
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
        return self.draw(self.head(x), call)

    def draw(self, logits, call: Call):
        """What a call returns: ``logits``, ``head``'s output, and the
        token drawn from them on the device, carried with the next position.
        """
        c = self.config
        _, drawn = Sample.step(
            logits.reshape(c.vocab_size + c.vocab_size % 2),
            self.draws,
            self.drawn,
            row=call.position * ROW_WORDS,
            at=call.position,
            drawable=c.vocab_size,
        )
        return logits, iron.carry(token=drawn, position=call.position + 1)

    def rotary(self, config: DecoderConfig) -> Rope:
        """``rotary_emb``, the RoPE table every layer holds: ``Rope``'s."""
        return Rope(config)

    def rope_row(self, n: int, begin: int) -> int:
        """The RoPE table row a chunk from ``begin`` of an ``n``-token prompt
        reads first (``Rope.table_start``).
        """
        rope = self.rotary_emb
        return begin + (0 if rope is None else rope.table_start(n))

    @classmethod
    def tune_arguments(cls, parser) -> None:
        """The flags ``tune_calls`` follows from (``tune.arguments``)."""
        from .tune import arguments

        arguments(parser)

    @classmethod
    def tune_calls(cls, parser, args) -> list:
        """``tune.calls`` on ``args``, built on weights it never reads."""
        from .tune import calls

        weights = weights_file(args.checkpoint)
        config = cls.default_config(weights)
        assert isinstance(config, DecoderConfig), "a decoder's"
        model = cls(config, Checkpoint(weights).tree("unread"))
        L, C = config.max_seq_len, config.prefill_chunk
        if not C <= args.context <= L or args.context % C:
            parser.error(
                f"--context {args.context} is not whole {C}-token chunks within "
                f"max_seq_len {L}"
            )
        sampler = Sampler(args.temperature, args.top_k)
        return calls(
            model, args.position, args.token, args.context, args.points, sampler
        )

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
        own, or those of a graph recording it in their bodies (a multimodal
        model's), in one arena, each prompt version feeding ``decode``.

        Args:
            decode: The decode step.
            prompt: A prompt chunk, on ``ids``.
            placed: A prompt chunk holding any of ``placeholders``, on its
                ``ids`` and ``before``, the count of each placeholder before
                the chunk.
            placeholders: The placeholder tokens, in ``before``'s order.
        """
        self.decode_step, self.prompt_chunk = decode, prompt
        self.placed_chunk, self.placeholders = placed, tuple(placeholders)
        self._loops, self.holder = {}, None
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
        if self.decode_step is None:
            raise RuntimeError(f"{type(self).__name__}: load_versions() first")
        values = {**self.call_values(), **values}
        if ids is None:
            return self.decode_step(**values)
        if before is not None:
            assert self.placed_chunk is not None
            return self.placed_chunk(ids, before, **values)
        assert self.prompt_chunk is not None
        return self.prompt_chunk(ids, **values)

    @property
    def device_loop(self) -> bool:
        """Whether ``generate`` can draw on the device: a full-ELF decode step."""
        if self.decode_step is None:
            raise RuntimeError(f"{type(self).__name__}: load_versions() first")
        return self.decode_step.emit is not None

    def loop(self, version: CompiledGraph) -> CarriedLoop:
        """The device loop of decode steps ``version`` starts, made once: its
        runs are bound to the versions, which every session shares.
        """
        if id(version) not in self._loops:
            assert self.decode_step is not None, "loaded with the version it starts"
            self._loops[id(version)] = CarriedLoop(version, self.decode_step, depth=2)
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
        if self.holder is not None:
            self.holder.forget(position)
