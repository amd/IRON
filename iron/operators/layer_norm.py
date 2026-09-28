# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import norm

from iron.common import Rowwise


class LayerNorm(Rowwise):
    """AIE-accelerated Layer Normalization of each row (gamma 1, beta 0)."""

    def kernel(self):
        return norm.layer_norm(self.tile_size)
