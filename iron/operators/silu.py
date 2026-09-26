# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import activation
from aie.utils.verify import Tolerance

from iron.common import UnaryElementwise, auto
from iron.common.testing import Testing, channeled_unary_cases


class SiLU(UnaryElementwise):
    """AIE-accelerated SiLU activation function."""

    test = Testing(
        channeled_unary_cases(channels=None), tolerance=Tolerance.relative(0.04, 1e-6)
    )

    # One channel per column: the LUT-based kernel is sized for it.
    num_channels: int = auto(1, repr=False, init=False)

    def kernel(self, target):
        return activation.silu_sized(self.tile_size)

    def reference(self, x):
        """CPU reference: ``x * sigmoid(x)``."""
        f = x.astype(np.float32)
        return (f / (1 + np.exp(-f))).astype(x.dtype)
