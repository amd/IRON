// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"
#include "lut_based_ops.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

// GELU (tanh approximation): 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3))).
// Same MAC-fused structure as the aie2p kernel, but tanh uses the LUT-based
// implementation (aie2 has no native bf16 tanh):
//   inner1 = s*x + s_beta*x*x^2  (single MAC, instead of mul+add+mul)
//   result = mac(0.5x, tanh, 0.5x)  (single MAC, instead of add+mul+mul)
static inline aie::vector<bfloat16, 32> gelu_tanh_approx(aie::vector<bfloat16, 32> x)
{
    const bfloat16 k0_5 = 0.5f;
    const bfloat16 sqrt_2_over_pi = 0.79788456f;        // sqrt(2/pi)
    const bfloat16 s_beta = sqrt_2_over_pi * 0.044715f; // precomputed s*beta

    auto v05 = aie::broadcast<bfloat16, 32>(k0_5);
    auto vs2opi = aie::broadcast<bfloat16, 32>(sqrt_2_over_pi);
    auto vsBeta = aie::broadcast<bfloat16, 32>(s_beta);

    aie::vector<bfloat16, 32> x2 = aie::mul(x, x).to_vector<bfloat16>();
    aie::vector<bfloat16, 32> sbeta_x = aie::mul(x, vsBeta).to_vector<bfloat16>();
    auto sx = aie::mul(x, vs2opi);
    auto half_x = aie::mul(x, v05);

    aie::vector<bfloat16, 32> inner1 = aie::mac(sx, sbeta_x, x2).to_vector<bfloat16>();

    // LUT-based tanh: split to 16-wide halves
    aie::vector<bfloat16, 16> tanh_lo = getTanhBf16(inner1.extract<16>(0));
    aie::vector<bfloat16, 16> tanh_hi = getTanhBf16(inner1.extract<16>(1));
    aie::vector<bfloat16, 32> tanh_out = aie::concat(tanh_lo, tanh_hi);

    return aie::mac(half_x, tanh_out, half_x.to_vector<bfloat16>()).to_vector<bfloat16>();
}

void gelu_tanh_approx_bf16(bfloat16 *restrict input_vector, bfloat16 *restrict output_vector, const int32_t vector_size)
{
    event0();

    auto it_in = aie::begin_restrict_vector<32>((bfloat16 *)input_vector);
    auto it_out = aie::begin_restrict_vector<32>((bfloat16 *)output_vector);

    // AIE_PREPARE_FOR_POSTPIPELINING kept for parity with the aie2p kernel. On aie2
    // neither pipeliner finds a schedule (LUT tanh register pressure), but the
    // MAC-fused body still reduces II from 129 to 87 cycles per 32 elements.
    auto body = [&]() __attribute__((always_inline))
    {
        *it_out++ = gelu_tanh_approx(*it_in++);
    };
    VERSIONED_LOOP(2, (vector_size + 31) / 32, body, AIE_PREPARE_FOR_POSTPIPELINING);

    event1();

    return;
}

extern "C" {

void gelu_bf16(bfloat16 *restrict input, bfloat16 *restrict output, int input_size)
{
    gelu_tanh_approx_bf16(input, output, input_size);
}

} // extern "C"
