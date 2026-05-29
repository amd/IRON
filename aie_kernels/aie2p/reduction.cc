// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Reduction kernel for AIE2P (NPU2)
// Supports: sum, mean, max, min along the reduction dimension
// AIE2P has enhanced vector capabilities compared to AIE2

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <type_traits>

extern "C" {

/**
 * Reduction Sum Kernel - AIE2P optimized
 * AIE2P has 8 columns and enhanced vector capabilities
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (sum of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_sum_bf16_scalar(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    bfloat16 acc = bfloat16(0.0f);

    for (int i = 0; i < reduction_size; i++) {
        acc += input[i];
    }

    output[0] = acc;
}

/**
 * Reduction Sum Kernel - Vectorized version for AIE2P
 * Uses larger vector factor for AIE2P (32 elements per vector)
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (sum of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_sum_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    constexpr int vec_factor = 16; // Use 16 for AIE2P accum<accfloat> compatibility (matches layer_norm/conv patterns; 32 can cause slow/erroneous peano compilation)

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Initialize accumulator using from_vector pattern for AIE2P bf16<->accfloat compatibility (prevents compile hangs)
    aie::accum<accfloat, vec_factor> acc_vec;
    acc_vec.from_vector(aie::zeros<float, vec_factor>(), 0);

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(16)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;
        // Use mac with ones vector for sum (mulacc-by-1 idiom) - addresses AIE2P bf16 accumulation compatibility
        auto ones = aie::broadcast<bfloat16, vec_factor>(bfloat16(1.0f));
        acc_vec = aie::mac(acc_vec, in_vec, ones);
    }

    // Horizontal sum using reduce_add on float vector (standard pattern, no .template needed here)
    aie::vector<float, vec_factor> red = acc_vec.to_vector<float>();
    float sum_f = aie::reduce_add(red);

    // Handle remaining elements (accumulate in float for precision)
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        sum_f += static_cast<float>(pIn[i]);
    }

    pOut[0] = static_cast<bfloat16>(sum_f);

    event1();
}

/**
 * Reduction Max Kernel - AIE2P optimized
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (max of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_max_bf16_scalar(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    bfloat16 max_val = input[0];

    for (int i = 1; i < reduction_size; i++) {
        max_val = (input[i] > max_val) ? input[i] : max_val;
    }

    output[0] = max_val;
}

/**
 * Reduction Max Kernel - Vectorized version for AIE2P
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (max of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_max_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    constexpr int vec_factor = 16; // Standardized to 16 for AIE2P vector/accum compatibility and fast compile

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Vectorized max using AIE native max + reduce_max (eliminates scalar pointwise inner loop that caused slow compiles and matches auditor recommendations)
    aie::vector<bfloat16, vec_factor> max_v = aie::broadcast<bfloat16, vec_factor>(bfloat16(-3.4028235e+38f));

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(16)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;

        max_v = aie::max(max_v, in_vec);
    }

    bfloat16 result = aie::reduce_max(max_v);

    // Handle remaining elements
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        if (pIn[i] > result) result = pIn[i];
    }

    pOut[0] = result;

    event1();
}

/**
 * Reduction Min Kernel - AIE2P optimized
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (min of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_min_bf16_scalar(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    bfloat16 min_val = input[0];

    for (int i = 1; i < reduction_size; i++) {
        min_val = (input[i] < min_val) ? input[i] : min_val;
    }

    output[0] = min_val;
}

/**
 * Reduction Min Kernel - Vectorized version for AIE2P
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (min of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_min_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    constexpr int vec_factor = 16; // Standardized to 16 for AIE2P vector/accum compatibility and fast compile

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Vectorized min using AIE native min + reduce_min (eliminates scalar pointwise inner loop)
    aie::vector<bfloat16, vec_factor> min_v = aie::broadcast<bfloat16, vec_factor>(bfloat16(3.4028235e+38f));

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(16)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;

        min_v = aie::min(min_v, in_vec);
    }

    bfloat16 result = aie::reduce_min(min_v);

    // Handle remaining elements
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        if (pIn[i] < result) result = pIn[i];
    }

    pOut[0] = result;

    event1();
}

/**
 * Reduction Mean Kernel - AIE2P optimized
 * Computes sum then divides by count
 *
 * @param input - Input tensor [reduction_dim]
 * @param output - Output scalar (mean of all elements)
 * @param reduction_size - Size of the reduction dimension
 */
void reduction_mean_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size)
{
    constexpr int vec_factor = 16; // Use 16 for AIE2P accum<accfloat> compatibility (matches layer_norm/conv patterns)

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Initialize accumulator using from_vector pattern for AIE2P bf16<->accfloat compatibility (prevents compile hangs)
    aie::accum<accfloat, vec_factor> acc_vec;
    acc_vec.from_vector(aie::zeros<float, vec_factor>(), 0);

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(16)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;
        // Use mac with ones vector for sum (mulacc-by-1 idiom) - addresses AIE2P bf16 accumulation compatibility
        auto ones = aie::broadcast<bfloat16, vec_factor>(bfloat16(1.0f));
        acc_vec = aie::mac(acc_vec, in_vec, ones);
    }

    // Horizontal sum using reduce_add on float vector (standard pattern)
    aie::vector<float, vec_factor> red = acc_vec.to_vector<float>();
    float sum_f = aie::reduce_add(red);

    // Handle remaining elements (accumulate in float)
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        sum_f += static_cast<float>(pIn[i]);
    }

    // Compute mean (in float then cast for better precision)
    bfloat16 mean = static_cast<bfloat16>(sum_f / static_cast<float>(reduction_size));
    pOut[0] = mean;

    event1();
}

} // end extern "C" for C-linkage kernels (fix for symbol resolution in aiecc link, matching reduction.cc fix)
