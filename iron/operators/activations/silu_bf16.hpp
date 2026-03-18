// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file silu_bf16.hpp
 * @brief SiLU (Sigmoid Linear Unit) activation function for bfloat16
 *
 * This header defines the SiLU activation operator, also known as Swish.
 * SiLU is a smooth, non-monotonic activation function used in modern
 * transformer architectures including Llama3.2.
 *
 * The SiLU operation is defined as:
 *   silu(x) = x * sigmoid(x)
 *           = x / (1 + exp(-x))
 *
 * Properties:
 * - Smooth and non-monotonic
 * - Bounded below (approaches 0 as x -> -inf)
 * - Unbounded above (approaches x as x -> inf)
 * - Has derivative: silu'(x) = sigmoid(x) + x * sigmoid(x) * (1 - sigmoid(x))
 *
 * @note This implementation supports bfloat16 precision
 * @note Uses tanh-based approximation for efficient sigmoid computation
 *
 * @see "Swish: a Self-Gated Activation Function" (Ramachandran et al., 2017)
 */

#pragma once

#include <cstddef>
#include <cstdint>

namespace iron
{
namespace operators
{
namespace activations
{

/**
 * @brief Apply SiLU (Sigmoid Linear Unit) activation function
 *
 * This function computes SiLU element-wise:
 *   output[i] = input[i] * sigmoid(input[i])
 *
 * The sigmoid is computed using the identity:
 *   sigmoid(x) = 0.5 * (1 + tanh(x / 2))
 *
 * @tparam T Data type (typically bfloat16 or float)
 *
 * @param input Input tensor of any shape
 * @param output Output tensor (same shape as input)
 * @param num_elements Total number of elements to process
 *
 * @note This is an element-wise operation, input and output can be the same
 *       pointer for in-place computation
 *
 * @example
 * @code
 * // For Llama3.2 MLP: batch=1, seq=128, hidden=8192
 * const int batch = 1;
 * const int seq = 128;
 * const int hidden = 8192;
 * const int num_elements = batch * seq * hidden;
 *
 * // Allocate tensors
 * bfloat16* input = ...;   // [batch, seq, hidden]
 * bfloat16* output = ...;  // [batch, seq, hidden]
 *
 * // Apply SiLU
 * silu_fwd(input, output, num_elements);
 * @endcode
 */
template <typename T> void silu_fwd(const T *input, T *output, int num_elements);

/**
 * @brief Apply SiLU activation in-place
 *
 * This variant performs in-place computation where input and output
 * share the same memory.
 *
 * @tparam T Data type
 *
 * @param input_output Tensor to transform in-place
 * @param num_elements Total number of elements
 */
template <typename T> void silu_inplace(T *input_output, int num_elements);

/**
 * @brief Apply SiLU with gating for SwiGLU
 *
 * SwiGLU is a gated variant used in Llama3.2 MLP:
 *   SwiGLU(x, gate) = SiLU(gate) * x
 *
 * @tparam T Data type
 *
 * @param input Input tensor to be gated
 * @param gate Gate tensor (same shape as input)
 * @param output Output tensor
 * @param num_elements Total number of elements
 */
template <typename T> void silu_gate(const T *input, const T *gate, T *output, int num_elements);

} // namespace activations
} // namespace operators
} // namespace iron
