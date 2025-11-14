# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_matrix_vector_mul_design NUM_COLUMNS M K m)

    set(EXAMPLE "matrix_vector_mul_${M}x${K}_${m}_${NUM_COLUMNS}col")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/example/matrix_vector_mul/golden_${EXAMPLE}")

    add_aie_executable(${EXAMPLE}
                       HOST matrix_vector_mul.cpp
                       PYTHON matrix_vector_mul.py
                       PYTHON_FLAGS --dev ${DEVICE} -M ${M} -K ${K} -m ${m} --cols ${NUM_COLUMNS} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
                       AIE_CORE_KERNELS mv.o
                       OUTPUT_HOST MATRIX_VECTOR_MUL_HOST
                       OUTPUT_XCLBIN MATRIX_VECTOR_MUL_XCLBIN
                       OUTPUT_INSTS MATRIX_VECTOR_MUL_INSTS)

    add_golden_reference_generator(${EXAMPLE}
        ${CMAKE_CURRENT_SOURCE_DIR}/matrix_vector_mul_golden.py
        ${GOLDEN_VALUES_PATH}
        -M ${M}
        -K ${K}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN
                        "${MATRIX_VECTOR_MUL_HOST} -k ${EXAMPLE} -x ${MATRIX_VECTOR_MUL_XCLBIN} -i ${MATRIX_VECTOR_MUL_INSTS} -M ${M} -K ${K} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
                    CHECK
                        "PASS!"
                    METRICS
                        "Latency" [=[Latency:\s*(?P<metric>\d+) us]=]
                        "GFLOP/s" [=[Throughput:\s*(?P<metric>[\d\.e\+-]+) GFLOP/s]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=])
endfunction()

add_aie_matrix_vector_mul_design(1 128 128 32)
add_aie_matrix_vector_mul_design(1 2048 8192 1)
add_aie_matrix_vector_mul_design(1 8192 2048 4)

add_aie_matrix_vector_mul_design(2 2048 8192 1)
add_aie_matrix_vector_mul_design(2 8192 2048 4)

add_aie_matrix_vector_mul_design(4 2048 8192 1)
add_aie_matrix_vector_mul_design(4 8192 2048 4)


if(IRONCLAD_AIE_TARGET STREQUAL aie2p)
    add_aie_matrix_vector_mul_design(8 2048 8192 1)
    add_aie_matrix_vector_mul_design(8 8192 2048 4)
endif()
