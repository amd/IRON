# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction, In, Out
from aie.iron.kernels import KernelContract, Param, eltwise
from aie.utils import config
from aie.utils.compile.jit.params import param
from aie.utils.verify import Tolerance

from iron.common import Rowwise
from iron.common.elementwise import CORES
from iron.common.testing import Case, Testing

POWER = """
#include "aie_kernel_utils.h"
#include "common/f32_split.h"
#include <aie_api/aie.hpp>
#include <stdint.h>

// re^2 + im^2 of complex float32 held as [re | im], POWER_ELEMS of each:
// magnitude_f32.cc's sum of limb products, smallest first, with the mid-lo
// products its square root does not need.
extern "C" void power_f32(float *restrict x, float *restrict out, int32_t n) {
  event0();
  aie::rounding_mode saved = aie::swap_rounding(aie::rounding_mode::conv_even);
  const bf16_vec one = bf16_splat(0x3f80);
  AIE_PREPARE_FOR_PIPELINING
  for (int i = 0; i < POWER_ELEMS; i += f32_lanes) {
    bf16_vec re_hi, re_mid, re_lo, im_hi, im_mid, im_lo;
    split3(f32_acc(aie::load_v<f32_lanes>(x + i)), re_hi, re_mid, re_lo, one);
    split3(f32_acc(aie::load_v<f32_lanes>(x + POWER_ELEMS + i)), im_hi, im_mid,
           im_lo, one);
    f32_acc p = aie::mul(re_mid, re_lo);
    p = aie::mac(p, re_mid, re_lo);
    p = aie::mac(aie::mac(p, im_mid, im_lo), im_mid, im_lo);
    p = aie::mac(p, re_mid, re_mid);
    p = aie::mac(p, im_mid, im_mid);
    p = aie::mac(aie::mac(p, re_hi, re_lo), re_hi, re_lo);
    p = aie::mac(aie::mac(p, im_hi, im_lo), im_hi, im_lo);
    p = aie::mac(aie::mac(p, re_hi, re_mid), re_hi, re_mid);
    p = aie::mac(aie::mac(p, im_hi, im_mid), im_hi, im_mid);
    p = aie::mac(aie::mac(p, re_hi, re_hi), im_hi, im_hi);
    aie::store_v(out + i, p.to_vector<float>());
  }
  aie::set_rounding(saved);
  event1();
}
"""


def power_ref(x):
    """`re^2 + im^2` of each call's two halves, in float64."""
    re, im = np.split(np.asarray(x, np.float64), 2, axis=-1)
    return re * re + im * im


def power_bound(x):
    """One float32 ulp from the correctly rounded power."""
    t = power_ref(x)
    r = t.astype(np.float32)
    return np.abs(t - r) + np.spacing(r).astype(np.float64)


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
        if self.power == 1:
            return eltwise.magnitude_f32(self.tile_size)
        return ExternalFunction(
            "power_f32",
            source_string=POWER,
            arg_types=[self.x.obj_type, self.y.obj_type, np.int32],
            include_dirs=[config.aie_kernels_dir()],
            compile_flags=[f"-DPOWER_ELEMS={self.tile_size}"],
            symbol_prefix=f"power_{self.tile_size}",
            contract=KernelContract(
                roles=(In, Out, Param),
                parameter_bindings=((2, self.tile_size),),
                reference=power_ref,
                tolerance=Tolerance.bounded(
                    power_bound,
                    note="one float32 ulp from correctly rounded; npu2 measured "
                    "1.18 ulps from the exact power over 6,144,000 results",
                ),
            ),
        )
