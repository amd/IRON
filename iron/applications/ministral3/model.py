# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ministral 3's text decoder on the shared decoder (``iron.lm``), its shape
that of Hugging Face's ``ministral3`` text model. The released checkpoints
are Mistral 3's vision-language model, the text config and weights nested
under it: both are read here, the vision tower left unread. It is judged
by transformers' own Mistral 3 (``hugging_face.py``).

Ministral 3 is Llama's layer under YaRN's RoPE (``YarnRopeScaling``), its
queries scaled by position past the context it was trained at: by ``1 +
beta * log(1 + floor(position / original_max_position_embeddings))``,
Llama 4's attention temperature. RoPE is linear in its angles, so the
queries turn by a table of their own, k's times that scale (``Rope``'s
``q_scale``).
"""

import dataclasses
import math

import numpy as np

from iron import Precision, lm
from iron.lm import CausalLM, DecoderConfig, Rope, subtree
from iron.lm.checkpoint import leaves


@dataclasses.dataclass(frozen=True)
class YarnRopeScaling:
    """YaRN's RoPE frequency scaling (``"rope_type": "yarn"``): a frequency
    turning fewer than ``beta_slow`` times over the original context is
    divided by ``factor``, one turning more than ``beta_fast`` times is
    kept, and one between is blended linearly by its dimension, the blend's
    bounds rounded outward to whole dimensions. The fields are the
    checkpoint's ``rope_parameters``.
    """

    factor: float
    original_max_position_embeddings: int
    beta_fast: float = 32.0
    beta_slow: float = 1.0
    mscale: float | None = None
    mscale_all_dim: float | None = None
    attention_factor: float | None = None

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        """``inv_freq`` (radians per position, per frequency), scaled."""
        dim = 2 * inv_freq.size
        log_base = -math.log(inv_freq[1]) * dim / 2

        def dimension(turns):
            # The dimension whose frequency turns `turns` times over the
            # original context.
            original = self.original_max_position_embeddings
            return dim * math.log(original / (turns * 2 * math.pi)) / (2 * log_base)

        low = max(math.floor(dimension(self.beta_fast)), 0)
        high = min(math.ceil(dimension(self.beta_slow)), dim - 1)
        ramp = np.clip((np.arange(dim // 2) - low) / max(high - low, 1e-3), 0, 1)
        return inv_freq / self.factor * ramp + inv_freq * (1 - ramp)

    def cos_sin_scale(self) -> float:
        """What YaRN multiplies cos and sin by: ``attention_factor``, else
        its ``mscale`` over its ``mscale_all_dim``'s.
        """
        if self.attention_factor is not None:
            return self.attention_factor

        def mscale(m):
            return 1.0 if self.factor <= 1 else 0.1 * m * math.log(self.factor) + 1

        if self.mscale and self.mscale_all_dim:
            return mscale(self.mscale) / mscale(self.mscale_all_dim)
        return mscale(1)

    @classmethod
    def from_dict(cls, data: dict) -> "YarnRopeScaling":
        """``rope_parameters`` as ``config.json`` writes them, the keys not
        YaRN's dropped.
        """
        names = {f.name for f in dataclasses.fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in names})

    def to_json(self) -> dict:
        given = {k: v for k, v in dataclasses.asdict(self).items() if v is not None}
        return {"rope_type": "yarn", **given}


@dataclasses.dataclass(frozen=True)
class Ministral3Config(DecoderConfig):
    """``DecoderConfig`` with its RoPE base, YaRN and attention temperature
    in ``rope_parameters``.
    """

    precision: Precision = lm.not_json(Precision.MEDIUM, kw_only=True)
    rope_theta: float = dataclasses.field(
        metadata={"json": "rope_parameters.rope_theta"}
    )
    rope_scaling: YarnRopeScaling | None = dataclasses.field(
        default=None,
        metadata={"json": "rope_parameters", "convert": YarnRopeScaling.from_dict},
    )
    llama_4_scaling_beta: float = dataclasses.field(
        default=0.0,
        kw_only=True,
        metadata={"json": "rope_parameters.llama_4_scaling_beta"},
    )
    tie_word_embeddings: bool = False

    def __post_init__(self):
        super().__post_init__()
        if self.llama_4_scaling_beta and self.rope_scaling is None:
            raise ValueError(
                "Ministral3Config: the query temperature counts YaRN's "
                "original context, and there is no YaRN"
            )
        if self.rope_scaling is not None:
            scale = self.rope_scaling.cos_sin_scale()
            object.__setattr__(self, "rope_attention_scaling", scale)

    @classmethod
    def from_json(cls, data: dict, source="config.json") -> "Ministral3Config":
        """``DecoderConfig.from_json``, on the ``text_config`` of a Mistral 3
        checkpoint's ``config.json`` where it has one.
        """
        return super().from_json(data.get("text_config", data), source)

    def to_json(self) -> dict:
        out = super().to_json()
        # rope_scaling's dict replaced the one rope_theta was written into.
        out.setdefault("rope_parameters", {})["rope_theta"] = self.rope_theta
        return out

    def query_scale(self) -> np.ndarray:
        """Each position's query scale, float32."""
        original = self.rope_scaling.original_max_position_embeddings
        blocks = np.floor(np.arange(self.max_seq_len) / original)
        return (1 + self.llama_4_scaling_beta * np.log1p(blocks)).astype(np.float32)


def text_weights(weights):
    """The text decoder's modules of a checkpoint's tree, as ``model`` and
    ``lm_head`` (none where the head is tied): a Mistral 3 checkpoint holds
    them at ``language_model.model`` and ``language_model.lm_head`` as
    transformers 4 saved it, or ``model.language_model`` and ``lm_head`` as
    transformers 5 does. A text checkpoint is returned as it is.

    Raises:
        ValueError: The checkpoint is FP8 (a ``weight_scale_inv``).
    """
    if any(n.endswith("weight_scale_inv") for n, _ in leaves(weights)):
        raise ValueError(
            "Ministral3: an FP8 checkpoint (weight_scale_inv) is not read; "
            "take a Base (bf16) one"
        )
    found = vars(weights)
    if "language_model" in found:
        nested = vars(weights.language_model)
        model, head = nested["model"], nested.get("lm_head")
    elif "model" in found and "language_model" in vars(weights.model):
        model, head = weights.model.language_model, found.get("lm_head")
    else:
        return weights
    if head is None:
        return subtree(weights, model=model)
    return subtree(weights, model=model, lm_head=head)


class Ministral3(CausalLM):
    """Ministral 3's text decoder on ``config``'s shape and a checkpoint's
    ``weights`` (``text_weights``), its output head ``lm_head`` or, tied,
    the embedding.
    """

    config = Ministral3Config

    def __init__(self, config: Ministral3Config, weights):
        super().__init__(config, text_weights(weights))

    @property
    def hugging_face(self):
        """transformers' Mistral 3, imported only where a golden is recorded."""
        from .hugging_face import HuggingFaceMistral3

        return HuggingFaceMistral3

    def rotary(self, config: Ministral3Config) -> Rope:
        """``Rope``'s table, its queries scaled where Llama 4 scaling is on."""
        scaled = config.llama_4_scaling_beta
        return Rope(config, q_scale=config.query_scale() if scaled else None)
