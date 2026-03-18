// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file rope_cache.cpp
 * @brief Implementation of pre-computed RoPE angle cache
 *
 * This file implements the RoPECache class for storing pre-computed
 * sinusoidal angle tables used in Rotary Positional Embeddings.
 *
 * The implementation:
 * - Pre-computes all sin/cos values at initialization time
 * - Creates a contiguous device buffer for efficient DMA transfer
 * - Targets initialization time < 100ms for 128K context
 * - Uses O(1) lookup during inference
 */

#include <chrono>
#include <cmath>
#include <cstring>
#include <iron/rope_cache.hpp>
#include <sstream>
#include <stdexcept>
#include <string>

namespace iron
{
namespace runtime
{

//==============================================================================
// Construction/Destruction
//==============================================================================

RoPECache::RoPECache(const Config &config) : config_(config)
{
    if (!config.isValid()) {
        throw std::invalid_argument("Invalid RoPECache configuration: "
                                    "maxSeqLen and headDim must be > 0, headDim must be even, theta > 0");
    }
    initialize();
}

RoPECache::~RoPECache() = default;

//==============================================================================
// Initialization
//==============================================================================

void RoPECache::initialize()
{
    auto startTime = std::chrono::high_resolution_clock::now();

    // Allocate caches
    size_t elements = config_.cacheElements();
    cosCache_.resize(elements);
    sinCache_.resize(elements);

    // Compute angles
    computeAngles();

    // Create device buffer (interleaved cos + sin)
    deviceBufferSize_ = config_.totalBytes();
    deviceBuffer_ = std::make_unique<uint8_t[]>(deviceBufferSize_);

    // Copy to device buffer in interleaved format
    // Layout: [all cos values][all sin values]
    std::memcpy(deviceBuffer_.get(), cosCache_.data(), elements * sizeof(float));
    std::memcpy(deviceBuffer_.get() + elements * sizeof(float), sinCache_.data(), elements * sizeof(float));

    auto endTime = std::chrono::high_resolution_clock::now();
    initializationTimeMs_ = std::chrono::duration<double, std::milli>(endTime - startTime).count();

    initialized_ = true;
}

void RoPECache::computeAngles()
{
    const size_t halfDim = config_.headDim / 2;

    // Pre-compute inverse frequencies
    // inv_freq[i] = theta^(-2*i/headDim)
    std::vector<float> invFreq(halfDim);
    for (size_t i = 0; i < halfDim; ++i) {
        invFreq[i] = getInverseFrequency(i, config_.headDim, config_.theta);
    }

    // Compute sin/cos for all positions and dimensions
    // This is the main O(maxSeqLen * headDim/2) computation
    for (size_t pos = 0; pos < config_.maxSeqLen; ++pos) {
        for (size_t i = 0; i < halfDim; ++i) {
            float angle = static_cast<float>(pos) * invFreq[i];
            size_t idx = pos * halfDim + i;
            cosCache_[idx] = std::cos(angle);
            sinCache_[idx] = std::sin(angle);
        }
    }
}

float RoPECache::getInverseFrequency(size_t i, size_t headDim, float theta) const
{
    // inv_freq[i] = 1 / (theta ^ (2*i/headDim))
    // Computed as: theta^(-2*i/headDim) for numerical stability
    const float exponent = -2.0f * static_cast<float>(i) / static_cast<float>(headDim);
    return std::pow(theta, exponent);
}

//==============================================================================
// Table Access
//==============================================================================

const float *RoPECache::getCosTable(size_t seqLen) const
{
    if (!initialized_) {
        throw std::runtime_error("RoPECache not initialized");
    }
    if (seqLen > config_.maxSeqLen) {
        throw std::out_of_range("Sequence length " + std::to_string(seqLen) + " exceeds maxSeqLen " +
                                std::to_string(config_.maxSeqLen));
    }
    // Return full table - caller uses first seqLen rows
    return cosCache_.data();
}

const float *RoPECache::getSinTable(size_t seqLen) const
{
    if (!initialized_) {
        throw std::runtime_error("RoPECache not initialized");
    }
    if (seqLen > config_.maxSeqLen) {
        throw std::out_of_range("Sequence length " + std::to_string(seqLen) + " exceeds maxSeqLen " +
                                std::to_string(config_.maxSeqLen));
    }
    // Return full table - caller uses first seqLen rows
    return sinCache_.data();
}

const void *RoPECache::getDeviceBuffer() const
{
    if (!initialized_) {
        throw std::runtime_error("RoPECache not initialized");
    }
    return deviceBuffer_.get();
}

size_t RoPECache::getDeviceBufferSize() const
{
    return deviceBufferSize_;
}

} // namespace runtime
} // namespace iron
