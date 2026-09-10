// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// mm_fused's output stage: convert one chunk of the f32 accumulator into a bf16
// output object the core body has already acquired from the C ObjectFifo,
// optionally applying an activation and a clamp on the way out.
//
// Fusing the activation here is the point: the values are already in registers
// after the f32 -> bf16 conversion, so gelu/silu/sigmoid costs one more vector
// op per 16 elements instead of a separate pass over L1 (which is what chaining
// a standalone activation operator after a GEMM would cost).
//
// The mode and clamp are compile-time, so every instantiation of this kernel
// has a branch-free inner loop. That differs from the design this was ported
// from, where one overlay served every activation and had to test a runtime
// mode word per chunk.
//
// This is a separate translation unit from mm_fused.cc so it can be built with
// its own flags and, if the per-call overhead ever shows up in a trace, be
// switched to an inlined LLVM-IR kernel independently of the much larger mmul.
#include "../aie_kernel_utils.h"
#include "activations.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

#if !defined(MM_FUSED_OUT_CHUNK) || !defined(MM_FUSED_C_DEPTH)
#error "design.py must pass -DMM_FUSED_OUT_CHUNK / -DMM_FUSED_C_DEPTH"
#endif

// 0 = none, 1 = gelu, 2 = silu, 3 = sigmoid
#ifndef MM_FUSED_EPILOGUE_MODE
#define MM_FUSED_EPILOGUE_MODE 0
#endif
#ifndef MM_FUSED_CLAMP
#define MM_FUSED_CLAMP 0
#endif
#ifndef MM_FUSED_CLAMP_MIN
#define MM_FUSED_CLAMP_MIN 0.0f
#endif
#ifndef MM_FUSED_CLAMP_MAX
#define MM_FUSED_CLAMP_MAX 0.0f
#endif

namespace
{
constexpr int CHUNK = MM_FUSED_OUT_CHUNK;
constexpr int DEPTH = MM_FUSED_C_DEPTH;
constexpr int V = 16; // one 512-bit bf16 vector
static_assert(CHUNK % V == 0, "output chunk must be a whole number of vectors");
} // namespace

extern "C" {

// Chunk (outer * DEPTH + half) of the accumulator -> one C object.
//
// The chunk index is split in two because the core body unrolls the drain by
// the C fifo depth to keep the acquired buffer index a compile-time constant;
// passing both parts avoids doing that arithmetic up there.
void mm_fused_epilogue_chunk(bfloat16 *y_out, float *y_acc, int32_t outer, int32_t half)
{
    // The f32 -> bf16 store below is a conversion, so it depends on the rounding
    // mode just as the mmul does, and must agree with it. Same flag, same
    // polarity: see mm_fused.cc.
#ifdef ROUND_CONV_EVEN
    ::aie::set_rounding(aie::rounding_mode::conv_even);
#else
    ::aie::set_rounding(aie::rounding_mode::floor);
#endif
    const float *__restrict src = y_acc + (outer * DEPTH + half) * CHUNK;

#if MM_FUSED_CLAMP
    const aie::vector<bfloat16, V> lo = aie::broadcast<bfloat16, V>(static_cast<bfloat16>(MM_FUSED_CLAMP_MIN));
    const aie::vector<bfloat16, V> hi = aie::broadcast<bfloat16, V>(static_cast<bfloat16>(MM_FUSED_CLAMP_MAX));
#endif

    AIE_LOOP_MAX_ITERATION_COUNT(CHUNK / V)
    for (int j = 0; j < CHUNK / V; j++) {
        aie::accum<accfloat, V> acc;
        acc.from_vector(aie::load_v<V>(src + j * V));
        // The assignment is the conversion: to_v16bfloat16 yields a raw
        // v16bfloat16, not an aie::vector.
        aie::vector<bfloat16, V> v = to_v16bfloat16(acc);
#if MM_FUSED_EPILOGUE_MODE == 1
        v = gelu_vec<V>(v);
#elif MM_FUSED_EPILOGUE_MODE == 2
        v = silu_vec<V>(v);
#elif MM_FUSED_EPILOGUE_MODE == 3
        v = sigmoid_vec<V>(v);
#endif
#if MM_FUSED_CLAMP
        v = aie::clamp(v, lo, hi);
#endif
        aie::store_v(y_out + j * V, v);
    }
}
}
