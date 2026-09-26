// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// One attention head's context in decode: ctx[d] = sum_l p[l] * V[l, d], read
// from the value cache's own (L, D) layout, so nothing transposes V first.
//
// The sum is mv_bf16.cc's, operation for operation, at VEC_SIZE 64 over
// DIM_K = L: the GEMV that computes the same context from the transposed
// cache, V^T (D, L) times p. So the two agree bit for bit. That GEMV gives
// each output row 64 lanes of partial sums, lane j taking positions
// l = 64 i + j for i = 0, 1, ... in order -- the first a multiply, the rest
// multiply-accumulates onto it -- and then halves the 64 lanes, adding lane
// j + 32 onto lane j, then j + 16, 8, 4, 2 and 1, and rounds the one float
// left to bf16, to nearest even.
//
// Here the 64 partial sums of every d are kept as 64 rows of D floats in
// acc: row j is lane j, for all d at once. Position l is one row of V, so it
// is one multiply-accumulate of that row by p[l] broadcast, into row l % 64.
// The halving is then adds of whole rows. A float product of two bf16 is
// exact and every add is IEEE float32, on the accumulator adders the GEMV's
// tree uses too, so the order is all that decides the bits.
//
// gqa_context_bf16(v, p, acc, out, flags) takes one chunk of CHUNK positions:
// v their CHUNK rows of V, p their probabilities. flags says where the chunk
// sits: GQA_CONTEXT_FIRST starts the sums (acc is not read), GQA_CONTEXT_LAST
// finishes them into out (DIM_D bf16). A whole context is one FIRST call,
// middle calls with no flags, and one LAST call, or one call with both.

#define NOCPP

#include <stdint.h>

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>

#ifndef DIM_D
#define DIM_D 64
#endif

#ifndef CHUNK
#error Please define CHUNK, the positions per call, at compile time.
#endif

// The GEMV's VEC_SIZE: partial sums per output.
#define LANES 64

#define GQA_CONTEXT_FIRST 1
#define GQA_CONTEXT_LAST 2

static_assert(DIM_D == 64, "a row of V is one 64-lane vector");
static_assert(CHUNK % LANES == 0, "a chunk is whole rounds of the 64 lanes");

// Adds partial-sum rows CHUNK / LANES rounds of positions deep: row j takes
// positions j, LANES + j, ... of the chunk, in that order. The first round of
// the first chunk multiplies, as the GEMV's first chunk does.
template <bool first>
static inline void accumulate(const bfloat16 *__restrict v,
                              const bfloat16 *__restrict p,
                              float *__restrict acc) {
  constexpr unsigned rounds = CHUNK / LANES;
  for (unsigned j = 0; j < LANES; j++) {
    const bfloat16 *__restrict vj = v + j * DIM_D;
    const bfloat16 *__restrict pj = p + j;
    float *__restrict row = acc + j * DIM_D;
    aie::accum<accfloat, DIM_D> sum;
    unsigned i = 0;
    if constexpr (first) {
      sum = aie::mul(aie::load_v<DIM_D>(vj),
                     aie::broadcast<bfloat16, DIM_D>(pj[0]));
      i = 1;
    } else {
      sum.from_vector(aie::load_v<DIM_D>(row));
    }
    AIE_LOOP_UNROLL_FULL
    for (; i < rounds; i++)
      sum = aie::mac(sum, aie::load_v<DIM_D>(vj + i * LANES * DIM_D),
                     aie::broadcast<bfloat16, DIM_D>(pj[i * LANES]));
    aie::store_v(row, sum.template to_vector<float>());
  }
}

// The GEMV's halving tree over the rows, then its round to bf16.
static inline void finish(float *__restrict acc, bfloat16 *__restrict out) {
  for (unsigned half = LANES / 2; half >= 1; half /= 2) {
    for (unsigned j = 0; j < half; j++) {
      aie::accum<accfloat, DIM_D> a, b;
      a.from_vector(aie::load_v<DIM_D>(acc + j * DIM_D));
      b.from_vector(aie::load_v<DIM_D>(acc + (j + half) * DIM_D));
      aie::store_v(acc + j * DIM_D, aie::add(a, b).template to_vector<float>());
    }
  }
  aie::accum<accfloat, DIM_D> sum;
  sum.from_vector(aie::load_v<DIM_D>(acc));
  aie::store_v(out, sum.template to_vector<bfloat16>());
}

extern "C" {

void gqa_context_bf16(const bfloat16 *__restrict v,
                      const bfloat16 *__restrict p, float *__restrict acc,
                      bfloat16 *__restrict out, int32_t flags) {
  event0();
  // The GEMV runs its whole body, sums included, in this mode.
  ::aie::rounding_mode saved_rounding =
      ::aie::swap_rounding(aie::rounding_mode::conv_even);
  if (flags & GQA_CONTEXT_FIRST)
    accumulate<true>(v, p, acc);
  else
    accumulate<false>(v, p, acc);
  if (flags & GQA_CONTEXT_LAST)
    finish(acc, out);
  ::aie::set_rounding(saved_rounding);
  event1();
}

} // extern "C"
