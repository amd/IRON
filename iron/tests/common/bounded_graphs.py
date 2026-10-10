# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graphs whose operands a per-call value bounds, shared by the tests that
trace, tune and run them.
"""

import numpy as np

import iron
from iron.common import Scratchpad
from iron.operators import GEMM, RoPE


class Rotate(iron.Graph):
    """RoPE over the first `n` positions, `n` given per call."""

    def body(self, x, angles, *, n: Scratchpad[np.int32]):
        return RoPE(x[:n], angles[:n])


class Project(iron.Graph):
    """The first `n` rows of `x` projected by `w`."""

    def body(self, x, w, *, n: Scratchpad[np.int32]):
        return GEMM(x[:n], w, b_col_maj=True)
