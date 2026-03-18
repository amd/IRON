// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file platform_utils.hpp
 * @brief Platform detection and utility functions header
 *
 * This header provides cross-platform utilities for:
 * - Runtime platform detection
 * - File system operations
 * - Environment variable access
 * - Logging and debugging
 * - Performance timing
 *
 * @note Most utilities are also available in npu_runtime.hpp
 *       This header provides additional low-level functions
 */

#pragma once

#include <cstdint>
#include <functional>
#include <memory>
#include <optional>
#include <string>
#include <vector>

namespace iron
{
namespace runtime
{
namespace platform
{

//==============================================================================
// Platform Detection
//==============================================================================

/**
 * @brief Operating system enumeration
 */
enum class OperatingSystem { Unknown, Windows, Linux, MacOS, Unix };

/**
 * @brief Detect current operating system
 */
[[nodiscard]] OperatingSystem getOperatingSystem();

/**
 * @brief Get OS name as string
 */
[[nodiscard]] const char *getOperatingSystemName();

/**
 * @brief Check if running on 64-bit system
 */
[[nodiscard]] bool is64Bit();

/**
 * @brief Check if running on Windows
 */
[[nodiscard]] inline bool isWindows()
{
    return getOperatingSystem() == OperatingSystem::Windows;
}

/**
 * @brief Check if running on Linux
 */
[[nodiscard]] inline bool isLinux()
{
    return getOperatingSystem() == OperatingSystem::Linux;
}

/**
 * @brief Check if running on macOS
 */
[[nodiscard]] inline bool isMacOS()
{
    return getOperatingSystem() == OperatingSystem::MacOS;
}

//==============================================================================
// File System Utilities
//==============================================================================

/**
 * @brief Check if file exists
 */
[[nodiscard]] bool fileExists(const std::string &path);

/**
 * @brief Check if path is a directory
 */
[[nodiscard]] bool isDirectory(const std::string &path);

/**
 * @brief Get file size in bytes
 */
[[nodiscard]] size_t getFileSize(const std::string &path);

/**
 * @brief Read entire file into memory
 *
 * @throws RuntimeError if file cannot be read
 */
[[nodiscard]] std::vector<uint8_t> readFile(const std::string &path);

/**
 * @brief Get absolute path
 */
[[nodiscard]] std::string getAbsolutePath(const std::string &path);

/**
 * @brief Get directory component of path
 */
[[nodiscard]] std::string getDirectory(const std::string &path);

/**
 * @brief Get filename component of path
 */
[[nodiscard]] std::string getFilename(const std::string &path);

/**
 * @brief Get filename without extension
 */
[[nodiscard]] std::string getStem(const std::string &path);

/**
 * @brief Get file extension (including dot)
 */
[[nodiscard]] std::string getExtension(const std::string &path);

/**
 * @brief Join path components
 */
[[nodiscard]] std::string joinPath(const std::string &base, const std::string &path);

/**
 * @brief Check if path is absolute
 */
[[nodiscard]] bool isAbsolutePath(const std::string &path);

//==============================================================================
// Environment Variables
//==============================================================================

/**
 * @brief Get environment variable value
 * @return Value if set, std::nullopt otherwise
 */
[[nodiscard]] std::optional<std::string> getEnvVar(const char *name);

/**
 * @brief Set environment variable
 * @return true if successful
 */
bool setEnvVar(const char *name, const std::string &value);

/**
 * @brief Check if environment variable is truthy
 */
[[nodiscard]] bool isEnvVarTruthy(const char *name);

//==============================================================================
// Timing Utilities
//==============================================================================

/**
 * @brief Get current time in microseconds
 */
[[nodiscard]] uint64_t getCurrentTimeMicros();

/**
 * @brief Get current time in milliseconds
 */
[[nodiscard]] uint64_t getCurrentTimeMillis();

/**
 * @brief Scope timer for performance measurement
 *
 * Usage:
 * @code
 * {
 *     ScopeTimer timer("My Operation");
 *     // ... code to measure
 * } // Timer automatically logs elapsed time on destruction
 * @endcode
 */
class ScopeTimer
{
  public:
    explicit ScopeTimer(const std::string &label);
    ~ScopeTimer();

