# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import datamovement

from iron.common import BinaryElementwise, param
from iron.common.testing import Testing, binary_elementwise_cases


class AXPY(BinaryElementwise):
    """AIE-accelerated aX + Y operator: the elementwise design with the
    scalar as a kernel argument.
    """

    # Every split at the default scalar (the 2048 shape in the default
    # suite), then every split at a second scalar, all extensive.
    test = Testing(
        lambda cls: binary_elementwise_cases(scalar_factor=3.0)(cls)
        + binary_elementwise_cases(scalar_factor=10.0, regular=None)(cls)
    )

    scalar_factor: float = param(default=3.0, array=True)

    def kernel(self, target):
        return datamovement.axpy(self.tile_size)

    def kernel_call(self, kernel, elem_a, elem_b, elem_out) -> None:
        # saxpy takes the scalar between its inputs and its output.
        kernel(elem_a, elem_b, self.scalar_factor, elem_out, self.tile_size)

    def reference(self, a, b):
        """CPU reference: ``scalar_factor * a + b`` in fp32, rounded once, as
        the kernel computes it; the scalar is bf16 on the device.
        """
        scalar = np.float32(np.asarray(self.scalar_factor, dtype=a.dtype))
        return (scalar * a.astype(np.float32) + b.astype(np.float32)).astype(a.dtype)
