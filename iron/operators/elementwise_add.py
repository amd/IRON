# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import eltwise

from iron import operators as catalog
from iron.common import BinaryElementwise, Chain, In, Link, Out, Rowwise
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class ElementwiseAdd(BinaryElementwise):
    """AIE-accelerated element-wise addition."""

    # A sum finished by silu in its own cores.
    test = Testing(
        [
            Sweep(channels=None),
            lambda cls, dev: [
                Case(
                    dict(
                        size=2048,
                        num_aie_columns=4,
                        finish=Chain((Link(catalog.SiLU(size=2048)),)),
                    ),
                    id="finish_SiLU",
                )
            ],
        ]
    )

    def kernel(self):
        return eltwise.add_sized(self.tile_size)


class RowwiseAdd(Rowwise):
    """Each row plus one row, ``x + row``: the row is a line every core
    holds for the call, one per channel shared by its columns. A linear
    projection's bias, added once per output column across every row.
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
        return eltwise.add_sized(self.tile_size)
