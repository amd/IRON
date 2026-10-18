# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import norm

from iron.common import WeightedRowwise


class LayerNorm(WeightedRowwise):
    """AIE-accelerated Layer Normalization of each row (beta 0), optionally
    times a learned weight row (gamma).
    """

    class Array(WeightedRowwise.Array):
        def kernel(self):
            return norm.layer_norm(self.tile_size)
