// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused INT4 dequantization + GEMV kernel for AIE2+.
//
// Loads INT4-packed weights, dequantizes in-register, and performs
// matrix-vector multiplication in a single pass.
//
// Weight layout per tile (m rows x K cols, group_size G):
//   [m * K / 2 bytes of packed uint4 weights]
//   [m * (K / G) bf16 scale factors, stored as (m * K / G * 2) bytes]
//
// Dequantization: w_bf16 = scale * unpack_uint4_to_bf16(w_uint4)
//
// The unpack chain matches the existing dequant kernel (expand.cc):
//   uint4 -> uint8 (aie::unpack) -> uint16 (aie::unpack) -> bf16 (aie::to_float)

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <type_traits>

template <uint32_t block_size>
void fused_dequant_matvec(uint32_t m,
                          uint32_t k,
                          const uint8_t *__restrict a_in,
                          const bfloat16 *__restrict b_in,
                          bfloat16 *__restrict c_out,
                          uint32_t group_size)
{
    static_assert(block_size == 32, "block_size must be 32 to match dequant vector width");

    ::aie::set_rounding(aie::rounding_mode::conv_even);

    const uint4 *weights_packed = reinterpret_cast<const uint4 *>(a_in);
    const uint8_t *scale_bytes = a_in + m * k / 2;
    const bfloat16 *scales = reinterpret_cast<const bfloat16 *>(scale_bytes);

    const uint32_t groups_per_row = k / group_size;
    const uint32_t blocks_per_group = group_size / block_size;

    event0();
    for (uint32_t row = 0; row < m; row++) {
        const uint4 *row_weights = weights_packed + row * k / 2;
        const bfloat16 *row_scales = scales + row * groups_per_row;
        const bfloat16 *b_ptr = b_in;

        aie::accum<accfloat, block_size> acc = aie::zeros<accfloat, block_size>();

        for (uint32_t g = 0; g < groups_per_row; g++) {
            bfloat16 sf = row_scales[g];
            aie::vector<bfloat16, block_size> sf_broadcast = aie::broadcast<bfloat16, block_size>(sf);

            for (uint32_t blk = 0; blk < blocks_per_group; blk++) {
                aie::vector<uint4, block_size> I0 = aie::load_v<block_size>(row_weights);
                row_weights += block_size / 2;

                aie::vector<uint8, block_size> as_int8 = aie::unpack(I0);
                aie::vector<uint16, block_size> as_int16 = aie::unpack(as_int8);
                aie::vector<bfloat16, block_size> as_bf16 = aie::to_float<bfloat16>(as_int16, 0);

                aie::vector<bfloat16, block_size> w_dequant = aie::mul(as_bf16, sf_broadcast).template to_vector<bfloat16>();

                aie::vector<bfloat16, block_size> b_vec = aie::load_v<block_size>(b_ptr);
                b_ptr += block_size;

                acc = aie::mac(acc, w_dequant, b_vec);
            }
        }

        *c_out = static_cast<bfloat16>(aie::reduce_add(acc.template to_vector<float>()));
        c_out++;
    }
    event1();
}

extern "C" {

void fused_dequant_matvec_bf16(uint32_t m,
                               uint32_t k,
                               uint32_t row_offset,
                               const uint8_t *__restrict a_in,
                               const bfloat16 *__restrict b_in,
                               bfloat16 *__restrict c_out,
                               uint32_t group_size)
{
    c_out += row_offset;
    fused_dequant_matvec<32>(m, k, a_in, b_in, c_out, group_size);
}

} // extern "C"
