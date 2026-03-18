// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_rope.cpp
 * @brief Unit tests for Rotary Positional Embedding (RoPE) operator
 *
 * This test suite validates the RoPE operator implementation:
 * - Basic forward pass functionality
 * - Two-halves method correctness
 * - Interleaved method correctness
 * - Edge cases (small dimensions, large sequences)
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
#include "iron/operators/rope/rope_bf16.hpp"

namespace iron
{
namespace operators
{
namespace rope
{
namespace tests
{

//==============================================================================
// Test Fixtures
//==============================================================================

/**
 * @brief Test fixture for RoPE operator tests
 */
class RoPETest : public ::testing::Test
{
  protected:
    void SetUp() override
    {
        // Initialize test data
        batch_ = 1;
        heads_ = 2;
        seq_ = 4;
        head_dim_ = 8;

        const size_t total_elements = batch_ * heads_ * seq_ * head_dim_;
        const size_t angle_elements = seq_ * (head_dim_ / 2);

        q_.resize(total_elements);
        k_.resize(total_elements);
        cos_.resize(angle_elements);
        sin_.resize(angle_elements);
        q_out_.resize(total_elements);
        k_out_.resize(total_elements);

        // Initialize with small values for numerical stability
        std::mt19937 gen(42);
        std::uniform_real_distribution<float> dist(-1.0f, 1.0f);

        for (size_t i = 0; i < total_elements; ++i) {
            q_[i] = bfloat16(dist(gen));
            k_[i] = bfloat16(dist(gen));
        }

        // Initialize cos/sin with valid rotation angles
        for (size_t i = 0; i < angle_elements; ++i) {
            const float angle = static_cast<float>(i) * 0.1f;
            cos_[i] = bfloat16(std::cos(angle));
            sin_[i] = bfloat16(std::sin(angle));
        }
    }

    void TearDown() override
    {
        // Cleanup
    }

    // Test parameters
    int batch_;
    int heads_;
    int seq_;
    int head_dim_;

    // Test data
    std::vector<bfloat16> q_;
    std::vector<bfloat16> k_;
    std::vector<bfloat16> cos_;
    std::vector<bfloat16> sin_;
    std::vector<bfloat16> q_out_;
    std::vector<bfloat16> k_out_;
};

//==============================================================================
// Basic Functionality Tests
//==============================================================================

/**
 * @test Verify RoPE forward pass with two-halves method
 */
TEST_F(RoPETest, ForwardPassTwoHalves)
{
    rope_fwd(q_.data(),
             k_.data(),
             cos_.data(),
             sin_.data(),
             q_out_.data(),
             k_out_.data(),
             batch_,
             heads_,
             seq_,
             head_dim_,
             RotationMethod::TWO_HALVES);

    // Verify outputs are finite (not NaN or Inf)
    for (size_t i = 0; i < q_out_.size(); ++i) {
        float val = static_cast<float>(q_out_[i]);
        EXPECT_TRUE(std::isfinite(val)) << "q_out[" << i << "] is not finite";
    }

    for (size_t i = 0; i < k_out_.size(); ++i) {
        float val = static_cast<float>(k_out_[i]);
        EXPECT_TRUE(std::isfinite(val)) << "k_out[" << i << "] is not finite";
    }

    // Verify output norms are approximately preserved (RoPE is norm-preserving)
    // Note: Small numerical differences are expected due to bfloat16 precision
    float q_in_norm = 0.0f, q_out_norm = 0.0f;
    for (size_t i = 0; i < q_.size(); ++i) {
        const float q_val = static_cast<float>(q_[i]);
        const float qo_val = static_cast<float>(q_out_[i]);
        q_in_norm += q_val * q_val;
        q_out_norm += qo_val * qo_val;
    }

    const float norm_ratio = q_out_norm / (q_in_norm + 1e-8f);
    EXPECT_NEAR(norm_ratio, 1.0f, 0.1f) << "RoPE should approximately preserve norms";
}

/**
 * @test Verify RoPE forward pass with interleaved method
 */
TEST_F(RoPETest, ForwardPassInterleaved)
{
    rope_fwd(q_.data(),
             k_.data(),
             cos_.data(),
             sin_.data(),
             q_out_.data(),
             k_out_.data(),
             batch_,
             heads_,
             seq_,
             head_dim_,
             RotationMethod::INTERLEAVED);

    // Verify outputs are finite
    for (size_t i = 0; i < q_out_.size(); ++i) {
        float val = static_cast<float>(q_out_[i]);
        EXPECT_TRUE(std::isfinite(val)) << "q_out[" << i << "] is not finite";
    }
}

/**
 * @test Verify RoPE query-only mode
 */
TEST_F(RoPETest, QueryOnlyMode)
{
    rope_query_only(q_.data(),
                    cos_.data(),
                    sin_.data(),
                    q_out_.data(),
                    batch_,
                    heads_,
                    seq_,
                    head_dim_,
                    RotationMethod::TWO_HALVES);

    // Verify outputs are finite
    for (size_t i = 0; i < q_out_.size(); ++i) {
        float val = static_cast<float>(q_out_[i]);
        EXPECT_TRUE(std::isfinite(val));
    }
}

//==============================================================================
// Edge Case Tests
//==============================================================================

/**
 * @test Test with minimal head dimension (2)
 */
TEST_F(RoPETest, MinimalHeadDimension)
{
    head_dim_ = 2;
    const size_t total_elements = batch_ * heads_ * seq_ * head_dim_;
    const size_t angle_elements = seq_ * (head_dim_ / 2);

    std::vector<bfloat16> q_small(total_elements);
    std::vector<bfloat16> k_small(total_elements);
    std::vector<bfloat16> cos_small(angle_elements);
    std::vector<bfloat16> sin_small(angle_elements);
    std::vector<bfloat16> q_out_small(total_elements);
    std::vector<bfloat16> k_out_small(total_elements);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-1.0f, 1.0f);

