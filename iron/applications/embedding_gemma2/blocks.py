# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Clipped``, EmbeddingGemma 2's audio tower's clipped linear."""

import dataclasses
from types import SimpleNamespace

import numpy as np

from iron.lm.blocks import ACCURATE
from iron.operators.clamp import Clamp
from iron.operators.gemm import GEMM


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
