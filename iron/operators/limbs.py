# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit import markers
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, Rowwise, param
from iron.common.testing import Case, Testing

from .split3 import SPLIT

# The limbs of each plane, in order: against a second operand split
# [hi, hi, mid, hi, mid, lo], the six products a float32 product keeps.
PLANES = (0, 1, 0, 2, 1, 0)
WEIGHT_PLANES = (0, 0, 1, 0, 1, 2)

LIMBS = SPLIT + """
extern "C" void limbs_f32(float *restrict x, bfloat16 *restrict y, int32_t n) {
    event0();
    aie::rounding_mode saved = aie::swap_rounding(aie::rounding_mode::conv_even);
    const bf_t one = bf_lanes(0x3f80);
    for (int i = 0; i < n; i += 32) chess_prepare_for_pipelining {
        bf_t hi, mid, lo;
        split3(acc_t(aie::load_v<32>(x + i)), hi, mid, lo, one);
        aie::store_v(y + i, hi);
        aie::store_v(y + n + i, mid);
        aie::store_v(y + 2 * n + i, hi);
        aie::store_v(y + 3 * n + i, lo);
        aie::store_v(y + 4 * n + i, mid);
        aie::store_v(y + 5 * n + i, hi);
    }
    aie::set_rounding(saved);
    event1();
}
"""


def split(x):
    """The bf16 limbs `hi`, `mid` and `lo` of `x`, each rounded to nearest
    even from the residual of those before it: they sum to a float32 `x`
    exactly, and to a float64 one to about float32's precision.
    """
    x = np.asarray(x)
    x = x if x.dtype == np.float64 else x.astype(np.float32)
    hi = x.astype(bfloat16)
    r = x - hi.astype(x.dtype)
    mid = r.astype(bfloat16)
    lo = (r - mid.astype(x.dtype)).astype(bfloat16)
    return hi, mid, lo


def planes(x):
    """Rows of `x` as the six planes `Limbs` writes, `(rows, 6 * line)`."""
    limbs = split(x)
    return np.concatenate([limbs[p] for p in PLANES], axis=-1)


def stacked(w):
    """The `(6 * K, N)` operand a GEMM by `Limbs`' planes takes for `w`
    `(K, N)`: its limbs stacked `[hi, hi, mid, hi, mid, lo]`.
    """
    limbs = split(w)
    return np.concatenate([limbs[p] for p in WEIGHT_PLANES])


class Limbs(Rowwise):
    """Each row of float32 as six planes of its bf16 limbs, `[hi, mid, hi,
    lo, mid, hi]`: a GEMM of them against a second operand split `[hi, hi,
    mid, hi, mid, lo]` is a float32 product to within the three smallest of
    its nine limb products.
    """

    test = Testing(
        [
            Case(dict(rows=64, line=160, num_aie_columns=1)),
            Case(dict(rows=512, line=320, num_aie_columns=4)),
            Case(dict(rows=4096, line=320, num_aie_columns=8), bench=True),
        ],
        draw=dict(normal=("x",)),
    )

    line: int = param()
    tile_size: int = param(default=lambda op: len(PLANES) * op.line)

    x = In(
        Rowwise.rows,
        line,
        dtype=np.float32,
        tile=(line,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        self.check_derived("tile_size")
        if self.line % 32:
            raise ValueError(
                f"Limbs: line ({self.line}) is not a whole number of 32-element "
                f"vectors"
            )

    def kernel(self):
        contract = KernelContract(
            roles=(markers.In, markers.Out, Param),
            parameter_bindings=((2, self.line),),
            reference=planes,
            tolerance=Tolerance.exact(
                note="each residual is exact, and so is each limb of it"
            ),
        )
        return ExternalFunction(
            "limbs_f32",
            source_string=LIMBS,
            arg_types=[self.x.tile, self.y.tile, np.int32],
            contract=contract,
        )
