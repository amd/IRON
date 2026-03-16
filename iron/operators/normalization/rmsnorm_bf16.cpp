// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file rmsnorm_bf16.cpp
 * @brief Implementation of Root Mean Square Layer Normalization (RMSNorm) operator
 *
 * This file contains the implementation of RMSNorm for bfloat16 precision,
 * optimized for CPU execution with SIMD vectorization where available.
 *
 * Key features:
 * - FP32 accumulation for numerical stability
 * - Optional weight and bias parameters
 * - Configurable epsilon for stability
 *
 * @note For best performance, ensure input tensors are properly aligned
 */

#include "rmsnorm_bf16.hpp"
#include "types.hpp"
#include <cmath>
#include <cstring>

namespace iron {
namespace operators {
namespace normalization {

/**
 * @brief Internal helper: square of bfloat16 as float
 */
inline float bf16_square(bfloat16 x) {
    float fx = static_cast<float>(x);
    return fx * fx;
}

/**
 * @brief Internal helper: multiply bfloat16 by float
 */
inline bfloat16 bf16_mul_float(bfloat16 a, float b) {
    return bfloat16(static_cast<float>(a) * b);
}

/**
 * @brief Internal helper: divide bfloat16 by float
 */
inline bfloat16 bf16_div_float(bfloat16 a, float b) {
    return bfloat16(static_cast<float>(a) / b);
}

//==============================================================================
// rms_norm_fwd Implementation - Full Version
//==============================================================================

template<typename T>
void rms_norm_fwd(
    const T* input,
    const T* weight,
    const T* bias,
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps
) {
    const int total_rows = batch * seq;

    // Process each row (each token position)
    for (int row = 0; row < total_rows; ++row) {
        const int row_offset = row * hidden;

        // Step 1: Compute sum of squares (using FP32 accumulation)
        float sum_sq = 0.0f;
        for (int i = 0; i < hidden; ++i) {
            sum_sq += bf16_square(input[row_offset + i]);
        }

        // Step 2: Compute RMS
        const float rms = std::sqrt(sum_sq / static_cast<float>(hidden) + eps);
        const float inv_rms = 1.0f / rms;

        // Step 3: Normalize and apply weight/bias
        if (weight != nullptr) {
            if (bias != nullptr) {
                // Full RMSNorm with weight and bias
                for (int i = 0; i < hidden; ++i) {
                    const float normalized = static_cast<float>(input[row_offset + i]) * inv_rms;
                    const float scaled = normalized * static_cast<float>(weight[i]);
                    const float result = scaled + static_cast<float>(bias[i]);
                    output[row_offset + i] = bfloat16(result);
                }
            } else {
                // RMSNorm with weight only (common case for Llama3.2)
                for (int i = 0; i < hidden; ++i) {
                    const float normalized = static_cast<float>(input[row_offset + i]) * inv_rms;
                    const float result = normalized * static_cast<float>(weight[i]);
                    output[row_offset + i] = bfloat16(result);
                }
            }
        } else {
            if (bias != nullptr) {
                // RMSNorm with bias only (rare case)
                for (int i = 0; i < hidden; ++i) {
                    const float normalized = static_cast<float>(input[row_offset + i]) * inv_rms;
                    const float result = normalized + static_cast<float>(bias[i]);
                    output[row_offset + i] = bfloat16(result);
                }
            } else {
                // Unit variance RMSNorm (no weight, no bias)
                for (int i = 0; i < hidden; ++i) {
                    const float normalized = static_cast<float>(input[row_offset + i]) * inv_rms;
                    output[row_offset + i] = bfloat16(normalized);
                }
            }
        }
    }
}

// Explicit template instantiation for bfloat16
template void rms_norm_fwd<bfloat16>(
    const bfloat16*, const bfloat16*, const bfloat16*,
    bfloat16*, int, int, int, float
);

//==============================================================================
// rms_norm_fwd Overload - Without Bias
//==============================================================================

template<typename T>
void rms_norm_fwd(
    const T* input,
    const T* weight,
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps
) {
    // Delegate to full version with nullptr bias
    rms_norm_fwd(input, weight, nullptr, output, batch, seq, hidden, eps);
}

// Explicit template instantiation for bfloat16
template void rms_norm_fwd<bfloat16>(
    const bfloat16*, const bfloat16*, bfloat16*, int, int, int, float
);

//==============================================================================
// rms_norm_fwd_simple Implementation - Without Weight and Bias
//==============================================================================

template<typename T>
void rms_norm_fwd_simple(
    const T* input,
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps
) {
    // Delegate to full version with nullptr weight and bias
    rms_norm_fwd(input, nullptr, nullptr, output, batch, seq, hidden, eps);
}

// Explicit template instantiation for bfloat16
template void rms_norm_fwd_simple<bfloat16>(
    const bfloat16*, bfloat16*, int, int, int, float
);

} // namespace normalization
} // namespace operators
} // namespace iron
