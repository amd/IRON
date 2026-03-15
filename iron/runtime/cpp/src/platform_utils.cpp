// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file platform_utils.cpp
 * @brief Platform detection and utility functions
 *
 * This file provides cross-platform utilities for:
 * - Runtime platform detection
 * - File system operations
 * - Environment variable access
 * - Logging and debugging
 * - Performance timing
 *
 * DESIGN NOTES:
 * - Uses conditional compilation for platform-specific code
 * - Provides unified interface regardless of platform
 * - Minimizes external dependencies
 */

#include <iron/runtime/platform_utils.hpp>
#include <iron/runtime/npu_runtime.hpp>

#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <chrono>
#include <iomanip>
#include <cctype>
#include <algorithm>
#include <iostream>

// Platform-specific headers
#if defined(_WIN32) || defined(_WIN64)
    #ifndef WIN32_LEAN_AND_MEAN
        #define WIN32_LEAN_AND_MEAN
    #endif
    #include <windows.h>
    #include <direct.h>
    #define IRON_PATH_SEPARATOR '\\'
#else
    #include <unistd.h>
    #include <sys/stat.h>
    #include <dlfcn.h>
    #define IRON_PATH_SEPARATOR '/'
#endif

namespace iron {
namespace runtime {
namespace platform {

//==============================================================================
// Platform Detection
//==============================================================================

/**
 * @brief Detect current operating system
 */
OperatingSystem getOperatingSystem() {
#if defined(_WIN32) || defined(_WIN64)
    return OperatingSystem::Windows;
#elif defined(__linux__)
    return OperatingSystem::Linux;
#elif defined(__APPLE__)
    return OperatingSystem::MacOS;
#elif defined(__unix__)
    return OperatingSystem::Unix;
#else
    return OperatingSystem::Unknown;
#endif
}

/**
 * @brief Get OS name as string
 */
const char* getOperatingSystemName() {
    switch (getOperatingSystem()) {
        case OperatingSystem::Windows:
            return "Windows";
        case OperatingSystem::Linux:
            return "Linux";
        case OperatingSystem::MacOS:
            return "macOS";
        case OperatingSystem::Unix:
            return "Unix";
        default:
            return "Unknown";
    }
}

/**
 * @brief Check if running on 64-bit system
 */
bool is64Bit() {
#if defined(_WIN64) || defined(__x86_64__) || defined(__aarch64__)
    return true;
#else
    return false;
#endif
}

//==============================================================================
// File System Utilities
//==============================================================================

/**
 * @brief Check if file exists
 */
bool fileExists(const std::string& path) {
    if (path.empty()) {
        return false;
    }

#if defined(_WIN32) || defined(_WIN64)
    struct _stat buffer;
    return (_wstat(std::wstring(path.begin(), path.end()).c_str(), &buffer) == 0);
#else
    struct stat buffer;
    return (stat(path.c_str(), &buffer) == 0);
#endif
}

/**
 * @brief Check if path is a directory
 */
bool isDirectory(const std::string& path) {
    if (path.empty()) {
        return false;
    }

#if defined(_WIN32) || defined(_WIN64)
    struct _stat buffer;
    if (_wstat(std::wstring(path.begin(), path.end()).c_str(), &buffer) != 0) {
        return false;
    }
    return (buffer.st_mode & _S_IFDIR) != 0;
#else
    struct stat buffer;
    if (stat(path.c_str(), &buffer) != 0) {
        return false;
    }
    return S_ISDIR(buffer.st_mode);
#endif
}

/**
 * @brief Get file size in bytes
 */
size_t getFileSize(const std::string& path) {
    if (path.empty() || !fileExists(path)) {
        return 0;
    }

#if defined(_WIN32) || defined(_WIN64)
    struct _stat buffer;
    _wstat(std::wstring(path.begin(), path.end()).c_str(), &buffer);
    return static_cast<size_t>(buffer.st_size);
#else
    struct stat buffer;
    stat(path.c_str(), &buffer);
    return static_cast<size_t>(buffer.st_size);
#endif
}

/**
 * @brief Read entire file into memory
 */
std::vector<uint8_t> readFile(const std::string& path) {
    std::vector<uint8_t> data;

    if (!fileExists(path)) {
        throw RuntimeError("File not found: " + path);
    }

    std::ifstream file(path, std::ios::binary | std::ios::ate);
    if (!file.is_open()) {
        throw RuntimeError("Failed to open file: " + path);
    }

    auto size = file.tellg();
    file.seekg(0, std::ios::beg);

    data.resize(static_cast<size_t>(size));
    if (!file.read(reinterpret_cast<char*>(data.data()), size)) {
        throw RuntimeError("Failed to read file: " + path);
    }

    return data;
}

/**
 * @brief Get absolute path
 */
std::string getAbsolutePath(const std::string& path) {
    if (path.empty()) {
        return "";
    }

#if defined(_WIN32) || defined(_WIN64)
    char absPath[MAX_PATH];
    if (_fullpath(absPath, path.c_str(), MAX_PATH) != nullptr) {
        return std::string(absPath);
    }
#else
    char* absPath = realpath(path.c_str(), nullptr);
    if (absPath != nullptr) {
        std::string result(absPath);
        free(absPath);
        return result;
    }
#endif

    // Fallback: return original path
    return path;
}

/**
 * @brief Get directory component of path
 */
std::string getDirectory(const std::string& path) {
    size_t pos = path.find_last_of("/\\");
    if (pos == std::string::npos) {
        return "";
    }
    return path.substr(0, pos);
}

/**
 * @brief Get filename component of path
 */
std::string getFilename(const std::string& path) {
    size_t pos = path.find_last_of("/\\");
    if (pos == std::string::npos) {
        return path;
    }
    return path.substr(pos + 1);
}

/**
 * @brief Get filename without extension
 */
std::string getStem(const std::string& path) {
    std::string filename = getFilename(path);
    size_t pos = filename.find_last_of('.');
    if (pos == std::string::npos) {
        return filename;
    }
    return filename.substr(0, pos);
}

/**
 * @brief Get file extension (including dot)
 */
std::string getExtension(const std::string& path) {
    std::string filename = getFilename(path);
    size_t pos = filename.find_last_of('.');
    if (pos == std::string::npos) {
        return "";
    }
    return filename.substr(pos);
}

/**
 * @brief Join path components
 */
std::string joinPath(const std::string& base, const std::string& path) {
    if (base.empty()) return path;
    if (path.empty()) return base;

    // Check if path is already absolute
    if (isAbsolutePath(path)) {
        return path;
    }

    char lastChar = base.back();
    if (lastChar == '/' || lastChar == '\\') {
        return base + path;
    } else {
        return base + static_cast<char>(IRON_PATH_SEPARATOR) + path;
    }
}

/**
 * @brief Check if path is absolute
 */
bool isAbsolutePath(const std::string& path) {
    if (path.empty()) {
        return false;
    }

#if defined(_WIN32) || defined(_WIN64)
    // Windows: Check for drive letter or UNC path
    if (path.size() >= 2 && path[1] == ':') {
        return true;
    }
    if (path.size() >= 2 && path[0] == '\\' && path[1] == '\\') {
        return true;  // UNC path
    }
    return false;
#else
    // Unix: Check for leading slash
    return path[0] == '/';
#endif
}

//==============================================================================
// Environment Variables
//==============================================================================

/**
 * @brief Get environment variable value
 */
std::optional<std::string> getEnvVar(const char* name) {
    if (!name) {
        return std::nullopt;
    }

#if defined(_WIN32) || defined(_WIN64)
    char* value = nullptr;
    size_t len = 0;
    if (_dupenv_s(&value, &len, name) == 0 && value != nullptr) {
        std::string result(value);
        free(value);
        return result;
    }
#else
    const char* value = std::getenv(name);
    if (value != nullptr) {
        return std::string(value);
    }
#endif

    return std::nullopt;
}

/**
 * @brief Set environment variable
 */
bool setEnvVar(const char* name, const std::string& value) {
    if (!name) {
        return false;
    }

#if defined(_WIN32) || defined(_WIN64)
    return _putenv_s(name, value.c_str()) == 0;
#else
    return setenv(name, value.c_str(), 1) == 0;
#endif
}

/**
 * @brief Check if environment variable is truthy
 */
bool isEnvVarTruthy(const char* name) {
    auto value = getEnvVar(name);
    if (!value.has_value()) {
        return false;
    }

    std::string val = value.value();
    std::transform(val.begin(), val.end(), val.begin(),
                   [](unsigned char c) { return std::tolower(c); });

    return (val == "1" || val == "true" || val == "yes" || val == "on");
}

//==============================================================================
// Timing Utilities
//==============================================================================

/**
 * @brief Get current time in microseconds
 */
uint64_t getCurrentTimeMicros() {
    auto now = std::chrono::high_resolution_clock::now();
    auto duration = now.time_since_epoch();
    return std::chrono::duration_cast<std::chrono::microseconds>(duration).count();
}

/**
 * @brief Get current time in milliseconds
 */
uint64_t getCurrentTimeMillis() {
    auto now = std::chrono::high_resolution_clock::now();
    auto duration = now.time_since_epoch();
    return std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();
}

/**
 * @brief Scope timer for performance measurement
 */
ScopeTimer::ScopeTimer(const std::string& label)
    : label_(label)
    , start_(getCurrentTimeMicros()) {}

ScopeTimer::~ScopeTimer() {
    auto end = getCurrentTimeMicros();
    auto elapsed = end - start_;
    // In production, this would log to a profiling system
    // For now, just provide the infrastructure
}

uint64_t ScopeTimer::elapsed() const {
    return getCurrentTimeMicros() - start_;
}

//==============================================================================
// String Utilities
//==============================================================================

/**
 * @brief Trim whitespace from string
 */
std::string trim(const std::string& str) {
    auto start = std::find_if_not(str.begin(), str.end(),
                                  [](unsigned char c) { return std::isspace(c); });
    auto end = std::find_if_not(str.rbegin(), str.rend(),
                                [](unsigned char c) { return std::isspace(c); }).base();
    return (start < end) ? std::string(start, end) : "";
}

/**
 * @brief Split string by delimiter
 */
std::vector<std::string> split(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::istringstream iss(str);
    std::string token;

    while (std::getline(iss, token, delimiter)) {
        if (!token.empty()) {
            tokens.push_back(token);
        }
    }

    return tokens;
}

/**
 * @brief Join strings with delimiter
 */
std::string join(const std::vector<std::string>& parts, const std::string& delimiter) {
    if (parts.empty()) return "";

    std::ostringstream oss;
    oss << parts[0];

    for (size_t i = 1; i < parts.size(); ++i) {
        oss << delimiter << parts[i];
    }

    return oss.str();
}

/**
 * @brief Convert string to lowercase
 */
std::string toLower(const std::string& str) {
    std::string result = str;
    std::transform(result.begin(), result.end(), result.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    return result;
}

/**
 * @brief Convert string to uppercase
 */
std::string toUpper(const std::string& str) {
    std::string result = str;
    std::transform(result.begin(), result.end(), result.begin(),
                   [](unsigned char c) { return std::toupper(c); });
    return result;
}

//==============================================================================
// Logging Utilities
//==============================================================================

namespace log {

static LogLevel gCurrentLogLevel = LogLevel::Info;
static LogCallback gLogCallback = nullptr;

void setLogLevel(LogLevel level) {
    gCurrentLogLevel = level;
}

LogLevel getLogLevel() {
    return gCurrentLogLevel;
}

void setLogCallback(LogCallback callback) {
    gLogCallback = callback;
}

const char* levelToString(LogLevel level) {
    switch (level) {
        case LogLevel::Debug: return "DEBUG";
        case LogLevel::Info:  return "INFO";
        case LogLevel::Warning: return "WARNING";
        case LogLevel::Error: return "ERROR";
        default: return "UNKNOWN";
    }
}

void log(LogLevel level, const std::string& message) {
    if (level < gCurrentLogLevel) {
        return;
    }

    auto timestamp = getCurrentTimeMillis();
    std::ostringstream oss;
    oss << "[" << levelToString(level) << "] "
        << "[" << timestamp << "ms] "
        << message;

    if (gLogCallback) {
        gLogCallback(level, oss.str());
    } else {
        // Default: output to stderr for errors, stdout for others
        if (level >= LogLevel::Warning) {
            std::cerr << oss.str() << std::endl;
        } else {
            std::cout << oss.str() << std::endl;
        }
    }
}

} // namespace log

} // namespace platform

} // namespace runtime
} // namespace iron

//==============================================================================
// Library Handle Implementation
//==============================================================================

namespace iron {
namespace runtime {
namespace platform {

LibraryHandle::LibraryHandle(const std::string& path)
    : handle_(nullptr)
    , valid_(false) {

#if defined(_WIN32) || defined(_WIN64)
        handle_ = LoadLibraryA(path.c_str());
#else
        handle_ = dlopen(path.c_str(), RTLD_LAZY | RTLD_LOCAL);
#endif
    valid_ = (handle_ != nullptr);
}

LibraryHandle::~LibraryHandle() {
    if (handle_) {
#if defined(_WIN32) || defined(_WIN64)
        FreeLibrary(static_cast<HMODULE>(handle_));
#else
        dlclose(handle_);
#endif
    }
}

LibraryHandle::LibraryHandle(LibraryHandle&& other) noexcept
    : handle_(other.handle_)
    , valid_(other.valid_) {
    other.handle_ = nullptr;
    other.valid_ = false;
}

LibraryHandle& LibraryHandle::operator=(LibraryHandle&& other) noexcept {
    if (this != &other) {
        if (handle_) {
#if defined(_WIN32) || defined(_WIN64)
            FreeLibrary(static_cast<HMODULE>(handle_));
#else
            dlclose(handle_);
#endif
        }
        handle_ = other.handle_;
        valid_ = other.valid_;
        other.handle_ = nullptr;
        other.valid_ = false;
    }
    return *this;
}

[[nodiscard]] bool LibraryHandle::isValid() const { return valid_; }

template<typename T>
T LibraryHandle::getSymbol(const char* name) const {
    if (!valid_ || !handle_) {
        return nullptr;
    }

#if defined(_WIN32) || defined(_WIN64)
    return reinterpret_cast<T>(GetProcAddress(static_cast<HMODULE>(handle_), name));
#else
    return reinterpret_cast<T>(dlsym(handle_, name));
#endif
}

[[nodiscard]] std::string LibraryHandle::getError() const {
    if (valid_) return "";

#if defined(_WIN32) || defined(_WIN64)
    DWORD error = GetLastError();
    return "LoadLibrary failed with error " + std::to_string(error);
#else
    const char* error = dlerror();
    return error ? std::string(error) : "dlopen failed";
#endif
}

// Explicit template instantiations for common symbol types
template void* LibraryHandle::getSymbol<void*>(const char*) const;
template void(*LibraryHandle::getSymbol<void(*)()>(const char*) const)(void);

} // namespace platform
} // namespace runtime
} // namespace iron
