# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction, In, Out
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit.params import param
from aie.utils.verify import Tolerance

from iron.common import Rowwise
from iron.common.elementwise import CORES
from iron.common.testing import Case, Testing

ROW_MAX = """
#include <aie_api/aie.hpp>
#include <stdint.h>

extern "C" void row_max_f32(float *restrict x, float *restrict y, int32_t n) {
  event0();
  aie::vector<float, 16> m = aie::load_v<16>(x);
  for (int32_t i = 16; i < ROW_MAX_ELEMS; i += 16) chess_prepare_for_pipelining {
    m = aie::max(m, aie::load_v<16>(x + i));
  }
  *y = aie::reduce_max(m);
  event1();
}
"""


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
        return ExternalFunction(
            "row_max_f32",
            source_string=ROW_MAX,
            arg_types=[self.x.obj_type, self.y.obj_type, np.int32],
            compile_flags=[f"-DROW_MAX_ELEMS={self.width}"],
            symbol_prefix=f"row_max_{self.width}",
            contract=KernelContract(
                roles=(In, Out, Param),
                parameter_bindings=((2, self.width),),
                reference=lambda x: np.max(x, axis=-1, keepdims=True),
                tolerance=Tolerance.exact(note="a selection"),
            ),
        )
