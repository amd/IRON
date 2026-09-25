# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator


@dataclass
class Sigmoid(ChanneledUnaryOperator):
    """AIE-accelerated Sigmoid activation function"""

    callback_fn: ClassVar[str] = "my_sigmoid"

    def _kernel(self):
        return activation.sigmoid(self._line_size)

    def reference(self, x):
        from iron.operators.sigmoid.reference import reference

        return reference(x)
