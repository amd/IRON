# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction, In, Out
from aie.iron.kernels import KernelContract, Param
from aie.utils import config
from aie.utils.compile.jit.params import param
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import UnaryElementwise
from iron.common.elementwise import CORES, Elementwise, Sweep
from iron.common.testing import Case, Testing

LOG10_CLAMP = """
#include "aie_kernel_utils.h"
#include "common/f32_split.h"
#include <aie_api/aie.hpp>
#include <stdint.h>

using f32_vec = aie::vector<float, f32_lanes>;

// log_f32.cc's log(m) for m in [sqrt(1/2), sqrt(2)): f q(f), f = m - 1.
static const float log_q[10] = {1.0f,
                                -0.49999988079071045f,
                                0.33333346247673035f,
                                -0.2500157952308655f,
                                0.20000939071178436f,
                                -0.1660836935043335f,
                                0.14199650287628174f,
                                -0.13266031444072723f,
                                0.12806610763072968f,
                                -0.07451186329126358f};

// log10(z) for z a positive normal float32: log_f32.cc's log, kept in the
// accumulator rather than rounded to bf16, times 1 / ln 10 on limbs.
static inline __attribute__((always_inline)) f32_vec
log10_f32(f32_vec z, const Limbs<f32_lanes> &inv_ln10) {
  const bf16_vec one = bf16_splat(0x3f80);
  const bf16_vec ln2_hi = bf16_splat(0x3f31);
  const bf16_vec ln2_mid = bf16_splat(0x3ae4);
  const bf16_vec ln2_lo = bf16_splat(0x35c0);
  auto bits = z.cast_to<int32_t>();
  auto e = aie::downshift(
      aie::sub(bits, aie::broadcast<int32_t, f32_lanes>(0x3f3504f3)), 23);
  auto m = aie::sub(bits, aie::upshift(e, 23)).cast_to<float>();
  auto e_magic = aie::add(e, aie::broadcast<int32_t, f32_lanes>(0x4b400000));
  bf16_vec ef = aie::add(f32_acc(e_magic.cast_to<float>()), -12582912.0f)
                    .to_vector<bfloat16>();
  bf16_vec fh, fm, fl;
#if AIE_ARCH_AIE2
  const bf16_vec half = bf16_splat(0x3f00);
  f32_acc f = aie::msc(aie::msc(f32_acc(m), one, half), one, half);
#else
  f32_acc f = aie::msc(f32_acc(m), one, one);
#endif
  split3(f, fh, fm, fl, one);
  f32_acc q =
      aie::add(f32_acc(aie::broadcast<float, f32_lanes>(0.0f)), log_q[9]);
  for (int k = 8; k >= 0; k--) {
    bf16_vec qh, qm, ql;
    split3(q, qh, qm, ql, one);
    q = aie::mul(ql, fh);
    q = aie::mac(aie::mac(q, qm, fm), qh, fl);
    q = aie::mac(aie::mac(q, qm, fh), qh, fm);
    q = aie::add(aie::mac(q, qh, fh), log_q[k]);
  }
  bf16_vec qh, qm, ql;
  split3(q, qh, qm, ql, one);
  f32_acc r = aie::mul(ef, ln2_lo);
  r = aie::mac(r, ef, ln2_mid);
  r = aie::mac(aie::mac(aie::mac(r, ql, fh), qm, fm), qh, fl);
  r = aie::mac(aie::mac(aie::mac(r, qm, fh), qh, fm), qh, fh);
  r = aie::mac(r, ef, ln2_hi);
  return mul_limbs(bf16_limbs(r), inv_ln10).to_vector<float>();
}

extern "C" void log10_clamp(float *restrict x, float *restrict peak,
                            bfloat16 *restrict y, int32_t n, float floor_,
                            float decades, float shift, float scale) {
  event0();
  aie::rounding_mode saved = aie::swap_rounding(aie::rounding_mode::conv_even);
  const Limbs<f32_lanes> inv_ln10 =
      bf16_limbs(f32_acc(aie::broadcast<float, f32_lanes>(0.43429448190325176f)));
  const Limbs<f32_lanes> s =
      bf16_limbs(f32_acc(aie::broadcast<float, f32_lanes>(scale)));
  const f32_vec lo = aie::broadcast<float, f32_lanes>(floor_);
  const f32_vec top =
      log10_f32(aie::max(aie::broadcast<float, f32_lanes>(*peak), lo), inv_ln10);
  const f32_vec least = aie::add(f32_acc(top), -decades).to_vector<float>();
  for (int i = 0; i < LOG10_ELEMS; i += f32_lanes) {
    f32_vec v = aie::max(
        log10_f32(aie::max(aie::load_v<f32_lanes>(x + i), lo), inv_ln10), least);
    aie::store_v(y + i, mul_limbs(bf16_limbs(aie::add(f32_acc(v), shift)), s)
                            .to_vector<bfloat16>());
  }
  aie::set_rounding(saved);
  event1();
}
"""


