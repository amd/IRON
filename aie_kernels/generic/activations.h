// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Branch-free activations over an aie::vector<float, N>, for mm_fused's fused
// epilogue.
//
// These are templated on the vector width and return a vector, so they compose
// inside an existing vector loop -- unlike aie_kernels/<arch>/{gelu,silu}.cc,
// which are whole-buffer entry points over a fixed 32-wide vector. mm_fused's
// epilogue needs the former: it applies the activation to the f32 accumulator
// it already has in registers, without a second pass over L1.
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

// All three take and return f32, and mm_fused converts to bf16 once at the end.
// Rounding the accumulator to bf16 BEFORE the activation, as an earlier version
// did, rounds twice and lets the activation's slope amplify the first rounding;
// measured against an exact f64 evaluation that costs 1.35x the error on silu,
// 1.17x on gelu and 1.08x on sigmoid.
//
// tanh is the one step that cannot always stay f32: AIE2P has a native f32
// tanh, while AIE2's LUT is bf16-only, so on AIE2 the tanh result is rounded
// and widened back. Everything around it -- the x/2 and 1.702x scalings, the
// (t+1)/2, and silu/gelu's outer multiply by x -- stays f32 on both, and that
// outer multiply is where most of the silu gain comes from.

// tanh of an f32 vector, on whichever path this architecture has.
template <int vec_size>
__attribute__((always_inline)) aie::vector<float, vec_size> tanh_vec(aie::vector<float, vec_size> x)
{
    // bf16 out on both paths, widened back to f32. Asking AIE2P for the f32
    // tanh instead defeats aiecc's stack measurement -- it reports a spurious
    // "__start -> _main_init -> core -> _main_init" recursion -- and tanh's
    // output is in [-1, 1], where bf16 costs at most 2^-9 absolute anyway. The
    // arithmetic AROUND it is where the f32 actually pays.
    aie::accum<accfloat, vec_size> widened;
#if ACTIVATIONS_NATIVE_TANH
    widened.from_vector(aie::tanh<bfloat16>(x));
#else
    static_assert(vec_size == 16,
                  "AIE2's LUT tanh is fixed at 16 lanes, which is mm_fused's "
                  "epilogue width; widening V needs an explicit split here");
    aie::accum<accfloat, vec_size> narrowed;
    narrowed.from_vector(x);
    widened.from_vector(getTanhBf16(narrowed.template to_vector<bfloat16>()));
#endif
    return widened.template to_vector<float>();
}

// sigmoid(x) = (tanh(x/2) + 1) / 2
template <int vec_size>
__attribute__((always_inline)) aie::vector<float, vec_size> sigmoid_vec(aie::vector<float, vec_size> x)
{
    const aie::vector<float, vec_size> v_half = aie::broadcast<float, vec_size>(0.5f);
    const aie::vector<float, vec_size> v_one = aie::broadcast<float, vec_size>(1.0f);
    aie::vector<float, vec_size> t =
        tanh_vec<vec_size>(aie::mul(x, v_half).template to_vector<float>());
    return aie::mul(aie::add(t, v_one), v_half).template to_vector<float>();
}

// silu(x) = x * sigmoid(x)
template <int vec_size>
__attribute__((always_inline)) aie::vector<float, vec_size> silu_vec(aie::vector<float, vec_size> x)
{
    return aie::mul(x, sigmoid_vec<vec_size>(x)).template to_vector<float>();
}

// gelu(x) ~= x * sigmoid(1.702x)
template <int vec_size>
__attribute__((always_inline)) aie::vector<float, vec_size> gelu_vec(aie::vector<float, vec_size> x)
{
    const aie::vector<float, vec_size> v_scale = aie::broadcast<float, vec_size>(1.702f);
    aie::vector<float, vec_size> scaled = aie::mul(x, v_scale).template to_vector<float>();
    return aie::mul(x, sigmoid_vec<vec_size>(scaled)).template to_vector<float>();
}

#endif // __ACTIVATIONS_H__
