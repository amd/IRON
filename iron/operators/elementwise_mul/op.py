# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwiseOperator


@dataclass
class ElementwiseMul(BinaryElementwiseOperator):
    """AIE-accelerated element-wise multiplication"""

    callback_fn: ClassVar[str] = "my_eltwise_mul"

    def _kernel(self):
        return eltwise.mul_sized(self._tile_elements)

    def reference(self, a, b):
        from iron.operators.elementwise_mul.reference import reference

        return reference(a, b)
