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

      static_assert(colA % 2 == 0);
      // Peano schedules the 2x-unrolled body better than it schedules the
      // rolled one; chess does not need the hand-unroll.
#if defined(__chess__)
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
#else
      AIE_LOOP_MAX_ITERATION_COUNT(colA / 2)
      for (unsigned i = 0; i < colA; i += 2) {
        // First iteration
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

        // Second iteration
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
#endif
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

#endif // __FLM_GEMM_MMUL_H__
