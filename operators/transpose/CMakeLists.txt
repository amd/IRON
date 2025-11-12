# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_transpose_design M N NUM_COLUMNS NUM_CHANNELS m n s TRACE_SIZE)
    set(OPERATOR "transpose_${M}_M_${N}_N_${NUM_COLUMNS}_cols_${NUM_CHANNELS}_channels_${m}_m_${n}_n_${s}_s")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/transpose/golden_${OPERATOR}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)

    add_aie_executable(${OPERATOR}
        HOST transpose.cpp
        HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
        PYTHON transpose.py
        PYTHON_FLAGS --dev ${DEVICE} -M ${M} -N ${N} --co ${NUM_COLUMNS} --chan ${NUM_CHANNELS} -m ${m} -n ${n} -s ${s} -tr ${TRACE_SIZE} --output-file-path ${CMAKE_BINARY_DIR}/aie/${OPERATOR}.mlir
        AIE_CORE_KERNELS transpose.o
        OUTPUT_HOST TRANSPOSE_HOST
        OUTPUT_XCLBIN TRANSPOSE_XCLBIN
        OUTPUT_INSTS TRANSPOSE_INSTS
    )

    add_golden_reference_generator(${OPERATOR}
        ${CMAKE_CURRENT_SOURCE_DIR}/transpose_golden.py
        ${GOLDEN_VALUES_PATH}
        --rows ${M}
        --cols ${N}
        --dtype ${OUTPUT_DATA_TYPE_PYTHON}
    )

    add_aie_ci_test(${OPERATOR}
        RUN
            "${TRANSPOSE_HOST} -k ${OPERATOR} -x ${TRANSPOSE_XCLBIN} -i ${TRANSPOSE_INSTS} --rows ${M} --columns ${N} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
        CHECK
            "PASS!"
        METRICS
            "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
            "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
    )
endfunction()

# We have a transpose of K in MHA, which for Llama has dimensions (sequence length, 64) for 8 heads
set(INPUT_LENGTHS "2048")
set(N_LIST "64")
set(TRACE_SIZE "65536")

# Fix the AIE core tile dimensions since the kernel also needs them for compilation
set(m "64")
set(n "64")
set(s_LIST "8")

if(EXTENSIVE_TESTING)
    # Sweep through sequence lengths
    list(APPEND INPUT_LENGTHS 64)
    # list(APPEND INPUT_LENGTHS 128)
    # list(APPEND INPUT_LENGTHS 256)
    # list(APPEND INPUT_LENGTHS 512)
    # list(APPEND INPUT_LENGTHS 1024)
    list(APPEND N_LIST 128)
    list(APPEND N_LIST 256)
    list(APPEND N_LIST 512)
    # list(APPEND s_LIST 4)
endif()

add_aie_kernel(transpose.o SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/generic/transpose.cc DEFINES "DIM_m=${m}" "DIM_n=${n}")

foreach(M IN LISTS INPUT_LENGTHS)
    foreach(N IN LISTS N_LIST)
        foreach(s IN LISTS s_LIST)
            # 1 input, channels can be 1 or 2
            foreach(NUM_COLUMNS RANGE 1 ${MAX_COLUMNS})
                foreach(NUM_CHANNELS RANGE 1 2)
                    # split workload across the column dimension for each NPU column
                    # and across the row dimension for each NPU channel
                    math(EXPR ROW_PART "${M} / ${NUM_CHANNELS}")
                    math(EXPR COL_PART "${N} / ${NUM_COLUMNS}")
                    math(EXPR ROW_DIVISIBLE "${ROW_PART} % ${m}")
                    math(EXPR COL_DIVISIBLE "${COL_PART} % ${n}")
                    if(ROW_DIVISIBLE EQUAL 0 AND COL_DIVISIBLE EQUAL 0)
                        math(EXPR CHECK_LENGTH "${ROW_PART} * ${COL_PART} * ${NUM_CHANNELS} * ${NUM_COLUMNS}")
                        math(EXPR LENGTH "${M} * ${N}")
                        if(CHECK_LENGTH EQUAL LENGTH)
                            add_aie_transpose_design(${M} ${N} ${NUM_COLUMNS} ${NUM_CHANNELS} ${m} ${n} ${s} ${TRACE_SIZE})
                        endif()
                    endif()
                endforeach()
            endforeach()
        endforeach()
    endforeach()
endforeach()