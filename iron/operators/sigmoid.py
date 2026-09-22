# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import torch

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class SigmoidOverlay(ChanneledUnaryOverlay):
    """The array for Sigmoid: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "sigmoid"
    kernel_fn_name: ClassVar[str] = "sigmoid_bf16"
    needs_lut_ops: ClassVar[bool] = True


@operator
class Sigmoid(ChanneledUnaryOperator[SigmoidOverlay]):
    """AIE-accelerated Sigmoid activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 4096))

    def reference(self, x):
        return torch.sigmoid(x)
