# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#[=============================================================================[
  @file CMakeLists.txt
  @brief CMake build configuration for Lemonade Router

  This CMakeLists.txt builds the Lemonade Router, which provides
  OpenAI-compatible API endpoints with support for multiple backends.

  BUILD OPTIONS:
    LEMONADE_BUILD_SHARED   - Build shared library (default: ON)
    LEMONADE_BUILD_TESTS    - Build test suite (default: OFF)
    LEMONADE_ENABLE_TRAY    - Enable system tray support (default: OFF)

  DEPENDENCIES:
    - C++17 compatible compiler (GCC 8+, Clang 7+, MSVC 2019+)
    - CMake 3.16 or higher
    - httplib (embedded)
    - nlohmann/json (embedded)
    - Python 3.8+ (for subprocess backends)

  USAGE:
    @code
    # Add to your CMakeLists.txt
    add_subdirectory(lemonade)
    target_link_libraries(your_target PRIVATE lemonade::router)
    @endcode

  #]=============================================================================]

cmake_minimum_required(VERSION 3.16)

# Prevent in-source builds
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_BINARY_DIR)
    message(FATAL_ERROR "In-source builds are not allowed. Please use a separate build directory.")
endif()

#[=============================================================================[
  Project Definition
  #]=============================================================================]

project(lemonade_router
    VERSION 1.0.0
    DESCRIPTION "Lemonade LLM Inference Server Router"
    HOMEPAGE_URL "https://github.com/lemonade-server/lemonade"
    LANGUAGES CXX
)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Generate compile_commands.json for IDE integration
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

#[=============================================================================[
  Build Options
  #]=============================================================================]

option(LEMONADE_BUILD_SHARED "Build shared library" ON)
option(LEMONADE_BUILD_TESTS "Build test suite" OFF)
option(LEMONADE_ENABLE_TRAY "Enable system tray support" OFF)

# Platform detection
if(WIN32)
    set(LEMONADE_PLATFORM_WINDOWS TRUE)
    set(LEMONADE_PLATFORM_LINUX FALSE)
else()
    set(LEMONADE_PLATFORM_WINDOWS FALSE)
    set(LEMONADE_PLATFORM_LINUX TRUE)
endif()

#[=============================================================================[
  Compiler Flags
  #]=============================================================================]

add_library(lemonade_compiler_flags INTERFACE)
target_compile_features(lemonade_compiler_flags INTERFACE cxx_std_17)

# Warning flags
if(MSVC)
    target_compile_options(lemonade_compiler_flags INTERFACE /W4 /permissive- /utf-8)
else()
    target_compile_options(lemonade_compiler_flags INTERFACE -Wall -Wextra -Wpedantic)
endif()

# Debug/Release flags
if(MSVC)
    target_compile_options(lemonade_compiler_flags INTERFACE
        $<$<CONFIG:Debug>:/Zi>
        $<$<CONFIG:Release>:/O2>
    )
else()
    target_compile_options(lemonade_compiler_flags INTERFACE
        $<$<CONFIG:Debug>:-g -O0>
        $<$<CONFIG:Release>:-O3 -DNDEBUG>
    )
endif()

#[=============================================================================[
  Library Sources
  #]=============================================================================]

# Header files
set(LEMONADE_HEADERS
    src/cpp/include/lemon/lemonade.h
    src/cpp/include/lemon/wrapped_server.h
    src/cpp/include/lemon/server_capabilities.h
    src/cpp/include/lemon/error_types.h
    src/cpp/include/lemon/backend_manager.h
    src/cpp/include/lemon/model_manager.h
    src/cpp/include/lemon/backends/backend_utils.h
    src/cpp/include/lemon/backends/llamacpp_server.h
    src/cpp/include/lemon/backends/ryzenaiserver.h
    src/cpp/include/lemon/backends/whisper_server.h
    src/cpp/include/lemon/backends/kokoro_server.h
    src/cpp/include/lemon/backends/sd_server.h
    src/cpp/include/lemon/backends/flm_server.h
    src/cpp/include/lemon/backends/iron_server.h
    src/cpp/include/lemon/utils/process_manager.h
    src/cpp/include/lemon/utils/http_utils.h
    src/cpp/include/lemon/utils/json_utils.h
)

# Source files
set(LEMONADE_SOURCES
    src/cpp/server/lemonade.cpp
    src/cpp/server/wrapped_server.cpp
    src/cpp/server/backend_manager.cpp
    src/cpp/server/model_manager.cpp
    src/cpp/server/router.cpp
    src/cpp/server/backends/backend_utils.cpp
    src/cpp/server/backends/llamacpp_server.cpp
    src/cpp/server/backends/ryzenaiserver.cpp
    src/cpp/server/backends/whisper_server.cpp
    src/cpp/server/backends/kokoro_server.cpp
    src/cpp/server/backends/sd_server.cpp
    src/cpp/server/backends/flm_server.cpp
    src/cpp/server/backends/iron_server.cpp
    src/cpp/server/utils/process_manager.cpp
    src/cpp/server/utils/http_utils.cpp
    src/cpp/server/utils/json_utils.cpp
)

#[=============================================================================[
  Library Target
  #]=============================================================================]

if(LEMONADE_BUILD_SHARED)
    add_library(lemonade-router SHARED ${LEMONADE_HEADERS} ${LEMONADE_SOURCES})
    target_compile_definitions(lemonade-router PRIVATE LEMONADE_SHARED)
else()
    add_library(lemonade-router STATIC ${LEMONADE_HEADERS} ${LEMONADE_SOURCES})
endif()

# Add alias
add_library(lemonade::router ALIAS lemonade-router)

# Include directories
target_include_directories(lemonade-router
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/include>
        $<INSTALL_INTERFACE:include>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp
)

# Link libraries
target_link_libraries(lemonade-router
    PRIVATE
        lemonade_compiler_flags
)

# Platform-specific libraries
if(WIN32)
    target_link_libraries(lemonade-router PRIVATE ws2_32)
endif()

# Version definitions
target_compile_definitions(lemonade-router
    PRIVATE
        LEMONADE_VERSION_MAJOR=${PROJECT_VERSION_MAJOR}
        LEMONADE_VERSION_MINOR=${PROJECT_VERSION_MINOR}
        LEMONADE_VERSION_PATCH=${PROJECT_VERSION_PATCH}
)

# Conditional compilation for tray support
if(LEMONADE_ENABLE_TRAY)
    target_compile_definitions(lemonade-router PRIVATE LEMONADE_TRAY)
endif()

#[=============================================================================[
  Installation
  #]=============================================================================]

include(GNUInstallDirs)

install(TARGETS lemonade-router
    EXPORT lemonade_router_targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY src/cpp/include/lemon
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING PATTERN "*.h"
)

#[=============================================================================[
  Summary
  #]=============================================================================]

message(STATUS "")
message(STATUS "Lemonade Router Configuration Summary:")
message(STATUS "  Version:           ${PROJECT_VERSION}")
message(STATUS "  Build type:        ${CMAKE_BUILD_TYPE}")
message(STATUS "  Library type:      $<IF:$<BOOL:${LEMONADE_BUILD_SHARED}>,SHARED,STATIC>")
message(STATUS "  Platform:          $<IF:$<BOOL:${LEMONADE_PLATFORM_WINDOWS}>,Windows,Linux>")
message(STATUS "  System tray:       ${LEMONADE_ENABLE_TRAY}")
message(STATUS "")
