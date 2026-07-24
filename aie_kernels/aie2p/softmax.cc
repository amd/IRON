// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <math.h>
#include <stdint.h>

#define SM_VEC_LEN 64   // 32
#define log2e 1.4453125 // 1.44269504089

using namespace aie;

void softmax_simple_bf16(bfloat16 *restrict input_vector, bfloat16 *restrict output_vector, const int32_t vector_size)
{
    event0();

    // VJUNG: We do 3 passes on the vector:
    // 1. Find the max value scaled by log2e in the vector
    // 2. Calculate the exponentials of the scaled values minus the maximum
    // 3. Calculate the softmax by dividing each exponential by the sum of all exponentials
    // Note: The multiplication by log2e is very sensitive, casting it to bf16 before exponentiation leads to wrong
    // output.

    auto it_log_in = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input_vector);
    auto it_log_out = aie::begin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input_vector);
    auto it_exp_in = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input_vector);
    auto it_exp_out = aie::begin_restrict_vector<SM_VEC_LEN>((bfloat16 *)output_vector);
    auto it_scale = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)output_vector);
    auto it_soft_out = aie::begin_restrict_vector<SM_VEC_LEN>((bfloat16 *)output_vector);

    aie::vector<bfloat16, SM_VEC_LEN> in_elems, exp_val, input_bf16, log2e_vec, max_val_vec;
    aie::accum<accfloat, SM_VEC_LEN> out_vals, exp_val_accum, scaled_accum, exp_in_accum;

    float max_val = -INFINITY;
    float accum_exp_val = 0;
    float running_max = 0;
    bfloat16 col_sum_inv;
    const int elem_iters = vector_size / SM_VEC_LEN;

    exp_val_accum = aie::zeros<accfloat, SM_VEC_LEN>();

    log2e_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)log2e);

    // First pass
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_log_in++;
        scaled_accum = aie::mul(input_bf16, log2e_vec);
        running_max = aie::reduce_max(scaled_accum.to_vector<bfloat16>());
        if (running_max > max_val) {
            max_val = running_max;
        }
    }
    max_val_vec = aie::broadcast<bfloat16, SM_VEC_LEN>(max_val);

    // Second pass
    for (int i = 0; i < elem_iters; i++) {

        input_bf16 = *it_exp_in++;

        scaled_accum = aie::mul(input_bf16, log2e_vec);
        exp_in_accum = aie::sub(scaled_accum, max_val_vec);
        exp_val = aie::exp2<bfloat16>(exp_in_accum.to_vector<float>());
        exp_val_accum = add(exp_val_accum, exp_val);

        *it_exp_out++ = exp_val;
    }

    // Final pass
    aie::vector<float, SM_VEC_LEN> reduce = exp_val_accum.to_vector<float>();
    accum_exp_val = aie::reduce_add(reduce);
    col_sum_inv = (bfloat16)aie::inv(accum_exp_val);

    for (int c = 0; c < elem_iters; c++) {
        in_elems = *it_scale++;
        out_vals = aie::mul(in_elems, col_sum_inv);
        *it_soft_out++ = out_vals.to_vector<bfloat16>();
    }

    event1();

    return;
}

// partial_softmax_alias_bf16 is a flash-attention style single-shot softmax
// used by the projected-fused path. It shares the same three-pass structure as
// softmax_simple_bf16 (find max, exp, normalize) but differs in two ways that
// make code sharing awkward: (1) it folds the query scale into the log2e
// multiply instead of using the fixed log2e constant, and (2) it maintains
// per-row running max/sum in an externally-supplied scale_buffer (flash
// accumulation across key tiles) rather than reducing a whole row locally. The
// softmax_partial_stats_impl / softmax_partial_norm_impl pair below implement a
// different (chunked, two-call) online softmax that keeps its running stats in
// a compact softmax_stats buffer; those are used by the standalone softmax
// operator, not by this projected-fused kernel.
void partial_softmax_alias_bf16(bfloat16 *restrict input_vector,
                                bfloat16 *restrict output_vector,
                                bfloat16 *restrict scale_buffer,
                                const int32_t vector_size,
                                const int32_t row_idx,
                                const int32_t num_rows,
                                const bfloat16 scale)
{
    event0();
    ::aie::set_rounding(aie::rounding_mode::conv_even);

    // VJUNG: We do 3 passes on the vector:
    // 1. Find the max value scaled by log2e in the vector
    // 2. Calculate the exponentials of the scaled values minus the maximum
    // 3. Calculate the softmax by dividing each exponential by the sum of all exponentials
    // Note: The multiplication by log2e is very sensitive, casting it to bf16 before exponentiation leads to wrong
    // output.

    auto it_log_in = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input_vector);
    auto it_log_out = aie::begin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input_vector);
    auto it_exp_in = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input_vector);
    auto it_exp_out = aie::begin_restrict_vector<SM_VEC_LEN>((bfloat16 *)output_vector);

    aie::vector<bfloat16, SM_VEC_LEN> in_elems, exp_val, input_bf16, log2e_vec, max_val_vec;
    aie::accum<accfloat, SM_VEC_LEN> out_vals, exp_val_accum, scaled_accum, exp_in_accum;

    float max_val = 0;
    float accum_exp_val = 0;
    float running_max = 0;
    float col_sum_inv;
    const int elem_iters = vector_size / SM_VEC_LEN;

    exp_val_accum = aie::zeros<accfloat, SM_VEC_LEN>();

    log2e_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)scale);

    // First pass
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_log_in++;
        scaled_accum = aie::mul(input_bf16, log2e_vec);
        running_max = aie::reduce_max(scaled_accum.to_vector<bfloat16>());
        if (running_max > max_val) {
            max_val = running_max;
        }
    }

    // Compute m_{i}
    if (max_val > scale_buffer[row_idx]) {
        scale_buffer[num_rows + row_idx] = max_val;
    } else {
        scale_buffer[num_rows + row_idx] = scale_buffer[row_idx];
        max_val = scale_buffer[row_idx];
    }

    max_val_vec = aie::broadcast<bfloat16, SM_VEC_LEN>(max_val);

    // Second pass
    for (int i = 0; i < elem_iters; i++) {

        input_bf16 = *it_exp_in++;

        scaled_accum = aie::mul(input_bf16, log2e_vec);
        exp_in_accum = aie::sub(scaled_accum, max_val_vec);
        exp_val = aie::exp2<bfloat16>(exp_in_accum.to_vector<float>());
        exp_val_accum = add(exp_val_accum, exp_val);

        *it_exp_out++ = exp_val;
    }

    aie::vector<float, SM_VEC_LEN> reduce = exp_val_accum.to_vector<float>();
    accum_exp_val = aie::reduce_add(reduce);

    scale_buffer[3 * num_rows + row_idx] = accum_exp_val;

    event1();

    return;
}

