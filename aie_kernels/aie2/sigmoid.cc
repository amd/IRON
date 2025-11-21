// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"
#include "lut_based_ops.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

void sigmoid_tanh_approx_bf16(bfloat16 *restrict input_vector,
                              bfloat16 *restrict output_vector,
                              const int32_t vector_size)
{
    event0();

    auto it_in = aie::begin_restrict_vector<16>((bfloat16 *)input_vector);
    auto it_out = aie::begin_restrict_vector<16>((bfloat16 *)output_vector);

    aie::vector<bfloat16, 16> register_0_5 = aie::broadcast<bfloat16, 16>(0.5f);
    aie::vector<bfloat16, 16> register_1 = aie::broadcast<bfloat16, 16>(1.0f);
    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(64)
    for (int i = 0; i < vector_size; i += 16) {
        // Load input vector
        aie::vector<bfloat16, 16> input = *it_in++;

        // Compute tanh approximation
        aie::vector<bfloat16, 16> half_x = aie::mul(input, register_0_5);
        aie::vector<bfloat16, 16> tanh_half_x = getTanhBf16(half_x);
        auto tanh_half_x_approx = aie::add(tanh_half_x, register_1);
        aie::vector<bfloat16, 16> sigmoid_approx = aie::mul(tanh_half_x_approx, register_0_5);

        // Store output vector
        *it_out++ = sigmoid_approx;
    }

    event1();

    return;
}

extern "C" {

void sigmoid_bf16(bfloat16 *restrict input, bfloat16 *restrict output, int input_size)
{
    sigmoid_tanh_approx_bf16(input, output, input_size);
}

} // extern "C"
