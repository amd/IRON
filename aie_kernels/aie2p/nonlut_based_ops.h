// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Branch-free, LUT-free activations over an aie::vector<bfloat16, N>.
//
// These are templated on the vector width and return a vector, so they compose
// inside an existing vector loop -- unlike aie_kernels/aie2p/{gelu,silu}.cc,
// which are whole-buffer entry points over a fixed 32-wide vector. flm_gemm's
// epilogue needs the former: it applies the activation to the same 16-wide
// vector it just converted from the f32 accumulator, without a second pass over
// L1.
//
// All three are built on tanh, which AIE2P has as a native vector op, so the
// sigmoid below is exact-by-identity rather than a polynomial fit:
//   sigmoid(x) == (tanh(x/2) + 1) / 2
// GELU then uses the sigmoid approximation gelu(x) ~= x * sigmoid(1.702x),
// which is NOT the same curve as gelu.cc's tanh approximation
//   0.5x(1 + tanh(sqrt(2/pi)(x + 0.044715x^3)))
// The two agree to well within bf16 precision over the range that matters, but
// they are different functions -- do not expect bit-identical results if you
// compare against the gelu operator.
#ifndef __NONLUT_BASED_OPS_H__
#define __NONLUT_BASED_OPS_H__
#include <aie_api/aie.hpp>

// sigmoid(x) = (tanh(x/2) + 1) / 2
template <int vec_size>
aie::vector<bfloat16, vec_size>
getSigmoidBf16_nonLUT(aie::vector<bfloat16, vec_size> x) {
  const bfloat16 half = 0.5f;
  const bfloat16 one = 1.0f;
  aie::vector<bfloat16, vec_size> v_half =
      aie::broadcast<bfloat16, vec_size>(half);
  aie::vector<bfloat16, vec_size> v_one =
      aie::broadcast<bfloat16, vec_size>(one);
  aie::accum<accfloat, vec_size> x_mul_half = aie::mul(x, v_half);
  aie::vector<bfloat16, vec_size> tanh_x_half =
      aie::tanh<bfloat16>(x_mul_half.template to_vector<float>());

  aie::vector<bfloat16, vec_size> tanh_x_half_plus_one =
      aie::add(tanh_x_half, v_one);
  return aie::mul(tanh_x_half_plus_one, v_half);
}

// silu(x) = x * sigmoid(x)
template <int vec_size>
aie::vector<bfloat16, vec_size>
getSiluBf16_nonLUT(aie::vector<bfloat16, vec_size> x) {
  aie::vector<bfloat16, vec_size> sigmoid_x = getSigmoidBf16_nonLUT<vec_size>(x);
  return aie::mul(x, sigmoid_x);
}

// gelu(x) ~= x * sigmoid(1.702x)
template <int vec_size>
aie::vector<bfloat16, vec_size>
getGeluBf16_nonLUT(aie::vector<bfloat16, vec_size> x) {
  constexpr bfloat16 x_scale = 1.702;
  aie::vector<bfloat16, vec_size> v_x_scale =
      aie::broadcast<bfloat16, vec_size>(x_scale);
  aie::vector<bfloat16, vec_size> x_scaled = aie::mul(x, v_x_scale);
  aie::vector<bfloat16, vec_size> sigmoid_x_scaled =
      getSigmoidBf16_nonLUT<vec_size>(x_scaled);
  return aie::mul(x, sigmoid_x_scaled);
}

#endif // __NONLUT_BASED_OPS_H__
