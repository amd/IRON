// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Branch-free activations over an aie::vector<bfloat16, N>, for mm_fused's
// fused epilogue.
//
// These are templated on the vector width and return a vector, so they compose
// inside an existing vector loop -- unlike aie_kernels/<arch>/{gelu,silu}.cc,
// which are whole-buffer entry points over a fixed 32-wide vector. mm_fused's
// epilogue needs the former: it applies the activation to the same 16-wide
// vector it just converted from the f32 accumulator, without a second pass over
// L1.
//
// All three are built on tanh, so the sigmoid below is exact-by-identity rather
// than a polynomial fit:
//   sigmoid(x) == (tanh(x/2) + 1) / 2
// GELU then uses the sigmoid approximation gelu(x) ~= x * sigmoid(1.702x),
// which is NOT the same curve as gelu.cc's tanh approximation
//   0.5x(1 + tanh(sqrt(2/pi)(x + 0.044715x^3)))
// The two agree to well within bf16 precision over the range that matters, but
// they are different functions -- do not expect bit-identical results if you
// compare against the gelu operator.
//
// Where that tanh comes from is the one part of mm_fused that is genuinely
// architecture-specific:
//
//   AIE2P has a native vector tanh (aie::tanh) evaluated on an f32 accumulator.
//   AIE2 (Phoenix) does not, so it falls back to the piecewise-linear LUT in
//   mlir-aie's aie_runtime_lib/AIE2/lut_based_ops.h -- the same getTanhBf16 that
//   aie_kernels/aie2/{tanh,sigmoid}.cc already use. That LUT is fixed at 16
//   lanes, which is exactly the epilogue's vector width, so nothing needs
//   splitting; the static_assert below pins that assumption.
//
// The two paths therefore do NOT produce bit-identical results, and the AIE2
// path carries the LUT's approximation error on top of bf16 rounding. test.py
// sets the accuracy budget per architecture accordingly.
#ifndef __ACTIVATIONS_H__
#define __ACTIVATIONS_H__
#include <aie_api/aie.hpp>

#if __AIE_ARCH__ >= 21
#define ACTIVATIONS_NATIVE_TANH 1
#else
#define ACTIVATIONS_NATIVE_TANH 0
// Supplies getTanhBf16. Resolved from the runtime-lib include directory the
// build adds for the target arch (aie_runtime_lib/AIE2), not from this file's
// own directory.
#include "lut_based_ops.h"
#endif

// tanh of an f32 accumulator, on whichever path this architecture has.
template <int vec_size>
__attribute__((always_inline)) aie::vector<bfloat16, vec_size> tanh_vec(aie::accum<accfloat, vec_size> x)
{
#if ACTIVATIONS_NATIVE_TANH
    return aie::tanh<bfloat16>(x.template to_vector<float>());
#else
    static_assert(vec_size == 16,
                  "AIE2's LUT tanh is fixed at 16 lanes, which is mm_fused's "
                  "epilogue width; widening V needs an explicit split here");
    return getTanhBf16(x.template to_vector<bfloat16>());
#endif
}

// sigmoid(x) = (tanh(x/2) + 1) / 2
template <int vec_size> aie::vector<bfloat16, vec_size> sigmoid_vec(aie::vector<bfloat16, vec_size> x)
{
    const bfloat16 half = 0.5f;
    const bfloat16 one = 1.0f;
    aie::vector<bfloat16, vec_size> v_half = aie::broadcast<bfloat16, vec_size>(half);
    aie::vector<bfloat16, vec_size> v_one = aie::broadcast<bfloat16, vec_size>(one);
    aie::accum<accfloat, vec_size> x_mul_half = aie::mul(x, v_half);
    aie::vector<bfloat16, vec_size> tanh_x_half = tanh_vec<vec_size>(x_mul_half);

    aie::vector<bfloat16, vec_size> tanh_x_half_plus_one = aie::add(tanh_x_half, v_one);
    return aie::mul(tanh_x_half_plus_one, v_half);
}

// silu(x) = x * sigmoid(x)
template <int vec_size> aie::vector<bfloat16, vec_size> silu_vec(aie::vector<bfloat16, vec_size> x)
{
    aie::vector<bfloat16, vec_size> sigmoid_x = sigmoid_vec<vec_size>(x);
    return aie::mul(x, sigmoid_x);
}

// gelu(x) ~= x * sigmoid(1.702x)
template <int vec_size> aie::vector<bfloat16, vec_size> gelu_vec(aie::vector<bfloat16, vec_size> x)
{
    constexpr bfloat16 x_scale = 1.702;
    aie::vector<bfloat16, vec_size> v_x_scale = aie::broadcast<bfloat16, vec_size>(x_scale);
    aie::vector<bfloat16, vec_size> x_scaled = aie::mul(x, v_x_scale);
    aie::vector<bfloat16, vec_size> sigmoid_x_scaled = sigmoid_vec<vec_size>(x_scaled);
    return aie::mul(x, sigmoid_x_scaled);
}

#endif // __ACTIVATIONS_H__
