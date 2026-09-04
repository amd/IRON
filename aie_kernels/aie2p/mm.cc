// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#define NOCPP

#include <stdio.h>
#include <stdlib.h>

#define REL_WRITE 0
#define REL_READ 1

#include "zero.cc"

#include <aie_api/aie.hpp>

template <typename T_in, typename T_out, int rowA, int colA, int colB, bool b_row_maj = true, bool c_row_maj = true>
static inline void matmul_scalar(T_in *a, T_in *b, T_out *c)
{
    event0();
    for (int row = 0; row < rowA; row++) {
        for (int col = 0; col < colB; col++) {
            T_out running_sum = 0;
            for (int i = 0; i < colA; i++) {
                T_in a_val = a[row * colA + i];
                T_in b_val;
                if constexpr (b_row_maj) {
                    b_val = b[i * colB + col];
                } else {
                    b_val = b[i + col * colA];
                }
                running_sum += a_val * b_val;
            }
            T_out *c_ptr;
            if constexpr (c_row_maj) {
                c_ptr = &c[row * colB + col];
            } else {
                c_ptr = &c[row + col * rowA];
            }
            *c_ptr += running_sum;
        }
    }
    event1();
}

/* Blocked MatMul kernel (vectorized) utilizing the aie::mmul class.
 * The matrices are assumed to be pre-tiled with the following shapes
 * for the aie:mmul class: A => rxs, B => sxt, C => rxt.
 *
 * The matrix dimensions of the kernel are defined by rowA, colA and colB.
 * In this particular kernel we expand the aie::mmul two times in each
 * input matrices A (in 'm' dimension, or rowA) and B (in 'n' dimension, or
 * ColB), leading to a 2x2 expansion in output matrix C (see C00, C01, C10, C11
 * below). This expansion helps with accumulator registers usage, which leads in
 * attaining high kernel efficiency (SIMD utilization).
 *
 * Data within each tile (rxs, sxt and rxt) are assumed to be in row-major
 * order. Also, the entire tiles themselves are stored in row-major order, as
 * shown in the example below for matrix A:
 *
 *      <-s->
 *    _  ________________________
 * 	  r |  1 |  2 |  3 | ...
 * 	  _ |____|____|____|
 * 	    |  x | x+1| x+2| ...
 * 	    |____|____|____|
 * 	    |.
 * 	    |.
 * 	    |.
 *
 * A simplified example of this kernel can be found in the AIE-API
 * documentation: https://xilinx.github.io/aie_api/group__group__mmul.html
 */
template <typename T_in,
          typename T_out,
          unsigned rowA,
          unsigned colA,
          unsigned colB,
          unsigned r,
          unsigned s,
          unsigned t,
          bool b_row_maj = true,
          bool c_row_maj = true,
          typename T_inB = T_in>
