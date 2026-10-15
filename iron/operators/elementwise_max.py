# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit import markers
from aie.utils.verify import Tolerance

from iron.common import BinaryElementwise, Operand
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing

MAX = """
#include <aie_api/aie.hpp>
#include <stdint.h>

extern "C" void eltwise_max_bf16(bfloat16 *restrict a, bfloat16 *restrict b,
                                 bfloat16 *restrict c, int32_t n) {
    event0();
    const int32_t whole = n / 32 * 32;
    for (int32_t i = 0; i < whole; i += 32) chess_prepare_for_pipelining {
        aie::store_v(c + i, aie::max(aie::load_v<32>(a + i), aie::load_v<32>(b + i)));
    }
    for (int32_t i = whole; i < n; i++) {
        c[i] = a[i] < b[i] ? b[i] : a[i];
    }
    event1();
}
"""


class ElementwiseMax(BinaryElementwise):
    """AIE-accelerated element-wise maximum."""

    # A line of 48, a whole vector and a scalar tail.
    test = Testing(
        [
            Sweep(channels=None),
            Case(dict(size=48 * 64, num_aie_columns=1, tile_size=48), id="tail"),
        ]
    )

    class Array(BinaryElementwise.Array):
        a: Operand
        b: Operand
        y: Operand

        def kernel(self):
            return ExternalFunction(
                "eltwise_max_bf16",
                source_string=MAX,
                arg_types=[self.a.obj_type, self.b.obj_type, self.y.obj_type, np.int32],
                contract=KernelContract(
                    roles=(markers.In, markers.In, markers.Out, Param),
                    parameter_bindings=((3, self.tile_size),),
                    reference=np.maximum,
                    tolerance=Tolerance.exact(note="a selection"),
                ),
            )
