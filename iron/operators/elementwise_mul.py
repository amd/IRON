# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwise, RowBroadcast


class ElementwiseMul(BinaryElementwise):
    """AIE-accelerated element-wise multiplication."""

    def kernel(self):
        return eltwise.mul_sized(self.tile_size)


class RowwiseMul(RowBroadcast):
    """Each row times one row, ``x * row``."""

    tile_cap: ClassVar[int] = 4096

    def kernel(self):
        return eltwise.mul_sized(self.line)
