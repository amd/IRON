# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwise, RowBroadcast


class ElementwiseAdd(BinaryElementwise):
    """AIE-accelerated element-wise addition."""

    def kernel(self):
        return eltwise.add_sized(self.tile_size)


class RowwiseAdd(RowBroadcast):
    """Each row plus one row, ``x + row``: a projection's bias."""

    tile_cap: ClassVar[int] = 4096

    def kernel(self):
        return eltwise.add_sized(self.line)
