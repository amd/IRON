# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import eltwise

from iron.common import In, Out, Param, Rowwise
from iron.common.testing import Case, Testing


class Magnitude(Rowwise):
    """The magnitude of each row of complex float32 held as `[re | im]`."""

    test = Testing(
        [
            Case(dict(rows=64, width=640, num_aie_columns=1)),
            Case(dict(rows=512, width=640, num_aie_columns=4)),
            Case(dict(rows=4096, width=640, num_aie_columns=8), bench=True),
        ],
        # Spectra span many decades and pad with zero bins.
        draw=lambda op: dict(
            given={
                op.x: (
                    np.random.default_rng(42).standard_normal((op.rows, op.width))
                    * 10.0 ** np.random.default_rng(43).uniform(-8, 3, (op.rows, 1))
                    * (np.arange(op.width) % op.tile_size < op.tile_size - 32)
                ).astype(np.float32)
            }
        ),
    )

    width: int = Param()
    tile_size: int = Param(derive=lambda op: op.width // 2)

    x = In(
        Rowwise.rows,
        width,
        dtype=np.float32,
        obj_shape=(width,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    y = Out(
        Rowwise.rows,
        tile_size,
        dtype=np.float32,
        obj_shape=(tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        self.check_derived("tile_size")
        if self.width % 2:
            raise ValueError(
                f"Magnitude: width ({self.width}) is not two halves, re and im"
            )

    class Array(Rowwise.Array):
        def kernel(self):
            return eltwise.magnitude_f32(self.tile_size)
