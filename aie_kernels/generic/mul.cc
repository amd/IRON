// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <type_traits>

template <typename T_in, typename T_out> void eltwise_mul(T_in *a, T_in *b, T_out *c, int size)
{
    for (int i = 0; i < size; i++) {
        c[i] = a[i] * b[i];
    }
}

template <typename T_in, typename T_out> void eltwise_vmul(T_in *a, T_in *b, T_out *c, int size)
{

    constexpr int vec_factor = 32;
    event0();
    // Bound on the last full vector, remainder scalar-wise; see add.cc.
    const int F = size / vec_factor;
    for (int i = 0; i < F * vec_factor; i += vec_factor) {
        auto A = aie::load_v<vec_factor>(a + i);
        auto B = aie::load_v<vec_factor>(b + i);
        auto C = aie::mul(A, B).template to_vector<T_out>();
        aie::store_v(c + i, C);
    }
    for (int i = F * vec_factor; i < size; i++) {
        c[i] = a[i] * b[i];
    }
    event1();
}

extern "C" {

void eltwise_mul_bf16_scalar(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out, int size)
{
    eltwise_mul<bfloat16, bfloat16>(a_in, b_in, c_out, size);
}
void eltwise_mul_bf16_vector(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out, int size)
{
    eltwise_vmul<bfloat16, bfloat16>(a_in, b_in, c_out, size);
}
} // extern "C"
