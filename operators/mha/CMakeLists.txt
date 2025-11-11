# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


# Configuration variables
set(num_KV_heads 0)

set(number_of_pipeline 1)

set(heads 1)
set(S_q 2048)
set(S_kv 2048)
set(d 64)
set(B_q 64)
set(k 64)
set(B_kv 64)
set(dtype "bf16")

set(verbose 0)
set(trace_size 65536)
set(device_name "npu2")
set(design_name "mha")

set(currentDesignTarget ${design_name})

# Derived variables
set(target_suffix "${heads}_${S_q}_${S_kv}_${d}_${B_q}x${d}x${B_kv}")

set(mm_kernel "mm_${B_q}x${d}x${B_kv}_${dtype}_${dtype}")
set(softmax_kernel "softmax_${B_kv}_${dtype}_${dtype}")
set(mha_kernel "mha_${d}_${B_q}x${d}x${B_kv}_${dtype}")
set(passthrough_kernel "passthrough_${B_q}x${B_kv}_${dtype}")

set(build_dir "${CMAKE_BINARY_DIR}/aie")

if(verbose STREQUAL "1")
    set(verbose_string "--verbose")
else()
    set(verbose_string "")
endif()

# Data type mappings
set(dtype_cpp "std::bfloat16_t")

# Display configuration
message(STATUS "Registering Executable: ${currentDesignTarget}")
message(STATUS "    Heads: ${heads}")
message(STATUS "    Number of KV Heads: ${num_KV_heads}")
message(STATUS "    Sequence Length Q: ${S_q}")
message(STATUS "    Sequence Length KV: ${S_kv}")
message(STATUS "    Embedding Dimension d: ${d}")
message(STATUS "    Tile dimensions: ${B_q}x${d}x${B_kv}")
message(STATUS "    Data type: ${dtype}")
message(STATUS "    Device: ${DEVICE}")
message(STATUS "    Design: ${design_name}")
message(STATUS "    Verbose mode: ${verbose}")

# Path configuration
if (IRONCLAD_AIE_TARGET STREQUAL "aie2")
    set(kernels_dir "${CMAKE_SOURCE_DIR}/aie_kernels/aie2")
elseif (IRONCLAD_AIE_TARGET STREQUAL "aie2p")
    set(kernels_dir "${CMAKE_SOURCE_DIR}/aie_kernels/aie2p")
endif ()
set(kernels_generic_dir "${CMAKE_SOURCE_DIR}/aie_kernels/generic")

# Build artifact paths
set(golden_ref_header "${build_dir}/golden_reference.h")
set(mlir_target "${build_dir}/aie_${target_suffix}.mlir")
set(xclbin_target "${build_dir}/mha.xclbin")
set(insts_target "${build_dir}/mha.bin")

set(kernels_archive "${build_dir}/kernels.a")

### Kernel compilation ###
add_aie_kernel(${mm_kernel} SOURCES ${kernels_dir}/mm.cc DEFINES
    "B_COL_MAJ"
    "${dtype}_${dtype}_ONLY"
    "DIM_M=${B_q}"
    "DIM_K=${d}"
    "DIM_N=${B_kv}"
    "AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16"
    "ROUND_CONV_EVEN"
    OUTPUT_OBJECT MM_OBJ
)

add_aie_kernel(${mm_kernel}_rowmaj SOURCES ${kernels_dir}/mm.cc DEFINES
    "${dtype}_${dtype}_ONLY"
    "DIM_M=${B_q}"
    "DIM_K=${d}"
    "DIM_N=${B_kv}"
    "AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16"
    "ROUND_CONV_EVEN"
    OUTPUT_OBJECT MM_ROWMAJ_OBJ
)

add_aie_kernel(${softmax_kernel} SOURCES ${kernels_dir}/softmax.cc
    OUTPUT_OBJECT SOFTMAX_OBJ
)

add_aie_kernel(${mha_kernel} SOURCES ${kernels_dir}/mha.cc
    OUTPUT_OBJECT MHA_OBJ
)

add_aie_kernel(${passthrough_kernel} SOURCES ${kernels_generic_dir}/passThrough.cc DEFINES
    "BIT_WIDTH=16"
    OUTPUT_OBJECT PASSTHROUGH_OBJ
)

# Rename symbols in row-major object file
add_custom_command(
    OUTPUT ${MM_ROWMAJ_OBJ}_renamed
    COMMAND llvm-objcopy-18 --redefine-sym matmul_bf16_bf16=matmul_bf16_bf16_rowmaj
    --redefine-sym matmul_scalar_bf16_bf16=matmul_scalar_bf16_bf16_rowmaj
    --redefine-sym zero_bf16=zero_bf16_rowmaj
    --redefine-sym zero_scalar_bf16=zero_scalar_bf16_rowmaj
    ${MM_ROWMAJ_OBJ} ${MM_ROWMAJ_OBJ}_renamed
    DEPENDS ${MM_ROWMAJ_OBJ}
    COMMENT "Renaming matmul_bf16_bf16 to matmul_bf16_bf16_rowmaj"
    )

