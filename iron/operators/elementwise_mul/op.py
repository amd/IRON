# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator


@operator
class ElementwiseMulOverlay(BinaryElementwiseOverlay):
    """The array for ElementwiseMul: the shared binary-elementwise design over its kernel."""

    kernel_name: ClassVar[str] = "mul"
    kernel_fn_name: ClassVar[str] = "eltwise_mul_bf16_vector_size"


@operator
class ElementwiseMul(BinaryElementwiseOperator[ElementwiseMulOverlay]):
    """AIE-accelerated element-wise multiplication"""

    def reference(self, a, b):
        from iron.operators.elementwise_mul.reference import reference

        return reference(a, b)
