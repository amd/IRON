# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_softmax_design INPUT_LENGTH TILE_SIZE NUM_COLUMNS NUM_CHANNELS TRACE_SIZE)

    set(OPERATOR "softmax_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${INPUT_LENGTH}_tile_${TILE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/softmax/golden_${OPERATOR}")
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)
    
    # Calculate matrix dimensions
    math(EXPR ROWS "${INPUT_LENGTH} / ${TILE_SIZE}")
    
    add_aie_executable(${OPERATOR} 
                       HOST softmax.cpp
                       HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
                       PYTHON softmax.py
                       PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} --tile-size ${TILE_SIZE} -tr ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${OPERATOR}.mlir
                       AIE_CORE_KERNELS "softmax.o"
                       OUTPUT_HOST SOFTMAX_HOST
                       OUTPUT_XCLBIN SOFTMAX_XCLBIN
                       OUTPUT_INSTS SOFTMAX_INSTS)
                       
    add_golden_reference_generator(${OPERATOR} 
        ${CMAKE_CURRENT_SOURCE_DIR}/softmax_golden.py
        ${GOLDEN_VALUES_PATH}
        --rows ${ROWS}
        --cols ${TILE_SIZE}
    )

    add_aie_ci_test(${OPERATOR}
                    RUN 
                        "${SOFTMAX_HOST} -k ${OPERATOR} -x ${SOFTMAX_XCLBIN} -i ${SOFTMAX_INSTS} -l ${INPUT_LENGTH} -r ${ROWS} -c ${TILE_SIZE} --dev ${DEVICE} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS 
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=])
endfunction()

# Helper function to determine optimal columns and channels for a given input length and size
function(get_optimal_columns_channels INPUT_LENGTH SIZE OUT_COLUMNS OUT_CHANNELS)
    # Calculate how many cores we need: input_length / size
    math(EXPR TOTAL_CORES "${INPUT_LENGTH} / ${SIZE}")
    
    if(TOTAL_CORES EQUAL 4)
        # 4 cores: use 2x2 configuration
        set(${OUT_COLUMNS} 2 PARENT_SCOPE)
        set(${OUT_CHANNELS} 2 PARENT_SCOPE)
    elseif(TOTAL_CORES EQUAL 8)
        # 8 cores: use 2x2 configuration (each core handles 2 iterations)
        set(${OUT_COLUMNS} 2 PARENT_SCOPE)
        set(${OUT_CHANNELS} 2 PARENT_SCOPE)
    elseif(TOTAL_CORES EQUAL 2)
        # 2 cores: use 1x2 configuration
        set(${OUT_COLUMNS} 1 PARENT_SCOPE)
        set(${OUT_CHANNELS} 2 PARENT_SCOPE)
    elseif(TOTAL_CORES EQUAL 1)
        # 1 core: use 1x1 configuration
        set(${OUT_COLUMNS} 1 PARENT_SCOPE)
        set(${OUT_CHANNELS} 1 PARENT_SCOPE)
    elseif(TOTAL_CORES EQUAL 16)
        # 16 cores: use 4x4 configuration
        set(${OUT_COLUMNS} 4 PARENT_SCOPE)
        set(${OUT_CHANNELS} 4 PARENT_SCOPE)
    else()
        # Default fallback for other cases
        set(${OUT_COLUMNS} 2 PARENT_SCOPE)
        set(${OUT_CHANNELS} 2 PARENT_SCOPE)
    endif()
endfunction()

set(INPUT_LENGTHS "4096")
set(TILE_SIZES "1024" "512" "2048")
set(WEIGHT_LENGTHS "1024" "512" "2048")
set(TRACE_SIZE "65536")
if(EXTENSIVE_TESTING)
    # TODO: Commented out sizes are broken; fix and re-enable.
    #list(APPEND INPUT_LENGTHS 1024)
    #list(APPEND INPUT_LENGTHS 8192)
endif()

# Generate Softmax designs for each tile size with optimal column/channel configuration
foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
    foreach(TILE_SIZE IN LISTS TILE_SIZES)
        get_optimal_columns_channels(${INPUT_LENGTH} ${TILE_SIZE} OPTIMAL_COLUMNS OPTIMAL_CHANNELS)
        add_aie_softmax_design(${INPUT_LENGTH} ${TILE_SIZE} ${OPTIMAL_COLUMNS} ${OPTIMAL_CHANNELS} ${TRACE_SIZE})
    endforeach()
endforeach()
