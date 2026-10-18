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

import numpy as np

import iron
from iron import Carried
from iron.operators.mha import MHA

from .config import DecoderConfig
from .causal import CausalLM, DecodeStep
from .encoder import Encoder


class EncoderDecoder(CausalLM):
    """A decoder on ``config``'s shape over the output of ``encoder``; a
    subclass gives ``head`` as a ``CausalLM``'s does.

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
        ValueError: The encoder's rows are fewer than a prompt chunk's.
    """

    def __init__(self, config: DecoderConfig, weights, encoder: Encoder, decoder=None):
        super().__init__(config, weights, decoder)
        self.encoder = encoder
        rows = encoder.soft_rows
        if rows < config.prefill_chunk:
            # A prompt chunk's queries are the last rows of what MHA attends.
            raise ValueError(
                f"EncoderDecoder: the encoder's {rows} rows are fewer than a "
                f"{config.prefill_chunk}-row prompt chunk's queries"
            )
        shapes = [
            (rows, a.groups, a.head_dim)
            for a in (
                config.layer(i).attention for i in range(config.num_hidden_layers)
            )
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
        given = dict(zip(self._parameters.inputs, inputs))
        encoded = given[f"encoder_{self.encoder_input}"]
        if encoded is not None:
            own = {v: values[f"encoder_{v}"] for v in self.encoder_values}
            memory = self.encoder.inline(self.encoder.body, encoded, **own)
            for i, w in enumerate(self.layers):
                k, v = self.config.layer(i).keys_values(w, memory)
                self.cross_keys[i][: k.shape[0]] = k
                self.cross_values[i][: v.shape[0]] = v
            return iron.carry(**{n: values[n] for n in self._parameters.carried})
        ids, rows, source = given["ids"], values["rows"], values["source"]
        prompt = ids is not None
        if prompt:
            x = self.lookup(ids[:rows])
        else:
            x = self.lookup(values["token"]).reshape(1, self.config.hidden_size)
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
        return self.config.layer(i)(weights, x, attend, step.angles, cross)

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