// Online (partial / tiled) softmax helpers.
//
// These kernels implement an online softmax that processes a row in sub-tile
// chunks, keeping running max and sum statistics in a small per-core buffer.
// The max is stored scaled by log2e and the sum accumulates exp2(x*log2e -
// max), matching the exp2-based normalization used below. softmax_stats names
// the two stats slots instead of using hard-coded array indices.
struct softmax_stats {
    bfloat16 max; // running max (scaled by log2e)
    bfloat16 sum; // running sum of exp2(x*log2e - max)
};

void softmax_partial_stats_impl(bfloat16 *restrict input, softmax_stats *restrict stats, const int32_t vector_size)
{
    event0();

    const int elem_iters = vector_size / SM_VEC_LEN;

    float running_max = (float)stats->max;
    float running_sum = (float)stats->sum;

    aie::vector<bfloat16, SM_VEC_LEN> input_bf16;
    aie::accum<accfloat, SM_VEC_LEN> scaled_accum, exp_in_accum;
    aie::accum<accfloat, SM_VEC_LEN> exp_val_accum = aie::zeros<accfloat, SM_VEC_LEN>();

    aie::vector<bfloat16, SM_VEC_LEN> log2e_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)log2e);

    auto it_in = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input);

    // Single-pass online algorithm (matches aie_kernels/aie2/softmax.cc): for
    // each vector chunk, update the running max if needed -- rescaling the
    // partial accumulator and running sum by exp2(old_max - new_max) -- then
    // accumulate exp2(x*log2e - max).
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_in++;
        scaled_accum = aie::mul(input_bf16, log2e_vec);
        float chunk_max = aie::reduce_max(scaled_accum.to_vector<bfloat16>());

        if (chunk_max > running_max) {
            aie::vector<float, SM_VEC_LEN> diff_vec = aie::broadcast<float, SM_VEC_LEN>(running_max - chunk_max);
            aie::vector<bfloat16, SM_VEC_LEN> corr = aie::exp2<bfloat16>(diff_vec);
            float scale = (float)corr[0];
            aie::vector<bfloat16, SM_VEC_LEN> scale_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)scale);
            exp_val_accum = aie::mul(exp_val_accum.to_vector<bfloat16>(), scale_vec);
            running_sum *= scale;
            running_max = chunk_max;
        }

        aie::vector<bfloat16, SM_VEC_LEN> max_val_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)running_max);
        exp_in_accum = aie::sub(scaled_accum, max_val_vec);
        aie::vector<bfloat16, SM_VEC_LEN> exp_val = aie::exp2<bfloat16>(exp_in_accum.to_vector<float>());
        exp_val_accum = add(exp_val_accum, exp_val);
    }

    aie::vector<float, SM_VEC_LEN> reduce = exp_val_accum.to_vector<float>();
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

    const int elem_iters = vector_size / SM_VEC_LEN;

    float max_val = (float)stats->max;
    float sum_val = (float)stats->sum;
    bfloat16 inv_sum = (bfloat16)aie::inv(sum_val);

    aie::vector<bfloat16, SM_VEC_LEN> log2e_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)log2e);
    aie::vector<bfloat16, SM_VEC_LEN> max_val_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)max_val);

    aie::vector<bfloat16, SM_VEC_LEN> input_bf16;
    aie::accum<accfloat, SM_VEC_LEN> scaled_accum, exp_in_accum, out_vals;

    auto it_in = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input);
    auto it_out = aie::begin_restrict_vector<SM_VEC_LEN>((bfloat16 *)output);

    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_in++;
        scaled_accum = aie::mul(input_bf16, log2e_vec);
        exp_in_accum = aie::sub(scaled_accum, max_val_vec);
        aie::vector<bfloat16, SM_VEC_LEN> exp_val = aie::exp2<bfloat16>(exp_in_accum.to_vector<float>());
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

void partial_softmax_bf16(bfloat16 *restrict input,
                          bfloat16 *restrict output,
                          bfloat16 *restrict scale_buffer,
                          const int32_t input_size,
                          const int32_t row_idx,
                          const int32_t num_rows,
                          const bfloat16 scale)
{
    partial_softmax_alias_bf16(input, output, scale_buffer, input_size, row_idx, num_rows, scale);
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

void mask_bf16(bfloat16 *inout, const int32 unmasked_size, const int32 total_size)
{
    // TODO: Optimize this to use vector code
    for (int32 i = unmasked_size; i < total_size; i++) {
        inout[i] = (bfloat16)(-INFINITY);
    }
}

} // extern "C"