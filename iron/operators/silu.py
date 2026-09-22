# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator, tunable
from iron.common.testing import Testing, channeled_unary_cases


@operator
class SiLUOverlay(ChanneledUnaryOverlay):
    """The array for SiLU: the shared elementwise design over its kernel."""

    # One channel per column, as before: the LUT-based kernel is sized for it.
    num_channels: int = tunable(1, repr=False, init=False)

    def kernel(self, target):
        return activation.silu_sized(self.line_size)


@operator
class SiLU(ChanneledUnaryOperator[SiLUOverlay]):
    """AIE-accelerated SiLU activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 4096, channels=None))

    def reference(self, x):
        return torch.nn.functional.silu(x)