static inline void
matmul_vectorized_2x2_mmul(const T_in *__restrict pA, const T_inB *__restrict pB, T_out *__restrict pC)
{

    using MMUL = aie::mmul<r, s, t, T_in, T_inB, accauto>;

    // int4 elements are 4-bit, but the AIE API's int4_t is an empty struct so
    // sizeof(int4_t) == 1. Manual pointer arithmetic on `const int4*` therefore
    // advances 2x the real byte distance; the aie::load_v<> helpers know the
    // true packed size, so only the explicit pointer offsets below need the
    // correction. Every B pointer advance is in "elements" of the packed type;
    // halve the count for int4 to recover the real byte stride.
    constexpr unsigned kBEls = std::is_same_v<T_inB, int4> ? 1u : 2u;
    constexpr unsigned B_ADV = (MMUL::size_B * kBEls) / 2; // elements per k-block (real bytes)

    event0();

    for (unsigned z = 0; z < rowA; z += 2)
        chess_prepare_for_pipelining chess_loop_range(4, )
        {

            T_out *__restrict pC1;
            T_out *__restrict pC2;
            if constexpr (c_row_maj) {
                pC1 = pC + (z * colB) * MMUL::size_C;
                pC2 = pC + ((z + 1) * colB) * MMUL::size_C;
            }

            for (unsigned j = 0; j < colB; j += 2)
#ifdef OPT_PERF_ENABLED
                chess_flatten_loop
#endif
                {

                    if constexpr (!c_row_maj) {
                        pC1 = pC + j * rowA * MMUL::size_C + z * MMUL::size_C;
                        pC2 = pC + (j + 1) * rowA * MMUL::size_C + z * MMUL::size_C;
                    }
                    const T_in *__restrict pA1 = pA + (z * colA) * MMUL::size_A;
                    const T_in *__restrict pA2 = pA + ((z + 1) * colA) * MMUL::size_A;
                    const T_inB *__restrict pB1;
                    const T_inB *__restrict pB2;
                    if constexpr (b_row_maj) {
                        pB1 = pB + (j)*B_ADV;
                        pB2 = pB + (j + 1) * B_ADV;
                    } else {
                        pB1 = pB + (j * colA) * B_ADV;
                        pB2 = pB + ((j + 1) * colA) * B_ADV;
                    }
                    aie::vector<T_in, MMUL::size_A> A0;
                    aie::vector<T_in, MMUL::size_A> A1;
                    aie::vector<T_inB, MMUL::size_B> B0;
                    aie::vector<T_inB, MMUL::size_B> B1;

                    // Load partial results from C buffer for accumulation in-place. The
                    // zero.cc function handles the zeroing of data when a new
                    // accumulation is needed (after the 'K' reduction dimension)
                    aie::vector<T_out, MMUL::size_C> acc_C00;
                    aie::vector<T_out, MMUL::size_C> acc_C01;
                    aie::vector<T_out, MMUL::size_C> acc_C10;
                    aie::vector<T_out, MMUL::size_C> acc_C11;
                    if constexpr (c_row_maj) {
                        acc_C00 = aie::load_v<MMUL::size_C>(pC1);
                        acc_C01 = aie::load_v<MMUL::size_C>(pC1 + MMUL::size_C);
                        acc_C10 = aie::load_v<MMUL::size_C>(pC2);
                        acc_C11 = aie::load_v<MMUL::size_C>(pC2 + MMUL::size_C);
                    } else {
                        acc_C00 = aie::transpose(aie::load_v<MMUL::size_C>(pC1), t, r);
                        acc_C01 = aie::transpose(aie::load_v<MMUL::size_C>(pC2), t, r);
                        acc_C10 = aie::transpose(aie::load_v<MMUL::size_C>(pC1 + MMUL::size_C), t, r);
                        acc_C11 = aie::transpose(aie::load_v<MMUL::size_C>(pC2 + MMUL::size_C), t, r);
                    }

                    MMUL C00(acc_C00);
                    MMUL C01(acc_C01);
                    MMUL C10(acc_C10);
                    MMUL C11(acc_C11);

                    // Software-pipelined k-loop: prefetch the next k-step's
                    // A/B tiles while the current tiles are still being
                    // consumed by the MACs. This hides the load->vmac latency
                    // that the plain loop leaves exposed as nops. The ping
                    // variables (A0n..B1n) become the next iteration's
                    // operands, so the MAC chain never waits on a load.
                    // All B pointer advances use B_ADV (see its definition
                    // above): for int4 weights the AIE API's int4_t is an
                    // empty struct (sizeof == 1) although each element is
                    // really 4 bits, so manual pointer arithmetic must halve
                    // the element counts to hit the true packed byte offsets.
                    A0 = aie::load_v<MMUL::size_A>(pA1);
                    pA1 += MMUL::size_A;
                    A1 = aie::load_v<MMUL::size_A>(pA2);
                    pA2 += MMUL::size_A;
                    if constexpr (b_row_maj) {
                        B0 = aie::load_v<MMUL::size_B>(pB1);
                        pB1 += B_ADV * colB;
                        B1 = aie::load_v<MMUL::size_B>(pB2);
                        pB2 += B_ADV * colB;
                    } else {
                        B0 = aie::transpose(aie::load_v<MMUL::size_B>(pB1), t, s);
                        pB1 += B_ADV;
                        B1 = aie::transpose(aie::load_v<MMUL::size_B>(pB2), t, s);
                        pB2 += B_ADV;
                    }
                    constexpr unsigned k_loop_trips = colA - 1;
                    constexpr unsigned k_loop_hint =
                        k_loop_trips >= 4 ? 4 : (k_loop_trips > 0 ? k_loop_trips : 1);
                    for (unsigned i = 1; i < colA; ++i)
                        chess_prepare_for_pipelining chess_loop_range(k_loop_hint, )
                        {
                            aie::vector<T_in, MMUL::size_A> A0n =
                                aie::load_v<MMUL::size_A>(pA1);
                            pA1 += MMUL::size_A;
                            aie::vector<T_in, MMUL::size_A> A1n =
                                aie::load_v<MMUL::size_A>(pA2);
                            pA2 += MMUL::size_A;
                            if constexpr (b_row_maj) {
                                aie::vector<T_inB, MMUL::size_B> B0n =
                                    aie::load_v<MMUL::size_B>(pB1);
                                pB1 += B_ADV * colB;
                                aie::vector<T_inB, MMUL::size_B> B1n =
                                    aie::load_v<MMUL::size_B>(pB2);
                                pB2 += B_ADV * colB;
                                C00.mac(A0, B0);
                                C01.mac(A0, B1);
                                C10.mac(A1, B0);
                                C11.mac(A1, B1);
                                A0 = A0n;
                                A1 = A1n;
                                B0 = B0n;
                                B1 = B1n;
                            } else {
                                aie::vector<T_inB, MMUL::size_B> B0n = aie::transpose(
                                    aie::load_v<MMUL::size_B>(pB1), t, s);
                                pB1 += B_ADV;
                                aie::vector<T_inB, MMUL::size_B> B1n = aie::transpose(
                                    aie::load_v<MMUL::size_B>(pB2), t, s);
                                pB2 += B_ADV;
                                C00.mac(A0, B0);
                                C01.mac(A0, B1);
                                C10.mac(A1, B0);
                                C11.mac(A1, B1);
                                A0 = A0n;
                                A1 = A1n;
                                B0 = B0n;
                                B1 = B1n;
                            }
                        }
                    C00.mac(A0, B0);
                    C01.mac(A0, B1);
                    C10.mac(A1, B0);
                    C11.mac(A1, B1);

                    // TODO make shift right here to keep most significat bits
                    // when lowering the output
                    // example below shows how to shift right 10 bits
                    // #define SHIFT 10
                    // aie::store_v(pC1, C00.template to_vector<T_out>(SHIFT));

                    if constexpr (c_row_maj) {
                        aie::store_v(pC1, C00.template to_vector<T_out>());
                        pC1 += MMUL::size_C;
                        aie::store_v(pC1, C01.template to_vector<T_out>());
                        pC1 += MMUL::size_C;
                        aie::store_v(pC2, C10.template to_vector<T_out>());
                        pC2 += MMUL::size_C;
                        aie::store_v(pC2, C11.template to_vector<T_out>());
                        pC2 += MMUL::size_C;
                    } else {
                        aie::store_v(pC1, aie::transpose(C00.template to_vector<T_out>(), r, t));
                        pC1 += MMUL::size_C;
                        aie::store_v(pC2, aie::transpose(C01.template to_vector<T_out>(), r, t));
                        pC2 += MMUL::size_C;
                        aie::store_v(pC1, aie::transpose(C10.template to_vector<T_out>(), r, t));
                        pC1 += MMUL::size_C;
                        aie::store_v(pC2, aie::transpose(C11.template to_vector<T_out>(), r, t));
                        pC2 += MMUL::size_C;
                    }
                }
        }

    event1();
}

