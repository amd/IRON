# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

#[=============================================================================[
  @file CMakeLists.txt
  @brief CMake build configuration for IRON NPU Runtime Python bindings

  This CMakeLists.txt builds the Python bindings for the IRON NPU runtime
  using pybind11, providing Python access to NPU kernel execution.

  BUILD OPTIONS:
    IRON_PYTHON_VERSION     - Python version to use (default: system default)
    IRON_PYBIND11_PATH      - Path to pybind11 (if not found by CMake)
    IRON_BUILD_PYTHON         - Build Python bindings (default: ON)

  DEPENDENCIES:
    - pybind11 >= 2.10.0
    - Python >= 3.8
    - IRON NPU Runtime library (iron::runtime)

  USAGE:
    @code
    # Build and install
    cmake -B build -S . -DIRON_BUILD_PYTHON=ON
    cmake --build build
    cmake --install build

    # Or copy .so/.pyd to Python path
    cp build/iron_runtime.cpython-*.so /path/to/site-packages/
    @endcode

  #=============================================================================]

cmake_minimum_required(VERSION 3.16)

# Prevent in-source builds
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_BINARY_DIR)
    message(FATAL_ERROR "In-source builds are not allowed. Please use a separate build directory.")
endif()

#[=============================================================================[
  Project Definition
  #=============================================================================]

project(iron_runtime_python
    VERSION 1.0.0
    DESCRIPTION "IRON NPU Runtime Python Bindings"
    LANGUAGES CXX
)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

#[=============================================================================[
  Build Options
  #=============================================================================]

option(IRON_BUILD_PYTHON "Build Python bindings" ON)
set(IRON_PYTHON_VERSION "" CACHE STRING "Python version to use (e.g., 3.8, 3.9)")
set(IRON_PYBIND11_PATH "" CACHE PATH "Path to pybind11 installation")

#[=============================================================================[
  Find Dependencies
  #=============================================================================]

# Find Python
if(IRON_PYTHON_VERSION)
    find_package(Python ${IRON_PYTHON_VERSION} COMPONENTS Interpreter Development REQUIRED)
else()
    find_package(Python COMPONENTS Interpreter Development REQUIRED)
endif()

message(STATUS "Python found: ${Python_EXECUTABLE}")
message(STATUS "Python version: ${Python_VERSION}")

# Find pybind11
if(IRON_PYBIND11_PATH)
    # Use specified pybind11 path
    list(APPEND CMAKE_PREFIX_PATH ${IRON_PYBIND11_PATH})
endif()

find_package(pybind11 2.10 CONFIG QUIET)

if(NOT pybind11_FOUND)
    # Fallback: use FetchContent to get pybind11
    message(STATUS "pybind11 not found, fetching from GitHub...")
    include(FetchContent)
    FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG v2.11.1
    )
    FetchContent_MakeAvailable(pybind11)
endif()

message(STATUS "pybind11 version: ${pybind11_VERSION}")

# Find IRON runtime library
find_package(iron_runtime CONFIG QUIET)

if(NOT iron_runtime_FOUND)
    # Try to build from source if not installed
    message(STATUS "IRON runtime not found as installed package, building from source...")

    # Check if we're in the right directory structure
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../cpp/CMakeLists.txt")
        add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../cpp ${CMAKE_CURRENT_BINARY_DIR}/cpp)
    else()
        message(FATAL_ERROR
            "IRON runtime library not found. Please either:\n"
            "1. Install the IRON runtime library first\n"
            "2. Build from the main CMakeLists.txt which includes this subdirectory"
        )
    endif()
endif()

#[=============================================================================[
  Python Module
  #=============================================================================]

# pybind11 module
pybind11_add_module(iron_runtime
    pybind11_bindings.cpp
)

# Link with IRON runtime
target_link_libraries(iron_runtime PRIVATE
    iron::runtime
)

