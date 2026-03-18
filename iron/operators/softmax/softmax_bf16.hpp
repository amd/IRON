// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file softmax_bf16.hpp
 * @brief Softmax activation function for bfloat16
 *
 * This header defines the Softmax operator for normalizing attention
 * weights in transformer attention mechanisms.
 *
 * The Softmax operation is defined as:
 *   softmax(x)[i] = exp(x[i] - max(x)) / sum(exp(x - max(x)))
 *
 * The implementation uses the numerically stable formulation:
 *   1. Subtract max for numerical stability
 *   2. Compute exp of shifted values
 *   3. Normalize by sum
 *
 * @note This implementation supports bfloat16 precision with FP32 accumulation
 * @note Softmax is applied along the last dimension by default
 *
 * @see "Attention Is All You Need" (Vaswani et al., 2017)
 */

#pragma once

#include <cstddef>
#include <cstdint>

namespace iron
{
namespace operators
{
namespace softmax
{

/**
 * @brief Apply Softmax activation function
 *
 * This function computes softmax along the last dimension:
 *   output[i, j] = exp(input[i, j] - max(input[i])) / sum(exp(input[i] - max(input[i])))
 *
 * @tparam T Data type (typically bfloat16 or float)
 *
 * @param input Input tensor [N, M] (flattened [batch*heads, seq])
 * @param output Output tensor [N, M]
 * @param N Number of rows (batch * heads)
 * @param M Number of columns (sequence length)
 *
 * @note Uses FP32 accumulation for numerical stability
 * @note Implements max subtraction for numerical stability
 *
 * @example
 * @code
 * // For attention weights: batch=1, heads=32, seq=128
 * const int batch = 1;
 * const int heads = 32;
 * const int seq = 128;
 * const int N = batch * heads;  // 32
 * const int M = seq;            // 128
 *
 * // Allocate tensors
 * bfloat16* input = ...;   // [N, M] = [32, 128]
 * bfloat16* output = ...;  // [N, M] = [32, 128]
 *
 * // Apply Softmax
 * softmax_fwd(input, output, N, M);
 * @endcode
 */
template <typename T> void softmax_fwd(const T *input, T *output, int N, int M);

/**
 * @brief Apply Softmax with scale factor (for attention scores)
 *
 * This variant applies a scale factor before softmax, commonly used
 * in scaled dot-product attention:
 *   output = softmax(input * scale)
 *
 * @tparam T Data type
 *
 * @param input Input tensor [N, M]
 * @param output Output tensor [N, M]
 * @param N Number of rows
 * @param M Number of columns
 * @param scale Scale factor (typically 1/sqrt(head_dim))
 */
template <typename T> void softmax_scaled_fwd(const T *input, T *output, int N, int M, float scale);

/**
 * @brief Apply Softmax along a specific dimension
 *
 * This variant allows specifying the dimension along which
 * to compute softmax.
 *
 * @tparam T Data type
 *
 * @param input Input tensor with arbitrary shape
 * @param output Output tensor (same shape)
 * @param shape Array of dimension sizes
 * @param dim Dimension along which to compute softmax (0-indexed)
 * @param num_dims Number of dimensions
 */
template <typename T> void softmax_along_dim(const T *input, T *output, const int *shape, int dim, int num_dims);

} // namespace softmax
} // namespace operators
} // namespace iron
