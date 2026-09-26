# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import field
from typing import ClassVar

from aie.iron.kernels import norm

import numpy as np

from aie.utils.verify import Tolerance

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.declare import dim
from iron.common.testing import Testing, channeled_unary_cases


@operator
class LayerNormOverlay(ChanneledUnaryOverlay):
    """The array for LayerNorm: the shared elementwise design over its kernel.

    ``tile_size`` is the row a core normalises, so it decides what the
    operator computes rather than how fast: a dimension here, not the
    tunable the template declares, and at most one line long.
    """

    tile_size: int = dim()
    tile_cap: ClassVar[int] = 8192

    def validate(self) -> None:
        super().validate()
        if self.tile_size > self.tile_cap:
            raise ValueError(
                f"tile_size={self.tile_size}: a LayerNorm row longer than the "
                f"{self.tile_cap}-element line a core holds would be normalised "
                f"in pieces"
            )

    def kernel(self, target):
        return norm.layer_norm(self.line_size)


@operator
class LayerNorm(ChanneledUnaryOperator[LayerNormOverlay]):
    """AIE-accelerated Layer Normalization operator"""

    test = Testing(
        channeled_unary_cases([1024, 2048, 4096, 8192], 8192),
        tolerance=Tolerance.relative(0.1, 0.05),
    )

    # Hardware trace buffer size; 0 disables tracing.
    trace_size: int = field(default=0, repr=False, kw_only=True)

    def reference(self, x):
        """CPU reference: each ``tile_size`` row normalised on its own, no affine."""
        rows = x.reshape(-1, self.ov.tile_size).astype(np.float32)
        mean = rows.mean(axis=-1, keepdims=True)
        # The biased variance, which is what torch normalises by.
        var = ((rows - mean) ** 2).mean(axis=-1, keepdims=True)
        y = (rows - mean) / np.sqrt(var + 1e-5)
        return y.astype(x.dtype).reshape(x.shape)
