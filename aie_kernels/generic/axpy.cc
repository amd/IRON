// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#define NOCPP

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define REL_WRITE 0
#define REL_READ 1

#include <aie_api/aie.hpp>

extern "C" {
// AXPY FIX PLAN 2026-03-20: Kernel optimization for small tile sizes
// Addresses: axpy_8_cols_2_channels_2048_tile_256_3.0 (-16.19% bandwidth)
// The fixed vector size of 64 is optimal for AIE architecture.
// Added loop unroll hint to reduce loop overhead for small tiles (256 elements = 4 iterations)
void saxpy(bfloat16 *restrict x, bfloat16 *restrict y, const float a, bfloat16 *restrict z, const int32_t vector_size)
{
    event0();
    ::aie::vector<bfloat16, 64> a_v =
        ::aie::broadcast<bfloat16, 64>(aie::to_float<bfloat16>(a, 0)); // Convert to bfloat16
// Loop unroll hint: reduces overhead for small tile sizes
// For tile_size=256: 4 iterations (fully unrolled by compiler hint)
// For tile_size=512: 8 iterations
// For tile_size=1024: 16 iterations
// For tile_size=2048: 32 iterations
#pragma clang loop unroll_count(4)
    for (int i = 0; i < vector_size; i += 64) {
        ::aie::vector<bfloat16, 64> x_v = ::aie::load_v<64>(x);
        x += 64;
        ::aie::vector<bfloat16, 64> y_v = ::aie::load_v<64>(y);
        y += 64;
        ::aie::accum<accfloat, 64> ax_v = ::aie::mul(x_v, a_v);
        ::aie::accum<accfloat, 64> z_v = ::aie::add(ax_v, y_v);
        ::aie::vector<bfloat16, 64> z_v_converted = z_v.to_vector<bfloat16>();
        ::aie::store_v(z, z_v_converted);
        z += 64;
    }
    event1();
}

void saxpy_scalar(bfloat16 *x, bfloat16 *y, const bfloat16 a, bfloat16 *z, const int32_t vector_size)
{
    event0();
    float a_f = a;
    for (int i = 0; i < vector_size; ++i) {
        z[i] = a_f * x[i] + y[i];
    }
    event1();
}
}