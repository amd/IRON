# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import UnaryElementwise, auto
from iron.common.testing import Testing, channeled_unary_cases


class SiLU(UnaryElementwise):
    """AIE-accelerated SiLU activation function."""

    test = Testing(channeled_unary_cases(channels=None))

    # One channel per column: the LUT-based kernel is sized for it.
    num_channels: int = auto(1, repr=False, init=False)

    def kernel(self, target):
        return activation.silu_sized(self.tile_size)
