# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What EmbeddingGemma 2's graphs share beyond ``iron.lm.Layer``: ``attend``,
the bidirectional attention its text encoder and vision tower give their
layers, and ``Clipped``, the audio tower's clipped linear.
"""

import dataclasses
from types import SimpleNamespace

import numpy as np

from iron.lm.blocks import ACCURATE
from iron.operators.clamp import Clamp
from iron.operators.gemm import GEMM
from iron.operators.mha import MHA


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


def attend(q, k, v, *, scale: float | None, window: int | None):
    """Attention of ``q`` ``(rows, heads, head_dim)`` over ``k`` and ``v``
    ``(rows, groups, head_dim)``, bidirectional, within ``window`` positions
    if given; ``Layer``'s ``attend``.
    """
    n, H, D = q.shape
    o = MHA.step(
        q,
        k,
        v,
        heads_interleaved=True,
        kv_interleaved=True,
        causal=False,
        emulate_bf16_mmul_with_bfp16=False,
        window=window,
        scale=scale,
    )
    return o.reshape(n, H * D)
