# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's own parts: Gemma's sandwich-normed layer
(``SandwichLayer``), the text encoder's (``TextLayer``) and the audio
tower's clipped linear (``Clipped``).
"""

import dataclasses
from functools import partial
from types import SimpleNamespace

import numpy as np

import iron.functional as F
from iron import Precision
from iron.lm import DecoderLayerSpec
from iron.operators.clamp import Clamp


@dataclasses.dataclass(frozen=True)
class SandwichLayer(DecoderLayerSpec):
    """``DecoderLayerSpec`` with each block's output normed again before its
    residual, by ``post_attention_layernorm`` and
    ``post_feedforward_layernorm``, the feed-forward's input by
    ``pre_feedforward_layernorm``.
    """

    def __call__(self, w, x, attend, angles):
        attention = partial(self.attention, w.self_attn, attend=attend, angles=angles)
        x = self.block(x, w.input_layernorm, attention, w.post_attention_layernorm)
        mlp = partial(self.mlp, w.mlp)
        return self.block(
            x, w.pre_feedforward_layernorm, mlp, w.post_feedforward_layernorm
        )


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
        act = self.mlp.act
        precision = self.mlp.precision
        g = act(F.linear(x, w.per_layer_input_gate.weight, precision=precision)) * ple
        g = F.linear(g, w.per_layer_projection.weight, precision=precision)
        x = self.add(x, self.norm(w.post_per_layer_input_norm, g))
        return x * scale


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
        y = F.linear(x, weight, precision=Precision.HIGHEST)
        return Clamp.step(y, low=float(w.output_min), high=float(w.output_max))

    def __call__(self, x):
        return self.project(self.clamp(x))
