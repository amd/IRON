# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from typing import ClassVar

import numpy as np
from aie.iron.kernels import datamovement

from iron.common import In, UnaryElementwise, Unresolvable, auto, param
from iron.common.testing import Testing, channeled_unary_cases


class Dequant(UnaryElementwise):
    """AIE-accelerated int4 -> bf16 dequantization: the elementwise design
    over a packed input.

    A core takes ``tile_size`` values as ``in_tile`` packed bytes (two 4-bit
    values per byte plus a bf16 scale per ``group_size``; no zero point) and
    produces ``tile_size`` bf16 values, so its two streams carry different
    tiles.
    """

    # The kernel's contract draws what it reads: packed int4 lines, each
    # followed by its scales.
    test = Testing(
        channeled_unary_cases(group_size=32),
        draw=lambda op: dict(
            x=datamovement.expand(op.tile_size, op.group_size)
            .contract.sample(np.random.default_rng(42), op.size // op.tile_size)[0]
            .reshape(-1)
        ),
    )

    group_size: int = param(default=32, repr=False, array=True)
    # The packed input's length: two 4-bit values per byte plus a bf16 scale
    # per group.
    packed: int = param(
        default=lambda op: op.size // 2 + (op.size // op.group_size) * 2, repr=False
    )
    # The packed size of one line; filled by resolve from ``tile_size``.
    in_tile: int = auto(repr=False)

    default_tile: ClassVar[int] = 4096
    tile_cap: ClassVar[int] = 16384

    x = In(
        packed,
        dtype=np.uint8,
        tile=(in_tile,),
        per=(UnaryElementwise.num_aie_columns, UnaryElementwise.num_channels),
    )

    def validate(self) -> None:
        self.check_derived("packed")
        if self.size % self.group_size:
            raise ValueError(
                f"size={self.size} is not whole groups of {self.group_size}"
            )

    def resolve(self, dev):
        op = super().resolve(dev)
        if op.tile_size % self.group_size:
            raise Unresolvable(
                f"tile_size={op.tile_size} is not whole groups of {self.group_size}"
            )
        packed = (op.tile_size // 2) + (op.tile_size // self.group_size) * 2
        return dataclasses.replace(op, in_tile=packed)

    def kernel(self):
        return datamovement.expand(self.tile_size, self.group_size)
