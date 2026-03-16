// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file rope_bf16.hpp
 * @brief Rotary Positional Embedding (RoPE) operator implementation for bfloat16
 *
 * This header defines the RoPE operator for applying rotary positional
 * embeddings to query and key tensors in transformer attention mechanisms.
 *
 * The RoPE operation is defined as:
 *   q_embed = (q * cos) + (rotate_half(q) * sin)
 *   k_embed = (k * cos) + (rotate_half(k) * sin)
 *
 * where rotate_half splits the last dimension in half and rotates:
 *   rotate_half(x) = concat(-x[..., d/2:], x[..., :d/2])
 *
 * @note This implementation supports bfloat16 precision for AIE2/AIE2P architectures
 * @note Supports both interleaved (method_type=1) and two-halves (method_type=0) methods
 *
 * @see "RoFormer: Enhanced Transformer with Rotary Position Embedding" (Su et al., 2021)
 */

#pragma once

#include <cstdint>
#include <cstddef>

namespace iron {
namespace operators {
namespace rope {

/**
 * @brief Rotation method for RoPE
 */
enum class RotationMethod {
    TWO_HALVES = 0,   ///< Two-halves method (used in HuggingFace transformers)
    INTERLEAVED = 1    ///< Interleaved method (used in original Llama paper)
};

/**
 * @brief Apply Rotary Positional Embedding to query and key tensors
 *
 * This function applies RoPE to both query and key tensors in-place.
 * The rotation is applied along the last dimension (head_dim).
 *
 * @tparam T Data type (typically bfloat16 or float)
 *
 * @param q Query tensor [batch, heads, seq, head_dim]
 * @param k Key tensor [batch, heads, seq, head_dim]
 * @param cos Cosine cache [seq, head_dim/2] or [1, 1, seq, head_dim/2]
 * @param sin Sine cache [seq, head_dim/2] or [1, 1, seq, head_dim/2]
 * @param q_out Output query tensor [batch, heads, seq, head_dim]
 * @param k_out Output key tensor [batch, heads, seq, head_dim]
 * @param batch Batch size (number of sequences)
 * @param heads Number of attention heads
 * @param seq Sequence length
 * @param head_dim Head dimension (must be even, typically 64)
 * @param method Rotation method (default: TWO_HALVES)
 *
 * @note head_dim must be even for the rotation operation
 * @note cos and sin caches should be precomputed using compute_rope_params
 *
 * @example
 * @code
 * // For Llama3.2: batch=1, heads=32, seq=128, head_dim=64
 * const int batch = 1;
 * const int heads = 32;
 * const int seq = 128;
 * const int head_dim = 64;
 *
 * // Allocate tensors (assuming bfloat16)
 * bfloat16* q = ...;  // [batch, heads, seq, head_dim]
 * bfloat16* k = ...;  // [batch, heads, seq, head_dim]
 * bfloat16* cos = ...; // [seq, head_dim/2]
 * bfloat16* sin = ...; // [seq, head_dim/2]
 * bfloat16* q_out = ...;
 * bfloat16* k_out = ...;
 *
 * // Apply RoPE
 * rope_fwd(q, k, cos, sin, q_out, k_out, batch, heads, seq, head_dim);
 * @endcode
 */
template<typename T>
void rope_fwd(
    const T* q,
    const T* k,
    const T* cos,
    const T* sin,
    T* q_out,
    T* k_out,
    int batch,
    int heads,
    int seq,
    int head_dim,
    RotationMethod method = RotationMethod::TWO_HALVES
);

/**
 * @brief Rotate half of the last dimension (180 degree rotation)
 *
 * This function implements the rotate_half operation:
 *   rotate_half(x)[..., :d/2] = -x[..., d/2:]
 *   rotate_half(x)[..., d/2:] = x[..., :d/2]
 *
 * @tparam T Data type (typically bfloat16 or float)
 *
 * @param x Input tensor [..., head_dim]
 * @param out Output tensor [..., head_dim]
 * @param num_elements Total number of elements to process
 * @param head_dim Head dimension (must be even)
 *
 * @note This is a helper function used internally by rope_fwd
 */
template<typename T>
void rotate_half(
    const T* x,
    T* out,
    int num_elements,
    int head_dim
);

/**
 * @brief Apply RoPE to query tensor only (for decoder self-attention)
 *
 * In decoder self-attention, only query RoPE is needed during generation.
 *
 * @tparam T Data type
 *
 * @param q Query tensor [batch, heads, seq, head_dim]
 * @param cos Cosine cache [seq, head_dim/2]
 * @param sin Sine cache [seq, head_dim/2]
 * @param q_out Output query tensor
 * @param batch Batch size
 * @param heads Number of heads
 * @param seq Sequence length
 * @param head_dim Head dimension
 * @param method Rotation method
 */
template<typename T>
void rope_query_only(
    const T* q,
    const T* cos,
    const T* sin,
    T* q_out,
    int batch,
    int heads,
    int seq,
    int head_dim,
    RotationMethod method = RotationMethod::TWO_HALVES
);

} // namespace rope
} // namespace operators
} // namespace iron
