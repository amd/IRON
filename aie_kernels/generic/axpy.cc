// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#define NOCPP

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define REL_WRITE 0
#define REL_READ 1

#include <aie_api/aie.hpp>

extern "C" {
void saxpy(bfloat16 *restrict x, bfloat16 *restrict y, const float a, bfloat16 *restrict z, const int32_t vector_size)
{
    event0();
    ::aie::vector<bfloat16, 64> a_v =
        ::aie::broadcast<bfloat16, 64>(aie::to_float<bfloat16>(a, 0)); // Convert to bfloat16
                                                                       // #pragma clang loop min_iteration_count(4)
    for (int i = 0; i < vector_size; i += 64) {
        ::aie::vector<bfloat16, 64> x_v = ::aie::load_v<64>(x);
        x += 64;
        ::aie::vector<bfloat16, 64> y_v = ::aie::load_v<64>(y);
        y += 64;
        ::aie::accum<accfloat, 64> ax_v = ::aie::mul(x_v, a_v);
        ::aie::accum<accfloat, 64> z_v = ::aie::add(ax_v, y_v);
        ::aie::vector<bfloat16, 64> z_v_converted = z_v.to_vector<bfloat16>();
        ::aie::store_v(z, z_v_converted);
        z += 64;
    }
    event1();
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
    event0();
    ::aie::vector<bfloat16, 64> a_v = ::aie::broadcast<bfloat16, 64>(aie::to_float<bfloat16>(a, 0));
    for (int i = 0; i < vector_size; i += 64) {
        ::aie::vector<bfloat16, 64> x_v = ::aie::load_v<64>(x);
        x += 64;
        ::aie::accum<accfloat, 64> z_v = ::aie::mul(x_v, a_v);
        ::aie::vector<bfloat16, 64> z_v_converted = z_v.to_vector<bfloat16>();
        ::aie::store_v(z, z_v_converted);
        z += 64;
    }
    event1();
}

// z = a + y  (scalar-vector add; AXPY without the *x term)
void scalar_add_bf16(bfloat16 *restrict y, bfloat16 *restrict z, const float a, const int32_t vector_size)
{
    event0();
    ::aie::vector<bfloat16, 64> a_v = ::aie::broadcast<bfloat16, 64>(aie::to_float<bfloat16>(a, 0));
    for (int i = 0; i < vector_size; i += 64) {
        ::aie::vector<bfloat16, 64> y_v = ::aie::load_v<64>(y);
        y += 64;
        ::aie::vector<bfloat16, 64> z_v = ::aie::add(y_v, a_v);
        ::aie::store_v(z, z_v);
        z += 64;
    }
    event1();
}

// z = (col > row) ? a : y     applied per-element of one tile, using a tile
// position (chunk_start_col, row_in_head) supplied via the idx_buffer.
//
// The tile is interpreted as a `vector_size`-wide horizontal strip of the
// per-head (S, S) attention-score block; idx[0] is the strip's starting
// column within that block, idx[1] is the strip's row within the block.
// The kernel implements the causal mask in-place by writing `a` to elements
// strictly above the diagonal and copying y -> z everywhere else.  This
// avoids materialising an H*S*S mask buffer entirely.
//
// For tiles whose entire range lies at-or-below the diagonal, the kernel
// degenerates to a copy (input still streamed through DMA — slightly
// wasteful but simpler than per-tile data-movement skipping).
void scalar_add_causal_bf16(bfloat16 *restrict y,
                            bfloat16 *restrict z,
                            int32_t *idx,
                            const float a,
                            const int32_t vector_size)
{
    event0();

    constexpr int VEC = 64;

    int32_t chunk_start_col = idx[0];
    int32_t row_in_head = idx[1];

    // Index of the first column in the tile that needs to be masked
    // (i.e. column index strictly greater than row_in_head).
    int32_t mask_start = row_in_head + 1 - chunk_start_col;
    if (mask_start < 0)
        mask_start = 0;
    if (mask_start > vector_size)
        mask_start = vector_size;

    bfloat16 s = (bfloat16)a;
    ::aie::vector<bfloat16, VEC> s_v = ::aie::broadcast<bfloat16, VEC>(s);
    int j = 0;

    // ---- Unmasked region [0, mask_start): copy y -> z ----
    // Vectorised body up to the largest VEC-aligned offset <= mask_start.
    int mask_start_floor = (mask_start / VEC) * VEC;
    for (; j < mask_start_floor; j += VEC) {
        ::aie::vector<bfloat16, VEC> v = ::aie::load_v<VEC>(y + j);
        ::aie::store_v(z + j, v);
    }
    // Scalar copy for the unmasked remainder (at most VEC - 1 elements).
    for (; j < mask_start; j++) {
        z[j] = y[j];
    }

    // ---- Masked region [mask_start, vector_size): write scalar ----
    // If mask_start isn't VEC-aligned, scalar-fill up to the next VEC
    // boundary (or to vector_size, whichever is smaller).
    int next_vec_boundary = ((j + VEC - 1) / VEC) * VEC;
    if (next_vec_boundary > vector_size)
        next_vec_boundary = vector_size;
    for (; j < next_vec_boundary; j++) {
        z[j] = s;
    }
    // Vectorised body of the masked region.
    for (; j + VEC <= vector_size; j += VEC) {
        ::aie::store_v(z + j, s_v);
    }
    // Scalar tail when vector_size isn't VEC-aligned (in practice this
    // doesn't fire since per_tile_elements is always a multiple of VEC).
    for (; j < vector_size; j++) {
        z[j] = s;
    }

    event1();
}
}