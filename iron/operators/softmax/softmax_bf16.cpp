// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file softmax_bf16.cpp
 * @brief Implementation of Softmax activation function
 *
 * This file contains the implementation of Softmax for bfloat16 precision,
 * optimized for CPU execution with numerical stability.
 *
 * Key features:
 * - Numerically stable computation (max subtraction)
 * - FP32 accumulation for accuracy
 * - Support for scaled softmax (attention)
 *
 * @note For best performance, ensure input tensors are properly aligned
 */

#include "softmax_bf16.hpp"

#include "types.hpp"

#include <cmath>
#include <cstring>

namespace iron
{
namespace operators
{
namespace softmax
{

//==============================================================================
// softmax_fwd Implementation
//==============================================================================

template <typename T> void softmax_fwd(const T *input, T *output, int N, int M)
{
    // Process each row
    for (int n = 0; n < N; ++n) {
        const int row_offset = n * M;

        // Step 1: Find maximum value in the row (for numerical stability)
        float max_val = static_cast<float>(input[row_offset]);
        for (int m = 1; m < M; ++m) {
            const float val = static_cast<float>(input[row_offset + m]);
            if (val > max_val) {
                max_val = val;
            }
        }

        // Step 2: Compute exp(x - max) and sum
        float sum_exp = 0.0f;
        for (int m = 0; m < M; ++m) {
            const float shifted = static_cast<float>(input[row_offset + m]) - max_val;
            const float exp_val = std::exp(shifted);
            output[row_offset + m] = bfloat16(exp_val);
            sum_exp += exp_val;
        }

        // Step 3: Normalize by sum (use kEpsilon for numerical stability)
        const float inv_sum = 1.0f / (sum_exp + kEpsilon);
        for (int m = 0; m < M; ++m) {
            const float normalized = static_cast<float>(output[row_offset + m]) * inv_sum;
            output[row_offset + m] = bfloat16(normalized);
        }
    }
}

// Explicit template instantiation for bfloat16
template void softmax_fwd<bfloat16>(const bfloat16 *, bfloat16 *, int, int);

//==============================================================================
// softmax_scaled_fwd Implementation
//==============================================================================

template <typename T> void softmax_scaled_fwd(const T *input, T *output, int N, int M, float scale)
{
    // Process each row
    for (int n = 0; n < N; ++n) {
        const int row_offset = n * M;

        // Step 1: Find maximum value (after scaling)
        float max_val = static_cast<float>(input[row_offset]) * scale;
        for (int m = 1; m < M; ++m) {
            const float val = static_cast<float>(input[row_offset + m]) * scale;
            if (val > max_val) {
                max_val = val;
            }
        }

        // Step 2: Compute exp(scaled_x - max) and sum
        float sum_exp = 0.0f;
        for (int m = 0; m < M; ++m) {
            const float scaled = static_cast<float>(input[row_offset + m]) * scale;
            const float shifted = scaled - max_val;
            const float exp_val = std::exp(shifted);
            output[row_offset + m] = bfloat16(exp_val);
            sum_exp += exp_val;
        }

        // Step 3: Normalize by sum (use kEpsilon for numerical stability)
        const float inv_sum = 1.0f / (sum_exp + kEpsilon);
        for (int m = 0; m < M; ++m) {
            const float normalized = static_cast<float>(output[row_offset + m]) * inv_sum;
            output[row_offset + m] = bfloat16(normalized);
        }
    }
}

// Explicit template instantiation for bfloat16
template void softmax_scaled_fwd<bfloat16>(const bfloat16 *, bfloat16 *, int, int, float);

//==============================================================================
// softmax_along_dim Implementation
//==============================================================================

template <typename T> void softmax_along_dim(const T *input, T *output, const int *shape, int dim, int num_dims)
{
    // Compute stride information
    int outer_size = 1; // Product of dimensions before 'dim'
    int dim_size = shape[dim];
    int inner_size = 1; // Product of dimensions after 'dim'

    for (int i = 0; i < dim; ++i) {
        outer_size *= shape[i];
    }
    for (int i = dim + 1; i < num_dims; ++i) {
        inner_size *= shape[i];
    }

    const int total_size = outer_size * dim_size * inner_size;

    // Process each "slice" along the softmax dimension
    for (int outer = 0; outer < outer_size; ++outer) {
        const int outer_offset = outer * dim_size * inner_size;

        // Process each inner element
        for (int inner = 0; inner < inner_size; ++inner) {
            // Find max value along the softmax dimension
            float max_val = -std::numeric_limits<float>::infinity();
            for (int d = 0; d < dim_size; ++d) {
                const int idx = outer_offset + d * inner_size + inner;
                const float val = static_cast<float>(input[idx]);
                if (val > max_val) {
                    max_val = val;
                }
            }

            // Compute exp(x - max) and sum
            float sum_exp = 0.0f;
            for (int d = 0; d < dim_size; ++d) {
                const int idx = outer_offset + d * inner_size + inner;
                const float shifted = static_cast<float>(input[idx]) - max_val;
                const float exp_val = std::exp(shifted);
                output[idx] = bfloat16(exp_val);
                sum_exp += exp_val;
            }

            // Normalize by sum (use kEpsilon for numerical stability)
            const float inv_sum = 1.0f / (sum_exp + kEpsilon);
            for (int d = 0; d < dim_size; ++d) {
                const int idx = outer_offset + d * inner_size + inner;
                const float normalized = static_cast<float>(output[idx]) * inv_sum;
                output[idx] = bfloat16(normalized);
            }
        }
    }
}

// Explicit template instantiation for bfloat16
template void softmax_along_dim<bfloat16>(const bfloat16 *, bfloat16 *, const int *, int, int);

} // namespace softmax
} // namespace operators
} // namespace iron
