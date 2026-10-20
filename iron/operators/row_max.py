# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import In, Out
from aie.iron.kernels import reduce
from aie.utils.compile.jit.params import param

from iron.common import Rowwise
from iron.common.elementwise import CORES
from iron.common.testing import Case, Testing


class RowMax(Rowwise):
    """The largest element of each row of float32, one float32 a row."""

    test = Testing(
        [
            Case(dict(rows=64, width=128, num_aie_columns=1)),
            # Whisper's clip, 3000 frames of 128 mels as 96 rows, then their peaks.
            Case(dict(rows=96, width=4000, num_aie_columns=8)),
            Case(dict(rows=1, width=96, num_aie_columns=1), id="one_row"),
            Case(dict(rows=2048, width=4096, num_aie_columns=8), bench=True),
        ],
        draw=lambda op: dict(normal=(op.x,)),
    )

    width: int = param()
    tile_size: int = param(derive=lambda op: 1)

    x = In(
        Rowwise.rows,
        width,
        dtype=np.float32,
        obj_shape=(width,),
        per=CORES,
    )
    y = Out(
        Rowwise.rows,
        tile_size,
        dtype=np.float32,
        obj_shape=(tile_size,),
        per=CORES,
    )

    def validate(self) -> None:
        if self.width % 16:
            raise ValueError(
                f"RowMax: width ({self.width}) is not whole 16-lane vectors"
            )

    def ops(self) -> int:
        return self.rows * self.width

    def kernel(self):
        return reduce.reduce_max(self.width, dtype=np.float32)
