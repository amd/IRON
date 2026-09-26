# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import eltwise

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases


class ReLU(UnaryElementwise):
    """AIE-accelerated ReLU activation function."""

    test = Testing(channeled_unary_cases(), draw=dict(centered=("x",)))  # both signs

    def kernel(self, target):
        return eltwise.relu_sized(self.tile_size)

    def reference(self, x):
        """CPU reference: ``max(x, 0)``."""
        return np.maximum(x, 0)
