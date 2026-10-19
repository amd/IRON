#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct on the shared decoder (``iron.lm``), its shape read
from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.phi3.model``.

Phi-4-mini is Llama's layer with three differences:

* **Fused projections.** Its checkpoint holds one ``qkv_proj`` and one
  ``mlp.gate_up_proj``, each one ``Linear`` whose rows a call projects by
  in turn (``Linear.split``).
* **Partial rotary.** Only the first ``rotary_dim`` (96 of 128) columns of
  each head rotate (``partial_rotary_factor``); ``Attention`` turns that
  prefix alone.
* **LongRoPE.** A forward call whose sequence passes
  ``original_max_position_embeddings`` (4096) rotates by the
  ``long_factor`` frequencies, any other by the ``short_factor`` ones, and
  every one carries LongRoPE's constant amplitude scale; rows a cache holds
  keep the rotation they were written with. ``angles`` stacks the long
  table, which a prompt passing 4096 reads (``LongRopeTable``), after the
  one a decode step reads at its position: short below 4096, long from it.
"""

import dataclasses
import math
from pathlib import Path

import numpy as np

from iron import lm
from iron.lm import (
    Attention,
    CausalLM,
    DecoderConfig,
    DecoderLayer,
    GatedMLP,
    Linear,
    not_json,
    rope_angles,
)
from iron.lm.blocks import Rope
from iron.operators.copy import Copy


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

    def to_json(self) -> dict:
        """The checkpoint's own ``rope_scaling``: ``from_dict``'s inverse."""
        return {
            "type": "longrope",
            "short_factor": list(self.short_factor),
            "long_factor": list(self.long_factor),
        }

    def short(self, inv_freq: np.ndarray) -> np.ndarray:
        return inv_freq / np.asarray(self.short_factor, np.float64)

    def long(self, inv_freq: np.ndarray) -> np.ndarray:
        return inv_freq / np.asarray(self.long_factor, np.float64)


@dataclasses.dataclass(frozen=True)
class Phi4Config(DecoderConfig):
    """``DecoderConfig`` and Phi-4-mini-instruct's own partial rotary and
    LongRoPE.
    """

    # LongRoPE's, read as longrope.
    rope_scaling: None = not_json(None)
    longrope: LongRope | None = dataclasses.field(
        default=None,
        kw_only=True,
        metadata={"json": "rope_scaling", "convert": LongRope.from_dict},
    )
    partial_rotary_factor: float = dataclasses.field(default=1.0, kw_only=True)
    original_max_position_embeddings: int | None = dataclasses.field(
        default=None, kw_only=True
    )

    def __post_init__(self):
        super().__post_init__()
        if self.rotary_dim is None and self.partial_rotary_factor != 1.0:
            object.__setattr__(
                self, "rotary_dim", int(self.head_dim * self.partial_rotary_factor)
            )
        # Set once, from the checkpoint's own context: a lowered max_seq_len
        # (dataclasses.replace) keeps it.
        if self.rope_attention_scaling == 1.0 and self.original_max_position_embeddings:
            factor = self.max_seq_len / self.original_max_position_embeddings
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
        """A decode step's table, short below the original context and long
        from it; then, ``max_seq_len`` rows on, the long one a prompt
        passing the original context reads.
        """
        if self.longrope is None:
            return super().angles()
        short, long = self._table(self.longrope.short), self._table(self.longrope.long)
        past = self.original_max_position_embeddings
        short[past:] = long[past:]
        return np.concatenate([short, long])


class LongRopeTable(Rope):
    """``Rope`` on LongRoPE's stacked table (``Phi4Config.angles``): a
    prompt chunk of a sequence passing ``long_past`` reads the long one,
    from the call's ``rope_start`` (``table_start``).
    """

    def __init__(self, c: Phi4Config):
        super().__init__(c)
        self.long_past, self.length = c.original_max_position_embeddings, c.max_seq_len

    def rows(self, call) -> tuple:
        if not call.prompt:
            return super().rows(call)
        start = call.rope_start
        k = Copy.step(self.table[start : start + self.chunk][: call.rows])
        return k, k

    def table_start(self, n: int) -> int:
        """The long table's first row past ``long_past`` tokens, else 0."""
        return self.length if n > self.long_past else 0


class Phi4Attention(Attention):
    """``Attention`` with q, k and v the rows of one ``qkv_proj``."""

    def projections(self, c: Phi4Config) -> None:
        H, G, D = self.heads, self.groups, self.head_dim
        self.qkv_proj = Linear(c.hidden_size, (H + 2 * G) * D, bias=False)

    def project(self, x, **gemv) -> list:
        H, G, D = self.heads, self.groups, self.head_dim
        return self.qkv_proj.split(x, H * D, G * D, G * D, **gemv)


class Phi4MLP(GatedMLP):
    """``GatedMLP`` with gate and up the rows of one ``gate_up_proj``."""

    def projections(self, c: Phi4Config) -> None:
        M = self.intermediate_size = c.intermediate_size
        self.gate_up_proj = Linear(c.hidden_size, 2 * M, bias=False)

    def body(self, x):
        M = self.intermediate_size
        gate, up = self.gate_up_proj.split(x, M, M)
        return self.down_proj(self.act(gate) * up)


class Phi4Layer(DecoderLayer):
    """Llama's layer on Phi-4's fused projections."""

    def __init__(self, c: Phi4Config, i: int):
        super().__init__(c, i, Phi4Attention(c, i), Phi4MLP(c))


class Phi4(CausalLM):
    """Phi-4-mini-instruct on ``config``'s shape and a checkpoint's
    ``weights``, from its checkpoint (one file, or a sharded index) and
    ``tokenizer.json``.
    """

    config = Phi4Config
    profile = Path(__file__).with_name("profiles")
    layer_class = Phi4Layer

    def rotary(self, config: Phi4Config) -> Rope:
        """``LongRopeTable`` where the config has LongRoPE."""
        if config.longrope is None:
            return super().rotary(config)
        return LongRopeTable(config)


if __name__ == "__main__":
    lm.main(Phi4)
