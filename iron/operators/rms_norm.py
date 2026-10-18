# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron import CompileTime
from aie.iron.kernels import norm

from iron.common import WeightedRowwise, field


class RMSNorm(WeightedRowwise):
    """AIE-accelerated RMS Normalization of each row, optionally times a
    learned weight row.
    """

    # The epsilon under the root: 1e-5 by default; a model states its own.
    epsilon: CompileTime[float] = field(default=1e-5, array=True)

    class Array(WeightedRowwise.Array):
        def kernel(self):
            return norm.rms_norm_eps(self.tile_size)

        def scalars(self) -> tuple:
            return (self.epsilon,)
