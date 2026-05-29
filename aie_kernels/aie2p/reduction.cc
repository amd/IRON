// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
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
    constexpr int vec_factor = 32; // AIE2P supports larger vectors

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Initialize accumulator vector
    aie::vector<bfloat16, vec_factor> acc_vec = aie::zeros<bfloat16, vec_factor>();

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(32)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;
        acc_vec = aie::add(acc_vec, in_vec);
    }

    // Horizontal sum of the accumulator vector
    bfloat16 result = aie::reduce_add(acc_vec);

    // Handle remaining elements if reduction_size is not divisible by vec_factor
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        result += pIn[i];
    }

    pOut[0] = result;

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
    constexpr int vec_factor = 32;

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Initialize with negative infinity for max
    bfloat16 max_val = bfloat16(-3.4e38f);

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(32)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;

        // Vector max reduction using AIE2P native max
        for (int j = 0; j < vec_factor; j++) {
            max_val = (in_vec[j] > max_val) ? in_vec[j] : max_val;
        }
    }

    // Handle remaining elements
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        max_val = (pIn[i] > max_val) ? pIn[i] : max_val;
    }

    pOut[0] = max_val;

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
    constexpr int vec_factor = 32;

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Initialize with positive infinity for min
    bfloat16 min_val = bfloat16(3.4e38f);

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(32)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;

        // Vector min reduction using AIE2P native min
        for (int j = 0; j < vec_factor; j++) {
            min_val = (in_vec[j] < min_val) ? in_vec[j] : min_val;
        }
    }

    // Handle remaining elements
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        min_val = (pIn[i] < min_val) ? pIn[i] : min_val;
    }

    pOut[0] = min_val;

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
    constexpr int vec_factor = 32;

    event0();

    bfloat16 *__restrict pIn = input;
    bfloat16 *__restrict pOut = output;

    // Initialize accumulator vector
    aie::vector<bfloat16, vec_factor> acc_vec = aie::zeros<bfloat16, vec_factor>();

    const int F = reduction_size / vec_factor;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(32)
    for (int i = 0; i < F; i++) {
        aie::vector<bfloat16, vec_factor> in_vec = aie::load_v<vec_factor>(pIn);
        pIn += vec_factor;
        acc_vec = aie::add(acc_vec, in_vec);
    }

    // Horizontal sum of the accumulator vector
    bfloat16 sum = aie::reduce_add(acc_vec);

    // Handle remaining elements
    const int remainder = reduction_size % vec_factor;
    for (int i = 0; i < remainder; i++) {
        sum += pIn[i];
    }

    // Compute mean
    bfloat16 mean = sum / bfloat16(static_cast<float>(reduction_size));
    pOut[0] = mean;

    event1();
}

extern "C" {

// Sum kernels
void reduction_sum_bf16_scalar(bfloat16 *input, bfloat16 *output, int reduction_size);
void reduction_sum_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size);

// Max kernels
void reduction_max_bf16_scalar(bfloat16 *input, bfloat16 *output, int reduction_size);
void reduction_max_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size);

// Min kernels
void reduction_min_bf16_scalar(bfloat16 *input, bfloat16 *output, int reduction_size);
void reduction_min_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size);

// Mean kernel (AIE2P only)
void reduction_mean_bf16_vector(bfloat16 *input, bfloat16 *output, int reduction_size);

} // extern "C"
