# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's own parts: Gemma's sandwich-normed layer
(``SandwichLayer``), the text encoder's (``TextLayer``) and the audio
tower's clipped linear (``Clipped``).
"""

import dataclasses
from types import SimpleNamespace

import numpy as np

import iron.functional as F
from iron.functional import ACCURATE
from iron.lm import DecoderLayer
from iron.operators.clamp import Clamp
from iron.operators.elementwise_mul import RowwiseMul
from iron.operators.gemm import GEMM


@dataclasses.dataclass(frozen=True)
class SandwichLayer(DecoderLayer):
    """``DecoderLayer`` with each block's output normed again before its
    residual, by ``post_attention_layernorm`` and
    ``post_feedforward_layernorm``, the feed-forward's input by
    ``pre_feedforward_layernorm``.
    """

    def __call__(self, w, x, attend, angles):
        h = self.attention(w.self_attn, self.norm(x, w.input_layernorm), attend, angles)
        x = self.add(x, self.norm(h, w.post_attention_layernorm))
        h = self.mlp(w.mlp, self.norm(x, w.pre_feedforward_layernorm))
        return self.add(x, self.norm(h, w.post_feedforward_layernorm))


@dataclasses.dataclass(frozen=True)
class TextLayer(SandwichLayer):
    """``SandwichLayer``, then its per-layer input gated in
    (``per_layer_input_gate``, ``per_layer_projection``,
    ``post_per_layer_input_norm``) and the sum scaled by ``layer_scalar``.
    """

    def __call__(self, w, x, attend, angles, *, ple, scale):
        """The layer on ``x``; ``ple`` is its per-layer input ``(rows,
        ple_dim)``, ``scale`` its ``layer_scalar`` as a row.
        """
        x = super().__call__(w, x, attend, angles)
        act = F.silu if self.mlp.activation == "silu" else F.gelu
        accurate = self.mlp.accurate
        g = act(F.linear(x, w.per_layer_input_gate.weight, accurate=accurate)) * ple
        g = F.linear(g, w.per_layer_projection.weight, accurate=accurate)
        x = x + F.rms_norm(g, w.post_per_layer_input_norm.weight, self.norm.eps)
        return RowwiseMul.step(x, scale)


@dataclasses.dataclass(frozen=True)
class Clipped:
    """A checkpoint's clipped linear: clamp, project by ``weight``, clamp."""

    linear: SimpleNamespace

    def clamp(self, x):
        w = self.linear
        return Clamp.step(x, low=float(w.input_min), high=float(w.input_max))

    def project(self, x, weight: np.ndarray | None = None):
        """``x``, already clamped, projected and clamped."""
        w = self.linear
        weight = w.linear.weight if weight is None else weight
        y = GEMM.step(x, weight, b_col_maj=True, **ACCURATE)
        return Clamp.step(y, low=float(w.output_min), high=float(w.output_max))

    def __call__(self, x):
        return self.project(self.clamp(x))
