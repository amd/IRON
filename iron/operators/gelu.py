# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import activation

from iron.common import UnaryElementwise
from iron.common.testing import Testing, channeled_unary_cases


class GELU(UnaryElementwise):
    """AIE-accelerated GELU activation function."""

    test = Testing(channeled_unary_cases())

    tile_cap: ClassVar[int] = 8192

    def kernel(self, target):
        return activation.gelu_sized(self.tile_size)
