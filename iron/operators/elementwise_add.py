# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwise, Link
from iron.common.testing import Case, Sweep, Testing
from iron.operators.silu import SiLU


class ElementwiseAdd(BinaryElementwise):
    """AIE-accelerated element-wise addition."""

    # A sum finished by silu in its own cores.
    test = Testing(
        [
            Sweep(channels=None),
            Case(
                dict(size=2048, num_aie_columns=4, finish=(Link(SiLU(size=2048)),)),
                id="finish_SiLU",
            ),
        ]
    )

    def kernel(self):
        return eltwise.add_sized(self.tile_size)
