// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

template <const int N, const int G> void quantize_bf16_to_i8_impl(bfloat16 *in, int8_t *out)
{
    constexpr int block_size = 16;
    constexpr int blocks_per_group = G / block_size;
    constexpr int groups_per_tile = N / G;
    static_assert((G % block_size) == 0, "GROUP_SIZE must be a multiple of 16");

    bfloat16 *__restrict pI = in;
    int8_t *__restrict pO = out;
    // Scale factors stored after int8 data. N is always a multiple of group_size (>= 16),
    // so out + N is guaranteed to be 2-byte aligned for bfloat16 access.
    bfloat16 *__restrict pSF = (bfloat16 *)(out + N);

    event0();
    for (int i = 0; i < groups_per_tile; i++)
        chess_prepare_for_pipelining chess_loop_range(groups_per_tile, )
        {
            // Pass 1: Find max absolute value in this group
            float max_abs = 0.0f;
            bfloat16 *pScan = pI;
            for (int k = 0; k < blocks_per_group; k++) {
                aie::vector<bfloat16, block_size> bf16_vec = aie::load_v<block_size>(pScan);
                pScan += block_size;
                aie::vector<bfloat16, block_size> abs_vec = aie::abs(bf16_vec);
                float block_max = (float)aie::reduce_max(abs_vec);
                if (block_max > max_abs)
                    max_abs = block_max;
            }

            // Compute scale factor and inverse scale
            float inv_scale;
            if (max_abs > 0.0f) {
                inv_scale = ::aie::div(127.0f, max_abs);
                *pSF = (bfloat16)::aie::div(max_abs, 127.0f);
            } else {
                inv_scale = 0.0f;
                *pSF = (bfloat16)0.0f;
            }
            pSF += 1;

            // Pass 2: Quantize values
            aie::vector<float, block_size> inv_scale_vec = aie::broadcast<float, block_size>(inv_scale);
            for (int k = 0; k < blocks_per_group; k++) {
                aie::vector<bfloat16, block_size> bf16_vec = aie::load_v<block_size>(pI);
                pI += block_size;

                // Convert bf16 -> float, scale, round, saturate to int8
                aie::accum<accfloat, block_size> acc;
                acc.from_vector(bf16_vec, 0);
                aie::vector<float, block_size> f32_vec = acc.to_vector<float>();
                aie::vector<float, block_size> scaled = aie::mul(f32_vec, inv_scale_vec);

                // Round to nearest (half-away-from-zero) and saturate to [-128, 127]
                // TODO: vectorize with aie::to_fixed when available for int8 targets
                for (int e = 0; e < block_size; e++) {
                    float val = scaled[e];
                    int32_t rounded;
                    if (val >= 0.0f)
                        rounded = (int32_t)(val + 0.5f);
                    else
                        rounded = (int32_t)(val - 0.5f);
                    if (rounded > 127)
                        rounded = 127;
                    else if (rounded < -128)
                        rounded = -128;
                    pO[e] = (int8_t)rounded;
                }
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

void quantize_bfloat16_to_i8(bfloat16 *a_in, int8_t *c_out)
{
    quantize_bf16_to_i8_impl<TILE_SIZE, GROUP_SIZE>(a_in, c_out);
}

} // extern "C"
