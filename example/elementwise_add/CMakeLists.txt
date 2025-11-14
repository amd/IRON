# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_eltwise_add_design INPUT_LENGTH NUM_COLUMNS NUM_CHANNELS TILE_SIZE TRACE_SIZE)
    set(EXAMPLE "eltwise_add_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/example/eltwise_add/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)
    add_aie_executable(${EXAMPLE}
                           HOST eltwise_add.cpp
                           HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP} TILE_SIZE=${TILE_SIZE}
                           PYTHON eltwise_add.py
                           PYTHON_FLAGS -d ${DEVICE} -l ${INPUT_LENGTH} -co ${NUM_COLUMNS} -ch ${NUM_CHANNELS} -ts ${TILE_SIZE} -t ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
                           AIE_CORE_KERNELS "add.o"
                           OUTPUT_HOST ELTWISE_ADD_HOST
                           OUTPUT_XCLBIN ELTWISE_ADD_XCLBIN
                           OUTPUT_INSTS ELTWISE_ADD_INSTS)

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/eltwise_add_golden.py
        ${GOLDEN_VALUES_PATH}
        --input_length ${INPUT_LENGTH}
        --dtype ${INPUT_DATA_TYPE_PYTHON}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${ELTWISE_ADD_HOST} -k ${EXAMPLE} -x ${ELTWISE_ADD_XCLBIN} -i ${ELTWISE_ADD_INSTS} -l ${INPUT_LENGTH} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

set(INPUT_LENGTHS "2048")
set(NUM_CHANNELS "2")  # 2 channels for 2 inputs
set(TRACE_SIZE "65536")
if(EXTENSIVE_TESTING)
    list(APPEND INPUT_LENGTHS 1024)
    list(APPEND INPUT_LENGTHS 4096)
    list(APPEND INPUT_LENGTHS 8192)
endif()

foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
    foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
        # Calculate tile_size as INPUT_LENGTH / NUM_COLUMNS
        math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${NUM_COLUMNS}")
        # Only proceed if TILE_SIZE * NUM_COLUMNS == INPUT_LENGTH (i.e., division is exact)
        math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${NUM_COLUMNS}")
        if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
            add_aie_eltwise_add_design(${INPUT_LENGTH} ${NUM_COLUMNS} ${NUM_CHANNELS} ${TILE_SIZE} ${TRACE_SIZE})
        endif()
    endforeach()
endforeach()
