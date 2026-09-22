# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import torch

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class TanhOverlay(ChanneledUnaryOverlay):
    """The array for Tanh: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "tanh"
    kernel_fn_name: ClassVar[str] = "tanh_bf16"
    needs_lut_ops: ClassVar[bool] = True


@operator
class Tanh(ChanneledUnaryOperator[TanhOverlay]):
    """AIE-accelerated Tanh activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 4096))

    def reference(self, x):
        return torch.tanh(x)
