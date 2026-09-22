# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import numpy as np
import torch

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator
from iron.common.testing import Case, Testing, device_columns


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


def _cases():
    """Every column count that divides each size, at two scalars; the 2048
    shape at the default scalar is the default suite."""
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for cols in range(1, device_columns() + 1):
            tile_size = size // cols
            if tile_size * cols != size:
                continue
            for scalar in (3.0, 10.0):
                out.append(
                    Case(
                        dict(
                            size=size,
                            num_aie_columns=cols,
                            tile_size=tile_size,
                            scalar_factor=scalar,
                        ),
                        extensive=not (size == 2048 and scalar == 3.0),
                    )
                )
    return out


@operator
class AXPY(BinaryElementwiseOperator[AXPYOverlay]):
    """AIE-accelerated aX + Y operator"""

    test = Testing(_cases)

    def reference(self, a, b):
        """CPU reference: ``scalar_factor * a + b``."""
        return torch.tensor(self.ov.scalar_factor, dtype=a.dtype) * a + b
