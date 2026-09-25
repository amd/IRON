# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from aie.iron.kernels import eltwise

from iron.common import ChanneledUnaryOperator


@dataclass
class ReLU(ChanneledUnaryOperator):
    """AIE-accelerated ReLU activation function"""

    callback_fn: ClassVar[str] = "my_relu"

    def _kernel(self):
        return eltwise.relu_sized(self._line_size)

    def reference(self, x):
        from iron.operators.relu.reference import reference

        return reference(x)
