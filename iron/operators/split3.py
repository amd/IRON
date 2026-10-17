# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# aie2's accumulator add drops bits below 24: `hi` is taken off in two halves.
SPLIT = """
#include <aie_api/aie.hpp>
#include <stdint.h>

using acc_t = aie::accum<accfloat, 32>;
using bf_t = aie::vector<bfloat16, 32>;

static inline bf_t bf_lanes(int16_t bits) {
    return aie::broadcast<int16_t, 32>(bits).cast_to<bfloat16>();
}

static inline void split3(acc_t a, bf_t &hi, bf_t &mid, bf_t &lo, bf_t one,
                          bf_t half) {
    hi = a.to_vector<bfloat16>();
    acc_t r = aie::msc(aie::msc(a, hi, half), hi, half);
    mid = r.to_vector<bfloat16>();
    lo = aie::msc(r, mid, one).to_vector<bfloat16>();
}
"""
