# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

#[=============================================================================[
  @file CMakeLists.txt
  @brief CMake build configuration for IRON NPU Runtime C++ library

  This CMakeLists.txt builds the IRON NPU Runtime C++ library, which provides
  a unified interface for NPU kernel execution on Linux (XRT) and Windows (xDNA).

  BUILD OPTIONS:
    IRON_BUILD_SHARED     - Build shared library (default: ON)
    IRON_BUILD_TESTS      - Build test suite (default: OFF)
    IRON_BUILD_EXAMPLES   - Build example programs (default: OFF)
    IRON_USE_XRT          - Enable XRT backend for Linux (default: ON on Linux)
    IRON_USE_XDNA         - Enable xDNA backend for Windows (default: ON on Windows)
    IRON_ENABLE_COVERAGE  - Enable code coverage (default: OFF)
    IRON_ENABLE_SANITIZER - Enable sanitizers (default: OFF)

  DEPENDENCIES:
    - C++17 compatible compiler (GCC 8+, Clang 7+, MSVC 2019+)
    - CMake 3.16 or higher
    - Linux: AMD XRT library (optional, for NPU support)
    - Windows: AMD xDNA Runtime SDK (optional, for NPU support)

  USAGE:
    @code
    # Add to your CMakeLists.txt
    find_package(IRON REQUIRED)
    target_link_libraries(your_target PRIVATE iron::runtime)
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

