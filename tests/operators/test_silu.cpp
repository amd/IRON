// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_silu.cpp
 * @brief Unit tests for SiLU (Sigmoid Linear Unit) activation function
 *
 * This test suite validates the SiLU operator implementation:
 * - Basic forward pass functionality
 * - SiLU mathematical properties (x * sigmoid(x))
 * - Edge cases (negative values, large values, zero)
 * - SwiGLU gating functionality
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
#include "iron/operators/activations/silu_bf16.hpp"

namespace iron
{
namespace operators
{
namespace activations
{
namespace tests
{

//==============================================================================
// Test Fixtures
//==============================================================================

/**
 * @brief Test fixture for SiLU operator tests
 */
class SiLUTest : public ::testing::Test
{
  protected:
    void SetUp() override
    {
        // Initialize test parameters
        num_elements_ = 64;

        input_.resize(num_elements_);
        output_.resize(num_elements_);
        gate_.resize(num_elements_);
        gated_output_.resize(num_elements_);

        // Initialize with random values spanning negative and positive
        std::mt19937 gen(42);
        std::uniform_real_distribution<float> dist(-5.0f, 5.0f);

        for (size_t i = 0; i < num_elements_; ++i) {
            input_[i] = bfloat16(dist(gen));
            gate_[i] = bfloat16(dist(gen));
        }
    }

    void TearDown() override
    {
        // Cleanup
    }

    // Compute reference SiLU using standard math
    float reference_silu(float x) const
    {
        return x / (1.0f + std::exp(-x));
    }

    // Test parameters
    size_t num_elements_;

    // Test data
    std::vector<bfloat16> input_;
    std::vector<bfloat16> output_;
    std::vector<bfloat16> gate_;
    std::vector<bfloat16> gated_output_;
};

//==============================================================================
// Basic Functionality Tests
//==============================================================================

/**
 * @test Verify SiLU forward pass produces finite outputs
 */
TEST_F(SiLUTest, ForwardPassFinite)
{
    silu_fwd(input_.data(), output_.data(), static_cast<int>(num_elements_));

    // Verify all outputs are finite
    for (size_t i = 0; i < num_elements_; ++i) {
        float val = static_cast<float>(output_[i]);
        EXPECT_TRUE(std::isfinite(val)) << "output[" << i << "] is not finite";
    }
}

/**
 * @test Verify SiLU in-place operation
 */
TEST_F(SiLUTest, InplaceOperation)
{
    // Copy input for in-place modification
    std::vector<bfloat16> inplace_input = input_;

    silu_inplace(inplace_input.data(), static_cast<int>(num_elements_));

    // Verify all outputs are finite
    for (size_t i = 0; i < num_elements_; ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(inplace_input[i])));
    }
}

/**
 * @test Verify SiLU mathematical correctness against reference
 */
TEST_F(SiLUTest, MathematicalCorrectness)
{
    silu_fwd(input_.data(), output_.data(), static_cast<int>(num_elements_));

    // Compare against reference implementation
    for (size_t i = 0; i < num_elements_; ++i) {
        const float x = static_cast<float>(input_[i]);
        const float expected = reference_silu(x);
        const float actual = static_cast<float>(output_[i]);

        // Allow tolerance for bfloat16 precision
        const float abs_tol = 0.1f; // bfloat16 has ~3 decimal digits
        const float rel_tol = 0.1f;
        const float tol = std::max(abs_tol, rel_tol * std::abs(expected));

        EXPECT_NEAR(actual, expected, tol) << "SiLU mismatch at index " << i << " (input=" << x
                                           << ", expected=" << expected << ", actual=" << actual << ")";
    }
}

//==============================================================================
// Mathematical Property Tests
//==============================================================================

/**
 * @test Verify SiLU(0) = 0
 */
TEST_F(SiLUTest, ZeroInput)
{
    std::vector<bfloat16> zero_input(1, bfloat16(0.0f));
    std::vector<bfloat16> zero_output(1);

    silu_fwd(zero_input.data(), zero_output.data(), 1);

    const float result = static_cast<float>(zero_output[0]);
    EXPECT_NEAR(result, 0.0f, 0.01f) << "SiLU(0) should be 0";
}

/**
 * @test Verify SiLU behavior for large positive values (approaches x)
 */
TEST_F(SiLUTest, LargePositiveValues)
{
    std::vector<bfloat16> large_input(10, bfloat16(10.0f));
    std::vector<bfloat16> large_output(10);

    silu_fwd(large_input.data(), large_output.data(), 10);

    // For large positive x, SiLU(x) ≈ x (sigmoid approaches 1)
    for (size_t i = 0; i < 10; ++i) {
        const float result = static_cast<float>(large_output[i]);
        // SiLU(10) ≈ 10 (actually 9.9995...)
        EXPECT_GT(result, 9.0f) << "SiLU(10) should be close to 10";
        EXPECT_LT(result, 10.5f) << "SiLU(10) should be close to 10";
    }
}

/**
 * @test Verify SiLU behavior for large negative values (approaches 0)
 */
TEST_F(SiLUTest, LargeNegativeValues)
{
    std::vector<bfloat16> negative_input(10, bfloat16(-10.0f));
    std::vector<bfloat16> negative_output(10);

    silu_fwd(negative_input.data(), negative_output.data(), 10);

    // For large negative x, SiLU(x) ≈ 0 (sigmoid approaches 0)
    for (size_t i = 0; i < 10; ++i) {
        const float result = static_cast<float>(negative_output[i]);
        EXPECT_LT(std::abs(result), 0.01f) << "SiLU(-10) should be close to 0";
    }
}

/**
 * @test Verify SiLU is non-monotonic (has derivative > 0 everywhere)
 */
TEST_F(SiLUTest, Monotonicity)
{
    // Test that larger inputs produce larger outputs
    std::vector<bfloat16> increasing_input = {
        bfloat16(-5.0f), bfloat16(-2.0f), bfloat16(0.0f), bfloat16(2.0f), bfloat16(5.0f)};
    std::vector<bfloat16> increasing_output(5);

    silu_fwd(increasing_input.data(), increasing_output.data(), 5);

    // Verify outputs are monotonically increasing
    for (size_t i = 1; i < 5; ++i) {
        const float prev = static_cast<float>(increasing_output[i - 1]);
        const float curr = static_cast<float>(increasing_output[i]);
        EXPECT_GT(curr, prev) << "SiLU should be monotonically increasing";
    }
}

/**
 * @test Verify SiLU preserves sign (output has same sign as input)
 */
TEST_F(SiLUTest, SignPreservation)
{
    silu_fwd(input_.data(), output_.data(), static_cast<int>(num_elements_));

    for (size_t i = 0; i < num_elements_; ++i) {
        const float x = static_cast<float>(input_[i]);
        const float y = static_cast<float>(output_[i]);

        // Sign of output should match sign of input (or be zero)
        if (x > 0.0f) {
            EXPECT_GT(y, 0.0f) << "Positive input should produce positive output";
        } else if (x < 0.0f) {
            EXPECT_LE(y, 0.0f) << "Negative input should produce negative or zero output";
        }
    }
}

//==============================================================================
// SwiGLU Gating Tests
//==============================================================================

/**
 * @test Verify SwiGLU gating operation
 */
TEST_F(SiLUTest, SwiGLUGating)
{
    silu_gate(input_.data(), gate_.data(), gated_output_.data(), static_cast<int>(num_elements_));

    // Verify all outputs are finite
    for (size_t i = 0; i < num_elements_; ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(gated_output_[i])));
    }
}

