#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4's text model over the shared decoder and layer (``iron.lm``):
its shape (``Gemma4Config``), its float32 forward pass on the host
(``Gemma4Oracle``, the reference it is judged by).

Each layer is ``Layer``: sandwich norms, q, k and v norms, GeGLU, a layer
scalar and a per-layer input, the sum of the embedding projected for the
layer and a row of the layer's own table by token. Sliding layers attend
within ``sliding_window`` positions, global layers over every position at a
wider head and rotate a quarter of it ("proportional" RoPE), and the last
``num_kv_shared_layers`` attend over the keys and values of the last earlier
layer of their kind. The logits are soft-capped.
"""

import dataclasses
import math

import numpy as np

from iron.lm import DecoderConfig, Layer, Oracle, rope_angles, widen


def _global_layers(layer_types: list[str]) -> tuple[int, ...]:
    return tuple(i for i, kind in enumerate(layer_types) if kind == "full_attention")


@dataclasses.dataclass(frozen=True)
class Proportional:
    """Proportional RoPE's frequencies: the first ``rotated`` of a head's
    pairs turn as the default's, the rest not at all.
    """

    rotated: int

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        return np.where(np.arange(inv_freq.size) < self.rotated, inv_freq, 0)


@dataclasses.dataclass(frozen=True)
class Gemma4Config(DecoderConfig):
    """Gemma 4's text model, from its checkpoint's ``text_config``: the
    shape of a sliding layer, and a global layer's own head size and RoPE.
    Its own key and value heads (``num_global_key_value_heads``) are read
    only with ``attention_k_eq_v``, which is not built.
    """

    vocab_size: int = dataclasses.field(metadata={"json": "text_config.vocab_size"})
    hidden_size: int = dataclasses.field(metadata={"json": "text_config.hidden_size"})
    num_hidden_layers: int = dataclasses.field(
        metadata={"json": "text_config.num_hidden_layers"}
    )
    num_attention_heads: int = dataclasses.field(
        metadata={"json": "text_config.num_attention_heads"}
    )
    num_key_value_heads: int = dataclasses.field(
        metadata={"json": "text_config.num_key_value_heads"}
    )
    head_dim: int = dataclasses.field(metadata={"json": "text_config.head_dim"})
    intermediate_size: int = dataclasses.field(
        metadata={"json": "text_config.intermediate_size"}
    )
    rope_theta: float = dataclasses.field(
        metadata={"json": "text_config.rope_parameters.sliding_attention.rope_theta"}
    )
    max_seq_len: int = dataclasses.field(
        default=131072, metadata={"json": "text_config.max_position_embeddings"}
    )
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh",
        metadata={"json": "text_config.hidden_activation"},
    )
    global_layers: tuple[int, ...] = dataclasses.field(
        default=(),
        metadata={"json": "text_config.layer_types", "convert": _global_layers},
    )
    global_head_dim: int = dataclasses.field(
        default=512, metadata={"json": "text_config.global_head_dim"}
    )
    global_rope_base: float = dataclasses.field(
        default=1000000.0,
        metadata={"json": "text_config.rope_parameters.full_attention.rope_theta"},
    )
    global_rotary: float = dataclasses.field(
        default=0.25,
        metadata={
            "json": "text_config.rope_parameters.full_attention.partial_rotary_factor"
        },
    )
    # A sliding layer's query attends over itself and the positions before
    # it, this many keys in all.
    sliding_window: int = dataclasses.field(
        default=512, metadata={"json": "text_config.sliding_window"}
    )
    shared_layers: int = dataclasses.field(
        default=0, metadata={"json": "text_config.num_kv_shared_layers"}
    )
    ple_dim: int = dataclasses.field(
        default=256, metadata={"json": "text_config.hidden_size_per_layer_input"}
    )
    logit_cap: float = dataclasses.field(
        default=30.0, metadata={"json": "text_config.final_logit_softcapping"}
    )
    k_eq_v: bool = dataclasses.field(
        default=False, metadata={"json": "text_config.attention_k_eq_v"}
    )
    moe: bool = dataclasses.field(
        default=False, metadata={"json": "text_config.enable_moe_block"}
    )
    eps: float = dataclasses.field(
        default=1e-6, kw_only=True, metadata={"json": "text_config.rms_norm_eps"}
    )

    def __post_init__(self):
        super().__post_init__()
        if self.k_eq_v or self.moe:
            raise ValueError(
                "Gemma4Config: attention_k_eq_v and enable_moe_block are not built"
            )

    def heads(self, i: int) -> tuple[int, int]:
        """Layer ``i``'s key and value heads and head size."""
        if i in self.global_layers:
            return self.num_key_value_heads, self.global_head_dim
        return self.num_key_value_heads, self.head_dim

    def kv_source(self, i: int) -> int:
        """Layer ``i`` itself, or for a shared layer the last layer of its
        kind before the shared ones.
        """
        first = self.num_hidden_layers - self.shared_layers
        if i < first:
            return i
        kind = i in self.global_layers
        return max(j for j in range(first) if (j in self.global_layers) == kind)

    def layer(self, i: int) -> Layer:
        """Layer ``i``: unscaled attention over RMS-normed values, a sliding
        layer's within ``sliding_window`` keys, and a per-layer input scaled
        by ``2 ** -0.5``.
        """
        G, D = self.heads(i)
        return Layer(
            heads=self.num_attention_heads,
            groups=G,
            head_dim=D,
            eps=self.eps,
            activation=self.hidden_act,
            scale=1.0,
            window=None if i in self.global_layers else self.sliding_window - 1,
            v_norm=True,
            accurate=True,
            shares_kv=self.kv_source(i) != i,
            ple_scale=2**-0.5,
        )

    def global_angles(self) -> np.ndarray:
        """A global layer's RoPE table, a row per position: its first
        ``global_rotary`` of each head's pairs turn.
        """
        D = self.global_head_dim
        rotated = Proportional(int(self.global_rotary * D // 2))
        return rope_angles(D, self.max_seq_len, self.global_rope_base, rotated)


class Gemma4Oracle(Oracle):
    """Gemma 4's text model in float32, on the host: the embedding scaled
    by ``sqrt(hidden_size)``, each layer's per-layer input and the soft-capped
    head over the tied embedding.
    """

    def __init__(self, config: Gemma4Config, weights):
        super().__init__(config, weights, weights.model.language_model)
        self.global_angles = config.global_angles()

    def embed(self, x):
        return x * np.float32(math.sqrt(self.config.hidden_size))

    def per_layer_inputs(self, tokens, x) -> np.ndarray:
        """Each layer's per-layer input for ``tokens`` embedded as ``x``,
        ``(rows, num_hidden_layers, ple_dim)``, over its ``2 ** -0.5``: the
        embedding projected and normed, plus the layer's own row.
        """
        c, d = self.config, self.decoder
        n, L, P = x.shape[0], c.num_hidden_layers, c.ple_dim
        projection = widen(d.per_layer_model_projection.weight)
        context = (x @ projection.T) * np.float32(c.hidden_size**-0.5)
        norm = widen(d.per_layer_projection_norm.weight)
        context = self.rms_norm(context.reshape(n, L, P), norm)
        rows = widen(d.embed_tokens_per_layer.weight[tokens]).reshape(n, L, P)
        return context + rows * np.float32(math.sqrt(P))

    def logits(self, tokens) -> np.ndarray:
        c = self.config
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n = tokens.size
        tables = {
            c.head_dim: self.angles[:n],
            c.global_head_dim: self.global_angles[:n],
        }
        x = self.embed(self.embedding[tokens])
        ple = self.per_layer_inputs(tokens, x)
        self.shared = {}
        for i, w in enumerate(self.layers):
            angles = tables[c.heads(i)[1]]
            x = self.layer(i, angles, widen(w), x, ple=ple[:, i])
        return self.head(x[-1])

    def head(self, x):
        c = self.config
        norm = widen(self.decoder.norm.weight)
        cap = np.float32(c.logit_cap)
        return np.tanh((self.rms_norm(x, norm) @ self.embedding.T) / cap) * cap
