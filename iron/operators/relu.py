# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import eltwise

from iron.common import UnaryElementwise
from iron.common.elementwise import Sweep
from iron.common.testing import Testing


class ReLU(UnaryElementwise):
    """AIE-accelerated ReLU activation function."""

    test = Testing(Sweep(), draw=lambda op: dict(centered=(op.x,)))  # both signs

    class Array(UnaryElementwise.Array):
        def kernel(self):
            return eltwise.relu_sized(self.tile_size)
