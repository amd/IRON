# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import activation

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases

# The shortest line mlir-aie's LUT activations take.
_LUT_LINE = 1024


class Tanh(UnaryElementwise):
    """AIE-accelerated Tanh activation function."""

    test = Testing(channeled_unary_cases(tile_floor=_LUT_LINE))

    default_tile: ClassVar[int] = _LUT_LINE

    def kernel(self, target):
        return activation.tanh(self.tile_size)
