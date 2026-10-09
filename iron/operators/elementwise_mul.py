# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwise, In, Out, Rowwise


class ElementwiseMul(BinaryElementwise):
    """AIE-accelerated element-wise multiplication."""

    def kernel(self):
        return eltwise.mul_sized(self.tile_size)


class RowwiseMul(Rowwise):
    """Each row times one row, ``x * row``: the row is a line every core
    holds for the call, one per channel shared by its columns.
    """

    # A core holds the row beside each line in and out.
    tile_cap: ClassVar[int] = 4096

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        tile=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    row = In(
        Rowwise.tile_size,
        tile=(Rowwise.tile_size,),
        per=(Rowwise.num_channels,),
        replicate=True,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        tile=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def kernel(self):
        return eltwise.mul_sized(self.tile_size)
