// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file npu_runtime.cpp
 * @brief Base implementation for NPU runtime abstraction layer
 *
 * This file contains the base implementation for the INpuRuntime interface,
 * including platform detection, factory methods, and common utilities.
 *
 * PLATFORM DETECTION:
 * - Compile-time: Preprocessor macros determine available backends
 * - Runtime: Device enumeration and availability checks
 *
 * THREAD SAFETY:
 * - Factory methods are thread-safe
 * - Runtime instances are NOT thread-safe by default
 * - Use external synchronization for concurrent access
 */

#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <iron/runtime/npu_runtime.hpp>
#include <sstream>

// Platform-specific includes
#if defined(_WIN32) || defined(_WIN64)
#define IRON_PLATFORM_WINDOWS 1
#define IRON_PLATFORM_LINUX 0
#if defined(IRON_HAS_XDNA) && IRON_HAS_XDNA
#include <iron/runtime/xdna_runtime.hpp>
#endif
#if defined(IRON_HAS_ONNXRUNTIME) && IRON_HAS_ONNXRUNTIME
#include <iron/runtime/onnxruntime_genai.hpp>
#endif
#else
#define IRON_PLATFORM_WINDOWS 0
#define IRON_PLATFORM_LINUX 1
#include <iron/runtime/xrt_runtime_wrapper.hpp>
#endif

