# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator


@operator
class SigmoidOverlay(ChanneledUnaryOverlay):
    """The array for Sigmoid: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "sigmoid"
    kernel_fn_name: ClassVar[str] = "sigmoid_bf16"
    needs_lut_ops: ClassVar[bool] = True


@operator
class Sigmoid(ChanneledUnaryOperator[SigmoidOverlay]):
    """AIE-accelerated Sigmoid activation function"""

    pass
