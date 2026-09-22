# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import torch

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator, tunable
from iron.common.testing import Testing, channeled_unary_cases


@operator
class SiLUOverlay(ChanneledUnaryOverlay):
    """The array for SiLU: the shared channeled-unary design over its kernel."""

    # One channel per column, as before: the LUT-based kernel is sized for it.
    num_channels: int = tunable(1, repr=False, init=False)

    kernel_name: ClassVar[str] = "silu"
    kernel_fn_name: ClassVar[str] = "silu_bf16_size"
    needs_lut_ops: ClassVar[bool] = True


@operator
class SiLU(ChanneledUnaryOperator[SiLUOverlay]):
    """AIE-accelerated SiLU activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 4096, channels=None))

    def reference(self, x):
        return torch.nn.functional.silu(x)
