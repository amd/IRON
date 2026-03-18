// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_softmax.cpp
 * @brief Unit tests for Softmax activation function
 *
 * This test suite validates the Softmax operator implementation:
 * - Basic forward pass functionality
 * - Output sums to 1 (normalization property)
 * - Output is positive
 * - Scaled softmax for attention
 * - Edge cases (large values, small values, uniform input)
 * - Numerical stability (max subtraction)
 *
 * @note Tests use Google Test framework
 * @note Reference values computed using PyTorch implementation
 */

#include <cmath>
#include <cstdint>
#include <gtest/gtest.h>
#include <limits>
#include <random>
#include <vector>

// Include the operator header
#include "iron/operators/softmax/softmax_bf16.hpp"

namespace iron
{
namespace operators
{
namespace softmax
{
namespace tests
{

//==============================================================================
// Test Fixtures
//==============================================================================

/**
 * @brief Test fixture for Softmax operator tests
 */
class SoftmaxTest : public ::testing::Test
{
  protected:
    void SetUp() override
    {
        // Initialize test parameters
        N_ = 4; // Number of rows (batch * heads)
        M_ = 8; // Number of columns (sequence length)

        input_.resize(N_ * M_);
        output_.resize(N_ * M_);

        // Initialize with random values
        std::mt19937 gen(42);
        std::uniform_real_distribution<float> dist(-2.0f, 2.0f);

        for (size_t i = 0; i < input_.size(); ++i) {
            input_[i] = bfloat16(dist(gen));
        }
    }

    void TearDown() override
    {
        // Cleanup
    }

    // Compute reference softmax using standard math
    std::vector<float> reference_softmax(const std::vector<bfloat16> &input, int N, int M) const
    {
        std::vector<float> output(N * M);

        for (int n = 0; n < N; ++n) {
            const int row_offset = n * M;

            // Find max
            float max_val = static_cast<float>(input[row_offset]);
            for (int m = 1; m < M; ++m) {
                max_val = std::max(max_val, static_cast<float>(input[row_offset + m]));
            }

            // Compute exp and sum
            float sum_exp = 0.0f;
            for (int m = 0; m < M; ++m) {
                const float shifted = static_cast<float>(input[row_offset + m]) - max_val;
                output[row_offset + m] = std::exp(shifted);
                sum_exp += output[row_offset + m];
            }

            // Normalize
            for (int m = 0; m < M; ++m) {
                output[row_offset + m] /= sum_exp;
            }
        }

        return output;
    }

    // Test parameters
    int N_;
    int M_;

