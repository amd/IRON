// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// bf16 GEMM compute kernel. Each compute tile owns an m x n slice of C and
// accumulates over K into an f32 accumulator that stays in L1.
//
//   mm_fused_acc_init        zero the accumulator, once per output tile
//   mm_fused_k_step          multiply one A band by one B chunk into it
//   mm_fused_epilogue_chunk  drain one chunk of it to a bf16 C object
//
// The loop nest is in design.py, not here, so every level has an ObjectFifo
// acquire point. Tile geometry arrives from there as -D flags.
#include "../aie_kernel_utils.h"
#include "activations.h"
#include "mm_fused_mmul.h"
#include "zero.cc"

#include <aie_api/aie.hpp>
#include <stdint.h>

#if !defined(MM_FUSED_TILE_M) || !defined(MM_FUSED_TILE_K) || !defined(MM_FUSED_TILE_N) || !defined(MM_FUSED_CT_K)
#error "design.py must pass -DMM_FUSED_TILE_M / _TILE_K / _TILE_N / _CT_K"
#endif
#if !defined(MM_FUSED_OUT_CHUNK) || !defined(MM_FUSED_C_DEPTH)
#error "design.py must pass -DMM_FUSED_OUT_CHUNK / -DMM_FUSED_C_DEPTH"
#endif

// Epilogue selection. 0 = none, 1 = gelu, 2 = silu, 3 = sigmoid, matching
// Epilogue.mode in design.py.
#ifndef MM_FUSED_EPILOGUE_MODE_MASK
#define MM_FUSED_EPILOGUE_MODE_MASK 0xF
#endif

namespace
{
constexpr int M = MM_FUSED_TILE_M;
// Asymmetric tile buffering: A spans MA rows and the accumulator M, so the
// core folds RHO = M / MA A bands into one C tile before releasing it. A dies
// on consumption while C lives across the K reduction, so sizing both to M
// would pay the peak L1 cost twice. MA == M is the symmetric case.
//
// From arXiv:2511.16041, "Can Asymmetric Tile Buffering Be Beneficial?";
// reference AIE implementation in Xilinx/mlir-aie PR #3076. Those configs
// accumulate in bf16/bfp16, affording larger C tiles; this one keeps an f32
// accumulator, so the freed L1 buys a deeper k slice instead.
constexpr int MA = MM_FUSED_TILE_MA;
constexpr int K = MM_FUSED_TILE_K;
constexpr int N = MM_FUSED_TILE_N;
// Register tiling, and how much of K a tile holds at a time. Both are
// design.py's to choose; CT_K trades against the n width for a fixed budget.
constexpr int R = MM_FUSED_R;
constexpr int S = MM_FUSED_S;
constexpr int T = MM_FUSED_T;
constexpr int CT_K = MM_FUSED_CT_K;

// Output stage geometry.
constexpr int CHUNK = MM_FUSED_OUT_CHUNK;
constexpr int C_DEPTH = MM_FUSED_C_DEPTH;
constexpr int V = 16; // one 512-bit bf16 vector
static_assert(CHUNK % V == 0, "output chunk must be a whole number of vectors");

// Same divisibility conditions mm.cc asserts for its own 2x2 mmul, plus the
// two the k blocking adds.
static_assert(M % MA == 0, "tile_m must be a whole number of A bands");
static_assert(MA % (2 * R) == 0, "tile_ma must be a multiple of 2*r (2x2 mmul)");
static_assert(N % (2 * T) == 0, "tile_n must be a multiple of 2*t (2x2 mmul)");
static_assert(K % CT_K == 0, "tile_k must be a multiple of the k slice");
static_assert(CT_K % S == 0, "k slice must be a multiple of s");

// The core powers up in rounding_mode::floor, so a converting kernel must
// choose explicitly. Truncation biases every conversion the same direction, so
// the error accumulates over the K reduction: ~1% of the result against ~0.02%
// for round-to-nearest-even, far more than the bfp16 emulation costs. Flag
// name and polarity follow mm.cc.
#ifdef ROUND_CONV_EVEN
constexpr aie::rounding_mode round_mode = aie::rounding_mode::conv_even;
#else
constexpr aie::rounding_mode round_mode = aie::rounding_mode::floor;
#endif
// One activation's inner loop. Templated so each mode compiles branch-free;
// mm_fused_epilogue_chunk selects between them once per chunk.
//
// The clamp is unconditional. An unclamped caller sends (-inf, +inf), which
// leaves every finite value bit-identical, so there is no unclamped
// instantiation to compile and no clamped-versus-not fork in the build.
template <int MODE>
static inline void
epilogue_body(bfloat16 *__restrict y_out, const float *__restrict src, float clamp_min, float clamp_max)
{
    const aie::vector<float, V> lo = aie::broadcast<float, V>(clamp_min);
    const aie::vector<float, V> hi = aie::broadcast<float, V>(clamp_max);

    AIE_LOOP_MAX_ITERATION_COUNT(CHUNK / V)
    for (int j = 0; j < CHUNK / V; j++) {
        // f32 through the activation and clamp, converted exactly once on the
        // store. Converting first would round twice and let the activation's
        // slope amplify the first rounding.
        aie::vector<float, V> f = aie::load_v<V>(src + j * V);
        if constexpr (MODE == 1)
            f = gelu_vec<V>(f);
        else if constexpr (MODE == 2)
            f = silu_vec<V>(f);
        else if constexpr (MODE == 3)
            f = sigmoid_vec<V>(f);
        f = aie::max(aie::min(f, hi), lo);
        aie::accum<accfloat, V> out;
        out.from_vector(f);
        // The assignment is the conversion: to_v16bfloat16 yields a raw
        // v16bfloat16, not an aie::vector.
        aie::vector<bfloat16, V> v = to_v16bfloat16(out);
        aie::store_v(y_out + j * V, v);
    }
}
} // namespace

