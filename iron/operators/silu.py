# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron import CompileTime
from aie.iron.kernels import activation

from iron.common import Auto, UnaryElementwise
from iron.common.elementwise import Sweep
from iron.common.testing import Testing


class SiLU(UnaryElementwise):
    """AIE-accelerated SiLU activation function."""

    test = Testing(Sweep(channels=None))

    # One channel per column: the LUT-based kernel is sized for it.
    num_channels: CompileTime[int] = Auto(default=1, repr=False, init=False)

    class Array(UnaryElementwise.Array):
        def kernel(self):
            # vtanh's error was most of Llama 3.2 3B's divergence; the table costs nothing.
            return activation.silu_sized(self.tile_size, use_lut=True)
