#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3's text decoder on the shared decoder (``iron.lm``), its shape
read from a ``config.json`` of Hugging Face's ``ministral3``. Run it with
``python -m iron.applications.ministral3.model``.

Ministral 3 is Llama's layer under YaRN's RoPE (``Yarn``), its queries
scaled by position past the context it was trained at: by ``1 + beta *
log(1 + floor(position / original_max_position_embeddings))``, Llama 4's
attention temperature. RoPE is linear in its angles, so the queries turn
by a second table, the first one times that scale (``Ministral3Layer``).
"""

import dataclasses
import math

import numpy as np
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import lm
from iron.lm import Attention, CausalLM, DecoderConfig, DecoderLayer
from iron.lm.blocks import Rope


@dataclasses.dataclass(frozen=True)
class Yarn:
    """YaRN's RoPE frequency scaling (``"rope_type": "yarn"``): a frequency
    turning fewer than ``beta_slow`` times over ``original`` positions is
    divided by ``factor``, one turning more than ``beta_fast`` times is
    kept, and one between is blended linearly by its dimension.
    """

    factor: float
    original_max_position_embeddings: int
    beta_fast: float = 32.0
    beta_slow: float = 1.0
    mscale: float = 1.0
    mscale_all_dim: float = 0.0
    # Hugging Face rounds the blend's bounds outward to whole dimensions.
    truncate: bool = True

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        dim = 2 * inv_freq.size
        original = self.original_max_position_embeddings

        log_base = -math.log(inv_freq[1]) * dim / 2

        def dimension(turns):
            # The dimension whose frequency turns `turns` times over `original`.
            return dim * math.log(original / (turns * 2 * math.pi)) / (2 * log_base)

        low, high = dimension(self.beta_fast), dimension(self.beta_slow)
        if self.truncate:
            low, high = math.floor(low), math.ceil(high)
        low, high = max(low, 0), min(high, dim - 1)
        ramp = np.clip((np.arange(dim // 2) - low) / max(high - low, 1e-3), 0, 1)
        return inv_freq / self.factor * ramp + inv_freq * (1 - ramp)

    def attention_factor(self) -> float:
        """What YaRN multiplies cos and sin by: its ``mscale``."""

        def mscale(m):
            return 1.0 if self.factor <= 1 else 0.1 * m * math.log(self.factor) + 1

        if self.mscale and self.mscale_all_dim:
            return mscale(self.mscale) / mscale(self.mscale_all_dim)
        return mscale(1)

    @classmethod
    def from_dict(cls, data: dict) -> "Yarn":
        """``rope_parameters`` as ``config.json`` writes them."""
        names = {f.name for f in dataclasses.fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in names})

    def to_json(self) -> dict:
        return {"rope_type": "yarn", **dataclasses.asdict(self)}


@dataclasses.dataclass(frozen=True)
class Ministral3Config(DecoderConfig):
    """``DecoderConfig`` with its RoPE base, YaRN and attention temperature
    in ``rope_parameters``.
    """

    rope_theta: float = dataclasses.field(
        metadata={"json": "rope_parameters.rope_theta"}
    )
    rope_scaling: Yarn | None = dataclasses.field(
        default=None, metadata={"json": "rope_parameters", "convert": Yarn.from_dict}
    )
    llama_4_scaling_beta: float = dataclasses.field(
        default=0.0,
        kw_only=True,
        metadata={"json": "rope_parameters.llama_4_scaling_beta"},
    )
    tie_word_embeddings: bool = False

    def __post_init__(self):
        super().__post_init__()
        if self.rope_scaling is not None:
            factor = self.rope_scaling.attention_factor()
            object.__setattr__(self, "rope_attention_scaling", factor)

    def to_json(self) -> dict:
        out = super().to_json()
        out.setdefault("rope_parameters", {})["rope_theta"] = self.rope_theta
        return out

    def query_angles(self) -> np.ndarray:
        """The RoPE table, each position's row times its query scale."""
        angles = self.angles()
        original = self.rope_scaling.original_max_position_embeddings
        blocks = np.floor(np.arange(self.max_seq_len) / original)
        scale = 1 + self.llama_4_scaling_beta * np.log1p(blocks)
        return angles * scale[:, None].astype(np.float32)


class QueryRope(Rope):
    """``Rope`` of the queries' table (``Ministral3Config.query_angles``)."""

    def __init__(self, c: Ministral3Config):
        super().__init__(c)
        self.table = iron.weight(c.query_angles().astype(bfloat16))


class Ministral3Attention(Attention):
    """Llama's attention, q turned by ``rows`` of the queries' table and k
    by the call's angles.
    """

    def body(self, x, cache, step, angles=None):
        n, H, G, D = x.shape[0], self.heads, self.groups, self.head_dim
        tiles = dict(tile_size_output=D // 2) if n == 1 else {}
        q, k, v = (
            F.linear(x, p.weight, p.bias, **tiles)
            for p in (self.q_proj, self.k_proj, self.v_proj)
        )
        rows = self.query_rope.rows(
            prompt=step.prompt,
            position=step.position,
            start=step.start,
            rows=step.rows,
            rope_start=None,
        )
        q = F.rope(q.reshape(n * H, D), rows)
        k = F.rope(k.reshape(n * G, D), angles)
        o = cache.attend(
            step, q.reshape(n, H, D), k.reshape(n, G, D), v.reshape(n, G, D)
        )
        return self.o_proj(o)


class Ministral3Layer(DecoderLayer):
    """Llama's layer, its attention ``Ministral3Attention``."""

    def __init__(self, c: Ministral3Config, i: int):
        super().__init__(c, i)
        self.self_attn = Ministral3Attention(c, i)


class Ministral3(CausalLM):
    """Ministral 3's text decoder on ``config``'s shape and a checkpoint's
    ``weights``, its (untied) output head ``lm_head``.
    """

    config = Ministral3Config
    layer_class = Ministral3Layer

    def __init__(self, config: Ministral3Config, weights):
        super().__init__(config, weights)
        rope = QueryRope(config)
        for layer in self.layers:
            layer.self_attn.query_rope = rope


if __name__ == "__main__":
    lm.main(Ministral3)
