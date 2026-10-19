#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4 E2B's text decoder on the shared decoder (``iron.lm``), its
shape read from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.gemma4.model``.

Gemma 4 is a sandwich-normed layer with a per-layer input gated in after
its MLP (``PleLayer``), q, k and v normed per head (v unweighted),
attention unscaled, GELU-tanh, the embedding scaled by
``sqrt(hidden_size)``, a tied head and its logits soft-capped. Sliding
layers attend to their own query and the ``sliding_window - 1`` keys
before it; global layers to every key, with heads of
``global_head_dim`` and a RoPE table of their own base, of which only the
first ``partial_rotary_factor`` of the pairs turn. The last ``num_kv_shared_layers`` layers project no keys or values:
each attends over the cache of the last earlier layer of its kind, and
has an MLP twice as wide where ``use_double_wide_mlp``.

Each layer's input is (projection + table row) * 2 ** -0.5: its slice of a
projection of the embedding, normed, and its row of a second token table
(``embed_tokens_per_layer``, held a layer's columns at a time).
"""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import lm
from iron.lm import (
    Attention,
    CausalLM,
    DecoderConfig,
    Embedding,
    GatedMLP,
    Linear,
    PleLayer,
    RMSNorm,
)
from iron.lm.blocks import KVCache, Rope
from iron.lm.causal import Decoder
from iron.lm.checkpoint import subtree
from iron.operators.copy import Copy
from iron.operators.tanh import Tanh


def _text(name: str, **kwargs):
    """A field at ``text_config.`` and ``name``, from the file's root."""
    return dataclasses.field(metadata={"json": f"text_config.{name}"}, **kwargs)


@dataclasses.dataclass(frozen=True)
class Gemma4Config(DecoderConfig):
    """``DecoderConfig`` under ``text_config``, the global layers' heads and
    RoPE, the shared caches, the per-layer inputs and the logits' cap.
    """

    json_prefix = "text_config."

    rope_theta: float = _text("rope_parameters.sliding_attention.rope_theta")
    max_seq_len: int = _text("max_position_embeddings")
    hidden_act: str = _text("hidden_activation", default="gelu_pytorch_tanh")
    eps: float = _text("rms_norm_eps", default=1e-6, kw_only=True)
    layer_types: tuple[str, ...] = dataclasses.field(
        kw_only=True, metadata={"convert": tuple}
    )
    global_head_dim: int = 512
    global_rope_theta: float = _text(
        "rope_parameters.full_attention.rope_theta", default=1000000.0
    )
    partial_rotary_factor: float = _text(
        "rope_parameters.full_attention.partial_rotary_factor", default=0.25
    )
    num_kv_shared_layers: int = 0
    use_double_wide_mlp: bool = False
    ple_dim: int = _text("hidden_size_per_layer_input", default=256)
    final_logit_softcapping: float | None = None

    @classmethod
    def from_json(cls, data: dict, source="config.json") -> "Gemma4Config":
        """``DecoderConfig.from_json``.

        Raises:
            ValueError: ``data`` asks for what is not built: keys equal to
                values, experts, an attention soft-cap, bidirectional text,
                a per-layer vocabulary other than the embedding's, or RoPE
                other than the sliding layers' default and the global ones'
                proportional.
        """
        text = dict(data.get("text_config", {}))
        for key in ("attention_k_eq_v", "enable_moe_block", "attn_logit_softcapping"):
            if text.get(key):
                raise ValueError(f"{source}: {key} {text[key]!r} is not built here")
        # "vision" makes only image tokens bidirectional; text has none.
        if text.get("use_bidirectional_attention") == "all":
            raise ValueError(f"{source}: bidirectional attention is not built here")
        per_layer = text.get("vocab_size_per_layer_input", text.get("vocab_size"))
        if per_layer != text.get("vocab_size"):
            raise ValueError(
                f"{source}: vocab_size_per_layer_input {per_layer} other than "
                f"vocab_size {text.get('vocab_size')} is not built here"
            )
        rope = text.get("rope_parameters", {})
        for kind, built in (
            ("sliding_attention", "default"),
            ("full_attention", "proportional"),
        ):
            got = rope.get(kind, {}).get("rope_type", built)
            if got != built:
                raise ValueError(f"{source}: {kind} RoPE {got!r} is not built here")
        return super().from_json({**data, "text_config": text}, source)

    def full(self, i: int) -> bool:
        """Whether layer ``i`` is global."""
        return self.layer_types[i] == "full_attention"

    def owner(self, i: int) -> int:
        """The layer whose cache layer ``i`` attends over: its own, or for a
        shared layer the last one before the shared of its kind.
        """
        first = self.num_hidden_layers - self.num_kv_shared_layers
        if i < first:
            return i
        owners = [j for j in range(first) if self.full(j) == self.full(i)]
        if not owners:
            raise ValueError(
                f"Gemma4Config: shared layer {i} has no earlier layer of its kind"
            )
        return owners[-1]


class Gemma4Decoder(Decoder):
    """``Decoder`` and the per-layer inputs' token table, projection and
    norm.
    """

    def __init__(self, c: Gemma4Config, layer):
        super().__init__(c, layer)
        L, P, E = c.num_hidden_layers, c.ple_dim, c.hidden_size
        self.embed_tokens_per_layer = Embedding(c.vocab_size, L * P)
        self.per_layer_model_projection = Linear(E, L * P, False, c.precision)
        self.per_layer_projection_norm = RMSNorm(P, c.eps)


class Gemma4Layer(PleLayer):
    """Layer ``i``: unscaled attention over normed q, k and v, its heads and
    whole context a global layer's where it is one, else within the
    window, and an MLP twice as wide on a shared layer where
    ``use_double_wide_mlp``.
    """

    def __init__(self, c: Gemma4Config, i: int):
        heads = dataclasses.replace(c, head_dim=c.global_head_dim) if c.full(i) else c
        mlp = None
        if c.use_double_wide_mlp and c.owner(i) != i:
            mlp = GatedMLP(
                dataclasses.replace(c, intermediate_size=2 * c.intermediate_size)
            )
        attention = Attention(heads, i, norms="qkv")
        cache = KVCache(heads, None if c.full(i) else c.window)
        super().__init__(c, i, attention, mlp, cache)
        self.self_attn.scaling = 1.0


class Gemma4(CausalLM):
    """Gemma 4's text decoder on ``config``'s shape and a checkpoint's
    ``weights``, the decoder's under ``model.language_model`` (the towers'
    unread), from its checkpoint and ``tokenizer.json``.
    """

    config = Gemma4Config
    decoder_class = Gemma4Decoder
    layer_class = Gemma4Layer

    def __init__(self, config: Gemma4Config, weights):
        super().__init__(config, subtree(weights, model=weights.model.language_model))
        c = config
        turned = int(c.partial_rotary_factor * c.global_head_dim // 2)
        full = dataclasses.replace(
            c,
            head_dim=c.global_head_dim,
            rope_theta=c.global_rope_theta,
            # Proportional RoPE: the pairs past ``turned`` stand still.
            rope_scaling=lambda f: np.where(np.arange(f.size) < turned, f, 0),
        )
        rope = Rope(full)
        for i, layer in enumerate(self.layers):
            if c.full(i):
                layer.rope = rope
            if c.owner(i) != i:
                attention = layer.self_attn
                attention.k_proj = attention.v_proj = attention.k_norm = None
                layer.cache = self.layers[c.owner(i)].cache

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        P, m = self.config.ple_dim, self.model
        scale = np.float32(bfloat16(np.sqrt(P)))
        table = m.embed_tokens_per_layer.weight
        for i, layer in enumerate(m.layers):
            # A layer's own columns, scaled, contiguous: one gather a layer.
            rows = table[:, i * P : (i + 1) * P].astype(np.float32) * scale
            layer.per_layer_embedding = rows.astype(bfloat16)
        m.embed_tokens_per_layer = None

    def lookup(self, ids):
        # The embedding times sqrt(hidden_size) in the weights' dtype.
        return super().lookup(ids) * float(bfloat16(np.sqrt(self.config.hidden_size)))

    def layer(self, call, i, w, x):
        """Layer ``i`` on ``x``, its input from the call's embeddings and
        ids.
        """
        c, m, P = self.config, self.model, self.config.ple_dim
        projection = m.per_layer_model_projection.weight[i * P : (i + 1) * P]
        ple = F.linear(call.embeddings, projection, precision=c.precision)
        # The projection's hidden_size ** -0.5 folded into the norm's
        # epsilon: RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        norm = m.per_layer_projection_norm.weight
        ple = F.rms_norm(ple, (P,), norm, c.eps * c.hidden_size)
        token = Copy.step(iron.weight(w.per_layer_embedding)[call.ids])
        return w(x, call, (ple + token.reshape(ple.shape)) * 2**-0.5)

    def head(self, x):
        """The tied head's logits, soft-capped where the config says."""
        logits, cap = super().head(x), self.config.final_logit_softcapping
        return logits if cap is None else Tanh.step(logits * (1 / cap)) * cap


if __name__ == "__main__":
    lm.main(Gemma4)
