// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file rope_cache.hpp
 * @brief Pre-computed RoPE angle cache for fast inference
 *
 * This header defines the RoPECache class for storing pre-computed
 * sinusoidal angle tables used in Rotary Positional Embeddings.
 *
 * MATHEMATICAL BACKGROUND:
 * RoPE applies rotational embeddings to query and key vectors:
 *   RoPE(x, pos, i) = x[i] * cos(theta_i * pos) - x[i+d/2] * sin(theta_i * pos)
 * where theta_i = 10000^(-2i/d)
 *
 * This class pre-computes cos(theta_i * pos) and sin(theta_i * pos) for all
 * positions and dimensions, enabling O(1) lookup during inference.
 *
 * MEMORY LAYOUT:
 * cosCache_: [pos0_dim0, pos0_dim1, ..., pos0_dimN/2,
 *             pos1_dim0, pos1_dim1, ..., pos1_dimN/2,
 *             ...]
 * Size: maxSeqLen * (headDim/2) * sizeof(float)
 *
 * THREAD SAFETY:
 * - Read operations are thread-safe after initialization
 * - Initialization must complete before concurrent access
 */

#pragma once

#include <vector>
#include <memory>
#include <cstdint>
#include <cstddef>

namespace iron {
namespace runtime {

/**
 * @brief Pre-computed RoPE angle cache for fast inference
 *
 * Stores sin/cos angle tables pre-computed at model load time.
 * Supports sequence lengths up to 131K (Llama3.2 max context).
 */
class RoPECache {
public:
    /**
     * @brief Configuration for RoPE cache
     *
     * Default values target Llama3.2 models with 64-dimensional heads
     * and up to 128K context length.
     */
    struct Config {
        size_t maxSeqLen = 131072;   ///< Llama3.2 max context (128K)
        size_t headDim = 64;         ///< Head dimension
        float theta = 10000.0f;      ///< RoPE theta parameter

        /**
         * @brief Calculate cache size in elements
         * @return Number of float elements per cache (cos or sin)
         */
        size_t cacheElements() const {
            return maxSeqLen * (headDim / 2);
        }

        /**
         * @brief Calculate total cache size in bytes
         * @return Total bytes for both cos and sin caches
         */
        size_t totalBytes() const {
            return cacheElements() * 2 * sizeof(float);  // cos + sin
        }

        /**
         * @brief Validate configuration
         * @return true if valid
         */
        bool isValid() const {
            return maxSeqLen > 0 && headDim > 0 && headDim % 2 == 0 && theta > 0.0f;
        }
    };

    /**
     * @brief Construct and initialize RoPE cache
     * @param config Cache configuration (uses defaults if not provided)
     * @throws std::invalid_argument if config is invalid
     * @throws std::bad_alloc if memory allocation fails
     */
    explicit RoPECache(const Config& config = Config());

    /**
     * @brief Destructor
     */
    ~RoPECache();

    // Prevent copying (large object)
    RoPECache(const RoPECache&) = delete;
    RoPECache& operator=(const RoPECache&) = delete;

    // Allow moving
    RoPECache(RoPECache&& other) noexcept = default;
    RoPECache& operator=(RoPECache&& other) noexcept = default;

    //==========================================================================
    // Table Access
    //==========================================================================

    /**
     * @brief Get pre-computed cos table for sequence length
     * @param seqLen Sequence length (must be <= maxSeqLen)
     * @return Pointer to cos values [seqLen, headDim/2]
     * @throws std::runtime_error if not initialized
     * @throws std::out_of_range if seqLen > maxSeqLen
     */
    const float* getCosTable(size_t seqLen) const;

    /**
     * @brief Get pre-computed sin table for sequence length
     * @param seqLen Sequence length (must be <= maxSeqLen)
     * @return Pointer to sin values [seqLen, headDim/2]
     * @throws std::runtime_error if not initialized
     * @throws std::out_of_range if seqLen > maxSeqLen
     */
    const float* getSinTable(size_t seqLen) const;

    /**
     * @brief Get combined cache in NPU-accessible format
     *
     * Returns interleaved [cos_data, sin_data] buffer suitable for
     * DMA transfer to NPU memory.
     *
     * @return Pointer to interleaved buffer
     * @throws std::runtime_error if not initialized
     */
    const void* getDeviceBuffer() const;

    /**
     * @brief Get device buffer size in bytes
     * @return Size in bytes
     */
    size_t getDeviceBufferSize() const;

    /**
     * @brief Get configuration
     * @return Current configuration
     */
    const Config& getConfig() const { return config_; }

    /**
     * @brief Check if cache is initialized
     * @return true if initialization complete
     */
    bool isInitialized() const { return initialized_; }

    /**
     * @brief Get pre-computation time (for profiling)
     * @return Initialization time in milliseconds
     */
    double getInitializationTimeMs() const { return initializationTimeMs_; }

private:
    Config config_;

    // Cosine cache: [maxSeqLen, headDim/2]
    std::vector<float> cosCache_;

    // Sine cache: [maxSeqLen, headDim/2]
    std::vector<float> sinCache_;

    // Device buffer: interleaved [cos..., sin...] for DMA transfer
    std::unique_ptr<uint8_t[]> deviceBuffer_;
    size_t deviceBufferSize_ = 0;

    // Initialization state
    bool initialized_ = false;
    double initializationTimeMs_ = 0.0;

    // Initialization methods
    void initialize();
    void computeAngles();

    /**
     * @brief Calculate inverse frequency for dimension i
     * @param i Dimension index (0 to headDim/2 - 1)
     * @param headDim Head dimension
     * @param theta RoPE theta parameter
     * @return Inverse frequency: 1 / (theta ^ (2*i/headDim))
     */
    float getInverseFrequency(size_t i, size_t headDim, float theta) const;
};

} // namespace runtime
} // namespace iron
