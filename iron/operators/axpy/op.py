# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import numpy as np
import torch

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator


@operator
class AXPYOverlay(BinaryElementwiseOverlay):
    """The array for aX + Y: the binary-elementwise design with the scalar as a kernel argument."""

    scalar_factor: float = 3.0

    kernel_name: ClassVar[str] = "axpy"
    kernel_fn_name: ClassVar[str] = "saxpy"

    def kernel_source(self, target):
        # axpy.cc is architecture-independent and lives under generic/.
        return target.kernels_dir / "generic" / "axpy.cc"

    def kernel_arg_types(self, tile_type) -> list:
        return [tile_type, tile_type, np.float32, tile_type, np.int32]

    def kernel_call(self, kernel, elem_a, elem_b, elem_out) -> None:
        kernel(elem_a, elem_b, self.scalar_factor, elem_out, self.per_tile)


@operator
class AXPY(BinaryElementwiseOperator[AXPYOverlay]):
    """AIE-accelerated aX + Y operator"""

    def reference(self, a, b):
        """CPU reference: ``scalar_factor * a + b``."""
        return torch.tensor(self.ov.scalar_factor, dtype=a.dtype) * a + b