def clamped(x, peak, floor, decades):
    """Each `log10(max(x, floor))` held to `decades` below `peak`'s: in
    float32, as Whisper's extractor takes it, and in float64.
    """
    lo = np.float32(floor)
    top = np.log10(np.maximum(np.asarray(peak, np.float32)[..., :1], lo))
    log = np.log10(np.maximum(np.asarray(x, np.float32), lo).astype(np.float64))
    return (
        np.maximum(
            log.astype(np.float32), top.astype(np.float32) - np.float32(decades)
        ),
        np.maximum(log, top - decades),
    )


def reference(x, peak, floor, decades, shift, scale):
    """Whisper's float32 steps after the log, rounded once to bf16."""
    v, _ = clamped(x, peak, floor, decades)
    return ((v + np.float32(shift)) * np.float32(scale)).astype(bfloat16)


def bound(x, peak, floor=1e-10, decades=8.0, shift=4.0, scale=0.25):
    """None, except where the exact result is within `gap` of a bf16
    rounding midpoint: there one bf16 ulp plus `gap`, 16 float32 ulps of the
    clamped log and the shift, how far the kernel's float32 steps and the
    reference's may lie apart (most where `y + shift` cancels).
    """
    _, v = clamped(x, peak, floor, decades)
    t = (v + shift) * scale
    b = t.astype(bfloat16).astype(np.float64)
    ulp = np.exp2(np.floor(np.log2(np.maximum(np.abs(b), 2.0**-126))) - 7)
    gap = 2.0**-20 * (np.abs(v) + abs(shift)) * abs(scale)
    return np.where(np.abs(np.abs(t - b) - ulp / 2) <= gap, ulp + gap, 0.0)


def draw(op):
    """Mel energies over seventeen decades, an eighth of them zero, and
    their largest as the peak.
    """
    rng = np.random.default_rng(42)
    x = 10.0 ** rng.uniform(-14, 3, op.size) * (rng.uniform(size=op.size) >= 0.125)
    x = x.astype(np.float32)
    return dict(given={op.x: x, op.peak: x.max(keepdims=True)})


class Log10Clamp(UnaryElementwise):
    """`log10(max(x, floor))` of float32 held to `decades` below that of
    `peak`, then `(y + shift) * scale`, rounded once to bf16: Whisper's
    log-mel features from mel energies and the clip's largest.
    """

    test = Testing(
        [
            Sweep(),
            # Whisper's clip: 3000 frames of 128 mels.
            Case(dict(size=384000, num_aie_columns=8, tile_size=1600), id="whisper"),
        ],
        draw=draw,
    )

    floor: float = param(default=1e-10, array=True)
    decades: float = param(default=8.0, array=True)
    shift: float = param(default=4.0, array=True)
    scale: float = param(default=0.25, array=True)

    x = In(
        UnaryElementwise.size,
        dtype=np.float32,
        obj_shape=(UnaryElementwise.tile_size,),
        per=CORES,
    )
    # One float32 every core holds for the call.
    peak = In(
        1,
        dtype=np.float32,
        obj_shape=(1,),
        per=(Elementwise.num_channels,),
        replicate=True,
    )
    y = Out(
        UnaryElementwise.size,
        obj_shape=(UnaryElementwise.tile_size,),
        per=CORES,
    )

    def compatible(self) -> None:
        super().compatible()
        if self.tile_size % 32:
            raise ValueError(
                f"Log10Clamp: tile_size ({self.tile_size}) is not whole 32-lane "
                f"vectors"
            )

    def kernel(self):
        return ExternalFunction(
            "log10_clamp",
            source_string=LOG10_CLAMP,
            arg_types=[
                self.x.obj_type,
                self.peak.obj_type,
                self.y.obj_type,
                np.int32,
                np.float32,
                np.float32,
                np.float32,
                np.float32,
            ],
            include_dirs=[config.aie_kernels_dir()],
            compile_flags=[f"-DLOG10_ELEMS={self.tile_size}"],
            symbol_prefix=f"log10_clamp_{self.tile_size}",
            contract=KernelContract(
                roles=(In, In, Out, Param, Param, Param, Param, Param),
                parameter_bindings=((3, self.tile_size),),
                reference=reference,
                tolerance=Tolerance.bounded(
                    bound,
                    note="Whisper's float32 steps, rounded once; a near tie may "
                    "round either way: 323 of 8,388,608 results on npu2",
                ),
            ),
        )

    def scalars(self) -> tuple:
        return (self.floor, self.decades, self.shift, self.scale)
