// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// int8-weight GEMV with IN-KERNEL dequantization (W8A16, AIE2P).
//
// The weight stream packs, per m-row tile: [ m*K int8 weights | m*G bf16
// scales ] (the (M, K/G) scale table rows ride with their weight rows).  The
// kernel streams the tile once, dequantizes in registers (int8 -> bf16 *
// group scale) and feeds the standard bf16 mac pipeline — dequantized weights
// NEVER touch DRAM, which is what makes quantization actually cut DRAM
// traffic (vs a standalone dequant op writing bf16 weights back out).
//
// Host-side preparation (gemv_int8 host packing):
//   - checkpoint qweight (K/4, M) int32, 4 int8 per int32 little-endian along
//     K, symmetric zero-point 127 already subtracted -> plain int8 (M, K)
//   - scales (G, M) fp16 -> transpose to (M, G) and convert to bf16
//   - tile payload: for each row-block of m rows: m*K int8 then m*G bf16
//
// Dequant formula: w[m,k] = (int8(a_q[m,k]) + 128 - 128) * a_scl[m, k/G]
// with the scale PRE-multiplied into x (xs = s*x, one mul per x element
// instead of one per weight): y[m] = sum (u8-128)*s*x = sum (u8-128)*xs.
// The u8 payload stores q+128 (centered via the +(-128) vector add here).
//
// NOTE: experimental variants (mode 7-23: legacy chains, f32 pipeline,
// two-phase TileFuse-style, corr) lived in this file behind #if DEQUANT_MODE
// until 2026-09-01; they caused a silent build-pollution incident (f352a9)
// and now live in their own files / the TileFuse-port study instead:
//   - two-stage construct study: ../tilefuse_mix_int8.cc (verbatim port) +
//     ../mv_int8_2stage.cc (decode-shape two-stage variant)
//   - docs/notes/2026-09-01-residual-fusion-battle.md

#define NOCPP

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>

#ifndef VEC_SIZE
#define VEC_SIZE 64
#endif

#ifndef GROUP_SIZE
#define GROUP_SIZE 128
#endif

constexpr int BLOCK = GROUP_SIZE;

/*
 * int8-weight matvec, in-kernel dequant (premul form).
 *  m:    number of output rows for THIS tile (m_input of the L1 W-tile)
 *  k:    K extent (multiple of BLOCK)
 *  a_q:  tile payload: [m*k int8 weights][m*(k/BLOCK) bf16 scales]
 *  b:    (k,) bf16 input vector
 *  c:    (m,) bf16 output
 */
void matvec_vectorized_int8(uint32_t m,
                            uint32_t k,
                            const bfloat16 *__restrict a_tile,
                            const bfloat16 *__restrict b,
                            bfloat16 *__restrict c)
{
    ::aie::set_rounding(aie::rounding_mode::conv_even);
    const int n_groups = k / BLOCK;
    const int8_t *__restrict a_q = (const int8_t *)a_tile;             // m*k bytes, int8 verbatim
    const bfloat16 *__restrict a_scl = a_tile + (size_t)m * k / 2;      // m*(k/BLOCK) bf16

    const aie::vector<bfloat16, VEC_SIZE> bias128 =
        aie::broadcast<bfloat16, VEC_SIZE>((bfloat16)-128.0f);

    // premul xs (= s*x) + vector add(-128) on the w side:
    // y = sum (u8-128)*s*x = sum (u8-128)*xs.  One mul per x element instead
    // of one per weight (the legacy 6-level per-weight RAW chain
    // load->unpack->to_float->add->mul->mac was latency-bound).
    for (uint32_t row = 0; row < m; row++) {
        const int8_t *__restrict arow = a_q + (size_t)row * k;
        const bfloat16 *__restrict srow = a_scl + (size_t)row * n_groups;
        aie::accum acc = aie::zeros<accfloat, VEC_SIZE>();
        for (int g = 0; g < n_groups; g++) {
            aie::vector<bfloat16, VEC_SIZE> s_vec =
                aie::broadcast<bfloat16, VEC_SIZE>(srow[g]);
            const int8_t *__restrict ablk = arow + (size_t)g * BLOCK;
            const bfloat16 *__restrict bblk = b + (size_t)g * BLOCK;
            for (int i = 0; i < BLOCK; i += VEC_SIZE) {
                aie::vector<bfloat16, VEC_SIZE> b_vec =
                    aie::load_v<VEC_SIZE>(bblk + i);
                aie::vector<bfloat16, VEC_SIZE> xs =
                    aie::mul(b_vec, s_vec).template to_vector<bfloat16>();
                // SIGNED payload: the -128 bias (and therefore the per-weight vector add) is
                // gone -- 2 ops per block instead of 3 (to_float -> mac).
                aie::vector<int8_t, VEC_SIZE> q = aie::load_v<VEC_SIZE>(ablk + i);
                aie::vector<bfloat16, VEC_SIZE> w = aie::to_float<bfloat16>(q);
                acc = aie::mac(acc, w, xs);
            }
        }
        c[row] = static_cast<bfloat16>(aie::reduce_add(acc.template to_vector<float>()));
    }
}

extern "C" {

void matvec_vectorized_int8_bf16(uint32_t m,
                                 uint32_t row_offset,
                                 const bfloat16 *__restrict a_tile,
                                 const bfloat16 *__restrict b_in,
                                 bfloat16 *__restrict c_out)
{
    c_out += row_offset;
    matvec_vectorized_int8(m, DIM_K, a_tile, b_in, c_out);
}

} // extern "C"