set(KERNEL_OBJ_LIST
    ${MM_OBJ}
    ${MM_ROWMAJ_OBJ}_renamed
    ${SOFTMAX_OBJ}
    ${MHA_OBJ}
    ${PASSTHROUGH_OBJ}
)

add_custom_command(
        OUTPUT ${kernels_archive}
        COMMAND ar rvs ${kernels_archive} ${KERNEL_OBJ_LIST} > /dev/null
        DEPENDS ${KERNEL_OBJ_LIST}
        COMMENT "Creating kernels archive"
)

add_custom_target("kernels.a" DEPENDS ${kernels_archive})

add_aie_executable(${currentDesignTarget}
    HOST test.cpp
    PYTHON mha.py
    PYTHON_FLAGS
        --heads ${heads}
        --S_q ${S_q} --S_kv ${S_kv} -d ${d}
        --B_q ${B_q} --B_kv ${B_kv}
        --number-of-pipeline ${number_of_pipeline}
        --num_KV_heads ${num_KV_heads}
        --trace_size 0 ${verbose_string}
        --output-file-path ${build_dir}/${currentDesignTarget}.mlir
    AIE_CORE_KERNELS "kernels.a"
    EXTRA_AIECC_FLAGS --dynamic-objFifos --profile
    OUTPUT_HOST MHA_HOST
    OUTPUT_XCLBIN MHA_XCLBIN
    OUTPUT_INSTS MHA_INSTS
)

set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/operators/mha/golden_mha")

add_golden_reference_generator(${currentDesignTarget}
    ${CMAKE_CURRENT_SOURCE_DIR}/mha_golden.py
    ${GOLDEN_VALUES_PATH}
    --heads ${heads} --S_q ${S_q} --S_kv ${S_kv} -d ${d}
    --num_KV_heads ${num_KV_heads}
    --dtype ${dtype}
    ${verbose_string}
)

add_aie_ci_test(${currentDesignTarget}
    RUN
        "${MHA_HOST} -x ${MHA_XCLBIN} -i ${MHA_INSTS} -k ${currentDesignTarget} --heads ${heads} --S_q ${S_q} --S_kv ${S_kv} -d ${d} -v 2 --warmup 5 --iters 1 --verbosity ${verbose} --ref ${GOLDEN_VALUES_PATH}/golden_reference.bin"
    CHECK
        "PASS!"
    METRICS
        "Latency" [=[Avg NPU matmul time: (?P<metric>\d+)us]=]
        "Bandwidth" [=[Avg Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
        "GFLOP/s" [=[Avg NPU gflops: (?P<metric>[\d\.e\+-]+)]=]
)


add_custom_target(mha_reconfig
    COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/mha.py
            --heads ${heads}
            --S_q ${S_q} --S_kv ${S_kv} -d ${d}
            --B_q ${B_q} --B_kv ${B_kv}
            --number-of-pipeline ${number_of_pipeline}
            --num_KV_heads ${num_KV_heads}
            --trace_size 0 ${verbose_string}
            --output-file-path ${build_dir}/mha_fast.mlir
    COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/mha_golden.py
            --heads ${heads} --S_q ${S_q} --S_kv ${S_kv} -d ${d}
            --num_KV_heads ${num_KV_heads}
            --dtype ${dtype} ${verbose_string}
            --output-bin ${GOLDEN_VALUES_PATH}/golden_reference_fast.bin
    COMMAND aiecc.py --no-compile --aie-generate-npu-insts --dynamic-objFifos --npu-insts-name=${build_dir}/mha_fast.bin ${build_dir}/mha_fast.mlir
    BYPRODUCTS
            ${build_dir}/mha_fast.mlir
            ${build_dir}/mha_fast.bin
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Fast reconfiguration: regenerate insts.bin and golden references only"
)

# Optional: run host with the newly generated instruction sequence and golden references
add_custom_target(mha_reconfig_run
    COMMAND ${CMAKE_BINARY_DIR}/operators/${currentDesignTarget}/${currentDesignTarget}
            -x /scratch/vjung/ironclad/build/aie/${currentDesignTarget}.xclbin
            -i ${build_dir}/mha_fast.bin
            -k ${currentDesignTarget}
            --heads ${heads} --S_q ${S_q} --S_kv ${S_kv} -d ${d}
            --verbosity ${verbose}
            --ref ${GOLDEN_VALUES_PATH}/golden_reference_fast.bin
    DEPENDS mha_reconfig
    COMMENT "Run host with new insts.bin (no xclbin rebuild)"
)
