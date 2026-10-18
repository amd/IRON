# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron import CompileTime
from aie.iron.kernels import datamovement

from iron.common import BinaryElementwise, field
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class AXPY(BinaryElementwise):
    """AIE-accelerated aX + Y operator."""

    # A second scalar on one shape, so it is seen to reach the kernel.
    test = Testing(
        [
            Sweep(channels=None, scalar_factor=3.0),
            Case(
                dict(size=2048, num_aie_columns=1, tile_size=2048, scalar_factor=1.003)
            ),
        ]
    )

    scalar_factor: CompileTime[float] = field(default=3.0, array=True)

    class Array(BinaryElementwise.Array):
        def kernel(self):
            return datamovement.axpy(self.tile_size)

        def scalars(self) -> tuple:
            return (self.scalar_factor,)
