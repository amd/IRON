# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import field
from typing import ClassVar

from aie.iron.kernels import norm

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases


class LayerNorm(UnaryElementwise):
    """AIE-accelerated Layer Normalization operator."""

    test = Testing(channeled_unary_cases())

    # Hardware trace buffer size; 0 disables tracing.
    trace_size: int = field(default=0, repr=False, kw_only=True)

    tile_cap: ClassVar[int] = 8192

    def kernel(self, target):
        return norm.layer_norm(self.tile_size)
