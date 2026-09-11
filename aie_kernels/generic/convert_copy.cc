// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

extern "C" {
// Define a utility function to convert an f32 buffer to bf16 using the AIE API
// in a way that preserves the number of elements (which means the total size
// of the input in bits gets reduced by half)
void convert_copy_f32_to_bf16(float *restrict input_vector, bfloat16 *restrict output_vector, const int32_t vector_size)
{
    event0();
    aie::accum<accfloat, 16> acc;
    // Bound on the last full vector, remainder scalar-wise; see add.cc.
    const unsigned F = vector_size / 16;
    for (unsigned i = 0; i < F * 16; i += 16) {
        aie::vector<float, 16> input = aie::load_v<16>(input_vector + i);
        acc.from_vector(input, 0);
        aie::store_v(output_vector + i, acc.to_vector<bfloat16>());
    }
    for (unsigned i = F * 16; i < (unsigned)vector_size; i++) {
        output_vector[i] = (bfloat16)input_vector[i];
    }
    event1();
    return;
}

} // extern "C"
