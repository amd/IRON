# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator
from iron.common.testing import Testing, binary_elementwise_cases


@operator
class ElementwiseAddOverlay(BinaryElementwiseOverlay):
    """The array for ElementwiseAdd: the shared binary-elementwise design over its kernel."""

    kernel_name: ClassVar[str] = "add"
    kernel_fn_name: ClassVar[str] = "eltwise_add_bf16_vector_size"


@operator
class ElementwiseAdd(BinaryElementwiseOperator[ElementwiseAddOverlay]):
    """AIE-accelerated element-wise addition"""

    test = Testing(binary_elementwise_cases([1024, 2048, 4096, 8192]))

    def reference(self, a, b):
        return a + b
