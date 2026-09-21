# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar
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

    pass
