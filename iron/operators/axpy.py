# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import datamovement

import numpy as np

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator
from iron.common.declare import Local, Semantics
from iron.common.testing import Case, Testing, device_columns


@operator
class AXPYOverlay(BinaryElementwiseOverlay):
    """The array for aX + Y: the elementwise design with the scalar as a kernel argument."""

    scalar_factor: float = 3.0

    def semantics(self) -> Semantics:
        return Local(1)

    def kernel(self, target):
        return datamovement.axpy(self.line_size)

    def kernel_call(self, kernel, elem_a, elem_b, elem_out) -> None:
        # saxpy takes the scalar between its inputs and its output.
        kernel(elem_a, elem_b, self.scalar_factor, elem_out, self.line_size)


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
        """CPU reference: ``scalar_factor * a + b`` in fp32, rounded once, as
        the kernel computes it; the scalar is bf16 on the device."""
        scalar = np.float32(np.asarray(self.ov.scalar_factor, dtype=a.dtype))
        return (scalar * a.astype(np.float32) + b.astype(np.float32)).astype(a.dtype)