namespace iron
{
namespace runtime
{

//==============================================================================
// Platform Detection Utilities
//==============================================================================

namespace detail
{

/**
 * @brief Get platform string from compile-time detection
 */
[[nodiscard]] std::string getCompileTimePlatform()
{
#if defined(_WIN32) || defined(_WIN64)
    return "windows";
#elif defined(__linux__)
    return "linux";
#elif defined(__APPLE__)
    return "macos";
#else
    return "unknown";
#endif
}

/**
 * @brief Check if environment variable is set to truthy value
 */
bool isEnvVarTruthy(const char *varName)
{
    if (!varName)
        return false;

    const char *value = std::getenv(varName);
    if (!value)
        return false;

    std::string val(value);
    std::transform(val.begin(), val.end(), val.begin(), ::tolower);

    return (val == "1" || val == "true" || val == "yes" || val == "on");
}

} // namespace detail

//==============================================================================
// INpuRuntime Static Implementations
//==============================================================================

bool INpuRuntime::isLinux()
{
    return getCurrentPlatform() == "linux";
}

bool INpuRuntime::isWindows()
{
    return getCurrentPlatform() == "windows";
}

std::string INpuRuntime::getCurrentPlatform()
{
    return detail::getCompileTimePlatform();
}

bool INpuRuntime::isDeviceAvailable()
{
#if IRON_PLATFORM_WINDOWS
// Check ONNX Runtime GenAI first (more likely to be available on modern Windows)
#if defined(IRON_HAS_ONNXRUNTIME) && IRON_HAS_ONNXRUNTIME
    if (OnnxRuntimeGenAiWrapper::isAvailable()) {
        return true;
    }
#endif

// Fallback to xDNA runtime
#if defined(IRON_HAS_XDNA) && IRON_HAS_XDNA
    return XdnaRuntime::isAvailable();
#else
    return false;
#endif
#elif IRON_PLATFORM_LINUX
    return XrtRuntimeWrapper::isAvailable();
#else
    return false;
#endif
}

std::vector<int> INpuRuntime::getAvailableDevices()
{
    std::vector<int> devices;

    // For now, assume single device (most common case)
    // In production, enumerate actual devices
    if (isDeviceAvailable()) {
        devices.push_back(0);
    }

    return devices;
}

std::unique_ptr<INpuRuntime> INpuRuntime::create(int deviceId)
{
#if IRON_PLATFORM_WINDOWS
// Windows: Try ONNX Runtime GenAI first (more likely to be available)
#if defined(IRON_HAS_ONNXRUNTIME) && IRON_HAS_ONNXRUNTIME
    if (OnnxRuntimeGenAiWrapper::isAvailable()) {
        return std::make_unique<OnnxRuntimeGenAiWrapper>(deviceId);
    }
#endif

// Fallback to xDNA runtime
#if defined(IRON_HAS_XDNA) && IRON_HAS_XDNA
    if (!XdnaRuntime::isAvailable()) {
        throw DeviceNotAvailableError(deviceId);
    }
    return std::make_unique<XdnaRuntime>(deviceId);
#else
    throw DeviceNotAvailableError(deviceId);
#endif

#elif IRON_PLATFORM_LINUX
    // Linux: Use XRT runtime
    if (!XrtRuntimeWrapper::isAvailable()) {
        throw DeviceNotAvailableError(deviceId);
    }
    return std::make_unique<XrtRuntimeWrapper>(deviceId);

#else
    // Unsupported platform
    throw RuntimeError("No NPU runtime available for this platform");
#endif
}

std::unique_ptr<INpuRuntime> INpuRuntime::createForPlatform(const std::string &platform, int deviceId)
{

    std::string lowerPlatform = platform;
    std::transform(lowerPlatform.begin(), lowerPlatform.end(), lowerPlatform.begin(), ::tolower);

    if (lowerPlatform == "mock" || lowerPlatform == "simulation") {
        // Return a mock runtime for testing
        // In production, this would create a MockRuntime instance
        throw RuntimeError("Mock runtime not implemented in this build");
    }

#if IRON_PLATFORM_LINUX
    if (lowerPlatform == "xrt" || lowerPlatform == "linux") {
        if (!XrtRuntimeWrapper::isAvailable()) {
            throw RuntimeError("XRT runtime not available");
        }
        return std::make_unique<XrtRuntimeWrapper>(deviceId);
    }
#endif

#if IRON_PLATFORM_WINDOWS
#if defined(IRON_HAS_XDNA) && IRON_HAS_XDNA
    if (lowerPlatform == "xdna" || lowerPlatform == "windows") {
        if (!XdnaRuntime::isAvailable()) {
            throw RuntimeError("xDNA runtime not available");
        }
        return std::make_unique<XdnaRuntime>(deviceId);
    }
#endif

#if defined(IRON_HAS_ONNXRUNTIME) && IRON_HAS_ONNXRUNTIME
    if (lowerPlatform == "onnx" || lowerPlatform == "onnxruntime") {
        if (!OnnxRuntimeGenAiWrapper::isAvailable()) {
            throw RuntimeError("ONNX Runtime GenAI not available");
        }
        return std::make_unique<OnnxRuntimeGenAiWrapper>(deviceId);
    }
#endif
#endif

    throw RuntimeError("Unsupported or unavailable platform: " + platform);
}

//==============================================================================
// KernelArgument Type Utilities
//==============================================================================

namespace detail
{

/**
 * @brief Get human-readable type name for KernelArgument
 */
const char *getKernelArgumentTypeName(const KernelArgument &arg)
{
    return std::visit(KernelArgumentVisitor{}, arg);
}

/**
 * @brief Validate kernel argument type matches expected type
 *
 * @param arg The argument value
 * @param expectedType Expected type name
 * @return true if type matches
 */
bool validateArgumentType(const KernelArgument &arg, const std::string &expectedType)
{
    const char *actualType = getKernelArgumentTypeName(arg);
    return expectedType == actualType;
}

} // namespace detail

//==============================================================================
// Buffer Utility Implementation
//==============================================================================

/**
 * @brief Allocate buffer and copy data
 *
 * Helper function for allocateBufferFromData implementations
 */
std::shared_ptr<IBuffer> allocateBufferWithInitialData(INpuRuntime *runtime, const void *data, size_t size)
{

    if (!runtime || !data || size == 0) {
        throw BufferError("Invalid parameters for buffer allocation");
    }

    auto buffer = runtime->allocateBuffer(size, true);
    buffer->write(data, size);

    return buffer;
}

//==============================================================================
// Error Code Utilities
//==============================================================================

namespace detail
{

/**
 * @brief Convert error code to human-readable string
 */
std::string errorCodeToString(int errorCode)
{
    std::ostringstream oss;

    // Common error codes
    switch (errorCode) {
    case 0:
        return "Success";
    case 1:
        return "General failure";
    case 2:
        return "Invalid argument";
    case 3:
        return "Device not found";
    case 4:
        return "Memory allocation failed";
    case 5:
        return "Timeout";
    case 6:
        return "I/O error";
    default:
        oss << "Unknown error code: " << errorCode;
        return oss.str();
    }
}

/**
 * @brief Get error category name
 */
const char *getErrorCategory(int errorCode)
{
    if (errorCode >= 0 && errorCode <= 100) {
        return "Runtime";
    } else if (errorCode >= 100 && errorCode <= 200) {
        return "Buffer";
    } else if (errorCode >= 200 && errorCode <= 300) {
        return "Kernel";
    } else {
        return "Unknown";
    }
}

} // namespace detail

//==============================================================================
// Version Information
//==============================================================================

// Version constants (file scope)
#define IRON_RUNTIME_VERSION "1.0.0"
#define IRON_VERSION_MAJOR 1
#define IRON_VERSION_MINOR 0
#define IRON_VERSION_PATCH 0

/**
 * @brief Get IRON runtime version
 */
std::string getIronRuntimeVersion()
{
    return IRON_RUNTIME_VERSION;
}

/**
 * @brief Get IRON runtime version components
 */
void getIronRuntimeVersion(int &major, int &minor, int &patch)
{
    major = IRON_VERSION_MAJOR;
    minor = IRON_VERSION_MINOR;
    patch = IRON_VERSION_PATCH;
}

} // namespace runtime
} // namespace iron
