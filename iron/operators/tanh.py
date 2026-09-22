# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class TanhOverlay(ChanneledUnaryOverlay):
    """The array for Tanh: the shared elementwise design over its kernel."""

    def kernel(self, target):
        return activation.tanh(self.line_size)


@operator
class Tanh(ChanneledUnaryOperator[TanhOverlay]):
    """AIE-accelerated Tanh activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 4096))

    def reference(self, x):
        import torch

        return torch.tanh(x)
