# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator


@operator
class ReLUOverlay(ChanneledUnaryOverlay):
    """The array for ReLU: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "relu"
    kernel_fn_name: ClassVar[str] = "relu_bf16_size"


@operator
class ReLU(ChanneledUnaryOperator[ReLUOverlay]):
    """AIE-accelerated ReLU activation function"""

    def reference(self, x):
        from iron.operators.relu.reference import reference

        return reference(x)
