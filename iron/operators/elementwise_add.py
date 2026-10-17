# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import eltwise

from iron import operators as catalog
from iron.common import BinaryElementwise, Chain, In, Out, Rowwise
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
                        finish=Chain.of(catalog.SiLU(size=2048)),
                    ),
                    id="finish_SiLU",
                )
            ],
        ]
    )

    class Array(BinaryElementwise.Array):
        def kernel(self):
            return eltwise.add_sized(self.tile_size)


class RowwiseAdd(Rowwise):
    """Each row plus one row, ``x + row``: a projection's bias."""

    tile_cap: ClassVar[int] = 4096

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_type=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    row = In(
        Rowwise.tile_size,
        obj_type=(Rowwise.tile_size,),
        per=(Rowwise.num_channels,),
        replicate=True,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_type=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    class Array(Rowwise.Array):
        def kernel(self):
            return eltwise.add_sized(self.tile_size)
