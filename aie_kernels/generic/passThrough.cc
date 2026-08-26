// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// #define __AIENGINE__ 1
#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdlib.h>

template <typename T, int N>
__attribute__((noinline)) void
passThrough_aie(T *restrict in, T *restrict out, const int32_t height, const int32_t width)
{
    event0();

    v64uint8 *restrict outPtr = (v64uint8 *)out;
    v64uint8 *restrict inPtr = (v64uint8 *)in;

    AIE_PREPARE_FOR_PIPELINING
    // No minimum trip count: the caller supplies all of height, width and N. The 6 that
    // was asserted here is false for mem_copy's 64-element bf16 tile, which runs two
    // iterations at N=32 and hangs on device.
    for (int j = 0; j < (height * width); j += N) // Nx samples per loop
    {
        *outPtr++ = *inPtr++;
    }

    event1();
}

extern "C" {

#if BIT_WIDTH == 8

void passThroughLine(uint8_t *in, uint8_t *out, int32_t lineWidth)
{
    passThrough_aie<uint8_t, 64>(in, out, 1, lineWidth);
}

void passThroughTile(uint8_t *in, uint8_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<uint8_t, 64>(in, out, tileHeight, tileWidth);
}

#elif BIT_WIDTH == 16

void passThroughLine(int16_t *in, int16_t *out, int32_t lineWidth)
{
    passThrough_aie<int16_t, 32>(in, out, 1, lineWidth);
}

void passThroughTile(int16_t *in, int16_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<int16_t, 32>(in, out, tileHeight, tileWidth);
}

#else // 32

void passThroughLine(int32_t *in, int32_t *out, int32_t lineWidth)
{
    passThrough_aie<int32_t, 16>(in, out, 1, lineWidth);
}

void passThroughTile(int32_t *in, int32_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<int32_t, 16>(in, out, tileHeight, tileWidth);
}

#endif

} // extern "C"
