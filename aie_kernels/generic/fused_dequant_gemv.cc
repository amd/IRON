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
//
// Optimization: double-pump — process 2 groups (64 elements) per iteration
// so the compiler can interleave the two independent unpack chains, hiding
// the dequant latency behind computation.

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <type_traits>

// Dequant one 32-element block: load uint4 → unpack → scale → return bf16
template <uint32_t block_size>
inline __attribute__((always_inline)) aie::vector<bfloat16, block_size>
dequant_block(const uint4 *&weights, const bfloat16 *&b_ptr,
              aie::vector<bfloat16, block_size> sf_broadcast,
              aie::accum<accfloat, block_size> &acc) {
    aie::vector<uint4, block_size> I0 = aie::load_v<block_size>(weights);
    weights += block_size / 2;

    aie::vector<uint8, block_size> as_int8 = aie::unpack(I0);
    aie::vector<uint16, block_size> as_int16 = aie::unpack(as_int8);
    aie::vector<bfloat16, block_size> as_bf16 = aie::to_float<bfloat16>(as_int16, 0);
    aie::vector<bfloat16, block_size> w_dequant =
        aie::mul(as_bf16, sf_broadcast).template to_vector<bfloat16>();

    aie::vector<bfloat16, block_size> b_vec = aie::load_v<block_size>(b_ptr);
    b_ptr += block_size;

    acc = aie::mac(acc, w_dequant, b_vec);
    return w_dequant;
}

// block_size: dequant vector width (must be 32 for aie::unpack)
// G: group size (compile-time for pipelining, must be multiple of block_size)
// DK: K dimension (compile-time for loop count optimization)
template <uint32_t block_size, uint32_t G, uint32_t DK>
void fused_dequant_matvec(uint32_t m,
                          const uint8_t *__restrict a_in,
                          const bfloat16 *__restrict b_in,
                          bfloat16 *__restrict c_out)
{
    static_assert(block_size == 32, "block_size must be 32 to match dequant vector width");
    static_assert(G % block_size == 0, "group_size must be a multiple of block_size");
    constexpr uint32_t blocks_per_group = G / block_size;
    constexpr uint32_t groups_per_row = DK / G;
    // For double-pump: process 2 groups per iteration when possible
    constexpr bool can_double_pump = (groups_per_row >= 2) && (groups_per_row % 2 == 0);
    constexpr uint32_t pump_groups = can_double_pump ? 2 : 1;
    constexpr uint32_t loop_iters = groups_per_row / pump_groups;

    ::aie::set_rounding(aie::rounding_mode::conv_even);

    const uint4 *weights_packed = reinterpret_cast<const uint4 *>(a_in);
    const uint8_t *scale_bytes = a_in + m * DK / 2;
    const bfloat16 *scales = reinterpret_cast<const bfloat16 *>(scale_bytes);

    event0();
    for (uint32_t row = 0; row < m; row++) {
        const uint4 *row_weights = weights_packed + row * DK / 2;
        const bfloat16 *row_scales = scales + row * groups_per_row;
        const bfloat16 *b_ptr = b_in;

        aie::accum<accfloat, block_size> acc = aie::zeros<accfloat, block_size>();

        if constexpr (can_double_pump && blocks_per_group == 1) {
            // Optimized path: 2 groups per iteration, 1 block per group
            // Two independent unpack chains for the compiler to interleave.
            AIE_LOOP_MIN_ITERATION_COUNT(loop_iters)
            for (uint32_t g = 0; g < groups_per_row; g += 2)
                chess_prepare_for_pipelining
            {
                // --- Chain A: group g ---
                bfloat16 sf_a = row_scales[g];
                aie::vector<bfloat16, block_size> sf_a_bc =
                    aie::broadcast<bfloat16, block_size>(sf_a);

                aie::vector<uint4, block_size> I0_a = aie::load_v<block_size>(row_weights);
                row_weights += block_size / 2;

                // --- Chain B: group g+1 (interleaved) ---
                bfloat16 sf_b = row_scales[g + 1];
                aie::vector<bfloat16, block_size> sf_b_bc =
                    aie::broadcast<bfloat16, block_size>(sf_b);

                aie::vector<uint4, block_size> I0_b = aie::load_v<block_size>(row_weights);
                row_weights += block_size / 2;

                // Unpack chain A
                aie::vector<uint8, block_size> a8_a = aie::unpack(I0_a);
                aie::vector<uint16, block_size> a16_a = aie::unpack(a8_a);
                aie::vector<bfloat16, block_size> abf_a = aie::to_float<bfloat16>(a16_a, 0);
                aie::vector<bfloat16, block_size> w_a =
                    aie::mul(abf_a, sf_a_bc).template to_vector<bfloat16>();

                // Unpack chain B
                aie::vector<uint8, block_size> a8_b = aie::unpack(I0_b);
                aie::vector<uint16, block_size> a16_b = aie::unpack(a8_b);
                aie::vector<bfloat16, block_size> abf_b = aie::to_float<bfloat16>(a16_b, 0);
                aie::vector<bfloat16, block_size> w_b =
                    aie::mul(abf_b, sf_b_bc).template to_vector<bfloat16>();

                // Load activation vectors and MAC
                aie::vector<bfloat16, block_size> b_a = aie::load_v<block_size>(b_ptr);
                b_ptr += block_size;
                acc = aie::mac(acc, w_a, b_a);

                aie::vector<bfloat16, block_size> b_b = aie::load_v<block_size>(b_ptr);
                b_ptr += block_size;
                acc = aie::mac(acc, w_b, b_b);
            }
        } else {
            // Generic path: 1 group per iteration
            AIE_LOOP_MIN_ITERATION_COUNT(loop_iters)
            for (uint32_t g = 0; g < groups_per_row; g++)
                chess_prepare_for_pipelining
            {
                bfloat16 sf = row_scales[g];
                aie::vector<bfloat16, block_size> sf_broadcast =
                    aie::broadcast<bfloat16, block_size>(sf);

                AIE_LOOP_MIN_ITERATION_COUNT(blocks_per_group)
                for (uint32_t blk = 0; blk < blocks_per_group; blk++) {
                    aie::vector<uint4, block_size> I0 = aie::load_v<block_size>(row_weights);
                    row_weights += block_size / 2;

                    aie::vector<uint8, block_size> as_int8 = aie::unpack(I0);
                    aie::vector<uint16, block_size> as_int16 = aie::unpack(as_int8);
                    aie::vector<bfloat16, block_size> as_bf16 =
                        aie::to_float<bfloat16>(as_int16, 0);
                    aie::vector<bfloat16, block_size> w_dequant =
                        aie::mul(as_bf16, sf_broadcast).template to_vector<bfloat16>();

                    aie::vector<bfloat16, block_size> b_vec = aie::load_v<block_size>(b_ptr);
                    b_ptr += block_size;

                    acc = aie::mac(acc, w_dequant, b_vec);
                }
            }
        }

        *c_out = static_cast<bfloat16>(aie::reduce_add(acc.template to_vector<float>()));
        c_out++;
    }
    event1();
}

#ifndef GROUP_SIZE
#define GROUP_SIZE 32
#endif

#ifndef DIM_K
#define DIM_K 2048
#endif

extern "C" {

void fused_dequant_matvec_bf16(uint32_t m,
                               uint32_t row_offset,
                               const uint8_t *__restrict a_in,
                               const bfloat16 *__restrict b_in,
                               bfloat16 *__restrict c_out)
{
    c_out += row_offset;
    fused_dequant_matvec<32, GROUP_SIZE, DIM_K>(m, a_in, b_in, c_out);
}

} // extern "C"