    // Prevent copying
    ScopeTimer(const ScopeTimer &) = delete;
    ScopeTimer &operator=(const ScopeTimer &) = delete;

    /**
     * @brief Get elapsed time in microseconds
     */
    [[nodiscard]] uint64_t elapsed() const;

    /**
     * @brief Get label
     */
    [[nodiscard]] const std::string &label() const
    {
        return label_;
    }

  private:
    std::string label_;
    uint64_t start_;
};

//==============================================================================
// String Utilities
//==============================================================================

/**
 * @brief Trim whitespace from string
 */
[[nodiscard]] std::string trim(const std::string &str);

/**
 * @brief Split string by delimiter
 */
[[nodiscard]] std::vector<std::string> split(const std::string &str, char delimiter);

/**
 * @brief Join strings with delimiter
 */
[[nodiscard]] std::string join(const std::vector<std::string> &parts, const std::string &delimiter);

/**
 * @brief Convert string to lowercase
 */
[[nodiscard]] std::string toLower(const std::string &str);

/**
 * @brief Convert string to uppercase
 */
[[nodiscard]] std::string toUpper(const std::string &str);

//==============================================================================
// Logging Utilities
//==============================================================================

/**
 * @brief Log level enumeration
 */
enum class LogLevel { Debug = 0, Info = 1, Warning = 2, Error = 3 };

/**
 * @brief Log callback function type
 */
using LogCallback = std::function<void(LogLevel, const std::string &)>;

namespace log
{

/**
 * @brief Set global log level
 */
void setLogLevel(LogLevel level);

/**
 * @brief Get current log level
 */
[[nodiscard]] LogLevel getLogLevel();

/**
 * @brief Set log callback
 *
 * If set, all log messages will be routed to this callback.
 * If not set, messages go to stdout/stderr.
 */
void setLogCallback(LogCallback callback);

/**
 * @brief Get log level as string
 */
[[nodiscard]] const char *levelToString(LogLevel level);

/**
 * @brief Log a message
 */
void log(LogLevel level, const std::string &message);

/**
 * @brief Log debug message
 */
inline void debug(const std::string &message)
{
    log(LogLevel::Debug, message);
}

/**
 * @brief Log info message
 */
inline void info(const std::string &message)
{
    log(LogLevel::Info, message);
}

/**
 * @brief Log warning message
 */
inline void warning(const std::string &message)
{
    log(LogLevel::Warning, message);
}

/**
 * @brief Log error message
 */
inline void error(const std::string &message)
{
    log(LogLevel::Error, message);
}

} // namespace log

//==============================================================================
// Dynamic Library Loading
//==============================================================================

/**
 * @brief Dynamic library handle for runtime backend loading
 *
 * RAII wrapper for platform-specific dynamic library loading
 * (LoadLibrary/dlopen). Used for optional backend loading.
 *
 * EXAMPLE:
 * @code
 * auto lib = std::make_unique<LibraryHandle>("/path/to/backend.so");
 * if (!lib->isValid()) {
 *     throw RuntimeError("Failed to load backend: " + lib->getError());
 * }
 * auto func = lib->getSymbol<void(*)()>("my_function");
 * @endcode
 */
class LibraryHandle
{
  public:
    /**
     * @brief Load dynamic library
     * @param path Path to library file
     */
    explicit LibraryHandle(const std::string &path);

    ~LibraryHandle();

    // Prevent copying
    LibraryHandle(const LibraryHandle &) = delete;
    LibraryHandle &operator=(const LibraryHandle &) = delete;

    // Allow moving
    LibraryHandle(LibraryHandle &&other) noexcept;
    LibraryHandle &operator=(LibraryHandle &&other) noexcept;

    /**
     * @brief Check if library loaded successfully
     */
    [[nodiscard]] bool isValid() const;

    /**
     * @brief Get symbol from library
     * @tparam T Symbol type (function pointer or data pointer)
     * @param name Symbol name
     * @return Pointer to symbol, or nullptr if not found
     */
    template <typename T> T getSymbol(const char *name) const;

    /**
     * @brief Get last error message
     * @return Error string (empty if no error)
     */
    [[nodiscard]] std::string getError() const;

  private:
    void *handle_;
    bool valid_;
};

} // namespace platform
} // namespace runtime
} // namespace iron
