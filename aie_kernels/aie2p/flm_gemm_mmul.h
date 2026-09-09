// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// The 2x2 mmul at the heart of flm_gemm, in the "one-buffer A" form its A
// ObjectFifo leg requires.
//
// A arrives as a SINGLE ObjectFifo object spanning every z slice, rather than a
// ping/pong pair the kernel locks for itself. The fifo owns that handshake, so
// there are no acquire/release pairs in here at all, and the core body acquires
// exactly one A object per call to this function.
//
// Each iteration of the j loop keeps four MMUL accumulators live (C00/C01/C10/
// C11) across a 2x2 block of output tiles, so each pair of A loads and each
// pair of B loads feeds four macs. That is what keeps the vector unit busy;
// dropping to a 1x1 tile would halve the arithmetic per load.
#ifndef __FLM_GEMM_MMUL_H__
#define __FLM_GEMM_MMUL_H__
#include "../aie_kernel_utils.h"
#include "flm_gemm_geometry.h"
#include <aie_api/aie.hpp>

// rowA/colA/colB count r x s (A), s x t (B) and r x t (C) sub-tiles, not
// elements. b_row_maj / is_b_s_t_in_row_major select B's in-L1 layout; flm_gemm
// always instantiates <false, true> (B column-major with row-major s x t
// sub-blocks), which is the layout its memtile forward() produces. The other
// combinations are kept because they are `if constexpr` and cost nothing, but
// they are untested here.
template <typename T_in, typename T_out, unsigned rowA, unsigned colA,
          unsigned colB, unsigned r, unsigned s, unsigned t,
          bool b_row_maj = true, bool is_b_s_t_in_row_major = false>
__aie_inline void
flm_gemm_mmul_2x2(const T_in *__restrict pA, const T_in *__restrict pB,
                  T_out *__restrict pC) {
  using MMUL = aie::mmul<r, s, t, T_in, T_in, accauto>;
  static_assert(r * s == MMUL::size_A);
  event0();
  AIE_LOOP_MAX_ITERATION_COUNT(rowA / 2)
  for (unsigned z = 0; z < rowA; z += 2) {
    T_out *__restrict pC1 = pC + (z * colB) * MMUL::size_C;
    T_out *__restrict pC2 = pC + ((z + 1) * colB) * MMUL::size_C;

    // A is one object spanning every z slice; index it directly.
    const T_in *__restrict pA_cur_buf = pA + (z >> 1) * (2 * r * colA * s);

    aie::vector<T_in, MMUL::size_A> A0;
    aie::vector<T_in, MMUL::size_A> A1;
    aie::vector<T_in, MMUL::size_B> B0;
    aie::vector<T_in, MMUL::size_B> B1;

    AIE_LOOP_MAX_ITERATION_COUNT(colB / 2)
    for (unsigned j = 0; j < colB; j += 2) {
      const T_in *__restrict pA1 = pA_cur_buf;
      const T_in *__restrict pA2 = pA_cur_buf + colA * MMUL::size_A;
      const T_in *__restrict pB1;
      const T_in *__restrict pB2;
      if constexpr (b_row_maj) {
        pB1 = pB + (j)*MMUL::size_B;
        pB2 = pB + (j + 1) * MMUL::size_B;
      } else {
        pB1 = pB + (j * colA) * MMUL::size_B;
        pB2 = pB + ((j + 1) * colA) * MMUL::size_B;
      }

      MMUL C00(aie::load_v<MMUL::size_C>(pC1));
      MMUL C01(aie::load_v<MMUL::size_C>(pC1 + MMUL::size_C));
      MMUL C10(aie::load_v<MMUL::size_C>(pC2));
      MMUL C11(aie::load_v<MMUL::size_C>(pC2 + MMUL::size_C));

      // Rolled, deliberately. An earlier 2x hand-unroll for the Peano path
      // is now a pessimization: with colA/2 = 4 trip counts there are too
      // few iterations to amortize the software pipeline's fill/drain.
      // Measured cycles per mmul call (HW trace, event0/event1): rolled
      // 1875, hand-unrolled 2x 2446, compiler unroll 4/8 3291/3221. Any
      // extra live state across this loop loses more than it gains --
      // Peano's register allocator is pipelining-unaware and manufactures
      // false loop-carried anti-deps (llvm-aie#1066), so keep the body
      // minimal and let the pipeliner overlap the iterations.
      AIE_LOOP_MAX_ITERATION_COUNT(colA)
      for (unsigned i = 0; i < colA; i++) {
        A0 = aie::load_v<MMUL::size_A>(pA1);
        pA1 += MMUL::size_A;
        A1 = aie::load_v<MMUL::size_A>(pA2);
        pA2 += MMUL::size_A;

        if constexpr (b_row_maj) {
          B0 = aie::load_v<MMUL::size_B>(pB1);
          pB1 += MMUL::size_B * colB;
          B1 = aie::load_v<MMUL::size_B>(pB2);
          pB2 += MMUL::size_B * colB;
        } else {
          if constexpr (is_b_s_t_in_row_major == false) {
            B0 = aie::transpose(aie::load_v<MMUL::size_B>(pB1), t, s);
            pB1 += MMUL::size_B;
            B1 = aie::transpose(aie::load_v<MMUL::size_B>(pB2), t, s);
            pB2 += MMUL::size_B;
          } else {
            B0 = aie::load_v<MMUL::size_B>(pB1);
            pB1 += MMUL::size_B;
            B1 = aie::load_v<MMUL::size_B>(pB2);
            pB2 += MMUL::size_B;
          }
        }

        C00.mac(A0, B0);
        C01.mac(A0, B1);
        C10.mac(A1, B0);
        C11.mac(A1, B1);
      }
      aie::store_v(pC1, C00.template to_vector<T_out>());
      pC1 += MMUL::size_C;
      aie::store_v(pC1, C01.template to_vector<T_out>());
      pC1 += MMUL::size_C;
      aie::store_v(pC2, C10.template to_vector<T_out>());
      pC2 += MMUL::size_C;
      aie::store_v(pC2, C11.template to_vector<T_out>());
      pC2 += MMUL::size_C;
    }
  }

  event1();
}

