# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

#[=============================================================================[
  @file CMakeLists.txt
  @brief CMake build configuration for IRON Operators

  This CMakeLists.txt builds the IRON operator library, including:
  - Convolution operators (Conv2D, Conv3D)
  - Normalization operators (RMSNorm, LayerNorm)
  - Activation operators (SiLU, GeLU, ReLU)
  - Attention operators (RoPE, Softmax)
  - Element-wise operators

  USAGE:
    @code
    # Add to your CMakeLists.txt
    add_subdirectory(iron/operators)
    target_link_libraries(your_target PRIVATE iron::operators)
    @endcode

  #]=============================================================================]

cmake_minimum_required(VERSION 3.16)

# Prevent in-source builds
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_BINARY_DIR)
    message(FATAL_ERROR "In-source builds are not allowed. Please use a separate build directory.")
endif()

project(iron_operators
    VERSION 1.0.0
    DESCRIPTION "IRON Operator Library"
    LANGUAGES CXX
)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Generate compile_commands.json
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

#[=============================================================================[
  Build Options
  #]=============================================================================]

option(IRON_OPERATORS_BUILD_TESTS "Build operator tests" OFF)
option(IRON_OPERATORS_ENABLE_BF16 "Enable bfloat16 support" ON)
option(IRON_OPERATORS_ENABLE_AVX512 "Enable AVX-512 optimizations" OFF)
option(IRON_OPERATORS_ENABLE_NEON "Enable NEON optimizations" ON)

#[=============================================================================[
  Compiler Flags
  #]=============================================================================]

add_library(iron_operators_flags INTERFACE)
target_compile_features(iron_operators_flags INTERFACE cxx_std_17)

# bfloat16 support
if(IRON_OPERATORS_ENABLE_BF16)
    target_compile_definitions(iron_operators_flags PRIVATE IRON_ENABLE_BF16)

    # Check for native bfloat16 support
    include(CheckCXXSourceCompiles)
    check_cxx_source_compiles("
        #include <stdint.h>
        #if defined(__ARM_NEON) || defined(__AVX512F__)
        #include <arm_bf16.h>
        #endif
        int main() { return 0; }
    " HAS_NATIVE_BF16)

    if(HAS_NATIVE_BF16)
        target_compile_definitions(iron_operators_flags PRIVATE HAS_NATIVE_BF16)
        message(STATUS "Native bfloat16 support detected")
    else()
        message(STATUS "Using software bfloat16 emulation")
    endif()
endif()

# Platform-specific optimizations
if(MSVC)
    target_compile_options(iron_operators_flags INTERFACE
        /W4
        /permissive-
        /Zc:__cplusplus
        /utf-8
    )
else()
    target_compile_options(iron_operators_flags INTERFACE
        -Wall
        -Wextra
        -Wpedantic
    )

    if(IRON_OPERATORS_ENABLE_AVX512)
        target_compile_options(iron_operators_flags INTERFACE -mavx512f -mavx512bw)
    endif()

    if(IRON_OPERATORS_ENABLE_NEON AND CMAKE_SYSTEM_PROCESSOR MATCHES "arm|aarch64")
        target_compile_options(iron_operators_flags INTERFACE -mfpu=neon)
    endif()
endif()

#[=============================================================================[
  Operator Sources
  #]=============================================================================]

# Convolution operators
set(CONV2D_SOURCES
    conv2d/conv2d_bf16_vector.cpp
    conv2d/conv2d_bf16_scalar.cpp
    conv2d/depthwise_conv2d_bf16_vector.cpp
    conv2d/pointwise_conv2d_bf16_vector.cpp
)

set(CONV3D_SOURCES
    conv3d/conv3d_bf16_vector.cpp
    conv3d/conv3d_bf16_large_kernel.cpp
    conv3d/depthwise_conv3d_bf16_vector.cpp
    conv3d/pointwise_conv3d_bf16_vector.cpp
)

# Normalization operators (NEW - for Llama3.2)
set(NORMALIZATION_SOURCES
    normalization/rmsnorm_bf16.cpp
)

# Activation operators (NEW - for Llama3.2)
set(ACTIVATION_SOURCES
    activations/silu_bf16.cpp
)

# Attention operators (NEW - for Llama3.2)
set(ATTENTION_SOURCES
    rope/rope_bf16.cpp
    softmax/softmax_bf16.cpp
)

# Element-wise operators
set(ELEMENTWISE_SOURCES
    elementwise_add/elementwise_add_bf16.cpp
    elementwise_mul/elementwise_mul_bf16.cpp
)

# Combine all sources
set(IRON_OPERATORS_SOURCES
    ${CONV2D_SOURCES}
    ${CONV3D_SOURCES}
    ${NORMALIZATION_SOURCES}
    ${ACTIVATION_SOURCES}
    ${ATTENTION_SOURCES}
    ${ELEMENTWISE_SOURCES}
)

# Header files
set(IRON_OPERATORS_HEADERS
    conv2d/conv2d_bf16.hpp
    conv3d/conv3d_bf16.hpp
    normalization/rmsnorm_bf16.hpp
    activations/silu_bf16.hpp
    rope/rope_bf16.hpp
    softmax/softmax_bf16.hpp
)

#[=============================================================================[
  Library Target
  #]=============================================================================]

# Check which source files actually exist
set(EXISTING_SOURCES "")
foreach(src ${IRON_OPERATORS_SOURCES})
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/${src}")
        list(APPEND EXISTING_SOURCES ${src})
        message(STATUS "Found operator source: ${src}")
    else()
        message(STATUS "Operator source not found (will be implemented): ${src}")
    endif()
endforeach()

# Create library with existing sources
if(EXISTING_SOURCES)
    add_library(iron_operators STATIC ${EXISTING_SOURCES})
else()
    # Create interface library if no sources exist yet
    add_library(iron_operators INTERFACE)
endif()

# Add alias
add_library(iron::operators ALIAS iron_operators)

# Include directories
target_include_directories(iron_operators
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include/iron/operators>
)

# Link compiler flags
target_link_libraries(iron_operators
    PRIVATE
        iron_operators_flags
)

# Set library properties
set_target_properties(iron_operators PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    POSITION_INDEPENDENT_CODE ON
)

#[=============================================================================[
  Installation
  #]=============================================================================]

include(GNUInstallDirs)

# Install headers
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/iron/operators
    FILES_MATCHING PATTERN "*.hpp"
)

