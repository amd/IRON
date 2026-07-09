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

// ---------------------------------------------------------------------------
// Online (partial / tiled) softmax helpers
//
// These three kernels implement a two-pass online softmax that processes a row
// in sub-tile chunks, keeping running max and sum statistics in a small local
// buffer (`stats`).  Layout of the stats buffer (bfloat16[16], only [0..1]
// used):
//   stats[0] = running max   (scaled by log2e)
//   stats[1] = running sum   (of exp2(x*log2e - max))
// ---------------------------------------------------------------------------

void softmax_partial_stats_impl(bfloat16 *restrict input, bfloat16 *stats, const int32_t vector_size)
{
    event0();

    const int elem_iters = vector_size / SM_VEC_LEN;

    aie::vector<bfloat16, SM_VEC_LEN> input_bf16;
    aie::accum<accfloat, SM_VEC_LEN> scaled_accum, exp_in_accum;
    aie::accum<accfloat, SM_VEC_LEN> exp_val_accum = aie::zeros<accfloat, SM_VEC_LEN>();

    aie::vector<bfloat16, SM_VEC_LEN> log2e_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)log2e);

    // --- Phase 1: find local max (scaled by log2e) -------------------------
    float local_max = -INFINITY;
    auto it_in1 = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input);
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_in1++;
        scaled_accum = aie::mul(input_bf16, log2e_vec);
        float chunk_max = aie::reduce_max(scaled_accum.to_vector<bfloat16>());
        if (chunk_max > local_max) {
            local_max = chunk_max;
        }
    }

    // --- Phase 2: update running max, rescale running sum ------------------
    float old_max = (float)stats[0];
    float old_sum = (float)stats[1];

    if (local_max > old_max) {
        // New max is larger — rescale the old sum by exp2(old_max - new_max)
        aie::vector<float, SM_VEC_LEN> diff_vec = aie::broadcast<float, SM_VEC_LEN>(old_max - local_max);
        aie::vector<bfloat16, SM_VEC_LEN> corr = aie::exp2<bfloat16>(diff_vec);
        old_sum = old_sum * (float)corr[0];
        old_max = local_max;
    }

    // --- Phase 3: accumulate exp2(input * log2e - max) for this chunk ------
    aie::vector<bfloat16, SM_VEC_LEN> max_val_vec = aie::broadcast<bfloat16, SM_VEC_LEN>((bfloat16)old_max);

    auto it_in2 = aie::cbegin_restrict_vector<SM_VEC_LEN>((bfloat16 *)input);
    for (int i = 0; i < elem_iters; i++) {
        input_bf16 = *it_in2++;
        scaled_accum = aie::mul(input_bf16, log2e_vec);
        exp_in_accum = aie::sub(scaled_accum, max_val_vec);
        aie::vector<bfloat16, SM_VEC_LEN> exp_val = aie::exp2<bfloat16>(exp_in_accum.to_vector<float>());
        exp_val_accum = add(exp_val_accum, exp_val);
    }

    aie::vector<float, SM_VEC_LEN> reduce = exp_val_accum.to_vector<float>();
    float local_sum = aie::reduce_add(reduce);

    // --- Phase 4: store updated stats --------------------------------------
    stats[0] = (bfloat16)old_max;
    stats[1] = (bfloat16)(old_sum + local_sum);

    event1();
}

void softmax_partial_norm_impl(bfloat16 *restrict input,
                               bfloat16 *restrict output,
                               bfloat16 *stats,
                               const int32_t vector_size)
{
    event0();

    const int elem_iters = vector_size / SM_VEC_LEN;

    float max_val = (float)stats[0];
    float sum_val = (float)stats[1];
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

void softmax_partial_init_bf16(bfloat16 *stats)
{
    stats[0] = (bfloat16)(-INFINITY);
    stats[1] = (bfloat16)(0.0f);
}

void softmax_partial_stats_bf16(bfloat16 *restrict input, bfloat16 *stats, const int32_t vector_size)
{
    softmax_partial_stats_impl(input, stats, vector_size);
}

void softmax_partial_norm_bf16(bfloat16 *restrict input,
                               bfloat16 *restrict output,
                               bfloat16 *stats,
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