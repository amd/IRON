// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

template <typename T, int N>
void rms_norm_general(const T *restrict input, const T *restrict input2, T *restrict output, int32_t cols, float epsilon)
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
    float inv_rms = aie::invsqrt(rms);
    // Normalize in f32 and round once. The previous code cast inv_rms to bf16 and did a
    // bf16*bf16 multiply, a coherent per-norm scale error that accumulated over a deep
    // residual stream and flipped near-tie argmaxes. Mirrors layer_norm.cc's accfloat path.
    ::aie::accum<accfloat, N> inv_rms_v;
    inv_rms_v.from_vector(::aie::broadcast<float, N>(inv_rms), 0);

    for (int i = 0; i < vector_chunks; i++) {
        ::aie::accum<accfloat, N> reg_a;
        reg_a.from_vector(::aie::load_v<N>(input + i * N), 0);
        reg_a = ::aie::mul(reg_a.template to_vector<float>(), inv_rms_v.template to_vector<float>());
        if (input2) {
            ::aie::accum<accfloat, N> reg_b;
            reg_b.from_vector(::aie::load_v<N>(input2 + i * N), 0);
            reg_a = ::aie::mul(reg_a.template to_vector<float>(), reg_b.template to_vector<float>());
        }
        ::aie::store_v(output + i * N, reg_a.template to_vector<T>());
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
    ::aie::set_rounding(aie::rounding_mode::conv_even);  // round-to-nearest-even; do not inherit a floor rounding mode from a prior kernel
    rms_norm_general<bfloat16, 16>(input, nullptr, output, size, epsilon);
}

void weighted_rms_norm(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out, int32_t size, float epsilon)
{
    ::aie::set_rounding(aie::rounding_mode::conv_even);  // round-to-nearest-even; do not inherit a floor rounding mode from a prior kernel
    rms_norm_general<bfloat16, 16>(a_in, b_in, c_out, size, epsilon);
}
}
