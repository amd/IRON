# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator


@operator
class SiLUOverlay(ChanneledUnaryOverlay):
    """The array for SiLU: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "silu"
    kernel_fn_name: ClassVar[str] = "silu_bf16_size"
    needs_lut_ops: ClassVar[bool] = True


@operator
class SiLU(ChanneledUnaryOperator[SiLUOverlay]):
    """AIE-accelerated SiLU activation function"""

    def reference(self, x):
        from iron.operators.silu.reference import reference

        return reference(x)
