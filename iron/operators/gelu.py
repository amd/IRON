# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import numpy as np
from aie.iron.kernels import activation
from aie.utils.verify import Tolerance

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases


class GELU(UnaryElementwise):
    """AIE-accelerated GELU activation function."""

    test = Testing(channeled_unary_cases(), tolerance=Tolerance.relative(0.04, 1e-6))

    tile_cap: ClassVar[int] = 8192

    def kernel(self, target):
        return activation.gelu_sized(self.tile_size)

    def reference(self, x):
        """CPU reference: the tanh approximation the kernel computes."""
        f = x.astype(np.float32)
        inner = np.sqrt(np.float32(2 / np.pi)) * (f + np.float32(0.044715) * f**3)
        return (0.5 * f * (1 + np.tanh(inner))).astype(x.dtype)
