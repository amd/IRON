# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import field
from typing import ClassVar

import torch
from aie.iron.kernels import norm

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases


@operator
class LayerNormOverlay(ChanneledUnaryOverlay):
    """The array for LayerNorm: the shared elementwise design over its kernel."""

    tile_cap: ClassVar[int] = 8192

    def kernel(self, target):
        return norm.layer_norm(self.line_size)


@operator
class LayerNorm(ChanneledUnaryOperator[LayerNormOverlay]):
    """AIE-accelerated Layer Normalization operator"""

    test = Testing(
        channeled_unary_cases([1024, 2048, 4096, 8192], 8192),
        rel_tol=0.1,
        abs_tol=0.1,
    )

    # Hardware trace buffer size; 0 disables tracing.
    trace_size: int = field(default=0, repr=False, kw_only=True)

    def reference(self, x):
        """CPU reference: each ``tile_size`` row normalised on its own, no affine."""
        cols = self.ov.tile_size
        if cols is None:
            raise ValueError("LayerNorm.reference needs tile_size (tune the overlay)")
        y = torch.nn.functional.layer_norm(
            x.reshape(-1, cols), normalized_shape=(cols,)
        )
        return y.reshape(x.shape)
