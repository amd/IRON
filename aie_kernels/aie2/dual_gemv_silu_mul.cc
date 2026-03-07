// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused dual-GEMV + SiLU + elementwise multiply kernel for AIE2.
// Same structure as AIE2+ variant but uses LUT-based getTanhBf16.

#define NOCPP

#include "../aie_kernel_utils.h"
#include "lut_based_ops.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <type_traits>

static bfloat16 left_buf[2048] __attribute__((aligned(64)));
static bfloat16 right_buf[2048] __attribute__((aligned(64)));

template <uint32_t r>
void matvec_vectorized(uint32_t m,
                       uint32_t k,
                       const bfloat16 *__restrict a,
                       const bfloat16 *__restrict b,
                       bfloat16 *__restrict c)
{
    ::aie::set_rounding(aie::rounding_mode::conv_even);
    bfloat16 *c_end = c + m;
    const bfloat16 *b_end = b + k;
    for (; c < c_end; c++) {
        aie::accum acc = aie::zeros<accfloat, r>();
        AIE_LOOP_MIN_ITERATION_COUNT(2)
        for (const bfloat16 *__restrict b_cur = b; b_cur < b_end; b_cur += r, a += r) {
            aie::vector<bfloat16, r> a_vec = aie::load_v<r>(a);
            aie::vector<bfloat16, r> b_vec = aie::load_v<r>(b_cur);
            acc = aie::mac(acc, a_vec, b_vec);
        }
        *c = static_cast<bfloat16>(aie::reduce_add(acc.template to_vector<float>()));
    }
}

extern "C" {

void dual_gemv_matvec_bf16(uint32_t m,
                           uint32_t k,
                           uint32_t row_offset,
                           const bfloat16 *__restrict a_in,
                           const bfloat16 *__restrict b_in,
                           uint32_t phase)
{
    bfloat16 *dst = (phase == 0) ? left_buf : right_buf;
    dst += row_offset;
    matvec_vectorized<64>(m, k, a_in, b_in, dst);
}

void dual_gemv_silu_mul_bf16(bfloat16 *__restrict c_out, int32_t m_output)
{
    event0();

    aie::vector<bfloat16, 16> register_0_5 = aie::broadcast<bfloat16, 16>(0.5f);
    aie::vector<bfloat16, 16> register_1 = aie::broadcast<bfloat16, 16>(1.0f);
    AIE_PREPARE_FOR_PIPELINING
    for (int i = 0; i < m_output; i += 16) {
        aie::vector<bfloat16, 16> left_val = aie::load_v<16>(left_buf + i);
        aie::vector<bfloat16, 16> right_val = aie::load_v<16>(right_buf + i);

        aie::vector<bfloat16, 16> half_x = aie::mul(left_val, register_0_5);
        aie::vector<bfloat16, 16> tanh_half_x = getTanhBf16(half_x);
        auto tanh_half_x_approx = aie::add(tanh_half_x, register_1);
        aie::vector<bfloat16, 16> sigmoid_approx = aie::mul(tanh_half_x_approx, register_0_5);
        auto silu_output = aie::mul(left_val, sigmoid_approx);

        auto fused_output = aie::mul(silu_output.to_vector<bfloat16>(), right_val);
        aie::store_v(c_out + i, fused_output.to_vector<bfloat16>());
    }

    event1();
}

} // extern "C"
