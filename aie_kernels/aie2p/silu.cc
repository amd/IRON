// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

template <int N>
static inline aie::vector<bfloat16, N> silu_vec(aie::vector<bfloat16, N> input)
{
    auto half_x = aie::mul(input, aie::broadcast<bfloat16, N>(0.5f));
    auto tanh_half_x = aie::tanh<bfloat16>(half_x.template to_vector<float>());
    auto sigmoid = aie::mul(
        aie::add(tanh_half_x, aie::broadcast<bfloat16, N>(1.0f)),
        aie::broadcast<bfloat16, N>(0.5f)
    ).template to_vector<bfloat16>();
    return aie::mul(input, sigmoid).template to_vector<bfloat16>();
}

extern "C" {

void silu_bf16(bfloat16 *restrict input_vector, bfloat16 *restrict output_vector, int vector_size)
{
    event0();

    int num_elems = vector_size;
    auto it_in = aie::begin_restrict_vector<32>((bfloat16 *)input_vector);
    auto it_out = aie::begin_restrict_vector<32>((bfloat16 *)output_vector);

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(4)
    for (int i = 0; i < num_elems; i += 32) {
        auto input = *it_in++;
        auto output = silu_vec<32>(input);
        *it_out++ = output;
    }

    event1();
}

void swiglu_bf16(
    bfloat16 *restrict input,
    bfloat16 *restrict output,
    int rows,
    int cols,
    int row_tile_size
)
{
    event0();

    const int row_block_size = row_tile_size * cols;
    auto it_in = input;
    auto it_out = output;

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(4)
    for (int row_block_start = 0; row_block_start < rows; row_block_start += row_tile_size) {
        auto gate_it = aie::begin_restrict_vector<32>(it_in);
        auto up_it = aie::begin_restrict_vector<32>(it_in + row_block_size);
        auto output_it = aie::begin_restrict_vector<32>(it_out);

        for (int vector_offset = 0; vector_offset < row_block_size; vector_offset += 32) {
            auto gate = *gate_it++;
            auto up = *up_it++;
            auto result = aie::mul(silu_vec<32>(gate), up);
            *output_it++ = result.to_vector<bfloat16>();
        }

        it_in += 2 * row_block_size;
        it_out += row_block_size;
    }

    event1();
}

} // extern "C"
