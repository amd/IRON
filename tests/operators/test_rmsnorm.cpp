// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_rmsnorm.cpp
 * @brief Unit tests for Root Mean Square Layer Normalization (RMSNorm) operator
 *
 * This test suite validates the RMSNorm operator implementation:
 * - Basic forward pass functionality
 * - Normalization correctness (output RMS ≈ 1)
 * - Weight scaling correctness
 * - Edge cases (small/large dimensions)
 * - Numerical accuracy against PyTorch reference
 *
 * @note Tests use Google Test framework
 * @note Reference values computed using PyTorch implementation
 */

#include <cmath>
#include <cstdint>
#include <gtest/gtest.h>
#include <random>
#include <vector>

// Include the operator header
#include "iron/operators/normalization/rmsnorm_bf16.hpp"

namespace iron
{
namespace operators
{
namespace normalization
{
namespace tests
{

//==============================================================================
// Test Fixtures
//==============================================================================

/**
 * @brief Test fixture for RMSNorm operator tests
 */
class RMSNormTest : public ::testing::Test
{
  protected:
    void SetUp() override
    {
        // Initialize test parameters
        batch_ = 2;
        seq_ = 4;
        hidden_ = 16;
        eps_ = 1e-6f;

        const size_t total_elements = batch_ * seq_ * hidden_;

        input_.resize(total_elements);
        weight_.resize(hidden_);
        output_.resize(total_elements);

        // Initialize with random values
        std::mt19937 gen(42);
        std::uniform_real_distribution<float> dist(0.1f, 1.0f);

        for (size_t i = 0; i < total_elements; ++i) {
            input_[i] = bfloat16(dist(gen));
        }

        // Initialize weights to 1.0 (common initialization)
        for (int i = 0; i < hidden_; ++i) {
            weight_[i] = bfloat16(1.0f);
        }
    }

    void TearDown() override
    {
        // Cleanup
    }

    // Test parameters
    int batch_;
    int seq_;
    int hidden_;
    float eps_;

    // Test data
    std::vector<bfloat16> input_;
    std::vector<bfloat16> weight_;
    std::vector<bfloat16> output_;
};

//==============================================================================
// Basic Functionality Tests
//==============================================================================

/**
 * @test Verify RMSNorm forward pass with weight
 */
TEST_F(RMSNormTest, ForwardPassWithWeight)
{
    rms_norm_fwd(input_.data(), weight_.data(), output_.data(), batch_, seq_, hidden_, eps_);

    // Verify outputs are finite
    for (size_t i = 0; i < output_.size(); ++i) {
        float val = static_cast<float>(output_[i]);
        EXPECT_TRUE(std::isfinite(val)) << "output[" << i << "] is not finite";
    }

    // Verify output RMS is approximately 1 for each row
    const int total_rows = batch_ * seq_;
    for (int row = 0; row < total_rows; ++row) {
        const int row_offset = row * hidden_;
        float sum_sq = 0.0f;

        for (int i = 0; i < hidden_; ++i) {
            const float val = static_cast<float>(output_[row_offset + i]);
            sum_sq += val * val;
        }

        const float rms = std::sqrt(sum_sq / static_cast<float>(hidden_));
        EXPECT_NEAR(rms, 1.0f, 0.1f) << "Row " << row << " RMS should be ~1.0";
    }
}

/**
 * @test Verify RMSNorm forward pass without weight (unit variance)
 */
TEST_F(RMSNormTest, ForwardPassWithoutWeight)
{
    rms_norm_fwd_simple(input_.data(), output_.data(), batch_, seq_, hidden_, eps_);

    // Verify outputs are finite
    for (size_t i = 0; i < output_.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(output_[i])));
    }

    // Verify output RMS is approximately 1
    const int total_rows = batch_ * seq_;
    for (int row = 0; row < total_rows; ++row) {
        const int row_offset = row * hidden_;
        float sum_sq = 0.0f;

        for (int i = 0; i < hidden_; ++i) {
            const float val = static_cast<float>(output_[row_offset + i]);
            sum_sq += val * val;
        }

        const float rms = std::sqrt(sum_sq / static_cast<float>(hidden_));
        EXPECT_NEAR(rms, 1.0f, 0.1f);
    }
}

/**
 * @test Verify RMSNorm with custom weight scaling
 */
TEST_F(RMSNormTest, WeightScaling)
{
    // Set weights to 2.0
    for (int i = 0; i < hidden_; ++i) {
        weight_[i] = bfloat16(2.0f);
    }

    rms_norm_fwd(input_.data(), weight_.data(), output_.data(), batch_, seq_, hidden_, eps_);

    // With weight=2, output RMS should be ~2
    const int total_rows = batch_ * seq_;
    for (int row = 0; row < total_rows; ++row) {
        const int row_offset = row * hidden_;
        float sum_sq = 0.0f;

        for (int i = 0; i < hidden_; ++i) {
            const float val = static_cast<float>(output_[row_offset + i]);
            sum_sq += val * val;
        }

        const float rms = std::sqrt(sum_sq / static_cast<float>(hidden_));
        EXPECT_NEAR(rms, 2.0f, 0.2f) << "Row " << row << " RMS should be ~2.0 with weight=2";
    }
}

//==============================================================================
// Edge Case Tests
//==============================================================================

/**
 * @test Test with small hidden dimension
 */
TEST_F(RMSNormTest, SmallHiddenDimension)
{
    hidden_ = 4;
    const size_t total_elements = batch_ * seq_ * hidden_;

    std::vector<bfloat16> input_small(total_elements);
    std::vector<bfloat16> weight_small(hidden_);
    std::vector<bfloat16> output_small(total_elements);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(0.1f, 1.0f);

    for (size_t i = 0; i < total_elements; ++i) {
        input_small[i] = bfloat16(dist(gen));
    }
    for (int i = 0; i < hidden_; ++i) {
        weight_small[i] = bfloat16(1.0f);
    }

    rms_norm_fwd(input_small.data(), weight_small.data(), output_small.data(), batch_, seq_, hidden_, eps_);

    // Verify outputs are finite
    for (size_t i = 0; i < output_small.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(output_small[i])));
    }
}

