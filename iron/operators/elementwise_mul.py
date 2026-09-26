# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator
from iron.common.testing import Testing, binary_elementwise_cases


@operator
class ElementwiseMulOverlay(BinaryElementwiseOverlay):
    """The array for ElementwiseMul: the shared elementwise design over its kernel."""

    def kernel(self, target):
        return eltwise.mul_sized(self.line_size)


@operator
class ElementwiseMul(BinaryElementwiseOperator[ElementwiseMulOverlay]):
    """AIE-accelerated element-wise multiplication"""

    test = Testing(binary_elementwise_cases([1024, 2048, 4096, 8192], 4096))

    def reference(self, a, b):
        return a * b