    // Test data
    std::vector<bfloat16> input_;
    std::vector<bfloat16> output_;
};

//==============================================================================
// Basic Functionality Tests
//==============================================================================

/**
 * @test Verify Softmax forward pass produces finite outputs
 */
TEST_F(SoftmaxTest, ForwardPassFinite)
{
    softmax_fwd(input_.data(), output_.data(), N_, M_);

    // Verify all outputs are finite
    for (size_t i = 0; i < output_.size(); ++i) {
        float val = static_cast<float>(output_[i]);
        EXPECT_TRUE(std::isfinite(val)) << "output[" << i << "] is not finite";
    }
}

/**
 * @test Verify Softmax output sums to 1 for each row
 */
TEST_F(SoftmaxTest, OutputSumsToOne)
{
    softmax_fwd(input_.data(), output_.data(), N_, M_);

    // Check each row sums to 1
    for (int n = 0; n < N_; ++n) {
        const int row_offset = n * M_;
        float row_sum = 0.0f;

        for (int m = 0; m < M_; ++m) {
            row_sum += static_cast<float>(output_[row_offset + m]);
        }

        EXPECT_NEAR(row_sum, 1.0f, 0.01f) << "Row " << n << " should sum to 1";
    }
}

/**
 * @test Verify Softmax output is positive
 */
TEST_F(SoftmaxTest, OutputIsPositive)
{
    softmax_fwd(input_.data(), output_.data(), N_, M_);

    // Check all outputs are positive
    for (size_t i = 0; i < output_.size(); ++i) {
        const float val = static_cast<float>(output_[i]);
        EXPECT_GT(val, 0.0f) << "Softmax output should be positive at index " << i;
    }
}

//==============================================================================
// Mathematical Correctness Tests
//==============================================================================

/**
 * @test Verify Softmax against reference implementation
 */
TEST_F(SoftmaxTest, MathematicalCorrectness)
{
    softmax_fwd(input_.data(), output_.data(), N_, M_);

    // Compute reference
    std::vector<float> reference = reference_softmax(input_, N_, M_);

    // Compare
    for (size_t i = 0; i < output_.size(); ++i) {
        const float expected = reference[i];
        const float actual = static_cast<float>(output_[i]);

        // Allow tolerance for bfloat16 precision
        const float tol = 0.05f;
        EXPECT_NEAR(actual, expected, tol)
            << "Softmax mismatch at index " << i << " (expected=" << expected << ", actual=" << actual << ")";
    }
}

/**
 * @test Verify Softmax with uniform input produces uniform output
 */
TEST_F(SoftmaxTest, UniformInput)
{
    // Set all inputs to same value
    std::vector<bfloat16> uniform_input(N_ * M_, bfloat16(5.0f));
    std::vector<bfloat16> uniform_output(N_ * M_);

    softmax_fwd(uniform_input.data(), uniform_output.data(), N_, M_);

    // Each row should be uniform with value 1/M
    const float expected = 1.0f / static_cast<float>(M_);

    for (size_t i = 0; i < uniform_output.size(); ++i) {
        const float actual = static_cast<float>(uniform_output[i]);
        EXPECT_NEAR(actual, expected, 0.01f) << "Uniform input should produce uniform output";
    }
}

/**
 * @test Verify Softmax with large positive values (numerical stability)
 */
TEST_F(SoftmaxTest, LargePositiveValues)
{
    std::vector<bfloat16> large_input(N_ * M_, bfloat16(100.0f));
    std::vector<bfloat16> large_output(N_ * M_);

    softmax_fwd(large_input.data(), large_output.data(), N_, M_);

    // Should still sum to 1 (no overflow)
    for (int n = 0; n < N_; ++n) {
        const int row_offset = n * M_;
        float row_sum = 0.0f;

        for (int m = 0; m < M_; ++m) {
            row_sum += static_cast<float>(large_output[row_offset + m]);
        }

        EXPECT_NEAR(row_sum, 1.0f, 0.01f) << "Large values should still sum to 1";
    }
}

/**
 * @test Verify Softmax with large negative values (numerical stability)
 */
TEST_F(SoftmaxTest, LargeNegativeValues)
{
    std::vector<bfloat16> negative_input(N_ * M_, bfloat16(-100.0f));
    std::vector<bfloat16> negative_output(N_ * M_);

    softmax_fwd(negative_input.data(), negative_output.data(), N_, M_);

    // Should still sum to 1 (no underflow issues)
    for (int n = 0; n < N_; ++n) {
        const int row_offset = n * M_;
        float row_sum = 0.0f;

        for (int m = 0; m < M_; ++m) {
            row_sum += static_cast<float>(negative_output[row_offset + m]);
        }

        EXPECT_NEAR(row_sum, 1.0f, 0.01f) << "Large negative values should still sum to 1";
    }
}

//==============================================================================
// Scaled Softmax Tests
//==============================================================================

/**
 * @test Verify scaled softmax for attention
 */
TEST_F(SoftmaxTest, ScaledSoftmax)
{
    const float scale = 0.125f; // 1/sqrt(64) for head_dim=64

    softmax_scaled_fwd(input_.data(), output_.data(), N_, M_, scale);

    // Verify outputs are finite
    for (size_t i = 0; i < output_.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(output_[i])));
    }

    // Verify row sums to 1
    for (int n = 0; n < N_; ++n) {
        const int row_offset = n * M_;
        float row_sum = 0.0f;

        for (int m = 0; m < M_; ++m) {
            row_sum += static_cast<float>(output_[row_offset + m]);
        }

        EXPECT_NEAR(row_sum, 1.0f, 0.01f);
    }
}

/**
 * @test Verify scaled softmax with attention-scale (1/sqrt(d_k))
 */
TEST_F(SoftmaxTest, AttentionScale)
{
    const int head_dim = 64;
    const float scale = 1.0f / std::sqrt(static_cast<float>(head_dim));

    // Create attention scores (query @ key^T)
    std::vector<bfloat16> attention_scores(N_ * M_);
    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-10.0f, 10.0f);

