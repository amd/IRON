// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Convert int32 to bfloat16 with scalar scale multiplication.
// scale_tile contains 16 bfloat16 values; only the first is used (broadcast).
// out[i] = bf16(float(in[i]) * float(scale_tile[0]))
extern "C" {

void scale_i32_to_bf16(int32_t *restrict in, bfloat16 *restrict scale_tile, bfloat16 *restrict out, int32_t size)
{
    float scale_f32 = (float)scale_tile[0];
    aie::vector<float, 16> scale_vec = aie::broadcast<float, 16>(scale_f32);

    event0();
    for (int i = 0; i < size; i += 16) {
        aie::vector<int32_t, 16> i32_vec = aie::load_v<16>(in + i);
        aie::vector<float, 16> f32_vec = aie::to_float<float>(i32_vec, 0);
        aie::vector<float, 16> scaled = aie::mul(f32_vec, scale_vec);
        aie::accum<accfloat, 16> acc;
        acc.from_vector(scaled, 0);
        aie::store_v(out + i, acc.to_vector<bfloat16>());
    }
    event1();
}

} // extern "C"
