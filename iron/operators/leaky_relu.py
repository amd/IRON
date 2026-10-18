# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import Param, UnaryElementwise
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class LeakyReLU(UnaryElementwise):
    """AIE-accelerated Leaky ReLU operator."""

    test = Testing(
        # Another alpha on one shape, so alpha is seen to reach the kernel.
        [
            Sweep(alpha=0.01),
            Case(
                dict(
                    size=2048,
                    num_aie_columns=1,
                    num_channels=1,
                    tile_size=2048,
                    alpha=0.1,
                )
            ),
        ],
        draw=lambda op: dict(centered=(op.x,)),
    )

    alpha: float = Param(default=0.01)

    class Array(UnaryElementwise.Array):
        alpha: float

        def kernel(self):
            return activation.leaky_relu(self.tile_size)

        def scalars(self) -> tuple:
            return (self.alpha,)
