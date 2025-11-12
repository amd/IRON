# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_dequant_design INPUT_LENGTH NUM_COLUMNS NUM_CHANNELS TILE_SIZE GROUP_SIZE TRACE_SIZE)

    set(OPERATOR "dequant_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/dequant/golden_${OPERATOR}")
    set(INPUT_DATA_TYPE_PYTHON ui8)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP uint8_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # Calculate matrix dimensions
    math(EXPR OUT_SIZE "${INPUT_LENGTH} * 2")

    add_aie_executable(${OPERATOR}
        HOST dequant.cpp
        HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
        PYTHON dequant.py
        PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} --tile-size ${TILE_SIZE} --group_size ${GROUP_SIZE} -tr ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${OPERATOR}.mlir
        AIE_CORE_KERNELS "expand_aie2_${TILE_SIZE}.o"
        OUTPUT_HOST DEQUANT_HOST
        OUTPUT_XCLBIN DEQUANT_XCLBIN
        OUTPUT_INSTS DEQUANT_INSTS)

    add_golden_reference_generator(${OPERATOR}
        ${CMAKE_CURRENT_SOURCE_DIR}/dequant_golden.py
        ${GOLDEN_VALUES_PATH}
        --input_length ${INPUT_LENGTH}
        --tile_size ${TILE_SIZE}
        --group_size ${GROUP_SIZE}
        --inp_dtype ${INPUT_DATA_TYPE_PYTHON}
        --out_dtype ${OUTPUT_DATA_TYPE_PYTHON}
    )

    add_aie_ci_test(${OPERATOR}
                    RUN
                        "${DEQUANT_HOST} -k ${OPERATOR} -x ${DEQUANT_XCLBIN} -i ${DEQUANT_INSTS} -l ${INPUT_LENGTH} -t ${TILE_SIZE} -b ${GROUP_SIZE} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

set(INPUT_LENGTHS "2048")
set(TRACE_SIZE "0")
if(EXTENSIVE_TESTING)
    list(APPEND INPUT_LENGTHS 1024)
    list(APPEND INPUT_LENGTHS 4096)
    list(APPEND INPUT_LENGTHS 8192)
endif()

set(GROUP_SIZE "32")
foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
    # 1 input, channels can be 1 or 2
    foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
        foreach(NUM_CHANNELS_RMS RANGE 1 2)
            # cores = num_columns * num_channels
            math(EXPR TOTAL_CORES "${NUM_COLUMNS} * ${NUM_CHANNELS_RMS}")
            math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${TOTAL_CORES}")
            # Cap tile_size at 16384 if it's greater
            if(TILE_SIZE GREATER 16384)
                set(TILE_SIZE 16384)
            endif()
            # Only proceed if TILE_SIZE * TOTAL_CORES == INPUT_LENGTH (i.e., division is exact)
            math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${TOTAL_CORES}")
            if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
                if(NOT TARGET "expand_aie2_${TILE_SIZE}.o")
                    add_aie_kernel("expand_aie2_${TILE_SIZE}.o" SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/generic/expand.cc DEFINES "GROUP_SIZE=${GROUP_SIZE}" "TILE_SIZE=${TILE_SIZE}")
                endif()
                add_aie_dequant_design(${INPUT_LENGTH} ${NUM_COLUMNS} ${NUM_CHANNELS_RMS} ${TILE_SIZE} ${GROUP_SIZE} ${TRACE_SIZE})
            endif()
        endforeach()
    endforeach()
endforeach()
