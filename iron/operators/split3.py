# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# Three bf16 limbs summing to `a` exactly: each residual is taken in the
# accumulator, where a bf16 times one is exact.
SPLIT = """
#include <aie_api/aie.hpp>
#include <stdint.h>

using acc_t = aie::accum<accfloat, 32>;
using bf_t = aie::vector<bfloat16, 32>;

static inline bf_t bf_lanes(int16_t bits) {
    return aie::broadcast<int16_t, 32>(bits).cast_to<bfloat16>();
}

static inline void split3(acc_t a, bf_t &hi, bf_t &mid, bf_t &lo, bf_t one) {
    hi = a.to_vector<bfloat16>();
    acc_t r = aie::msc(a, hi, one);
    mid = r.to_vector<bfloat16>();
    lo = aie::msc(r, mid, one).to_vector<bfloat16>();
}
"""