// The same 2x2 mmul, but B arrives ALREADY in bfp16ebs8 rather than bf16.
//
// The bf16 form converts B inside every mac -- transpose, widen, then
// to_v64bfp16ebs8 -- purely to feed hardware that only multiplies bfp16. B is
// static weights, so pack_B does that conversion once on the host instead.
// The values are unchanged: this hoists a rounding that already happened, it
// does not add one. It also makes B 9 bytes per 8 elements instead of 16,
// which is why it is worth doing at all -- the operator is DMA-bound.
//
// B is streamed rather than pointer-indexed because a block_vector cannot be
// aie::load_v'd, and because bfp16ebs8 pointer arithmetic counts BYTES, not
// blocks (llvm-aie#1232). The stream sidesteps both.
template <typename T_out, unsigned rowA, unsigned colA, unsigned colB,
          unsigned r, unsigned s, unsigned t>
__aie_inline void flm_gemm_mmul_2x2_bfpb(const bfloat16 *__restrict pA,
                                         const bfp16ebs8 *__restrict pB,
                                         T_out *__restrict pC) {
  constexpr unsigned sizeA = r * s;
  constexpr unsigned sizeB = s * t;
  constexpr unsigned sizeC = r * t;
  event0();
  AIE_LOOP_MAX_ITERATION_COUNT(rowA / 2)
  for (unsigned z = 0; z < rowA; z += 2) {
    T_out *__restrict pC1 = pC + (z * colB) * sizeC;
    T_out *__restrict pC2 = pC + ((z + 1) * colB) * sizeC;
    const bfloat16 *__restrict pA_cur = pA + (z >> 1) * (2 * r * colA * s);

    AIE_LOOP_MAX_ITERATION_COUNT(colB / 2)
    for (unsigned j = 0; j < colB; j += 2) {
      const bfloat16 *__restrict pA1 = pA_cur;
      const bfloat16 *__restrict pA2 = pA_cur + colA * sizeA;

      aie::block_vector_input_buffer_stream<bfp16ebs8, sizeB> pB1(pB);
      aie::block_vector_input_buffer_stream<bfp16ebs8, sizeB> pB2(pB);
      pB1.seek(j * colA);
      pB2.seek((j + 1) * colA);

      aie::accum<accfloat, sizeC> C00(aie::load_v<sizeC>(pC1));
      aie::accum<accfloat, sizeC> C01(aie::load_v<sizeC>(pC1 + sizeC));
      aie::accum<accfloat, sizeC> C10(aie::load_v<sizeC>(pC2));
      aie::accum<accfloat, sizeC> C11(aie::load_v<sizeC>(pC2 + sizeC));

      aie::vector<bfloat16, sizeA> A0;
      aie::vector<bfloat16, sizeA> A1;
      aie::accum<accfloat, sizeA> accA0;
      aie::accum<accfloat, sizeA> accA1;

      // Rolled for the same reason as the bf16 form: extra live state across
      // this loop loses more than it gains (llvm-aie#1066).
      AIE_LOOP_MAX_ITERATION_COUNT(colA)
      for (unsigned i = 0; i < colA; i++) {
        // One conversion per A operand per i, reused by both j accumulators,
        // rather than one inside each of the four macs. Same values.
        //
        // The two operands are widened by DIFFERENT routes, exactly as
        // mlir-aie's mm_bfp_mixed.cc does. Widening both by assignment makes
        // Peano's AIE2P backend abort with "Use not jointly dominated by
        // defs"; mul_elem_64 by one is the same arithmetic and codegens.
        A0 = aie::load_v<sizeA>(pA1);
        pA1 += sizeA;
        A1 = aie::load_v<sizeA>(pA2);
        pA2 += sizeA;
        accA0 = A0;
        accA1 = mul_elem_64(A1, concat(broadcast_one_to_v32bfloat16(),
                                       broadcast_one_to_v32bfloat16()));

        aie::block_vector<bfp16ebs8, sizeB> B0 = pB1.pop();
        aie::block_vector<bfp16ebs8, sizeB> B1 = pB2.pop();

        C00 = mac_8x8_8x8T(accA0.template to_vector<bfp16ebs8>(), B0, C00);
        C01 = mac_8x8_8x8T(accA0.template to_vector<bfp16ebs8>(), B1, C01);
        C10 = mac_8x8_8x8T(accA1.template to_vector<bfp16ebs8>(), B0, C10);
        C11 = mac_8x8_8x8T(accA1.template to_vector<bfp16ebs8>(), B1, C11);
      }
      aie::store_v(pC1, C00.template to_vector<T_out>());
      pC1 += sizeC;
      aie::store_v(pC1, C01.template to_vector<T_out>());
      pC1 += sizeC;
      aie::store_v(pC2, C10.template to_vector<T_out>());
      pC2 += sizeC;
      aie::store_v(pC2, C11.template to_vector<T_out>());
      pC2 += sizeC;
    }
  }
  event1();
}

#endif // __FLM_GEMM_MMUL_H__
