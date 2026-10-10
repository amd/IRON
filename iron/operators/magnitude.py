# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit import markers
from aie.utils.verify import Tolerance

from iron.common import In, Out, Rowwise, param
from iron.common.testing import Case, Testing

from .split3 import SPLIT

# aie2p has no float32 vector multiply: every product here is of bf16 limbs,
# exact in the float32 accumulator.
MAGNITUDE = SPLIT + """
extern "C" void magnitude_f32(float *restrict x, float *restrict out, int32_t n) {
    event0();
    aie::rounding_mode saved = aie::swap_rounding(aie::rounding_mode::conv_even);
    const bf_t one = bf_lanes(0x3f80);
    const bf_t half = bf_lanes(0x3f00);
    for (int i = 0; i < n; i += 32) chess_prepare_for_pipelining {
        bf_t rh, rm, rl, ih, im, il;
        split3(acc_t(aie::load_v<32>(x + i)), rh, rm, rl, one);
        split3(acc_t(aie::load_v<32>(x + n + i)), ih, im, il, one);
        acc_t p = aie::mul(rm, rm);
        p = aie::mac(p, im, im);
        p = aie::mac(aie::mac(p, rh, rl), rh, rl);
        p = aie::mac(aie::mac(p, ih, il), ih, il);
        p = aie::mac(aie::mac(p, rh, rm), rh, rm);
        p = aie::mac(aie::mac(p, ih, im), ih, im);
        p = aie::mac(aie::mac(p, rh, rh), ih, ih);

        // 1 / sqrt(p): the bit-trick estimate, 3.4e-2 off, then a Newton
        // step to about 4e-3. p = 0 gives a finite estimate, and s = 0.
        auto bits = p.to_vector<float>().cast_to<int32_t>();
        auto y0_bits = aie::sub(aie::broadcast<int32_t, 32>(0x5f3759df),
                                aie::downshift(bits, 1));
        bf_t y0 = acc_t(y0_bits.cast_to<float>()).to_vector<bfloat16>();
        bf_t ph, pm, pl;
        split3(p, ph, pm, pl, one);
        bf_t py = aie::mac(aie::mul(pm, y0), ph, y0).to_vector<bfloat16>();
        acc_t r = aie::msc(acc_t(aie::broadcast<float, 32>(1.0f)), py, y0);
        bf_t y0_half = aie::mul(y0, half).to_vector<bfloat16>();
        bf_t y = aie::mac(aie::mul(y0, one), r.to_vector<bfloat16>(), y0_half)
                     .to_vector<bfloat16>();
        bf_t y_half = aie::mul(y, half).to_vector<bfloat16>();

        // s = p y, then s += y / 2 (p - s^2): each step multiplies the error
        // by y's, and p - s^2 is taken from s's exact limb products.
        acc_t s = aie::mac(aie::mac(aie::mul(pl, y), pm, y), ph, y);
        for (int k = 0; k < 3; k++) {
            bf_t sh, sm, sl;
            split3(s, sh, sm, sl, one);
            acc_t e = aie::msc(p, sh, sh);
            e = aie::msc(aie::msc(e, sh, sm), sh, sm);
            e = aie::msc(aie::msc(e, sh, sl), sh, sl);
            e = aie::msc(e, sm, sm);
            bf_t eh = e.to_vector<bfloat16>();
            bf_t em = aie::msc(e, eh, one).to_vector<bfloat16>();
            s = aie::mac(aie::mac(s, em, y_half), eh, y_half);
        }
        aie::store_v(out + i, s.to_vector<float>());
    }
    aie::set_rounding(saved);
    event1();
}
"""


def magnitude(x):
    """`sqrt(re^2 + im^2)` of rows `[re | im]`, in float64."""
    re, im = np.split(np.asarray(x, np.float64), 2, axis=-1)
    return np.hypot(re, im)


class Magnitude(Rowwise):
    """The magnitude of each row of complex float32, held as `[re | im]`:
    a row of `width` floats in, `width / 2` out.
    """

    test = Testing(
        [
            Case(dict(rows=64, width=640, num_aie_columns=1)),
            Case(dict(rows=512, width=640, num_aie_columns=4)),
            Case(dict(rows=4096, width=640, num_aie_columns=8), bench=True),
        ],
        # Spectra span many decades and pad with zero bins.
        draw=lambda op: dict(
            x=(
                np.random.default_rng(42).standard_normal((op.rows, op.width))
                * 10.0 ** np.random.default_rng(43).uniform(-8, 3, (op.rows, 1))
                * (np.arange(op.width) % op.tile_size < op.tile_size - 32)
            ).astype(np.float32)
        ),
    )

    width: int = param()
    tile_size: int = param(default=lambda op: op.width // 2)

    x = In(
        Rowwise.rows,
        width,
        dtype=np.float32,
        tile=(width,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    y = Out(
        Rowwise.rows,
        tile_size,
        dtype=np.float32,
        tile=(tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        self.check_derived("tile_size")
        if self.width % 64:
            raise ValueError(
                f"Magnitude: width ({self.width}) is not two halves of whole "
                f"32-element vectors"
            )

    def kernel(self):
        contract = KernelContract(
            roles=(markers.In, markers.Out, Param),
            parameter_bindings=((2, self.tile_size),),
            reference=magnitude,
            tolerance=Tolerance.relative(
                2e-7, note="measured 1.43e-7 for magnitudes 1e-15 to 1e15"
            ),
        )
        return ExternalFunction(
            "magnitude_f32",
            source_string=MAGNITUDE,
            arg_types=[self.x.tile, self.y.tile, np.int32],
            contract=contract,
        )
