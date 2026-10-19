#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 3 1B on the shared decoder (``iron.lm``), its shape read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.gemma3.model``.

Gemma 3 is a sandwich-normed layer (``SandwichLayer``) with q and k normed
per head, GELU-tanh, attention scaled by ``query_pre_attn_scalar ** -0.5``,
every norm scaling by ``1 + weight`` (rounded to bf16 at load, where HF
keeps it float32), the embedding scaled by ``sqrt(hidden_size)`` and the
output head tied to it. Its sliding layers turn q and k by a RoPE table of
their own base (``rope_local_base_freq``).

The context is at most ``sliding_window``, where a sliding layer sees
every position, until MHA keeps HF's window (its own query and the
``sliding_window - 1`` keys before it) and windows a decode step: a
checkpoint's longer native context is cut to it, a longer one asked for
refused.
"""

import dataclasses

import numpy as np
from ml_dtypes import bfloat16

from iron import lm
from iron.common.graph.compiled import walk
from iron.lm import Attention, CausalLM, DecoderConfig, RMSNorm, SandwichLayer
from iron.lm.blocks import Rope
from iron.lm.config import unscaled


@dataclasses.dataclass(frozen=True)
class Gemma3Config(DecoderConfig):
    """``DecoderConfig``, the attention scale, the sliding layers' RoPE
    base and which layers slide.

    Raises:
        ValueError: ``max_seq_len`` is past ``sliding_window``.
    """

    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh", metadata={"json": "hidden_activation"}
    )
    query_pre_attn_scalar: float = 256
    rope_local_base_freq: float = 10000.0
    # Hugging Face's default: five sliding layers, then a global one.
    layer_types: tuple[str, ...] | None = dataclasses.field(
        default=None, kw_only=True, metadata={"convert": tuple}
    )

    def __post_init__(self):
        super().__post_init__()
        if self.layer_types is None:
            kinds = ("sliding_attention",) * 5 + ("full_attention",)
            types = tuple(kinds[i % 6] for i in range(self.num_hidden_layers))
            object.__setattr__(self, "layer_types", types)
        if self.sliding_window is not None:
            if self.max_seq_len > self.sliding_window:
                raise ValueError(
                    f"Gemma3Config: max_seq_len {self.max_seq_len} is past "
                    f"sliding_window {self.sliding_window}, which MHA cannot window"
                )
            L = min(self.prefill_chunk, self.max_seq_len)
            object.__setattr__(self, "prefill_chunk", L)

    @classmethod
    def from_json(cls, data: dict, source="config.json") -> "Gemma3Config":
        """``DecoderConfig.from_json``, the native context cut to
        ``sliding_window``, and the RoPE bases from a transformers 5
        ``rope_parameters`` where it has one.

        Raises:
            ValueError: ``data`` asks for what is not built: a logit
                soft-cap, bidirectional attention or a scaled RoPE.
        """
        for key in (
            "final_logit_softcapping",
            "attn_logit_softcapping",
            "use_bidirectional_attention",
        ):
            if data.get(key):
                raise ValueError(f"{source}: {key} {data[key]!r} is not built here")
        data = dict(data)
        if data.get("rope_parameters"):
            rope = data.pop("rope_parameters")
            for kind in rope.values():
                unscaled(kind)
            data["rope_theta"] = rope["full_attention"]["rope_theta"]
            data["rope_local_base_freq"] = rope["sliding_attention"]["rope_theta"]
        window, native = data.get("sliding_window"), data.get("max_position_embeddings")
        if window is not None and native is not None:
            data["max_position_embeddings"] = min(native, window)
        return super().from_json(data, source)


class Gemma3Layer(SandwichLayer):
    """Gemma 3's layer: q and k normed per head, scaled by
    ``query_pre_attn_scalar ** -0.5``.
    """

    def __init__(self, c: Gemma3Config, i: int):
        super().__init__(c, i, Attention(c, i, norms="qk"))
        self.self_attn.scaling = c.query_pre_attn_scalar**-0.5


class Gemma3(CausalLM):
    """Gemma 3 on ``config``'s shape and a checkpoint's ``weights``, from
    its checkpoint and ``tokenizer.json``.
    """

    config = Gemma3Config
    layer_class = Gemma3Layer

    def __init__(self, config: Gemma3Config, weights):
        super().__init__(config, weights)
        local = Rope(
            dataclasses.replace(config, rope_theta=config.rope_local_base_freq)
        )
        for layer, kind in zip(self.layers, config.layer_types):
            if kind == "sliding_attention":
                layer.rope = local

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # Every norm scales by 1 + weight, summed in float32 (Gemma3RMSNorm).
        for _, weight, norm, _ in list(walk(self)):
            if isinstance(norm, RMSNorm):
                norm.weight = (weight.astype(np.float32) + 1).astype(bfloat16)

    def lookup(self, ids):
        # The embedding times sqrt(hidden_size) in the weights' dtype.
        return super().lookup(ids) * float(bfloat16(np.sqrt(self.config.hidden_size)))


if __name__ == "__main__":
    lm.main(Gemma3)
