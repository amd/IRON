# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit import markers
from aie.utils.verify import Tolerance

from iron.common import BinaryElementwise

MAX_CC = """
extern "C" void eltwise_max_bf16(bfloat16 *restrict a, bfloat16 *restrict b,
                                 bfloat16 *restrict c, int32_t n) {
    event0();
    for (int32_t i = 0; i < n; i++) {
        c[i] = a[i] > b[i] ? a[i] : b[i];
    }
    event1();
}
"""


def _max_ref(a, b):
    return np.maximum(a, b)


class ElementwiseMax(BinaryElementwise):
    """AIE-accelerated element-wise maximum of two tiles: ``max-pool``'s own
    running max of the kernel's ``k * k`` shifted, channels-last views, each
    a plain contiguous row (no per-channel gather, which a channels-last
    layout cannot express as an aligned DMA -- see ``MaxPool2d``).
    """

    def kernel(self):
        return ExternalFunction(
            "eltwise_max_bf16",
            source_string=MAX_CC,
            arg_types=[self.a.tile, self.b.tile, self.y.tile, np.int32],
            contract=KernelContract(
                roles=(markers.In, markers.In, markers.Out, Param),
                parameter_bindings=((3, self.tile_size),),
                reference=_max_ref,
                tolerance=Tolerance.exact(note="a selection, not an arithmetic op"),
            ),
        )
