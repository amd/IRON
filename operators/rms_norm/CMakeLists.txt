# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_rms_norm_design INPUT_LENGTH NUM_COLUMNS NUM_CHANNELS TILE_SIZE TRACE_SIZE)
    set(OPERATOR "rms_norm_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/rms_norm/golden_${OPERATOR}")
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # Calculate matrix dimensions
    math(EXPR ROWS "${INPUT_LENGTH} / ${TILE_SIZE}")

    add_aie_executable(${OPERATOR}
        HOST rms_norm.cpp
        HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
        PYTHON rms_norm.py
        PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} --tile-size ${TILE_SIZE} -tr ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${OPERATOR}.mlir
        AIE_CORE_KERNELS "rms_norm.o"
        OUTPUT_HOST RMS_NORM_HOST
        OUTPUT_XCLBIN RMS_NORM_XCLBIN
        OUTPUT_INSTS RMS_NORM_INSTS
    )

    add_golden_reference_generator(${OPERATOR}
        ${CMAKE_CURRENT_SOURCE_DIR}/rms_norm_golden.py
        ${GOLDEN_VALUES_PATH}
        --rows ${ROWS}
        --cols ${TILE_SIZE}
    )

    add_aie_ci_test(${OPERATOR}
        RUN
            "${RMS_NORM_HOST} -k ${OPERATOR} -x ${RMS_NORM_XCLBIN} -i ${RMS_NORM_INSTS} -l ${INPUT_LENGTH} -r ${ROWS} -c ${TILE_SIZE} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
        CHECK
            "PASS!"
        METRICS
            "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
            "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

function(add_aie_weighted_rms_norm_design INPUT_LENGTH NUM_COLUMNS NUM_CHANNELS TILE_SIZE TRACE_SIZE)
    set(OPERATOR "weighted_rms_norm_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_weights_${TILE_SIZE}")
        set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/rms_norm/golden_${OPERATOR}")

    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)
    add_aie_executable(${OPERATOR}
        HOST weighted_rms_norm.cpp
        HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP} TILE_SIZE=${TILE_SIZE}
        PYTHON weighted_rms_norm.py
        PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} -ts ${TRACE_SIZE} -wl ${TILE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${OPERATOR}.mlir
        AIE_CORE_KERNELS "rms_norm.o"
        OUTPUT_HOST WEIGHTED_RMS_NORM_HOST
        OUTPUT_XCLBIN WEIGHTED_RMS_NORM_XCLBIN
        OUTPUT_INSTS WEIGHTED_RMS_NORM_INSTS
    )

    add_golden_reference_generator(${OPERATOR}
        ${CMAKE_CURRENT_SOURCE_DIR}/weighted_rms_norm_golden.py
        ${GOLDEN_VALUES_PATH}
        --input_length ${INPUT_LENGTH}
        --weight_length ${TILE_SIZE}
    )

    add_aie_ci_test(${OPERATOR}
        RUN
            "${WEIGHTED_RMS_NORM_HOST} -k ${OPERATOR} -x ${WEIGHTED_RMS_NORM_XCLBIN} -i ${WEIGHTED_RMS_NORM_INSTS} -l ${INPUT_LENGTH} -w ${TILE_SIZE} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
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
    # Normal RMS norm: 1 input, channels can be 1 or 2
    foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
        foreach(NUM_CHANNELS_RMS RANGE 1 2)
            # For normal RMS norm: cores = num_columns * num_channels
            math(EXPR TOTAL_CORES "${NUM_COLUMNS} * ${NUM_CHANNELS_RMS}")
            math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${TOTAL_CORES}")
            # Cap tile_size at 8192 if it's greater
            if(TILE_SIZE GREATER 8192)
                set(TILE_SIZE 8192)
            endif()
            # Only proceed if TILE_SIZE * TOTAL_CORES == INPUT_LENGTH (i.e., division is exact)
            math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${TOTAL_CORES}")
            if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
                add_aie_rms_norm_design(${INPUT_LENGTH} ${NUM_COLUMNS} ${NUM_CHANNELS_RMS} ${TILE_SIZE} ${TRACE_SIZE})
            endif()
        endforeach()
    endforeach()

    # Weighted RMS norm: 2 inputs, channels = 2 (fixed)
    foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
        # channels = 2 (fixed for weighted RMS norm)
        math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${NUM_COLUMNS}")
        # Cap tile_size at 4096 if it's greater
        if(TILE_SIZE GREATER 4096)
            set(TILE_SIZE 4096)
        endif()
        # Only proceed if TILE_SIZE * NUM_COLUMNS == INPUT_LENGTH (i.e., division is exact)
        math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${NUM_COLUMNS}")
        if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
            add_aie_weighted_rms_norm_design(${INPUT_LENGTH} ${NUM_COLUMNS} ${NUM_CHANNELS} ${TILE_SIZE} ${TRACE_SIZE})
        endif()
    endforeach()
endforeach()
