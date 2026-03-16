// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file rmsnorm_bf16.hpp
 * @brief Root Mean Square Layer Normalization (RMSNorm) operator for bfloat16
 *
 * This header defines the RMSNorm operator for normalizing activations
 * in transformer models. RMSNorm is a simplified layer normalization
 * that omits the mean centering operation.
 *
 * The RMSNorm operation is defined as:
 *   rms = sqrt(mean(x^2) + eps)
 *   output = (x / rms) * weight
 *
 * where:
 * - rms is computed over the last dimension (hidden dimension)
 * - eps is a small constant for numerical stability
 * - weight is an optional learnable scale parameter
 *
 * @note This implementation supports bfloat16 precision with FP32 accumulation
 * @note RMSNorm is used in Llama3.2 and other modern transformer architectures
 *
 * @see "Root Mean Square Layer Normalization" (Zhang & Sennrich, 2019)
 */

#pragma once

#include <cstdint>
#include <cstddef>

namespace iron {
namespace operators {
namespace normalization {

/**
 * @brief Apply Root Mean Square Layer Normalization
 *
 * This function computes RMSNorm over the last dimension of the input tensor.
 * The normalization is computed as:
 *   rms = sqrt(sum(x^2) / hidden + eps)
 *   output = (x / rms) * weight
 *
 * @tparam T Data type (typically bfloat16 or float)
 *
 * @param input Input tensor [batch, seq, hidden]
 * @param weight Scale parameter [hidden] (optional, can be nullptr)
 * @param bias Bias parameter [hidden] (optional, can be nullptr)
 * @param output Output tensor [batch, seq, hidden]
 * @param batch Batch size (number of sequences)
 * @param seq Sequence length
 * @param hidden Hidden dimension (last dimension)
 * @param eps Epsilon for numerical stability (default: 1e-6)
 *
 * @note weight and bias are optional. If nullptr, weight defaults to 1.0
 *       and bias defaults to 0.0
 * @note Uses FP32 accumulation for improved numerical accuracy
 *
 * @example
 * @code
 * // For Llama3.2: batch=1, seq=128, hidden=2048
 * const int batch = 1;
 * const int seq = 128;
 * const int hidden = 2048;
 * const float eps = 1e-6f;
 *
 * // Allocate tensors
 * bfloat16* input = ...;   // [batch, seq, hidden]
 * bfloat16* weight = ...;  // [hidden]
 * bfloat16* output = ...;  // [batch, seq, hidden]
 *
 * // Apply RMSNorm
 * rms_norm_fwd(input, weight, nullptr, output, batch, seq, hidden, eps);
 * @endcode
 */
template<typename T>
void rms_norm_fwd(
    const T* input,
    const T* weight,
    const T* bias,
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps = 1e-6f
);

/**
 * @brief Apply RMSNorm without bias (common case for Llama3.2)
 *
 * This is a convenience overload for the common case where bias is not used.
 *
 * @tparam T Data type
 *
 * @param input Input tensor [batch, seq, hidden]
 * @param weight Scale parameter [hidden]
 * @param output Output tensor [batch, seq, hidden]
 * @param batch Batch size
 * @param seq Sequence length
 * @param hidden Hidden dimension
 * @param eps Epsilon for numerical stability
 */
template<typename T>
void rms_norm_fwd(
    const T* input,
    const T* weight,
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps = 1e-6f
);

/**
 * @brief Apply RMSNorm without weight or bias (unit variance normalization)
 *
 * This variant normalizes to unit variance without learnable parameters.
 *
 * @tparam T Data type
 *
 * @param input Input tensor [batch, seq, hidden]
 * @param output Output tensor [batch, seq, hidden]
 * @param batch Batch size
 * @param seq Sequence length
 * @param hidden Hidden dimension
 * @param eps Epsilon for numerical stability
 */
template<typename T>
void rms_norm_fwd_simple(
    const T* input,
    T* output,
    int batch,
    int seq,
    int hidden,
    float eps = 1e-6f
);

} // namespace normalization
} // namespace operators
} // namespace iron
