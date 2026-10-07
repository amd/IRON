# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit import markers
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, UnaryElementwise, param
from iron.common.testing import Sweep, Testing

from .limbs import SPLIT

# log(m) for m in [sqrt(1/2), sqrt(2)) is f q(f), f = m - 1, with q
# log1p(f) / f interpolated at Chebyshev nodes: 7.5e-9 off in float32.
DEGREE = 9
LOW, HIGH = np.sqrt(0.5) - 1, np.sqrt(2.0) - 1
NODES = (LOW + HIGH) / 2 + (HIGH - LOW) / 2 * np.cos(
    (2 * np.arange(DEGREE + 1) + 1) * np.pi / (2 * DEGREE + 2)
)
COEFFICIENTS = np.polynomial.polynomial.polyfit(
    NODES, np.log1p(NODES) / NODES, DEGREE
).astype(np.float32)
LN2 = np.float64(np.log(2))
LN2_HI = LN2.astype(bfloat16)
LN2_MID = (LN2 - np.float64(LN2_HI)).astype(bfloat16)
LN2_LO = (LN2 - np.float64(LN2_HI) - np.float64(LN2_MID)).astype(bfloat16)

LOG = SPLIT + f"""
static const float C[{DEGREE + 1}] = {{{", ".join(f"{float(c)!r}f" for c in COEFFICIENTS)}}};

extern "C" void log_f32_bf16(float *restrict x, bfloat16 *restrict y, int32_t n,
                             float offset) {{
    event0();
    aie::rounding_mode saved = aie::swap_rounding(aie::rounding_mode::conv_even);
    const bf_t one = bf_lanes(0x3f80);
    const bf_t ln2_hi = bf_lanes({int(LN2_HI.view(np.int16))});
    const bf_t ln2_mid = bf_lanes({int(LN2_MID.view(np.int16))});
    const bf_t ln2_lo = bf_lanes({int(LN2_LO.view(np.int16))});
    for (int i = 0; i < n; i += 32) chess_prepare_for_pipelining {{
        auto bits = aie::add(acc_t(aie::load_v<32>(x + i)), offset)
                        .to_vector<float>()
                        .cast_to<int32_t>();
        // z = 2^e m with m in [sqrt(1/2), sqrt(2)).
        auto e = aie::downshift(
            aie::sub(bits, aie::broadcast<int32_t, 32>(0x3f3504f3)), 23);
        auto m = aie::sub(bits, aie::upshift(e, 23)).cast_to<float>();
        auto e_magic = aie::add(e, aie::broadcast<int32_t, 32>(0x4b400000));
        bf_t ef = aie::add(acc_t(e_magic.cast_to<float>()), -12582912.0f)
                      .to_vector<bfloat16>();
        bf_t fh, fm, fl;
        split3(aie::msc(acc_t(m), one, one), fh, fm, fl, one);

        acc_t q = aie::add(acc_t(aie::broadcast<float, 32>(0.0f)), C[{DEGREE}]);
        for (int k = {DEGREE - 1}; k >= 0; k--) {{
            bf_t qh, qm, ql;
            split3(q, qh, qm, ql, one);
            q = aie::mul(ql, fh);
            q = aie::mac(aie::mac(q, qm, fm), qh, fl);
            q = aie::mac(aie::mac(q, qm, fh), qh, fm);
            q = aie::add(aie::mac(q, qh, fh), C[k]);
        }}
        bf_t qh, qm, ql;
        split3(q, qh, qm, ql, one);
        acc_t r = aie::mul(ef, ln2_lo);
        r = aie::mac(r, ef, ln2_mid);
        r = aie::mac(aie::mac(aie::mac(r, ql, fh), qm, fm), qh, fl);
        r = aie::mac(aie::mac(aie::mac(r, qm, fh), qh, fm), qh, fh);
        aie::store_v(y + i, aie::mac(r, ef, ln2_hi).to_vector<bfloat16>());
    }}
    aie::set_rounding(saved);
    event1();
}}
"""


def log(x, offset):
    """`log(x + offset)`, the offset as the kernel holds it, in float64."""
    return np.log(np.asarray(x, np.float64) + np.float64(np.float32(offset)))


class Log(UnaryElementwise):
    """`log(x + offset)` of float32, rounded once to bf16."""

    test = Testing(
        Sweep(),
        # Mel energies: positive, over eleven decades.
        draw=lambda op: dict(
            x=(10.0 ** np.random.default_rng(42).uniform(-6, 5, op.size)).astype(
                np.float32
            )
        ),
    )

    offset: float = param(default=0.0, array=True)

    x = In(
        UnaryElementwise.size,
        dtype=np.float32,
        tile=(UnaryElementwise.tile_size,),
        per=(UnaryElementwise.num_aie_columns, UnaryElementwise.num_channels),
    )

    def kernel(self):
        contract = KernelContract(
            roles=(markers.In, markers.Out, Param, Param),
            parameter_bindings=((2, self.tile_size),),
            reference=log,
            tolerance=Tolerance.bf16_ulps(
                1, note="float32 to 7.5e-9, then rounded once to bf16"
            ),
        )
        return ExternalFunction(
            "log_f32_bf16",
            source_string=LOG,
            arg_types=[self.x.tile, self.y.tile, np.int32, np.float32],
            contract=contract,
        )

    def scalars(self) -> tuple:
        return (self.offset,)
