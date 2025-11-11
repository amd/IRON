# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_rope_design INPUT_LENGTH TILE_SIZE NUM_COLUMNS NUM_CHANNELS TRACE_SIZE METHOD_TYPE)

    set(EXAMPLE "rope_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}_${METHOD_TYPE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/rope/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # Calculate matrix dimensions
    math(EXPR ROWS "${INPUT_LENGTH} / ${TILE_SIZE}")

    add_aie_executable(${EXAMPLE}
                       HOST rope.cpp
                       HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
                       PYTHON rope.py
                       PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} --tile-size ${TILE_SIZE} -tr ${TRACE_SIZE} -mt ${METHOD_TYPE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
                       AIE_CORE_KERNELS "rope_${METHOD_TYPE}.o"
                       OUTPUT_HOST ROPE_HOST
                       OUTPUT_XCLBIN ROPE_XCLBIN
                       OUTPUT_INSTS ROPE_INSTS)

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/rope_golden.py
        ${GOLDEN_VALUES_PATH}
        --rows ${ROWS}
        --cols ${TILE_SIZE}
        --method_type ${METHOD_TYPE}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${ROPE_HOST} -k ${EXAMPLE} -x ${ROPE_XCLBIN} -i ${ROPE_INSTS} -l ${INPUT_LENGTH} -r ${ROWS} -c ${TILE_SIZE} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

set(INPUT_LENGTHS "4096")
set(NUM_CHANNELS "2")  # 2 channels for 2 inputs
set(TRACE_SIZE "65536")
set(METHOD_TYPES "0") # 0: Two-halves method, 1: interleaved method
if(EXTENSIVE_TESTING)
    list(APPEND INPUT_LENGTHS 1024)
    list(APPEND INPUT_LENGTHS 8192)
    list(APPEND METHOD_TYPES 1)
endif()

foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
    foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
        # Both inputs (data + frequencies) are distributed per column
        math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${NUM_COLUMNS}")
        # Cap tile_size at 4096 if it's greater
        if(TILE_SIZE GREATER 4096)
            set(TILE_SIZE 4096)
        endif()
        # Only proceed if TILE_SIZE * NUM_COLUMNS == INPUT_LENGTH (i.e., division is exact)
        math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${NUM_COLUMNS}")
        if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
            foreach(METHOD_TYPE IN LISTS METHOD_TYPES)
                add_aie_rope_design(${INPUT_LENGTH} ${TILE_SIZE} ${NUM_COLUMNS} ${NUM_CHANNELS} ${TRACE_SIZE} ${METHOD_TYPE})
            endforeach()
        endif()
    endforeach()
endforeach()