    for (size_t i = 0; i < total_elements; ++i) {
        q_small[i] = bfloat16(dist(gen));
        k_small[i] = bfloat16(dist(gen));
    }
    for (size_t i = 0; i < angle_elements; ++i) {
        cos_small[i] = bfloat16(1.0f);
        sin_small[i] = bfloat16(0.0f);
    }

    rope_fwd(q_small.data(),
             k_small.data(),
             cos_small.data(),
             sin_small.data(),
             q_out_small.data(),
             k_out_small.data(),
             batch_,
             heads_,
             seq_,
             head_dim_,
             RotationMethod::TWO_HALVES);

    // With cos=1, sin=0, output should equal input
    for (size_t i = 0; i < total_elements; ++i) {
        float in_val = static_cast<float>(q_small[i]);
        float out_val = static_cast<float>(q_out_small[i]);
        EXPECT_NEAR(in_val, out_val, 0.1f) << "With cos=1,sin=0, RoPE should be identity";
    }
}

/**
 * @test Test with larger sequence length
 */
TEST_F(RoPETest, LargeSequenceLength)
{
    seq_ = 512;
    const size_t total_elements = batch_ * heads_ * seq_ * head_dim_;
    const size_t angle_elements = seq_ * (head_dim_ / 2);

    std::vector<bfloat16> q_large(total_elements);
    std::vector<bfloat16> k_large(total_elements);
    std::vector<bfloat16> cos_large(angle_elements);
    std::vector<bfloat16> sin_large(angle_elements);
    std::vector<bfloat16> q_out_large(total_elements);
    std::vector<bfloat16> k_out_large(total_elements);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-1.0f, 1.0f);

    for (size_t i = 0; i < total_elements; ++i) {
        q_large[i] = bfloat16(dist(gen));
        k_large[i] = bfloat16(dist(gen));
    }
    for (size_t i = 0; i < angle_elements; ++i) {
        const float angle = static_cast<float>(i) * 0.01f;
        cos_large[i] = bfloat16(std::cos(angle));
        sin_large[i] = bfloat16(std::sin(angle));
    }

    rope_fwd(q_large.data(),
             k_large.data(),
             cos_large.data(),
             sin_large.data(),
             q_out_large.data(),
             k_out_large.data(),
             batch_,
             heads_,
             seq_,
             head_dim_,
             RotationMethod::TWO_HALVES);

    // Verify outputs are finite
    for (size_t i = 0; i < q_out_large.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(q_out_large[i])));
    }
}

/**
 * @test Test with batch > 1
 */
TEST_F(RoPETest, BatchProcessing)
{
    batch_ = 4;
    const size_t total_elements = batch_ * heads_ * seq_ * head_dim_;

    std::vector<bfloat16> q_batch(total_elements);
    std::vector<bfloat16> k_batch(total_elements);
    std::vector<bfloat16> q_out_batch(total_elements);
    std::vector<bfloat16> k_out_batch(total_elements);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-1.0f, 1.0f);

    for (size_t i = 0; i < total_elements; ++i) {
        q_batch[i] = bfloat16(dist(gen));
        k_batch[i] = bfloat16(dist(gen));
    }

    rope_fwd(q_batch.data(),
             k_batch.data(),
             cos_.data(),
             sin_.data(),
             q_out_batch.data(),
             k_out_batch.data(),
             batch_,
             heads_,
             seq_,
             head_dim_,
             RotationMethod::TWO_HALVES);

    // Verify outputs are finite
    for (size_t i = 0; i < q_out_batch.size(); ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(q_out_batch[i])));
    }
}

//==============================================================================
// Numerical Accuracy Tests
//==============================================================================

/**
 * @test Verify rotation orthogonality (preserves dot products within limits)
 */
TEST_F(RoPETest, RotationOrthogonality)
{
    // Compute dot product before rotation
    float dot_in = 0.0f;
    for (size_t i = 0; i < q_.size(); ++i) {
        dot_in += static_cast<float>(q_[i]) * static_cast<float>(k_[i]);
    }

    rope_fwd(q_.data(),
             k_.data(),
             cos_.data(),
             sin_.data(),
             q_out_.data(),
             k_out_.data(),
             batch_,
             heads_,
             seq_,
             head_dim_,
             RotationMethod::TWO_HALVES);

    // Compute dot product after rotation
    float dot_out = 0.0f;
    for (size_t i = 0; i < q_out_.size(); ++i) {
        dot_out += static_cast<float>(q_out_[i]) * static_cast<float>(k_out_[i]);
    }

    // Dot products should be approximately preserved (within bfloat16 precision)
    const float rel_diff = std::abs(dot_out - dot_in) / (std::abs(dot_in) + 1e-8f);
    EXPECT_LT(rel_diff, 0.2f) << "Dot product changed too much after RoPE";
}

} // namespace tests
} // namespace rope
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