project(iron_runtime
    VERSION 1.0.0
    DESCRIPTION "IRON NPU Runtime Abstraction Layer"
    HOMEPAGE_URL "https://github.com/iron-project/iron"
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

option(IRON_BUILD_SHARED "Build shared library" ON)
option(IRON_BUILD_TESTS "Build test suite" OFF)
option(IRON_BUILD_EXAMPLES "Build example programs" OFF)
option(IRON_BUILD_DOCUMENTATION "Build documentation" OFF)
option(IRON_USE_XRT "Enable XRT backend for Linux" ON)
option(IRON_USE_XDNA "Enable xDNA backend for Windows" ON)
option(IRON_USE_ONNXRUNTIME "Enable ONNX Runtime GenAI backend for Windows" ON)
option(IRON_ENABLE_COVERAGE "Enable code coverage" OFF)
option(IRON_ENABLE_SANITIZER "Enable sanitizers" OFF)
option(IRON_ENABLE_WARNINGS_AS_ERRORS "Treat warnings as errors" OFF)

# Platform detection
if(WIN32)
    set(IRON_PLATFORM_WINDOWS TRUE)
    set(IRON_PLATFORM_LINUX FALSE)
else()
    set(IRON_PLATFORM_WINDOWS FALSE)
    set(IRON_PLATFORM_LINUX TRUE)
endif()

#[=============================================================================[
  Compiler Flags and Definitions
  #]=============================================================================]

# Common compiler flags
add_library(iron_compiler_flags INTERFACE)
target_compile_features(iron_compiler_flags INTERFACE cxx_std_17)

# Warning flags
if(MSVC)
    target_compile_options(iron_compiler_flags INTERFACE
        /W4
        /permissive-
        /Zc:__cplusplus
        /utf-8
    )
    if(IRON_ENABLE_WARNINGS_AS_ERRORS)
        target_compile_options(iron_compiler_flags INTERFACE /WX)
    endif()
else()
    target_compile_options(iron_compiler_flags INTERFACE
        -Wall
        -Wextra
        -Wpedantic
        -Wconversion
        -Wsign-conversion
        -Wcast-align
        -Wnull-dereference
        -Wdouble-promotion
    )
    if(IRON_ENABLE_WARNINGS_AS_ERRORS)
        target_compile_options(iron_compiler_flags INTERFACE -Werror)
    endif()
endif()

# Debug/Release flags
if(MSVC)
    target_compile_options(iron_compiler_flags INTERFACE
        $<$<CONFIG:Debug>:/Zi>
        $<$<CONFIG:Release>:/O2>
    )
else()
    target_compile_options(iron_compiler_flags INTERFACE
        $<$<CONFIG:Debug>:-g -O0>
        $<$<CONFIG:Release>:-O3 -DNDEBUG>
    )
endif()

# Code coverage
if(IRON_ENABLE_COVERAGE)
    if(NOT MSVC)
        target_compile_options(iron_compiler_flags INTERFACE --coverage)
        target_link_options(iron_compiler_flags INTERFACE --coverage)
    endif()
endif()

# Sanitizers
if(IRON_ENABLE_SANITIZER AND NOT MSVC)
    set(SANITIZER_FLAGS "-fsanitize=address,undefined")
    target_compile_options(iron_compiler_flags INTERFACE ${SANITIZER_FLAGS})
    target_link_options(iron_compiler_flags INTERFACE ${SANITIZER_FLAGS})
endif()

#[=============================================================================[
  External Dependencies
  #]=============================================================================]

# Find XRT on Linux
if(IRON_PLATFORM_LINUX AND IRON_USE_XRT)
    find_package(PkgConfig QUIET)
    if(PkgConfig_FOUND)
        pkg_check_modules(XRT xrt)
    endif()

    if(NOT XRT_FOUND)
        # Fallback: try to find XRT manually
        find_path(XRT_INCLUDE_DIR
            NAMES xrt/xrt.h
            PATHS
                /opt/xilinx/xrt/include
                /usr/local/include
                /usr/include
        )
        find_library(XRT_LIBRARY
            NAMES xrt_core xrt_coreutil
            PATHS
                /opt/xilinx/xrt/lib
                /usr/local/lib
                /usr/lib
        )

        if(XRT_INCLUDE_DIR AND XRT_LIBRARY)
            set(XRT_FOUND TRUE)
            set(XRT_INCLUDE_DIRS ${XRT_INCLUDE_DIR})
            set(XRT_LIBRARIES ${XRT_LIBRARY})
        endif()
    endif()

    if(XRT_FOUND)
        message(STATUS "XRT found: ${XRT_INCLUDE_DIRS}")
        add_definitions(-DIRON_HAS_XRT=1)
    else()
        message(WARNING "XRT not found - XRT backend will be disabled")
        add_definitions(-DIRON_HAS_XRT=0)
    endif()
endif()

# Find xDNA on Windows
if(IRON_PLATFORM_WINDOWS AND IRON_USE_XDNA)
    # Note: $ENV{ProgramFiles(x86)} requires escaping parentheses for CMake
    find_path(XDNA_INCLUDE_DIR
        NAMES xdna/xdna.h xdna_runtime.h
        PATHS
            "$ENV{ProgramFiles}/AMD/xDNA/include"
            "$ENV{ProgramFiles_x86_}/AMD/xDNA/include"
            "C:/Program Files/AMD/xDNA/include"
    )
    find_library(XDNA_LIBRARY
        NAMES xdna_runtime xdna
        PATHS
            "$ENV{ProgramFiles}/AMD/xDNA/lib"
            "$ENV{ProgramFiles_x86_}/AMD/xDNA/lib"
            "C:/Program Files/AMD/xDNA/lib"
    )

    if(XDNA_INCLUDE_DIR AND XDNA_LIBRARY)
        set(XDNA_FOUND TRUE)
        message(STATUS "xDNA found: ${XDNA_INCLUDE_DIR}")
        add_definitions(-DIRON_HAS_XDNA=1)
    else()
        message(WARNING "xDNA not found - xDNA backend will be disabled")
        add_definitions(-DIRON_HAS_XDNA=0)
    endif()
endif()

# Find ONNX Runtime GenAI on Windows
if(IRON_PLATFORM_WINDOWS AND IRON_USE_ONNXRUNTIME)
    # Search for ONNX Runtime GenAI in RyzenAI package locations
    # Header file is ort_genai.h located in LLM/include subdirectory
    find_path(ONNXRUNTIME_INCLUDE_DIR
        NAMES ort_genai.h ort_genai_c.h
        PATHS
            "$ENV{ProgramFiles}/RyzenAI"
            "C:/Program Files/RyzenAI"
            "$ENV{LOCALAPPDATA}/pip/cache"
            "$ENV{USERPROFILE}/.cache/lemonade/bin/ryzenai-server/npu"
        PATH_SUFFIXES
            "1.7.0/LLM/include"
            "1.6.0/LLM/include"
            "1.5.1/LLM/include"
            "LLM/include"
    )

    # Also check if ONNX Runtime GenAI is installed as Python package
    if(NOT ONNXRUNTIME_INCLUDE_DIR)
        execute_process(
            COMMAND python -c "import onnxruntime_genai; import os; print(os.path.dirname(onnxruntime_genai.__file__))"
            OUTPUT_VARIABLE ONNXRUNTIME_PYTHON_PATH
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
        if(ONNXRUNTIME_PYTHON_PATH)
            # For Python package, the DLL is available but headers may be in the RyzenAI install
            find_path(ONNXRUNTIME_INCLUDE_DIR
                NAMES ort_genai.h ort_genai_c.h
                PATHS
                    "$ENV{ProgramFiles}/RyzenAI"
                    "C:/Program Files/RyzenAI"
                PATH_SUFFIXES
                    "1.7.0/LLM/include"
                    "1.6.0/LLM/include"
                    "1.5.1/LLM/include"
            )
        endif()
    endif()

    find_library(ONNXRUNTIME_LIBRARY
        NAMES onnxruntime-genai onnxruntime
        PATHS
            "$ENV{ProgramFiles}/RyzenAI"
            "C:/Program Files/RyzenAI"
            "$ENV{USERPROFILE}/.cache/lemonade/bin/ryzenai-server/npu"
        PATH_SUFFIXES
            "lib"
            "1.7.0/lib"
            "1.6.0/lib"
            "1.5.1/lib"
            "1.7.0/LLM/lib"
            "1.6.0/LLM/lib"
            "1.5.1/LLM/lib"
    )

    if(ONNXRUNTIME_INCLUDE_DIR OR ONNXRUNTIME_LIBRARY)
        set(ONNXRUNTIME_FOUND TRUE)
        message(STATUS "ONNX Runtime GenAI found: ${ONNXRUNTIME_INCLUDE_DIR}")
        add_definitions(-DIRON_HAS_ONNXRUNTIME=1)
    else()
        message(WARNING "ONNX Runtime GenAI not found - ONNX backend will be disabled")
        add_definitions(-DIRON_HAS_ONNXRUNTIME=0)
    endif()
endif()

#[=============================================================================[
  Library Sources
  #]=============================================================================]

# Header files
set(IRON_RUNTIME_HEADERS
    include/iron/runtime/npu_runtime.hpp
    include/iron/runtime/xdna_runtime.hpp
    include/iron/runtime/xrt_runtime_wrapper.hpp
    include/iron/runtime/onnxruntime_genai.hpp
    include/iron/runtime/platform_utils.hpp
)

# Source files
set(IRON_RUNTIME_SOURCES
    src/npu_runtime.cpp
    src/platform_utils.cpp
)

# Platform-specific sources
if(IRON_PLATFORM_LINUX)
    list(APPEND IRON_RUNTIME_SOURCES src/xrt_runtime_impl.cpp)
elseif(IRON_PLATFORM_WINDOWS)
    # Windows: Add xDNA stub (always included for API compatibility)
    list(APPEND IRON_RUNTIME_SOURCES src/xdna_runtime_impl.cpp)

    # Add ONNX Runtime GenAI backend if enabled
    if(IRON_USE_ONNXRUNTIME)
        list(APPEND IRON_RUNTIME_SOURCES src/onnxruntime_genai_impl.cpp)
    endif()
endif()

#[=============================================================================[
  Library Target
  #]=============================================================================]

if(IRON_BUILD_SHARED)
    # Shared library
    add_library(iron_runtime SHARED ${IRON_RUNTIME_HEADERS} ${IRON_RUNTIME_SOURCES})
    target_compile_definitions(iron_runtime PRIVATE IRON_RUNTIME_EXPORTS)
    target_compile_definitions(iron_runtime PUBLIC IRON_RUNTIME_SHARED)
else()
    # Static library
    add_library(iron_runtime STATIC ${IRON_RUNTIME_HEADERS} ${IRON_RUNTIME_SOURCES})
endif()

# Add alias for use with add_subdirectory
add_library(iron::runtime ALIAS iron_runtime)

# Include directories
target_include_directories(iron_runtime
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

# Link compiler flags
target_link_libraries(iron_runtime
    PRIVATE
        iron_compiler_flags
)

# Platform-specific libraries
if(IRON_PLATFORM_LINUX)
    target_link_libraries(iron_runtime
        PRIVATE
            ${XRT_LIBRARIES}
            dl
            pthread
    )
    target_include_directories(iron_runtime
        PRIVATE
            ${XRT_INCLUDE_DIRS}
    )
endif()

if(IRON_PLATFORM_WINDOWS)
    # xDNA libraries (if available)
    if(XDNA_FOUND)
        target_link_libraries(iron_runtime
            PRIVATE
                ${XDNA_LIBRARY}
                ws2_32
        )
        target_include_directories(iron_runtime
            PRIVATE
                ${XDNA_INCLUDE_DIR}
        )
    endif()

    # ONNX Runtime GenAI libraries (if available)
    if(ONNXRUNTIME_FOUND)
        # Link both onnxruntime-genai and base onnxruntime libraries
        set(ONNXRUNTIME_LIBS ${ONNXRUNTIME_LIBRARY})
        # Add base onnxruntime.lib if not already included
        find_library(ONNXRUNTIME_BASE_LIBRARY
            NAMES onnxruntime
            PATHS
                "$ENV{ProgramFiles}/RyzenAI"
                "C:/Program Files/RyzenAI"
            PATH_SUFFIXES
                "lib"
                "1.7.0/lib"
                "1.6.0/lib"
                "1.5.1/lib"
        )
        if(ONNXRUNTIME_BASE_LIBRARY)
            list(APPEND ONNXRUNTIME_LIBS ${ONNXRUNTIME_BASE_LIBRARY})
        endif()

        target_link_libraries(iron_runtime
            PRIVATE
                ${ONNXRUNTIME_LIBS}
                ws2_32
        )
        # Add both the include dir and the onnxruntime subdirectory for C++ API headers
        # ONNXRUNTIME_INCLUDE_DIR points to LLM/include (ort_genai.h)
        # We also need onnxruntime/include for onnxruntime_cxx_api.h
        target_include_directories(iron_runtime
            PRIVATE
                ${ONNXRUNTIME_INCLUDE_DIR}
                "${ONNXRUNTIME_INCLUDE_DIR}/../../onnxruntime/include"
        )
    endif()
endif()

# Version definitions
target_compile_definitions(iron_runtime
    PRIVATE
        IRON_VERSION_MAJOR=${PROJECT_VERSION_MAJOR}
        IRON_VERSION_MINOR=${PROJECT_VERSION_MINOR}
        IRON_VERSION_PATCH=${PROJECT_VERSION_PATCH}
)

# Set library properties
set_target_properties(iron_runtime PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    PUBLIC_HEADER "${IRON_RUNTIME_HEADERS}"
    POSITION_INDEPENDENT_CODE ON
)

#[=============================================================================[
  Installation
  #]=============================================================================]

include(GNUInstallDirs)

# Install library
install(TARGETS iron_runtime
    EXPORT iron_runtime_targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/iron/runtime
)

# Install headers
install(DIRECTORY include/iron/runtime
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/iron
    FILES_MATCHING PATTERN "*.hpp"
)

# Install CMake configuration
install(EXPORT iron_runtime_targets
    FILE iron_runtime_targets.cmake
    NAMESPACE iron::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/iron_runtime
)

# Generate package config file
include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/iron_runtime_config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/iron_runtime_config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/iron_runtime
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/iron_runtime_config_version.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/iron_runtime_config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/iron_runtime_config_version.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/iron_runtime
)

#[=============================================================================[
  Tests
  #]=============================================================================]

if(IRON_BUILD_TESTS)
    message(STATUS "Building tests")

    enable_testing()

    # Find GTest
    find_package(GTest QUIET)
    if(NOT GTest_FOUND)
        # Fetch GTest if not found
        include(FetchContent)
        FetchContent_Declare(
            googletest
            URL https://github.com/google/googletest/archive/release-1.13.0.zip
        )
        FetchContent_MakeAvailable(googletest)
    endif()

    # Test executable
    add_executable(iron_runtime_tests
        tests/test_npu_runtime.cpp
        tests/test_buffer.cpp
        tests/test_kernel.cpp
        tests/test_platform_utils.cpp
    )

    target_link_libraries(iron_runtime_tests
        PRIVATE
            iron_runtime
            GTest::gtest_main
    )

    include(GoogleTest)
    gtest_discover_tests(iron_runtime_tests)
endif()

#[=============================================================================[
  Examples
  #]=============================================================================]

if(IRON_BUILD_EXAMPLES)
    message(STATUS "Building examples")

    # Basic example
    add_executable(example_basic examples/basic_usage.cpp)
    target_link_libraries(example_basic PRIVATE iron::runtime)

    # Buffer pooling example
    add_executable(example_buffer_pool examples/buffer_pool.cpp)
    target_link_libraries(example_buffer_pool PRIVATE iron::runtime)

    # Kernel execution example
    add_executable(example_kernel_exec examples/kernel_execution.cpp)
    target_link_libraries(example_kernel_exec PRIVATE iron::runtime)
endif()

#[=============================================================================[
  Documentation
  #]=============================================================================]

if(IRON_BUILD_DOCUMENTATION)
    find_package(Doxygen QUIET)
    if(DOXYGEN_FOUND)
        set(DOXYGEN_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/docs)
        set(DOXYGEN_GENERATE_HTML YES)
        set(DOXYGEN_GENERATE_MAN NO)

        doxygen_add_docs(iron_docs
            ${CMAKE_CURRENT_SOURCE_DIR}/include
            ${CMAKE_CURRENT_SOURCE_DIR}/src
            COMMENT "Generating API documentation with Doxygen"
        )
    endif()
endif()

#[=============================================================================[
  Python Bindings
  #]=============================================================================]

option(IRON_BUILD_PYTHON "Build Python bindings" OFF)

if(IRON_BUILD_PYTHON)
    message(STATUS "Building Python bindings")

    # Check if Python bindings directory exists
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../python/CMakeLists.txt")
        add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../python ${CMAKE_CURRENT_BINARY_DIR}/python)
    else()
        message(WARNING "Python bindings directory not found - disabling Python bindings")
    endif()
endif()

#[=============================================================================[
  Summary
  #]=============================================================================]

message(STATUS "")
message(STATUS "IRON Runtime Configuration Summary:")
message(STATUS "  Version:           ${PROJECT_VERSION}")
message(STATUS "  Build type:        ${CMAKE_BUILD_TYPE}")
message(STATUS "  Library type:      $<IF:$<BOOL:${IRON_BUILD_SHARED}>,SHARED,STATIC>")
message(STATUS "  Platform:          $<IF:$<BOOL:${IRON_PLATFORM_WINDOWS}>,Windows,Linux>")
message(STATUS "  C++ Standard:      ${CMAKE_CXX_STANDARD}")
if(IRON_PLATFORM_LINUX)
    message(STATUS "  XRT backend:     $<IF:$<BOOL:${XRT_FOUND}>,Enabled,Disabled>")
endif()
if(IRON_PLATFORM_WINDOWS)
    message(STATUS "  xDNA backend:    $<IF:$<BOOL:${XDNA_FOUND}>,Enabled,Disabled>")
endif()
message(STATUS "  Build tests:     ${IRON_BUILD_TESTS}")
message(STATUS "  Build examples:  ${IRON_BUILD_EXAMPLES}")
message(STATUS "  Coverage:        ${IRON_ENABLE_COVERAGE}")
message(STATUS "  Sanitizers:      ${IRON_ENABLE_SANITIZER}")
message(STATUS "")
