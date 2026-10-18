#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct on the shared decoder (``iron.lm``), its shape read
from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.phi3.model``.

Phi-4-mini is Llama's layer with three differences, each ``Layer``'s or
``DecoderConfig``'s:

* **Fused projections.** Its checkpoint holds one ``qkv_proj`` and one
  ``mlp.gate_up_proj``, which ``Layer`` cuts by rows, each piece a view of
  the checkpoint's own array.
* **Partial rotary.** Only the first ``rotary_dim`` (96 of 128) columns of
  each head rotate (``partial_rotary_factor``); ``Layer`` turns that
  prefix alone.
* **LongRoPE.** A forward call whose sequence passes
  ``original_max_position_embeddings`` (4096) rotates by the
  ``long_factor`` frequencies, any other by the ``short_factor`` ones, and
  every one carries LongRoPE's constant amplitude scale; rows a cache holds
  keep the rotation they were written with. ``long_angles`` gives the
  long table, which a prompt passing 4096 reads (``CausalLM``), and
  ``angles`` the one a decode step reads at its position: short below
  4096, long from it.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np

from iron import lm
from iron.lm import CausalLM, DecoderConfig, rope_angles


@dataclasses.dataclass(frozen=True)
class LongRope:
    """LongRoPE's per-frequency divisors, the checkpoint's ``rope_scaling``:
    ``short_factor`` within the original context, ``long_factor`` past it.
    """

    short_factor: tuple[float, ...]
    long_factor: tuple[float, ...]

    @classmethod
    def from_dict(cls, data: dict) -> "LongRope":
        """``data`` as the checkpoint's ``rope_scaling`` (``"type":
        "longrope"``).

        Raises:
            ValueError: It is another type.
        """
        kind = data.get("type", data.get("rope_type"))
        if kind != "longrope":
            raise ValueError(f"LongRope: rope_scaling of type {kind!r}")
        return cls(tuple(data["short_factor"]), tuple(data["long_factor"]))

    def short(self, inv_freq: np.ndarray) -> np.ndarray:
        return inv_freq / np.asarray(self.short_factor, np.float64)

    def long(self, inv_freq: np.ndarray) -> np.ndarray:
        return inv_freq / np.asarray(self.long_factor, np.float64)


@dataclasses.dataclass(frozen=True)
class Phi4Config(DecoderConfig):
    """``DecoderConfig`` and Phi-4-mini-instruct's own partial rotary and
    LongRoPE.
    """

    longrope: LongRope | None = dataclasses.field(
        default=None,
        kw_only=True,
        metadata={"json": "rope_scaling", "convert": LongRope.from_dict},
    )
    partial_rotary_factor: float = dataclasses.field(
        default=1.0, kw_only=True, metadata={"json": "partial_rotary_factor"}
    )
    original_max_position_embeddings: int | None = dataclasses.field(
        default=None,
        kw_only=True,
        metadata={"json": "original_max_position_embeddings"},
    )
    # The checkpoint's own full LongRoPE context, for the amplitude formula,
    # whatever context a caller serves.
    longrope_context: int | None = dataclasses.field(
        default=None, kw_only=True, metadata={"json": "max_position_embeddings"}
    )

    def __post_init__(self):
        super().__post_init__()
        if self.rotary_dim is None and self.partial_rotary_factor != 1.0:
            object.__setattr__(
                self, "rotary_dim", int(self.head_dim * self.partial_rotary_factor)
            )
        if (
            self.rope_attention_scaling == 1.0
            and self.original_max_position_embeddings
            and self.longrope_context
        ):
            factor = self.longrope_context / self.original_max_position_embeddings
            scale = math.sqrt(
                1 + math.log(factor) / math.log(self.original_max_position_embeddings)
            )
            object.__setattr__(self, "rope_attention_scaling", scale)

    def _table(self, scaling) -> np.ndarray:
        angles = rope_angles(
            self.rope_width, self.max_seq_len, self.rope_theta, scaling
        )
        return angles * np.float32(self.rope_attention_scaling)

    def angles(self) -> np.ndarray:
        """A decode step's table: short below the original context, long
        from it.
        """
        if self.longrope is None:
            return super().angles()
        angles = self._table(self.longrope.short)
        past = self.original_max_position_embeddings
        angles[past:] = self._table(self.longrope.long)[past:]
        return angles

    def long_angles(self) -> tuple[int, np.ndarray] | None:
        if self.longrope is None:
            return None
        return self.original_max_position_embeddings, self._table(self.longrope.long)


class Phi4(CausalLM):
    """Phi-4-mini-instruct on ``config``'s shape and a checkpoint's ``weights``."""

    profile = Path(__file__).with_name("profiles")


#: ``<|endoftext|>``, the checkpoint's bos_token, eos_token and pad_token alike.
BOS = 199999


class Runner(lm.Runner):
    """Phi-4-mini-instruct, from its checkpoint (one file, or a sharded
    index) and ``tokenizer.json``.
    """

    config = Phi4Config
    model = Phi4
    bos = BOS


if __name__ == "__main__":
    lm.main(Runner, "Phi-4-mini-instruct on the NPU")
