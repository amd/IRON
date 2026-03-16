// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file silu_bf16.cpp
 * @brief Implementation of SiLU (Sigmoid Linear Unit) activation function
 *
 * This file contains the implementation of SiLU for bfloat16 precision,
 * optimized for CPU execution with SIMD vectorization where available.
 *
 * The implementation uses the tanh-based approximation:
 *   sigmoid(x) = 0.5 * (1 + tanh(x / 2))
 *   silu(x) = x * sigmoid(x)
 *
 * @note For best performance, ensure input tensors are properly aligned
 * @note Uses FP32 intermediate computation for improved accuracy
 */

#include "silu_bf16.hpp"
#include "types.hpp"
#include <cmath>
#include <cstring>

namespace iron {
namespace operators {
namespace activations {

//==============================================================================
// silu_fwd Implementation
//==============================================================================

template<typename T>
void silu_fwd(const T* input, T* output, int num_elements) {
    // Constants for sigmoid approximation using tanh
    constexpr float kHalf = 0.5f;
    constexpr float kOne = 1.0f;

    for (int i = 0; i < num_elements; ++i) {
        const float x = static_cast<float>(input[i]);

        // Compute sigmoid using tanh identity:
        // sigmoid(x) = 0.5 * (1 + tanh(x / 2))
        const float half_x = x * kHalf;
        const float tanh_half_x = std::tanh(half_x);
        const float sigmoid_x = kHalf * (kOne + tanh_half_x);

        // Compute SiLU: x * sigmoid(x)
        const float silu_result = x * sigmoid_x;

        output[i] = bfloat16(silu_result);
    }
}

// Explicit template instantiation for bfloat16
template void silu_fwd<bfloat16>(const bfloat16*, bfloat16*, int);

//==============================================================================
// silu_inplace Implementation
//==============================================================================

template<typename T>
void silu_inplace(T* input_output, int num_elements) {
    // Separate implementation to avoid potential aliasing issues
    // when the same pointer is passed as both input and output
    constexpr float kHalf = 0.5f;
    constexpr float kOne = 1.0f;

    for (int i = 0; i < num_elements; ++i) {
        const float x = static_cast<float>(input_output[i]);

        // Compute sigmoid using tanh identity:
        // sigmoid(x) = 0.5 * (1 + tanh(x / 2))
        const float half_x = x * kHalf;
        const float tanh_half_x = std::tanh(half_x);
        const float sigmoid_x = kHalf * (kOne + tanh_half_x);

        // Compute SiLU: x * sigmoid(x)
        const float silu_result = x * sigmoid_x;

        input_output[i] = bfloat16(silu_result);
    }
}

// Explicit template instantiation for bfloat16
template void silu_inplace<bfloat16>(bfloat16*, int);

//==============================================================================
// silu_gate Implementation (for SwiGLU)
//==============================================================================

template<typename T>
void silu_gate(const T* input, const T* gate, T* output, int num_elements) {
    constexpr float kHalf = 0.5f;
    constexpr float kOne = 1.0f;

    for (int i = 0; i < num_elements; ++i) {
        const float g = static_cast<float>(gate[i]);
        const float x = static_cast<float>(input[i]);

        // Compute sigmoid(gate) using tanh identity
        const float half_g = g * kHalf;
        const float tanh_half_g = std::tanh(half_g);
        const float sigmoid_g = kHalf * (kOne + tanh_half_g);

        // Compute SiLU(gate) = gate * sigmoid(gate)
        const float silu_g = g * sigmoid_g;

        // Apply gate: silu(gate) * input
        const float result = silu_g * x;

        output[i] = bfloat16(result);
    }
}

// Explicit template instantiation for bfloat16
template void silu_gate<bfloat16>(const bfloat16*, const bfloat16*, bfloat16*, int);

} // namespace activations
} // namespace operators
} // namespace iron