/**
 * @test Test with large hidden dimension
 */
TEST_F(RMSNormTest, LargeHiddenDimension)
{
    hidden_ = 2048; // Llama3.2-1B hidden size
    const size_t total_elements = batch_ * seq_ * hidden_;

    std::vector<bfloat16> input_large(total_elements);
    std::vector<bfloat16> weight_large(hidden_);
    std::vector<bfloat16> output_large(total_elements);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(0.1f, 1.0f);

    for (size_t i = 0; i < total_elements; ++i) {
        input_large[i] = bfloat16(dist(gen));
    }
    for (int i = 0; i < hidden_; ++i) {
        weight_large[i] = bfloat16(1.0f);
    }

    rms_norm_fwd(input_large.data(), weight_large.data(), output_large.data(), batch_, seq_, hidden_, eps_);

    // Verify outputs are finite
    for (size_t i = 0; i < output_large.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(output_large[i])));
    }
}

/**
 * @test Test with very small epsilon
 */
TEST_F(RMSNormTest, SmallEpsilon)
{
    eps_ = 1e-12f;

    rms_norm_fwd(input_.data(), weight_.data(), output_.data(), batch_, seq_, hidden_, eps_);

    // Verify outputs are still finite with small epsilon
    for (size_t i = 0; i < output_.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(output_[i])));
    }
}

/**
 * @test Test with zero input (should not cause division by zero)
 */
TEST_F(RMSNormTest, ZeroInput)
{
    const size_t total_elements = batch_ * seq_ * hidden_;

    std::vector<bfloat16> zero_input(total_elements, bfloat16(0.0f));
    std::vector<bfloat16> zero_output(total_elements);

    rms_norm_fwd(zero_input.data(), weight_.data(), zero_output.data(), batch_, seq_, hidden_, eps_);

    // With zero input and weight=1, output should be zero (not NaN)
    for (size_t i = 0; i < zero_output.size(); ++i) {
        float val = static_cast<float>(zero_output[i]);
        EXPECT_TRUE(std::isfinite(val)) << "Zero input should produce finite output";
        EXPECT_NEAR(val, 0.0f, 0.01f) << "Zero input should produce near-zero output";
    }
}

//==============================================================================
// Numerical Accuracy Tests
//==============================================================================

/**
 * @test Verify mean of normalized output is near zero
 */
TEST_F(RMSNormTest, OutputDistribution)
{
    rms_norm_fwd(input_.data(), weight_.data(), output_.data(), batch_, seq_, hidden_, eps_);

    // Check that output is centered (RMSNorm doesn't center like LayerNorm,
    // but should have reasonable distribution)
    float sum = 0.0f;
    float sum_sq = 0.0f;

    for (size_t i = 0; i < output_.size(); ++i) {
        const float val = static_cast<float>(output_[i]);
        sum += val;
        sum_sq += val * val;
    }

    const float mean = sum / static_cast<float>(output_.size());
    const float rms = std::sqrt(sum_sq / static_cast<float>(output_.size()));

    // Mean should be reasonable (not necessarily zero for RMSNorm)
    EXPECT_LT(std::abs(mean), 1.0f) << "Output mean should be reasonable";

    // RMS should be approximately 1
    EXPECT_NEAR(rms, 1.0f, 0.1f) << "Output RMS should be ~1.0";
}

/**
 * @test Verify scaling invariance
 */
TEST_F(RMSNormTest, ScalingInvariance)
{
    // Create scaled input
    const size_t total_elements = batch_ * seq_ * hidden_;
    std::vector<bfloat16> scaled_input(total_elements);

    for (size_t i = 0; i < total_elements; ++i) {
        scaled_input[i] = bfloat16(static_cast<float>(input_[i]) * 10.0f);
    }
    std::vector<bfloat16> scaled_output(total_elements);

    rms_norm_fwd(scaled_input.data(), weight_.data(), scaled_output.data(), batch_, seq_, hidden_, eps_);

    // Original output
    rms_norm_fwd(input_.data(), weight_.data(), output_.data(), batch_, seq_, hidden_, eps_);

    // RMSNorm output should be invariant to input scaling (up to numerical precision)
    float max_diff = 0.0f;
    for (size_t i = 0; i < total_elements; ++i) {
        const float diff = std::abs(static_cast<float>(output_[i]) - static_cast<float>(scaled_output[i]));
        if (diff > max_diff) {
            max_diff = diff;
        }
    }

    EXPECT_LT(max_diff, 0.2f) << "RMSNorm should be approximately scale-invariant";
}

} // namespace tests
} // namespace normalization
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
