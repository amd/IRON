# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import datamovement

from iron.common import In, Param, Rowwise
from iron.common.testing import Case, Testing

# The planes of a stacked weight, as limbs_f32_split's (hi, mid, lo) indices,
# against the six planes datamovement.limbs_f32 writes of an activation.
WEIGHT_PLANES = (0, 0, 1, 0, 1, 2)


def stacked(w):
    """`w` `(K, N)` as its limbs stacked `[hi, hi, mid, hi, mid, lo]`."""
    limbs = datamovement.limbs_f32_split(w)
    return np.concatenate([limbs[p] for p in WEIGHT_PLANES])


class Limbs(Rowwise):
    """Each row of float32 as six planes of its bf16 limbs, `[hi, mid, hi,
    lo, mid, hi]`, for a float32 product by GEMM.
    """

    test = Testing(
        [
            Case(dict(rows=64, line=160, num_aie_columns=1)),
            Case(dict(rows=512, line=320, num_aie_columns=4)),
            Case(dict(rows=4096, line=320, num_aie_columns=8), bench=True),
        ],
        draw=lambda op: dict(normal=(op.x,)),
    )

    line: int = Param()
    tile_size: int = Param(derive=lambda op: 6 * op.line)

    x = In(
        Rowwise.rows,
        line,
        dtype=np.float32,
        obj_type=(line,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        self.check_derived("tile_size")

    class Array(Rowwise.Array):
        def kernel(self):
            return datamovement.limbs_f32(self.line)
