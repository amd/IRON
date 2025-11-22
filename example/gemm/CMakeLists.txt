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
set(n "64")

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

add_aie_kernel("convert_copy" SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/generic/convert_copy.cc OUTPUT_OBJECT CONVERT_OBJ)

# Create archive for B_COL_MAJ=0, C_COL_MAJ=0 (both row major)
set(MM_KERNEL_DEFINES ${MM_KERNEL_DEFINES_BASE})
set(ARCHIVE_NAME_0_0 "gemm_${m}x${k}x${n}_0_bcolmaj_0_ccolmaj_archive.a")
set(ARCHIVE_PATH_0_0 "${AIE_BUILD_DIR}/${ARCHIVE_NAME_0_0}")

add_aie_kernel("gemm_${m}x${k}x${n}_0_bcolmaj_0_ccolmaj"
    SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/${IRONCLAD_AIE_TARGET}/mm.cc
    DEFINES ${MM_KERNEL_DEFINES} OUTPUT_OBJECT MM_OBJ_0_0)

add_aie_archive(${ARCHIVE_NAME_0_0}
    OBJECT_FILES ${MM_OBJ_0_0} ${CONVERT_OBJ}
    OUTPUT_OBJECT ${ARCHIVE_PATH_0_0}
)

# Create archive for B_COL_MAJ=1, C_COL_MAJ=0 (B column major)
set(MM_KERNEL_DEFINES ${MM_KERNEL_DEFINES_BASE})
list(APPEND MM_KERNEL_DEFINES "B_COL_MAJ")
set(ARCHIVE_NAME_1_0 "gemm_${m}x${k}x${n}_1_bcolmaj_0_ccolmaj_archive.a")
set(ARCHIVE_PATH_1_0 "${AIE_BUILD_DIR}/${ARCHIVE_NAME_1_0}")

add_aie_kernel("gemm_${m}x${k}x${n}_1_bcolmaj_0_ccolmaj"
    SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/${IRONCLAD_AIE_TARGET}/mm.cc
    DEFINES ${MM_KERNEL_DEFINES} OUTPUT_OBJECT MM_OBJ_1_0)

add_aie_archive(${ARCHIVE_NAME_1_0}
    OBJECT_FILES ${MM_OBJ_1_0} ${CONVERT_OBJ}
    OUTPUT_OBJECT ${ARCHIVE_PATH_1_0}
)

# Create archive for B_COL_MAJ=0, C_COL_MAJ=1 (C column major)
set(MM_KERNEL_DEFINES ${MM_KERNEL_DEFINES_BASE})
list(APPEND MM_KERNEL_DEFINES "C_COL_MAJ")
set(ARCHIVE_NAME_0_1 "gemm_${m}x${k}x${n}_0_bcolmaj_1_ccolmaj_archive.a")
set(ARCHIVE_PATH_0_1 "${AIE_BUILD_DIR}/${ARCHIVE_NAME_0_1}")

add_aie_kernel("gemm_${m}x${k}x${n}_0_bcolmaj_1_ccolmaj"
    SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/${IRONCLAD_AIE_TARGET}/mm.cc
    DEFINES ${MM_KERNEL_DEFINES} OUTPUT_OBJECT MM_OBJ_0_1)

add_aie_archive(${ARCHIVE_NAME_0_1}
    OBJECT_FILES ${MM_OBJ_0_1} ${CONVERT_OBJ}
    OUTPUT_OBJECT ${ARCHIVE_PATH_0_1}
)

set(TRACE_SIZE "0")
if(EXTENSIVE_TESTING)
    list(APPEND K_LIST 8192)
    list(APPEND K_LIST 64)
    list(APPEND N_LIST 8192)
endif()

# Test with B and C both row major
set(B_COL_MAJ 0)
set(C_COL_MAJ 0)
add_aie_gemm_xclbin(${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME_0_0})

foreach(M IN LISTS M_LIST)
    foreach(K IN LISTS K_LIST)
        foreach(N IN LISTS N_LIST)
            # GEMM of {sequence length}*8192*8192 doesn't occur with the model, so skipping it to save time
            if(N EQUAL 8192 AND K EQUAL 8192)
                continue()
            endif()
            add_aie_gemm_design(${M} ${K} ${N} ${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME_0_0})
        endforeach()
    endforeach()
endforeach()

# Test with B column major
set(B_COL_MAJ 1)
set(C_COL_MAJ 0)
add_aie_gemm_xclbin(${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME_1_0})

foreach(M IN LISTS M_LIST)
    foreach(K IN LISTS K_LIST)
        foreach(N IN LISTS N_LIST)
            # GEMM of {sequence length}*8192*8192 doesn't occur with the model, so skipping it to save time
            if(N EQUAL 8192 AND K EQUAL 8192)
                continue()
            endif()
            add_aie_gemm_design(${M} ${K} ${N} ${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME_1_0})
        endforeach()
    endforeach()
endforeach()

# Test with C column major
set(B_COL_MAJ 0)
set(C_COL_MAJ 1)
add_aie_gemm_xclbin(${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME_0_1})

foreach(M IN LISTS M_LIST)
    foreach(K IN LISTS K_LIST)
        foreach(N IN LISTS N_LIST)
            # GEMM of {sequence length}*8192*8192 doesn't occur with the model, so skipping it to save time
            if(N EQUAL 8192 AND K EQUAL 8192)
                continue()
            endif()
            add_aie_gemm_design(${M} ${K} ${N} ${m} ${k} ${n} ${MAX_COLUMNS} ${B_COL_MAJ} ${C_COL_MAJ} ${TRACE_SIZE} ${ARCHIVE_NAME_0_1})
        endforeach()
    endforeach()
endforeach()
