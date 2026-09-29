# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import datamovement

from iron.common import BinaryElementwise, param
from iron.common.testing import Sweep, Testing


class AXPY(BinaryElementwise):
    """AIE-accelerated aX + Y operator: the elementwise design with the
    scalar bound into the kernel.
    """

    # Every split at the default scalar and at a non-integer one that bf16
    # rounds (the 2048 shape in the default suite), then every split at a
    # third scalar, all extensive.
    test = Testing(
        [
            Sweep(channels=None, scalar_factor=3.0),
            Sweep(channels=None, scalar_factor=1.003, bench=None),
            Sweep(channels=None, scalar_factor=10.0, regular=None, bench=None),
        ]
    )

    scalar_factor: float = param(default=3.0, array=True)

    def kernel(self):
        return datamovement.axpy(self.tile_size, a=self.scalar_factor)
