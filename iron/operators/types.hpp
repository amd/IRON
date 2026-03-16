// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file types.hpp
 * @brief Common type definitions for IRON operators
 *
 * This header provides common type definitions used across all IRON operators,
 * including bfloat16 emulation for platforms without native support.
 *
 * @note Include this header before using any operator functions
 */

#pragma once

#include <cstdint>
#include <cmath>

namespace iron {
namespace operators {

//==============================================================================
// bfloat16 Type Definition
//==============================================================================

#if defined(__ARM_NEON) || defined(__AVX512F__) || defined(_M_ARM64)
    // Hardware bfloat16 support (ARM NEON or AVX-512F)
    #if defined(__ARM_NEON) || defined(_M_ARM64)
        #include <arm_bf16.h>
        using bfloat16 = __bf16;
    #elif defined(__AVX512F__)
        #include <immintrin.h>
        using bfloat16 = _Float16;
    #endif
#else
    // Software bfloat16 emulation for platforms without native support
    // This represents bfloat16 as a 16-bit value with:
    // - 1 sign bit
    // - 8 exponent bits (same as float32)
    // - 7 mantissa bits (truncated from float32's 23)
    struct bfloat16 {
        uint16_t val;

        /// Default constructor (initializes to zero)
        bfloat16() : val(0) {}

        /// Construct from float (truncates lower 16 bits of float32)
        bfloat16(float f) {
            val = static_cast<uint16_t>(static_cast<uint32_t>(f) >> 16);
        }

        /// Construct from int (converts to float first)
        bfloat16(int i) {
            val = static_cast<uint16_t>(static_cast<uint32_t>(static_cast<float>(i)) >> 16);
        }

        /// Implicit conversion to float
        operator float() const {
            uint32_t bits = (static_cast<uint32_t>(val) << 16);
            return *reinterpret_cast<const float*>(&bits);
        }

        /// Unary negation
        bfloat16 operator-() const {
            bfloat16 result;
            result.val = val ^ 0x8000; // Flip sign bit
            return result;
        }

        /// Addition assignment
        bfloat16& operator+=(const bfloat16& other) {
            *this = bfloat16(static_cast<float>(*this) + static_cast<float>(other));
            return *this;
        }

        /// Subtraction assignment
        bfloat16& operator-=(const bfloat16& other) {
            *this = bfloat16(static_cast<float>(*this) - static_cast<float>(other));
            return *this;
        }

        /// Multiplication assignment
        bfloat16& operator*=(const bfloat16& other) {
            *this = bfloat16(static_cast<float>(*this) * static_cast<float>(other));
            return *this;
        }

        /// Division assignment
        bfloat16& operator/=(const bfloat16& other) {
            *this = bfloat16(static_cast<float>(*this) / static_cast<float>(other));
            return *this;
        }
    };

    /// Binary addition
    inline bfloat16 operator+(const bfloat16& a, const bfloat16& b) {
        return bfloat16(static_cast<float>(a) + static_cast<float>(b));
    }

    /// Binary subtraction
    inline bfloat16 operator-(const bfloat16& a, const bfloat16& b) {
        return bfloat16(static_cast<float>(a) - static_cast<float>(b));
    }

    /// Binary multiplication
    inline bfloat16 operator*(const bfloat16& a, const bfloat16& b) {
        return bfloat16(static_cast<float>(a) * static_cast<float>(b));
    }

    /// Binary division
    inline bfloat16 operator/(const bfloat16& a, const bfloat16& b) {
        return bfloat16(static_cast<float>(a) / static_cast<float>(b));
    }

    /// Equality comparison
    inline bool operator==(const bfloat16& a, const bfloat16& b) {
        return static_cast<float>(a) == static_cast<float>(b);
    }

    /// Less than comparison
    inline bool operator<(const bfloat16& a, const bfloat16& b) {
        return static_cast<float>(a) < static_cast<float>(b);
    }

    /// Less than or equal comparison
    inline bool operator<=(const bfloat16& a, const bfloat16& b) {
        return static_cast<float>(a) <= static_cast<float>(b);
    }

    /// Greater than comparison
    inline bool operator>(const bfloat16& a, const bfloat16& b) {
        return static_cast<float>(a) > static_cast<float>(b);
    }

    /// Greater than or equal comparison
    inline bool operator>=(const bfloat16& a, const bfloat16& b) {
        return static_cast<float>(a) >= static_cast<float>(b);
    }
#endif

//==============================================================================
// Common Constants
//==============================================================================

/// Epsilon value for numerical stability in softmax and normalization
constexpr float kEpsilon = 1e-8f;

/// Epsilon value for RMSNorm (slightly larger for stability)
constexpr float kRmsEpsilon = 1e-6f;

/// Minimum float value (used for clamping)
constexpr float kMinFloat = -3.4028235e+38f;

/// Pi constant for trigonometric operations
constexpr float kPi = 3.14159265358979323846f;

} // namespace operators
} // namespace iron
