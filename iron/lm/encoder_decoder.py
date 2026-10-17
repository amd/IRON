# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder whose layers also attend over an encoder's output, as one graph.

``EncoderDecoder`` is a ``CausalLM`` holding its encoder. Its encode version
runs the encoder and projects the output into each layer's cross keys and
values, states the decode step and the prompt chunks read, bounded to the
call's ``source`` rows.
"""

import inspect
from functools import partial

import aie.utils as aie_utils
import numpy as np

import iron
from iron import Carried
from iron.operators.copy import Copy
from iron.operators.mha import MHA

from .base import DecoderConfig, Oracle, widen
from .causal import CausalLM, DecodeStep
from .encoder import Encoder, Tower


class EncoderDecoder(CausalLM):
    """A decoder on ``config``'s shape over the output of ``encoder``; a
    subclass gives ``head`` and ``oracle`` as a ``CausalLM``'s does.

    Its versions are the decoder's own and the encode version, which takes
    the encoder's input and per-call values, each named with ``encoder_``
    before it. Every version carries ``source``, the rows of the encoder's
    output the cross attention reads, which ``encode`` sets.

    Args:
        config: The decoder's shape.
        weights: The checkpoint's tree.
        encoder: The encoder, its weights its own.
        decoder: The decoder's module of ``weights`` (``CausalLM``).

    Raises:
        TypeError: The encoder takes other than one input.
    """

    oracle: "type[EncoderDecoderOracle]"

    def __init__(self, config: DecoderConfig, weights, encoder: Encoder, decoder=None):
        super().__init__(config, weights, decoder)
        self.encoder = encoder
        rows = encoder.soft_rows if isinstance(encoder, Tower) else encoder.max_tokens
        shapes = [
            (rows, config.layer(i).groups, config.layer(i).head_dim)
            for i in range(config.n_layers)
        ]
        self.cross_keys = [iron.state(shape) for shape in shapes]
        self.cross_values = [iron.state(shape) for shape in shapes]
        P = inspect.Parameter
        parameters = list(encoder.signature().parameters.values())
        inputs = [p.name for p in parameters if p.kind is not P.KEYWORD_ONLY]
        if len(inputs) != 1:
            raise TypeError(f"EncoderDecoder: an encoder takes one input, not {inputs}")
        (self.encoder_input,) = inputs
        self.encoder_values = [p.name for p in parameters if p.kind is P.KEYWORD_ONLY]
        self._encode = None
        self._source: int | None = None

    def signature(self) -> inspect.Signature:
        P = inspect.Parameter
        own = list(inspect.signature(CausalLM.body, eval_str=True).parameters.values())
        inputs = [p for p in own[1:] if p.kind is not P.KEYWORD_ONLY]
        values = [p for p in own[1:] if p.kind is P.KEYWORD_ONLY]
        values.append(P("source", P.KEYWORD_ONLY, annotation=Carried[np.int32]))
        for p in self.encoder.signature().parameters.values():
            named = p.replace(name=f"encoder_{p.name}")
            if p.kind is P.KEYWORD_ONLY:
                values.append(named)
            else:
                inputs.append(named.replace(default=None))
        return inspect.Signature(inputs + values)

    def body(self, *inputs, **values):
        given = dict(zip(self._inputs, inputs))
        encoded = given[f"encoder_{self.encoder_input}"]
        if encoded is not None:
            own = {v: values[f"encoder_{v}"] for v in self.encoder_values}
            memory = self.encoder.inline(self.encoder.body, encoded, **own)
            for i, w in enumerate(self.layers):
                k, v = self.config.layer(i).cross_kv(w, memory)
                Copy.step(k, self.cross_keys[i][: k.shape[0]])
                Copy.step(v, self.cross_values[i][: v.shape[0]])
            return iron.carry(**{n: values[n] for n in self._carried})
        ids, rows, source = given["ids"], values["rows"], values["source"]
        prompt = ids is not None
        if prompt:
            x = self.lookup(ids[:rows])
        else:
            x = self.lookup(values["token"]).reshape(1, self.config.emb_dim)
        logits, carry = self.forward(
            x,
            prompt=prompt,
            position=values["position"],
            start=values["start"],
            rope_start=values["rope_start"],
            rows=rows,
            source=source,
        )
        return logits, iron.carry(**carry, source=source)

    def layer(self, step: DecodeStep, i: int, weights, x):
        """Layer ``i`` on ``x``: ``config.layer(i)``, attending over the
        caches and over the encoder's output.
        """
        attend = partial(self.attend, step, i)
        cross = partial(self.cross, step, i)
        return self.config.layer(i).step(weights, x, attend, step.angles, cross=cross)

    def cross(self, step: DecodeStep, i: int, q, *, scale: float | None = None):
        """``q`` ``(rows, heads, head_dim)`` over the first ``step.source``
        rows of layer ``i``'s cross keys and values, the logits scaled by
        ``scale`` (MHA's ``1 / sqrt(head_dim)`` if None).
        """
        n, H, D = q.shape
        span = np.s_[: step.source]
        o = MHA.step(
            q,
            self.cross_keys[i][span],
            self.cross_values[i][span],
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            scale=scale,
        )
        return o.reshape(n, H * D)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: the decoder's, then the
        encoder's, named with ``encoder_`` before each.
        """
        encoded = [
            {f"encoder_{n}": shape for n, shape in s.items()}
            for s in self.encoder.shapes()
        ]
        return [*super().shapes(), *encoded]

    def load(
        self,
        *,
        release=None,
        tuner=None,
        full_elf: bool | None = None,
        dev=None,
    ) -> "EncoderDecoder":
        """Compile and load every version before the first call, in one
        arena, the prompt chunk feeding off the decode step, and run the
        decoder's on them (``use``).

        Args:
            release: Given each piece of each weight once it is on the device.
            tuner: Folds, narrows and packs each version's designs by cost.
            full_elf: Each version's packaging (``Graph.compile``).
            dev: The device every version compiles for, else the current one.
        """
        if dev is None:
            dev = aie_utils.ensure_current_device()
        compiled, decode = [], None
        for shapes in self.shapes():
            version = self.compile(
                dev=dev,
                feeds=decode if "ids" in shapes else None,
                tuner=tuner,
                full_elf=full_elf,
                **shapes,
            )
            version.load(release=release)
            if not shapes and version.emit is not None:
                decode = version
            compiled.append(version)
        decode_step, prompt_chunk, *encoded = compiled
        self.use(decode_step, prompt_chunk)
        (self._encode,) = encoded
        return self

    def encode(self, *raw) -> None:
        """Run the encoder on ``raw``, as its ``inputs`` takes it, and hold
        its keys and values for the calls after; the caches' tokens are
        forgotten, since each attended over the encoder's last output.

        Raises:
            RuntimeError: The versions are not loaded: ``load()`` first.
        """
        if self._encode is None:
            raise RuntimeError(f"{type(self).__name__}: load() first")
        buffer, values = self.encoder.inputs(*raw)
        self._source = (
            self.encoder.soft(values)
            if isinstance(self.encoder, Tower)
            else values[self.encoder.bound]
        )
        name = f"encoder_{self.encoder_input}"
        inputs = [buffer if n == name else None for n in self._inputs]
        named = {f"encoder_{v}": x for v, x in values.items()}
        self._encode(*inputs, token=0, position=0, source=self._source, **named)
        self.forget(0)

    def call_values(self) -> dict:
        """The ``source`` the last ``encode`` set.

        Raises:
            RuntimeError: Nothing is encoded yet: ``encode()`` first.
        """
        if self._source is None:
            raise RuntimeError(f"{type(self).__name__}: encode() first")
        return dict(source=self._source)


class EncoderDecoderOracle(Oracle):
    """An ``EncoderDecoder``'s float32 forward pass on the host: ``encode``
    projects an encoder's output into each layer's keys and values once,
    which every ``logits`` after attends over.
    """

    def encode(self, memory) -> None:
        """Hold each layer's keys and values of the encoder's output
        ``memory`` ``(rows, width)``.
        """
        memory = np.asarray(memory, np.float32)
        self.memory = [
            self.config.layer(i).cross_kv_oracle(self, widen(w), memory)
            for i, w in enumerate(self.layers)
        ]

    def layer(self, i: int, angles, w, x):
        """Layer ``i`` on ``x``, ``config.layer(i)``'s twin, attending
        causally and over the encoder's output.
        """
        keys, values = self.memory[i]
        return self.config.layer(i).oracle(
            self,
            w,
            x,
            partial(self.attend, causal=True),
            angles,
            cross=partial(self.attend, k=keys, v=values),
        )
