# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import norm
from aie.utils.compile.jit.params import param

from iron.common import WeightedRowwise


class RMSNorm(WeightedRowwise):
    """AIE-accelerated RMS Normalization of each row, optionally times a
    learned weight row.
    """

    # The epsilon under the root: 1e-5 by default; a model states its own.
    epsilon: float = param(default=1e-5, array=True)

    def kernel(self):
        return norm.rms_norm_eps(self.tile_size)

    def scalars(self) -> tuple:
        return (self.epsilon,)
