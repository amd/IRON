// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#define NOCPP

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define REL_WRITE 0
#define REL_READ 1

#include <aie_api/aie.hpp>

// One vectorised AXPY-family kernel. The compile-time flags select which terms
// are emitted so the public entry points share a single loop body:
//   Mul && Add : z = a * x + y   (saxpy)
//   Mul        : z = a * x       (scale_bf16)
//   Add        : z = a + y       (scalar_add_bf16)
template <bool Mul, bool Add>
static inline void saxpy_family(const bfloat16 *restrict x,
                                const bfloat16 *restrict y,
                                const float a,
                                bfloat16 *restrict z,
                                const int32_t vector_size)
{
    event0();
    ::aie::vector<bfloat16, 64> a_v = ::aie::broadcast<bfloat16, 64>((bfloat16)a);
    for (int i = 0; i < vector_size; i += 64) {
        ::aie::vector<bfloat16, 64> result;
        if constexpr (Mul && Add) {
            ::aie::vector<bfloat16, 64> x_v = ::aie::load_v<64>(x);
            x += 64;
            ::aie::vector<bfloat16, 64> y_v = ::aie::load_v<64>(y);
            y += 64;
            ::aie::accum<accfloat, 64> ax_v = ::aie::mul(x_v, a_v);
            result = ::aie::add(ax_v, y_v).to_vector<bfloat16>();
        } else if constexpr (Mul) {
            ::aie::vector<bfloat16, 64> x_v = ::aie::load_v<64>(x);
            x += 64;
            result = ::aie::mul(x_v, a_v).to_vector<bfloat16>();
        } else {
            ::aie::vector<bfloat16, 64> y_v = ::aie::load_v<64>(y);
            y += 64;
            result = ::aie::add(y_v, a_v);
        }
        ::aie::store_v(z, result);
        z += 64;
    }
    event1();
}

// General in-place triangular fill over a horizontal strip of a square (N, N)
// block. The strip is one `vector_size`-wide row segment; idx[0] is the
// segment's starting column within the block row and idx[1] is the row index.
// Elements strictly above the diagonal (column > row) are updated from the
// scalar `a`; elements on or below the diagonal copy the input y -> z. This
// realises e.g. a causal attention mask (a = -inf) without materialising a
// full (N, N) mask buffer. Segments lying entirely on/below the diagonal
// degenerate to a copy.
//
// The masked update is templated: FillConst writes the raw scalar `a`, while
// !FillConst adds `a` to the input (an AXPY-like masked update).
template <bool FillConst>
static inline void triangular_fill_impl(const bfloat16 *restrict y,
                                        bfloat16 *restrict z,
                                        const int32_t *restrict idx,
                                        const float a,
                                        const int32_t vector_size)
{
    event0();

    constexpr int VEC = 64;

    int32_t chunk_start_col = idx[0];
    int32_t row_in_head = idx[1];

    // Index of the first column in the strip that needs to be masked
    // (i.e. column index strictly greater than row_in_head).
    int32_t mask_start = row_in_head + 1 - chunk_start_col;
    if (mask_start < 0)
        mask_start = 0;
    if (mask_start > vector_size)
        mask_start = vector_size;

    bfloat16 s = (bfloat16)a;
    ::aie::vector<bfloat16, VEC> s_v = ::aie::broadcast<bfloat16, VEC>(s);
    int j = 0;

    // Unmasked region [0, mask_start): copy y -> z. Vectorised body up to the
    // largest VEC-aligned offset <= mask_start.
    int mask_start_floor = (mask_start / VEC) * VEC;
    for (; j < mask_start_floor; j += VEC) {
        ::aie::vector<bfloat16, VEC> v = ::aie::load_v<VEC>(y + j);
        ::aie::store_v(z + j, v);
    }
    // Scalar copy for the unmasked remainder (at most VEC - 1 elements).
    for (; j < mask_start; j++) {
        z[j] = y[j];
    }

    // Masked region [mask_start, vector_size). If mask_start isn't VEC-aligned,
    // scalar-update up to the next VEC boundary to keep the vector body aligned.
    int next_vec_boundary = ((j + VEC - 1) / VEC) * VEC;
    if (next_vec_boundary > vector_size)
        next_vec_boundary = vector_size;
    for (; j < next_vec_boundary; j++) {
        if constexpr (FillConst)
            z[j] = s;
        else
            z[j] = (bfloat16)(a + (float)y[j]);
    }
    // Vectorised body of the masked region.
    for (; j + VEC <= vector_size; j += VEC) {
        if constexpr (FillConst) {
            ::aie::store_v(z + j, s_v);
        } else {
            ::aie::vector<bfloat16, VEC> v = ::aie::load_v<VEC>(y + j);
            ::aie::store_v(z + j, ::aie::add(v, s_v));
        }
    }
    // Scalar tail when vector_size isn't VEC-aligned (in practice this doesn't
    // fire since per_tile_elements is always a multiple of VEC).
    for (; j < vector_size; j++) {
        if constexpr (FillConst)
            z[j] = s;
        else
            z[j] = (bfloat16)(a + (float)y[j]);
    }

    event1();
}

extern "C" {
void saxpy(bfloat16 *restrict x, bfloat16 *restrict y, const float a, bfloat16 *restrict z, const int32_t vector_size)
{
    saxpy_family<true, true>(x, y, a, z, vector_size);
}

void saxpy_scalar(bfloat16 *x, bfloat16 *y, const bfloat16 a, bfloat16 *z, const int32_t vector_size)
{
    event0();
    float a_f = a;
    for (int i = 0; i < vector_size; ++i) {
        z[i] = a_f * x[i] + y[i];
    }
    event1();
}

// z = a * x  (scalar-vector multiply; AXPY without the +y term)
void scale_bf16(bfloat16 *restrict x, bfloat16 *restrict z, const float a, const int32_t vector_size)
{
    saxpy_family<true, false>(x, nullptr, a, z, vector_size);
}

// z = a + y  (scalar-vector add; AXPY without the *x term)
void scalar_add_bf16(bfloat16 *restrict y, bfloat16 *restrict z, const float a, const int32_t vector_size)
{
    saxpy_family<false, true>(nullptr, y, a, z, vector_size);
}

// Causal attention mask: write `a` (typically -inf) strictly above the
// per-row diagonal and copy the input elsewhere. Thin wrapper over the general
// triangular fill (constant-fill specialization).
void scalar_add_causal_bf16(bfloat16 *restrict y,
                            bfloat16 *restrict z,
                            int32_t *idx,
                            const float a,
                            const int32_t vector_size)
{
    triangular_fill_impl<true>(y, z, idx, a, vector_size);
}
}