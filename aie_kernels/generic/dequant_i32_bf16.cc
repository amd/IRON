// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

template <const int N, const int G> void dequant_i32_to_bf16_impl(int32_t *in, bfloat16 *out)
{
    constexpr int block_size = 16;
    constexpr int blocks_per_group = G / block_size;
    constexpr int groups_per_tile = N / G;
    static_assert((G % block_size) == 0, "GROUP_SIZE must be a multiple of 16");

    int32_t *__restrict pI = in;
    bfloat16 *__restrict pSF = (bfloat16 *)(in + N); // Scale factors after int32 data
    bfloat16 *__restrict pO = out;

    event0();
    for (int i = 0; i < groups_per_tile; i++)
        chess_prepare_for_pipelining chess_loop_range(groups_per_tile, )
        {
            bfloat16 sf = *pSF;
            pSF += 1;
            aie::vector<float, block_size> sf_f32 = aie::broadcast<float, block_size>((float)sf);

            for (int k = 0; k < blocks_per_group; k++) {
                aie::vector<int32_t, block_size> i32_vec = aie::load_v<block_size>(pI);
                pI += block_size;

                // Convert int32 -> float, scale in float32, then convert to bfloat16
                aie::vector<float, block_size> f32_vec = aie::to_float<float>(i32_vec, 0);
                aie::vector<float, block_size> scaled_f32 = aie::mul(f32_vec, sf_f32);
                aie::accum<accfloat, block_size> acc;
                acc.from_vector(scaled_f32, 0);
                aie::store_v(pO, acc.to_vector<bfloat16>());
                pO += block_size;
            }
        }
    event1();
}

extern "C" {

#ifndef GROUP_SIZE
#define GROUP_SIZE 32
#endif

#ifndef TILE_SIZE
#define TILE_SIZE 1024
#endif

void dequant_i32_to_bfloat16(int32_t *a_in, bfloat16 *c_out)
{
    dequant_i32_to_bf16_impl<TILE_SIZE, GROUP_SIZE>(a_in, c_out);
}

} // extern "C"
