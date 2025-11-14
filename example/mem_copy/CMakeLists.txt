# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_mem_copy_xclbin NUM_CORES NUM_CHANNELS BYPASS TILE_SIZE TRACE_SIZE)
    set(XCLBIN_NAME "mem_copy_${NUM_CORES}_cores_${NUM_CHANNELS}_chans_tile_${TILE_SIZE}_${BYPASS}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # Use a problem size that matches exactly what the NPU is configured for 
    math(EXPR DUMMY_INPUT_LENGTH "${TILE_SIZE} * ${NUM_CORES}")

    add_aie_design(${XCLBIN_NAME}
                   XCLBIN_ONLY
                   PYTHON mem_copy.py
                   PYTHON_FLAGS --dev ${DEVICE} -l ${DUMMY_INPUT_LENGTH} --cores ${NUM_CORES} --channels ${NUM_CHANNELS} --bypass ${BYPASS} --tile-size ${TILE_SIZE} --trace-size ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${XCLBIN_NAME}.mlir
                   AIE_CORE_KERNELS mem_copy.o
                   EXTRA_AIECC_FLAGS --dynamic-objFifos
                   OUTPUT_XCLBIN MEM_COPY_XCLBIN_${XCLBIN_NAME})

    # Make the outputs available to parent scope
    set(MEM_COPY_HOST_${XCLBIN_NAME} ${MEM_COPY_HOST_${XCLBIN_NAME}} PARENT_SCOPE)
    set(MEM_COPY_XCLBIN_${XCLBIN_NAME} ${MEM_COPY_XCLBIN_${XCLBIN_NAME}} PARENT_SCOPE)
endfunction()

function(add_aie_mem_copy_design INPUT_LENGTH NUM_CORES NUM_CHANNELS BYPASS TILE_SIZE TRACE_SIZE)

    set(EXAMPLE "mem_copy_${NUM_CORES}_cores_${NUM_CHANNELS}_chans_${INPUT_LENGTH}_tile_${TILE_SIZE}_${BYPASS}")
    set(XCLBIN_NAME "mem_copy_${NUM_CORES}_cores_${NUM_CHANNELS}_chans_tile_${TILE_SIZE}_${BYPASS}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/example/mem_copy/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    # Generate instructions only (reuse xclbin from add_aie_mem_copy_xclbin)
    add_aie_host(${EXAMPLE}
                 HOST mem_copy.cpp
                 HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
                 OUTPUT_HOST MEM_COPY_HOST)
    add_aie_design(${EXAMPLE}
                   INSTS_ONLY
                   PYTHON mem_copy.py
                   PYTHON_FLAGS --dev ${DEVICE} -l ${INPUT_LENGTH} --cores ${NUM_CORES} --channels ${NUM_CHANNELS} --bypass ${BYPASS} --tile-size ${TILE_SIZE} --trace-size ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
                   EXTRA_AIECC_FLAGS --dynamic-objFifos
                   OUTPUT_INSTS MEM_COPY_INSTS)

    add_dependencies(${EXAMPLE} ${XCLBIN_NAME}_xclbin)
    add_dependencies(${EXAMPLE} ${EXAMPLE}_insts)

    set(MEM_COPY_XCLBIN ${MEM_COPY_XCLBIN_${XCLBIN_NAME}})

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/mem_copy_golden.py
        ${GOLDEN_VALUES_PATH}
        --input_length ${INPUT_LENGTH}
        --dtype ${INPUT_DATA_TYPE_PYTHON}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${MEM_COPY_HOST} -k ${XCLBIN_NAME} -x ${MEM_COPY_XCLBIN} -i ${MEM_COPY_INSTS} -l ${INPUT_LENGTH} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

set(INPUT_LENGTHS "2048")
set(TRACE_SIZE "65536")
set(BYPASS False)
set(TEST_PADDING False)
if(EXTENSIVE_TESTING)
    list(APPEND INPUT_LENGTHS 1024)
    list(APPEND INPUT_LENGTHS 4096)
    list(APPEND INPUT_LENGTHS 8192)
    list(APPEND BYPASS True)
endif()

# Calculate the maximum cores that can be utilized for design without using memtile distribute and join operations,
# which is the product of maximum columns and maximum shim channels
math(EXPR MAX_CORES "${MAX_COLUMNS} * 2")

foreach(INPUT_LENGTH IN LISTS INPUT_LENGTHS)
    foreach(NUM_CORES RANGE 1 ${MAX_CORES})        
        # 1 input, channels can be 1 or 2
        foreach(NUM_CHANNELS RANGE 1 2)
            foreach(BYPASS_MODE IN LISTS BYPASS)
                # Calculate the maximum cores the can be utilized with 1 or 2 shim channels
                math(EXPR MAX_CORES "${MAX_COLUMNS} * ${NUM_CHANNELS}")
                if (MAX_CORES GREATER_EQUAL NUM_CORES AND NUM_CORES GREATER_EQUAL NUM_CHANNELS)
                    math(EXPR TILE_SIZE "${INPUT_LENGTH} / ${NUM_CORES}")
                    # Cap tile_size at 8192 if it's greater
                    if(TILE_SIZE GREATER 8192)
                        set(TILE_SIZE 8192)
                    endif()
                    # Only proceed if TILE_SIZE * NUM_CORES == INPUT_LENGTH (i.e., division is exact)
                    math(EXPR CHECK_LENGTH "${TILE_SIZE} * ${NUM_CORES}")
                    if(CHECK_LENGTH EQUAL ${INPUT_LENGTH})
                        add_aie_mem_copy_xclbin(${NUM_CORES} ${NUM_CHANNELS} ${BYPASS_MODE} ${TILE_SIZE} ${TRACE_SIZE})
                        add_aie_mem_copy_design(${INPUT_LENGTH} ${NUM_CORES} ${NUM_CHANNELS} ${BYPASS_MODE} ${TILE_SIZE} ${TRACE_SIZE})

                        if (TEST_PADDING)
                            # Add four cases:
                            # -Process a workload sligthly smaller than what the NPU is configured for
                            # -Process a workload much smaller than what the NPU is configured for
                            # -Process a workload slightly larger than what the NPU is configured for
                            # -Process a workload much larger than what the NPU is configured for
                            
                            # Case 1
                            math(EXPR SMALLER_INPUT_LENGTH "${INPUT_LENGTH} - 2")
                            add_aie_mem_copy_design(${SMALLER_INPUT_LENGTH} ${NUM_CORES} ${NUM_CHANNELS} ${BYPASS_MODE} ${TILE_SIZE} ${TRACE_SIZE})

                            # Case 2
                            add_aie_mem_copy_design(2 ${NUM_CORES} ${NUM_CHANNELS} ${BYPASS_MODE} ${TILE_SIZE} ${TRACE_SIZE})
                            
                            # Case 3
                            math(EXPR LARGER_INPUT_LENGTH "${INPUT_LENGTH} + 2")
                            add_aie_mem_copy_design(${LARGER_INPUT_LENGTH} ${NUM_CORES} ${NUM_CHANNELS} ${BYPASS_MODE} ${TILE_SIZE} ${TRACE_SIZE})

                            # Case 4
                            math(EXPR LARGER_INPUT_LENGTH "${INPUT_LENGTH} * 8 - 2")
                            add_aie_mem_copy_design(${LARGER_INPUT_LENGTH} ${NUM_CORES} ${NUM_CHANNELS} ${BYPASS_MODE} ${TILE_SIZE} ${TRACE_SIZE})
                        endif()
                    endif()
                endif()
            endforeach()
        endforeach()
    endforeach()
endforeach()
