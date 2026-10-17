#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Phi-4-mini-instruct over the shared decoder and layer (``iron.lm``): its
head on the NPU (``Phi4``) and on the CPU in float32 (``Phi4Oracle``, the
reference it is judged by), its tokenizer and its shape, read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.phi3.model``.

Phi-4-mini is Llama's layer with three differences, each ``Layer``'s or
``DecoderConfig``'s:

* **Fused projections.** Its checkpoint holds one ``qkv_proj`` and one
  ``mlp.gate_up_proj``, which ``Layer`` cuts by rows, each piece a view of
  the checkpoint's own array.
* **Partial rotary.** Only the first ``rotary_dim`` (96 of 128) columns of
  each head rotate (``partial_rotary_factor``); ``Layer`` turns that
  prefix alone.
* **LongRoPE.** Within ``original_max_position_embeddings`` (4096) every
  position takes the ``short_factor`` (all 1.0) and LongRoPE's constant
  amplitude scale, derived from that and ``max_position_embeddings``.

TODO(Erika's LongRoPE call): the ``long_factor`` regime, which the native
131072-position context needs; until it is built ``max_seq_len`` stays
4096, the short regime's whole range.
"""

import dataclasses
import math
from pathlib import Path

from tokenizers import Tokenizer

from iron import lm
from iron.lm import CausalLM, DecoderConfig, Oracle, widen
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm


@dataclasses.dataclass(frozen=True)
class Phi4Config(DecoderConfig):
    """``DecoderConfig`` and Phi-4-mini-instruct's own partial rotary and
    LongRoPE short regime.
    """

    # The short_factor regime's range, until the long_factor one is built.
    max_seq_len: int = 4096
    partial_rotary_factor: float = dataclasses.field(
        default=1.0, kw_only=True, metadata={"json": "partial_rotary_factor"}
    )
    original_max_position_embeddings: int | None = dataclasses.field(
        default=None,
        kw_only=True,
        metadata={"json": "original_max_position_embeddings"},
    )
    # The checkpoint's own full LongRoPE context (max_position_embeddings),
    # for the amplitude formula alone: this port's own max_seq_len (4096)
    # stays within original_max_position_embeddings's short regime.
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


class Phi4Oracle(Oracle):
    """Phi-4-mini-instruct's forward pass in float32, on the host."""

    def head(self, x):
        norm = widen(self.weights.model.norm.weight)
        return self.rms_norm(x, norm) @ self.embedding.T


class Phi4(CausalLM):
    """Phi-4-mini-instruct on ``config``'s shape and a checkpoint's
    ``weights``, by its names. The embedding is the output head too. Every
    matrix is read ``(out, in)``, as the checkpoint ships it: GEMV's ``(M,
    K)`` and GEMM's column-major B.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Phi4Oracle

    def head(self, x):
        return GEMV.step(
            self.weights.model.embed_tokens.weight,
            RMSNorm.step(
                x, weight=self.weights.model.norm.weight, epsilon=self.config.eps
            ),
        )


class Phi4Tokenizer:
    """Phi-4-mini-instruct's tokenizer, Hugging Face's ``tokenizers`` over
    its ``tokenizer.json`` (an auto-converted GPT-4o-style BPE, not a
    tiktoken ``.model`` file: no chat template or added-token handling
    beyond plain encode/decode, enough for a teacher-forced oracle check
    and a raw continuation).
    """

    def __init__(self, path):
        self._tokenizer = Tokenizer.from_file(str(path))

    def encode(self, text: str) -> list[int]:
        return self._tokenizer.encode(text).ids

    def decode(self, tokens) -> str:
        return self._tokenizer.decode(list(tokens))


#: ``<|endoftext|>``, the checkpoint's bos_token, eos_token and pad_token alike.
BOS = 199999


class Runner(lm.Runner):
    """Phi-4-mini-instruct, from its checkpoint (one file, or a sharded
    index) and ``tokenizer.json``.
    """

    config = Phi4Config
    model = Phi4
    open_tokenizer = Phi4Tokenizer
    bos = BOS


if __name__ == "__main__":
    lm.main(Runner, "Phi-4-mini-instruct on the NPU")
