// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

// One 16-lane GELU (tanh approximation): 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3))).
static inline aie::vector<bfloat16, 16> gelu_tanh_approx_v16(aie::vector<bfloat16, 16> x)
{
    const bfloat16 k0_5 = 0.5f;
    const bfloat16 k1 = 1.0f;
    const bfloat16 sqrt_2_over_pi = 0.79788456f; // sqrt(2/pi)
    const bfloat16 kBeta = 0.044715f;

    auto v05 = aie::broadcast<bfloat16, 16>(k0_5);
    auto v1 = aie::broadcast<bfloat16, 16>(k1);
    auto vs2opi = aie::broadcast<bfloat16, 16>(sqrt_2_over_pi);
    auto vBeta = aie::broadcast<bfloat16, 16>(kBeta);

    aie::vector<bfloat16, 16> x2 = aie::mul(x, x);
    aie::vector<bfloat16, 16> x3 = aie::mul(x, x2);
    aie::vector<bfloat16, 16> x3_beta = aie::mul(x3, vBeta);
    aie::vector<bfloat16, 16> inner = aie::add(x, x3_beta);
    auto inner1 = aie::mul(inner, vs2opi);
    auto tanh_out = aie::tanh<bfloat16>(inner1.to_vector<float>());
    aie::vector<bfloat16, 16> one_plus_tanh = aie::add(tanh_out, v1);
    aie::vector<bfloat16, 16> mul_v05 = aie::mul(v05, one_plus_tanh);
    return aie::mul(x, mul_v05).to_vector<bfloat16>();
}

// Out-of-place GELU: output_vector = gelu(input_vector). input and output must not alias.
void gelu_tanh_approx_bf16(bfloat16 *restrict input_vector, bfloat16 *restrict output_vector, const int32_t vector_size)
{
    event0();
    auto it_in = aie::begin_restrict_vector<16>((bfloat16 *)input_vector);
    auto it_out = aie::begin_restrict_vector<16>((bfloat16 *)output_vector);

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(1)
    for (int i = 0; i < vector_size; i += 16) {
        *it_out++ = gelu_tanh_approx_v16(*it_in++);
    }
    event1();
}

// In-place GELU: v = gelu(v). Single pointer, so aliasing-correct (each 16-lane slot is read then written).
static inline void gelu_tanh_approx_inplace_bf16(bfloat16 *restrict v, const int32_t vector_size)
{
    event0();
    auto it = aie::begin_restrict_vector<16>(v);
    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(1)
    for (int i = 0; i < vector_size; i += 16) {
        aie::vector<bfloat16, 16> x = *it;
        *it++ = gelu_tanh_approx_v16(x);
    }
    event1();
}

extern "C" {

void gelu_bf16(bfloat16 *restrict input, bfloat16 *restrict output, int input_size)
{
    gelu_tanh_approx_bf16(input, output, input_size);
}

// In-place GELU over n bf16 elements (n a multiple of 16). Intended as a fused epilogue over a compute
// tile (e.g. a GEMV output tile), applied once per tile in the producing core.
void gelu_tile_bf16(uint32_t n, bfloat16 *restrict c)
{
    gelu_tanh_approx_inplace_bf16(c, (int32_t)n);
}

} // extern "C"
