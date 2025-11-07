// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

void leaky_relu_vectorized_bf16(bfloat16 *restrict a,
                                bfloat16 *restrict c,
                                const int32_t vector_size,
                                const bfloat16 alpha)
{
    event0();

    auto it_in = aie::begin_restrict_vector<32>((bfloat16 *)a);
    auto it_out = aie::begin_restrict_vector<32>((bfloat16 *)c);

    // Broadcast alpha to a vector
    vector<bfloat16, 32> alpha_vec = aie::broadcast<bfloat16, 32>(alpha);
    vector<bfloat16, 32> zeroes = aie::zeros<bfloat16, 32>();

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(32)
    for (int i = 0; i < vector_size; i += 32) {
        vector<bfloat16, 32> input = *it_in++;
        // Leaky RELU: f(x) = max(x, alpha * x) where alpha is typically 0.01
        // When alpha < 1: if x > 0 then x, else alpha * x
        vector<bfloat16, 32> alpha_times_input = aie::mul(input, alpha_vec);
        vector<bfloat16, 32> output = aie::max(input, alpha_times_input);
        *it_out++ = output;
    }

    event1();

    return;
}

extern "C" {

void leaky_relu_bf16(bfloat16 *restrict input, bfloat16 *restrict output, int input_size, bfloat16 alpha)
{
    leaky_relu_vectorized_bf16(input, output, input_size, alpha);
}

} // extern "C"