# Include directories
target_include_directories(iron_runtime PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Set module properties
set_target_properties(iron_runtime PROPERTIES
    OUTPUT_NAME "iron_runtime"
    PREFIX ""  # No 'lib' prefix on Unix
    VERSION ${PROJECT_VERSION}
)

# Platform-specific settings
if(WIN32)
    # Windows: .pyd file
    set_target_properties(iron_runtime PROPERTIES
        SUFFIX ".pyd"
    )
else()
    # Unix: .so file with proper suffix
    set_target_properties(iron_runtime PROPERTIES
        SUFFIX ".so"
    )
endif()

#[=============================================================================[
  Installation
  #=============================================================================]

include(GNUInstallDirs)

# Install Python module
install(TARGETS iron_runtime
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/python/iron
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}/python/iron
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# Install Python package files
install(FILES
    __init__.py
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/python/iron
)

install(FILES
    README.md
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/python/iron
)

#[=============================================================================[
  Optional: Create Python wheel
  #=============================================================================]

# Check if we should build wheel
option(IRON_BUILD_WHEEL "Build Python wheel" OFF)

if(IRON_BUILD_WHEEL)
    # Find setuptools for wheel building
    execute_process(
        COMMAND ${Python_EXECUTABLE} -m pip --version
        OUTPUT_VARIABLE PIP_VERSION_OUTPUT
        ERROR_QUIET
        RESULT_VARIABLE PIP_RESULT
    )

    if(PIP_RESULT EQUAL 0)
        message(STATUS "pip found, wheel building enabled")

        # Create setup.py for wheel building
        configure_file(
            ${CMAKE_CURRENT_SOURCE_DIR}/setup.py.in
            ${CMAKE_CURRENT_BINARY_DIR}/setup.py
            @ONLY
        )

        # Add custom target for building wheel
        add_custom_target(wheel
            COMMAND ${Python_EXECUTABLE} -m pip wheel . --no-deps
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            COMMENT "Building Python wheel"
        )
    else()
        message(WARNING "pip not found, wheel building disabled")
    endif()
endif()

#[=============================================================================[
  Tests (optional)
  #=============================================================================]

option(IRON_BUILD_PYTHON_TESTS "Build Python binding tests" OFF)

if(IRON_BUILD_PYTHON_TESTS)
    # Find pytest
    execute_process(
        COMMAND ${Python_EXECUTABLE} -c "import pytest"
        ERROR_QUIET
        RESULT_VARIABLE PYTEST_RESULT
    )

    if(PYTEST_RESULT EQUAL 0)
        message(STATUS "pytest found, Python tests enabled")

        # Copy module to build directory for testing
        add_custom_command(TARGET iron_runtime POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:iron_runtime> ${CMAKE_CURRENT_BINARY_DIR}/
            COMMENT "Copying module to build directory for testing"
        )

        # Add test target
        add_custom_target(test_python
            COMMAND ${Python_EXECUTABLE} -m pytest tests/
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            DEPENDS iron_runtime
            COMMENT "Running Python binding tests"
        )
    else()
        message(STATUS "pytest not found, Python tests disabled")
    endif()
endif()

#[=============================================================================[
  Summary
  #=============================================================================]

message(STATUS "")
message(STATUS "IRON Runtime Python Bindings Configuration:")
message(STATUS "  Version:              ${PROJECT_VERSION}")
message(STATUS "  Build type:           ${CMAKE_BUILD_TYPE}")
message(STATUS "  Python executable:    ${Python_EXECUTABLE}")
message(STATUS "  Python version:       ${Python_VERSION}")
message(STATUS "  Python include:       ${Python_INCLUDE_DIRS}")
message(STATUS "  pybind11 version:     ${pybind11_VERSION}")
message(STATUS "  Build wheel:          ${IRON_BUILD_WHEEL}")
message(STATUS "  Build tests:          ${IRON_BUILD_PYTHON_TESTS}")
message(STATUS "")