extern "C" {

// Zero the f32 accumulator before the k loop accumulates into it. A bias is
// deliberately unsupported: initialising from one would consume an extra
// object through the B fifo's handshake, desynchronising it into a hang.
void mm_fused_acc_init(float *y_acc)
{
    // zero_vectorized brackets itself in event0/event1 for tracing.
    zero_vectorized<float, M, N>(y_acc);
}

// One step of the k loop: one B chunk against one A band, into y_acc.
//
// Takes no locks -- the A and B fifos own the handshake, so the core body
// acquires around this call. mm_fused_b_elem_t is bfp16ebs8 or bfloat16
// depending on the architecture, but the signature is the same either way.
void mm_fused_k_step(bfloat16 *a_buf, mm_fused_b_elem_t *b_buf, float *y_acc, int32_t band)
{
    ::aie::set_rounding(round_mode);
    // The accumulator is [row-block][col-block][r*t], so band b starts at
    // b * MA * N -- b*(MA/R) row-blocks in, each colB*(r*t) wide.
    mm_fused_mmul_2x2<(MA / R), (CT_K / S), (N / T), R, S, T>(a_buf, b_buf, y_acc + band * (MA * N));
}

// Convert chunk (outer * C_DEPTH + half) of the f32 accumulator into a bf16 C
// object the core body already acquired, applying an activation and clamp on
// the way out. Fusing them costs one more vector op per 16 elements instead of
// a separate pass over L1.
//
// The mode is runtime, tested once per chunk so the inner loops stay
// branch-free; the cost is program memory, since every mode in the mask is
// compiled in. The bounds arrive as raw int32 because npu_write_rtp only
// writes i32 words, and the chunk index comes in two parts because the core
// body unrolls the drain.
void mm_fused_epilogue_chunk(bfloat16 *y_out,
                             float *y_acc,
                             int32_t outer,
                             int32_t half,
                             int32_t mode,
                             int32_t clamp_min_bits,
                             int32_t clamp_max_bits)
{
    // The store below is a conversion, so it obeys the same rounding mode the
    // mmul does and must agree with it.
    ::aie::set_rounding(round_mode);
    const float *__restrict src = y_acc + (outer * C_DEPTH + half) * CHUNK;
    // __builtin_bit_cast, not memcpy: memcpy leaves an unresolved external
    // call here rather than folding to a register move.
    const float clamp_min = __builtin_bit_cast(float, clamp_min_bits);
    const float clamp_max = __builtin_bit_cast(float, clamp_max_bits);

    switch (mode) {
#if MM_FUSED_EPILOGUE_MODE_MASK & 2
    case 1:
        epilogue_body<1>(y_out, src, clamp_min, clamp_max);
        return;
#endif
#if MM_FUSED_EPILOGUE_MODE_MASK & 4
    case 2:
        epilogue_body<2>(y_out, src, clamp_min, clamp_max);
        return;
#endif
#if MM_FUSED_EPILOGUE_MODE_MASK & 8
    case 3:
        epilogue_body<3>(y_out, src, clamp_min, clamp_max);
        return;
#endif
    // Mode 0 is always compiled, so a mode the mask leaves out yields an
    // unactivated result rather than an unwritten buffer. op.py rejects that
    // combination up front; this is the backstop.
    default:
        epilogue_body<0>(y_out, src, clamp_min, clamp_max);
        return;
    }
}
}
