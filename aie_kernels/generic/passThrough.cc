// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// #define __AIENGINE__ 1
#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdlib.h>

// Pipelined selects the loop's minimum-trip-count promise. The kernel cannot prove a
// trip count from height/width/N alone -- that has to come from the caller, since
// asserting >=6 for a call that runs fewer iterations hangs on device (mem_copy's
// 64-element bf16 tile runs two at N=32). Callers that can guarantee >=6 should use
// the Pipelined=true entry points below for the software-pipelined loop.
template <typename T, int N, bool Pipelined>
__attribute__((noinline)) void
passThrough_aie(T *restrict in, T *restrict out, const int32_t height, const int32_t width)
{
    event0();

    v64uint8 *restrict outPtr = (v64uint8 *)out;
    v64uint8 *restrict inPtr = (v64uint8 *)in;

    if constexpr (Pipelined) {
        AIE_PREPARE_FOR_PIPELINING
        AIE_LOOP_MIN_ITERATION_COUNT(6)
        for (int j = 0; j < (height * width); j += N) // Nx samples per loop
        {
            *outPtr++ = *inPtr++;
        }
    } else {
        AIE_PREPARE_FOR_PIPELINING
        for (int j = 0; j < (height * width); j += N) // Nx samples per loop
        {
            *outPtr++ = *inPtr++;
        }
    }

    event1();
}

extern "C" {

#if BIT_WIDTH == 8

void passThroughLine(uint8_t *in, uint8_t *out, int32_t lineWidth)
{
    passThrough_aie<uint8_t, 64, false>(in, out, 1, lineWidth);
}

void passThroughTile(uint8_t *in, uint8_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<uint8_t, 64, false>(in, out, tileHeight, tileWidth);
}

// Trip count (height*width)/64 must be >=6, or this hangs on device.
void passThroughLinePipelined(uint8_t *in, uint8_t *out, int32_t lineWidth)
{
    passThrough_aie<uint8_t, 64, true>(in, out, 1, lineWidth);
}

void passThroughTilePipelined(uint8_t *in, uint8_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<uint8_t, 64, true>(in, out, tileHeight, tileWidth);
}

#elif BIT_WIDTH == 16

void passThroughLine(int16_t *in, int16_t *out, int32_t lineWidth)
{
    passThrough_aie<int16_t, 32, false>(in, out, 1, lineWidth);
}

void passThroughTile(int16_t *in, int16_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<int16_t, 32, false>(in, out, tileHeight, tileWidth);
}

// Trip count (height*width)/32 must be >=6, or this hangs on device.
void passThroughLinePipelined(int16_t *in, int16_t *out, int32_t lineWidth)
{
    passThrough_aie<int16_t, 32, true>(in, out, 1, lineWidth);
}

void passThroughTilePipelined(int16_t *in, int16_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<int16_t, 32, true>(in, out, tileHeight, tileWidth);
}

#else // 32

void passThroughLine(int32_t *in, int32_t *out, int32_t lineWidth)
{
    passThrough_aie<int32_t, 16, false>(in, out, 1, lineWidth);
}

void passThroughTile(int32_t *in, int32_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<int32_t, 16, false>(in, out, tileHeight, tileWidth);
}

// Trip count (height*width)/16 must be >=6, or this hangs on device.
void passThroughLinePipelined(int32_t *in, int32_t *out, int32_t lineWidth)
{
    passThrough_aie<int32_t, 16, true>(in, out, 1, lineWidth);
}

void passThroughTilePipelined(int32_t *in, int32_t *out, int32_t tileHeight, int32_t tileWidth)
{
    passThrough_aie<int32_t, 16, true>(in, out, tileHeight, tileWidth);
}

#endif

} // extern "C"
