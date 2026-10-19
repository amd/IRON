# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A decoder whose layers also attend over an encoder's output, as one graph.

``EncoderDecoder`` is a ``CausalLM`` holding its encoder. Its encode version
runs the encoder and projects the output into each layer's ``CrossCache``,
which the decode step and the prompt chunks read, bounded to the call's
``source`` rows.
"""

import inspect

import numpy as np

import iron
from iron import Carried

from .blocks import CrossCache, CrossDecoderLayer
from .config import DecoderConfig
from .causal import Call, CausalLM
from .encoder import Encoder


class EncoderDecoder(CausalLM):
    """A decoder on ``config``'s shape over the output of ``encoder``, of
    ``CrossDecoderLayer`` layers, each given a ``CrossCache`` of the
    encoder's rows.

    Its versions are the decoder's own and the encode version, which takes
    the encoder's input and per-call values, each named with ``encoder_``
    before it. Every version carries ``source``, the rows of the encoder's
    output the cross attention reads, which ``encode`` sets.

    Args:
        config: The decoder's shape.
        weights: The decoder's checkpoint tree (``CausalLM``).
        encoder: The encoder, its weights its own.

    Raises:
        TypeError: The encoder takes other than one input.
        ValueError: The encoder's rows are fewer than a prompt chunk's.
    """

    layer_class = CrossDecoderLayer

    def __init__(self, config: DecoderConfig, weights, encoder: Encoder):
        super().__init__(config, weights)
        self.encoder = encoder
        rows = encoder.soft_rows
        if rows < config.prefill_chunk:
            # A prompt chunk's queries are the last rows of what MHA attends.
            raise ValueError(
                f"EncoderDecoder: the encoder's {rows} rows are fewer than a "
                f"{config.prefill_chunk}-row prompt chunk's queries"
            )
        for layer in self.layers:
            layer.cross = CrossCache(config, rows)
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
        given = dict(zip(self._parameters.inputs, inputs))
        encoded = given[f"encoder_{self.encoder_input}"]
        if encoded is not None:
            own = {v: values[f"encoder_{v}"] for v in self.encoder_values}
            memory = self.encoder.inline(self.encoder.body, encoded, **own)
            for layer in self.layers:
                layer.cross.write(*layer.encoder_attn.keys_values(memory))
            return iron.carry(**{n: values[n] for n in self._parameters.carried})
        ids, rows, source = given["ids"], values["rows"], values["source"]
        position, rope_start = values["position"], values["rope_start"]
        if ids is not None:
            x = self.lookup(ids[:rows])
            call = Call(True, values["start"], rows, position, rope_start, source)
        else:
            x = self.lookup(values["token"]).reshape(1, self.config.hidden_size)
            call = Call(False, position, rows, position, rope_start, source)
        logits, carry = self.forward(x, call)
        return logits, iron.carry(**carry, source=source)

    def shapes(self) -> list[dict]:
        """The input shapes of each version: the decoder's, then the
        encoder's, named with ``encoder_`` before each.
        """
        encoded = [
            {f"encoder_{n}": shape for n, shape in s.items()}
            for s in self.encoder.shapes()
        ]
        return [*super().shapes(), *encoded]

    def loaded(self, versions: list) -> None:
        """Run the decoder's versions (``use``) and hold the encode
        version.
        """
        decode_step, prompt_chunk, self._encode = versions
        self.use(decode_step, prompt_chunk)

    def encode(self, *raw) -> None:
        """Run the encoder on ``raw``, as its ``inputs`` takes it, and hold
        its keys and values for the calls after; the caches' tokens are
        forgotten, since each attended over the encoder's last output.

        Raises:
            RuntimeError: The versions are not loaded: ``load_versions()`` first.
        """
        if self._encode is None:
            raise RuntimeError(f"{type(self).__name__}: load_versions() first")
        buffer, values = self.encoder.inputs(*raw)
        self._source = self.encoder.soft(values)
        name = f"encoder_{self.encoder_input}"
        inputs = [buffer if n == name else None for n in self._parameters.inputs]
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
