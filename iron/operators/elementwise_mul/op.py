# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import BinaryElementwiseOperator


@dataclass
class ElementwiseMul(BinaryElementwiseOperator):
    """AIE-accelerated element-wise multiplication"""

    kernel_name: ClassVar[str] = "mul"
    kernel_fn_name: ClassVar[str] = "eltwise_mul_bf16_vector_size"
    kernel_subdir: ClassVar[str] = "generic"
    callback_fn: ClassVar[str] = "my_eltwise_mul"
    kernels_from_mlir_aie: ClassVar[bool] = True

    def reference(self, a, b):
        from iron.operators.elementwise_mul.reference import reference

        return reference(a, b)
