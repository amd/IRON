# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_gemm_xclbin m k n NUM_COLUMNS B_COL_MAJ C_COL_MAJ TRACE_SIZE ARCHIVE_NAME)
    set(XCLBIN_NAME "gemm_${m}x${k}x${n}_${NUM_COLUMNS}_cols_${B_COL_MAJ}_bcolmaj_${C_COL_MAJ}_ccolmaj_${TRACE_SIZE}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # We use a dummy problem size since xclbin doesn't depend on it
    math(EXPR DUMMY_M "${m} * 8")
    math(EXPR DUMMY_K "${k} * 8")
    math(EXPR DUMMY_N "${n} * 8")

    add_aie_design(${XCLBIN_NAME}
                   XCLBIN_ONLY
                   PYTHON gemm.py
                   PYTHON_FLAGS --dev ${DEVICE} -M ${DUMMY_M} -K ${DUMMY_K} -N ${DUMMY_N} -m ${m} -k ${k} -n ${n} --n-aie-cols ${NUM_COLUMNS} --b-col-maj ${B_COL_MAJ} --c-col-maj ${C_COL_MAJ} --dtype_in ${INPUT_DATA_TYPE_PYTHON} --dtype_out ${OUTPUT_DATA_TYPE_PYTHON} --trace_size ${TRACE_SIZE} ${EMULATE_STR} ${PRIO_ACC_STR} --archive ${ARCHIVE_NAME} --output-file-path ${CMAKE_BINARY_DIR}/aie/${XCLBIN_NAME}.mlir
                   AIE_CORE_KERNELS ${ARCHIVE_NAME}
                   EXTRA_AIECC_FLAGS --dynamic-objFifos
                   OUTPUT_XCLBIN GEMM_XCLBIN_${XCLBIN_NAME})

    # Make the outputs available to parent scope
    set(GEMM_HOST_${XCLBIN_NAME} ${GEMM_HOST_${XCLBIN_NAME}} PARENT_SCOPE)
    set(GEMM_XCLBIN_${XCLBIN_NAME} ${GEMM_XCLBIN_${XCLBIN_NAME}} PARENT_SCOPE)
endfunction()

function(add_aie_gemm_design M K N m k n NUM_COLUMNS B_COL_MAJ C_COL_MAJ TRACE_SIZE ARCHIVE_NAME)
    set(EXAMPLE "gemm_${M}x${K}x${N}_${m}x${k}x${n}_${NUM_COLUMNS}_cols_${B_COL_MAJ}_bcolmaj_${C_COL_MAJ}_ccolmaj_${TRACE_SIZE}")
    set(XCLBIN_NAME "gemm_${m}x${k}x${n}_${NUM_COLUMNS}_cols_${B_COL_MAJ}_bcolmaj_${C_COL_MAJ}_ccolmaj_${TRACE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/example/gemm/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # Generate instructions only (reuse xclbin from add_aie_gemm_xclbin)
    add_aie_host(${EXAMPLE}
                 HOST gemm.cpp
                 HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
                 OUTPUT_HOST GEMM_HOST)
    add_aie_design(${EXAMPLE}
                   INSTS_ONLY
                   PYTHON gemm.py
                   PYTHON_FLAGS --dev ${DEVICE} -M ${M} -K ${K} -N ${N} -m ${m} -k ${k} -n ${n} --n-aie-cols ${NUM_COLUMNS} --b-col-maj ${B_COL_MAJ} --c-col-maj ${C_COL_MAJ} --dtype_in ${INPUT_DATA_TYPE_PYTHON} --dtype_out ${OUTPUT_DATA_TYPE_PYTHON} --trace_size ${TRACE_SIZE} ${EMULATE_STR} ${PRIO_ACC_STR} --archive ${ARCHIVE_NAME} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
                   EXTRA_AIECC_FLAGS --dynamic-objFifos
                   OUTPUT_INSTS GEMM_INSTS)

    add_dependencies(${EXAMPLE} ${XCLBIN_NAME}_xclbin)
    add_dependencies(${EXAMPLE} ${EXAMPLE}_insts)

    set(GEMM_XCLBIN ${GEMM_XCLBIN_${XCLBIN_NAME}})

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/gemm_golden.py
        ${GOLDEN_VALUES_PATH}
        -M ${M}
        -K ${K}
        -N ${N}
        -b-col-maj ${B_COL_MAJ}
        -c-col-maj ${C_COL_MAJ}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${GEMM_HOST} -k ${XCLBIN_NAME} -x ${GEMM_XCLBIN} -i ${GEMM_INSTS} --rows ${M} --inner ${K} --columns ${N} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
                        "GFLOP/s" [=[Throughput:\s*(?P<metric>[\d\.e\+-]+) GFLOP/s]=])
endfunction()

set(M_LIST "2048")
set(K_LIST "2048")
set(N_LIST "2048")

# Fix the AIE core tile dimensions
# TODO: Do we need to sweep through a list of them instead?
set(m "64")
set(k "64")
set(n "32")

set(AIE_BUILD_DIR ${CMAKE_BINARY_DIR}/aie)

set(PRIO_ACCURACY True)
set(EMULATE_BFLOAT16_MMUL_WITH_BFP16 False)

# Common kernel defines setup
set(MM_KERNEL_DEFINES_BASE "DIM_M=${m}" "DIM_K=${k}" "DIM_N=${n}" "ROUND_CONV_EVEN")
if (EMULATE_BFLOAT16_MMUL_WITH_BFP16)
    set(EMULATE_STR --emulate-bf16-mmul-with-bfp16)
    list(APPEND MM_KERNEL_DEFINES_BASE "AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16")
endif()
if (PRIO_ACCURACY)
    set(PRIO_ACC_STR --prio-accuracy)
    list(APPEND MM_KERNEL_DEFINES_BASE "bf16_f32_ONLY")
else()
    list(APPEND MM_KERNEL_DEFINES_BASE "bf16_bf16_ONLY")
endif()

function(add_gemm_archive m k n B_COL_MAJ C_COL_MAJ CONVERT_OBJ)
    # Set up kernel defines based on configuration
    set(MM_KERNEL_DEFINES ${MM_KERNEL_DEFINES_BASE})
    if(B_COL_MAJ EQUAL 1)
        list(APPEND MM_KERNEL_DEFINES "B_COL_MAJ")
    endif()
    if(C_COL_MAJ EQUAL 1)
        list(APPEND MM_KERNEL_DEFINES "C_COL_MAJ")
    endif()
    
    # Set archive name and path
    set(ARCHIVE_NAME "gemm_${m}x${k}x${n}_${B_COL_MAJ}_bcolmaj_${C_COL_MAJ}_ccolmaj_archive.a")
    set(ARCHIVE_PATH "${AIE_BUILD_DIR}/${ARCHIVE_NAME}")
    
    # Create kernel
    add_aie_kernel("gemm_${m}x${k}x${n}_${B_COL_MAJ}_bcolmaj_${C_COL_MAJ}_ccolmaj"
        SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/${IRONCLAD_AIE_TARGET}/mm.cc
        DEFINES ${MM_KERNEL_DEFINES} OUTPUT_OBJECT MM_OBJ)
    
    # Create archive
    add_aie_archive(${ARCHIVE_NAME}
        OBJECT_FILES ${MM_OBJ} ${CONVERT_OBJ}
        OUTPUT_OBJECT ${ARCHIVE_PATH}
    )
    
    # Export archive name to parent scope
    set(ARCHIVE_NAME ${ARCHIVE_NAME} PARENT_SCOPE)
endfunction()

add_aie_kernel("convert_copy" SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/generic/convert_copy.cc OUTPUT_OBJECT CONVERT_OBJ)

set(TRACE_SIZE "0")
if(EXTENSIVE_TESTING)
    list(APPEND K_LIST 8192)
    list(APPEND K_LIST 64)
    list(APPEND N_LIST 8192)
endif()

# Loop through different combinations of B_COL_MAJ and C_COL_MAJ
set(B_COL_MAJ_LIST 0 1 0)
set(C_COL_MAJ_LIST 0 0 1)

list(LENGTH B_COL_MAJ_LIST NUM_CONFIGS)
math(EXPR NUM_CONFIGS_MINUS_1 "${NUM_CONFIGS} - 1")

foreach(CONFIG_IDX RANGE ${NUM_CONFIGS_MINUS_1})
    list(GET B_COL_MAJ_LIST ${CONFIG_IDX} B_COL_MAJ)
    list(GET C_COL_MAJ_LIST ${CONFIG_IDX} C_COL_MAJ)
    
    # Create archive for this configuration
    add_gemm_archive(${m} ${k} ${n} ${B_COL_MAJ} ${C_COL_MAJ} ${CONVERT_OBJ})
    
    add_aie_gemm_xclbin(${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME})
    
    foreach(M IN LISTS M_LIST)
        foreach(K IN LISTS K_LIST)
            foreach(N IN LISTS N_LIST)
                # GEMM of {sequence length}*8192*8192 doesn't occur with the model, so skipping it to save time
                if(N EQUAL 8192 AND K EQUAL 8192)
                    continue()
                endif()
                add_aie_gemm_design(${M} ${K} ${N} ${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME})
            endforeach()
        endforeach()
    endforeach()
endforeach()
