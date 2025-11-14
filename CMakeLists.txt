# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.24 FATAL_ERROR)

project(
    IRONCLAD
    VERSION       0.1.0
    DESCRIPTION   "IRONCLAD"
    HOMEPAGE_URL  "https://gitenterprise.xilinx.com/XRLabs/ironclad"
    LANGUAGES     CXX C
)

# Options
set(IRONCLAD_AIE_TARGET "aie2p" CACHE STRING "AIE architecture, select either aie2 or aie2p")
set_property(CACHE IRONCLAD_AIE_TARGET PROPERTY STRINGS "aie2" "aie2p")
if (IRONCLAD_AIE_TARGET STREQUAL "aie2")
    set(DEVICE npu)
    set(MAX_COLUMNS 4)
    set(AIE_COLS_LIST 1 2 4)
elseif (IRONCLAD_AIE_TARGET STREQUAL "aie2p")
    set(DEVICE npu2)
    set(MAX_COLUMNS 8)
    set(AIE_COLS_LIST 1 2 4 8)
else ()
    message(FATAL_ERROR "Unknown AIE target ${IRONCLAD_AIE_TARGET}")
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Find IRON and Peano Packages
# Use the Python in your active venv
find_package(Python3 COMPONENTS Interpreter REQUIRED)

set(IRONCLAD_PEANO_DIR "$ENV{PEANO_INSTALL_DIR}" CACHE PATH "Peano install dir")
if (NOT IRONCLAD_PEANO_DIR)
    execute_process(
        COMMAND ${Python3_EXECUTABLE} -c "import aie.utils.config; print(aie.utils.config.peano_install_dir());"
        OUTPUT_VARIABLE IRONCLAD_PEANO_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
endif()
if(NOT IRONCLAD_PEANO_DIR)
    message(FATAL_ERROR "Could not find Peano install dir. Please set the environment variable PEANO_INSTALL_DIR or install the llvm-aie wheel.")
endif()

set(IRONCLAD_MLIR_AIE_DIR "$ENV{MLIR_AIE_INSTALL_DIR}" CACHE PATH "MLIR AIE install dir")
if (NOT IRONCLAD_MLIR_AIE_DIR)
    execute_process(
        COMMAND ${Python3_EXECUTABLE} -c "import aie.utils.config; print(aie.utils.config.root_path());"
        OUTPUT_VARIABLE IRONCLAD_MLIR_AIE_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
endif()
if(NOT IRONCLAD_MLIR_AIE_DIR)
    message(FATAL_ERROR "Could not find Peano install dir. Please set the environment variable MLIR_AIE_INSTALL_DIR or install the mlir-aie wheel.")
endif()

# Set your original cache variables to these resolved paths
set(IRONCLAD_MLIR_AIE_RUNTIME_DIR "${IRONCLAD_MLIR_AIE_DIR}/runtime_lib/x86_64/test_lib/" CACHE PATH "Path to built/installed test_lib from MLIR_AIE")

# More Options
option(BUILD_EXAMPLES "Build operators" ON)
option(BUILD_APPLICATIONS "Build example applications" OFF)
option(EXTENSIVE_TESTING "Generate a larger number of operators and tests" OFF)

message(STATUS "IRONCLAD_PEANO_DIR: ${IRONCLAD_PEANO_DIR}")
message(STATUS "IRONCLAD_MLIR_AIE_DIR: ${IRONCLAD_MLIR_AIE_DIR}")
message(STATUS "IRONCLAD_MLIR_AIE_RUNTIME_DIR: ${IRONCLAD_MLIR_AIE_RUNTIME_DIR}")

# CMake modules
list(INSERT CMAKE_MODULE_PATH 0 ${CMAKE_CURRENT_LIST_DIR}/cmake/Modules)
include(AIEConfig)
include(AIECITest)

# Packages
find_package(xrt REQUIRED)

# C++ library
include(${PROJECT_SOURCE_DIR}/cmake/IroncladCompilerOptions.cmake)

add_library(ironclad INTERFACE)
add_library(ironclad::ironclad ALIAS ironclad)

target_include_directories(ironclad SYSTEM INTERFACE
    ${XRT_INCLUDE_DIRS}
    ${MLIR_AIE_INSTALL_DIR}/include
)
target_link_libraries(ironclad INTERFACE XRT::xrt_coreutil)
target_compile_definitions(ironclad INTERFACE KERNELS_BIN_PATH="${KERNELS_BIN_PATH}")
ironclad_compiler_warnings(ironclad)

# Add kernels
add_subdirectory(aie_kernels)

# Add examples
# Pass the architecure to support aie2p
if (BUILD_EXAMPLES)
    add_subdirectory(example)
endif()

# Add example applications
if (BUILD_APPLICATIONS)
    add_subdirectory(applications)
endif()

generate_aie_ci_test_list("ci_tests.py")
