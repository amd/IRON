# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import In, Out
from aie.iron.kernels import eltwise
from aie.utils.compile.jit.params import param

from iron.common import Rowwise
from iron.common.elementwise import CORES
from iron.common.testing import Case, Testing


class Magnitude(Rowwise):
    """The magnitude of each row of complex float32 held as `[re | im]`, or
    with `power=2` its square, the power spectrum.
    """

    test = Testing(
        [
            Case(dict(rows=64, width=640, num_aie_columns=1)),
            Case(dict(rows=512, width=640, num_aie_columns=4)),
            Case(dict(rows=4096, width=640, num_aie_columns=8), bench=True),
            # Whisper's 201 bins, padded to 256.
            Case(dict(rows=64, width=512, num_aie_columns=1, power=2), lower=True),
            Case(dict(rows=3000, width=512, num_aie_columns=8, power=2), bench=True),
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

    width: int = param()
    power: int = param(default=1, array=True)
    tile_size: int = param(derive=lambda op: op.width // 2)

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
        if self.width % 2:
            raise ValueError(
                f"Magnitude: width ({self.width}) is not two halves, re and im"
            )
        if self.power not in (1, 2):
            raise ValueError(f"Magnitude: power ({self.power}) is not 1 or 2")

    def kernel(self):
        return eltwise.magnitude_f32(self.tile_size, power=self.power)
