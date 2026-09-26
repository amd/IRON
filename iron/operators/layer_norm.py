# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import field
from typing import ClassVar

import numpy as np
from aie.iron.kernels import norm
from aie.utils.verify import Tolerance

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases


class LayerNorm(UnaryElementwise):
    """AIE-accelerated Layer Normalization operator."""

    test = Testing(channeled_unary_cases(), tolerance=Tolerance.relative(0.1, 0.05))

    # Hardware trace buffer size; 0 disables tracing.
    trace_size: int = field(default=0, repr=False, kw_only=True)

    tile_cap: ClassVar[int] = 8192

    def kernel(self, target):
        return norm.layer_norm(self.tile_size)

    def reference(self, x):
        """CPU reference: each ``tile_size`` row normalised on its own, no affine."""
        cols = self.tile_size
        if cols is None:
            raise ValueError("LayerNorm.reference needs tile_size (resolve first)")
        rows = x.reshape(-1, cols).astype(np.float32)
        mean = rows.mean(axis=-1, keepdims=True)
        # The biased variance, which is what torch normalises by.
        var = ((rows - mean) ** 2).mean(axis=-1, keepdims=True)
        y = (rows - mean) / np.sqrt(var + 1e-5)
        return y.astype(x.dtype).reshape(x.shape)