    for (size_t i = 0; i < attention_scores.size(); ++i) {
        attention_scores[i] = bfloat16(dist(gen));
    }

    softmax_scaled_fwd(attention_scores.data(), output_.data(), N_, M_, scale);

    // Verify outputs are valid probabilities
    for (size_t i = 0; i < output_.size(); ++i) {
        const float val = static_cast<float>(output_[i]);
        EXPECT_GE(val, 0.0f) << "Softmax output should be non-negative";
        EXPECT_LE(val, 1.0f) << "Softmax output should be <= 1";
    }
}

//==============================================================================
// Edge Case Tests
//==============================================================================

/**
 * @test Test with small sequence length
 */
TEST_F(SoftmaxTest, SmallSequenceLength)
{
    M_ = 2;
    input_.resize(N_ * M_);
    output_.resize(N_ * M_);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-2.0f, 2.0f);

    for (size_t i = 0; i < input_.size(); ++i) {
        input_[i] = bfloat16(dist(gen));
    }

    softmax_fwd(input_.data(), output_.data(), N_, M_);

    // Verify row sums
    for (int n = 0; n < N_; ++n) {
        float row_sum = 0.0f;
        for (int m = 0; m < M_; ++m) {
            row_sum += static_cast<float>(output_[n * M_ + m]);
        }
        EXPECT_NEAR(row_sum, 1.0f, 0.01f);
    }
}

/**
 * @test Test with large sequence length
 */
TEST_F(SoftmaxTest, LargeSequenceLength)
{
    M_ = 512; // Typical context length
    input_.resize(N_ * M_);
    output_.resize(N_ * M_);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-2.0f, 2.0f);

    for (size_t i = 0; i < input_.size(); ++i) {
        input_[i] = bfloat16(dist(gen));
    }

    softmax_fwd(input_.data(), output_.data(), N_, M_);

    // Verify row sums
    for (int n = 0; n < N_; ++n) {
        float row_sum = 0.0f;
        for (int m = 0; m < M_; ++m) {
            row_sum += static_cast<float>(output_[n * M_ + m]);
        }
        EXPECT_NEAR(row_sum, 1.0f, 0.01f);
    }
}

/**
 * @test Test with single row
 */
TEST_F(SoftmaxTest, SingleRow)
{
    N_ = 1;
    output_.resize(M_);

    softmax_fwd(input_.data(), output_.data(), N_, M_);

    float row_sum = 0.0f;
    for (int m = 0; m < M_; ++m) {
        row_sum += static_cast<float>(output_[m]);
    }

    EXPECT_NEAR(row_sum, 1.0f, 0.01f);
}

/**
 * @test Test with max value at different positions
 */
TEST_F(SoftmaxTest, MaxValuePosition)
{
    // Create input where max is at different positions for each row
    std::vector<bfloat16> shifted_input(N_ * M_, bfloat16(0.0f));

    for (int n = 0; n < N_; ++n) {
        const int max_pos = (n * M_) / N_; // Different max position per row
        shifted_input[n * M_ + max_pos] = bfloat16(10.0f);
    }

    softmax_fwd(shifted_input.data(), output_.data(), N_, M_);

    // Each row should have highest probability at max position
    for (int n = 0; n < N_; ++n) {
        const int max_pos = (n * M_) / N_;
        float max_prob = static_cast<float>(output_[n * M_ + max_pos]);

        for (int m = 0; m < M_; ++m) {
            if (m != max_pos) {
                const float prob = static_cast<float>(output_[n * M_ + m]);
                EXPECT_LT(prob, max_prob) << "Max position should have highest probability";
            }
        }
    }
}

} // namespace tests
} // namespace softmax
} // namespace operators
} // namespace iron

//==============================================================================
// Main Test Entry Point
//==============================================================================

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
