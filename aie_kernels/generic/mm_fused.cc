// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// bf16 GEMM compute kernel. Each compute tile owns an m x n slice of C and
// accumulates over K into an f32 accumulator that stays in L1 for the whole
// reduction.
//
// Three entry points, each called once per iteration of a loop nest that lives
// in the design (iron/operators/flm/gemm/design.py) rather than here:
//
//   mm_fused_acc_init        zero the accumulator, once per output tile
//   mm_fused_k_step          multiply one A band by one B chunk into it
//   mm_fused_epilogue_chunk  drain one chunk of it to a bf16 C object
//
// The nest lives in the design so that every level of it has an ObjectFifo
// acquire point, a fifo consumer having to acquire once per object.
//
// Tile geometry arrives as -D flags from design.py, which is the single source
// of truth for it: the same constants size the design's buffers and set its
// unroll factors.
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
constexpr int M = MM_FUSED_TILE_M;
// Asymmetric tile buffering: the A tile spans MA rows while the accumulator
// spans M, so the core folds RHO = M / MA A bands into one C tile before
// releasing it. A dies as soon as it is consumed while C must live across the
// whole K reduction, so sizing both to M would pay the peak L1 cost twice.
// MA == M is the symmetric case.
//
// Technique from "Can Asymmetric Tile Buffering Be Beneficial?", C. Wang,
// W. Pang, X. Wu, G. Jun, L. Romero, E. Taka, D. Marculescu, T. Nowatzki,
// P. Vasireddy, J. Melber, D. Chen, J. Cong, arXiv:2511.16041 (2025),
// https://arxiv.org/abs/2511.16041. Reference AIE implementation is
// Xilinx/mlir-aie PR #3076 by @ChengyueWang, in
// programming_examples/ml/block_datatypes/gemm_asymmetric_tile_buffering.
// Those configs accumulate in bf16/bfp16, which is what affords their larger C
// tiles; this kernel keeps an f32 accumulator, so here the win comes from
// spending the freed L1 on a deeper k slice rather than on a wider C tile.
constexpr int MA = MM_FUSED_TILE_MA;
constexpr int K = MM_FUSED_TILE_K;
constexpr int N = MM_FUSED_TILE_N;
// Register tiling, and how much of K one compute tile holds at a time. Both are
// design.py's to choose -- CT_K in particular trades against the n width for a
// fixed L1 budget.
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

// The core powers up in rounding_mode::floor, so a kernel that converts must
// choose explicitly. Truncation biases every conversion the same direction, so
// the error accumulates over the K reduction instead of cancelling -- ~1% of
// the result, against ~0.02% for round-to-nearest-even, which is far more than
// the bfp16 emulation itself costs. Every entry point that converts sets it:
// the mmul and the epilogue's f32->bf16 store, both below.
//
// Flag name and polarity follow mm.cc, so the two kernels are configured the
// same way; the operator passes -DROUND_CONV_EVEN by default.
#ifdef ROUND_CONV_EVEN
constexpr aie::rounding_mode round_mode = aie::rounding_mode::conv_even;
#else
constexpr aie::rounding_mode round_mode = aie::rounding_mode::floor;
#endif
} // namespace

extern "C" {

// Zero the f32 accumulator, before the k loop starts accumulating into it.
//
// A bias is deliberately not supported: initialising the accumulator from one
// would mean consuming an extra object through the handshake the B ObjectFifo
// owns, which desynchronises that fifo and hangs rather than mis-computing.
void mm_fused_acc_init(float *y_acc)
{
    // zero_vectorized brackets itself in event0/event1 for tracing.
    zero_vectorized<float, M, N>(y_acc);
}

// One step of the k loop: one B chunk multiplied against one A band,
// accumulated into y_acc.
//
// Takes no locks. A is a single object spanning every z slice of the mmul, and
// the A and B fifos own the handshake, so the core body acquires around this
// call rather than the kernel acquiring inside it.
// mm_fused_b_elem_t is bfp16ebs8 or bfloat16 depending on how B is stored,
// which mm_fused_mmul.h selects from the architecture. One signature either
// way, so the design's Kernel declaration does not have to care.
void mm_fused_k_step(bfloat16 *a_buf, mm_fused_b_elem_t *b_buf, float *y_acc, int32_t band)
{
    ::aie::set_rounding(round_mode);
    // The accumulator is [row-block][col-block][r*t], so band b starts at
    // b * MA * N -- b*(MA/R) row-blocks in, each colB*(r*t) wide.
    mm_fused_mmul_2x2<(MA / R), (CT_K / S), (N / T), R, S, T>(a_buf, b_buf, y_acc + band * (MA * N));
}

// The output stage: convert chunk (outer * C_DEPTH + half) of the f32
// accumulator into a bf16 C object the core body has already acquired from the
// C ObjectFifo, optionally applying an activation and a clamp on the way out.
//
// Fusing the activation here is the point: the values are already in registers
// after the f32 -> bf16 conversion, so gelu/silu/sigmoid costs one more vector
// op per 16 elements instead of a separate pass over L1 (which is what chaining
// a standalone activation operator after a GEMM would cost). The mode and clamp
// are compile-time, so the inner loop below is branch-free.
//
// The chunk index is split in two because the core body unrolls the drain by
// the C fifo depth to keep the acquired buffer index a compile-time constant;
// passing both parts avoids doing that arithmetic up there.
void mm_fused_epilogue_chunk(bfloat16 *y_out, float *y_acc, int32_t outer, int32_t half)
{
    // The store below is a conversion, so it obeys the same rounding mode the
    // mmul does and must agree with it.
    ::aie::set_rounding(round_mode);
    const float *__restrict src = y_acc + (outer * C_DEPTH + half) * CHUNK;

#if MM_FUSED_CLAMP
    const aie::vector<float, V> lo = aie::broadcast<float, V>(MM_FUSED_CLAMP_MIN);
    const aie::vector<float, V> hi = aie::broadcast<float, V>(MM_FUSED_CLAMP_MAX);
#endif

    AIE_LOOP_MAX_ITERATION_COUNT(CHUNK / V)
    for (int j = 0; j < CHUNK / V; j++) {
        // The accumulator stays f32 through the activation and the clamp, and
        // is converted to bf16 exactly once, on the store. Converting first
        // would round twice and let the activation's slope amplify the first
        // rounding -- see activations.h.
        aie::vector<float, V> f = aie::load_v<V>(src + j * V);
#if MM_FUSED_EPILOGUE_MODE == 1
        f = gelu_vec<V>(f);
#elif MM_FUSED_EPILOGUE_MODE == 2
        f = silu_vec<V>(f);
#elif MM_FUSED_EPILOGUE_MODE == 3
        f = sigmoid_vec<V>(f);
#endif
#if MM_FUSED_CLAMP
        f = aie::max(aie::min(f, hi), lo);
#endif
        aie::accum<accfloat, V> out;
        out.from_vector(f);
        // The assignment is the conversion: to_v16bfloat16 yields a raw
        // v16bfloat16, not an aie::vector.
        aie::vector<bfloat16, V> v = to_v16bfloat16(out);
        aie::store_v(y_out + j * V, v);
    }
}
}
