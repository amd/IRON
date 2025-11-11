# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_leaky_relu_design INPUT_LENGTH NUM_COLUMNS NUM_CHANNELS TILE_SIZE TRACE_SIZE)

    set(EXAMPLE "leaky_relu_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/examples/leaky_relu/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    add_aie_executable(${EXAMPLE}
        HOST leaky_relu.cpp
        HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
        PYTHON leaky_relu.py
        PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} --tile-size ${TILE_SIZE} --trace-size ${TRACE_SIZE} --alpha 0.01 --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
        AIE_CORE_KERNELS "leaky_relu.o"
        OUTPUT_HOST LEAKY_RELU_HOST
        OUTPUT_XCLBIN LEAKY_RELU_XCLBIN
        OUTPUT_INSTS LEAKY_RELU_INSTS)

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/leaky_relu_golden.py
        ${GOLDEN_VALUES_PATH}
        --input_length ${INPUT_LENGTH}
        --alpha 0.01
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${LEAKY_RELU_HOST} -k ${EXAMPLE} -x ${LEAKY_RELU_XCLBIN} -i ${LEAKY_RELU_INSTS} -l ${INPUT_LENGTH} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin --alpha 0.01"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

set(INPUT_LENGTHS "2048")
set(NUM_CHANNELS "1")  # 1 channel for 1 input (like normal RMS norm)
set(TRACE_SIZE "65536")
if(EXTENSIVE_TESTING)
    list(APPEND INPUT_LENGTHS 1024)
    list(APPEND INPUT_LENGTHS 4096)
    list(APPEND INPUT_LENGTHS 8192)
endif()

if(BUILD_LEAKY_RELU)
    foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
        foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
            # Only 1 input, so simple distribution across columns
            math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${NUM_COLUMNS}")
            # Cap tile_size at 4096 if it's greater
            if(TILE_SIZE GREATER 4096)
                set(TILE_SIZE 4096)
            endif()
            # Only proceed if TILE_SIZE * NUM_COLUMNS == INPUT_LENGTH (i.e., division is exact)
            math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${NUM_COLUMNS}")
            if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
                add_aie_leaky_relu_design(${INPUT_LENGTH} ${NUM_COLUMNS} ${NUM_CHANNELS} ${TILE_SIZE} ${TRACE_SIZE})
            endif()
        endforeach()
    endforeach()
endif()

