// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Compute kernel for the flm_gemm operator: a bf16 GEMM over a fixed 4x8 grid
// of compute tiles, where each tile owns an m x n slice of C and accumulates
// over K in f32.
//
// Split into per-step entry points rather than one entry point owning the whole
// loop nest. The loop nest lives in the design's core body instead
// (iron/operators/flm_gemm/design.py), which is what gives each level of it an
// ObjectFifo acquire point -- a fifo needs its consumer to acquire once per
// object, so a single entry point spanning a whole dispatch could not be fed by
// one.
//
// Tile geometry comes from the design as -D flags so design.py stays the single
// source of truth; the design's own buffer sizes and unroll factors are derived
// from the same constants.
#include "flm_gemm_mmul.h"
#include "zero.cc"
#include <aie_api/aie.hpp>
#include <stdint.h>

#if !defined(FLM_GEMM_TILE_M) || !defined(FLM_GEMM_TILE_K) ||                  \
    !defined(FLM_GEMM_TILE_N)
#error "design.py must pass -DFLM_GEMM_TILE_M / _TILE_K / _TILE_N"
#endif

namespace {
constexpr int M = FLM_GEMM_TILE_M;
// Asymmetric tile buffering: the A tile spans MA rows while the accumulator
// spans M, so the core folds RHO = M / MA A-bands into one C tile before
// releasing it. A dies as soon as it is consumed and C must live across the
// whole K reduction, so sizing both to M pays the peak cost twice. Defaults
// to M, which is the symmetric design.
#ifndef FLM_GEMM_TILE_MA
#define FLM_GEMM_TILE_MA FLM_GEMM_TILE_M
#endif
constexpr int MA = FLM_GEMM_TILE_MA;
static_assert(M % MA == 0, "tile_m must be a whole number of A bands");
constexpr int K = FLM_GEMM_TILE_K;
constexpr int N = FLM_GEMM_TILE_N;
constexpr int R = 8; // register tiling r/s/t
constexpr int S = 8;
constexpr int T = 8;

// How much of K one compute tile holds at a time, given the n width.
#ifdef FLM_GEMM_CT_K
constexpr int CT_K = FLM_GEMM_CT_K;
#else
constexpr int CT_K = compute_CT_k_max_n<N>();
#endif
static_assert(CT_K > 0, "no K-blocking geometry for this tile_n");

static_assert(MA % (2 * R) == 0, "tile_ma must be a multiple of 2*r (2x2 mmul)");
static_assert(N % (2 * T) == 0, "tile_n must be a multiple of 2*t (2x2 mmul)");
static_assert(K % CT_K == 0, "tile_k must be a multiple of the k slice");
static_assert(CT_K % S == 0, "k slice must be a multiple of s");

// The core powers up with rounding_mode::floor. Truncation biases every
// operand conversion the same direction, so the error accumulates coherently
// over the K reduction instead of cancelling -- measured as a ~1% bias in the
// result, ~20x worse than round-to-nearest-even, which is far more than the
// bfp16 emulation itself costs. Set it explicitly in every entry point that
// converts (the mmul here, and the f32->bf16 store in the epilogue).
#ifdef FLM_GEMM_ROUND_FLOOR
constexpr aie::rounding_mode round_mode = aie::rounding_mode::floor;
#else
constexpr aie::rounding_mode round_mode = aie::rounding_mode::conv_even;
#endif
} // namespace

extern "C" {

// Zero the f32 accumulator. Called once per mega-block-row, before the k loop
// starts accumulating into it.
//
// ADD_BIAS is deliberately not supported: initialising the accumulator from a
// bias vector would mean consuming an extra object through the same handshake
// the B ObjectFifo now owns, which would desynchronise that fifo and hang
// rather than silently mis-compute.
void flm_gemm_acc_init(float *y_acc) {
  // zero_vectorized brackets itself in event0/event1 for tracing.
  zero_vectorized<float, M, N>(y_acc);
}

// One l-step of a k iteration: one B chunk multiplied against one A object,
// accumulated into y_acc.
//
// The l loop lives in the core body so that each B chunk gets its own acquire
// point. A is a single object spanning every z slice of the mmul, so this takes
// no locks -- the A and B fifos own that handshake.
void flm_gemm_k_step(bfloat16 *a_buf, bfloat16 *b_buf, float *y_acc,
                     int32_t band) {
  ::aie::set_rounding(round_mode);
  constexpr int NUM_ITER = K / CT_K;
  // The accumulator is [row-block][col-block][r*t], so band b starts at
  // b * MA * N -- b*(MA/R) row-blocks in, each colB*(r*t) wide.
  flm_gemm_mmul_2x2<bfloat16, float, (MA / R), ((K / NUM_ITER) / S), (N / T), R,
                    S, T, /*b_row_maj=*/false, /*is_b_s_t_in_row_major=*/true>(
      a_buf, b_buf, y_acc + band * (MA * N));
}
}