#[=============================================================================[
  Tests
  #]=============================================================================]

if(IRON_OPERATORS_BUILD_TESTS)
    message(STATUS "Building operator tests")

    enable_testing()

    # Find GTest
    find_package(GTest QUIET)
    if(NOT GTest_FOUND)
        include(FetchContent)
        FetchContent_Declare(
            googletest
            URL https://github.com/google/googletest/archive/release-1.13.0.zip
        )
        FetchContent_MakeAvailable(googletest)
    endif()

    # RMSNorm test
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/normalization/rmsnorm_bf16.cpp")
        add_executable(test_rmsnorm ../../tests/operators/test_rmsnorm.cpp)
        target_link_libraries(test_rmsnorm PRIVATE iron_operators GTest::gtest_main)
        gtest_discover_tests(test_rmsnorm)
    endif()

    # RoPE test
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/rope/rope_bf16.cpp")
        add_executable(test_rope ../../tests/operators/test_rope.cpp)
        target_link_libraries(test_rope PRIVATE iron_operators GTest::gtest_main)
        gtest_discover_tests(test_rope)
    endif()

    # SiLU test
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/activations/silu_bf16.cpp")
        add_executable(test_silu ../../tests/operators/test_silu.cpp)
        target_link_libraries(test_silu PRIVATE iron_operators GTest::gtest_main)
        gtest_discover_tests(test_silu)
    endif()

    # Softmax test
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/softmax/softmax_bf16.cpp")
        add_executable(test_softmax ../../tests/operators/test_softmax.cpp)
        target_link_libraries(test_softmax PRIVATE iron_operators GTest::gtest_main)
        gtest_discover_tests(test_softmax)
    endif()
endif()

#[=============================================================================[
  Summary
  #]=============================================================================]

message(STATUS "")
message(STATUS "IRON Operators Configuration Summary:")
message(STATUS "  Version:        ${PROJECT_VERSION}")
message(STATUS "  Build type:     ${CMAKE_BUILD_TYPE}")
message(STATUS "  bfloat16:       ${IRON_OPERATORS_ENABLE_BF16}")
message(STATUS "  AVX-512:        ${IRON_OPERATORS_ENABLE_AVX512}")
message(STATUS "  NEON:           ${IRON_OPERATORS_ENABLE_NEON}")
message(STATUS "  Build tests:    ${IRON_OPERATORS_BUILD_TESTS}")
message(STATUS "")
