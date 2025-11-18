# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

include_guard()

include(${PROJECT_SOURCE_DIR}/cmake/IroncladCompilerOptions.cmake)

set(WARNING_FLAGS -Wno-parentheses -Wno-attributes -Wno-macro-redefined -Wno-empty-body -Wno-missing-template-arg-list-after-template-kw)
set(PEANOWRAP2_FLAGS -O2 -std=c++20 --target=${IRONCLAD_AIE_TARGET}-none-unknown-elf ${WARNING_FLAGS})

# Add an AIE executable target, which consists of a host CPU executable and an AIE design
#
# To generate only the design or only the host code, use below functions
# add_aie_design and add_aie_host.
#
# This function generates an executable target from the provided source code,
# compiles it with peano, and links it to the final xclbin file.
#
# Args:
#     TARGET_NAME (string): The name of the target executable.
#     Other arguments: See add_aie_design and add_aie_host functions below for their specific arguments which will be forwarded.
#
function(add_aie_executable
    TARGET_NAME  # Output target name
)
    set(options)
    set(oneValueArgs HOST PYTHON DEVICE OUTPUT_HOST OUTPUT_XCLBIN OUTPUT_INSTS)
    set(multiValueArgs HOST_FLAGS PYTHON_FLAGS DEVICE_FLAGS AIE_CORE_KERNELS EXTRA_AIECC_FLAGS)

    # Parse the remaining arguments
    cmake_parse_arguments(ADD_AIE_EXECUTABLE "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    # All output goes to AIE subdir
    set(BUILD_DIR ${CMAKE_BINARY_DIR}/aie)

    add_aie_design(${TARGET_NAME}
        PYTHON ${ADD_AIE_EXECUTABLE_PYTHON}
        PYTHON_FLAGS ${ADD_AIE_EXECUTABLE_PYTHON_FLAGS}
        DEVICE ${ADD_AIE_EXECUTABLE_DEVICE}
        DEVICE_FLAGS ${ADD_AIE_EXECUTABLE_DEVICE_FLAGS}
        AIE_CORE_KERNELS ${ADD_AIE_EXECUTABLE_AIE_CORE_KERNELS}
        EXTRA_AIECC_FLAGS ${ADD_AIE_EXECUTABLE_EXTRA_AIECC_FLAGS}
        OUTPUT_XCLBIN XCLBIN_OUTPUT
        OUTPUT_INSTS INSTRUCTIONS_OUTPUT)

    add_aie_host(${TARGET_NAME} HOST ${ADD_AIE_EXECUTABLE_HOST} HOST_FLAGS ${ADD_AIE_EXECUTABLE_HOST_FLAGS} OUTPUT_HOST HOST_OUTPUT)
    add_dependencies(${TARGET_NAME} ${TARGET_NAME}_xclbin)

    if(ADD_AIE_EXECUTABLE_OUTPUT_HOST)
        set(${ADD_AIE_EXECUTABLE_OUTPUT_HOST} ${HOST_OUTPUT} PARENT_SCOPE)
    endif()
    if(ADD_AIE_EXECUTABLE_OUTPUT_XCLBIN)
        set(${ADD_AIE_EXECUTABLE_OUTPUT_XCLBIN} ${XCLBIN_OUTPUT} PARENT_SCOPE)
    endif()
    if(ADD_AIE_EXECUTABLE_OUTPUT_INSTS)
        set(${ADD_AIE_EXECUTABLE_OUTPUT_INSTS} ${INSTRUCTIONS_OUTPUT} PARENT_SCOPE)
    endif()
endfunction()

# Compile a C++ host code to run on the CPU for invoking an AIE design.
# This wraps normal C++ compilation to add the necessary includes and links the necessary libraries for interacting with the NPU.
#
# Args:
#     HOST (string): The source file for the host-side executable.
#     HOST_FLAGS (string; optional): Compiler defines to be passed to the host target
#     OUTPUT_HOST (string; optional): Variable name that this function should write the path of the compiled host binary to upon return.
function(add_aie_host TARGET_NAME)
    set(options)
    set(oneValueArgs HOST OUTPUT_HOST)
    set(multiValueArgs HOST_FLAGS)

    cmake_parse_arguments(ADD_AIE_HOST "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(BUILD_DIR ${CMAKE_BINARY_DIR}/aie)

    message(STATUS "Registering Executable: ${TARGET_NAME}")
    if(ADD_AIE_HOST_HOST)
        message(STATUS "    Host: ${ADD_AIE_HOST_HOST}")
    endif()
    if(ADD_AIE_HOST_HOST_FLAGS)
        message(STATUS "    Host flags: ${ADD_AIE_HOST_HOST_FLAGS}")
    endif()

    add_executable(${TARGET_NAME} ${ADD_AIE_HOST_HOST})

    target_compile_definitions(${TARGET_NAME} PRIVATE ${ADD_AIE_HOST_HOST_FLAGS})
    target_include_directories(${TARGET_NAME} PUBLIC
        ${CMAKE_SOURCE_DIR}/host_lib/include
        ${IRONCLAD_MLIR_AIE_RUNTIME_DIR}/include
    )
    target_link_libraries(${TARGET_NAME} PRIVATE ironclad::ironclad)
    target_link_directories(${TARGET_NAME} PUBLIC ${IRONCLAD_MLIR_AIE_RUNTIME_DIR}/lib)
    target_link_libraries(${TARGET_NAME} PUBLIC test_utils)
    ironclad_compiler_warnings(${TARGET_NAME})
    ironclad_compiler_options(${TARGET_NAME})

    if(ADD_AIE_HOST_OUTPUT_HOST)
        set(${ADD_AIE_HOST_OUTPUT_HOST} $<TARGET_FILE:${TARGET_NAME}> PARENT_SCOPE)
    endif()
endfunction()

# Add an AIE design target, which results in a instruction sequence (ints.bin) and an xclbin.
# This fully describes the program for the AIE, but not the host code invoking it on the CPU.
#
# Args:
#     TARGET_NAME: Target name will be suffixed with `_xclbin` for the xclbin and `_insts` for the instruction sequence.
#     PYTHON (string): The Python script used to generate the MLIR file.
#     PYTHON_FLAGS (string; optional): Arguments to be passed to Python script
#     AIE_CORE_KERNELS (string): The name(s) of kernel(s) from /aie/{aie1,aie2,aie2p} needed by this design.
#     OUTPUT_XCLBIN (string; optional): Variable name that this function should write the path of the compiled static NPU configuration (XCLBin) to upon return.
#     OUTPUT_INSTS (string; optional): Variable name that this function should write the path of the compiled command processor instruction stream (insts.bin) to upon return.
#     EXTRA_AIECC_FLAGS (string; optional): additional flags to pass to aiecc.py
#     INSTS_ONLY: generate only the instruction sequence (runtime part of the design)
#     XCLBIN_ONLY: generate only the xclbin (static part of the design)
function(add_aie_design TARGET_NAME)
    set(options INSTS_ONLY XCLBIN_ONLY)
    set(oneValueArgs PYTHON DEVICE OUTPUT_XCLBIN OUTPUT_INSTS)
    set(multiValueArgs PYTHON_FLAGS DEVICE_FLAGS AIE_CORE_KERNELS EXTRA_AIECC_FLAGS)

    # Parse the remaining arguments
    cmake_parse_arguments(ADD_AIE_DESIGN "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    # All output goes to AIE subdir
    set(BUILD_DIR ${CMAKE_BINARY_DIR}/aie)
    set(XCLBIN_OUTPUT ${BUILD_DIR}/${TARGET_NAME}.xclbin)
    set(INSTRUCTIONS_OUTPUT ${BUILD_DIR}/${TARGET_NAME}.bin)
    set(MLIR_OUTPUT ${BUILD_DIR}/${TARGET_NAME}.mlir)

    # Print the target
    message(STATUS "Registering Executable: ${TARGET_NAME}")
    if(ADD_AIE_DESIGN_PYTHON)
        message(STATUS "    Python: ${ADD_AIE_DESIGN_PYTHON}")
    endif()
    if(ADD_AIE_DESIGN_PYTHON_FLAGS)
        message(STATUS "    Python Flags: ${ADD_AIE_DESIGN_PYTHON_FLAGS}")
    endif()

    # Generate MLIR file using aie2.py
    add_custom_command(
        OUTPUT ${MLIR_OUTPUT}
        COMMAND ${CMAKE_COMMAND} -E make_directory ${BUILD_DIR}
        COMMAND ${CMAKE_COMMAND} -E chdir ${BUILD_DIR}
            python3 ${CMAKE_CURRENT_LIST_DIR}/${ADD_AIE_DESIGN_PYTHON} ${ADD_AIE_DESIGN_PYTHON_FLAGS}
        DEPENDS ${ADD_AIE_DESIGN_PYTHON} ${ADD_AIE_DESIGN_AIE_CORE_KERNELS}
        COMMENT "Generating AIE MLIR file from ${ADD_AIE_DESIGN_PYTHON}"
        VERBATIM
    )
    set(XCLBIN_DEPENDENCIES "${MLIR_OUTPUT}")

    # Compile AIE source using peano
    if(ADD_AIE_DESIGN_AIE_CORE_KERNELS)
        foreach(CORE_KERNEL IN LISTS ADD_AIE_DESIGN_AIE_CORE_KERNELS)
            # The definition of this dependency should be added by a call to add_aie_kernel in the aie_kernels directory.
            if(IS_ABSOLUTE "${CORE_KERNEL}")
                set(_kernel_path "${CORE_KERNEL}")
            else()
                set(_kernel_path "${BUILD_DIR}/${CORE_KERNEL}")
            endif()
            list(APPEND XCLBIN_DEPENDENCIES "${_kernel_path}")
        endforeach()
    endif()    
    
    # Generate the final xclbin file
    # Workaround: currently .elf files with the same name can collide if we run a parallelized build.
    # This should be fixed in MLIR-AIE soon (PR #2544). Until then, we isolate each aiecc.py
    # invocation in its own temporary subdirectory so files of parallel builds cannot overwrite each other.
    set(AIECC_TMP_BUILD_DIR ${BUILD_DIR}/tmp_${TARGET_NAME})
    set(TMP_KERNEL_COPY_CMDS "")
    foreach(kernel IN LISTS ADD_AIE_DESIGN_AIE_CORE_KERNELS)
        if(IS_ABSOLUTE "${kernel}")
            set(_kpath "${kernel}")
        else()
            set(_kpath "${BUILD_DIR}/${kernel}")
        endif()
        list(APPEND TMP_KERNEL_COPY_CMDS COMMAND ${CMAKE_COMMAND} -E copy_if_different "${_kpath}" ${AIECC_TMP_BUILD_DIR}/)
    endforeach()

    set(AIECC_XCLBIN_FLAGS "")
    set(COMMENT "Compiling MLIR to")
    if(NOT ADD_AIE_DESIGN_INSTS_ONLY)
        set(AIECC_XCLBIN_FLAGS "--aie-generate-xclbin" "--xclbin-name=${XCLBIN_OUTPUT}" "--xclbin-kernel-name=${TARGET_NAME}")
        set(COMMENT "${COMMENT} xclbin")
        if(NOT ADD_AIE_DESIGN_XCLBIN_ONLY)
            set(COMMENT "${COMMENT} and")
        endif()
    else()
        set(AIECC_XCLBIN_FLAGS "--no-compile")
    endif()

    if(NOT ADD_AIE_DESIGN_XCLBIN_ONLY)
        set(AIECC_XCLBIN_FLAGS ${AIECC_XCLBIN_FLAGS} "--aie-generate-npu-insts" "--npu-insts-name=${INSTRUCTIONS_OUTPUT}")
        set(COMMENT "${COMMENT} instruction sequence")
    endif()

    add_custom_command(
        OUTPUT ${XCLBIN_OUTPUT} ${INSTRUCTIONS_OUTPUT}
        COMMAND ${CMAKE_COMMAND} -E make_directory ${AIECC_TMP_BUILD_DIR}
        ${TMP_KERNEL_COPY_CMDS}
        COMMAND ${CMAKE_COMMAND} -E chdir ${AIECC_TMP_BUILD_DIR}
            aiecc.py --no-compile-host --no-xchesscc --no-xbridge --peano ${IRONCLAD_PEANO_DIR}
                     ${AIECC_XCLBIN_FLAGS}
                     ${ADD_AIE_DESIGN_EXTRA_AIECC_FLAGS}
                     ${MLIR_OUTPUT}
        DEPENDS ${XCLBIN_DEPENDENCIES}
        COMMENT ${COMMENT}
        VERBATIM
    )

    # Create a custom target for final.xclbin
    add_custom_target(${TARGET_NAME}_xclbin DEPENDS ${XCLBIN_OUTPUT})
    if(ADD_AIE_DESIGN_AIE_CORE_KERNELS)
        set(_kernel_targets "")
        foreach(_k IN LISTS ADD_AIE_DESIGN_AIE_CORE_KERNELS)
            if(TARGET "${_k}")
                list(APPEND _kernel_targets "${_k}")
            else()
                get_filename_component(_kname "${_k}" NAME)
                if(TARGET "${_kname}")
                    list(APPEND _kernel_targets "${_kname}")
                endif()
            endif()
        endforeach()
        if(_kernel_targets)
            add_dependencies(${TARGET_NAME}_xclbin ${_kernel_targets})
        endif()
    endif()
    add_custom_target(${TARGET_NAME}_insts DEPENDS ${INSTRUCTIONS_OUTPUT})

    if(ADD_AIE_DESIGN_OUTPUT_XCLBIN)
        set(${ADD_AIE_DESIGN_OUTPUT_XCLBIN} ${XCLBIN_OUTPUT} PARENT_SCOPE)
    endif()
    if(ADD_AIE_DESIGN_OUTPUT_INSTS)
        set(${ADD_AIE_DESIGN_OUTPUT_INSTS} ${INSTRUCTIONS_OUTPUT} PARENT_SCOPE)
    endif()

endfunction()

# Add an AIE core kernel. The result is an object file that can be linked into
# a whole design. This is code that should run on a single AIE core. We use
# peano (LLVM-AIE) to compile this
#
# Args:
#     TARGET_NAME (string): Name of the target kernel.
#     SOURCES (string): Input C++ source code (may use the AIE API)
#     DEVICE (string; optional): The source file for the device-side executable.
#     DEFINES (string; optional): Compiler defines to be passed to peano
#     OUTPUT_OBJECT (string; optional): Absolute path to the kernel object
function(add_aie_kernel TARGET_NAME)
    set(options)
    set(oneValueArgs SOURCES OUTPUT_OBJECT)
    set(multiValueArgs DEFINES)
    cmake_parse_arguments(ADD_AIE_KERNEL "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(ABS_SOURCES)
    foreach(SRC IN LISTS ADD_AIE_KERNEL_SOURCES)
        cmake_path(ABSOLUTE_PATH SRC BASE_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}" NORMALIZE)
        list(APPEND ABS_SOURCES "${SRC}")
    endforeach()

    set(BUILD_DIR ${CMAKE_BINARY_DIR}/aie)
    SET(AIE_OBJECT ${BUILD_DIR}/${TARGET_NAME})
    set(DEVICE_DEFINES "")
    foreach(device_flag ${ADD_AIE_KERNEL_DEFINES})
        list(APPEND DEVICE_DEFINES "-D${device_flag}")
    endforeach()
    if(ADD_AIE_KERNEL_DEFINES)
        message(STATUS "Kernel Flags: ${DEVICE_DEFINES}")
    endif()
    add_custom_command(
        OUTPUT ${AIE_OBJECT}
        COMMAND ${CMAKE_COMMAND} -E make_directory ${BUILD_DIR}
        COMMAND ${CMAKE_COMMAND} -E chdir ${BUILD_DIR}
                ${IRONCLAD_PEANO_DIR}/bin/clang++ ${PEANOWRAP2_FLAGS} ${DEVICE_DEFINES}
                                        -I ${IRONCLAD_MLIR_AIE_DIR}/include
                                        -c ${ABS_SOURCES}
                                        -o ${AIE_OBJECT}
        DEPENDS ${ADD_AIE_KERNEL_SOURCES}
        COMMENT "Compiling target ${TARGET_NAME} using ${ADD_AIE_KERNEL_SOURCES} with LLVM-AIE (peano)"
        VERBATIM
    )
    add_custom_target(${TARGET_NAME} DEPENDS ${AIE_OBJECT})

    if(ADD_AIE_KERNEL_OUTPUT_OBJECT)
        set(${ADD_AIE_KERNEL_OUTPUT_OBJECT} ${AIE_OBJECT} PARENT_SCOPE)
    endif()
endfunction()

# Add an AIE core kernel archive. The result is an object file that can be linked into
# a whole design. This is code that should run on a single AIE core.
#
# Args:
#     TARGET_NAME (string): Name of the target kernel.
#     OBJECT_FILES (string): Input object files.
#     OUTPUT_OBJECT (string; optional): Absolute path to the kernel object
function(add_aie_archive TARGET_NAME)
    set(options)
    set(oneValueArgs OUTPUT_OBJECT)
    set(multiValueArgs OBJECT_FILES)
    cmake_parse_arguments(ADD_AIE_ARCHIVE "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(BUILD_DIR ${CMAKE_BINARY_DIR}/aie)
    set(ABS_OBJECT_FILES)
    foreach(SRC IN LISTS ADD_AIE_ARCHIVE_OBJECT_FILES)
        cmake_path(ABSOLUTE_PATH SRC BASE_DIRECTORY "${BUILD_DIR}" NORMALIZE)
        list(APPEND ABS_OBJECT_FILES "${SRC}")
    endforeach()

    set(AIE_OBJECT ${BUILD_DIR}/${TARGET_NAME})

    add_custom_command(
        OUTPUT ${AIE_OBJECT}
        COMMAND ${CMAKE_COMMAND} -E make_directory ${BUILD_DIR}
        COMMAND ${CMAKE_COMMAND} -E chdir ${BUILD_DIR}
                ${CMAKE_AR} rs ${AIE_OBJECT} ${ABS_OBJECT_FILES}
        DEPENDS ${ADD_AIE_ARCHIVE_OBJECT_FILES}
        COMMENT "Creating target ${TARGET_NAME} using ${ADD_AIE_ARCHIVE_OBJECT_FILES}"
        VERBATIM
    )
    add_custom_target(${TARGET_NAME} DEPENDS ${AIE_OBJECT})

    if(ADD_AIE_ARCHIVE_OUTPUT_OBJECT)
        set(${ADD_AIE_ARCHIVE_OUTPUT_OBJECT} ${AIE_OBJECT} PARENT_SCOPE)
    endif()
endfunction()
