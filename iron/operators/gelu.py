# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import activation

import numpy as np

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class GELUOverlay(ChanneledUnaryOverlay):
    """The array for GELU: the shared elementwise design over its kernel."""

    tile_cap: ClassVar[int] = 8192

    def kernel(self, target):
        return activation.gelu_sized(self.line_size)


@operator
class GELU(ChanneledUnaryOperator[GELUOverlay]):
    """AIE-accelerated GELU activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 8192))

    def reference(self, x):
        """CPU reference: the tanh approximation the kernel computes."""
        f = x.astype(np.float32)
        inner = np.sqrt(np.float32(2 / np.pi)) * (f + np.float32(0.044715) * f**3)
        return (0.5 * f * (1 + np.tanh(inner))).astype(x.dtype)
