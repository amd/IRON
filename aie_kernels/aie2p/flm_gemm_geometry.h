// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// K-blocking geometry for the flm_gemm design: how much of K one compute tile
// holds at a time, as a function of the n tile width. flm_gemm.cc reads this to
// size its k loop; flm_gemm_mmul.h is the mmul that consumes the result.
//
// The values are a fixed L1 budget split two ways: a wider n tile leaves less
// room for the k slice of B, so the product stays roughly constant. n=128 (the
// only width flm_gemm currently builds) caps the core's k slice at 32.
#ifndef __FLM_GEMM_GEOMETRY_H__
#define __FLM_GEMM_GEOMETRY_H__
#include <aie_api/aie.hpp>
#include <stdint.h>

constexpr int CT_k_max_n_16 = 16;
constexpr int CT_k_max_n_32 = 32;
constexpr int CT_k_max_n_64 = 128;
constexpr int CT_k_max_n_128 = 32;
constexpr int CT_k_max_n_256 = 16;

template <int N>
constexpr int compute_CT_k_max_n() {
  if constexpr (N == 16) {
    return CT_k_max_n_16;
  } else if constexpr (N == 32) {
    return CT_k_max_n_32;
  } else if constexpr (N == 64) {
    return CT_k_max_n_64;
  } else if constexpr (N == 128) {
    return CT_k_max_n_128;
  } else if constexpr (N == 256) {
    return CT_k_max_n_256;
  } else {
    return -1;
  }
}

#endif // __FLM_GEMM_GEOMETRY_H__
