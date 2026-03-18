// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file rope_bf16.cpp
 * @brief Implementation of Rotary Positional Embedding (RoPE) operator
 *
 * This file contains the implementation of RoPE for bfloat16 precision,
 * optimized for CPU execution with SIMD vectorization where available.
 *
 * The implementation supports two rotation methods:
 * - TWO_HALVES: Used by HuggingFace transformers
 * - INTERLEAVED: Used in the original Llama paper
 *
 * @note For best performance, ensure input tensors are properly aligned
 * @note Uses FP32 accumulation for improved numerical accuracy
 */

#include "rope_bf16.hpp"

#include "types.hpp"

#include <cmath>
#include <cstring>

namespace iron
{
namespace operators
{
namespace rope
{

/**
 * @brief Internal helper: compute negative of bfloat16
 */
inline bfloat16 bf16_neg(bfloat16 x)
{
    return bfloat16(-static_cast<float>(x));
}

/**
 * @brief Internal helper: multiply two bfloat16 values with FP32 accumulation
 */
inline bfloat16 bf16_mul(bfloat16 a, bfloat16 b)
{
    return bfloat16(static_cast<float>(a) * static_cast<float>(b));
}

/**
 * @brief Internal helper: add two bfloat16 values with FP32 accumulation
 */
inline bfloat16 bf16_add(bfloat16 a, bfloat16 b)
{
    return bfloat16(static_cast<float>(a) + static_cast<float>(b));
}

/**
 * @brief Internal helper: subtract two bfloat16 values
 */
inline bfloat16 bf16_sub(bfloat16 a, bfloat16 b)
{
    return bfloat16(static_cast<float>(a) - static_cast<float>(b));
}

//==============================================================================
// rotate_half Implementation
//==============================================================================

template <typename T> void rotate_half(const T *x, T *out, int num_elements, int head_dim)
{
    const int half_dim = head_dim / 2;

    // Process each sequence position
    for (int i = 0; i < num_elements; i += head_dim) {
        // First half: -x[..., d/2:]
        for (int j = 0; j < half_dim; ++j) {
            out[i + j] = bf16_neg(x[i + j + half_dim]);
        }
        // Second half: x[..., :d/2]
        for (int j = half_dim; j < head_dim; ++j) {
            out[i + j] = x[i + j - half_dim];
        }
    }
}

// Explicit template instantiation for bfloat16
template void rotate_half<bfloat16>(const bfloat16 *, bfloat16 *, int, int);

//==============================================================================
// rope_fwd Implementation - Two Halves Method
//==============================================================================

template <typename T>
void rope_fwd_two_halves(const T *q,
                         const T *k,
                         const T *cos,
                         const T *sin,
                         T *q_out,
                         T *k_out,
                         int batch,
                         int heads,
                         int seq,
                         int head_dim)
{
    const int half_dim = head_dim / 2;
    const int total_tokens = batch * heads * seq;

    // Process each token (batch * heads * seq)
    for (int t = 0; t < total_tokens; ++t) {
        const int token_offset = t * head_dim;
        const int seq_idx = t % seq;
        const int angle_offset = seq_idx * half_dim;

        // Process query embeddings
        for (int d = 0; d < half_dim; ++d) {
            const float q1 = static_cast<float>(q[token_offset + d]);
            const float q2 = static_cast<float>(q[token_offset + d + half_dim]);
            const float c = static_cast<float>(cos[angle_offset + d]);
            const float s = static_cast<float>(sin[angle_offset + d]);

            // q_embed[..., d] = q1 * cos - q2 * sin
            q_out[token_offset + d] = bfloat16(q1 * c - q2 * s);
            // q_embed[..., d + half_dim] = q2 * cos + q1 * sin
            q_out[token_offset + d + half_dim] = bfloat16(q2 * c + q1 * s);
        }

        // Process key embeddings
        for (int d = 0; d < half_dim; ++d) {
            const float k1 = static_cast<float>(k[token_offset + d]);
            const float k2 = static_cast<float>(k[token_offset + d + half_dim]);
            const float c = static_cast<float>(cos[angle_offset + d]);
            const float s = static_cast<float>(sin[angle_offset + d]);

            // k_embed[..., d] = k1 * cos - k2 * sin
            k_out[token_offset + d] = bfloat16(k1 * c - k2 * s);
            // k_embed[..., d + half_dim] = k2 * cos + k1 * sin
            k_out[token_offset + d + half_dim] = bfloat16(k2 * c + k1 * s);
        }
    }
}

//==============================================================================
// rope_fwd Implementation - Interleaved Method
//==============================================================================

template <typename T>
void rope_fwd_interleaved(const T *q,
                          const T *k,
                          const T *cos,
                          const T *sin,
                          T *q_out,
                          T *k_out,
                          int batch,
                          int heads,
                          int seq,
                          int head_dim)
{
    const int half_dim = head_dim / 2;
    const int total_tokens = batch * heads * seq;

    // Process each token
    for (int t = 0; t < total_tokens; ++t) {
        const int token_offset = t * head_dim;
        const int seq_idx = t % seq;
        const int angle_offset = seq_idx * half_dim;

        // Process query embeddings (interleaved pattern)
        for (int d = 0; d < half_dim; ++d) {
            const int even_idx = d * 2;    // Even position: 2*d
            const int odd_idx = d * 2 + 1; // Odd position: 2*d + 1

            const float q_even = static_cast<float>(q[token_offset + even_idx]);
            const float q_odd = static_cast<float>(q[token_offset + odd_idx]);
            const float c = static_cast<float>(cos[angle_offset + d]);
            const float s = static_cast<float>(sin[angle_offset + d]);

            // q_rot[..., 2*d] = q_even * cos - q_odd * sin
            q_out[token_offset + even_idx] = bfloat16(q_even * c - q_odd * s);
            // q_rot[..., 2*d + 1] = q_even * sin + q_odd * cos
            q_out[token_offset + odd_idx] = bfloat16(q_even * s + q_odd * c);
        }

        // Process key embeddings (interleaved pattern)
        for (int d = 0; d < half_dim; ++d) {
            const int even_idx = d * 2;
            const int odd_idx = d * 2 + 1;

            const float k_even = static_cast<float>(k[token_offset + even_idx]);
            const float k_odd = static_cast<float>(k[token_offset + odd_idx]);
            const float c = static_cast<float>(cos[angle_offset + d]);
            const float s = static_cast<float>(sin[angle_offset + d]);

            // k_rot[..., 2*d] = k_even * cos - k_odd * sin
            k_out[token_offset + even_idx] = bfloat16(k_even * c - k_odd * s);
            // k_rot[..., 2*d + 1] = k_even * sin + k_odd * cos
            k_out[token_offset + odd_idx] = bfloat16(k_even * s + k_odd * c);
        }
    }
}

//==============================================================================
// Main rope_fwd Template Implementation
//==============================================================================

template <typename T>
void rope_fwd(const T *q,
              const T *k,
              const T *cos,
              const T *sin,
              T *q_out,
              T *k_out,
              int batch,
              int heads,
              int seq,
              int head_dim,
              RotationMethod method)
{
    // Validate inputs
    if (head_dim <= 0 || head_dim % 2 != 0) {
        // Invalid head dimension - head_dim must be positive and even
        // In debug builds, this could trigger an assertion
        return;
    }

    switch (method) {
    case RotationMethod::TWO_HALVES:
        rope_fwd_two_halves(q, k, cos, sin, q_out, k_out, batch, heads, seq, head_dim);
        break;
    case RotationMethod::INTERLEAVED:
        rope_fwd_interleaved(q, k, cos, sin, q_out, k_out, batch, heads, seq, head_dim);
        break;
    default:
        // Default to two-halves method
        rope_fwd_two_halves(q, k, cos, sin, q_out, k_out, batch, heads, seq, head_dim);
        break;
    }
}

// Explicit template instantiation for bfloat16
template void rope_fwd<bfloat16>(const bfloat16 *,
                                 const bfloat16 *,
                                 const bfloat16 *,
                                 const bfloat16 *,
                                 bfloat16 *,
                                 bfloat16 *,
                                 int,
                                 int,
                                 int,
                                 int,
                                 RotationMethod);

//==============================================================================
// rope_query_only Implementation
//==============================================================================

template <typename T>
void rope_query_only(const T *q,
                     const T *cos,
                     const T *sin,
                     T *q_out,
                     int batch,
                     int heads,
                     int seq,
                     int head_dim,
                     RotationMethod method)
{
    const int half_dim = head_dim / 2;
    const int total_tokens = batch * heads * seq;

    if (method == RotationMethod::INTERLEAVED) {
        // Interleaved method for query only
        for (int t = 0; t < total_tokens; ++t) {
            const int token_offset = t * head_dim;
            const int seq_idx = t % seq;
            const int angle_offset = seq_idx * half_dim;

            for (int d = 0; d < half_dim; ++d) {
                const int even_idx = d * 2;
                const int odd_idx = d * 2 + 1;

                const float q_even = static_cast<float>(q[token_offset + even_idx]);
                const float q_odd = static_cast<float>(q[token_offset + odd_idx]);
                const float c = static_cast<float>(cos[angle_offset + d]);
                const float s = static_cast<float>(sin[angle_offset + d]);

                q_out[token_offset + even_idx] = bfloat16(q_even * c - q_odd * s);
                q_out[token_offset + odd_idx] = bfloat16(q_even * s + q_odd * c);
            }
        }
    } else {
        // Two-halves method for query only
        for (int t = 0; t < total_tokens; ++t) {
            const int token_offset = t * head_dim;
            const int seq_idx = t % seq;
            const int angle_offset = seq_idx * half_dim;

            for (int d = 0; d < half_dim; ++d) {
                const float q1 = static_cast<float>(q[token_offset + d]);
                const float q2 = static_cast<float>(q[token_offset + d + half_dim]);
                const float c = static_cast<float>(cos[angle_offset + d]);
                const float s = static_cast<float>(sin[angle_offset + d]);

                q_out[token_offset + d] = bfloat16(q1 * c - q2 * s);
                q_out[token_offset + d + half_dim] = bfloat16(q2 * c + q1 * s);
            }
        }
    }
}

// Explicit template instantiation for bfloat16
template void rope_query_only<bfloat16>(const bfloat16 *,
                                        const bfloat16 *,
                                        const bfloat16 *,
                                        bfloat16 *,
                                        int,
                                        int,
                                        int,
                                        int,
                                        RotationMethod);

} // namespace rope
} // namespace operators
} // namespace iron
