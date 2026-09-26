# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import numpy as np
from aie.iron.kernels import activation
from aie.utils.verify import Tolerance

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases

# The shortest line mlir-aie's LUT activations take.
_LUT_LINE = 1024


class Tanh(UnaryElementwise):
    """AIE-accelerated Tanh activation function."""

    test = Testing(
        channeled_unary_cases(tile_floor=_LUT_LINE),
        tolerance=Tolerance.relative(0.04, 1e-6),
    )

    default_tile: ClassVar[int] = _LUT_LINE

    def kernel(self, target):
        return activation.tanh(self.tile_size)

    def reference(self, x):
        """CPU reference: ``tanh(x)``."""
        return np.tanh(x.astype(np.float32)).astype(x.dtype)
