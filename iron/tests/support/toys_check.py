# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Toys ``check`` holds a call to a base call with: one multiply, its per-call bound named per side."""

import numpy as np

import iron
from iron import Scratchpad
from iron.operators.elementwise_mul import ElementwiseMul


class MulUpToN(iron.Graph):
    """``x * y`` over the first ``n`` elements, ``n`` per call."""

    def body(self, x, y, *, n: Scratchpad[np.int32]):
        return ElementwiseMul.step(x, y[:n], size=256, tile_size=64)


class MulUpToM(iron.Graph):
    """``MulUpToN`` with its per-call bound named ``m``, as the operator a graph replaces names its own."""

    def body(self, x, y, *, m: Scratchpad[np.int32]):
        return ElementwiseMul.step(x, y[:m], size=256, tile_size=64)
