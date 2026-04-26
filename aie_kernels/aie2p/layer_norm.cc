// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

template <typename T, int N> void layer_norm(const T *restrict input, T *restrict output, int32_t cols)
{
    event0();
    constexpr float epsilon = 1e-5f;
    const float gamma = 1.0f;
    const float beta = 0.0f;

    ::aie::vector<T, N> gamma_v = ::aie::broadcast<T, N>(gamma);
    ::aie::vector<T, N> beta_v = ::aie::broadcast<T, N>(beta);
    ::aie::vector<T, N> sum_acc = ::aie::zeros<T, N>();
    ::aie::vector<float, N> sum_sq_acc = ::aie::zeros<float, N>();

    int vector_chunks = cols / N;
    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<T, N> reg_a = ::aie::load_v<N>(input + i * N);
        sum_acc = ::aie::add(sum_acc, reg_a);
        ::aie::vector<float, N> sq_acc = ::aie::mul(reg_a, reg_a);
        sum_sq_acc = ::aie::add(sum_sq_acc, sq_acc);
    }

    float sum_of_vals = ::aie::reduce_add(sum_acc);
    float sum_of_sq_vals = ::aie::reduce_add(sum_sq_acc);

    float mean = sum_of_vals / float(cols);
    float mean_sq = mean * mean;
    float variance = (sum_of_sq_vals / float(cols)) - mean_sq;
    float inv_std = aie::invsqrt(variance + epsilon);

    ::aie::vector<T, N> mean_v = ::aie::broadcast<T, N>(mean);
    ::aie::vector<T, N> inv_std_v = ::aie::broadcast<T, N>(inv_std);

    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<T, N> reg_a = ::aie::load_v<N>(input + i * N);
        ::aie::vector<T, N> diff_v = ::aie::sub(reg_a, mean_v);
        ::aie::vector<T, N> norm_v = ::aie::mul(diff_v, inv_std_v);
        ::aie::vector<T, N> scaled_v = ::aie::mul(norm_v, gamma_v);
        ::aie::vector<T, N> out_v = ::aie::add(scaled_v, beta_v);
        ::aie::store_v(output + i * N, out_v);
    }
    event1();
}

// The below kernel increases the accuracy of the output by performing the calculations in f32, with performance
// cost of a lower bandwidth by up to 2x.
void layer_norm_bf16_f32_calculation(const bfloat16 *restrict input, bfloat16 *restrict output, int32_t cols)
{
    event0();
    const float epsilon = 1e-5f;
    const float gamma = 1.0f;
    const float beta = 0.0f;

    // Note: Using a vector of 8 for float dtype because using a size of 16 causes a compile
    // error with llvm-aie (peano)
    ::aie::vector<float, 8> gamma_v = ::aie::broadcast<float, 8>(gamma);
    ::aie::vector<float, 8> beta_v = ::aie::broadcast<float, 8>(beta);
    ::aie::accum<accfloat, 8> sum_acc;
    ::aie::accum<accfloat, 8> sum_sq_acc;
    sum_acc.from_vector(::aie::zeros<float, 8>(), 0);
    sum_sq_acc.from_vector(::aie::zeros<float, 8>(), 0);

    int vector_chunks = cols / 8;
    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<bfloat16, 8> reg_a = ::aie::load_v<8>(input + i * 8);
        sum_acc = ::aie::add(sum_acc, reg_a);
        ::aie::vector<float, 8> sq_acc = ::aie::mul(reg_a, reg_a);
        sum_sq_acc = ::aie::add(sum_sq_acc, sq_acc);
    }

    float sum_of_vals = ::aie::reduce_add(sum_acc.to_vector<float>());
    float sum_of_sq_vals = ::aie::reduce_add(sum_sq_acc.to_vector<float>());

    float mean = ::aie::div(sum_of_vals, aie::to_float(cols));
    float mean_sq = mean * mean;
    float variance = ::aie::div(sum_of_sq_vals, aie::to_float(cols)) - mean_sq;
    float inv_std = ::aie::invsqrt(variance + epsilon);

    ::aie::accum<accfloat, 8> mean_v;
    ::aie::accum<accfloat, 8> inv_std_v;
    mean_v.from_vector(::aie::broadcast<float, 8>(mean), 0);
    inv_std_v.from_vector(::aie::broadcast<float, 8>(inv_std), 0);

    for (int i = 0; i < vector_chunks; i++) {
        ::aie::accum<accfloat, 8> reg_a;
        reg_a.from_vector(::aie::load_v<8>(input + i * 8), 0);
        reg_a = ::aie::sub(reg_a, mean_v);
        reg_a = ::aie::mul(reg_a.to_vector<float>(), inv_std_v.to_vector<float>());
        reg_a = ::aie::mul(reg_a.to_vector<float>(), gamma_v);
        reg_a = ::aie::add(reg_a, beta_v);
        ::aie::store_v(output + i * 8, reg_a.to_vector<bfloat16>());
    }
    event1();
}

extern "C" {
void layer_norm(bfloat16 *input, bfloat16 *output, int32_t cols)
{
    ::aie::set_rounding(aie::rounding_mode::conv_even);
    layer_norm<bfloat16, 32>(input, output, cols);
}
}