#ifdef B_COL_MAJ
constexpr bool is_b_row_maj = false;
#else
constexpr bool is_b_row_maj = true;
#endif

#ifdef C_COL_MAJ
constexpr bool is_c_row_maj = false;
#else
constexpr bool is_c_row_maj = true;
#endif

// The rounding mode can be set for bfloat16 mmul to improve accuracy
#ifdef ROUND_CONV_EVEN
constexpr aie::rounding_mode round_mode = aie::rounding_mode::conv_even;
#else
constexpr aie::rounding_mode round_mode = aie::rounding_mode::floor; // default
#endif

// The following kernel definitions use mmul shapes that have been found to be
// optimal for AIE2P in combination with the 2x2 mmul expanded kernel.
//
// All available matrix multiplication shapes in the AIE-API can be found here:
// https://xilinx.github.io/aie_api/group__group__mmul.html
//
// They are all defined based on the shape of the mmul, the input data format
// and the output data format.
//
// Additionally, they check for the correct
// divisibility of the tile dimensions. Note that while both the 'm' and 'n'
// dimensions of the mmul are expanded, the 'k' dimension is not.

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_4x4x8_i16_i16(const int16 *__restrict pA, const int16 *__restrict pB, int16 *__restrict pC)
{
    constexpr int r = 4;
    constexpr int s = 4;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    return matmul_vectorized_2x2_mmul<int16, int16, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_4x4x8_i16_i32(const int16 *__restrict pA, const int16 *__restrict pB, int32 *__restrict pC)
{
    constexpr int r = 4;
    constexpr int s = 4;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    return matmul_vectorized_2x2_mmul<int16, int32, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_4x8x8_bf16_bf16(const bfloat16 *__restrict pA, const bfloat16 *__restrict pB, bfloat16 *__restrict pC)
{
    constexpr int r = 4;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    ::aie::set_rounding(round_mode);

    return matmul_vectorized_2x2_mmul<bfloat16,
                                      bfloat16,
                                      (m / r),
                                      (k / s),
                                      (n / t),
                                      r,
                                      s,
                                      t,
                                      is_b_row_maj,
                                      is_c_row_maj>(pA, pB, pC);
}

// Note that this shape is only possible for bf16 when using bfp16 emulation
// during matmuls.
template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_8x8x8_bf16_bf16(const bfloat16 *__restrict pA, const bfloat16 *__restrict pB, bfloat16 *__restrict pC)
{
    constexpr int r = 8;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    ::aie::set_rounding(round_mode);

    return matmul_vectorized_2x2_mmul<bfloat16,
                                      bfloat16,
                                      (m / r),
                                      (k / s),
                                      (n / t),
                                      r,
                                      s,
                                      t,
                                      is_b_row_maj,
                                      is_c_row_maj>(pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_4x8x8_bf16_f32(const bfloat16 *__restrict pA, const bfloat16 *__restrict pB, float *__restrict pC)
{
    constexpr int r = 4;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    ::aie::set_rounding(round_mode);

    return matmul_vectorized_2x2_mmul<bfloat16, float, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_8x8x8_bf16_f32(const bfloat16 *__restrict pA, const bfloat16 *__restrict pB, float *__restrict pC)
{
    constexpr int r = 8;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    ::aie::set_rounding(round_mode);

    return matmul_vectorized_2x2_mmul<bfloat16, float, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_8x8x8_i8_i8(const int8 *__restrict pA, const int8 *__restrict pB, int8 *__restrict pC)
{
    constexpr int r = 8;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    return matmul_vectorized_2x2_mmul<int8, int8, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_8x8x8_i8_i16(const int8 *__restrict pA, const int8 *__restrict pB, int16 *__restrict pC)
{
    constexpr int r = 8;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    return matmul_vectorized_2x2_mmul<int8, int16, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_8x8x8_i8_i32(const int8 *__restrict pA, const int8 *__restrict pB, int32 *__restrict pC)
{
    constexpr int r = 8;
    constexpr int s = 8;
    constexpr int t = 8;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    return matmul_vectorized_2x2_mmul<int8, int32, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj, is_c_row_maj>(
        pA, pB, pC);
}

// Asymmetric 4-bit weight GEMM: A stays int8, B is int4 packed two-per-byte
// (the caller stores 4-bit weights in an int8 buffer; nibbles are (b & 0xf),
// (b >> 4)). AIE2P (Strix Halo, arch 22) exposes mmul_8_4 shapes 4x16x16 and
// 8x8x8; the 4x16x16 shape does 4*16*16 = 1024 MACs per instruction (vs 512
// for int8xint8 8x8x8), so INT4 weights double the MAC density. The
// accumulator is 32-bit (accauto for int8 x int4).
template <unsigned m, unsigned k, unsigned n>
static inline void
matmul_vectorized_4x16x16_i8_i4(const int8 *__restrict pA, const int8 *__restrict pB, int32 *__restrict pC)
{
    constexpr int r = 4;
    constexpr int s = 16;
    constexpr int t = 16;

    static_assert(m % (2 * r) == 0);
    static_assert(k % s == 0);
    static_assert(n % (2 * t) == 0);

    return matmul_vectorized_2x2_mmul<int8, int32, (m / r), (k / s), (n / t), r, s, t, is_b_row_maj,
                                      is_c_row_maj, int4>(pA, reinterpret_cast<const int4 *>(pB), pC);
}

extern "C" {

// If you want to compile microkernels with different inner tile sizes,
// define DIM_M, DIM_K and DIM_N at compile time using -DDIM_M 32 etc.
// These dimensions must be divisible by the r, s, t dimensions used in
// the kernels.

#ifndef DIM_M
#define DIM_M 64
#endif

#ifndef DIM_K
#define DIM_K 64
#endif

#ifndef DIM_N
#define DIM_N 64
#endif

#ifdef i8_i8_ONLY
#define combos(X) X(int8, i8, int8, i8, 8, 8, 8)
#endif

#ifdef i8_i16_ONLY
#define combos(X) X(int8, i8, int16, i16, 8, 8, 8)
#endif

#ifdef i8_i32_ONLY
#define combos(X) X(int8, i8, int32, i32, 8, 8, 8)
#endif

#ifdef i8_i4_ONLY
// Asymmetric: A int8, B int4 packed in int8 storage. Vectorized only (the
// scalar path is not instantiated for 4-bit inputs). AIE2P shape 4x16x16.
// combos stays empty so the generic instantiations (which would redefine
// zero_i32) are skipped; only combos_i4 emits matmul_i8_i4 + zero_i32.
#define combos(X)
#define combos_i4(X) X(int8, i8, int32, i32, 4, 16, 16)
#endif

#ifdef i16_i16_ONLY
#define combos(X) X(int16, i16, int16, i16, 4, 4, 8)
#endif

#ifdef i16_i32_ONLY
#define combos(X) X(int16, i16, int32, i32, 4, 4, 8)
#endif

// The emulation of bf16 changes the available shapes for matrix multiplication
#ifdef bf16_bf16_ONLY
#ifdef AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16
#define combos(X) X(bfloat16, bf16, bfloat16, bf16, 8, 8, 8)
#else
#define combos(X) X(bfloat16, bf16, bfloat16, bf16, 4, 8, 8)
#endif
#endif

#ifdef bf16_f32_ONLY
#ifdef AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16
#define combos(X) X(bfloat16, bf16, float, f32, 8, 8, 8)
#else
#define combos(X) X(bfloat16, bf16, float, f32, 4, 8, 8)
#endif
#endif

#ifndef combos
#ifdef AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16
#define combos(X)                                                                                                      \
    X(int8, i8, int8, i8, 8, 8, 8)                                                                                     \
    X(int16, i16, int16, i16, 4, 4, 8)                                                                                 \
    X(int16, i16, int32, i32, 4, 4, 8)                                                                                 \
    X(bfloat16, bf16, bfloat16, bf16, 8, 8, 8)                                                                         \
    X(bfloat16, bf16, float, f32, 8, 8, 8)
#else
#define combos(X)                                                                                                      \
    X(int8, i8, int8, i8, 8, 8, 8)                                                                                     \
    X(int16, i16, int16, i16, 4, 4, 8)                                                                                 \
    X(int16, i16, int32, i32, 4, 4, 8)                                                                                 \
    X(bfloat16, bf16, bfloat16, bf16, 4, 8, 8)                                                                         \
    X(bfloat16, bf16, float, f32, 4, 8, 8)
#endif
#endif

#define matmul_vectorized_c_func(ctype_in, mlir_type_in, ctype_out, mlir_type_out, r, s, t)                            \
    void matmul_##mlir_type_in##_##mlir_type_out(ctype_in *a_in, ctype_in *b_in, ctype_out *c_out)                     \
    {                                                                                                                  \
        matmul_vectorized_##r##x##s##x##t##_##mlir_type_in##_##mlir_type_out<DIM_M, DIM_K, DIM_N>(a_in, b_in, c_out);  \
    }

#define matmul_scalar_c_func(ctype_in, mlir_type_in, ctype_out, mlir_type_out, r, s, t)                                \
    void matmul_scalar_##mlir_type_in##_##mlir_type_out(ctype_in *a_in, ctype_in *b_in, ctype_out *c_out)              \
    {                                                                                                                  \
        matmul_scalar<ctype_in, ctype_out, DIM_M, DIM_K, DIM_N, is_b_row_maj, is_c_row_maj>(a_in, b_in, c_out);        \
    }

#define zero_vectorized_c_func(ctype_in, mlir_type_in, ctype_out, mlir_type_out, r, s, t)                              \
    void zero_##mlir_type_out(ctype_out *c_out)                                                                        \
    {                                                                                                                  \
        zero_vectorized<ctype_out, DIM_M, DIM_N>(c_out);                                                               \
    }

#define zero_scalar_c_func(ctype_in, mlir_type_in, ctype_out, mlir_type_out, r, s, t)                                  \
    void zero_scalar_##mlir_type_out(ctype_out *c_out)                                                                 \
    {                                                                                                                  \
        zero_scalar<ctype_out, DIM_M, DIM_N>(c_out);                                                                   \
    }

// Asymmetric i8 x i4: the extern-C symbol is matmul_i8_i4 and B arrives as
// int8 storage (the kernel reinterprets to int4). r/s/t come from combos_i4.
#define matmul_i4_vectorized_c_func(ctype_in, mlir_type_in, ctype_out, mlir_type_out, r, s, t)                         \
    void matmul_##mlir_type_in##_i4(ctype_in *a_in, ctype_in *b_in, ctype_out *c_out)                                  \
    {                                                                                                                  \
        matmul_vectorized_##r##x##s##x##t##_##mlir_type_in##_i4<DIM_M, DIM_K, DIM_N>(a_in, b_in, c_out);              \
    }

#define zero_i4_vectorized_c_func(ctype_in, mlir_type_in, ctype_out, mlir_type_out, r, s, t)                           \
    void zero_##mlir_type_out(ctype_out *c_out)                                                                        \
    {                                                                                                                  \
        zero_vectorized<ctype_out, DIM_M, DIM_N>(c_out);                                                               \
    }

combos(matmul_vectorized_c_func) combos(matmul_scalar_c_func) combos(zero_vectorized_c_func) combos(zero_scalar_c_func)
#ifdef combos_i4
combos_i4(matmul_i4_vectorized_c_func) combos_i4(zero_i4_vectorized_c_func)
#endif

} // extern "C"