# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import activation

import numpy as np

from aie.utils.verify import Tolerance

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class SigmoidOverlay(ChanneledUnaryOverlay):
    """The array for Sigmoid: the shared elementwise design over its kernel."""

    # The shortest line mlir-aie's LUT activations take.
    default_tile: ClassVar[int] = 1024

    def kernel(self, target):
        return activation.sigmoid(self.line_size)


@operator
class Sigmoid(ChanneledUnaryOperator[SigmoidOverlay]):
    """AIE-accelerated Sigmoid activation function"""

    test = Testing(
        channeled_unary_cases(
            [1024, 2048, 4096, 8192], 4096, tile_floor=SigmoidOverlay.default_tile
        ),
        tolerance=Tolerance.relative(0.04, 1e-6),
    )

    def reference(self, x):
        """CPU reference: ``1 / (1 + exp(-x))``."""
        f = x.astype(np.float32)
        return (1 / (1 + np.exp(-f))).astype(x.dtype)