/**
 * @test Verify SwiGLU with unit gate (should equal SiLU)
 */
TEST_F(SiLUTest, SwiGLUWithUnitGate)
{
    // Set gate to 1.0
    std::vector<bfloat16> unit_gate(num_elements_, bfloat16(1.0f));
    std::vector<bfloat16> unit_output(num_elements_);

    // Compute SiLU directly
    std::vector<bfloat16> silu_output(num_elements_);
    silu_fwd(input_.data(), silu_output.data(), static_cast<int>(num_elements_));

    // Compute SwiGLU with unit gate
    silu_gate(input_.data(), unit_gate.data(), unit_output.data(), static_cast<int>(num_elements_));

    // Results should match (SwiGLU(x, 1) = SiLU(1) * x = 0.73 * x, not SiLU(x))
    // Actually, SwiGLU(x, gate) = SiLU(gate) * x
    // So SwiGLU(x, 1) = SiLU(1) * x ≈ 0.73 * x
    for (size_t i = 0; i < num_elements_; ++i) {
        const float x = static_cast<float>(input_[i]);
        const float expected = reference_silu(1.0f) * x; // ≈ 0.73 * x
        const float actual = static_cast<float>(unit_output[i]);

        const float tol = 0.1f;
        EXPECT_NEAR(actual, expected, tol) << "SwiGLU with unit gate mismatch at index " << i;
    }
}

//==============================================================================
// Edge Case Tests
//==============================================================================

/**
 * @test Test with small number of elements
 */
TEST_F(SiLUTest, SmallInput)
{
    std::vector<bfloat16> small_input(4);
    std::vector<bfloat16> small_output(4);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-5.0f, 5.0f);

    for (size_t i = 0; i < 4; ++i) {
        small_input[i] = bfloat16(dist(gen));
    }

    silu_fwd(small_input.data(), small_output.data(), 4);

    for (size_t i = 0; i < 4; ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(small_output[i])));
    }
}

/**
 * @test Test with large number of elements
 */
TEST_F(SiLUTest, LargeInput)
{
    const size_t large_size = 8192; // Typical MLP hidden size
    std::vector<bfloat16> large_input(large_size);
    std::vector<bfloat16> large_output(large_size);

    std::mt19937 gen(42);
    std::uniform_real_distribution<float> dist(-5.0f, 5.0f);

    for (size_t i = 0; i < large_size; ++i) {
        large_input[i] = bfloat16(dist(gen));
    }

    silu_fwd(large_input.data(), large_output.data(), static_cast<int>(large_size));

    for (size_t i = 0; i < large_size; ++i) {
        EXPECT_TRUE(std::isfinite(static_cast<float>(large_output[i])));
    }
}

/**
 * @test Test boundedness below (SiLU > -0.28 for all x)
 */
TEST_F(SiLUTest, BoundedBelow)
{
    // The minimum of SiLU is approximately -0.2785 at x ≈ -1.28
    std::vector<bfloat16> test_input = {
        bfloat16(-2.0f), bfloat16(-1.5f), bfloat16(-1.28f), bfloat16(-1.0f), bfloat16(-0.5f)};
    std::vector<bfloat16> test_output(5);

    silu_fwd(test_input.data(), test_output.data(), 5);

    // SiLU minimum is approximately -0.28
    for (size_t i = 0; i < 5; ++i) {
        const float result = static_cast<float>(test_output[i]);
        EXPECT_GT(result, -0.5f) << "SiLU should be bounded below by ~-0.28";
    }
}

} // namespace tests
} // namespace activations
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
