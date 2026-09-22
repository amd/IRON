# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from aie.iron.kernels import eltwise

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class ReLUOverlay(ChanneledUnaryOverlay):
    """The array for ReLU: the shared elementwise design over its kernel."""

    def kernel(self, target):
        return eltwise.relu_sized(self.line_size)


@operator
class ReLU(ChanneledUnaryOperator[ReLUOverlay]):
    """AIE-accelerated ReLU activation function"""

    test = Testing(
        channeled_unary_cases([1024, 2048, 4096, 8192], 4096),
        draw=dict(centered=("x",)),  # both signs
    )

    def reference(self, x):
        return torch.nn.functional.relu(x)
