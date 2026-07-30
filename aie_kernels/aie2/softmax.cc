// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "lut_based_ops.h"

#include <aie_api/aie.hpp>
#include <math.h>
#include <stdint.h>

using namespace aie;

void softmax_simple_bf16(bfloat16 *restrict input_vector, bfloat16 *restrict output_vector, const int32_t vector_size)
{
    event0();

    int num_elems = vector_size;
    float accum_exp_val;
    auto it_exp_in = aie::cbegin_vector<16>((bfloat16 *)input_vector);
    auto it_exp_out = aie::begin_vector<16>((bfloat16 *)output_vector);
    auto it_scale = aie::cbegin_restrict_vector<16>((bfloat16 *)output_vector);
    auto it_soft_out = aie::begin_restrict_vector<16>((bfloat16 *)output_vector);

    bfloat16 col_sum_inv;
    aie::vector<bfloat16, 16> in_elems, va;
    aie::accum<accfloat, 16> out_vals;
    int col_iters = num_elems >> 4;
    accum_exp_val = 0;

    /////////////////////
    //// Compute exp ////
    /////////////////////
    aie::vector<bfloat16, 16> exp_val;
    aie::vector<float, 16> input_fp32;

    const int elem_iters = num_elems / 16;
    aie::vector<bfloat16, 16> input_bf16;
    aie::accum<accfloat, 16> exp_val_accum;
    exp_val_accum = aie::zeros<accfloat, 16>();
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_exp_in++;
        exp_val = to_v16bfloat16(getExpBf16(input_bf16));
        exp_val_accum = add(exp_val_accum, exp_val);
        *it_exp_out++ = exp_val;
    }
    aie::vector<float, 16> reduce = exp_val_accum.to_vector<float>();
    accum_exp_val = aie::reduce_add(reduce);
    /////////////////////

    col_sum_inv = (bfloat16)aie::inv(accum_exp_val);
    for (int c = 0; c < col_iters; c++) {
        in_elems = *it_scale++;
        out_vals = aie::mul(in_elems, col_sum_inv);
        *it_soft_out++ = out_vals.to_vector<bfloat16>();
    }

    event1();

    return;
}

// Online (partial / tiled) softmax helpers.
//
// These kernels implement an online softmax that processes a row in sub-tile
// chunks, keeping running max and sum statistics in a small per-core buffer.
// softmax_stats names the two stats slots instead of using hard-coded array
// indices.
struct softmax_stats {
    bfloat16 max; // running max
    bfloat16 sum; // running sum of exp(x - max)
};

void softmax_partial_stats_impl(bfloat16 *restrict input, softmax_stats *restrict stats, const int32_t vector_size)
{
    event0();

    const int elem_iters = vector_size / 16;

    float running_max = (float)stats->max;
    float running_sum = (float)stats->sum;

    aie::vector<bfloat16, 16> input_bf16;
    aie::accum<accfloat, 16> exp_val_accum = aie::zeros<accfloat, 16>();

    auto it_in = aie::cbegin_vector<16>((bfloat16 *)input);

    // Single-pass online algorithm: for each vector chunk, check if max
    // needs updating, rescale the running sum if so, then accumulate
    // exp(x - max).
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_in++;
        float chunk_max = aie::reduce_max(input_bf16);

        if (chunk_max > running_max) {
            // Rescale accumulated exp values by exp(old_max - new_max)
            aie::vector<bfloat16, 16> correction =
                to_v16bfloat16(getExpBf16(aie::broadcast<bfloat16, 16>((bfloat16)(running_max - chunk_max))));
            float scale = (float)correction[0];
            // Rescale the partial vector accumulator
            aie::vector<bfloat16, 16> scale_vec = aie::broadcast<bfloat16, 16>((bfloat16)scale);
            exp_val_accum = aie::mul(exp_val_accum.to_vector<bfloat16>(), scale_vec);
            // Rescale the running scalar sum from previous chunks
            running_sum *= scale;
            running_max = chunk_max;
        }

        aie::vector<bfloat16, 16> shifted = aie::sub(input_bf16, aie::broadcast<bfloat16, 16>((bfloat16)running_max));
        aie::vector<bfloat16, 16> exp_val = to_v16bfloat16(getExpBf16(shifted));
        exp_val_accum = add(exp_val_accum, exp_val);
    }

    // Reduce the vector accumulator and add to running sum
    aie::vector<float, 16> reduce = exp_val_accum.to_vector<float>();
    running_sum += aie::reduce_add(reduce);

    stats->max = (bfloat16)running_max;
    stats->sum = (bfloat16)running_sum;

    event1();
}

void softmax_partial_norm_impl(bfloat16 *restrict input,
                               bfloat16 *restrict output,
                               softmax_stats *restrict stats,
                               const int32_t vector_size)
{
    event0();

    const int elem_iters = vector_size / 16;

    float max_val = (float)stats->max;
    float sum_val = (float)stats->sum;
    bfloat16 inv_sum = (bfloat16)aie::inv(sum_val);

    aie::vector<bfloat16, 16> max_val_vec = aie::broadcast<bfloat16, 16>((bfloat16)max_val);

    aie::vector<bfloat16, 16> input_bf16;
    aie::accum<accfloat, 16> out_vals;

    auto it_in = aie::cbegin_restrict_vector<16>((bfloat16 *)input);
    auto it_out = aie::begin_restrict_vector<16>((bfloat16 *)output);

    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_in++;
        aie::vector<bfloat16, 16> shifted = aie::sub(input_bf16, max_val_vec);
        aie::vector<bfloat16, 16> exp_val = to_v16bfloat16(getExpBf16(shifted));
        out_vals = aie::mul(exp_val, inv_sum);
        *it_out++ = out_vals.to_vector<bfloat16>();
    }

    event1();
}

extern "C" {

void softmax_bf16(bfloat16 *restrict input, bfloat16 *restrict output, const int32_t input_size)
{
    softmax_simple_bf16(input, output, input_size);
}

void softmax_partial_init_bf16(softmax_stats *restrict stats)
{
    stats->max = (bfloat16)(-INFINITY);
    stats->sum = (bfloat16)(0.0f);
}

void softmax_partial_stats_bf16(bfloat16 *restrict input, softmax_stats *restrict stats, const int32_t vector_size)
{
    softmax_partial_stats_impl(input, stats, vector_size);
}

void softmax_partial_norm_bf16(bfloat16 *restrict input,
                               bfloat16 *restrict output,
                               softmax_stats *restrict stats,
                               const int32_t vector_size)
{
    softmax_partial_norm_impl(input, output, stats, vector_size);
}

void mask_bf16(bfloat16 *inout, const int32_t unmasked_size, const int32_t total_size)
{
    for (int32_t i = unmasked_size; i < total_size; i++) {
        inout[i] = (bfloat16)(-INFINITY);
    }
}

} // extern "C"
