# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import activation

from iron.common import In, Param, UnaryElementwise
from iron.common.elementwise import Sweep
from iron.common.testing import Testing


class Log(UnaryElementwise):
    """`log(x + offset)` of float32, rounded once to bf16."""

    test = Testing(
        Sweep(),
        # Mel energies: positive, over eleven decades.
        draw=lambda op: dict(
            given={
                op.x: (
                    10.0 ** np.random.default_rng(42).uniform(-6, 5, op.size)
                ).astype(np.float32)
            }
        ),
    )

    offset: float = Param(default=0.0)

    x = In(
        UnaryElementwise.size,
        dtype=np.float32,
        obj_type=(UnaryElementwise.tile_size,),
        per=(UnaryElementwise.num_aie_columns, UnaryElementwise.num_channels),
    )

    class Array(UnaryElementwise.Array):
        offset: float

        def kernel(self):
            return activation.log_f32(self.tile_size)

        def scalars(self) -> tuple:
            return (self.offset,)
