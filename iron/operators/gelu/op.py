# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import torch

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator


@operator
class GELUOverlay(ChanneledUnaryOverlay):
    """The array for GELU: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "gelu"
    kernel_fn_name: ClassVar[str] = "gelu_bf16_size"
    needs_lut_ops: ClassVar[bool] = True
    tile_cap: ClassVar[int] = 8192


@operator
class GELU(ChanneledUnaryOperator[GELUOverlay]):
    """AIE-accelerated GELU activation function"""

    def reference(self, x):
        """CPU reference: the tanh approximation the kernel computes."""
        return torch.nn.functional.gelu(x, approximate="tanh")
