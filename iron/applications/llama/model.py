#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 on the shared decoder (``iron.lm``): Llama 3's RoPE scaling and
Llama 3.2 1B's shape. Run it with ``python -m
iron.applications.llama.model``.

The operators' tunables are the graph's profile, ``profiles/<device>.json``,
keyed by operator shape at Llama 3.2 1B's shape: a decode step's and a
2048-row prompt chunk's, at any ``max_seq_len``, which sizes the caches and
the RoPE table alone. A call site gives a tunable only where two operators of
one shape want different ones.
"""

import dataclasses
from pathlib import Path

import numpy as np

from iron import Precision, lm
from iron.lm import CausalLM, DecoderConfig


@dataclasses.dataclass(frozen=True)
class Llama3RopeScaling:
    """Llama 3's RoPE frequency scaling (``"rope_type": "llama3"``).

    How Llama 3.1 and later stretch a model trained at
    ``original_max_position_embeddings`` to a longer context, by frequency:
    one whose wavelength is under ``original / high_freq_factor`` positions
    is kept, one over ``original / low_freq_factor`` is divided by
    ``factor``, and one between is interpolated between the two by where its
    wavelength falls. The fields are the checkpoint's ``rope_scaling``.
    """

    factor: float
    low_freq_factor: float
    high_freq_factor: float
    original_max_position_embeddings: int

    def __call__(self, inv_freq: np.ndarray) -> np.ndarray:
        """``inv_freq`` (radians per position, per frequency), scaled."""
        original = self.original_max_position_embeddings
        wavelen = 2 * np.pi / inv_freq
        smooth = (original / wavelen - self.low_freq_factor) / (
            self.high_freq_factor - self.low_freq_factor
        )
        between = (1 - smooth) * inv_freq / self.factor + smooth * inv_freq
        return np.where(
            wavelen < original / self.high_freq_factor,
            inv_freq,
            np.where(
                wavelen > original / self.low_freq_factor,
                inv_freq / self.factor,
                between,
            ),
        )

    @classmethod
    def from_dict(cls, data: dict) -> "Llama3RopeScaling":
        """``data`` as the checkpoint's own ``rope_scaling``, its
        ``rope_type`` (every size's is ``"llama3"``) dropped.

        Raises:
            ValueError: Its ``rope_type`` is another.
        """
        if data.get("rope_type") != "llama3":
            raise ValueError(f"rope_scaling {data}: no RoPE table here builds it")
        return cls(**{k: v for k, v in data.items() if k != "rope_type"})

    def to_json(self) -> dict:
        """The checkpoint's own ``rope_scaling``: ``from_dict``'s inverse."""
        return {"rope_type": "llama3", **dataclasses.asdict(self)}


@dataclasses.dataclass(frozen=True)
class LlamaConfig(DecoderConfig):
    """``DecoderConfig``, Llama 3's own ``rope_scaling``, and every
    projection's ``precision``: a caller's, else ``Precision.HIGH`` from
    3B's width up, else ``F.linear``'s.
    """

    rope_scaling: Llama3RopeScaling | None = dataclasses.field(
        default=None, metadata={"convert": Llama3RopeScaling.from_dict}
    )
    precision: Precision | None = lm.not_json(None, kw_only=True)

    def __post_init__(self):
        super().__post_init__()
        # 3B's accuracy needs bf16 macs on its projections (decision 40).
        if self.precision is None and self.hidden_size >= 3072:
            object.__setattr__(self, "precision", Precision.HIGH)


class Llama(CausalLM):
    """Llama 3 on ``config``'s shape and a checkpoint's ``weights``."""

    config = LlamaConfig
    profile = Path(__file__).with_name("profiles")


if __name__ == "__main__":
    lm.main(Llama)
