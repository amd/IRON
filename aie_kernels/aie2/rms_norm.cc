// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "aie2_math.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

template <typename T, int N>
void rms_norm_general(const T *restrict input,
                      const T *restrict input2,
                      T *restrict output,
                      int32_t cols,
                      float epsilon)
{
    event0();
    ::aie::vector<float, N> add_res = ::aie::zeros<float, N>();

    int vector_chunks = cols / N;
    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<T, N> reg_a = ::aie::load_v<N>(input + i * N);
        ::aie::vector<float, N> square_v = ::aie::mul_square(reg_a);
        add_res = ::aie::add(add_res, square_v);
    }
    float sum_sq = ::aie::reduce_add(add_res);

    int remaining = cols % N;
    if (remaining > 0) {
        int start_idx = vector_chunks * N;
        for (int i = 0; i < remaining; i++) {
            T val = input[start_idx + i];
            float square = static_cast<float>(val) * static_cast<float>(val);
            sum_sq += square;
        }
    }

    float rms = sum_sq / cols + epsilon;
    float inv_rms = invsqrt(rms);
    // Peano has no f32 vector multiply for AIE2, so the f32 scale rides in a
    // bf16 pair and is applied as two exact products accumulated in f32. A
    // single bf16 scale would shift every element of a norm the same way.
    T inv_rms_hi = static_cast<T>(inv_rms);
    T inv_rms_lo = static_cast<T>(inv_rms - static_cast<float>(inv_rms_hi));

    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<T, N> reg_a = ::aie::load_v<N>(input + i * N);
        ::aie::accum<accfloat, N> acc = ::aie::mul(reg_a, inv_rms_hi);
        acc = ::aie::mac(acc, reg_a, inv_rms_lo);
        if (input2) {
            acc = ::aie::mul(acc.template to_vector<T>(), ::aie::load_v<N>(input2 + i * N));
        }
        ::aie::store_v(output + i * N, acc.template to_vector<T>());
    }

    if (remaining > 0) {
        int start_idx = vector_chunks * N;
        for (int i = 0; i < remaining; i++) {
            T val = input[start_idx + i];
            T norm_val = static_cast<T>(static_cast<float>(val) * inv_rms);
            if (input2) {
                T mul_val = input2[start_idx + i];
                output[start_idx + i] = static_cast<T>(static_cast<float>(norm_val) * static_cast<float>(mul_val));
            } else {
                output[start_idx + i] = norm_val;
            }
        }
    }
    event1();
}

extern "C" {
void rms_norm_bf16_vector(bfloat16 *input, bfloat16 *output, int32_t size, float epsilon)
{
    ::aie::set_rounding(aie::rounding_mode::conv_even); // round-to-nearest-even
    rms_norm_general<bfloat16, 32>(input, nullptr, output, size, epsilon);
}

void weighted_rms_norm(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out, int32_t size, float epsilon)
{
    ::aie::set_rounding(aie::rounding_mode::conv_even); // round-to-nearest-even
    rms_norm_general<bfloat16, 32>(a_in, b_in, c_out, size, epsilon);
}
}
