// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_rope_cache.cpp
 * @brief Unit tests for RoPECache class
 *
 * This test suite validates the RoPE cache implementation:
 * - Construction and initialization
 * - Pre-computation correctness
 * - Table lookup accuracy
 * - Device buffer layout
 * - Performance targets
 *
 * @note Uses Google Test framework
 */

#include <chrono>
#include <cmath>
#include <gtest/gtest.h>
#include <iron/rope_cache.hpp>
#include <vector>

using namespace iron::runtime;

namespace
{

//==============================================================================
// Test Fixture
//==============================================================================

/**
 * @brief Test fixture for RoPECache tests
 */
class RoPECacheTest : public ::testing::Test
{
  protected:
    RoPECache::Config createTestConfig()
    {
        RoPECache::Config config;
        config.maxSeqLen = 2048; // Small for testing
        config.headDim = 64;
        config.theta = 10000.0f;
        return config;
    }

    /**
     * @brief Compute expected RoPE values using reference formula
     */
    void computeReferenceAngles(std::vector<float> &cosOut,
                                std::vector<float> &sinOut,
                                size_t seqLen,
                                size_t headDim,
                                float theta)
    {
        const size_t halfDim = headDim / 2;
        cosOut.resize(seqLen * halfDim);
        sinOut.resize(seqLen * halfDim);

        for (size_t pos = 0; pos < seqLen; ++pos) {
            for (size_t i = 0; i < halfDim; ++i) {
                float invFreq = std::pow(theta, -2.0f * static_cast<float>(i) / static_cast<float>(headDim));
                float angle = static_cast<float>(pos) * invFreq;
                size_t idx = pos * halfDim + i;
                cosOut[idx] = std::cos(angle);
                sinOut[idx] = std::sin(angle);
            }
        }
    }
};

//==============================================================================
// Construction Tests
//==============================================================================

TEST_F(RoPECacheTest, Construction)
{
    auto config = createTestConfig();
    RoPECache cache(config);

    EXPECT_TRUE(cache.isInitialized());
    EXPECT_TRUE(cache.getConfig().maxSeqLen == config.maxSeqLen);
    EXPECT_TRUE(cache.getConfig().headDim == config.headDim);
}

TEST_F(RoPECacheTest, ConstructionWithDefaults)
{
    RoPECache cache;

    EXPECT_TRUE(cache.isInitialized());
    EXPECT_EQ(cache.getConfig().maxSeqLen, 131072); // 128K
    EXPECT_EQ(cache.getConfig().headDim, 64);
    EXPECT_FLOAT_EQ(cache.getConfig().theta, 10000.0f);
}

TEST_F(RoPECacheTest, ConstructionWithInvalidConfig)
{
    RoPECache::Config config;
    config.maxSeqLen = 0; // Invalid
    EXPECT_THROW(RoPECache cache(config), std::invalid_argument);
}

TEST_F(RoPECacheTest, ConstructionWithOddHeadDim)
{
    RoPECache::Config config;
    config.maxSeqLen = 1024;
    config.headDim = 63; // Must be even
    EXPECT_THROW(RoPECache cache(config), std::invalid_argument);
}

//==============================================================================
// Initialization Performance Tests
//==============================================================================

TEST_F(RoPECacheTest, InitializationTime)
{
    // Test with a reasonably large config
    RoPECache::Config config;
    config.maxSeqLen = 32768; // 32K
    config.headDim = 64;

    RoPECache cache(config);

    // Should complete in < 100ms
    EXPECT_LT(cache.getInitializationTimeMs(), 100.0);
}

TEST_F(RoPECacheTest, MemoryUsage)
{
    RoPECache::Config config;
    config.maxSeqLen = 131072; // 128K
    config.headDim = 64;

    RoPECache cache(config);

    // Cache size: 128K * 32 * 2 * 4 bytes = ~32 MB for both cos and sin
    size_t expectedBytes = config.maxSeqLen * (config.headDim / 2) * 2 * sizeof(float);
    EXPECT_EQ(cache.getDeviceBufferSize(), expectedBytes);

    // Should be < 64MB as per spec
    EXPECT_LT(cache.getDeviceBufferSize(), 64 * 1024 * 1024);
}

//==============================================================================
// Table Lookup Tests
//==============================================================================

TEST_F(RoPECacheTest, GetCosTable)
{
    auto config = createTestConfig();
    RoPECache cache(config);

    const float *cosTable = cache.getCosTable(100);
    ASSERT_NE(cosTable, nullptr);

    // First position should have cos(0) = 1 for all dimensions
    const size_t halfDim = config.headDim / 2;
    for (size_t i = 0; i < halfDim; ++i) {
        EXPECT_NEAR(cosTable[i], 1.0f, 1e-5);
    }
}

TEST_F(RoPECacheTest, GetSinTable)
{
    auto config = createTestConfig();
    RoPECache cache(config);

    const float *sinTable = cache.getSinTable(100);
    ASSERT_NE(sinTable, nullptr);

    // First position should have sin(0) = 0 for all dimensions
    const size_t halfDim = config.headDim / 2;
    for (size_t i = 0; i < halfDim; ++i) {
        EXPECT_NEAR(sinTable[i], 0.0f, 1e-5);
    }
}

TEST_F(RoPECacheTest, GetTableSequenceLengthExceedsMax)
{
    auto config = createTestConfig();
    RoPECache cache(config);

    EXPECT_THROW(cache.getCosTable(config.maxSeqLen + 1), std::out_of_range);
    EXPECT_THROW(cache.getSinTable(config.maxSeqLen + 1), std::out_of_range);
}

TEST_F(RoPECacheTest, NumericalAccuracy)
{
    auto config = createTestConfig();
    RoPECache cache(config);

    // Compute reference values
    std::vector<float> refCos, refSin;
    computeReferenceAngles(refCos, refSin, config.maxSeqLen, config.headDim, config.theta);

    const float *cosTable = cache.getCosTable(config.maxSeqLen);
    const float *sinTable = cache.getSinTable(config.maxSeqLen);

    // Check accuracy at various positions
    const size_t halfDim = config.headDim / 2;
    const std::vector<size_t> testPositions = {0, 1, 10, 100, 500, 1000, 2000};

    for (size_t pos : testPositions) {
        if (pos >= config.maxSeqLen)
            continue;

        for (size_t i = 0; i < halfDim; ++i) {
            size_t idx = pos * halfDim + i;
            EXPECT_NEAR(cosTable[idx], refCos[idx], 1e-5) << "Position " << pos << ", dim " << i;
            EXPECT_NEAR(sinTable[idx], refSin[idx], 1e-5) << "Position " << pos << ", dim " << i;
        }
    }
}

//==============================================================================
// Device Buffer Tests
//==============================================================================

TEST_F(RoPECacheTest, GetDeviceBuffer)
{
    auto config = createTestConfig();
    RoPECache cache(config);

    const void *deviceBuffer = cache.getDeviceBuffer();
    ASSERT_NE(deviceBuffer, nullptr);

    // Buffer should contain interleaved cos and sin data
    const float *buffer = static_cast<const float *>(deviceBuffer);
    const size_t elements = config.cacheElements();

    // First half should be cos values
    for (size_t i = 0; i < elements; ++i) {
        EXPECT_FLOAT_EQ(buffer[i], cache.getCosTable(config.maxSeqLen)[i]);
    }

    // Second half should be sin values
    for (size_t i = 0; i < elements; ++i) {
        EXPECT_FLOAT_EQ(buffer[elements + i], cache.getSinTable(config.maxSeqLen)[i]);
    }
}

TEST_F(RoPECacheTest, DeviceBufferSize)
{
    RoPECache::Config config;
    config.maxSeqLen = 4096;
    config.headDim = 128;

    RoPECache cache(config);

    size_t expectedSize = config.maxSeqLen * (config.headDim / 2) * 2 * sizeof(float);
    EXPECT_EQ(cache.getDeviceBufferSize(), expectedSize);
}

//==============================================================================
// Edge Case Tests
//==============================================================================

TEST_F(RoPECacheTest, SmallSequenceLength)
{
    RoPECache::Config config;
    config.maxSeqLen = 16;
    config.headDim = 64;

    RoPECache cache(config);

    const float *cosTable = cache.getCosTable(1);
    ASSERT_NE(cosTable, nullptr);

    // First position: all cos = 1, all sin = 0
    const size_t halfDim = config.headDim / 2;
    for (size_t i = 0; i < halfDim; ++i) {
        EXPECT_NEAR(cosTable[i], 1.0f, 1e-5);
    }
}

TEST_F(RoPECacheTest, LargeHeadDim)
{
    RoPECache::Config config;
    config.maxSeqLen = 1024;
    config.headDim = 256;

    RoPECache cache(config);

    EXPECT_TRUE(cache.isInitialized());
    EXPECT_EQ(cache.getDeviceBufferSize(), config.maxSeqLen * (config.headDim / 2) * 2 * sizeof(float));
}

TEST_F(RoPECacheTest, DifferentTheta)
{
    RoPECache::Config config;
    config.maxSeqLen = 1024;
    config.headDim = 64;
    config.theta = 5000.0f; // Different from default

    RoPECache cache(config);

    // Verify theta affects the computed values
    const float *cosTable = cache.getCosTable(10);

    // At position 1, dim 0, with theta=5000:
    // inv_freq = 5000^0 = 1
    // angle = 1 * 1 = 1
    // cos(1) ≈ 0.5403
    EXPECT_NEAR(cosTable[0], std::cos(1.0f), 1e-4);
}

//==============================================================================
// Not Initialized Tests (for completeness, though init happens in ctor)
//==============================================================================

TEST_F(RoPECacheTest, GetCosTableBeforeInit)
{
    // This test is somewhat artificial since initialization happens in constructor
    // In practice, isInitialized() should always be true after construction
    RoPECache cache(createTestConfig());
    EXPECT_TRUE(cache.isInitialized());
}

} // anonymous namespace
