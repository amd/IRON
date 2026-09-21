# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import torch
from dataclasses import field

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator


@operator
class LayerNormOverlay(ChanneledUnaryOverlay):
    """The array for LayerNorm: the shared channeled-unary design over its kernel."""

    kernel_name: ClassVar[str] = "layer_norm"
    kernel_fn_name: ClassVar[str] = "layer_norm"
    tile_cap: ClassVar[int] = 8192


@operator
class LayerNorm(ChanneledUnaryOperator[LayerNormOverlay]):
    """AIE-accelerated Layer Normalization operator"""

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
