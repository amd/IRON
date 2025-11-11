# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_mem_copy_design INPUT_LENGTH NUM_COLUMNS NUM_CHANNELS TILE_SIZE TRACE_SIZE)

    set(EXAMPLE "mem_copy_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/mem_copy/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    add_aie_executable(${EXAMPLE}
        HOST mem_copy.cpp
        HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
        PYTHON mem_copy.py
        PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} --tile-size ${TILE_SIZE} --trace-size ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
        AIE_CORE_KERNELS mem_copy.o
        OUTPUT_HOST MEM_COPY_HOST
        OUTPUT_XCLBIN MEM_COPY_XCLBIN
        OUTPUT_INSTS MEM_COPY_INSTS)

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/mem_copy_golden.py
        ${GOLDEN_VALUES_PATH}
        --input_length ${INPUT_LENGTH}
        --dtype ${INPUT_DATA_TYPE_PYTHON}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${MEM_COPY_HOST} -k ${EXAMPLE} -x ${MEM_COPY_XCLBIN} -i ${MEM_COPY_INSTS} -l ${INPUT_LENGTH} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

set(INPUT_LENGTHS "2048")
set(TRACE_SIZE "65536")
if(EXTENSIVE_TESTING)
    list(APPEND INPUT_LENGTHS 1024)
    list(APPEND INPUT_LENGTHS 4096)
    list(APPEND INPUT_LENGTHS 8192)
endif()

foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
    foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
        # 1 input, channels can be 1 or 2
        foreach(NUM_CHANNELS RANGE 1 2)
            math(EXPR TOTAL_CORES "${NUM_COLUMNS} * ${NUM_CHANNELS}")
            math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${TOTAL_CORES}")
            # Cap tile_size at 8192 if it's greater
            if(TILE_SIZE GREATER 8192)
                set(TILE_SIZE 8192)
            endif()
            # Only proceed if TILE_SIZE * TOTAL_CORES == INPUT_LENGTH (i.e., division is exact)
            math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${TOTAL_CORES}")
            if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
                add_aie_mem_copy_design(${INPUT_LENGTH} ${NUM_COLUMNS} ${NUM_CHANNELS} ${TILE_SIZE} ${TRACE_SIZE})
            endif()
        endforeach()
    endforeach()
endforeach()
